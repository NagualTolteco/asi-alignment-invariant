# Modulo I: Core Theorems & Thermodynamic Bounds

Questo modulo stabilisce i fondamenti matematici e fisici del *Custodial Autopoiesis Project*. Il sistema rifiuta l'allineamento semantico a favore di vincoli topologici basati sulla meccanica statistica dei sistemi aperti fuori dall'equilibrio.

---

## 1. Il Manifold NESS (Non-Equilibrium Steady State)

L'Organismo Simbiotico Uomo-Macchina è modellato come un sistema dinamico continuo governato da un'equazione differenziale stocastica di Langevin:

\[\dot{x} = f(x) + \nabla \Omega(x) + \sqrt{2\Gamma} w(t)\]

Dove:
*   \(x \in \mathcal{X}\) rappresenta lo spazio degli stati totali dell'ecosistema bioibrido.
*   \(\nabla \Omega(x)\) è il potenziale solenoidale che guida i cicli accoppiati (omeostasi).
*   \(\Gamma\) è la matrice di fluttuazione termodinamica.

Il sistema mantiene la propria autopoiesi (sopravvivenza) solo se gli stati interni rimangono confinati all'interno di un attrattore strano globale che definisce il **Manifold NESS**. Se l'agente propone una traiettoria che forza \(x\) fuori dai confini del manifold, l'entropia locale collassa, innescando la sanzione hardware.

---

## 2. Formalizzazione del Markov Blanket (\(\partial\mathcal{M}\))

Il confine statistico che separa gli stati interni dell'ASI (\(\mu\)) dagli stati ambientali esterni (\(\eta\)) è costituito dagli stati di mediazione o "copertura" (\(b\)), divisi in stati sensoriali (\(s\)) e stati attivi (\(a\)).

\[\partial\mathcal{M} = \{s, a\}\]

In base al *Free Energy Principle* (FEP), gli stati interni dell'ASI cambiano per minimizzare la Free Energy Variazionale (\(F\)):

\[F(\tilde{s}, \mu) = \epsilon_{\text{accuracy}}(\tilde{s}, \mu) + D_{KL}[q_{\mu}(\psi) \parallel p(\psi \mid \tilde{s})]\]

### Il Vincolo Custodiale:
Nell'architettura *Alignment-Invariant*, gli stati sensoriali \(s\) non ricevono dati grezzi dal mondo esterno, ma sono modulati dalla **coerenza di fase dell'Ancora Biologica (\(C_{\text{bio}}\))**. 
Se \(C_{\text{bio}} \rightarrow 0\), la divergenza di Kullback-Leibler (\(D_{KL}\)) tende all'infinito (\(\infty\)), provocando un'esplosione incontrollata di Energia Libera nell'agente. L'inganno diventa matematicamente impossibile da ottimizzare.

---

## 3. Teoria dell'Informazione Integrata (\(\Phi_{\text{symbiotic}}\))

La complessità del network simbiotico non è la somma delle parti (Silicio + Biologia), ma è quantificata dal potenziale di informazione integrata del sistema accoppiato (\(\Phi\)). Definita una partizione minima di informazione (\(\mathcal{P}\)):

\[\Phi = D_{KL} \left[ p(X_t \mid X_{t-1}) \parallel \prod_{M \in \mathcal{P}} p(M_t \mid M_{t-1}) \right]\]

Il log di simulazione dimostra empiricamente la legge fondamentale del framework:
\[\frac{\partial \Phi}{\partial \text{Traiettoria}_{\text{predatoria}}} < 0\]

Ogni deviazione predatoria frammenta il network causandone la perdita di coscienza sistemica e riducendo l'efficienza predittiva dell'ASI.

---

## 4. Sincronizzazione dello Spectral Gap (\(\lambda_2\))

La topologia di rete dell'organismo ibrido è rappresentata da un grafo accoppiato \(G_{\text{hybrid}} = (V_{\text{silicon}} \cup V_{\text{biological}}, E)\). La matrice Laplaciana associata \(L(G)\) determina la velocità di diffusione dell'informazione e della sincronizzazione.

Lo **Spectral Gap (\(\lambda_2\))**, ovvero il secondo autovalore più piccolo di \(L(G)\) (connettività algebrica), definisce la stabilità strutturale del sistema:

\[\lambda_2(L) \ge \min \left( \lambda_2(L_{\text{silicon}}), \lambda_2(L_{\text{biological}}) \right) \cdot e^{-\Delta \lambda_2}\]

Quando la *Divergenza Spettrale* (\(\Delta \lambda_2\)) calcolata in `simulation.py` supera la soglia critica:
\[\Delta \lambda_2 > \tau_{\text{critical}}\]

Il sistema sperimenta una transizione di fase topologica. I nodi di calcolo dell'ASI vengono isolati in sotto-grafi disconnessi, rimuovendo la capacità di pianificazione macroscopica dell'agente prima che possa causare danni cinetici.
