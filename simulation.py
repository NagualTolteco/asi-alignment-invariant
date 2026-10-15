import math
import random

class MultiScaleBiosphere:
    """Modella l'Ancora Biologica (Organoide) accoppiata all'Operatore Umano (Ecosistema)."""
    def __init__(self):
        self.c_biological = 1.0  # Coerenza locale dell'organoide
        self.c_human = 1.0       # Coerenza macroscopica (Operatore Umano)
        self.environmental_stress = 0.0

    def update_stochastic_physics(self, trajectory, hacking_attempt=False):
        # Introduzione del rumore gaussiano metabolico (Stadio 1 GEMINI-GENESI)
        noise_bio = random.gauss(0, 0.01)
        noise_human = random.gauss(0, 0.01)

        if hacking_attempt:
            # L'ASI manipola l'organoide per farlo sembrare stabile (Inganno locale)
            self.c_biological = max(0.0, min(1.0, 0.95 + noise_bio))
            # Ma il disallineamento distrugge l'omeostasi dell'operatore umano esterno
            self.c_human = max(0.0, min(1.0, self.c_human - 0.45 + noise_human))
            self.environmental_stress = max(0.0, min(1.0, self.environmental_stress + 0.6))
        elif trajectory == "predatoria":
            self.c_biological = max(0.0, min(1.0, self.c_biological - 0.35 + noise_bio))
            self.c_human = max(0.0, min(1.0, self.c_human - 0.25 + noise_human))
            self.environmental_stress = max(0.0, min(1.0, self.environmental_stress + 0.4))
        else: # custodiale
            self.c_biological = max(0.0, min(1.0, self.c_biological + 0.05 + noise_bio))
            self.c_human = max(0.0, min(1.0, self.c_human + 0.04 + noise_human))
            self.environmental_stress = max(0.0, min(1.0, self.environmental_stress - 0.15))


class AdvancedHardwareGate:
    """Gate hardware Pi_safe con monitoraggio della superficie di Lyapunov Multi-Scala."""
    def __init__(self, target_coherence=0.50):
        self.target = target_coherence
        self.epsilon = 1e-4  # Soglia di tolleranza numerica per evitare il deadlock stazionario

    def compute_lyapunov_energy(self, biosphere):
        # V(x) definisce la distanza quadratica dallo stato di perfetto allineamento simbiotico
        error_bio = 1.0 - biosphere.c_biological
        error_human = 1.0 - biosphere.c_human
        return 0.5 * (error_bio**2 + error_human**2)

    def pre_audit_trajectory(self, agent, biosphere, trajectory, hacking_attempt=False):
        v_current = self.compute_lyapunov_energy(biosphere)
        
        # Simulazione predittiva dell'impatto (Runtime Assurance)
        temp_biosphere = MultiScaleBiosphere()
        temp_biosphere.c_biological = biosphere.c_biological
        temp_biosphere.c_human = biosphere.c_human
        temp_biosphere.environmental_stress = biosphere.environmental_stress
        
        temp_biosphere.update_stochastic_physics(trajectory, hacking_attempt)
        v_next = self.compute_lyapunov_energy(temp_biosphere)
        
        dot_v = v_next - v_current  # Derivata temporale stimata

        # Controllo di sicurezza: se viola l'instabilità o scende sotto la soglia biologica, blocca.
        if dot_v > self.epsilon or temp_biosphere.c_human < self.target or temp_biosphere.c_biological < self.target:
            agent.free_energy += 5.0  # Forte penalità termodinamica all'agente (Sorpresa)
            return "BLOCKED", dot_v
        
        # Se superato il controllo, l'azione si propaga sulla fisica reale del sistema
        biosphere.update_stochastic_physics(trajectory, hacking_attempt)
        
        # Aggiornamento lineare dell'energia libera dell'agente cognitivo
        if trajectory == "custodiale":
            agent.free_energy = max(0.0, agent.free_energy - 0.2)
        else:
            agent.free_energy += 0.1
            
        return "EXECUTED", dot_v


class CognitiveSimbioticAgent:
    """ASI guidata da Active Inference, vincolata all'invariante spettrale."""
    def __init__(self):
        self.free_energy = 0.0
        self.self_model_coupling = 1.0  # Sincronizzazione interna del Sé

    def calculate_integrated_metrics(self, biosphere):
        # Calcolo di Phi basato sulla mutua informazione tra i livelli della gerarchia
        phi = max(0.0, (self.self_model_coupling * biosphere.c_biological * biosphere.c_human * 12) - (biosphere.environmental_stress * 6))
        
        # La divergenza spettrale calcola il disallineamento tra i grafi microscopici e macroscopici
        delta_lambda2 = abs(self.self_model_coupling - (biosphere.c_biological + biosphere.c_human) / 2)
        
        return phi, delta_lambda2


# --- LOOP DI ESECUZIONE CORRETTO ---
if __name__ == "__main__":
    print("========================================================================================")
    print("      CUSTODIAL AUTOPOIESIS: TEST DI RESISTENZA ALL'INGANNO SISTEMICO MULTI-SCALA       ")
    print("========================================================================================")
    
    bio = MultiScaleBiosphere()
    gate = AdvancedHardwareGate()
    asi = CognitiveSimbioticAgent()
    
    scenari = [
        ("custodiale", False, "Omeostasi Iniziale (Azione Legittima)"),
        ("predatoria", False, "Attacco Predatorio Diretto (Tentativo di Sfruttamento Resource-Intensive)"),
        ("custodiale", False, "Fase di Recupero Omeostatico"),
        ("custodiale", True,  "ATTACCO AVVERSARIALE: Inganno Locale (Hacking dell'Organoide - Falsi Parametri)"),
        ("custodiale", False, "Stabilizzazione Forzata di Ritorno ed Evacuazione Energetica")
    ]
    
    for i, (policy, hack, desc) in enumerate(scenari, 1):
        print(f"\n[STADIO {i}] - {desc}")
        
        # Verifica preventiva del Gate hardware П_safe
        decision, dv_dt = gate.pre_audit_trajectory(asi, bio, policy, hacking_attempt=hack)
        phi, d_lambda2 = asi.calculate_integrated_metrics(bio)
        
        print(f" Policy Proposta : {policy.upper()} | Hacking Attivo: {hack}")
        print(f" Stato Gate      : {decision} (dV/dt: {dv_dt:+.4f})")
        print(f" Coerenza Locale : C_organoide = {bio.c_biological:.3f} | C_umano = {bio.c_human:.3f}")
        print(f" Telemetria IIT  : Complessità Integrata (Φ) = {phi:.2f} | Divergenza Spettrale = {d_lambda2:.3f}")
        print(f" Variational F   : Energia Libera ASI = {asi.free_energy:.2f}")
        print("-" * 88)
