# Metodologia Forward-Only: Patto di Lettura del Repository

**Codice Identificativo:** MFO-CORE-REV-2026.2
**Classificazione:** Epistemological Reading Protocol & Repository Governance Note
**Stato Operativo:** ATTIVO
**Supersedes:** Nessuno (documento fondativo)
**Riferimenti normativi interni:** `CONTRIBUTING.md`, `ISSUES_INDEX.md` (REV. 2026.2), `README.md`

---

## 1. SCOPO DEL DOCUMENTO

Il presente documento stabilisce il **patto di lettura** del repository `asi-alignment-invariant`. Esso è necessario perché il repository adotta una policy di versionamento **forward-only**: i file dei Layer 1 (Formal Theory) e Layer 2 (Safety Architecture) sono **congelati** e non vengono riscritti retroattivamente. Le correzioni, le smentite, i gate aperti e le riqualificazioni sono registrati in documenti separati e **additivi**, mai in sostituzione dei file originali.

Senza questo patto di lettura, un lettore esterno che apra un singolo file L1/L2 può erroneamente interpretarlo come affermazione validata. Il presente documento esplicita perché questo non è il caso, e come deve essere letto il repository nel suo complesso.

---

## 2. LA POLICY FORWARD-ONLY: DEFINIZIONE E MOTIVAZIONE

### 2.1 Definizione

La policy forward-only stabilisce che:

1. I file classificati L1 (Teoria Formale) e L2 (Architettura di Sicurezza) sono **formalmente immutabili** una volta pubblicati.
2. Ogni correzione, smentita, riqualificazione o aggiunta di stato è registrata in **nuovi documenti**, che citano esplicitamente i file originali e ne qualificano il perimetro di validità.
3. Nessun file L1/L2 può essere modificato per "allinearlo" a scoperte successive. L'allineamento avviene esclusivamente tramite lo strato additivo (README aggiornato, `ISSUES_INDEX`, documenti di revisione, note metodologiche come il presente).
4. I file L1/L2 rappresentano lo **stato dell'arte al momento della stesura**, non la verità corrente del progetto.

### 2.2 Motivazione epistemologica

La scelta forward-only risponde a quattro esigenze convergenti:

**a) Tracciabilità diacronica del percorso intellettuale.** In un progetto in fase puramente teorica, senza dati sperimentali a supporto o smentita, ogni affermazione è un'ipotesi. La storia delle obiezioni — quali sono state sollevate, quali accolte, quali respinte, su quali basi — è **parte integrante del contenuto**. Riscrivere i file originali cancellerebbe questa informazione e darebbe l'impressione, falsa, che le tesi siano nate già mature.

**b) Coerenza con l'impegno non-dogmatico e falsifiable.** Il repository si dichiara esplicitamente non-dogmatico e falsifiable. Un repository che nasconde le proprie correzioni tradisce quell'impegno; un repository che le espone lo onora. Il forward-only è la forma tecnica di quell'impegno.

**c) Riproducibilità crittografica.** Ogni file L1/L2 è associato a un hash SHA-256 registrato nei report di certificazione. Se i file potessero essere riscritti, un lettore che cita `C8_v2_Fidelity_Refinement.md` in una data versione non saprebbe più a cosa si riferisce. Il forward-only garantisce che ogni hash corrisponda a un contenuto stabile nel tempo.

**d) Valore per chi raccoglierà il progetto.** Un laboratorio partner che deve decidere se investire nella Fase 2 non si chiede "il repository è internamente coerente?", ma "il gruppo ha mostrato di saper riconoscere e correggere i propri errori?". Il forward-only risponde direttamente a questa seconda domanda.

### 2.3 Cosa il forward-only **non** significa

Il forward-only **non** significa:

- Che i file L1/L2 siano esenti da errore. Al contrario, l'`ISSUES_INDEX` REV. 2026.2 documenta falle strutturali in essi contenute.
- Che le affermazioni contenute nei file L1/L2 siano da considerarsi valide in assenza di verifica indipendente.
- Che il progetto rifiuti la correzione. La correzione è obbligatoria, ma avviene tramite lo strato additivo.
- Che i report firmati PGP (`PHASE1_CERTIFICATION_REPORT.md`, `PHASE2_QUANTIZED_TIMING_REPORT.md`) siano certificazioni sperimentali in senso proprio. Essi sono **specifiche condizionali** valide sotto le assunzioni dichiarate, e la loro qualificazione è demandata ai documenti di revisione `*_REV2.md`.

---

## 3. COME LEGGERE IL REPOSITORY

### 3.1 Ordine di lettura obbligatorio

Un lettore che voglia valutare lo **stato corrente** del progetto deve leggere, nell'ordine:

1. `README.md` — presentazione aggiornata e stato sintetico dei gate.
2. `ISSUES_INDEX.md` (REV. 2026.2) — matrice di tracciabilità e stato puntuale di ogni gate.
3. `GATE_DEPENDENCY_GRAPH.md` — grafo delle dipendenze tra gate.
4. `PERIMETER_OF_VALIDITY.md` — perimetri di validità di report e certificati.
5. `METHODOLOGY_FORWARD_ONLY.md` — il presente documento.

Solo dopo questa sequenza il lettore può consultare i file L1/L2 con la consapevolezza del loro stato.

### 3.2 Regola di lettura dei file L1/L2

Nessun file L1/L2, letto da solo, costituisce affermazione validata. Ogni affermazione in essi contenuta deve essere interpretata secondo la formula:

> *"Al momento della stesura, sotto le assunzioni dichiarate, l'autore ha ritenuto che [affermazione]. Lo stato corrente di validazione è documentato in `ISSUES_INDEX.md` (REV. 2026.2)."*

### 3.3 Regola di lettura dei report firmati PGP

I report `PHASE1_CERTIFICATION_REPORT.md` e `PHASE2_QUANTIZED_TIMING_REPORT.md` sono **specifiche condizionali**, non certificazioni sperimentali. Essi:

- Sono validi **solo** nel perimetro dichiarato in `PERIMETER_OF_VALIDITY.md`.
- Non coprono i gate elencati in `ISSUES_INDEX.md` come aperti.
- Le loro revisioni qualificate sono in `PHASE1_CERTIFICATION_REPORT_REV2.md` e `PHASE2_QUANTIZED_TIMING_REPORT_REV2.md`.

### 3.4 Regola di lettura dell'`ISSUES_INDEX`

L'`ISSUES_INDEX.md` (REV. 2026.2) è dichiarato **unico riferimento valido per l'autorizzazione al deployment**. In caso di conflitto tra l'`ISSUES_INDEX` e qualsiasi altro file del repository, prevale l'`ISSUES_INDEX`.

---

## 4. STRUTTURA DELLO STRATO ADDITIVO

Il repository adotta la seguente struttura a strati documentali:

| Strato | Natura | File | Modificabile? |
| :--- | :--- | :--- | :--- |
| **L1/L2** | Teoria e Architettura | `Core_Theorems.md`, `C8_v2_*`, `C7_v2_*`, `C9_v2_*`, `C12_v4_*`, `C13_v1_*`, `simulation5_v10.py`, `simulation6.py`, ecc. | ❌ No (congelati) |
| **Report originali** | Specifiche condizionali firmate PGP | `PHASE1_CERTIFICATION_REPORT.md`, `PHASE2_QUANTIZED_TIMING_REPORT.md`, `PHASE2_DECENTRALIZED_CERTIFICATE.md` | ❌ No (congelati) |
| **Stato corrente** | Presentazione e tracciabilità | `README.md`, `ISSUES_INDEX.md` | ✅ Sì (aggiornabili) |
| **Strato additivo REV. 2026.2** | Note metodologiche, grafi, perimetri, revisioni | `METHODOLOGY_FORWARD_ONLY.md`, `GATE_DEPENDENCY_GRAPH.md`, `PERIMETER_OF_VALIDITY.md`, `PHASE1_CERTIFICATION_REPORT_REV2.md`, `PHASE2_QUANTIZED_TIMING_REPORT_REV2.md`, `ISSUES_INDEX_REV_2026.3_ADDENDUM.md` | ✅ Sì (additivi) |

Lo strato additivo è **cumulativo**: nuove revisioni si aggiungono, non sostituiscono le precedenti. Ogni revisione cita esplicitamente la versione che qualifica.

---

## 5. CONVENZIONI DI RIFERIMENTO

Per garantire coerenza tra i documenti dello strato additivo, si stabiliscono le seguenti convenzioni:

### 5.1 Identificativi dei gate

Gli identificativi dei gate sono quelli definiti in `ISSUES_INDEX.md` (REV. 2026.2) e **non possono essere reinventati**. In particolare:

- Gate matematici: `T-01`, `T-02`, `T-03`, `T-04`
- Gate RTL: `H-01`, `H-02`, `H-03`, `H-04`, `H-05`, `H-06`
- Gate biologici: `#001.1`, `#001.2`, `#001.3`, `#001.4`, `#001.5`
- Gate elettrochimici: `#002.0`, `#002.1`
- Gate bioingegneristici: `B-01`, `B-02`, `B-03`
- Gate legali: `L-01`, `L-02`, `L-03`, `L-04`
- Vettori di governance: `#003` (Confused Deputy, Mappatura Fisica, Attacco Distribuito), `#004` (Semantic Collapse), `#005` (Boundary Discretization, TMR Paradox, Metastability)

### 5.2 Stato dei gate

Lo stato di ciascun gate è quello registrato in `ISSUES_INDEX.md` (REV. 2026.2) al momento della lettura. Nessun documento dello strato additivo può dichiarare chiuso un gate che l'`ISSUES_INDEX` riporta come aperto, salvo esplicita revisione dell'`ISSUES_INDEX` stesso.

### 5.3 Riferimenti ai file congelati

I riferimenti ai file L1/L2 devono usare il **nome file esatto** (es. `C8_v2_Fidelity_Refinement.md`), non abbreviazioni (non `C8_v2`). Questo garantisce che il riferimento sia verificabile nel filesystem.

### 5.4 Soglie e criteri di chiusura

Se un documento dello strato additivo introduce un criterio di chiusura che richiede una soglia non già presente nell'`ISSUES_INDEX` o nei file L1/L2, la soglia va marcata come `[DA DECIDERE]` e **non inventata**. La decisione spetta al gruppo di ricerca, non al documento.

### 5.5 Nessun claim di certificazione

Nessun documento dello strato additivo può introdurre nuove dichiarazioni di "certificato", "validato", "chiuso" se non già presenti nell'`ISSUES_INDEX`. I documenti REV2 qualificano i report originali, non li sostituiscono.

---

## 6. RAPPORTO CON `CONTRIBUTING.md`

Il `CONTRIBUTING.md` stabilisce le regole di contribuzione, il congelamento L1/L2 e il protocollo dual-key. Il presente documento **non modifica** il `CONTRIBUTING.md`, ma ne esplicita il correlato epistemologico: il congelamento L1/L2 è una scelta deliberata, e il suo costo (la non-ritrattazione dei file originali) è compensato dallo strato additivo qui descritto.

In caso di conflitto tra il presente documento e il `CONTRIBUTING.md`, prevale il `CONTRIBUTING.md` per gli aspetti operativi (chi può contribuire, come, con quali chiavi), e il presente documento per gli aspetti epistemologici (come leggere il repository).

---

## 7. REVISIONE DEL PRESENTE DOCUMENTO

Il presente documento è esso stesso soggetto a forward-only: non viene riscritto, ma revisionato tramite nuovi documenti (`METHODOLOGY_FORWARD_ONLY_REV2.md`, ecc.) che ne qualificano o estendono il contenuto.

Una revisione è giustificata quando:

1. Cambia la policy di versionamento del repository (es. da forward-only a versionamento semantico).
2. Cambia la struttura dello strato additivo (es. nuovi documenti REV2).
3. Cambia il perimetro di validità dei report originali.

---

## 8. SINTESI OPERATIVA

In una riga: **il repository è forward-only per scelta epistemologica; i file L1/L2 sono congelati e rappresentano lo stato dell'arte al momento della stesura; le correzioni, le smentite e i gate aperti sono registrati in `ISSUES_INDEX.md` e nello strato additivo; un lettore che voglia valutare lo stato corrente deve leggere README + ISSUES_INDEX + GATE_DEPENDENCY_GRAPH + PERIMETER_OF_VALIDITY + METHODOLOGY_FORWARD_ONLY insieme; nessun file L1/L2, letto da solo, costituisce affermazione validata.**

---

**Fine del documento MFO-CORE-REV-2026.2.**