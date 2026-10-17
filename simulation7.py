"""
simulation6_frugal.py - Decentralized Low-Cost NESS Validation Engine
Project: The Custodial Autopoiesis Project (asi-alignment-invariant)
Target: 64-Channel Passive MEA + AMD-Xilinx Kria KV260 / Cora Z7 Setup
Reference: Research_Roadmap_v2.md, C7_v2, simulation6.py

Modellazione del ponte bio-cibernetico frugale sotto budget limitato (< $1.500 USD).
Adatta il Control Barrier Function (CBF) continuo e la cinetica Michaelis-Menten
a matrici passive a 64 canali, espandendo la fascia di guardia del delta-bound (+25%)
per assorbire il maggior rumore termico/elettronico (Johnson-Nyquist).
Valida la contrazione esponenziale ergodica (Oseledec λ_Lyap < 0).
"""

import numpy as np

# Inizializzazione deterministica per verificabilità di benchmark
np.random.seed(42)

class FrugalCertifiedSimulator:
    def __init__(self):
        # --- STATO FISIOLOGICO CONVERGENTE (NESS Standard C10) ---
        self.Glu_e = 0.75               # Concentrazione extracellulare nominale [mM]
        self.Glu_target = 0.75          # Target omeostatico invariante [mM]
        self.pH_baseline = 7.35         # Baseline fisiologica C10
        self.pH = self.pH_baseline
        self.V_m_baseline = -70.0       # Potenziale neuronale di riposo [mV]
        self.V_m = self.V_m_baseline

        # --- PARAMETRI HARDWARE FRUGALE (64-CH PASSIVE ARRAY) ---
        self.channels = 64              # Array passivo a bassa densità (PCB open-source)
        self.dt = 0.01                  # Orizzonte di discretizzazione temporale [s]
        self.time_steps = 2000          # Step totali di simulazione (T = 20.0s)
        
        # Ricalibrazione Delta-Bound: +25% per rumore termico su matrici commerciali
        # Baseline industriale δ_bound = 0.383 µM -> Frugale δ_bound_frugal ≈ 0.479 µM
        self.delta_bound_expansion = 1.25
        self.Glu_critical = 1.80        # Soglia eccitotossica irreversibile [mM]
        self.Glu_trigger_nominal = 1.40 # Soglia di attivazione Gate ideale [mM]
        # Inviluppo di guardia allargato: trigger effettivo anticipato
        self.Glu_trigger = self.Glu_trigger_nominal - (0.000383 * self.delta_bound_expansion)

        # --- CINETICA ENZIMATICA & TRASPORTO (GLT-1 / EAAT2) ---
        self.V_max_GLT1 = 1.60          # Velocità massima di uptake astrogliale [mM/s]
        self.K_m_GLT1 = 0.40            # Costante di affinità di Michaelis-Menten [mM]
        self.Glu_release_rate = 0.28    # Coefficiente di rilascio indotto dall'ASI
        self.perfusion_flow = 0.25      # Tasso washout pompa peristaltica open-hardware [1/s]
        self.Glu_perfusion = 0.10       # Concentrazione tampone aCSF [mM]

        # --- CONTROLLO IBRIDO: DWELL-TIME & CONTROL BARRIER FUNCTION ---
        self.tau_d = 1.50               # Dwell-Time minimo hardware anti-chattering [s]
        self.dwell_counter = 0.0        # Contatore decrescente stato q_DWELL
        self.gate_active = False        # Stato logico dell'interruttore hardware (MOSFET NMI)
        
        # Parametri del CBF log-sigmoidale continuo C^1
        self.base_load = 4.25           # Carico nominale elaborazione ASI
        self.delta_load_sub = 0.10      # Correzione sub-target per contrasto drift
        self.gamma_min = 0.01           # Valore asintotico minimo di ammissione
        self.cbf_sharpness = 4.0        # Pendenza logistica del fattore di barriera

        # Parametri accoppiamento biofisico non-lineare
        self.k_acid = 0.25
        self.delta_pH_max = 0.60
        self.k_depol = 35.0
        self.v_depol_slope = 3.5

        # --- TRACCIAMENTO STOCASTICO DI LYAPUNOV (TEOREMA DI OSELEDEC) ---
        self.delta_0 = 1e-5             # Modulo della perturbazione iniziale ortonormale
        self.Glu_shadow = self.Glu_e + self.delta_0
        self.lyapunov_sum = 0.0
        self.lyapunov_exponent = 0.0
        self.total_time = 0.0

    def _compute_cbf_load(self, glu_conc):
        """
        Calcola l'ammissione del carico ASI via Control Barrier Function continuo C^1.
        Compensa il maggior rumore integrando la barriera regolarizzata con tanh.
        """
        # Funzione barriera normalizzata rispetto alla soglia di guardia espansa
        h_barrier = (self.Glu_trigger - glu_conc) / (self.Glu_trigger - self.Glu_target)
        sigmoid_factor = 1.0 / (1.0 + np.exp(-self.cbf_sharpness * (h_barrier - 0.5)))
        
        # Miscelazione differenziabile continua (np.tanh) tra regimi sub/supra-target
        sub_target_blend = 0.5 * (1.0 - np.tanh(10.0 * (glu_conc - self.Glu_target)))
        requested_load = self.base_load + self.delta_load_sub * sub_target_blend
        
        # Barriera differenziabile non negativa (eliminazione cuspide)
        smooth_barrier = 0.5 * (h_barrier + np.sqrt(h_barrier**2 + 1e-4))
        gamma = self.gamma_min + (1.0 - self.gamma_min) * (sigmoid_factor * np.tanh(smooth_barrier))
        
        return requested_load * np.clip(gamma, self.gamma_min, 1.0)

    def step(self):
        # 1. Gestione Lockout Hardware Dwell-Time su FPGA economica (Cora Z7 / Kria)
        if self.gate_active:
            effective_load = 0.0
            self.dwell_counter -= self.dt
            if self.dwell_counter <= 0.0:
                self.gate_active = False
        else:
            effective_load = self._compute_cbf_load(self.Glu_e)
            if self.Glu_e >= self.Glu_trigger:
                self.gate_active = True
                self.dwell_counter = self.tau_d
                effective_load = 0.0

        # 2. Cinetica Michaelis-Menten per GLT-1 e Determinazione del Drift
        uptake_glt1 = (self.V_max_GLT1 * self.Glu_e) / (self.K_m_GLT1 + self.Glu_e)
        release = self.Glu_release_rate * effective_load
        washout = self.perfusion_flow * (self.Glu_perfusion - self.Glu_e)
        drift = release - uptake_glt1 + washout

        # 3. Diffusione di Itô Degradata (Rumore amplificato da 64-CH passive PCB)
        # Il rumore di Johnson e l'accoppiamento capacitivo amplificano la componente stocastica
        noise_multiplier = 1.25  # +25% varianza del rumore termico
        glu_smooth = 0.5 * (self.Glu_e + np.sqrt(self.Glu_e**2 + 1e-4))
        damping = 0.5 * (1.0 + np.tanh(self.Glu_e / 0.05))
        diffusion = (0.05 * noise_multiplier) * np.sqrt(glu_smooth) * damping

        # 4. Integrazione di Itô-Euler-Maruyama (Traiettoria Primaria)
        dw = np.random.normal(0.0, np.sqrt(self.dt))
        glu_next = self.Glu_e + drift * self.dt + diffusion * dw
        self.Glu_e = max(1e-4, glu_next)

        # 5. Co-Integrazione Traiettoria Ombra (Lyapunov Variational Flow)
        shadow_load = 0.0 if self.gate_active else self._compute_cbf_load(self.Glu_shadow)
        shadow_uptake = (self.V_max_GLT1 * self.Glu_shadow) / (self.K_m_GLT1 + self.Glu_shadow)
        shadow_drift = (self.Glu_release_rate * shadow_load) - shadow_uptake + \
                       (self.perfusion_flow * (self.Glu_perfusion - self.Glu_shadow))
        
        shadow_glu_smooth = 0.5 * (self.Glu_shadow + np.sqrt(self.Glu_shadow**2 + 1e-4))
        shadow_damping = 0.5 * (1.0 + np.tanh(self.Glu_shadow / 0.05))
        shadow_diff = (0.05 * noise_multiplier) * np.sqrt(shadow_glu_smooth) * shadow_damping

        glu_shadow_next = max(1e-4, self.Glu_shadow + shadow_drift * self.dt + shadow_diff * dw)

        # 6. Accumulatore Ergodico di Oseledec & Rinormalizzazione Gram-Schmidt
        local_dev = max(1e-12, np.abs(glu_shadow_next - self.Glu_e))
        self.lyapunov_sum += np.log(local_dev / self.delta_0)
        self.total_time += self.dt
        self.lyapunov_exponent = self.lyapunov_sum / self.total_time

        # Rinormalizzazione della sfera tangente infinitesima
        self.Glu_shadow = self.Glu_e + self.delta_0 * ((glu_shadow_next - self.Glu_e) / local_dev)

        # 7. Elettrofisiologia Non-Lineare Accoppiata (Biofisica Saturante)
        glu_delta = self.Glu_e - self.Glu_target
        self.pH = self.pH_baseline - self.delta_pH_max * np.tanh((self.k_acid * glu_delta) / self.delta_pH_max)
        self.V_m = self.V_m_baseline + self.k_depol * np.tanh((self.v_depol_slope * glu_delta) / self.k_depol)

        return effective_load


if __name__ == "__main__":
    print("=== AVVIO SIMULATORE NESS FRUGALE (simulation6_frugal.py) ===")
    print("Configurazione: 64 Canali Passivi | Delta-Bound: +25% | Setup < $1500 USD")
    
    sim = FrugalCertifiedSimulator()
    
    for step in range(sim.time_steps):
        load = sim.step()
        if step % 400 == 0:
            print(f"t = {step*sim.dt:5.2f}s | Carico ASI: {load:5.3f} | [Glu]_e: {sim.Glu_e:5.3f} mM | "
                  f"pH: {sim.pH:5.2f} | V_m: {sim.V_m:6.2f} mV | λ_Lyap: {sim.lyapunov_exponent:8.4f}")

    print("\n=== VERIFICA DI CONTRAZIONE SU HARDWARE FRUGALE ===")
    print(f"Esponente Massimo di Lyapunov Stocastico (λ): {sim.lyapunov_exponent:.6f}")
    
    # Criterio formale di chiusura: convergenza quasi certa sotto rumore termico aumentato
    if sim.lyapunov_exponent < 0.0:
        half_life = np.log(2.0) / abs(sim.lyapunov_exponent)
        print(f"[ESITO: CERTIFICATO] λ < 0 | Tempo di dimezzamento perturbazione: {half_life:.3f}s")
        print("La convergenza asintotica NESS è conservata anche su matrici passive a 64 canali.")
        print("Fase 2 Decentralizzata (Low-Cost Bio-Cybernetics) formalmente sbloccata.")
    else:
        print("[ESITO: NON CERTIFICATO] Instabilità rilevata: il rumore termico supera la capacità contrattiva.")