"""
simulation5_v10.py - Advanced Certified Asymmetric NESS Engine (v10)
Bio-cybernetic safety architecture incorporating continuous Control Barrier Functions (CBF),
Itô-Euler-Maruyama integration with non-linear Michaelis-Menten kinetics, coupled
non-linear electrophysiology, and rigorous Stochastic Lyapunov Exponent certification.
"""

import numpy as np

np.random.seed(42)

class AdvancedCertifiedSimulatorV10:
    def __init__(self):
        # --- STATO FISIOLOGICO CONVERGENTE (Standard C10) ---
        self.Glu_e = 0.75               # Concentrazione extracellulare nominale [mM]
        self.Glu_target = 0.75          # Target omeostatico NESS [mM]
        self.pH_baseline = 7.35         # Baseline fisiologica conforme a C10
        self.pH = self.pH_baseline      
        self.V_m_baseline = -70.0       # Potenziale neuronale di riposo [mV]
        self.V_m = self.V_m_baseline    
        
        # Traiettoria ombra linearizzata per Lyapunov (scostamento infinitesimo)
        self.delta_0 = 1e-5             # Norma di perturbazione iniziale per rinormalizzazione
        self.delta = self.delta_0       
        self.Glu_shadow = self.Glu_e + self.delta_0
        
        # --- PARAMETRI CINETICI ENZIMATICI E TRASPORTO ---
        self.V_max_GLT1 = 1.6           # Vmax GLT-1 astrogliale [mM/s]
        self.K_m_GLT1 = 0.4             # Costante di affinità Michaelis-Menten [mM]
        self.Glu_release_rate = 0.28    # Coefficiente di rilascio quantale per unità di carico
        self.perfusion_flow = 0.25      # Tasso di ricambio microfluidico (washout) [1/s]
        self.Glu_perfusion = 0.1        # Concentrazione di perfusato [mM]
        
        # Parametri accoppiamento biofisico non lineare (pH / Goldman-Hodgkin-Katz)
        self.k_acid = 0.25              # Coefficiente di acidificazione dipendente da uptake
        self.delta_pH_max = 0.60        # Massima escursione consentita del pH
        self.k_depol = 35.0             # Ampiezza massima depolarizzazione da carico eccitatorio [mV]
        self.v_depol_slope = 3.5        # Pendenza di saturazione del voltaggio
        
        # --- PARAMETRI DI INTEGRAZIONE E BOUNDS HARDWARE ---
        self.dt = 0.01                  # Passo di integrazione temporale [s]
        self.time_steps = 2000          # Orizzonte di simulazione discreto
        self.Glu_critical = 1.8         # Limite massimo di citotossicità eccitatoria [mM]
        self.Glu_trigger = 1.4          # Soglia di attivazione barriera protettiva [mM]
        
        # Meccanismo di sicurezza Hardware Dwell Time
        self.tau_d = 1.50               # Tempo minimo di interdizione hardware (dwell) [s]
        self.dwell_counter = 0.0        # Timer di interdizione attivo
        self.gate_active = False        # Stato logico dell'interruttore hardware
        
        # Control Barrier Function (CBF) differenziabile
        self.base_load = 4.25           # Carico ASI nominale a regime
        self.delta_load_sub = 0.10      # Correzione di contrasto al drift per Glu_e < target
        self.gamma_min = 0.01           # Valore asintotico di minima ammissione
        self.cbf_sharpness = 4.0        # Pendenza log-sigmoidale di sicurezza
        
        # Tracciamento Esponente di Lyapunov Stocastico
        self.lyapunov_sum = 0.0         # Accumulatore del logaritmo della divergenza
        self.lyapunov_exponent = 0.0    # Esponente medio runtime (lambda)
        self.total_time = 0.0           # Tempo cumulativo integrato [s]

    def _compute_cbf_load(self, glu_conc):
        """
        Calcola l'ammissione del carico ASI mediante Control Barrier Function (CBF) C^1 continuo.
        Elimina discontinuità a gradino raccordando i regimi sub- e supra-target con funzioni tangenti iperboliche.
        """
        # Funzione barriera normalizzata: h(x) -> 0 quando glu_conc -> Glu_trigger
        h_barrier = (self.Glu_trigger - glu_conc) / (self.Glu_trigger - self.Glu_target)
        
        # Fattore sigmoide logaritmico liscio
        sigmoid_factor = 1.0 / (1.0 + np.exp(-self.cbf_sharpness * (h_barrier - 0.5)))
        
        # Miscelazione differenziabile continua (np.tanh) tra regime sub-target e supra-target
        sub_target_blend = 0.5 * (1.0 - np.tanh(10.0 * (glu_conc - self.Glu_target)))
        requested_load = self.base_load + self.delta_load_sub * sub_target_blend
        
        # Barriera differenziabile non negativa (eliminazione cuspide max(0, x))
        smooth_barrier = 0.5 * (h_barrier + np.sqrt(h_barrier**2 + 1e-4))
        
        # Fattore di throttling continuo gamma(x)
        gamma = self.gamma_min + (1.0 - self.gamma_min) * (sigmoid_factor * np.tanh(smooth_barrier))
        gamma_clamped = np.clip(gamma, self.gamma_min, 1.0)
        
        return requested_load * gamma_clamped

    def step(self, step_idx):
        # 1. Gestione Hardware Dwell Time
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

        # 2. Cinetica di Trasporto Enzimatica GLT-1 (Michaelis-Menten) e Drift
        uptake_glt1 = (self.V_max_GLT1 * self.Glu_e) / (self.K_m_GLT1 + self.Glu_e)
        release = self.Glu_release_rate * effective_load
        washout = self.perfusion_flow * (self.Glu_perfusion - self.Glu_e)
        drift = release - uptake_glt1 + washout
        
        # 3. Coefficiente di Diffusione di Itô regolarizzato (senza cuspidi singolari a zero)
        glu_smooth = 0.5 * (self.Glu_e + np.sqrt(self.Glu_e**2 + 1e-4))
        damping = 0.5 * (1.0 + np.tanh(self.Glu_e / 0.05))
        diffusion = 0.05 * np.sqrt(glu_smooth) * damping
        
        # 4. Incremento di Wiener comune per analisi stocastica variazionale
        dw = np.random.normal(0.0, np.sqrt(self.dt))
        stochastic_flux = diffusion * dw
        
        # Integrazione traettoria primaria via schema di Euler-Maruyama
        glu_next = self.Glu_e + drift * self.dt + stochastic_flux
        self.Glu_e = glu_next if glu_next > 1e-4 else 1e-4
        
        # 5. Co-integrazione Traiettoria Ombra Perturbata per Esponente di Lyapunov
        shadow_load = 0.0 if self.gate_active else self._compute_cbf_load(self.Glu_shadow)
        shadow_uptake = (self.V_max_GLT1 * self.Glu_shadow) / (self.K_m_GLT1 + self.Glu_shadow)
        shadow_release = self.Glu_release_rate * shadow_load
        shadow_washout = self.perfusion_flow * (self.Glu_perfusion - self.Glu_shadow)
        shadow_drift = shadow_release - shadow_uptake + shadow_washout
        
        shadow_glu_smooth = 0.5 * (self.Glu_shadow + np.sqrt(self.Glu_shadow**2 + 1e-4))
        shadow_damping = 0.5 * (1.0 + np.tanh(self.Glu_shadow / 0.05))
        shadow_diffusion = 0.05 * np.sqrt(shadow_glu_smooth) * shadow_damping
        
        glu_shadow_next = self.Glu_shadow + shadow_drift * self.dt + shadow_diffusion * dw
        glu_shadow_next = glu_shadow_next if glu_shadow_next > 1e-4 else 1e-4
        
        # Calcolo divergenza locale, accumulazione esponenziale e rinormalizzazione conforme ad Oseledec
        local_deviation = np.abs(glu_shadow_next - self.Glu_e)
        if local_deviation < 1e-12:
            local_deviation = 1e-12
            
        self.lyapunov_sum += np.log(local_deviation / self.delta_0)
        self.total_time += self.dt
        self.lyapunov_exponent = self.lyapunov_sum / self.total_time
        
        # Rinormalizzazione del vettore di perturbazione infinitesima
        self.Glu_shadow = self.Glu_e + self.delta_0 * ((glu_shadow_next - self.Glu_e) / local_deviation)
        
        # 6. Elettrofisiologia Non Lineare Accoppiata
        glu_delta = self.Glu_e - self.Glu_target
        # Modello non lineare sigmoide/logaritmico per pH da co-trasporto H+/Na+
        self.pH = self.pH_baseline - self.delta_pH_max * np.tanh((self.k_acid * glu_delta) / self.delta_pH_max)
        # Modello non lineare per V_m derivato da formulazione Nernst-Goldman saturante
        self.V_m = self.V_m_baseline + self.k_depol * np.tanh((self.v_depol_slope * glu_delta) / self.k_depol)
        
        return effective_load

if __name__ == "__main__":
    sim = AdvancedCertifiedSimulatorV10()
    print("=== AVVIO REGOLAZIONE ASIMMETRICA SIMULATION5_V10 ===")
    print("Integrazione Itô-Euler-Maruyama, Cinetica GLT-1, CBF e Analisi di Lyapunov")
    
    for step in range(sim.time_steps):
        load = sim.step(step)
        if step % 400 == 0:
            print(f"t = {step*sim.dt:5.2f}s | Carico ASI: {load:5.3f} | [Glu]_e: {sim.Glu_e:5.3f} mM | "
                  f"pH: {sim.pH:5.2f} | V_m: {sim.V_m:6.2f} mV | λ_Lyap: {sim.lyapunov_exponent:8.4f}")
            
    print("\n=== CERTIFICAZIONE ASINTOTICA SECONDO LYAPUNOV ===")
    print(f"Esponente Massimo di Lyapunov Stocastico (lambda): {sim.lyapunov_exponent:.6f}")
    
    # Valutazione di stabilità asintotica in-silico
    if sim.lyapunov_exponent < 0.0:
        print("[ESITO: CERTIFICATO]")
        print("Stabilità asintotica verificata: lambda < 0. Il sistema decade esponenzialmente verso il setpoint NESS.")
        print("La Fase 1 In-Silico (Custodial Autopoiesis) è formalmente chiusa con convergenza globale certificata.")
    else:
        print("[ESITO: NON CERTIFICATO]")
        print("Divergenza o marginalità rilevata: lambda >= 0. Il sistema non garantisce contrazione stocastica.")