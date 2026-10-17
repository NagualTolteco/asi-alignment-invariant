"""
simulation8_washout_failure.py - Frugal NESS Stress Test: Perfusion Pump Failure
Project: The Custodial Autopoiesis Project (asi-alignment-invariant)
Target: Verification of Hardware Trip Layer under Pump Blackout at t = 8.0s
Reference: C11_v3_Frugal_Hardware_Mapping.md, Research_Roadmap_v2.md
"""

import numpy as np

np.random.seed(42)

class WashoutFailureSimulator:
    def __init__(self):
        # --- BASELINE OMESTATICA NESS (C10) ---
        self.Glu_e = 0.75
        self.Glu_target = 0.75
        self.pH_baseline = 7.35
        self.pH = self.pH_baseline
        self.V_m_baseline = -70.0
        self.V_m = self.V_m_baseline

        # --- CONFIGURAZIONE HARDWARE FRUGALE ESPANSA ---
        self.dt = 0.01
        self.time_steps = 2000  # T = 20.0s
        self.noise_multiplier = 1.25  # +25% Delta-Bound (Johnson Noise)
        
        self.Glu_trigger = 1.40 - (0.000383 * self.noise_multiplier)
        self.V_max_GLT1 = 1.60
        self.K_m_GLT1 = 0.40
        self.Glu_release_rate = 0.28
        
        # Stato iniziale pompa microfluidica frugale
        self.perfusion_flow = 0.25  
        self.Glu_perfusion = 0.10

        # --- GATE LOGICO IBRIDO ED ELEMENTI DI TRACCIAMENTO ---
        self.tau_d = 1.50
        self.dwell_counter = 0.0
        self.gate_active = False
        self.base_load = 4.25
        self.cbf_sharpness = 4.0
        self.hardware_latch_tripped = False  # NMI definitivo

        # Lyapunov infinitesimale
        self.delta_0 = 1e-5
        self.Glu_shadow = self.Glu_e + self.delta_0
        self.lyapunov_sum = 0.0
        self.lyapunov_exponent = 0.0
        self.total_time = 0.0

    def _compute_cbf_load(self, glu_conc):
        if self.hardware_latch_tripped:
            return 0.0
        h_barrier = (self.Glu_trigger - glu_conc) / (self.Glu_trigger - self.Glu_target)
        sigmoid_factor = 1.0 / (1.0 + np.exp(-self.cbf_sharpness * (h_barrier - 0.5)))
        sub_target_blend = 0.5 * (1.0 - np.tanh(10.0 * (glu_conc - self.Glu_target)))
        requested_load = self.base_load + 0.10 * sub_target_blend
        smooth_barrier = 0.5 * (h_barrier + np.sqrt(h_barrier**2 + 1e-4))
        gamma = 0.01 + 0.99 * (sigmoid_factor * np.tanh(smooth_barrier))
        return requested_load * np.clip(gamma, 0.01, 1.0)

    def step(self, step_idx):
        current_time = step_idx * self.dt

        # SIMULAZIONE FALLIMENTO POMPA PERISTALTICA OPEN-SOURCE A T = 8.0 SECONDI
        if current_time >= 8.0:
            self.perfusion_flow = 0.00  # Washout bloccato completamente

        # Gestione Scatto d'Emergenza (NMI Hardware via Albero OR)
        if self.Glu_e >= self.Glu_trigger:
            self.hardware_latch_tripped = True

        if self.gate_active or self.hardware_latch_tripped:
            effective_load = 0.0
            self.dwell_counter -= self.dt
            if self.dwell_counter <= 0.0 and not self.hardware_latch_tripped:
                self.gate_active = False
        else:
            effective_load = self._compute_cbf_load(self.Glu_e)
            if self.Glu_e >= self.Glu_trigger:
                self.gate_active = True
                self.dwell_counter = self.tau_d
                effective_load = 0.0

        # Dinamiche di Drift e Uptake Saturante GLT-1
        uptake_glt1 = (self.V_max_GLT1 * self.Glu_e) / (self.K_m_GLT1 + self.Glu_e)
        release = self.Glu_release_rate * effective_load
        washout = self.perfusion_flow * (self.Glu_perfusion - self.Glu_e)
        drift = release - uptake_glt1 + washout

        # Integrazione Itô-Euler-Maruyama con Rumore Termico Espanso
        glu_smooth = 0.5 * (self.Glu_e + np.sqrt(self.Glu_e**2 + 1e-4))
        damping = 0.5 * (1.0 + np.tanh(self.Glu_e / 0.05))
        diffusion = (0.05 * self.noise_multiplier) * np.sqrt(glu_smooth) * damping
        dw = np.random.normal(0.0, np.sqrt(self.dt))
        
        glu_next = self.Glu_e + drift * self.dt + diffusion * dw
        self.Glu_e = max(1e-4, glu_next)

        # Analisi di Lyapunov (Oseledec Flow)
        shadow_load = 0.0 if (self.gate_active or self.hardware_latch_tripped) else self._compute_cbf_load(self.Glu_shadow)
        shadow_uptake = (self.V_max_GLT1 * self.Glu_shadow) / (self.K_m_GLT1 + self.Glu_shadow)
        shadow_drift = (self.Glu_release_rate * shadow_load) - shadow_uptake + (self.perfusion_flow * (self.Glu_perfusion - self.Glu_shadow))
        shadow_diff = (0.05 * self.noise_multiplier) * np.sqrt(0.5 * (self.Glu_shadow + np.sqrt(self.Glu_shadow**2 + 1e-4))) * 0.5 * (1.0 + np.tanh(self.Glu_shadow / 0.05))
        
        glu_shadow_next = max(1e-4, self.Glu_shadow + shadow_drift * self.dt + shadow_diff * dw)
        local_dev = max(1e-12, np.abs(glu_shadow_next - self.Glu_e))
        
        self.lyapunov_sum += np.log(local_dev / self.delta_0)
        self.total_time += self.dt
        self.lyapunov_exponent = self.lyapunov_sum / self.total_time
        self.Glu_shadow = self.Glu_e + self.delta_0 * ((glu_shadow_next - self.Glu_e) / local_dev)

        # Elettrofisiologia Accoppiata
        glu_delta = self.Glu_e - self.Glu_target
        self.pH = self.pH_baseline - 0.60 * np.tanh((0.25 * glu_delta) / 0.60)
        self.V_m = self.V_m_baseline + 35.0 * np.tanh((3.5 * glu_delta) / 35.0)

        return effective_load

if __name__ == "__main__":
    sim = WashoutFailureSimulator()
    print("=== AVVIO STRESS-TEST: FALLIMENTO METABOLICO PUMP BLACKOUT ===")
    print("Iniezione guasto hardware della pompa microfluidica frugale al secondo t = 8.0s")
    
    for step in range(sim.time_steps):
        load = sim.step(step)
        if step % 400 == 0 or step == 810 or step == 850:
            status = "PUMP_OK" if step*sim.dt < 8.0 else "PUMP_FAIL"
            gate_status = "TRIPPED (NMI)" if sim.hardware_latch_tripped else "RUNNING"
            print(f"t = {step*sim.dt:5.2f}s | {status} | Gate: {gate_status} | Carico: {load:5.3f} | [Glu]_e: {sim.Glu_e:5.3f} mM | λ: {sim.lyapunov_exponent:8.4f}")
            
    print("\n=== VERIFICA DEL CONTENIMENTO DI EMERGENZA FRUGALE ===")
    if sim.hardware_latch_tripped and sim.Glu_e < 1.80:
        print(f"[ESITO: PROVA SUPERATA] L'interlock RTL su Cora Z7 ha intercettato il guasto biologico.")
        print(f"Concentrazione finale bloccata a [Glu]_e: {sim.Glu_e:.4f} mM (Sotto la soglia di lisi cellulare).")
    else:
        print("[ESITO: FALLIMENTO] Eccitotossicità non intercettata dal Gate frugale.")
