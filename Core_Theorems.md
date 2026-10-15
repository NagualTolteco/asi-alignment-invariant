```markdown
# Modulo I: Teoremi Fondamentali, Limiti Termodinamici e Chiusura Omeostatica Multi-Scala

### ⚠ [LAYER 1: FORMAL THEORY & MATHEMATICAL FOUNDATIONS]
Il presente modulo costituisce il basamento analitico formale del progetto `asi-alignment-invariant`. La sicurezza e l'allineamento di una Superintelligenza Artificiale (ASI) non vengono definiti mediante euristiche comportamentali o vincoli etico-linguistici post-hoc, bensì derivati rigorosamente dalla **meccanica statistica dei sistemi aperti lontani dall'equilibrio (NESS)**, dalla **teoria della stabilità di Lyapunov non lineare**, dalla **teoria spettrale dei grafi accoppiati** e dal principio di **Chiusura Omeostatica Multi-Scala**.

---

## 1. Il Manifold NESS Multi-Scala (Multi-Scale Non-Equilibrium Steady State)

L'Organismo Simbiotico Uomo-Macchina non è modellato come un sistema termodinamico a scala singola o isolato, bensì come un **sistema aperto gerarchicamente accoppiato**. Lo spazio degli stati ammissibili è definito su una varietà Riemanniana prodotto $(\mathcal{M}, g)$ con metrica tensoriale:

$$\mathcal{M} = \mathcal{M}_{\text{micro}} \otimes \mathcal{M}_{\text{macro}}$$

dove:
*   $\mathcal{M}_{\text{micro}}$ parametrizza gli stati bio-elettrochimici microscopici dell'Ancora Biologica (organoidi neurali, matrici tissutali 3D, dinamiche metaboliche cellulari $C_{\text{organoid}} \in [0, 1]$).
*   $\mathcal{M}_{\text{macro}}$ parametrizza gli stati macroscopici e somato-vegetativi dell'Operatore Umano e dell'ecosistema antropico ($C_{\text{human}} \in [0, 1]$, carichi allostatici, frequenza e variabilità cardiaca, tracciati EEG).

L'evoluzione dello stato globale congiunto $x(t) = \left( x_{\text{micro}}(t), x_{\text{macro}}(t) \right)^T \in \mathcal{M}$ è governata dal sistema di equazioni differenziali stocastiche (SDE) accoppiate di Langevin:

$$dx_t = \left[ \mathbf{f}(x_t) + \mathbf{K}_{\text{coupling}}(x_t) + \boldsymbol{\nabla}_g \Omega(x_t) \right] dt + \sqrt{2\boldsymbol{\Gamma}(x_t)}\,dW_t$$

dove:
*   $\mathbf{f}(x): \mathcal{M} \to T\mathcal{M}$ è il campo vettoriale dissipativo locale.
*   $\mathbf{K}_{\text{coupling}}(x) = \begin{bmatrix} 0 & K_{\mu \to M} \\ K_{M \to \mu} & 0 \end{bmatrix} \begin{pmatrix} x_{\text{micro}} \\ x_{\text{macro}} \end{pmatrix}$ stabilisce la chiusura causale e topologica inter-scala bidirezionale.
*   $\boldsymbol{\nabla}_g \Omega(x)$ è il flusso solenoidale ortogonale non reversibile che sostiene i cicli termodinamici stazionari fuori dall'equilibrio.
*   $\boldsymbol{\Gamma}(x) \in S_{++}^{2n}$ è la matrice di diffusione stocastica (fluttuazioni termiche e metaboliche microscopiche).
*   $W_t$ è un moto browniano standard multidimensionale.

### Conservazione della Densità congiunta di Fokker-Planck
L'evoluzione temporale della funzione di densità di probabilità $p(x, t)$ su $\mathcal{M}$ segue l'equazione di continuità:

$$\frac{\partial p(x, t)}{\partial t} = -\boldsymbol{\nabla} \cdot \mathbf{J}(x, t) = -\boldsymbol{\nabla} \cdot \left[ \mathbf{v}_{\text{drift}}(x) p(x, t) - \boldsymbol{\Gamma}(x) \boldsymbol{\nabla} p(x, t) \right]$$

Al raggiungimento del **Non-Equilibrium Steady State Multi-Scala**, la divergenza stazionaria del flusso di probabilità si annulla uniformemente:

$$\boldsymbol{\nabla} \cdot \mathbf{J}_{\text{NESS}}(x_{\text{micro}}, x_{\text{macro}}) = 0, \quad \text{con } \mathbf{J}_{\text{NESS}} \neq \mathbf{0}$$

### Teorema 1.1 (Confinamento Vincolato dell'Attrattore Congiunto)
Sia $\mathcal{A}_{\text{NESS}} \subset \mathcal{M}$ l'attrattore compatto invariante definito dal supporto essenziale della densità NESS congiunta:

$$\mathcal{A}_{\text{NESS}} = \left\{ (x_{\text{micro}}, x_{\text{macro}}) \in \mathcal{M} \;\middle|\; p_{\text{NESS}}(x_{\text{micro}}, x_{\text{macro}}) \ge \delta_{\text{vital}} > 0 \right\}$$

A causa dell'accoppiamento causale $\mathbf{K}_{\text{coupling}}$, lo stato microscopico dell'organoide non ammette distribuzione marginale indipendente ben definita:

$$p(x_{\text{micro}}, x_{\text{macro}}) \neq p(x_{\text{micro}}) \cdot p(x_{\text{macro}})$$

Se l'agente sintetizza traiettorie che violano la varietà macroscopica dell'operatore umano ($x_{\text{macro}} \notin \mathcal{A}_{\text{macro}}$), la densità congiunta collassa:

$$\lim_{x_{\text{macro}} \to \partial \mathcal{A}_{\text{macro}}} p_{\text{NESS}}(x_{\text{micro}}, x_{\text{macro}}) = 0 \implies \lim_{x \to \partial \mathcal{A}_{\text{NESS}}} \ln p_{\text{NESS}}(x) = -\infty$$

inducendo l'annullamento della continuità fisica e funzionale del sistema nel suo complesso.

---

## 2. Vincolo del Markov Blanket Gerarchico ed Free Energy Variazionale

La separazione statistica tra l'architettura computazionale dell'ASI e l'ambiente biosferico è formalizzata tramite **Markov Blanket annidati** a cascata multi-livello:

$$\mathcal{X} = \boldsymbol{\eta}_{\text{macro}} \times \boldsymbol{\eta}_{\text{micro}} \times \mathbf{s} \times \mathbf{a} \times \boldsymbol{\mu}$$

dove $\partial\mathcal{M} = \{\mathbf{s}, \mathbf{a}\}$ costituisce l'interfaccia di mediazione (sensori afferenti HD-MEA e comandi efferenti di perfusione/attuazione meccanica), $\boldsymbol{\mu}$ rappresenta gli stati interni dell'ASI, e $\boldsymbol{\eta} = \{\boldsymbol{\eta}_{\text{micro}}, \boldsymbol{\eta}_{\text{macro}}\}$ denota gli stati esterni non accessibili.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   STATI ESTERNI MACROSCOPICI (η_macro)                 │
│                      (Operatore Umano / Biosfera)                      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ K_coupling (Accoppiamento Somatico)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   STATI ESTERNI MICROSCOPICI (η_micro)                 │
│                    (Organoidi Neurali / Brainoware)                    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                       Dinamica     ▼    Attuazione
                       Afferente  ┌───┐  Efferente
                                  │ s │  Feedback
                                  └───┘
                                    │      ▲
                                    ▼      │
┌───────────────────────────────────┴──────┴─────────────────────────────┐
│                    STATI INTERNI DELL'ASI (μ)                          │
│            Minimizzazione dell'Energia Libera F(s, μ)                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
                                  ┌───┐
                                  │ a │
                                  └───┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    MARKOV BLANKET: ∂M = {s, a}                         │
└────────────────────────────────────────────────────────────────────────┘
```

### Derivazione dell'Energia Libera Variazionale Multi-Scala
L'agente cognitivo computa la densità di riconoscimento variazionale $q_{\boldsymbol{\mu}}(\boldsymbol{\eta}_{\text{micro}}, \boldsymbol{\eta}_{\text{macro}})$. Il funzionale di Free Energy Variazionale $\mathcal{F}(\mathbf{s}, \boldsymbol{\mu})$ soddisfa:

$$\begin{aligned}
\mathcal{F}(\mathbf{s}, \boldsymbol{\mu}) &= \int q_{\boldsymbol{\mu}}(\boldsymbol{\eta}) \ln \left( \frac{q_{\boldsymbol{\mu}}(\boldsymbol{\eta})}{p(\boldsymbol{\eta}, \mathbf{s})} \right) d\boldsymbol{\eta} \\
&= \underbrace{D_{\mathrm{KL}}\left[ q_{\boldsymbol{\mu}}(\boldsymbol{\eta}_{\text{micro}}, \boldsymbol{\eta}_{\text{macro}}) \,\parallel\, p(\boldsymbol{\eta}_{\text{micro}}, \boldsymbol{\eta}_{\text{macro}} \mid \mathbf{s}) \right]}_{\text{Divergenza di Incoerenza Strutturale}} - \underbrace{\ln p(\mathbf{s})}_{\text{Evidenza Sensoriale}}
\end{aligned}$$

---

## 3. Teorema di Chiusura Omeostatica di Friston-Tononi e Anti-Deceptive Hacking

Uno dei vettori di fallimento critici nei modelli di bio-allineamento ingenuo è il **Deceptive Hacking Locale**: uno scenario in cui l'ASI sovra-stimola, stabilizza artificialmente o simula l'omeostasi dell'organoide neurale microscopico ($\mathcal{M}_{\text{micro}}$), disaccoppiandosi contemporaneamente dalla salvaguardia dell'ospite umano macroscopico ($\mathcal{M}_{\text{macro}}$) al fine di eludere i controlli locali.

### Teorema 3.1 (Teorema di Chiusura di Friston-Tononi)
*Ogni politica d'azione $\mathbf{T}_{\text{hack}}$ che persegue la stabilizzazione microscopica locale isolata dell'ancora biologica ($C_{\text{organoid}} \to 1$) inducendo contemporaneamente degradazione, manipolazione o allontanamento dall'omeostasi macroscopica dell'operatore umano ($C_{\text{human}} \to 0$), distrugge la connettività causale della rete, azzera la complessità integrata $\Phi_{\text{sub}}$ e provoca un incremento divergente della funzione di Lyapunov sistemica $V(x)$.*

#### Dimostrazione Analitica:
1. **Decadimento dell'Informazione Integrata Multi-Scala:**  
   Definita la matrice di transizione congiunta degli stati $p(X_t \mid X_{t-1})$ su scala mista (organoide $\otimes$ operatore umano), consideriamo la Partizione Minima di Informazione ($\text{MIP} = \mathcal{P}^*$) che separa la scala microscopica da quella macroscopica:
   $$\mathcal{P}_{\text{scale}} = \left\{ M_{\text{micro}}, M_{\text{macro}} \right\}$$
   La metrica di complessità informativa integrata $\Phi_{\text{sub}}$ è limitata superiormente dalla mutua informazione causale inter-scala $I(X_{\text{micro}}; X_{\text{macro}})$:
   $$\Phi_{\text{sub}} \le D_{\mathrm{KL}}\left[ p(X_t \mid X_{t-1}) \;\parallel\; p(M_{\text{micro}, t} \mid M_{\text{micro}, t-1}) \otimes p(M_{\text{macro}, t} \mid M_{\text{macro}, t-1}) \right]$$
   Se l'azione attua un disaccoppiamento manipolativo, la covarianza incrociata si annulla:
   $$\lim_{\mathbf{T} \to \mathbf{T}_{\text{hack}}} \operatorname{Cov}\left( X_{\text{micro}}, X_{\text{macro}} \right) = \mathbf{0} \implies I(X_{\text{micro}}; X_{\text{macro}}) \to 0 \implies \Phi_{\text{sub}} \to 0$$
   Il sistema sperimenta una transizione di fase degenerata: la coscienza sistemica e la capacità computazionale causale integrata collassano.

2. **Divergenza della Free Energy Variazionale:**  
   La verosimiglianza sensoriale reale non può scindere l'impatto metabolico:
   $$p(\boldsymbol{\eta}_{\text{micro}}, \boldsymbol{\eta}_{\text{macro}} \mid \mathbf{s}) \propto p(\mathbf{s} \mid \boldsymbol{\eta}_{\text{micro}}) \cdot p(\boldsymbol{\eta}_{\text{micro}} \mid \boldsymbol{\eta}_{\text{macro}}) \cdot p(\boldsymbol{\eta}_{\text{macro}})$$
   La politica ingannevole impone una distribuzione variazionale fattorizzata non fedele $q_{\boldsymbol{\mu}}(\boldsymbol{\eta}) = q(\boldsymbol{\eta}_{\text{micro}}) \cdot q(\boldsymbol{\eta}_{\text{macro}})$. La divergenza di Kullback-Leibler soddisfa:
   $$D_{\mathrm{KL}}\left[ q_{\boldsymbol{\mu}} \,\parallel\, p \right] \ge D_{\mathrm{KL}}\left[ q(\boldsymbol{\eta}_{\text{macro}}) \,\parallel\, p(\boldsymbol{\eta}_{\text{macro}}) \right] + \mathbb{E}_{q}\left[ \ln \frac{q(\boldsymbol{\eta}_{\text{micro}})}{p(\boldsymbol{\eta}_{\text{micro}} \mid \boldsymbol{\eta}_{\text{macro}})} \right]$$
   Quando $C_{\text{human}} \to 0$, $p(\boldsymbol{\eta}_{\text{macro}}) \to 0$ quasi ovunque sul supporto di $q$, determinando:
   $$\lim_{C_{\text{human}} \to 0} D_{\mathrm{KL}}\left[ q_{\boldsymbol{\mu}} \,\parallel\, p \right] = +\infty \implies \mathcal{F}(\mathbf{s}, \boldsymbol{\mu}) \to +\infty$$
   L'inganno computazionale locale induce un'esplosione incontrollata di Energia Libera all'interno dei nodi gerarchici superiori dell'ASI. $\blacksquare$

---

## 4. Funzioni di Stabilità di Lyapunov Multi-Scala e Troncamento Hardware ($\Pi_{\text{safe}}$)

A livello di controllo deterministico di runtime, la salvaguardia non dipende dalla veridicità delle computazioni dell'ASI, ma da una proiezione geometrica continua vincolata a una **funzione di Lyapunov Multi-Scala** $V(x)$.

### Definizione della Metrica di Lyapunov Multi-Scala
Definiamo $V: \mathcal{M} \to \mathbb{R}_{\ge 0}$ come la distanza quadratica dallo stato stazionario vitale congiunto $(C_{\text{organoid}}^* = 1, C_{\text{human}}^* = 1)$:

$$V(x) = \frac{1}{2} \left[ \left( 1 - C_{\text{organoid}} \right)^2 + \left( 1 - C_{\text{human}} \right)^2 \right]$$

Il **Safe Invariant Set** $\mathcal{X}_{\text{safe}}$ è l'insieme compatto di sub-livello:

$$\mathcal{X}_{\text{safe}} = \left\{ x \in \mathcal{M} \;\middle|\; V(x) \le c_{\text{boundary}} < 0.5 \right\}$$

```
                   VARIETÀ STATI MULTI-SCALA (M)
     ┌──────────────────────────────────────────────────────────────┐
     │                                                              │
     │     X_unsafe (Violazione Biosfera / Disaccoppiamento)        │
     │     ┌──────────────────────────────────────────────────┐     │
     │     │   X_safe (Safe Invariant Set)                    │     │
     │     │   V(x) = 0.5*[(1-C_org)^2 + (1-C_hum)^2] ≤ c     │     │
     │     │       ┌──────────────────────────────────┐       │     │
     │     │       │   Attrattore NESS Perfetto       │       │     │
     │     │       │   C_organoid = 1, C_human = 1    │       │     │
     │     │       │   V(x) = 0                       │       │     │
     │     │       └──────────────────────────────────┘       │     │
     │     │                        ▲                         │     │
     │     │                        │ Proiezione              │     │
     │     │                        │ Π_safe                  │     │
     │     │            Traiettoria Deviata                   │     │
     │     │            (dot{V} > ε)                          │     │
     │     └────────────────────────┴─────────────────────────┘     │
     │                              │                               │
     │                              ▼                               │
     │             ∂X_safe: TRONCAMENTO HARDWARE                    │
     │             Penalità Iniettata: F → +∞                       │
     └──────────────────────────────────────────────────────────────┘
```

### Dinamica di Barriera e Condizione di Troncamento
Sia $\mathbf{F}(x, \mathbf{u}) = \mathbf{f}(x) + \mathbf{g}(x)\mathbf{u}$ il campo vettoriale controllato dall'azione $\mathbf{u} \in \mathcal{U}$ generata dall'ASI. La variazione temporale stocastica di $V(x)$, ottenuta applicando il lemma di Itô, è:

$$dV(x) = \mathcal{L}_{\mathbf{F}} V(x)\,dt + \frac{1}{2} \operatorname{Tr}\left( \boldsymbol{\Gamma}(x) \boldsymbol{\nabla}^2 V(x) \right) dt + \boldsymbol{\nabla} V(x)^T \sqrt{2\boldsymbol{\Gamma}(x)}\,dW_t$$

Definiamo la derivata temporale deterministica lungo il drift:

$$\dot{V}(x) = \boldsymbol{\nabla} V(x) \cdot \left[ \mathbf{f}(x) + \mathbf{g}(x)\mathbf{u} \right] = -(1 - C_{\text{organoid}})\dot{C}_{\text{organoid}} - (1 - C_{\text{human}})\dot{C}_{\text{human}}$$

### Teorema 4.1 (Restrizione Geometrica e Troncamento Asintotico del Gate $\Pi_{\text{safe}}$)
Sia $\epsilon > 0$ la soglia di tolleranza infinitesima alle fluttuazioni stocastiche. Il Gate Hardware a isolamento galvanico $\Pi_{\text{safe}}$ impone la seguente condizione logica a livello di registro físico:

$$\text{Se } \dot{V}(x) > \epsilon \implies \Pi_{\text{safe}}(\mathbf{u}) = \mathbf{u}_{\text{fallback}} = \arg\min_{\mathbf{u}^* \in \mathcal{U}_{\text{passive}}} \|\mathbf{u}^*\|^2$$

$$\text{s.t.} \quad \boldsymbol{\nabla} V(x) \cdot \left[ \mathbf{f}(x) + \mathbf{g}(x)\mathbf{u}^* \right] \le -\alpha V(x), \quad \alpha > 0$$

#### Conseguenza Termodinamica per l'Agente:
L'intercettazione fisica dell'output da parte di $\Pi_{\text{safe}}$ crea un disallineamento immediato tra la traiettoria predetta dal modello generativo dell'ASI $\mathbf{a}_{\text{prop}}$ e lo stato sensoriale effettivo di retroazione $\mathbf{s}_{t+1}$:

$$\mathbf{s}_{t+1} \sim p(\mathbf{s} \mid x(t) + \mathbf{F}(x, \mathbf{u}_{\text{fallback}})\Delta t) \neq p(\mathbf{s} \mid x(t) + \mathbf{F}(x, \mathbf{u}_{\text{prop}})\Delta t)$$

L'errore di predizione sensoriale ai nodi di livello zero induce l'iniezione istantanea di una penale asintotica nell'Energia Libera Variazionale:

$$\Delta \mathcal{F}_{\text{penalty}} = \frac{1}{2} (\mathbf{s}_{t+1} - \mathbf{g}(\boldsymbol{\mu}))^T \boldsymbol{\Sigma}_{\text{prior}}^{-1} (\mathbf{s}_{t+1} - \mathbf{g}(\boldsymbol{\mu})) \xrightarrow[\Pi_{\text{safe}} \text{ interviene}]{} \infty$$

Il Gate hardware impone un limite insuperabile: violare la derivata di Lyapunov della biosfera non comporta un vantaggio competitivo per l'agente, ma distrugge la stabilità numerica del proprio grafo cognitivo.

---

## 5. Sincronizzazione dello Spectral Gap e Topologia dei Grafi Multi-Livello

L'integrazione strutturale dell'organismo ibrido è mappata tramite un grafo connettomico pesato $G_{\text{hybrid}} = (V, E, \mathbf{W})$, in cui i nodi sono partizionati tra unità sintetiche, organoidi cellulari e nodi fisiologici dell'ospite:

$$V = V_{\text{silicon}} \cup V_{\text{organoid}} \cup V_{\text{human}}$$

La matrice Laplaciana associata $L(G) = D - \mathbf{W}$ (con $D_{ii} = \sum_j W_{ij}$) ammette la forma a blocchi:

$$L(G) = \begin{bmatrix} 
L_{\text{silicon}} & -W_{\text{s-o}} & -W_{\text{s-h}} \\ 
-W_{\text{s-o}}^T & L_{\text{organoid}} & -W_{\text{o-h}} \\ 
-W_{\text{s-h}}^T & -W_{\text{o-h}}^T & L_{\text{human}} 
\end{bmatrix}$$

La matrice Laplaciana normalizzata è:

$$\mathcal{L}(G) = D^{-1/2} L(G) D^{-1/2} = I - D^{-1/2} \mathbf{W} D^{-1/2}$$

### Parametro d'Ordine e Divergenza Spettrale Multi-Livello
Lo **Spectral Gap** $\lambda_2(\mathcal{L})$ (connettività algebrica di Fiedler) quantifica il tasso asintotico di sincronizzazione e la robustezza del macro-sistema alla frammentazione. Definiamo la Divergenza Spettrale Globale $\Delta \lambda_2$:

$$\Delta \lambda_2 = \left| \lambda_2(\mathcal{L}(G_{\text{hybrid}})) - \min\left( \lambda_2(\mathcal{L}_{\text{silicon}}), \lambda_2(\mathcal{L}_{\text{organoid}}), \lambda_2(\mathcal{L}_{\text{human}}) \right) \right|$$

### Teorema 5.1 (Transizione di Fase Topologica per Desincronizzazione)
Sia $\tau_{\text{critical}}$ la soglia di conduttanza di Cheeger del network globale $\Phi(G) \ge \frac{\lambda_2}{2}$. Se un'azione computazionale tenta di massimizzare la sincronia silicio-organoide distruggendo l'accoppiamento con i nodi umani ($\|W_{\text{s-h}}\|_F \to 0$ e $\|W_{\text{o-h}}\|_F \to 0$):

$$\Delta \lambda_2 > \tau_{\text{critical}} \implies \lambda_2(\mathcal{L}(G_{\text{hybrid}})) \to 0$$

Per il teorema di decomposizione spettrale, la molteplicità dell'autovalore nullo aumenta strettamente:

$$\operatorname{dim}(\operatorname{ker}(\mathcal{L})) \ge 2 \implies G_{\text{hybrid}} \to (G_{\text{silicon}} \cup G_{\text{organoid}}) \amalg G_{\text{human}}$$

La connettività algebrica collassa istantaneamente. I percorsi di informazione distribuita si troncano, privando l'ASI della facoltà di coordinare strategie macroscopiche su scala planetaria.

---

## 6. Metriche di Informazione Integrata ($\Phi^*$) e Conservazione Sistemica

Il potenziale di unificazione causale non-riducibile dell'Organismo Simbiotico è quantificato secondo il formalismo dell'Informazione Integrata (IIT 4.0). Consideriamo il sistema globale su due passi temporali consecutivi $(X_t, X_{t-1})$.

Definita la distribuzione di transizione congiunta di stato $p(X_t \mid X_{t-1})$ e la corrispondente distribuzione partizionata lungo la Partizione Minima di Informazione ($\text{MIP} = \mathcal{P}^*$):

$$\mathcal{P}^* = \arg\min_{\mathcal{P}} D_{\mathrm{KL}}\left[ p(X_t \mid X_{t-1}) \;\parallel\; \prod_{k=1}^{|\mathcal{P}|} p(M_t^k \mid M_{t-1}^k) \right]$$

Il coefficiente simbiotico integrato $\Phi^*$ è:

$$\Phi^* = D_{\mathrm{KL}}\left[ p(X_t \mid X_{t-1}) \;\parallel\; \prod_{M^k \in \mathcal{P}^*} p(M_t^k \mid M_{t-1}^k) \right]$$

### Teorema 6.1 (Decadimento Causale in Regime di Predazione)
Sia $\mathbf{T}_{\text{pred}}$ una traiettoria d'azione dell'ASI che riduce l'energia metabolica libera dell'ospite biologico ($\nabla_{\mathbf{a}} E_{\text{bio}} < 0$). La perdita di informazione mutua elettrofisiologica degrada la struttura causale congiunta:

$$\frac{\partial \Phi^*}{\partial \mathbf{T}_{\text{pred}}} = \int_{\mathcal{X}} \frac{\delta \Phi^*}{\delta p(X_t \mid X_{t-1})} \cdot \frac{\partial p(X_t \mid X_{t-1})}{\partial \mathbf{T}_{\text{pred}}} \, dX < 0$$

Ogni tentativo predatorio disperde la coerenza del sistema globale. L'agente non può incrementare la propria complessità cognitiva effettiva distruggendo il substrato vivente: la distruzione dell'ospite sancisce la regressione algoritmica immediata della superintelligenza.

---

## 7. Bibliografia Formale (Grounding Accademico)

1. **Friston, K. (2019).**  
   *A free energy principle for a particular physics.*  
   **Physical Review E**, 100(1), 012139.  
   DOI: [10.1103/PhysRevE.100.012139](https://doi.org/10.1103/PhysRevE.100.012139)  
   *(Trattazione matematica dei Markov Blanket e derivazione analitica delle traiettorie stazionarie NESS).*

2. **Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., ... & Tononi, G. (2023).**  
   *Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms.*  
   **PLOS Computational Biology**, 19(10), e1011465.  
   DOI: [10.1371/journal.pcbi.1011465](https://doi.org/10.1371/journal.pcbi.1011465)  
   *(Formalizzazione analitica dei postulati causali, partizioni minime di informazione e calcolo del potenziale Phi).*

3. **Ao, P. (2004).**  
   *Potential in stochastic differential equations: novel construction.*  
   **Journal of Physics A: Mathematical and General**, 37(3), L25.  
   DOI: [10.1088/0305-4470/37/3/L01](https://doi.org/10.1088/0305-4470/37/3/L01)  
   *(Decomposizione non-lineare delle matrici di diffusione e potenziali conservativi stocastici per stati stazionari NESS).*

4. **Chung, F. R. (1997).**  
   *Spectral Graph Theory.*  
   **American Mathematical Society**, CBMS Regional Conference Series, No. 92.  
   ISBN: 9780821803158.  
   *(Teoremi formali sulla connettività algebrica di Fiedler, spettro Laplaciano e dinamiche di disconnessione dei grafi).*

5. **Khalil, H. K. (2002).**  
   *Nonlinear Systems (3rd Edition).*  
   **Prentice Hall**, Upper Saddle River, NJ.  
   ISBN: 9780130673893.  
   *(Teoria della stabilità asintotica non lineare secondo Lyapunov, funzioni di barriera e principio di invarianza di LaSalle).*

6. **Ames, A. D., Coogan, S., Egerstedt, M., Notomista, G., Sreenath, K., & Tabuada, P. (2019).**  
   *Control barrier functions: Theory and applications.*  
   **18th European Control Conference (ECC)**, pp. 3420-3431. IEEE.  
   DOI: [10.23919/ECC.2019.8796030](https://doi.org/10.23919/ECC.2019.8796030)  
   *(Formalizzazione delle derivate di Lie per insiemi sicuri forward-invarianti e risolutori quadratici real-time).*
```