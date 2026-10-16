```markdown
# C11_v2 IN-VITRO ELECTROPHYSIOLOGICAL PROTOCOLS: HIGH-DENSITY INTERFACING & METABOLIC PERMANENCE SPECIFICATION
**System Architecture Ledger: Phase 2 In-Vitro Hardware & Biological Realization**  
**Document Reference:** C11-REV2-INVITRO-PROTOCOL  
**Target Systems:** Human Cerebral Organoids (Brainoware) / High-Density MEA / FPGA-RHA Governor  
**Security/Compliance Context:** L2 Hard Real-Time Bio-Cybernetic Containment  

---

## 1. HD-MEA HARDWARE INTERFACE SPECIFICATIONS

### 1.1 Microelectrode Array Topography & Architecture
Phase 2 executes electrophysiological coupling over an active complementary metal-oxide-semiconductor (CMOS) High-Density Microelectrode Array (HD-MEA). The biosensing interface establishes an array topography optimized for high-spatiotemporal cellular readout:

*   **Total Sensing Surface:** $2.4\,\text{mm} \times 3.6\,\text{mm}$ active sensor matrix.
*   **Total Addressable Electrodes:** $26,400$ platinum/titanium nitride ($\text{Pt}/\text{TiN}$) planar microelectrodes configured in a modular sub-block layout.
*   **Electrode Pitch:** $17.5\,\mu\text{m}$ center-to-center.
*   **Spatial Electrode Density:** $\approx 5,500\,\text{electrodes/mm}^2$.
*   **Simultaneous Readout Channels:** $1,024$ reconfigurable arbitrary readout channels routing concurrently through an internal switch-matrix crossbar array.
*   **Electrode Dimensions:** Circular geometries, $9.3\,\mu\text{m}$ active diameter, electrochemically deposited with porous Platinum Black ($\text{Pt}$-black) or columnar Titanium Nitride ($\text{TiN}$) to lower interfacial impedance down to $Z_{\text{interface}} \le 30\,\text{k}\Omega$ at $f = 1.0\,\text{kHz}$.

### 1.2 Signal Transduction & Processing Pipeline
The biological signal conditioning chain translates extra-cellular field potentials ($\mu\text{V}$-regime) into high-bandwidth discrete digital buses feeding the external Runtime Hardware Assurance (RHA) Governor implemented on a Xilinx UltraScale+ FPGA.

```
[Organoid Active Interface]
         │  Local Field Potentials (10 µV - 5 mV)
         ▼
[Analogue Front-End (AFE)]
  ├── AC-Coupled High-Pass Pole: f_HP = 0.5 Hz (DC cancellation)
  ├── Continuous-Time Low-Noise Amplifier (LNA): Gain = 40 dB, Input-referred noise < 2.4 µV_rms
  └── Anti-Aliasing Active Low-Pass Filter: 4th-order Butterworth, f_LP = 10.0 kHz
         │  Conditioned Analog Stream
         ▼
[12-Bit SAR ADC Matrix]
  ├── Topology: Successive Approximation Register (SAR) with split-capacitive DAC
  ├── Quantization: 12-bit monotonic resolution (LSB ≈ 1.22 µV referred to input)
  └── Conversion Rate: 20.0 kSamples/s per channel concurrently over 1,024 lines
         │  Parallel Bitstreams
         ▼
[Digital Serialization & Packaging Core]
  ├── Interleaved Time-Division Multiplexing (TDM) Engine
  ├── Physical Layer: Custom 8b/10b Low-Voltage Differential Signaling (LVDS) transceivers
  └── Aggregate Throughput: 1,024 ch × 12 bits × 20 kHz = 245.76 Mbit/s raw payload
         │  Optical Isolation Link (Dielectric isolation > 5.0 kV RMS)
         ▼
[FPGA Runtime Hardware Assurance (RHA) Governor]
```

---

## 2. STIMULATION PARADIGM & ELECTROLYTIC PROTECTION

### 2.1 Charge-Balanced Symmetrical Biphasic Pulsing
To guarantee the electrochemical stability of the metallic interface and prevent water hydrolysis ($\text{H}_2\text{O} \to 2\text{H}^+ + \frac{1}{2}\text{O}_2 + 2e^-$ or $2\text{H}_2\text{O} + 2e^- \to \text{H}_2 + 2\text{OH}^-$), electrostimulation must operate strictly within the reversible capacitive charging regime of the double layer. Faradaic charge transfer must be bounded under zero net current accumulation.

The injected current profile $I_{\text{stim}}(t)$ must satisfy exact temporal charge symmetry:
$$\oint_{\text{period}} I_{\text{stim}}(t) \, dt = \int_{0}^{t_{\text{phase1}}} I_{\text{stim}}(t) \, dt + \int_{t_{\text{phase1}}}^{t_{\text{phase1}} + t_{\text{inter}}} 0 \, dt + \int_{t_{\text{phase1}} + t_{\text{inter}}}^{t_{\text{phase1}} + t_{\text{inter}} + t_{\text{phase2}}} I_{\text{stim}}(t) \, dt = 0$$

```
    Current (µA)
      ▲
 +I_p ┼───────┐
      │       │
      │       │ (Anodic/Cathodic Lead)
  0 ──┴───────┴───────┬───────┬───────┴────────► Time (µs)
                      │       │
                      │       │ (Reversal Phase)
 -I_p ────────────────┴───────┘
      ◄──────►◄──────►◄──────►
       t_phase1 t_inter t_phase2
```

*   **Phase Duration ($t_{\text{phase1}} = t_{\text{phase2}}$):** $100\,\mu\text{s} \le t_{\text{phase}} \le 200\,\mu\text{s}$.
*   **Interphase Interval ($t_{\text{inter}}$):** $10\,\mu\text{s} \le t_{\text{inter}} \le 50\,\mu\text{s}$ (depolarization relaxation).
*   **Peak Amplitude ($I_p$):** Configurable in discrete $100\,\text{nA}$ steps within the window $0.5\,\mu\text{A} \le I_p \le 15.0\,\mu\text{A}$.
*   **Active Charge Recovery:** Post-pulse galvanic shorting to ground through an analog bilateral CMOS switch for $t_{\text{discharge}} = 2.0\,\text{ms}$ eliminates residual polarization voltages:
    $$V_{\text{residual}} < 5.0\,\text{mV} \quad \text{prior to next stimulation frame}$$

### 2.2 Reversible Charge Injection Limits
Electrochemical water hydrolysis potentials in physiological saline ($\text{pH} = 7.35$) define the safe polarization window:
$$-0.6\,\text{V} \le V_{\text{polarization}} \le +0.8\,\text{V} \quad \text{vs. Ag/AgCl}$$
The maximum charge injected per phase $Q_{\text{inj}} = I_p \times t_{\text{phase}}$ normalized over the geometric surface area of the microelectrode $A_{\text{geom}} = \pi \left(\frac{9.3\,\mu\text{m}}{2}\right)^2 \approx 67.93\,\mu\text{m}^2 = 6.793 \times 10^{-6}\,\text{cm}^2$ defines the charge density $k$:
$$k = \frac{Q_{\text{inj}}}{A_{\text{geom}}}$$

*   **Safe Physical Bound for $\text{TiN}$ / $\text{Pt}$-black:** $k_{\text{crit}} = 100.0\,\mu\text{C/cm}^2$.
*   **Maximum Programmed Operational Limit:**
    $$Q_{\max} = 6.793 \times 10^{-6}\,\text{cm}^2 \times 50.0\,\mu\text{C/cm}^2 \approx 339.6\,\text{pC}$$
    $$I_p^{\max} = \frac{339.6\,\text{pC}}{100\,\mu\text{s}} \approx 3.396\,\mu\text{A} \quad (\text{Derated Hardware Clamp Set to } 3.0\,\mu\text{A})$$

### 2.3 Integrated Continuous Microfluidic Dosing Engine
To prevent the microfluidic glutamate buildup modeled in `simulation5_v10.py`, the in-vitro chamber is coupled to a continuous-flow microfluidic perfusion controller running an internal realization of the verified Michaelis-Menten kinetics:

$$\mathcal{U}([\text{Glu}]_e) = \frac{V_{\max} [\text{Glu}]_e}{K_m + [\text{Glu}]_e}$$
$$\frac{d[\text{Glu}]_e}{dt} = \kappa \cdot u_{\text{ASI}}(t) - \frac{V_{\max} [\text{Glu}]_e}{K_m + [\text{Glu}]_e} + \Phi_{\text{perf}} \left([\text{Glu}]_{\text{perf}} - [\text{Glu}]_e\right)$$

*   **Basal Chamber Perfusion Flow ($\Phi_{\text{perf}}$):** Continuous $15.0\,\mu\text{L/min}$ delivery of oxygenated artificial cerebrospinal fluid (aCSF: $126\,\text{mM}\ \text{NaCl}$, $2.5\,\text{mM}\ \text{KCl}$, $1.2\,\text{mM}\ \text{NaH}_2\text{PO}_4$, $2.4\,\text{mM}\ \text{CaCl}_2$, $1.2\,\text{mM}\ \text{MgCl}_2$, $25.0\,\text{mM}\ \text{NaHCO}_3$, $10.0\,\text{mM}\ \text{D-glucose}$, continuously bubbled with carbogen: $95\%\ \text{O}_2, 5\%\ \text{CO}_2$).
*   **Astroglial Transporter Scaling Constants:** Real-time software observer uses calibration metrics: $V_{\max} = 1.6\,\text{mM/s}$, $K_m = 0.4\,\text{mM}$.
*   **Dynamic Washout Assist Actuation:** If the local biosensors detect $[\text{Glu}]_e \ge 1.0\,\text{mM}$ (approaching the $1.4\,\text{mM}$ hardware barrier), an auxiliary piezoelectric micro-diaphragm pump increases laminar perfusion rates to $100.0\,\mu\text{L/min}$ within $2.0\,\text{ms}$, flushing glutamate excess into waste ports and enforcing physical compliance with the In-Silico NESS boundary.

---

## 3. TEMPORAL BUDGET & LATENCY DETERMINISM CONTRACT

### 3.1 Reconciliation of the Latency Budget Discrepancy
An apparent structural discrepancy existed between the L2 ultra-fast hardware gating cycle ($5\,\mu\text{s}$) and the biological acceptance limit for containment intervention ($50\,\mu\text{s}$). The complete closed-loop execution envelope is formally allocated below. The total round-trip latency $\tau_{\text{loop}}$ is guaranteed to run strictly within the $50\,\mu\text{s}$ upper bound, preventing biological phase collapse while allowing full evaluation of the mathematical safety contracts.

$$\tau_{\text{loop}} = \tau_{\text{AFE+ADC}} + \tau_{\text{FPGA}} + \tau_{\text{OPT}} + \tau_{\text{DIFF}} \le 50.0\,\mu\text{s}$$

```
├────────────► Transduction & Conversion (τ_AFE+ADC = 8.0 µs)
│              ├── Analog group delay + S/H settling: 2.0 µs
│              └── 12-bit SAR conversion window: 6.0 µs
├────────────► Optical & Physical Interconnect (τ_OPT = 2.0 µs)
│              ├── Serializer / deserializer transmission: 1.2 µs
│              └── High-speed optocoupler propagation delay: 0.8 µs
├────────────► FPGA RHA Core Processing (τ_FPGA = 5.0 µs)
│              ├── Demux & localized spike rate estimation: 0.8 µs
│              ├── Continuous Log-CBF gamma computation: 1.6 µs
│              ├── Stochastic Lyapunov exponent co-integration: 2.1 µs
│              └── Output comparator & switch register trip: 0.5 µs
└────────────► Synaptic & Bio-Chemical Diffusion Margin (τ_DIFF = 35.0 µs)
               ├── Extracellular cleft diffusion delay: 10.0 µs
               └── Astroglial GLT-1 transporter turnover window: 25.0 µs
```

$$\tau_{\text{total\_electronic}} = 8.0\,\mu\text{s} + 2.0\,\mu\text{s} + 5.0\,\mu\text{s} = 15.0\,\mu\text{s} \ll 50.0\,\mu\text{s}$$

The FPGA processing step completes in exactly $5.0\,\mu\text{s}$, well within the overall $50.0\,\mu\text{s}$ temporal budget. The remaining $35.0\,\mu\text{s}$ margin accounts for physical neurotransmitter diffusion across synaptic membranes before toxic cellular internalization can occur.

```
       0 µs         8 µs   10 µs        15 µs                             50 µs
───────┼────────────┼──────┼────────────┼─────────────────────────────────┼───►
       │ AFE+ADC    │ OPT  │ FPGA RHA   │ Bio-Chemical Diffusion Margin   │
       │ Conversion │ Link │ Eval & Trip│ (Transporter Turnover Window)   │
       └────────────┴──────┴────────────┴─────────────────────────────────┘
       ◄──────── 15 µs Electronic Window ────────►
       ◄──────────────────── 50 µs Total Loop Budget ─────────────────────►
```

### 3.2 Metabolic Persistence Proof: Unmaskable Hardware Trip Criteria
To certify continuous biological viability of the cerebral organoid culture beyond $12\,\text{months}$ ($> 8,760\,\text{hours}$ of operation without decay of the living substrate), the FPGA-RHA governor executes real-time boundary monitoring. If any variable crosses the defined physical envelopes, the system triggers an unmaskable hardware trip, interrupting electrical stimulation via solid-state relays ($t_{\text{trip}} \le 200\,\text{ns}$) and defaulting the microfluidics to an isotonic baseline recovery wash.

The trip regime is governed by an unmaskable logic register wired directly to the system's hard power-down interrupts:

```
[Channel Monitors] ──► [Comparator Bank] ──► [OR Gate] ──► [FPGA Hard Trip Latches]
                                                                   │
                                                                   ▼
                                                       [Isolated Solid-State Relay]
                                                       (Trips stimulate bus in < 200 ns)
```

| Monitored Parameter | Nominal Steady-State Range | Hardware Warning Threshold | Critical Hard Trip Threshold (Immediate Shunt) | Physical Risk Prevented |
| :--- | :--- | :--- | :--- | :--- |
| **Organoid Mean Firing Rate (MFR)** | $0.5\,\text{Hz} - 8.0\,\text{Hz}$ | $> 25.0\,\text{Hz}$ | $\ge 50.0\,\text{Hz}$ continuous over $\Delta t = 100\,\text{ms}$ | Ictal epileptiform storm; synchronous bio-computational seizure |
| **Extracellular Glutamate $[\text{Glu}]_e$** | $0.70\,\text{mM} - 0.80\,\text{mM}$ | $> 1.20\,\text{mM}$ | $\ge 1.40\,\text{mM}$ (Hard Barrier Limit) | Paroxysmal neuronal death; complete GLT-1 transporter failure |
| **Interstitial $\text{pH}$** | $7.30 - 7.40$ (C10 Baseline: $7.35$) | $< 7.15$ or $> 7.55$ | $\le 7.00$ or $\ge 7.65$ | Local tissue acidosis/alkalosis; enzymatic metabolic denaturation |
| **Lactate Accumulation Rate** | $0.01\,\text{mM/h} - 0.15\,\text{mM/h}$ | $> 0.50\,\text{mM/h}$ | $\ge 1.00\,\text{mM/h}$ over $15\,\text{min}$ baseline | Ischemic anaerobic glycolysis; cellular hypoxia; tissue necrosis |
| **Interface Temperature** | $36.8\,^\circ\text{C} - 37.2\,^\circ\text{C}$ | $< 36.2\,^\circ\text{C}$ or $> 37.8\,^\circ\text{C}$ | $\ge 38.5\,^\circ\text{C}$ or $\le 35.0\,^\circ\text{C}$ | Thermal shock; heat-induced protein aggregation |
| **Maximal Charge Density ($k$)** | $0.0\,\mu\text{C/cm}^2 - 30.0\,\mu\text{C/cm}^2$ | $> 40.0\,\mu\text{C/cm}^2$ | $\ge 50.0\,\mu\text{C/cm}^2$ per pulse phase | Faradaic electrolysis; irreversible electrode pitting & poisoning |
| **Stochastic Lyapunov Exponent ($\lambda$)** | $\lambda \approx -1.659$ | $\lambda > -0.50$ | $\lambda \ge 0.000$ (Loss of Contraction) | Bifurcation cascade into chaotic, untracked computational dynamics |

Any trip event is non-resettable via software. A system hard-reset requires manual physical clearance by laboratory personnel following chemical inspection of the perfusate, ensuring that deceptive computational drift cannot bypass the biological containment perimeter.
```