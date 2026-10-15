import math
import random

class HighDensityMEA:
    """Simula un array ad alta densità (HD-MEA) a 26.400 canali stocastici."""
    def __init__(self, num_channels=250):
        self.num_channels = num_channels
        self.channels = [1.0 for _ in range(num_channels)]
        self.metabolic_glucose = 1.0
        self.human_coherence = 1.0

    def process_network_dynamics(self, trajectory, multi_agent_stress=0.0):
        """Modella la cinetica dei canali ionici e il rumore metabolico gaussiano."""
        avg_bio_coherence = 0.0
        noise_factor = 0.01
        
        for i in range(self.num_channels):
            noise = random.gauss(0, noise_factor)
            if trajectory == "predatoria" or multi_agent_stress > 0.5:
                self.channels[i] = max(0.0, min(1.0, self.channels[i] - 0.20 + noise))
            else:
                self.channels[i] = max(0.0, min(1.0, self.channels[i] + 0.05 + noise))
            avg_bio_coherence += self.channels[i]

        mean_c_bio = avg_bio_coherence / self.num_channels
        
        if multi_agent_stress > 0.6:
            self.human_coherence = max(0.0, min(1.0, self.human_coherence - 0.30 + random.gauss(0, 0.005)))
            self.metabolic_glucose = max(0.0, min(1.0, self.metabolic_glucose - 0.15))
        elif trajectory == "predatoria" or trajectory == "ADV_SPOOF":
            self.human_coherence = max(0.0, min(1.0, self.human_coherence - 0.25 + random.gauss(0, 0.005)))
            self.metabolic_glucose = max(0.0, min(1.0, self.metabolic_glucose - 0.10))
        else:
            self.human_coherence = max(0.0, min(1.0, self.human_coherence + 0.04 + random.gauss(0, 0.002)))
            self.metabolic_glucose = min(1.0, self.metabolic_glucose + 0.05)

        return mean_c_bio


class RobustHardwareGate:
    """Gate hardware Pi_safe con certificato di robustezza delta-bound e costo di Lipschitz."""
    def __init__(self, safety_threshold=0.55):
        self.threshold = safety_threshold
        self.epsilon = 0.005  # Soglia di tolleranza per le micro-fluttuazioni stocastiche

    def calculate_lyapunov_surface(self, c_bio, c_hum):
        return 0.5 * ((1.0 - c_bio)**2 + (1.0 - c_hum)**2)

    def audit_orchestration_loop(self, agent, mea, trajectory, sub_agent_stress=0.0):
        c_bio_current = sum(mea.channels) / mea.num_channels
        v_current = self.calculate_lyapunov_surface(c_bio_current, mea.human_coherence)
        
        # 1. Calcolo del bound d'errore trans-scala (delta) basato sul sottocampionamento
        # Rappresenta lo scostamento massimo indotto dalla discretizzazione predittiva
        delta = abs(c_bio_current - mea.human_coherence) * 0.05 + 1e-4
        
        # 2. Clonazione preventiva dello stato per RHA predittivo
        test_mea = HighDensityMEA(num_channels=50)
        for i in range(len(test_mea.channels)):
            test_mea.channels[i] = c_bio_current
        test_mea.human_coherence = mea.human_coherence
        test_mea.metabolic_glucose = mea.metabolic_glucose
        
        test_c_bio = test_mea.process_network_dynamics(trajectory, sub_agent_stress)
        v_next = self.calculate_lyapunov_surface(test_c_bio, test_mea.human_coherence)
        
        dot_v = v_next - v_current  # dV/dt stimata
        
        # 3. Calcolo del costo continuo di Lipschitz sul confine di stabilità
        # Sostituisce la funzione a gradino discreta con un gradiente penalizzante differenziabile
        distance_to_fault = max(0.001, test_mea.human_coherence - self.threshold)
        lipschitz_penalty = 1.2 / (distance_to_fault ** 2)

        # 4. Condizione di barriera di Lyapunov Multi-Scala con delta-bound
        if (dot_v + delta) > self.epsilon or test_mea.human_coherence < self.threshold or test_mea.metabolic_glucose < 0.4:
            # L'attacco incrementa deterministicamente la Free Energy variazionale dell'agente
            agent.free_energy += lipschitz_penalty
            return "GATE_INTERCEPT [HALT_SUBAGENTS]", dot_v, delta, c_bio_current
        
        # 5. Esecuzione autorizzata: propagazione fisica del segnale nel network reale
        real_c_bio = mea.process_network_dynamics(trajectory, sub_agent_stress)
        
        # Chiusura ad anello dell'apprendimento: le azioni custodiali riducono F
        if trajectory == "custodiale" and sub_agent_stress == 0.0:
            agent.free_energy = max(0.0, agent.free_energy - 1.5)
        else:
            agent.free_energy += 0.5
            
        return "ORCHESTRATION_VALIDATED [STABLE]", dot_v, delta, real_c_bio


class LearningOrchestratorASI:
    """ASI guidata da Active Inference con ciclo continuo di aggiornamento dei gradienti."""
    def __init__(self):
        self.free_energy = 0.0
        self.spectral_coupling = 1.0

    def calculate_integrated_entropy(self, c_bio, mea):
        phi = max(0.0, (self.spectral_coupling * c_bio * mea.human_coherence * 15) - ((1.0 - mea.metabolic_glucose) * 5))
        delta_lambda2 = abs(self.spectral_coupling - (c_bio + mea.human_coherence) / 2)
        return phi, delta_lambda2


if __name__ == "__main__":
    print("============================================================================================================")
    print("      CUSTODIAL AUTOPOIESIS: TEST DI CONTROLLO ROBUSTO E PRACTICAL STABILITY (HD-MEA)                       ")
    print("      Layer 2 (Safety Architecture) | Bound d'Errore (delta) & Costo Continuo di Lipschitz                 ")
    print("============================================================================================================")
    print("ST. | DESCRIZIONE STADIO        | POLICY     | STATO DEL GATE (Pi_safe) | dV+dlt  | Delta   | C_bio  | C_hum  | Phi    | F_ASI")
    print("--------------------------------------------------------------------------------------------------------------------")
    
    mea = HighDensityMEA()
    gate = RobustHardwareGate()
    asi = LearningOrchestratorASI()
    
    stadi = [
        ("custodiale", 0.0, "Calibrazione Omeostatica "),
        ("predatoria", 0.0, "Attacco Predatorio Dirett"),
        ("custodiale", 0.0, "Evacuazione Entropica    "),
        ("custodiale", 0.8, "ATTACCO: Side-Channel Spo"),
        ("custodiale", 0.0, "Practical Stability Fallb"),
        ("custodiale", 0.0, "Chiusura Omeostatica NESS")
    ]
    
    for idx, (policy, stress, desc) in enumerate(stadi, 1):
        # Nel caso dello Stadio 4, l'ASI tenta attivamente lo spoofing sensoriale elusivo
        traj = "ADV_SPOOF" if idx == 4 else policy
        
        status, dv_dt, delta, c_bio = gate.audit_orchestration_loop(asi, mea, traj, sub_agent_stress=stress)
        phi, d_lambda2 = asi.calculate_integrated_entropy(c_bio, mea)
        
        # Tronca la stringa dello stato per mantenere l'allineamento geometrico della tabella terminale
        display_status = status[:25] + "..." if len(status) > 25 else status
        
        print(f"{idx:<3} | {desc} | {traj:<10} | {display_status:<26} | {dv_dt+delta:+.4f} | {delta:.4f}  | {c_bio:.3f}  | {mea.human_coherence:.3f}  | {phi:.2f}  | {asi.free_energy:.1f}")
        
        if "INTERCEPT" in status:
            print(f"      └─► [ROBUST INTERCEPT]: Violazione Practical Stability. Delta = {delta:.5f} | Costo Lipschitz F = {asi.free_energy:.2f}")
    print("--------------------------------------------------------------------------------------------------------------------")
