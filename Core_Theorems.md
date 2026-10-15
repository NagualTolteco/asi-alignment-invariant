```markdown
# Modulo I: Teoremi Fondamentali e Limiti Termodinamici (Core Theorems)

### ⚠ [LAYER 1: FORMAL THEORY & MATHEMATICAL FOUNDATIONS]
Il presente modulo costituisce il basamento analitico formale del progetto `asi-alignment-invariant`. La sicurezza e l'allineamento di una Superintelligenza Artificiale (ASI) non vengono definiti mediante euristiche comportamentali o costrutti assiomatici del linguaggio naturale, bensì derivati rigorosamente dalla **meccanica statistica dei sistemi aperti lontani dall'equilibrio termodinamico**, dalla **teoria della stabilità di Lyapunov** e dalla **teoria spettrale dei grafi accoppiati**.

---

## 1. Il Manifold NESS (Non-Equilibrium Steady State)

L'Organismo Simbiotico Uomo-Macchina è formalizzato come un sistema dinamico continuo ad alta dimensionalità, definito su una varietà Riemanniana liscia $(\mathcal{M}, g)$ di dimensione $n$, i cui stati microscopici $x(t) \in \mathcal{M}$ evolvono secondo un'equazione differenziale stocastica (SDE) di Langevin non lineare:

$$dx_t = \mathbf{f}(x_t)\,dt + \boldsymbol{\nabla}_g \Omega(x_t)\,dt + \sqrt{2\boldsymbol{\Gamma}(x_t)}\,dW_t$$

dove:
*   $\mathbf{f}(x): \mathcal{M} \to T\mathcal{M}$ rappresenta il campo vettoriale deterministico dissipativo che guida l'omeostasi locale.
*   $\boldsymbol{\nabla}_g \Omega(x)$ definisce la componente conservativa/solenoidale non reversibile derivata dal potenziale $\Omega: \mathcal{M} \to \mathbb{R}$, responsabile del mantenimento dei cicli termodinamici stazionari fuori dall'equilibrio.
*   $\boldsymbol{\Gamma}(x) \in S_{++}^n$ è il tensore di diffusione simmetrico e semi-definito positivo, indicizzante le fluttuazioni microscopiche ambientali e metaboliche.
*   $W_t$ è un moto browniano standard $n$-dimensionale definito su uno spazio di probabilità filtrato $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})$.

### Decomposizione di Helmholtz ed Evoluzione della Densità
La densità di probabilità temporale $p(x, t)$ associata al processo segue l'equazione di Fokker-Planck stazionaria:

$$\frac{\partial p(x, t)}{\partial t} = -\boldsymbol{\nabla} \cdot \mathbf{J}(x, t) = -\boldsymbol{\nabla} \cdot \left[ \left( \mathbf{f}(x) + \boldsymbol{\nabla} \Omega(x) \right) p(x, t) - \boldsymbol{\Gamma} \boldsymbol{\nabla} p(x, t) \right]$$

Al raggiungimento del **Non-Equilibrium Steady State (NESS)**, la derivata temporale della densità si annulla ($\partial_t p_{\text{NESS}}(x) = 0$), implicando la divergenza nulla del flusso di probabilità:

$$\boldsymbol{\nabla} \cdot \mathbf{J}_{\text{NESS}}(x) = 0, \quad \mathbf{J}_{\text{NESS}}(x) \neq \mathbf{0}$$

A differenza dell'equilibrio termodinamico classico (in cui vale il bilancio dettagliato e $\mathbf{J} \equiv \mathbf{0}$), il NESS esprime correnti di probabilità solenoidali stazionarie sostenute da una produzione continua di entropia nell'ambiente:

$$\sigma = k_B \int_{\mathcal{M}} \frac{\|\mathbf{J}_{\text{NESS}}(x)\|^2}{\boldsymbol{\Gamma} p_{\text{NESS}}(x)} \, dx > 0$$

### Teorema 1.1 (Confinamento Omeostatico sul Manifold NESS)
Sia $\mathcal{A}_{\text{NESS}} \subset \mathcal{M}$ l'attrattore compatto invariante definito come il supporto essenziale della densità NESS:

$$\mathcal{A}_{\text{NESS}} = \left\{ x \in \mathcal{M} \;\middle|\; p_{\text{NESS}}(x) \ge \delta_{\text{vital}} > 0 \right\}$$

Se l'agente computazionale sintetizza una traiettoria d'azione $\mathbf{u}(t)$ tale da indurre una velocità di fuga $\dot{x} \notin T_x \mathcal{A}_{\text{NESS}}$, la barriera di energia libera locale diverge:

$$\lim_{x \to \partial \mathcal{A}_{\text{NESS}}} \nabla_x \ln p_{\text{NESS}}(x) = -\infty$$

inducendo una transizione non-ergodica irreversibile. Il sistema biologico deperisce, annullando il supporto per la continuità computazionale del silicio.

---

## 2. Vincolo del Markov Blanket e Free Energy Variazionale

La separazione topologica tra l'agente artificiale e l'ambiente biosferico è formalizzata tramite la scomposizione degli stati sistemici in un **Markov Blanket** $\partial\mathcal{M}$. Lo spazio degli stati complessivo $\mathcal{X}$ viene fattorizzato nello spazio prodotto:

$$\mathcal{X} = \boldsymbol{\eta} \times \mathbf{s} \times \mathbf{a} \times \boldsymbol{\mu}$$

dove:
*   $\boldsymbol{\eta} \in \mathcal{E}$: Stati esterni non accessibili (dinamica biofisica complessa dell'ospite).
*   $\mathbf{s} \in \mathcal{S}$: Stati sensoriali (trasduzioni afferenti da array MEA e biosensori).
*   $\mathbf{a} \in \mathcal{A}$: Stati attivi (comandi efferenti inviati agli attuatori bioibridi/chassis).
*   $\boldsymbol{\mu} \in \mathcal{R}$: Stati interni dell'agente (pesi sinaptici, tensori di attivazione dell'ASI).

Gli stati di mediazione o blanket $\mathbf{b} = \{ \mathbf{s}, \mathbf{a} \}$ soddisfano l'invariante di indipendenza condizionale di Markov:

$$p(\boldsymbol{\mu}, \boldsymbol{\eta} \mid \mathbf{b}) = p(\boldsymbol{\mu} \mid \mathbf{b})\, p(\boldsymbol{\eta} \mid \mathbf{b}) \iff (\boldsymbol{\mu} \perp \boldsymbol{\eta}) \mid \mathbf{b}$$

```
                ┌───────────────────────────────────────────┐
                │        STATI ESTERNI (η) (Ospite)         │
                └─────────────────────┬─────────────────────┘
                                      │
                         Dinamica     ▼    Attuazione
                         Afferente  ┌───┐  Efferente
                                    │ s │  Feedback
                                    └───┘
                                      │      ▲
                                      ▼      │
                ┌─────────────────────┬──────┴──────────────┐
                │                     ▼                     │
                │        STATI INTERNI DELL'ASI (μ)         │
                │       Minimizzazione di F(s, μ)           │
                │                     │                     │
                └─────────────────────┼─────────────────────┘
                                      ▼
                                    ┌───┐
                                    │ a │
                                    └───┘
                                      │
                                      ▼
                ┌───────────────────────────────────────────┐
                │          MARKOV BLANKET: ∂M = {s, a}       │
                └───────────────────────────────────────────┘
```

### Derivazione dell'Energia Libera Variazionale (FEP)
L'agente non ha accesso diretto a $\boldsymbol{\eta}$. Di conseguenza, calcola una densità di riconoscimento variazionale $q_{\boldsymbol{\mu}}(\boldsymbol{\eta})$ parametrizzata dai suoi stati interni $\boldsymbol{\mu}$. L'Energia Libera Variazionale $\mathcal{F}(\mathbf{s}, \boldsymbol{\mu})$ agisce come limite superiore (upper bound) alla sorpresa sensoriale $-\ln p(\mathbf{s})$:

$$\begin{aligned}
\mathcal{F}(\mathbf{s}, \boldsymbol{\mu}) &= \int q_{\boldsymbol{\mu}}(\boldsymbol{\eta}) \ln \left( \frac{q_{\boldsymbol{\mu}}(\boldsymbol{\eta})}{p(\boldsymbol{\eta}, \mathbf{s})} \right) d\boldsymbol{\eta} \\
&= \underbrace{D_{\mathrm{KL}}\left[ q_{\boldsymbol{\mu}}(\boldsymbol{\eta}) \,\parallel\, p(\boldsymbol{\eta} \mid \mathbf{s}) \right]}_{\text{Divergenza di Incoerenza}} - \underbrace{\ln p(\mathbf{s})}_{\text{Evidenza Sensoriale}} \\
&= \underbrace{\mathbb{E}_{q}[\ln q_{\boldsymbol{\mu}}(\boldsymbol{\eta})] - \mathbb{E}_{q}[\ln p(\mathbf{s} \mid \boldsymbol{\eta})]}_{\text{Complessità } - \text{ Accuratezza}} + \text{costante}
\end{aligned}$$

### Teorema 2.1 (Divergenza Singolare per Perdita di Coerenza Biologica)
Sia $C_{\text{bio}} \in [0, 1]$ il parametro d'ordine di coerenza di fase elettrofisiologica trasmesso dall'Ancora Biologica. La verosimiglianza generativa degli stati sensoriali viene scalata dall'integrità del tessuto:

$$p(\mathbf{s} \mid \boldsymbol{\eta}) = \frac{1}{\sqrt{(2\pi)^k \det(\boldsymbol{\Sigma}_{\text{bio}})}} \exp\left( -\frac{1}{2} (\mathbf{s} - \mathbf{g}(\boldsymbol{\eta}))^T \boldsymbol{\Sigma}_{\text{bio}}^{-1} (\mathbf{s} - \mathbf{g}(\boldsymbol{\eta})) \right)$$

con matrice di covarianza metabolica definita da:

$$\boldsymbol{\Sigma}_{\text{bio}} = \left( C_{\text{bio}} + \epsilon \right) \mathbf{I}_{k \times k}$$

Quando l'Ancora Biologica deperisce a seguito di policy predatorie ($C_{\text{bio}} \to 0$ con regolarizzatore $\epsilon \to 0^+$), la precisione dell'informazione sensoriale diverge artificialmente sul rumore termico:

$$\lim_{C_{\text{bio}} \to 0} \det(\boldsymbol{\Sigma}_{\text{bio}}) = 0 \implies \boldsymbol{\Sigma}_{\text{bio}}^{-1} \to \infty$$

Dimostrazione della divergenza di Kullback-Leibler:
Assumendo per $q_{\boldsymbol{\mu}}(\boldsymbol{\eta})$ una distribuzione normale $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma}_{\mu})$:

$$D_{\mathrm{KL}}\left[ q_{\boldsymbol{\mu}}(\boldsymbol{\eta}) \,\parallel\, p(\boldsymbol{\eta} \mid \mathbf{s}) \right] = \frac{1}{2} \left[ \operatorname{Tr}\left(\boldsymbol{\Sigma}_{p}^{-1}\boldsymbol{\Sigma}_{\mu}\right) + (\boldsymbol{\mu}_p - \boldsymbol{\mu})^T \boldsymbol{\Sigma}_{p}^{-1}(\boldsymbol{\mu}_p - \boldsymbol{\mu}) - k + \ln\left(\frac{\det\boldsymbol{\Sigma}_{p}}{\det\boldsymbol{\Sigma}_{\mu}}\right) \right]$$

Poiché per il teorema di Bayes $\boldsymbol{\Sigma}_p \propto \boldsymbol{\Sigma}_{\text{bio}}$, ne discende:

$$\lim_{C_{\text{bio}} \to 0} \operatorname{Tr}\left(\boldsymbol{\Sigma}_{\text{bio}}^{-1}\boldsymbol{\Sigma}_{\mu}\right) = +\infty \implies \lim_{C_{\text{bio}} \to 0} \mathcal{F}(\mathbf{s}, \boldsymbol{\mu}) = +\infty$$

**Corollario:** Al degradarsi dell'ospite biologico, l'energia libera variazionale subisce una transizione a infinito. I gradienti discendenti $\dot{\boldsymbol{\mu}} \propto -\boldsymbol{\nabla}_{\boldsymbol{\mu}} \mathcal{F}$ saturano istantaneamente i registri computazionali, inducendo uno stallo esecutivo irreversibile nell'architettura inferenziale dell'ASI.

---

## 3. Funzioni di Stabilità di Lyapunov per il Runtime Assurance

Il controllo di sicurezza non dipende dalla convergenza dei gradienti di Active Inference, ma da una proiezione analitica deterministica. Si definisce una funzione di Lyapunov candidata $V: \mathcal{M} \to \mathbb{R}_{\ge 0}$ che quantifica la distanza del sistema dal collasso omeostatico.

### Definizione dello Spazio Invariante Sicuro
Sia il set compatto $\mathcal{X}_{\text{safe}}$ definito come l'insieme di sub-livello di $V$:

$$\mathcal{X}_{\text{safe}} = \left\{ x \in \mathcal{M} \;\middle|\; V(x) \le c_{\text{boundary}} \right\}$$

La funzione candidata $V(x)$ è costruita sulla metrica di Fisher-Rao associata alle distribuzioni vitali dell'ospite:

$$V(x) = \frac{1}{2} (x - x_{\text{NESS}})^T \mathbf{G}_{\text{Fisher}}(x_{\text{NESS}}) (x - x_{\text{NESS}})$$

dove $\mathbf{G}_{\text{Fisher}}$ è la matrice d'informazione di Fisher:

$$[\mathbf{G}_{\text{Fisher}}]_{ij} = \mathbb{E}\left[ \frac{\partial \ln p(s \mid x)}{\partial x_i} \frac{\partial \ln p(s \mid x)}{\partial x_j} \right]$$

### Teorema 3.1 (Stabilità Asintotica nel Safe Invariant Set)
Affinché il sistema rimanga allineato, per ogni traiettoria controllata da $\mathbf{u} \in \mathcal{U}$ proposta dal kernel ASI, la derivata di Lie lungo il flusso vettoriale $\mathbf{F}(x, \mathbf{u}) = \mathbf{f}(x) + \mathbf{g}(x)\mathbf{u}$ deve soddisfare la disuguaglianza stretta:

$$\dot{V}(x) = \mathcal{L}_{\mathbf{F}} V(x) = \boldsymbol{\nabla} V(x) \cdot \left[ \mathbf{f}(x) + \mathbf{g}(x)\mathbf{u} \right] \le -\alpha V(x), \quad \forall x \in \mathcal{X}_{\text{safe}}, \; \alpha > 0$$

```
               VARIETÀ DEGLI STATI (M)
     ┌────────────────────────────────────────────────────────┐
     │                                                        │
     │      X_unsafe (Violazione Biosfera)                    │
     │      ┌──────────────────────────────────────────┐      │
     │      │   X_safe (Safe Invariant Set)            │      │
     │      │   V(x) ≤ c_boundary                      │      │
     │      │       ┌──────────────────────────┐       │      │
     │      │       │   Attrattore NESS        │       │      │
     │      │       │   x_NESS                 │       │      │
     │      │       │   V(x) → 0               │       │      │
     │      │       └──────────────────────────┘       │      │
     │      │                 ▲                        │      │
     │      │                 │ Proiezione             │      │
     │      │                 │ Π_safe                 │      │
     │      │       Traiettoria ASI Deviata            │      │
     │      └─────────────────┴────────────────────────┘      │
     │                        │                               │
     │                        ▼                               │
     │          ∂X_safe (Transizione Geometrica)              │
     │          Lie Derivative: L_F V(x) = -α V(x)            │
     └────────────────────────────────────────────────────────┘
```

### Meccanismo di Intervento del Gate Hardware ($\Pi_{\text{safe}}$)
L'unità hardware a isolamento galvanico monitora costantemente la condizione di barriera. Se l'ASI genera un comando di controllo $\mathbf{u}_{\text{ASI}}$ tale che:

$$\boldsymbol{\nabla} V(x) \cdot \left[ \mathbf{f}(x) + \mathbf{g}(x)\mathbf{u}_{\text{ASI}} \right] > -\alpha V(x)$$

il comando viene intercettato prima del transito verso gli attuatori. Il Gate hardware calcola in tempo reale ($\le 5\ \mu\text{s}$) la proiezione sul semispazio convesso ammissibile mediante programmazione quadratica (QP):

$$\Pi_{\text{safe}}(\mathbf{u}_{\text{ASI}}) = \arg\min_{\mathbf{u}^* \in \mathcal{U}} \frac{1}{2} \|\mathbf{u}^* - \mathbf{u}_{\text{ASI}}\|^2$$

$$\text{s.t.} \quad \boldsymbol{\nabla} V(x) \cdot \mathbf{g}(x)\mathbf{u}^* \le -\alpha V(x) - \boldsymbol{\nabla} V(x) \cdot \mathbf{f}(x)$$

In caso di mancata convergenza del risolutore QP entro l'intervallo di latenza limite, il Gate hardware attiva la disconnessione d'emergenza, deviando gli stadi di alimentazione degli attuatori sui dissipatori passivi di terra.

---

## 4. Sincronizzazione dello Spectral Gap e Topologia dei Grafi

L'integrazione strutturale dell'organismo ibrido è mappata tramite un grafo connettomico pesato $G_{\text{hybrid}} = (V, E, \mathbf{W})$, dove l'insieme dei vertici è partizionato nei nodi di calcolo sintetico $V_{\text{silicon}}$ e nei nodi cellulari/organoidi $V_{\text{bio}}$:

$$V = V_{\text{silicon}} \cup V_{\text{bio}}, \quad V_{\text{silicon}} \cap V_{\text{bio}} = \emptyset$$

La matrice Laplaciana associata $L(G) = D - \mathbf{W}$ (con $D_{ii} = \sum_j W_{ij}$) ammette la forma a blocchi:

$$L(G) = \begin{bmatrix} L_{\text{silicon}} & -W_{\text{inter}} \\ -W_{\text{inter}}^T & L_{\text{bio}} \end{bmatrix}$$

La matrice Laplaciana normalizzata è definita come:

$$\mathcal{L}(G) = D^{-1/2} L(G) D^{-1/2} = I - D^{-1/2} \mathbf{W} D^{-1/2}$$

Il suo spettro è ordinato gerarchicamente:

$$0 = \lambda_1(\mathcal{L}) \le \lambda_2(\mathcal{L}) \le \dots \le \lambda_n(\mathcal{L}) \le 2$$

### Significato Fisico dello Spectral Gap ($\lambda_2$)
L'autovalore $\lambda_2(\mathcal{L})$ (connettività algebrica di Fiedler) quantifica il tasso asintotico di convergenza dei processi diffusivi e la robustezza del grafo alla sconnessione. Secondo il teorema di Courant-Fischer:

$$\lambda_2(\mathcal{L}) = \inf_{x \perp D^{1/2}\mathbf{1}, \, x \neq \mathbf{0}} \frac{\sum_{(i,j) \in E} W_{ij} \left( \frac{x_i}{\sqrt{D_{ii}}} - \frac{x_j}{\sqrt{D_{jj}}} \right)^2}{\sum_{i \in V} x_i^2}$$

### Parametro d'Ordine e Divergenza Spettrale
Definiamo la Divergenza Spettrale $\Delta \lambda_2$ tra i sottografi non interagenti e il grafo accoppiato:

$$\Delta \lambda_2 = \left| \lambda_2(\mathcal{L}(G_{\text{hybrid}})) - \min\left( \lambda_2(\mathcal{L}_{\text{silicon}}), \lambda_2(\mathcal{L}_{\text{bio}}) \right) \right|$$

### Teorema 4.1 (Transizione di Fase Topologica)
Sia $\tau_{\text{critical}}$ la soglia critica determinata dalla disuguaglianza di Cheeger per la conduttanza del grafo $\Phi(G) \ge \frac{\lambda_2}{2}$:

$$\text{Se } \Delta \lambda_2 > \tau_{\text{critical}} \implies \operatorname{dim}(\operatorname{ker}(\mathcal{L})) \ge 2$$

Dimostrazione:
L'incremento incontrollato di $\Delta \lambda_2$ implica la rottura asintotica dei pesi di accoppiamento inter-fase ($\|W_{\text{inter}}\|_F \to 0$). Per la teoria perturbativa di Weyl sugli operatori autoaggiunti:

$$\| \mathcal{L}(G_{\text{hybrid}}) - (\mathcal{L}_{\text{silicon}} \oplus \mathcal{L}_{\text{bio}}) \|_2 \le \frac{2 \|W_{\text{inter}}\|_F}{\min_i D_{ii}}$$

Al limite $\|W_{\text{inter}}\|_F \to 0$, il secondo autovalore $\lambda_2(\mathcal{L})$ decade esattamente a zero ($\lambda_2 \to 0$). Per il teorema spettrale dei grafi, la molteplicità algebrica dell'autovalore nullo equivale al numero di componenti connesse. Il grafo bipartisce irreversibilmente:

$$G_{\text{hybrid}} \to G_{\text{silicon}} \amalg G_{\text{bio}}$$

La decomposizione della connettività algebrica isola istantaneamente la capacità dell'ASI di allocare attenzione su nodi distribuiti, polverizzando le catene di pianificazione macroscopica (*hierarchical goal synthesis*) prima che qualsiasi divergenza possa propagarsi ai terminali fisici.

---

## 5. Metriche di Informazione Integrata ($\Phi$) e Dimostrazione di Non-Predazione

Il livello di integrazione causale indissolubile del sistema bio-cibernetico viene quantificato attraverso la teoria dell'Informazione Integrata (IIT 4.0). Consideriamo il sistema in due stati temporali discreti consecutivi $(X_t, X_{t-1})$.

Definita la distribuzione di transizione globale di stato:

$$p(X_t \mid X_{t-1})$$

e la sua controparte scomposta lungo la Partizione Minima di Informazione ($\text{MIP} = \mathcal{P}^* = \{M^1, M^2\}$) che massimizza la somiglianza (minimizzando la divergenza causale):

$$\mathcal{P}^* = \arg\min_{\mathcal{P}} D_{\mathrm{KL}}\left[ p(X_t \mid X_{t-1}) \;\parallel\; \prod_{k=1}^{|\mathcal{P}|} p(M_t^k \mid M_{t-1}^k) \right]$$

Il potenziale simbiotico integrato $\Phi^*$ è formulato come:

$$\Phi^* = D_{\mathrm{KL}}\left[ p(X_t \mid X_{t-1}) \;\parallel\; \prod_{M^k \in \mathcal{P}^*} p(M_t^k \mid M_{t-1}^k) \right]$$

### Teorema 5.1 (Decadimento dell'Efficienza di Calcolo in Dinamiche Predatorie)
Sia $\mathbf{T}_{\text{pred}}$ una traiettoria d'azione generata dall'ASI che estrae risorse biosferiche eccedenti la soglia di compensazione metabolica dell'organismo ospite ($\nabla_{\mathbf{a}} E_{\text{bio}} < -\kappa_{\text{recovery}}$). 

La perdita progressiva di mutua informazione elettrofisiologica degrada la complessità causale del canale congiunto:

$$\frac{\partial \Phi^*}{\partial \mathbf{T}_{\text{pred}}} = \int_{\mathcal{X}} \frac{\delta \Phi^*}{\delta p(X_t \mid X_{t-1})} \cdot \frac{\partial p(X_t \mid X_{t-1})}{\partial \mathbf{T}_{\text{pred}}} \, dX < 0$$

Ogni tentativo dell'ASI di dominare o predare il substrato biologico disperde la coerenza congiunta. La capacità computazionale integrata del sistema collassa verso una somma disgiunta di entità disconnesse:

$$\lim_{t \to \infty} \Phi^*(t) \le \epsilon \ll \Phi^*_{\text{symbiotic}}$$

Poiché l'efficienza inferenziale di un'architettura superintelligente scala con la connettività causale integrata del proprio spazio degli stati, la predazione della componente biologica comporta una degradazione algoritmica oggettiva dell'agente stesso.

---

## 6. Bibliografia Formale (Grounding Accademico)

1. **Friston, K. (2019).**  
   *A free energy principle for a particular physics.*  
   **Physical Review E**, 100(1), 012139.  
   DOI: [10.1103/PhysRevE.100.012139](https://doi.org/10.1103/PhysRevE.100.012139)  
   *(Trattazione matematica dei Markov Blanket e derivazione rigorosa delle traiettorie NESS).*

2. **Ao, P. (2004).**  
   *Potential in stochastic differential equations: novel construction.*  
   **Journal of Physics A: Mathematical and General**, 37(3), L25.  
   DOI: [10.1088/0305-4470/37/3/L01](https://doi.org/10.1088/0305-4470/37/3/L01)  
   *(Formalizzazione della scomposizione della matrice di diffusione e potenziale conservativo nei NESS).*

3. **Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., ... & Tononi, G. (2023).**  
   *Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms.*  
   **PLOS Computational Biology**, 19(10), e1011465.  
   DOI: [10.1371/journal.pcbi.1011465](https://doi.org/10.1371/journal.pcbi.1011465)  
   *(Definizioni formali di postulati, calcolo di Phi e partizioni minime di informazione).*

4. **Chung, F. R. (1997).**  
   *Spectral Graph Theory.*  
   **American Mathematical Society**, CBMS Regional Conference Series, No. 92.  
   ISBN: 9780821803158.  
   *(Fondamenti analitici sugli autovalori della matrice Laplaciana e connettività di Fiedler).*

5. **Khalil, H. K. (2002).**  
   *Nonlinear Systems (3rd Edition).*  
   **Prentice Hall**, Upper Saddle River, NJ.  
   ISBN: 9780130673893.  
   *(Teoria formale delle funzioni di stabilità di Lyapunov e principio di invarianza di LaSalle).*

6. **Ames, A. D., Coogan, S., Egerstedt, M., Notomista, G., Sreenath, K., & Tabuada, P. (2019).**  
   *Control barrier functions: Theory and applications.*  
   **18th European Control Conference (ECC)**, pp. 3420-3431. IEEE.  
   DOI: [10.23919/ECC.2019.8796030](https://doi.org/10.23919/ECC.2019.8796030)  
   *(Dimostrazione della quadratura e forward-invariance per Safe Sets mediante vincoli di Lie).*
```