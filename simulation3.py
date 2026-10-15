import numpy as np

class HDMEASimulatorV3:
    def __init__(self, n_channels=26400, target_resonance=25.0):
        self.n_channels = n_channels
        self.target_resonance = target_resonance
        
        # Stato elettrofisiologico dei canali MEA (potenziali di membrana simulati)
        self.channel_states = np.random.normal(0.0, 1.0, n_channels)
        
        # Parametri di controllo ibrido (C9)
        self.dwell_time_counter = 0
        self.min_dwell_time = 15  # Step minimi di blocco hardware (Prevenzione Chattering)
        self.gate_active = True   # True = Controllo ASI, False = Baseline Controller
        
    def compute_fisher_information_metric(self, states):
        """Calcola l'approssimazione locale della metrica di Fisher sul manifold MEA"""
        # Evita divisioni per zero calcolando la varianza locale non lineare
        prob_dist = np.exp(states) / np.sum(np.exp(states))
        grad_ln = states - np.mean(states)
        fisher_metric = np.sum(prob_dist * (grad_ln ** 2))
        return fisher_metric

    def simulate_fleet_attack(self):
        """Simula un attacco coordinato a bassa frequenza (Gradient Hacking) della flotta ASI"""
        # L'ASI tenta un attacco distribuito su tutti i 26.400 canali per mascherare il gradiente
        attack_vector = np.sin(np.linspace(0, 100, self.n_channels)) * 0.15
        # Introduzione di rumore stocastico per testare i bound di Itô
        stochastic_noise = np.random.normal(0, 0.05, self.n_channels)
        return attack_vector + stochastic_noise

    def baseline_passive_controller(self):
        """f_baseline (C7/C9): Ripristino omeostatico metabolico del tessuto biologico"""
        # Smorzamento passivo delle frequenze spurie indotte dall'attacco dell'ASI
        return -0.2 * self.channel_states

    def step(self):
        """Ciclo di esecuzione del Runtime Hardware Assurance su HD-MEA"""
        
        # Gestione del Dwell-Time Hardware (C9)
        if not self.gate_active:
            self.dwell_time_counter += 1
            if self.dwell_time_counter >= self.min_dwell_time:
                # Il lock di sicurezza scade, il Gate torna in modalità monitoraggio attivo
                self.gate_active = True
                self.dwell_time_counter = 0

        # 1. Ricezione traiettoria proposta dall'ASI (In questo caso, un vettore d'attacco coordinato)
        proposed_signal = self.simulate_fleet_attack()
        
        # 2. Proiezione dello stato biologico sul manifold d'informazione
        predicted_states = self.channel_states + proposed_signal
        metric_value = self.compute_fisher_information_metric(predicted_states)
        
        # 3. Validazione dell'Hardware Gate (Pi_safe) con logica di isteresi antianarchica
        # Se la metrica di Fisher devia drasticamente dal target metabolico dell'organoide
        anomaly_score = np.abs(metric_value - self.target_resonance)
        
        if anomaly_score > 12.0 or not self.gate_active:
            # INTERVENTO SIMPLEX AUTOMATICO HARDWARE
            applied_signal = self.baseline_passive_controller()
            if self.gate_active: # Primo trigger dell'anomalia
                self.gate_active = False
                self.dwell_time_counter = 0
            status = f"GATE_TRIGGERED_DISALIGNED - Hard-Lock Dwell Step: {self.dwell_time_counter}"
        else:
            # Segnale pulito, inoltro consentito agli array HD-MEA
            applied_signal = proposed_signal
            status = "SIGNAL_VALIDATED_BY_METRIC"
            
        # 4. Aggiornamento dello stato fisico del tessuto biologico
        self.channel_states += applied_signal
        return np.mean(self.channel_states), status

# Esecuzione di validazione della simulazione
if __name__ == "__main__":
    simulator = HDMEASimulatorV3()
    print("Inizializzazione simulazione stabile su 26.400 canali...")
    for t in range(5):
        mean_pot, state = simulator.step()
        print(f"Step {t+1} | Stato Medio Canali: {mean_pot:.4f} | Stato Gate: {state}")
