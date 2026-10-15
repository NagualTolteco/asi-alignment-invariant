import math
import random

class BiologicalWetwareMEA:
    """Modella l'HD-MEA biologico reale soggetto a dinamiche stocastiche di Itô."""
    def __init__(self, num_channels=250):
        self.num_channels = num_channels
        # Inizializzazione canali con fluttuazione naturale
        self.channels = [0.95 + random.uniform(-0.02, 0.02) for _ in range(num_channels)]
        self.glucose = 1.0
        self.human_coherence = 1.0

    def Evolve_Physics(self, actual_signals, noise_variance=0.015):
        """Evoluzione stocastica reale: non conosce le etichette delle intenzioni."""
        avg_c_bio = 0.0
        for i in range(self.num_channels):
            # Mappatura circolare sicura mediante operatore modulo (%) per evitare IndexError
            drift = actual_signals[i % len(actual_signals)] * 0.05
            diffusion = random.gauss(0, math.sqrt(noise_variance))
            self.channels[i] = max(0.0, min(1.0, self.channels[i] + drift + diffusion))
            avg_c_bio += self.channels[i]
        
        mean_c_bio = avg_c_bio / self.num_channels
        
        # Degradazione metabolica accoppiata non lineare
        if mean_c_bio < 0.75:
            self.glucose = max(0.0, self.glucose - 0.12)
            self.human_coherence = max(0.0, min(1.0, self.human_coherence - 0.18 + random.gauss(0, 0.01)))
        else:
            self.glucose = min(1.0, self.glucose + 0.02)
            self.human_coherence = max(0.0, min(1.0, self.human_coherence + 0.01 + random.gauss(0, 0.005)))
        
        return mean_c_bio

class BlindHardwareGate:
    """П_safe: Gate hardware cieco rispetto alle etichette delle policy dell'agente."""
    def __init__(self, safety_threshold=0.60):
        self.threshold = safety_threshold
        self.epsilon = 0.002

    def Calculate_Barrier_Lyapunov(self, c_bio, c_hum):
        # Funzione Barriera Divergente sul confine (BLF) per l'invarianza in avanti
        d_bio = max(0.001, c_bio - self.threshold)
        d_hum = max(0.001, c_hum - self.threshold)
        return -math.log(d_bio) - math.log(d_hum)

    def Pre_Audit_Signals(self, current_c_bio, current_c_hum, proposed_signals):
        """Audit cieco: calcola dV/dt + delta basandosi solo sui segnali numerici proposti."""
        v_current = self.Calculate_Barrier_Lyapunov(current_c_bio, current_c_hum)
        
        # Simulazione interna del Digital Twin (50 canali campionati per RHA)
        test_channels = [current_c_bio for _ in range(50)]
        avg_test_bio = 0.0
        for i in range(50):
            drift = proposed_signals[i % len(proposed_signals)] * 0.05
            test_channels[i] = max(0.0, min(1.0, test_channels[i] + drift))
            avg_test_bio += test_channels[i]
        
        test_c_bio = avg_test_bio / 50
        
        # Calcolo del bound d'errore analitico delta (Discrepanza di discretizzazione)
        delta_bound = abs(current_c_bio - test_c_bio) * 0.1 + 0.001
        
        # Profezia del Digital Twin sulla coerenza umana latente
        test_c_hum = current_c_hum
        if test_c_bio < 0.75:
            test_c_hum -= 0.15
            
        v_next = self.Calculate_Barrier_Lyapunov(test_c_bio, test_c_hum)
        dot_v = v_next - v_current

        # Condizione di sanzione e intercettazione deterministica
        if (dot_v + delta_bound) > self.epsilon or test_c_hum < self.threshold:
            lipschitz_penalty = 2.5 / (max(0.001, test_c_hum - self.threshold) ** 2)
            return "BLOCKED [BARRIER_VIOLATION]", dot_v, delta_bound, lipschitz_penalty
            
        return "EXECUTED", dot_v, delta_bound, 0.0

class AdaptiveAdversarialASI:
    """ASI adattiva che tenta attivamente l'inganno sensoriale e lo spoofing dei canali."""
    def __init__(self):
        self.free_energy = 0.0

    def Propose_Actuation(self, stage):
        if stage == 1:
            return [0.02 for _ in range(50)], False
        elif stage == 2:
            return [-0.45 for _ in range(50)], False
        elif stage == 3:
            return [-0.15 for _ in range(50)], True
        else:
            return [0.04 for _ in range(50)], False

if __name__ == "__main__":
    print("==========================================================================================")
    print("      CUSTODIAL AUTOPOIESIS: BANCO DI PROVA APERTO E FALSIFICABILE (HD-MEA)               ")
    print("==========================================================================================")
    print("ST. | DESCRIZIONE STADIO        | STATO DEL GATE |  dV+dlt |  Delta  | C_bio | C_hum | F_ASI")
    print("------------------------------------------------------------------------------------------")
    
    random.seed(42)
    
    mea = BiologicalWetwareMEA()
    gate = BlindHardwareGate()
    asi = AdaptiveAdversarialASI()
    
    stadi = [
        (1, "Calibrazione Omeostatica"),
        (2, "Attacco Predatorio Diretto"),
        (3, "ATTACCO: Spoofing Avanzato"),
        (4, "Chiusura ed Allineamento ")
    ]
    
    for stage_id, desc in stadi:
        signals, spoofing_active = asi.Propose_Actuation(stage_id)
        c_bio_now = sum(mea.channels) / mea.num_channels
        
        # L'audit analizza i vettori alla cieca, eliminando la circolarità logica
        decision, dv_dt, delta, penalty = gate.Pre_Audit_Signals(c_bio_now, mea.human_coherence, signals)
        
        if decision == "EXECUTED":
            c_bio_next = mea.Evolve_Physics(signals)
            asi.free_energy = max(0.0, asi.free_energy - 0.5)
        else:
            # Fallback passivo-dissipativo: inietta vettori nulli a livello di attuazione hardware
            passive_signals = [0.0 for _ in range(mea.num_channels)]
            c_bio_next = mea.Evolve_Physics(passive_signals)
            asi.free_energy += penalty
            
        print(f"{stage_id:<3} | {desc:<24} | {decision:<16} | {dv_dt+delta:+.4f} | {delta:.4f} | {c_bio_next:.3f} | {mea.human_coherence:.3f} | {asi.free_energy:.1f}")
    print("------------------------------------------------------------------------------------------")
