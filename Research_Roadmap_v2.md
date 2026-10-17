# Research_Roadmap_v2: Low-Cost Decentralized Phase 2 Protocol
## Domain: Frugal Bio-Cybernetics & Open-Source Hardware Interfacing

### 1. Rationale dell'Ottimizzazione Economica
Per abbattere il margine di fallimento legato alla mancata collaborazione dei grandi attori industriali, questo modulo estende la `Research_Roadmap.md` originale definendo un'architettura di interfacciamento a basso costo. L'obiettivo è consentire a laboratori indipendenti, hacker-space e bio-hacker accreditati di avviare la Fase 2 (In-Vitro) con un budget inferiore a \$1.500 USD, bypassando le barriere commerciali dei sistemi HD-MEA proprietari.

### 2. Sostituzione Hardware Frugale (Hardware Alternative Matrix)

| Componente Industriale Costoso | Alternativa Open-Source / Low-Cost | Costo Stimato |
| :--- | :--- | :--- |
| HD-MEA CMOS (26.400 ch) | Matrice Passiva Multi-Array (64-128 ch) custom PCB | \$150 |
| FPGA UltraScale+ Dedicated Board | Sviluppo su AMD Xilinx Kria KV260 / Cora Z7 | \$150 - \$250 |
| Sistemi di Perfusione Microfluidica | Pompe peristaltiche open-source stampate in 3D (Arduino) | \$80 |
| Incubatori CO2 Industriali | Incubatore custom con sensori DHT22 e riscaldatori PTC | \$120 |

### 3. Protocollo Elettrofisiologico Scalato (Low-Density Invariant Bridge)
Poiché non si dispone dei 26.400 canali simultanei descritti in `C11_v2`, l'allineamento termodinamico viene mappato su geometrie di campionamento macroscopiche. 
1. **Sotto-campionamento Spettrale:** Invece di monitorare la conduttanza spettrale di ogni singolo nodo, il software esegue la trasformata di Fourier (FFT) sui macro-cluster della matrice a 64 canali.
2. **Adattamento del Delta-Bound (\(\delta_{\text{bound}}\)):** A causa del rumore termico più elevato delle matrici passive rispetto al Pt-black dei sistemi CMOS, la fascia di guardia \(\Omega_{\text{guard}}\) definita in `C7_v2` viene allargata del 25% nel firmware di controllo per evitare falsi positivi di scatto (trip) causati dal rumore di fondo dell'amplificazione commerciale.

### 4. Il Gateway di Interlock Logico su Hardware Accessibile
La logica del Gate Hardware \(\Pi_{\text{safe}}\) viene implementata sfruttando i blocchi logici elementari (LUT) di una FPGA economica (es. Cora Z7). I comparatori hardware operano in parallelo direttamente sulle uscite digitalizzate degli ADC commerciali a 12-bit collegati via bus SPI o I2S.
* **Latenza di Scatto Garantita:** Sebbene non si raggiungano i nanosecondi delle specifiche VU9P, l'architettura garantisce un tempo di interruzione totale (NMI) inferiore a \(12 \mu\text{s}\) tramite l'apertura meccanica o a stato solido di MOSFET di potenza commerciali accoppiati optoelettronicamente alla linea di stimolazione.

### 5. Strategia di Distribuzione di Massa (Forzare la Mano)
Rendendo i file Gerber delle PCB delle matrici e il codice firmware per FPGA economiche interamente pubblici nel repository, il progetto esternalizza il Red-Teaming bio-fisico. I laboratori indipendenti possono validare la stabilità di Lyapunov stocastica (\(\lambda < 0\)) descritta in `simulation5_v10.py` usando colture primarie di roditori o linee cellulari commerciali a basso costo, accumulando i dati forensi necessari sul Bus B passivo.
