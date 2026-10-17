```markdown
# C13_v1 FPGA FIXED-POINT CONSTRAINTS & CLOCK DOMAIN CROSSING (CDC) SPECIFICATION
**System Hardware Implementation Ledger: Layer 2 Physical Synthesis & Pinout Mapping**  
**Document Reference:** C13-REV1-SYNTHESIS-CONSTRAINTS  
**Target Hardware:** Digilent Cora Z7 (Zynq-7000 XC7Z010-1CLG400C) / AMD-Xilinx Kria KV260 (Zynq UltraScale+ xck26-sfvc784-2LV-c)  
**Toolchain Support:** Vivado Design Suite 2023.2+ (Target Language: SystemVerilog-2017 / XDC)  
**Safety Classification:** Hardware Root of Trust / Fail-Safe Deterministic Shunt  

---

## 1. INTRODUZIONE E SCOPO DEL MODULO

Il presente modulo formalizza i vincoli di sintesi fisica (XDC), la mappatura dei pin e le barriere di Clock Domain Crossing (CDC) per l'implementazione del **Doppio Watchdog Asincrono (`C12_v4`)** e della **Pipeline CBF in virgola fissa Q8.16 (`C11_v3`)**. 

L'obiettivo è prevenire fenomeni di metastabilità durante il transito dei campioni tra il dominio di campionamento dell'ADC ($f_s = 20\,\text{kHz}$, asincrono) e il dominio di clock principale di elaborazione FPGA ($f_{\text{clk}} = 100\,\text{MHz}$), garantendo che l'albero di interruzione a ridondanza modulare tripla (TMR Muller C-Element) rispetti il contratto di scatto deterministico in **$\le 3$ cicli di clock (30 ns)**.

---

## 2. ISOLAMENTO DEI DOMINI DI CLOCK (CDC) E PREVENZIONE DELLA METASTABILITÀ

Il sistema opera su tre domini di clock fisicamente disaccoppiati:
1.  **`clk_main` (100.000 MHz):** Clock principale sincrono per la pipeline Q8.16 CBF, il contatore di timeout fluidico (PFM) e la FSM di controllo.
2.  **`clk_adc_async` (20.000 kHz nominali / Bus SPI a 25.0 MHz):** Dominio di campionamento e trasduzione dei 64 canali della matrice passiva.
3.  **`pump_tach_pulse` (Asincrono, 0.5–50 Hz):** Treno d'impulsi digitale generato dal sensore Hall/ottico della pompa peristaltica.

```
+-----------------------------------------------------------------------------------------+
|                               CLOCK DOMAIN ARCHITECTURE                                 |
|                                                                                         |
|   [clk_adc_async] (20 kHz)           [pump_tach_pulse] (Asincrono)                      |
|          │                                      │                                       |
|          ▼                                      ▼                                       |
|   +──────────────+                       +──────────────+                               |
|   | Dual-Clock   |                       | 3-Stage      |                               |
|   | Gray-FIFO    |                       | Synchronizer | (MTBF > 10^9 ore)             |
|   +──────┬───────+                       +──────┬───────+                               |
|          │                                      │                                       |
|          └──────────────────┬───────────────────┘                                       |
|                             ▼                                                           |
|             [clk_main] DOMAIN (100.000 MHz)                                             |
|             ├── Fixed-Point Q8.16 Log-CBF Pipeline                                      |
|             ├── 24-bit Fluidic PFM Counter (15.000.000 cicli = 150 ms timeout)          |
|             └── TMR Majority Voter & Muller C-Elements (Trip <= 3 cicli = 30 ns)        |
+-----------------------------------------------------------------------------------------+
```

### 2.1 Sincronizzatore a 3 Stadi per Segnali Monobit (Linea 2 - Fluidica)
Gli impulsi della pompa `pump_tach_pulse` transitano nel dominio `clk_main` attraverso una catena di sincronizzazione a 3 flip-flop cascata con attributi di sintesi `ASYNC_REG = TRUE`.

Il Mean Time Between Failures (MTBF) per il sincronizzatore a 100 MHz su Zynq-7000 è quantificato da:
$$\text{MTBF} = \frac{e^{\frac{t_{\text{resolve}}}{\tau}}}{T_0 \cdot f_{\text{clk}} \cdot f_{\text{data}}} > 1.42 \times 10^{11} \text{ ore}$$
garantendo l'immunità operativa contro l'indeterminazione logica.

### 2.2 FIFO Asincrona Gray-Coded (Linea 1 - Dati Elettrofisiologici)
I pacchetti serializzati dei 64 canali dall'ADC transitano su una FIFO a doppia porta asincrona ( larghezza: 24 bit, profondità: 32 parole) con puntatori codificati in codice Gray. La sincronizzazione del puntatore di scrittura nel dominio di lettura avviene tramite doppi registri con vincolo di skew massimo vincolato da XDC:
$$\tau_{\text{skew}} < T_{\text{clk\_main}} = 10.0\,\text{ns}$$

---

## 3. MAPPATURA DEI PIN FISICI (HARDWARE PINOUT LEDGER)

### 3.1 Target A: Digilent Cora Z7 (Zynq-7000 XC7Z010-1CLG400C)
Utilizza i connettori standard PMOD e lo shield I/O per interfacciare la scheda PCB passiva a 64 canali e il driver GaN/MOSFET.

| Segnale RTL | Descrizione Funzionale | Pin FPGA (Cora Z7) | Standard I/O | Direzione | Note Hardware |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`clk_125m_in`** | Clock oscillatore primario | `H16` | LVCMOS33 | Input | Convertito a 100 MHz via MMCM interno |
| **`rst_n_hard`** | Reset manuale (Pulsante BTN0) | `D20` | LVCMOS33 | Input | Active-Low con pull-up |
| **`adc_spi_sck`** | Clock seriale bus ADC (25 MHz) | `Y18` (PMOD JA-1) | LVCMOS33 | Output | Slew-rate fast |
| **`adc_spi_cs_n`**| Chip Select bus ADC | `Y19` (PMOD JA-2) | LVCMOS33 | Output | Active-Low |
| **`adc_spi_miso`**| Dati seriali multiplexati | `Y16` (PMOD JA-3) | LVCMOS33 | Input | Connesso ad ADC 12-bit (ch 1-64) |
| **`pump_tach_in`**| Treno d'onda PFM pompa | `Y17` (PMOD JA-4) | LVCMOS33 | Input | Opto-isolato da sensore tachimetro |
| **`nmi_trip_out`**| Trigger scatto di sicurezza GaN | `U18` (PMOD JB-1) | LVCMOS33 | Output | Active-High, comanda MOSFET/GaN shunt |
| **`gate_status`** | LED debug stato Gate (LD0 verde) | `L15` | LVCMOS33 | Output | 1 = NESS Safe, 0 = Tripped |

### 3.2 Target B: AMD-Xilinx Kria KV260 (Vision AI Starter Kit)
Mappatura sui connettori Raspberry Pi Header e PMOD per installazioni industriali modulari.

| Segnale RTL | Descrizione Funzionale | Pin SoM (KV260) | Standard I/O | Direzione | Note Hardware |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`clk_100m_in`** | Clock di sistema da carrier board| `C11` | LVCMOS18 | Input | Clock nativo 100 MHz a basso jitter |
| **`rst_n_hard`** | Pulsante reset carrier | `B10` | LVCMOS18 | Input | Pull-up esterno su carrier |
| **`adc_spi_sck`** | Bus SPI Clock (ADC) | `H12` (RPi Pin 23) | LVCMOS33 | Output | Livellato da traslatore a bordo |
| **`adc_spi_cs_n`**| Bus SPI Chip Select | `E10` (RPi Pin 24) | LVCMOS33 | Output | Active-Low |
| **`adc_spi_miso`**| Bus SPI MISO Data Line | `D10` (RPi Pin 21) | LVCMOS33 | Input | Dati campionati 64 canali |
| **`pump_tach_in`**| Telemetria PFM Pompa | `C12` (RPi Pin 16) | LVCMOS33 | Input | Schmitt trigger condizionato |
| **`nmi_trip_out`**| Linea Non-Maskable Shunt GaN | `B11` (PMOD Pin 1) | LVCMOS33 | Output | Pilotaggio rapido $< 200\,\text{ns}$ |
| **`gate_status`** | Segnale telemetrico stato | `A12` (PMOD Pin 2) | LVCMOS33 | Output | Interfaccia verso sistema diagnostico |

---

## 4. VINCOLI FISICI E TEMPORALI XDC (VIVADO MASTER CONSTRAINTS)

Il seguente blocco XDC definisce i requisiti di timing deterministici per il target **Digilent Cora Z7**. Configura i clock, forza il posizionamento dei registri di sincronizzazione e impone l'immutabilità della logica TMR.

```tcl
# ==============================================================================
# MASTER XDC CONSTRAINTS: C13_v1_FPGA_Fixed_Point_Constraints
# Target: Digilent Cora Z7 (XC7Z010-1CLG400C)
# Project: The Custodial Autopoiesis Project
# ==============================================================================

# --- 1. DEFINIZIONE DEI CLOCK PRIMARI E DERIVATI ---
create_clock -period 8.000 -name clk_125m [get_ports clk_125m_in]
create_clock -period 40.000 -name clk_adc_spi [get_ports adc_spi_sck]

# Generazione clock interno a 100 MHz via MMCM (clk_main)
# Period = 10.000 ns (Setup Slack target >= 1.500 ns)

# --- 2. GESTIONE DEI DOMINI ASINCRONI E CLOCK DOMAIN CROSSING (CDC) ---
set_clock_groups -asynchronous \
    -group [get_clocks -include_generated_clocks clk_125m] \
    -group [get_clocks clk_adc_spi]

# Protezione catena di sincronizzazione a 3 stadi (pump_tach_pulse)
set_property ASYNC_REG TRUE [get_cells -hierarchical *tach_sync_reg*]
set_max_delay -from [get_ports pump_tach_in] -to [get_cells -hierarchical *tach_sync_reg[0]*] 10.000 -datapath_only

# Protezione puntatori Gray per FIFO Asincrona ADC
set_property ASYNC_REG TRUE [get_cells -hierarchical *gray_ptr_sync*]
set_max_delay -from [get_cells -hierarchical *wptr_gray_reg*] -to [get_cells -hierarchical *rptr_gray_sync_reg[0]*] 8.000 -datapath_only

# --- 3. CONTRATTO DI TEMPO REALE SULL'ALBERO DI TRIP (TMR / MULLER C-ELEMENT) ---
# Forza la latenza dell'albero logico di trip a un massimo di 3 cicli di clock (30.0 ns)
set_max_delay -from [get_cells -hierarchical *trip_latch_reg*] -to [get_ports nmi_trip_out] 5.000 -datapath_only

# Inibizione dell'ottimizzazione logica ridondante (Preservazione TMR)
set_property DONT_TOUCH TRUE [get_cells -hierarchical *tmr_voter_core*]
set_property DONT_TOUCH TRUE [get_cells -hierarchical *muller_c_gate*]

# --- 4. CONFIGURAZIONE ELETTRICA E PINOUT (Esempio Cora Z7) ---
set_property -dict { PACKAGE_PIN H16 IOSTANDARD LVCMOS33 } [get_ports clk_125m_in]
set_property -dict { PACKAGE_PIN D20 IOSTANDARD LVCMOS33 } [get_ports rst_n_hard]

# Linee ADC SPI (PMOD JA)
set_property -dict { PACKAGE_PIN Y18 IOSTANDARD LVCMOS33 DRIVE 8 SLEW FAST } [get_ports adc_spi_sck]
set_property -dict { PACKAGE_PIN Y19 IOSTANDARD LVCMOS33 DRIVE 8 SLEW FAST } [get_ports adc_spi_cs_n]
set_property -dict { PACKAGE_PIN Y16 IOSTANDARD LVCMOS33 PULLUP TRUE }       [get_ports adc_spi_miso]

# Linea Monitor Pompa (PMOD JA Pin 4)
set_property -dict { PACKAGE_PIN Y17 IOSTANDARD LVCMOS33 }                  [get_ports pump_tach_in]

# Linea Shunt GaN NMI (PMOD JB Pin 1)
set_property -dict { PACKAGE_PIN U18 IOSTANDARD LVCMOS33 DRIVE 16 SLEW FAST } [get_ports nmi_trip_out]

# Status LED
set_property -dict { PACKAGE_PIN L15 IOSTANDARD LVCMOS33 }                  [get_ports gate_status]
```

---

## 5. REGOLE DI VALIDAZIONE TIMING & COMMIT POLICY

1.  **Chiusura del Timing (Timing Closure):**
    Il bitstream sintetizzato non deve presentare violazioni di Setup (WNS $\ge +1.200\,\text{ns}$) né di Hold (WHS $\ge +0.150\,\text{ns}$) nel dominio `clk_main`.
2.  **Verifica CDC (Vivado Report CDC):**
    Il report `report_cdc` deve categorizzare il 100% degli attraversamenti asincroni come **"Safe"**. Qualsiasi flag di stato **"Critical"** o **"Unsafe"** blocca automaticamente la pipeline di continuous deployment.
3.  **Preservazione dell'Albero Ridondante:**
    La direttiva `DONT_TOUCH TRUE` deve essere confermata sul log di implementazione finale (`impl_1`) per prevenire che l'ottimizzatore di Vivado fonda le tre diramazioni parallele TMR in una singola funzione logica (eliminazione del single-point-of-failure).
```