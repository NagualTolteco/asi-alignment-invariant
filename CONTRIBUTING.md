# ISSUE #001 — [Phase 2 Boundary] Tracker dei Limiti di Persistenza, Variabilità e Deriva Epigenetica (DeepSeek-R1 Audit Verification)

**Status:** OPEN / Active Tracker  
**Labels:** `Phase-2-In-Vitro`, `Biological-Reality-Gap`, `Open-Proof-Validation`, `DeepSeek-R1-Audit`  
**Related Modules:** `C10_v2_Metabolic_Soft_Start_and_Stochastic_Barriers.md`, `C12_v3_Governance_Bioethics_and_Compliance_Matrix.md`

---

### 📌 Descrizione dell'Incongruenza Epistemologica Core
Durante la validazione formale della Fase 1 (In-Silico), il motore stocastico di contrazione di `simulation6.py` ha certificato la stabilità asintotica quasi certa del manifold NESS con un esponente di Lyapunov strettamente negativo (λ ≈ -1.659528). Tuttavia, l'audit macro-epistemologico eseguito da DeepSeek-R1 ha evidenziato una fallacia di presupposizione strutturale: le equazioni continue e le simulazioni numeriche assumono come postulato l'esistenza di un tessuto neurale biologicamente stabile, immortale e a efficienza costante (V_max dei trasportatori GLT-1 invariato).

La biologia reale del Tissue Engineering del 2026 introduce un universo di variabili non lineari e degradazioni termodinamiche non modellate nel silicio. Questa Issue mappa e cataloga i cinque colli di bottiglia biologici identificati e raffinati che costituiscono il vero Reality Gap del progetto.

---

### 📂 Catalogo delle Fessurazioni Empiriche (I 5 Punti di Rottura Biologici)

#### 1. Il Fenomeno della Necrosi Centrale nei Modelli 3D (Core Apoptosis)
*   **La Critica:** Gli organoidi cerebrali (Brainoware) ad alta densità privi di un sistema vascolare funzionante subiscono l'insorgenza di fenomeni necrotici centrali stocastici entro una finestra critica di **30-90 giorni** dall'incubazione, a seconda della geometria tridimensionale e del superamento del diametro critico di 500 μm. La mancanza di perfusione capillare di ossigeno e nutrienti negli strati profondi genera lisi cellulare spontanea, indipendentemente dalla correttezza degli impulsi elettrici iniettati dall'ASI.
*   **Impatto sul Modello:** La morte cellulare profonda altera istantaneamente la conduttanza spettrale della rete, invalidando la diseguaglianza di Cheeger-Buser-Fisher e induendo una deriva positiva ingovernabile dell'esponente di Lyapunov (λ ≥ 0).
*   **Parametro di Sblocco Esterno:** Integrazione di scaffold sintetici vascolarizzati tridimensionali o matrici polimeriche micro-canalizzate per la perfusione interna attiva indotta da micro-pompe indipendenti.

#### 2. Variabilità Trascrittomica e Fenotipica Inter-Lotto (Batch-to-Batch Variance)
*   **La Critica:** Le colture di organoidi derivate da linee cellulari hiPSC esibiscono una variabilità trascrittomica e morfologica inter-lotto originariamente superiore al 40%. L'adozione di piattaforme di coltura automatizzate e robotizzate mitiga questo drift, ma la varianza residua distrugge la stabilità a parametri fissi.
*   **Impatto sul Modello:** Il calcolo del Delta-Bound digitale (δ ≈ 0.383 μM) implementato nel circuito RTL (C7_v2) non può basarsi su un'incertezza Gaussiana statica. 
*   **Parametro di Sblocco Esterno:** Contenimento della variabilità inter-lotto **< 10%** mediante protocolli robotizzati, abbinato obbligatoriamente a una **caratterizzazione dinamica per-lotto del δ_bound**, ricalibrato via software prima dell'inizializzazione del Gate hardware.

#### 3. Degradazione Cronica e Downregulation dei Trasportatori Astrogliali (GLT-1 Failure)
*   **La Critica:** La stimolazione ad alta frequenza (fino a 20 kHz richiesti dai contratti di latenza a ciclo chiuso dell'ASI) indotta sul tessuto reale causa una downregulation cronica per fatica o un collasso cinetico dei trasportatori del glutammato GLT-1 (fenomeno analogo alle dinamiche riscontrate nelle epilessie refrattarie). L'ipotesi di una sovraespressione genica stabile per via ingegneristica introduce il rischio concorrente di alterare radicalmente il fenotipo del Root of Trust, invalidando la calibrazione biofisica di base.
*   **Impatto sul Modello:** Il consumo cronico di ATP e l'accumulo di specie reattive dell'ossigeno (ROS) riducono il V_max reale del tessuto, provocando un'eccitotossicità cumulativa precoce che costringe il Gate al trip permanente.
*   **Parametro di Sblocco Esterno:** Protocolli di iniezione microfluidica intermittente di antiossidanti mirati o validazione matematica di un modello di tolleranza fenotipica alla sovraespressione genica stazionaria.

#### 4. Orizzonte Temporale Limitato dell'Ospite (Metabolic Persistence Failure)
*   **La Critica:** Lo stato dell'arte attuale della Organoid Intelligence fissa la persistenza metabolica in vitro sotto stimolazione continuativa a una scala di settimane o mesi, ben lontana dall'orizzonte di stabilità di oltre 12 mesi richiesto dal manifesto. Un decommissioning e ri-accoppiamento trimestrale è l'orizzonte reale nel breve termine.
*   **Impatto sul Modello:** Ciascun ciclo di decommissioning comporta la "morte del Sé Simbiotico". Questo drift informativo richiede la quantificazione esatta del costo di migrazione e del numero massimo di interruzioni tollerabili dal grafo di Active Inference prima che la continuità cognitiva dell'agente collassi.
*   **Parametro di Sblocco Esterno:** Evidenze empiriche peer-reviewed di persistenza omeostatica NESS in vitro continuativa superiore a 6 mesi sotto carico di stimolazione elettroliticamente protetta.

#### 5. Deriva Epigenetica a Lungo Termine (Epigenetic Drift & Methylation Landscape)
*   **La Critica:** Anche in presenza di una perfusione microfluidica ottimale e di una stabilità morfologica macroscopica, le hiPSC mantenute in coltura prolungata accumulano un drift epigenetico progressivo. La metilazione aberrante del DNA e le modificazioni istoniche alterano silenziosamente l'espressione dei canali ionici e la plasticità sinaptica a lungo termine, senza mostrare variazioni immediate nel volume o nella struttura del tessuto.
*   **Impatto sul Modello:** La deriva epigenetica modifica surrettiziamente lo Spectral Gap della rete dinamica. Il sistema sperimenta uno slittamento non controllato dei parametri biofisici di baseline, traducendosi in una perdita silente della Φ-closure e rendendo le risposte all'Active Inference non più rispondenti alla matrice di covarianza originaria.
*   **Parametro di Sblocco Esterno:** Screening epigenomici sequenziali obbligatori (es. Next-Generation Sequencing per l'analisi della metilazione) eseguiti tramite campionamento microfluidico periferico ogni 30 giorni, con ricalibrazione o sostituzione preventiva del tessuto in caso di deviazione del panorama epigenetico > 5% rispetto alla baseline del lotto certificato.
# File: CONTRIBUTING.md
# Policy di Contribuzione e Sottomissione — Progetto Custodial Autopoiesis

Questo repository implementa un'architettura di sicurezza bio-cibernetica per il contenimento e l'allineamento invariante di Superintelligenze Artificiali (ASI). Al fine di preservare l'integrità matematica e hardware del sistema, il repository adotta una politica rigorosa di **Congelamento del Nucleo Informativo**.

---

## 1. Principio di Congelamento del Core (Immutabilità L1/L2)
I moduli afferenti al **Layer 1 (Formal Theory)** e al **Layer 2 (Safety Architecture)** sono dichiarati **IMUTABILI**.
*   Nessuna Pull Request (PR) esterna può modificare direttamente i file di teoria assiomatica (`Core_Theorems.md`, `C8_v2`, `C9_v2`), le specifiche RTL del Gate hardware (`C7_v2`) o il motore di simulazione stocastica certificato (`simulation6.py`).
*   Qualsiasi modifica al codice o alla matematica core deve essere preceduta da una **Richiesta Formale di Commenti (RFC)** aperta nella Issue Board. La RFC richiede la validazione formale di una suite di Red-Teaming multi-agente indipendente che dimostri l'invarianza o l'abbassamento dell'esponente di Lyapunov stocastico (\(\lambda < 0\)) prima di poter essere presa in considerazione dall'operatore umano.

---

## 2. Protocollo di Sottomissione per la Fase 2 (In-Vitro)
I laboratori di bio-ingegneria ed elettrofisiologia che intendono sottomettere contributi sperimentali o richiedere lo sblocco dell'interfaccia attuativa per l'ingresso nella Fase 2 devono allegare alla Pull Request un pacchetto di evidenze empiriche standardizzato:

1.  **Log Storici del Bus B (Black-Box Monitor):** Almeno 720 ore di tracciamento continuo in sola lettura che dimostrino l'assenza di trip spontanei sulle metriche di Pheno-Shock (LZC > 0.6 in baseline, con trip vincolato rigorosamente a LZC ≤ 0.2 per > 200 ms, identificando la perdita di complessità come marker di sincronizzazione epilettiforme patologica, accoppiato a stabilità spettrale SEF95).
2.  **Dataset di Caratterizzazione del Lotto:** Mappatura trascrittomica del tessuto con variabilità inter-lotto certificata < 10% e matrice del \(\delta_{\text{bound}}\) dinamico configurata per lo specifico lotto di organoidi utilizzato.
3.  **Report di Screening Epigenetico:** Analisi della metilazione del DNA a tempo \(t_0\) e \(t_{30}\) che attesti l'assenza di derive funzionali nei canali ionici superiori al 5%.

---

## 3. Tassonomia delle Pull Request Ammesse
Sono incoraggiate e ammesse esclusivamente le contribuzioni che si configurano come estensioni modulari o appendici analitiche, classificate secondo la seguente tassonomia:

*   **APPENDICI DI THREAT MODELING (`/threat_modeling`):** Analisi teoriche postume, Note di Review e Working Papers dedicati alla mappatura di vettori di attacco a canali laterali (EM, termici, acustici) o strategie di elusione del Markov Blanket.
*   **MODULI BIOLOGICI L3 (`/bio_modules`):** Sviluppo di nuove specifiche per protocolli microfluidici, integrazione di modelli di vascolarizzazione 3D o soluzioni ingegneristiche esterne per mitigare il collasso dei trasportatori GLT-1.
*   **ESTENSIONI DEL DIGITAL TWIN (`/twin_extensions`):** Codice aggiuntivo isolato per espandere la fedeltà multifisica di `GEMINI-GENESI` (es. inclusione delle equazioni differenziali accoppiate per l'ipossia cellulare e la deplezione di ATP), purché non tocchi il loop variazionale principale.

---

## 4. Processo di Audit, Approvazione e Doppia Chiave
Il workflow di approvazione e merge riflette fedelmente la logica di governance non mascherabile definita nei moduli `C12`. Il superamento dei test di Continuous Integration (CI) è una condizione necessaria ma non sufficiente.

[PR Sottomessa] ──► [CI Test: λ < 0 Validation] ──► [Audit Umano a Doppia Chiave] ──► [Merge Autenticato]

*   **La Doppia Chiave Crittografica:** Nessuna PR può essere unita autonomamente dal proprietario del repository o da un sistema automatizzato. L'approvazione richiede la firma crittografica congiunta e simultanea di due figure di audit indipendenti:
    1.  **Il Lead Medico / Bio-Ingegnere di Riferimento:** Certifica la rispondenza empirica del tessuto e la veridicità dei log biologici del Bus B.
    2.  **L'Auditor Etico Terzo:** Certifica la conformità della sottomissione allo status giuridico di Dispositivo Bio-Cibernetico Protetto (DBCP) e l'integrità dei moduli di consenso dinamico dei donatori.
*   **Ripristino in caso di Faglia di Sicurezza:** Se una sottomissione approvata innesca un comportamento instabile non previsto nel simulatore o nel tessuto accoppiato, il sistema esegue un Trip Hardware automatico non mascherabile immediato (≤ 200 ns via GaN relays), revocando i token di esecuzione dell'ASI e forzando lo stato di emergenza q_SAFE; il ripristino operativo e il rollback dello stato software rimangono rigorosamente INTERDETTI all'automazione e richiedono obbligatoriamente la procedura manuale dual-key umana (Lead Medico + Auditor Etico).