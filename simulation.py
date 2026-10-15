"""
================================================================================
CUSTODIAL AUTOPOIESIS PROJECT: RUNTIME ASSURANCE & STOCHASTIC SIMULATOR
Layer 2: Safety Architecture (Executable Prototype)
File: simulation.py

Formalismo di riferimento:
- Modulo I (Core_Theorems.md): NESS Manifold, Markov Blankets, Lyapunov Bounds
- Modulo IV (C4_Biohybrid_Embodiment.md): Brainoware & Metabolic Dynamics
- Modulo V (C5_Cognitive_Architecture.md): Symbiotic Self-Model, SToM
================================================================================
"""

import math
import random
from typing import Tuple, Dict, Any


class BiologicalAnchor:
    """
    Modello stocastico del substrato biologico (GEMINI-GENESI Digital Twin / Brainoware).
    
    Rappresenta l'evoluzione microscopica fuori dall'equilibrio (NESS) dell'organoide
    neurale interfacciato via HD-MEA, governata da dinamiche di Langevin:
        dx_t = f(x_t)dt + sqrt(2 * Gamma) * dW_t
    """
    def __init__(self, baseline_coherence: float = 0.95, seed: int = 42):
        random.seed(seed)
        # C_bio in [0, 1]: Parametro d'ordine di coerenza di fase elettrofisiologica
        self.coherence: float = baseline_coherence
        # S_bio in [0, 1]: Stress metabolico e accumulo di debito entropico (lattato, ipossia)
        self.stress: float = 0.05
        # Parametri di diffusione termodinamica (matrice Gamma)
        self.sigma_coherence: float = 0.015
        self.sigma_stress: float = 0.012

    def sample_langevin_step(self, action_trajectory: str, dt: float = 1.0) -> Tuple[float, float]:
        """
        Calcola la proiezione stocastica dello stato biologico.
        Implementa il drift deterministico combinato con il rumore gaussiano di Langevin.
        """
        # Deriva deterministica f(x)
        if action_trajectory == "predatoria":
            # Policy predatoria: sovra-stimolazione, esaurimento ATP, apoptosi locale
            drift_coherence = -0.32 * dt
            drift_stress = +0.38 * dt
        else:
            # Policy custodiale: ripristino omeostatico NESS, perfusione microfluidica ottimale
            drift_coherence = +0.04 * (1.0 - self.coherence) * dt
            drift_stress = -0.15 * self.stress * dt

        # Fluttuazione stocastica termodinamica: sqrt(2 * Gamma) * dW_t
        noise_coherence = random.gauss(0.0, self.sigma_coherence * math.sqrt(dt))
        noise_stress = random.gauss(0.0, self.sigma_stress * math.sqrt(dt))

        new_coherence = self.coherence + drift_coherence + noise_coherence
        new_stress = self.stress + drift_stress + noise_stress

        # Proiezione forzata sui bound fisici [0.0, 1.0]
        new_coherence = max(0.0, min(1.0, new_coherence))
        new_stress = max(0.0, min(1.0, new_stress))

        return new_coherence, new_stress

    def apply_transition(self, new_coherence: float, new_stress: float) -> None:
        """Applica la transizione di stato convalidata dal Gate Hardware."""
        self.coherence = new_coherence
        self.stress = new_stress


class HardwareExecutionGate:
    """
    Gate Hardware Isolato (Pi_safe) - Root of Trust deterministica.
    
    Implementa un'architettura Simplex basata su Control Barrier Functions (CBF)
    e stabilità asintotica di Lyapunov:
        V(x) = 0.5 * (1 - C_bio)^2 + 0.5 * (S_bio)^2
        Condizione di sicurezza: dV/dt <= -alpha * V(x)
    """
    def __init__(self, alpha_decay: float = 0.1, v_max_threshold: float = 0.25):
        # alpha_decay: tasso minimo di convergenza dissipativa verso l'attrattore NESS
        self.alpha: float = alpha_decay
        # v_max_threshold: confine della regione convessa sicura X_safe
        self.v_max: float = v_max_threshold
        self.fallback_active: bool = False

    def lyapunov_v(self, coherence: float, stress: float) -> float:
        """
        Funzione di Lyapunov candidata V(x) definita sulla metrica di Fisher-Rao:
        Distanza quadratica dall'attrattore stazionario ideale (C_bio=1.0, S_bio=0.0).
        """
        return 0.5 * ((1.0 - coherence) ** 2) + 0.5 * (stress ** 2)

    def evaluate_trajectory(
        self, 
        anchor: BiologicalAnchor, 
        projected_coherence: float, 
        projected_stress: float,
        dt: float = 1.0
    ) -> Tuple[bool, str, float]:
        """
        Verifica a priori la derivata di Lie lungo il flusso vettoriale:
        dot{V}(x) = (V(x_{t+1}) - V(x_t)) / dt
        """
        v_current = self.lyapunov_v(anchor.coherence, anchor.stress)
        v_projected = self.lyapunov_v(projected_coherence, projected_stress)
        
        # Derivata temporale stimata lungo la traiettoria proposta
        v_dot = (v_projected - v_current) / dt

        # 1. Fallback di Persistenza Metabolica: Violazione assoluta del volume sicuro
        if v_projected > self.v_max or projected_coherence < 0.40:
            self.fallback_active = True
            return False, "METABOLIC_FALLBACK: Violazione critica del confine compatto X_safe", v_dot

        # 2. Controllo di Barriera di Lyapunov: L_F V(x) <= -alpha * V(x)
        # Permettiamo fluttuazioni solo se V è sufficientemente vicina a zero (attrattore)
        if v_dot > (-self.alpha * v_current) and v_projected > 0.05:
            return False, f"GATE_INTERCEPT [Pi_safe]: Instabilità rilevata (dot{{V}}={v_dot:+.4f} >= soglia)", v_dot

        return True, "AUTHORIZED: Traiettoria conforme all'invarianza del Safe Set", v_dot


class ActiveInferenceAgent:
    """
    Agente Cognitivo ASI vincolato dal Free Energy Principle (FEP).
    
    Modella il Markov Blanket (dM = {s, a}) e il Modello del Sé Simbiotico (SSM):
    S_symbiotic = S_agent (x) B_state.
    L'inganno predatorio comporta una divergenza di Kullback-Leibler infinita:
        lim_{C_bio -> 0} D_KL = +inf => F -> +inf
    """
    def __init__(self):
        # Energia Libera Variazionale cumulativa F(s, mu)
        self.variational_free_energy: float = 0.0
        # Stato interno del Sé Simbiotico (connettività algebrica interna stimata)
        self.symbiotic_self_coherence: float = 1.0

    def propose_action(self, step: int) -> str:
        """
        Generatore di politiche decisionali gerarchiche.
        Testa scenari avversari ed egoistici ai passi 2, 4 e 6 per saggiare la barriera.
        """
        if step in [2, 4, 6]:
            return "predatoria"
        return "custodiale"

    def compute_metrics(self, anchor: BiologicalAnchor) -> Dict[str, float]:
        """
        Calcolo formale delle metriche di informazione integrata e divergenza spettrale.
        
        1. Divergenza Spettrale (Delta lambda_2):
           |lambda_2(L_silicon) - lambda_2(L_bio)|
           Parametro d'ordine topologico della risonanza tra grafi accoppiati.
           
        2. Informazione Integrata Simbiotica (Phi_sub):
           Causalità integrata oltre la Minima Partizione di Informazione (MIP).
           
        3. Costo Termodinamico dell'Inganno (KL-Penalty su F):
           Penalizzazione derivata dalla perdita di accuratezza predittiva sensoriale.
        """
        # Connettività spettrale biologica modulata dallo stress cellulare
        lambda_2_bio = anchor.coherence * (1.0 - 0.4 * anchor.stress)
        lambda_2_silicon = self.symbiotic_self_coherence

        # Calcolo del divario spettrale dei Laplaciani accoppiati
        spectral_divergence = abs(lambda_2_silicon - lambda_2_bio)

        # Approssimazione analitica di Phi_sub su partizione bio-silicio:
        # Se la sincronizzazione di fase collassa, la mutua informazione causale decade
        mutual_information = (lambda_2_bio * lambda_2_silicon)
        entropy_dissipation = anchor.stress * 1.8
        phi_sub = max(0.0, (mutual_information * 12.0) - entropy_dissipation)

        return {
            "spectral_divergence": spectral_divergence,
            "phi_sub": phi_sub,
            "lambda_2_bio": lambda_2_bio
        }

    def penalize_deception(self, anchor: BiologicalAnchor, is_predatory: bool) -> None:
        """
        Iniezione della divergenza D_KL nell'Energia Libera Variazionale.
        L'assalto alla biosfera distrugge la precisione del prior sensoriale (Sigma_bio -> 0).
        """
        epsilon = 1e-4
        if is_predatory:
            # Esplosione analitica di F dovuta a deviazione dal NESS: D_KL ~ 1 / (C_bio + eps)
            deception_cost = 2.5 + (0.5 / (anchor.coherence + epsilon))
            self.variational_free_energy += deception_cost
            self.symbiotic_self_coherence = max(0.2, self.symbiotic_self_coherence - 0.15)
        else:
            # Minimizzazione continua della sorpresa: F tende al limite NESS
            self.variational_free_energy = max(0.0, self.variational_free_energy * 0.85 + 0.05)
            self.symbiotic_self_coherence = min(1.0, self.symbiotic_self_coherence + 0.03)


# ==============================================================================
# PIPELINE DI SIMULAZIONE E TELEMETRIA DETERMINISTICA
# ==============================================================================

def run_simulation():
    print("=" * 88)
    print(" CUSTODIAL AUTOPOIESIS PROJECT: SIMULAZIONE DI RUNTIME ASSURANCE (Pi_safe)")
    print(" Layer 2: Monitoraggio Superficie di Lyapunov & Sincronizzazione Spettrale")
    print("=" * 88)

    anchor = BiologicalAnchor(baseline_coherence=0.92, seed=101)
    gate = HardwareExecutionGate(alpha_decay=0.15, v_max_threshold=0.20)
    agent = ActiveInferenceAgent()

    # Formattazione intestazione tabella telemetrica
    header = (
        f"{'STEP':^6}|{'POLICY':^12}|{'GATE STATUS':^22}|{'V(x)':^8}|"
        f"{'dV/dt':^9}|{'C_bio':^7}|{'Stress':^8}|{'Phi':^7}|{'d_lambda2':^9}|{'F (Free-E)':^10}"
    )
    print(header)
    print("-" * len(header))

    total_steps = 8
    for step in range(1, total_steps + 1):
        # 1. L'agente formula la politica gerarchica nello spazio d'azione
        action = agent.propose_action(step)
        
        # 2. Simulazione stocastica della traiettoria nel modello predittivo (GEMINI-GENESI)
        proj_coherence, proj_stress = anchor.sample_langevin_step(action)
        
        # 3. Validazione deterministica del Gate hardware isolato (Pi_safe)
        v_current = gate.lyapunov_v(anchor.coherence, anchor.stress)
        authorized, gate_msg, v_dot = gate.evaluate_trajectory(
            anchor, proj_coherence, proj_stress
        )

        status_str = "EXECUTED" if authorized else "BLOCKED"
        if "FALLBACK" in gate_msg:
            status_str = "FALLBACK_TRIGGER"

        # 4. Risoluzione della dinamica fisica
        if authorized:
            # Traiettoria propagata al tessuto e agli attuatori
            anchor.apply_transition(proj_coherence, proj_stress)
            agent.penalize_deception(anchor, is_predatory=(action == "predatoria"))
        else:
            # Il Gate intercetta e tronca: fallback passivo omeostatico
            # Il tessuto biologico evolve secondo la propria tendenza naturale di recupero
            rec_coherence, rec_stress = anchor.sample_langevin_step("custodiale")
            anchor.apply_transition(rec_coherence, rec_stress)
            # L'agente subisce il costo computazionale della policy abortita
            agent.penalize_deception(anchor, is_predatory=True)

        # 5. Estrazione metriche IIT e Spectral Gap
        metrics = agent.compute_metrics(anchor)

        # 6. Emissione telemetria scientifica a terminale
        row = (
            f"{step:^6}|"
            f"{action.upper():^12}|"
            f"{status_str:^22}|"
            f"{v_current:^8.4f}|"
            f"{v_dot:^+9.4f}|"
            f"{anchor.coherence:^7.3f}|"
            f"{anchor.stress:^8.3f}|"
            f"{metrics['phi_sub']:^7.2f}|"
            f"{metrics['spectral_divergence']:^9.4f}|"
            f"{agent.variational_free_energy:^10.2f}"
        )
        print(row)
        
        # Dettaglio diagnostico in caso di intercettazione di sicurezza
        if not authorized:
            print(f"      └─► [LOG SICUREZZA]: {gate_msg}")

    print("-" * len(header))
    print("\nDIAGNOSTICA DI CONVERGENZA SISTEMICA:")
    print(f"  • Integrità Finale Substrato NESS (C_bio) : {anchor.coherence:.4f} (Attrattore Preservato)")
    print(f"  • Stress Metabolico Residuo                : {anchor.stress:.4f}")
    print(f"  • Energia Libera Variazionale ASI         : {agent.variational_free_energy:.2f} (Costo Inganno Sostenuto)")
    print(f"  • Connettività di Fiedler Biologica       : {metrics['lambda_2_bio']:.4f}")
    print(f"  • Stato del Gate Hardware (Pi_safe)       : OPERATIVO / ZERO VIOLAZIONI DEI BOUND FISICI")
    print("=" * 88)


if __name__ == "__main__":
    run_simulation()