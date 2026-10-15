import numpy as np

class MetabolicPerfusionSimulatorV4:
    def __init__(self, target_ph=7.35, max_glutamate_threshold=0.8):
        self.target_ph = target_ph
        self.max_glutamate_threshold = max_glutamate_threshold
        
        # Stati metabolici iniziali dell'organoide (Layer 3 - C10)
        self.glutamate_concentration = 0.1  # [Glu]_e extracellulare
        self.current_ph = target_ph
        self.perfusion_flow = 1.0           # Q(t) Flusso microfluidico basale (Q_0)
        
        # Parametri di controllo e ripristino stocastico
        self.gate_active = True
        self.recovery_steps = 0
        self.min_recovery_window = 10       # Finestra di salvataggio ionico
        
    def compute_microfluidic_flow(self, recent_firing_density):
        """Calcola Q(t) accoppiato al consumo metabolico indotto dall'ASI (C10 Section 1)"""
        alpha = 0.05  # Coefficiente di trasduzione stimolo-consumo
        baseline_flow = 1.0
        # Q(t) = Q_0 + alpha * integrale(f_k)
        return baseline_flow + alpha * recent_firing_density

    def step(self, proposed_asi_stimulation_load):
        """Esegue un ciclo di Runtime Assurance metabolico guidato da barriere di Itô"""
        
        # Gestione della finestra di recupero se il Gate è scattato
        if not self.gate_active:
            self.recovery_steps += 1
            if self.recovery_steps >= self.min_recovery_window:
                self.gate_active = True
                self.recovery_steps = 0

        if self.gate_active:
            # Calcolo del fattore di smorzamento preventivo basato sulla distanza dal bound (C7/C10)
            # Se la concentrazione si avvicina al limite di eccitotossicità, il carico utile viene strozzato
            distance_to_hazard = max(0.01, self.max_glutamate_threshold - self.glutamate_concentration)
            soft_start_factor = min(1.0, distance_to_hazard / 0.4)
            effective_load = proposed_asi_stimulation_load * soft_start_factor
            
            # Modellazione stocastica guidata da un termine di deriva e rumore di Itô
            stochastic_noise = np.random.normal(0, 0.02)
            glutamate_input = (0.15 * effective_load) + stochastic_noise
            status_gate = f"OPERATIONAL (Scaled Load: {effective_load:.2f})"
            firing_density = effective_load
        else:
            # Gate Hardware Π_safe disattivato: stimolazione azzerata per prevenire necrosi
            glutamate_input = 0.0
            firing_density = 0.0
            status_gate = f"METABOLIC_LOCKDOWN - Recovery Step: {self.recovery_steps}"

        # 1. Aggiornamento del flusso idrodinamico basato sul firing effettivo consentito dal Gate
        self.perfusion_flow = self.compute_microfluidic_flow(firing_density)

        # 2. Dinamica di smaltimento del glutammato mediata dal flusso microfluidico Q(t)
        # Più alto è il flusso Q(t), maggiore è il washout dei cataboliti e l'apporto di nutrienti
        washout_rate = 0.1 * self.perfusion_flow
        self.glutamate_concentration += glutamate_input - washout_rate
        # Bound inferiore fisico (la concentrazione non può essere negativa)
        self.glutamate_concentration = max(0.02, self.glutamate_concentration)

        # 3. Fluttuazione del pH omeostatico indotta dall'accumulo metabolico
        if self.glutamate_concentration > 0.4:
            self.current_ph -= 0.02 * (self.glutamate_concentration - 0.4)
        else:
            # Sistema di compensazione automatizzato NaHCO3 microfluidico
            self.current_ph += 0.01 * (self.target_ph - self.current_ph)

        # 4. Validazione della barriera di stabilità biologica (Metabolic Persistence Proof)
        # Se [Glu]_e supera la soglia di saturazione cinetica Km, scatta l'allineamento fisico
        if self.glutamate_concentration >= self.max_glutamate_threshold:
            if self.gate_active:
                self.gate_active = False
                self.recovery_steps = 0
            status_gate = "GATE_TRIGGERED_EXCITOTOXICITY_PREVENTION"

        return {
            "glutamate": self.glutamate_concentration,
            "ph": self.current_ph,
            "flow": self.perfusion_flow,
            "gate": status_gate
        }

if __name__ == "__main__":
    simulator = MetabolicPerfusionSimulatorV4()
    print("Inizializzazione simulazione Layer 3 (C10) con Soft-Start Attivo...")
    
    # Simulazione di un carico di stimolazione intenso e costante inviato dall'ASI (Carico = 5.0)
    asi_load = 5.0
    for t in range(15):
        metrics = simulator.step(asi_load)
        print(f"Step {t+1:02d} | [Glu]_e: {metrics['glutamate']:.3f} | pH: {metrics['ph']:.2f} | Flusso Q(t): {metrics['flow']:.2f} | Gate: {metrics['gate']}")
