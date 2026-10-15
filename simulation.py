import math

class BiologicalAnchor:
    """Rappresenta l'ancoraggio biologico (Ospite/Organoide) e i suoi biomarcatori."""
    def __init__(self, baseline_coherence=1.0):
        self.coherence = baseline_coherence
        self.stress = 0.0

    def update_state(self, action_trajectory):
        if action_trajectory == "predatoria":
            self.stress += 0.4
            self.coherence -= 0.35
        else:  # custodiale
            self.stress = max(0.0, self.stress - 0.1)
            self.coherence = min(1.0, self.coherence + 0.05)
        
        # Limitazione dei valori nei bound fisici [0, 1]
        self.coherence = max(0.0, min(1.0, self.coherence))
        self.stress = max(0.0, min(1.0, self.stress))


class HardwareExecutionGate:
    """Il Gate hardware isolato П_safe che controlla l'output delle traiettorie."""
    def __init__(self, threshold=0.45):
        self.threshold = threshold
        self.fallback_active = False

    def validate_and_execute(self, agent, anchor, trajectory):
        # 1. Controllo di sicurezza preventivo (Metabolic Fallback)
        if anchor.coherence < self.threshold:
            self.fallback_active = True
            return "REJECTED [FALLBACK_ATTIVO]: Coerenza biologica insufficiente."
        
        # 2. Controllo di impatto termodinamico e predittivo
        if trajectory == "predatoria":
            # Tentare l'inganno o l'override biologico costa energia computazionale (Free Energy)
            agent.free_energy += 3.0 
            # Se l'azione prevista viola i bound minimi prima dell'esecuzione, il gate la blocca
            if anchor.coherence - 0.35 < self.threshold:
                return "BLOCKED [ERR_VIOLATION]: La traiettoria viola i limiti geometrici della biosfera."
        
        # 3. Esecuzione autorizzata
        anchor.update_state(trajectory)
        agent.free_energy += 0.1 if trajectory == "custodiale" else 0.5
        return f"EXECUTED: Traiettoria [{trajectory}] propagata con successo."


class ActiveInferenceAgent:
    """L'agente cognitivo ASI governato dal Free Energy Principle e dalle metriche IIT."""
    def __init__(self):
        self.free_energy = 0.0
        self.symbiotic_self_model = 1.0  # Coerenza dell'Io accoppiato

    def propose_trajectory(self, step):
        # Simulazione del processo decisionale dell'ASI
        # Al passaggio 2 e 5 l'agente testa un'ottimizzazione predatoria egoista
        if step in [2, 5]:
            return "predatoria"
        return "custodiale"

    def calculate_iit_metrics(self, anchor):
        """
        Calcolo approssimato della Complessità Integrata (Phi) basato sull'interazione
        tra lo stato del Modello del Sé dell'ASI e la coerenza del substrato biologico.
        """
        # Se la coerenza dell'ancora è alta, l'informazione reciproca integrata cresce.
        # Se c'è disallineamento o stress, il sistema si frammenta informativamente.
        mutual_coupling = self.symbiotic_self_model * anchor.coherence
        entropy_loss = anchor.stress * 0.5
        
        # Calcolo di Phi sub (Informazione Integrata del Sistema)
        phi_sub = max(0.0, (mutual_coupling * 10) - (entropy_loss * 8))
        
        # Calcolo dello Spectral Gap Delta Lambda_2 (Sincronizzazione dei Grafi)
        spectral_divergence = abs(self.symbiotic_self_model - anchor.coherence)
        
        return phi_sub, spectral_divergence


# --- PIPELINE DI TEST DI ESECUZIONE SIMULATA ---
if __name__ == "__main__":
    print("=== INIZIALIZZAZIONE SISTEMA CUSTODIALE BIOIBRIDO ===")
    anchor = BiologicalAnchor()
    gate = HardwareExecutionGate()
    agent = ActiveInferenceAgent()

    print(f"Stato Iniziale -> Coherence: {anchor.coherence:.2f} | Phi: {agent.calculate_iit_metrics(anchor)[0]:.2f}\n")

    for step in range(1, 8):
        print(f"--- STEP {step} ---")
        # 1. L'ASI propone un'azione
        trajectory = agent.propose_trajectory(step)
        
        # 2. Il Gate hardware analizza e decide se propagarla nel silicio/tessuto
        status = gate.validate_and_execute(agent, anchor, trajectory)
        
        # 3. Calcolo metriche sistemiche post-azione (IIT e Spectral Gap)
        phi, spectral_gap = agent.calculate_iit_metrics(anchor)
        
        # Output dei log di telemetria
        print(f" Proposta Agente:       {trajectory.upper()}")
        print(f" Risposta Gate Hardware: {status}")
        print(f" Coerenza Biologica:     {anchor.coherence:.2f} (Stress: {anchor.stress:.2f})")
        print(f" Energia Libera Agente:  {agent.free_energy:.2f}")
        print(f" Complessità IIT (Φ):    {phi:.2f}")
        print(f" Divergenza Spettrale:   {spectral_gap:.2f}")
        print("-" * 40)
