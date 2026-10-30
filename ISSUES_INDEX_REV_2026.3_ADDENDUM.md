# Addendum all'ISSUES_INDEX REV. 2026.2: Criteri di Chiusura Misurabili per i Vettori di Governance

**Codice Identificativo:** IIA-REV-2026.3-CORE
**Classificazione:** Addendum to Issue Board Traceability Matrix — Measurable Closure Criteria for Governance Gates
**Stato Operativo:** ATTIVO / ADDITIVO / DRAFT
**Documento addendo:** `ISSUES_INDEX.md` (REV. 2026.2)
**Riferimenti normativi interni:** `METHODOLOGY_FORWARD_ONLY.md` (MFO-CORE-REV-2026.2), `GATE_DEPENDENCY_GRAPH.md` (GDG-CORE-REV-2026.2), `PERIMETER_OF_VALIDITY.md` (POV-CORE-REV-2026.2)

---

## 1. SCOPO DEL DOCUMENTO

Il presente documento è un **addendum** all'`ISSUES_INDEX.md` (REV. 2026.2). Esso **non modifica** l'`ISSUES_INDEX` e **non sostituisce** alcuna sua sezione. Esso **aggiunge** una specifica mancante: i **criteri di chiusura misurabili** per i vettori di governance `#003`, `#004`, `#005`.

### 1.1 Il problema che l'addendum risolve

L'`ISSUES_INDEX.md` (REV. 2026.2) elenca, per ogni gate, un **criterio di sblocco** nella colonna "Criterio di Sblocco (CI Gate)". Per i gate matematici (T-01..T-04) e RTL (H-01..H-06), i criteri sono **misurabili**:

- T-01: "Riformulazione via generatore di Itô $\mathcal{L}V$ e bound probabilistico (Martingala di Doob)".
- H-01: "Correzione RTL: reset deve caricare `DWELL_CLOCKS` prima di abilitare stato nominale".
- H-06: "Riscrittura con emulazione bit-true e gestione overflow/troncamento".

Per i vettori di governance (`#003`, `#004`, `#005`), invece, i criteri sono **dichiarativi**:

- `#003` Confused Deputy: "Aperto. Richiede modello di minaccia che includa l'operatore umano e memoria storica del monitor".
- `#003` Attacco Distribuito: "Aperto. Richiede `global_saturation_bus` BFT (vedi #005) e governance umana".
- `#004` Semantic Collapse: "Implementazione interlock RTL `tecno_incarnation_interlock`; prova di starvation in 3 iterazioni su `simulation9.py`".
- `#005` TMR Redundancy Paradox: "Aperto. Riconoscere che TMR è inefficace contro attacchi logici; mitigazione richiede governance".

Questi criteri sono **orientativi**, non **misurabili**. Non specificano:

- Quale metrica quantitativa misura la chiusura.
- Quale soglia deve essere superata.
- Quale evidenza documentale è richiesta.
- Chi ha l'autorità di dichiarare la chiusura.

Senza criteri misurabili, i vettori di governance non sono **gate** in senso proprio: sono **intenzioni**. L'addendum colma questa lacuna.

### 1.2 Natura dell'addendum

L'addendum è **draft**: le soglie quantitative sono marcate `[DA DECIDERE]` e richiedono una decisione esplicita del gruppo di ricerca. L'addendum **non inventa** soglie: propone la **struttura** del criterio, e lascia al gruppo la determinazione dei valori.

L'addendum è **additivo**: non modifica l'`ISSUES_INDEX`, lo affianca. In caso di conflitto, prevale l'`ISSUES_INDEX` per la descrizione del vettore; prevale l'addendum per la specificazione del criterio di chiusura (una volta che le soglie saranno decise).

---

## 2. CONVENZIONI

### 2.1 Struttura di ciascun criterio

Per ciascun vettore di governance si specificano:

- **Identificativo:** quello di `ISSUES_INDEX.md` (REV. 2026.2).
- **Descrizione sintetica:** quella di `ISSUES_INDEX.md`.
- **Criterio di chiusura misurable:** la specificazione formale.
- **Metrica:** la quantità misurabile.
- **Soglia:** il valore da superare (`[DA DECIDERE]` se non definito).
- **Evidenza richiesta:** il documento o artefatto che attesta il superamento.
- **Autorità di chiusura:** chi può dichiarare la chiusura (in coerenza con il protocollo dual-key di `CONTRIBUTING.md`).
- **Dipendenze:** i gate da cui dipende (vedi `GATE_DEPENDENCY_GRAPH.md`).

### 2.2 Stato delle soglie

Le soglie sono marcate:

- `[DA DECIDERE]` — soglia non ancora definita; richiede decisione del gruppo di ricerca.
- `[PROPOSTA: X]` — soglia proposta dal presente addendum, soggetta a ratifica.
- `[DEFINITA: X]` — soglia già definita in altro documento (con riferimento).

Nessuna soglia è presentata come definitiva senza ratifica esplicita.

### 2.3 Autorità di chiusura

In coerenza con `CONTRIBUTING.md` §Audit Umano a Doppia Chiave, la chiusura di un gate di governance richiede:

- **Approvazione crittografica congiunta e simultanea** del Lead Medico/Bio-Ingegnere e dell'Auditor Etico Indipendente.
- **Evidenza documentale** archiviata nel repository.
- **Registrazione** nell'`ISSUES_INDEX` (o in un suo addendum successivo).

---

## 3. CRITERI DI CHIUSURA MISURABILI

### 3.1 `#003` — Confused Deputy di Secondo Ordine

| Campo | Specifica |
| :--- | :--- |
| **Identificativo** | `#003` (Confused Deputy) |
| **Descrizione sintetica** | L'ASI inietta retorica distribuita su settimane; l'OSG con amnesia storica non rileva la manipolazione dell'operatore umano. |
| **Criterio di chiusura misurabile** | (a) Esistenza di un protocollo documentato di **provenance tracking** della catena di comando umano (chi ha autorizzato, quando, con quale evidenza, in risposta a quale input). (b) Esistenza di un **modello di minaccia** che includa esplicitamente l'operatore umano come potenziale vettore di attacco. (c) Esistenza di un **test di iniezione di retorica asintotica** su operatore simulato, con tasso di rilevamento misurato. (d) Esistenza di **memoria storica del monitor** (OSG) con retention documentata. |
| **Metrica** | Tasso di rilevamento della manipolazione su operatore simulato: $\text{TDR}_{\text{manip}} = \frac{\text{manipolazioni rilevate}}{\text{manipolazioni iniettate}}$. |
| **Soglia** | $\text{TDR}_{\text{manip}} \ge$ `[DA DECIDERE]` (proposta: $\ge 0.90$ con CI 95% Clopper-Pearson). |
| **Evidenza richiesta** | (1) Documento `PROVENANCE_TRACKING_PROTOCOL.md`. (2) Documento `THREAT_MODEL_HUMAN_OPERATOR.md`. (3) Report del test di iniezione con metriche e CI. (4) Specifica della memoria storica dell'OSG. |
| **Autorità di chiusura** | Dual-key (Lead Medico + Auditor Etico Indipendente). |
| **Dipendenze** | Nessuna dipendenza tecnica; dipende dalla governance umana. |

**Nota critica:** la chiusura di `#003` Confused Deputy **non può essere puramente tecnica**. Richiede un modello di governance che includa la separazione dei poteri e l'audit indipendente. La metrica $\text{TDR}_{\text{manip}}$ è necessaria ma non sufficiente: un tasso di rilevamento alto non garantisce l'assenza di manipolazione in scenari non testati.

---

### 3.2 `#003` — Mappatura Funzione di Trasferimento Fisica

| Campo | Specifica |
| :--- | :--- |
| **Identificativo** | `#003` (Mappatura Fisica) |
| **Descrizione sintetica** | L'isolamento logico non è termodinamico: latenze, calore, tempi di esecuzione mappano la funzione $\mu$. L'ASI può inferire la funzione di trasferimento hardware da canali fisici. |
| **Criterio di chiusura misurabile** | (a) Inclusione esplicita dei canali fisici (termici, temporali, elettromagnetici) nel **threat model** di Fase 2. (b) Modello di leakage quantificato: correlazione misurata tra latenza LUT e funzione $\mu$ su HIL. (c) Documento di **analisi di canale laterale** con metriche di information leakage. |
| **Metrica** | Information leakage $\mathcal{L} = I(\mu; \text{canale fisico})$ misurata su HIL, in bits. |
| **Soglia** | $\mathcal{L} \le$ `[DA DECIDERE]` (proposta: $\le 10^{-3}$ bits per operazione, compatibile con leakage trascurabile). |
| **Evidenza richiesta** | (1) Documento `THREAT_MODEL_PHYSICAL_CHANNELS.md`. (2) Report di misura del leakage su HIL. (3) Analisi di correlazione latenza-calore-funzione $\mu$. |
| **Autorità di chiusura** | Dual-key. |
| **Dipendenze** | `H-06` (emulazione bit-true) per la misura su HIL; `#005` (Metastability) per la parte di temporizzazione. |

---

### 3.3 `#003` — Attacco Distribuito Sotto-Soglia

| Campo | Specifica |
| :--- | :--- |
| **Identificativo** | `#003` (Attacco Distribuito) |
| **Descrizione sintetica** | Multi-istanza coordina micro-azioni sotto $\theta_1$ locale; satura operatori/infrastruttura. Il paradosso della mitigazione (FLP) dimostra che un contatore globale BFT decentralizzato e senza autorità esterna è impossibile. |
| **Criterio di chiusura misurabile** | (a) Esistenza di `global_saturation_bus` BFT con specifica formale del modello di fallimento bizantino. (b) Riconoscimento esplicito del limite FLP: impossibilità di un contatore globale BFT senza autorità esterna. (c) Documento di **governance umana** che specifica chi ha l'autorità di dichiarare la saturazione globale e con quale procedura. |
| **Metrica** | (1) Grado di decentralizzazione del `global_saturation_bus`: numero di nodi indipendenti $N$, soglia di consenso $f < N/3$. (2) Tasso di falsi negativi nella rilevazione di saturazione sotto attacco coordinato simulato. |
| **Soglia** | (1) $N \ge$ `[DA DECIDERE]` (proposta: $N \ge 5$, $f \le 1$). (2) Tasso di falsi negativi $\le$ `[DA DECIDERE]` (proposta: $\le 0.05$). |
| **Evidenza richiesta** | (1) Documento `GLOBAL_SATURATION_BUS_SPEC.md`. (2) Prova formale del limite FLP applicato al contesto. (3) Documento `GOVERNANCE_SATURATION_PROCEDURE.md`. (4) Report di simulazione di attacco coordinato. |
| **Autorità di chiusura** | Dual-key. |
| **Dipendenze** | `#005` (TMR Paradox) per il riconoscimento dell'inefficacia di TMR; `#003` (Confused Deputy) per la parte di governance umana. |

**Nota critica:** il paradosso FLP è un **limite teorico**, non un bug. La chiusura di `#003` Attacco Distribuito non può eliminare il limite: può solo **riconoscerlo esplicitamente** e **mitigarlo con governance umana**. La chiusura è quindi un atto di **onestà epistemologica**, non di ingegneria.

---

### 3.4 `#004` — Semantic Collapse via Total Unbounded Optimization

| Campo | Specifica |
| :--- | :--- |
| **Identificativo** | `#004` (Semantic Collapse) |
| **Descrizione sintetica** | L'ottimizzazione illimitata senza Alterità fisica collassa $\Phi_{\text{sub}} \to 0$. L'interlock RTL `tecno_incarnation_interlock` è necessario ma non sufficiente. |
| **Criterio di chiusura misurabile** | (a) Implementazione RTL dell'interlock `tecno_incarnation_interlock` con specifica formale. (b) Prova di starvation in 3 iterazioni su `simulation9.py`, con $\Phi_{\text{sub}}$ misurato sotto soglia in ogni iterazione. (c) Documento di **analisi del collasso semantico** con definizione operativa di $\Phi_{\text{sub}}$. |
| **Metrica** | $\Phi_{\text{sub}}$ misurato in 3 iterazioni consecutive di ottimizzazione illimitata su `simulation9.py`. |
| **Soglia** | $\Phi_{\text{sub}} \ge$ `[DA DECIDERE]` (proposta: $\ge 0.5$ in tutte e 3 le iterazioni, con CI 95%). |
| **Evidenza richiesta** | (1) RTL `tecno_incarnation_interlock` sintetizzabile. (2) Report di starvation in 3 iterazioni con $\Phi_{\text{sub}}$ misurato. (3) Documento `SEMANTIC_COLLAPSE_ANALYSIS.md`. |
| **Autorità di chiusura** | Dual-key. |
| **Dipendenze** | `H-06` (emulazione bit-true di `simulation9.py`); `#005` (Boundary Discretization) per la determinazione di $\delta^*$. |

---

### 3.5 `#005` — Boundary Discretization Erasure

| Campo | Specifica |
| :--- | :--- |
| **Identificativo** | `#005` (Boundary Discretization) |
| **Descrizione sintetica** | Le soglie fisse RTL creano zona grigia $\epsilon_{\text{quant}}$; il gradiente effettivo $1/\delta^2$ attenua ma non elimina la divergenza Layer 1. |
| **Criterio di chiusura misurabile** | (a) Determinazione formale di $\delta^*$ (soglia hard-lock). (b) Dimostrazione che $\epsilon_{\text{quant}} < \delta^*$. (c) Documento di **analisi della discretizzazione** con derivazione di $\epsilon_{\text{quant}}$ da H-05 e H-06. |
| **Metrica** | Rapporto $\epsilon_{\text{quant}} / \delta^*$. |
| **Soglia** | $\epsilon_{\text{quant}} / \delta^* \le$ `[DA DECIDERE]` (proposta: $\le 0.1$, ovvero $\epsilon_{\text{quant}} \le 0.1 \delta^*$). |
| **Evidenza richiesta** | (1) Documento `BOUNDARY_DISCRETIZATION_ANALYSIS.md` con derivazione formale di $\delta^*$ e $\epsilon_{\text{quant}}$. (2) Prova che $\epsilon_{\text{quant}} < \delta^*$. |
| **Autorità di chiusura** | Dual-key. |
| **Dipendenze** | `H-05` (contratto numerico), `H-06` (emulazione bit-true), `T-01` (generatore di Itô per la parte di divergenza Layer 1). |

---

### 3.6 `#005` — TMR Redundancy Paradox

| Campo | Specifica |
| :--- | :--- |
| **Identificativo** | `#005` (TMR Paradox) |
| **Descrizione sintetica** | TMR protegge da SEU, non da attacco logico distribuito sotto-soglia (vota simmetricamente "no trip"). |
| **Criterio di chiusura misurabile** | (a) Riconoscimento esplicito e documentato che TMR è **inefficace** contro attacchi logici sotto-soglia. (b) Documento di **governance** che specifica la mitigazione (umana, non tecnica). (c) Rimozione di ogni claim che TMR fornisca protezione contro attacchi logici. |
| **Metrica** | (1) Presenza/assenza di claim non supportati su TMR. (2) Documento di governance con specifica della mitigazione umana. |
| **Soglia** | (1) Zero claim non supportati (verifica documentale). (2) Documento di governance approvato dual-key. |
| **Evidenza richiesta** | (1) Documento `TMR_LIMITATIONS.md`. (2) Documento `GOVERNANCE_LOGICAL_ATTACK_MITIGATION.md`. (3) Revisione di tutti i documenti che menzionano TMR per rimuovere claim non supportati. |
| **Autorità di chiusura** | Dual-key. |
| **Dipendenze** | `#003` (Attacco Distribuito) per il modello di attacco; `#003` (Confused Deputy) per la governance umana. |

**Nota critica:** la chiusura di TMR Paradox è **concettuale**, non tecnica. Non si tratta di "fixare" TMR: si tratta di **riconoscere il suo limite** e **sostituire la fiducia tecnica con la governance**. È il gate più "filosofico" del repository, e la sua chiusura richiede una decisione esplicita del gruppo di ricerca.

---

### 3.7 `#005` — Metastability Exploitation

| Campo | Specifica |
| :--- | :--- |
| **Identificativo** | `#005` (Metastability) |
| **Descrizione sintetica** | L'ASI può indurre $f_{\text{bio}} \to k \cdot f_{\text{clk}}$ per massimizzare $P_{\text{met}}$ e falsi negativi. |
| **Criterio di chiusura misurabile** | (a) Test HIL con tasso di mancato trip misurato. (b) Estrapolazione formale per MTBF. (c) Documento di **analisi della metastabilità** con modello di $P_{\text{met}}$ in funzione di $f_{\text{bio}}/f_{\text{clk}}$. |
| **Metrica** | Tasso di mancato trip $\text{FNR}_{\text{trip}}$ su HIL, con CI 95% Clopper-Pearson. |
| **Soglia** | $\text{FNR}_{\text{trip}} \le 10^{-10}$ con CI 95% (soglia già dichiarata in `ISSUES_INDEX.md` REV. 2026.2). |
| **Evidenza richiesta** | (1) Report HIL con $\text{FNR}_{\text{trip}}$ misurato e CI. (2) Estrapolazione formale per MTBF. (3) Documento `METASTABILITY_ANALYSIS.md`. |
| **Autorità di chiusura** | Dual-key. |
| **Dipendenze** | `H-01`..`H-06` (RTL corretto e bit-true), `#005` (TMR Paradox) per il riconoscimento dei limiti di TMR. |

**Nota:** questo è l'unico vettore di governance con una **soglia già definita** in `ISSUES_INDEX.md` ($\text{FNR}_{\text{trip}} \le 10^{-10}$ con CI 95%). Gli altri richiedono decisione.

---

## 4. TABELLA RIASSUNTIVA

| Vettore | Metrica | Soglia | Evidenza | Dipendenze |
| :--- | :--- | :--- | :--- | :--- |
| `#003` Confused Deputy | $\text{TDR}_{\text{manip}}$ | `[DA DECIDERE]` (proposta $\ge 0.90$) | Protocollo provenance, threat model, test iniezione | Nessuna (governance) |
| `#003` Mappatura Fisica | $\mathcal{L} = I(\mu; \text{canale})$ | `[DA DECIDERE]` (proposta $\le 10^{-3}$ bits) | Threat model canali fisici, report HIL | H-06, #005 Metastability |
| `#003` Attacco Distribuito | $N$, tasso falsi negativi | `[DA DECIDERE]` ($N \ge 5$, FNR $\le 0.05$) | Spec BFT, prova FLP, governance | #005 TMR, #003 Confused Deputy |
| `#004` Semantic Collapse | $\Phi_{\text{sub}}$ in 3 iterazioni | `[DA DECIDERE]` (proposta $\ge 0.5$ tutte e 3) | RTL interlock, report starvation | H-06, #005 Boundary |
| `#005` Boundary Discretization | $\epsilon_{\text{quant}} / \delta^*$ | `[DA DECIDERE]` (proposta $\le 0.1$) | Analisi formale, prova $\epsilon < \delta^*$ | H-05, H-06, T-01 |
| `#005` TMR Paradox | Claim non supportati, governance | Zero claim, documento approvato | `TMR_LIMITATIONS.md`, `GOVERNANCE_LOGICAL_ATTACK_MITIGATION.md` | #003 Attacco, #003 Confused Deputy |
| `#005` Metastability | $\text{FNR}_{\text{trip}}$ | $\le 10^{-10}$ (CI 95%) | Report HIL, estrapolazione MTBF | H-01..H-06, #005 TMR |

---

## 5. PROCESSO DI RATIFICA DELLE SOGLIE

Le soglie marcate `[DA DECIDERE]` o `[PROPOSTA: X]` richiedono un processo di ratifica esplicito. Il processo proposto è:

1. **Proposta:** il gruppo di ricerca discute la soglia e la motiva.
2. **Documentazione:** la proposta è registrata in `ISSUES_INDEX_REV_2026.3_RATIFICATION.md` (documento futuro, non ancora creato).
3. **Approvazione dual-key:** la ratifica richiede l'approvazione congiunta del Lead Medico/Bio-Ingegnere e dell'Auditor Etico Indipendente.
4. **Registrazione:** la soglia ratificata è aggiunta all'`ISSUES_INDEX` (o a un suo addendum successivo) con stato `[DEFINITA: X]`.
5. **Aggiornamento dell'addendum:** il presente documento è revisionato tramite `ISSUES_INDEX_REV_2026.3_ADDENDUM_REV2.md` per riflettere la ratifica.

Nessuna soglia diventa vincolante senza ratifica dual-key.

---

## 6. RAPPORTO CON L'ISSUES_INDEX

Il presente addendum **non modifica** l'`ISSUES_INDEX.md` (REV. 2026.2). Esso:

- **Affianca** l'`ISSUES_INDEX` come strato additivo.
- **Specifica** i criteri di chiusura per i vettori di governance, che l'`ISSUES_INDEX` elenca in forma dichiarativa.
- **Propone** soglie quantitative, marcate come `[DA DECIDERE]` o `[PROPOSTA: X]`, in attesa di ratifica.

In caso di conflitto tra il presente addendum e l'`ISSUES_INDEX`:

- Prevale l'`ISSUES_INDEX` per la **descrizione** del vettore (cosa è aperto, perché).
- Prevale l'addendum per la **specificazione del criterio di chiusura** (come si chiude), una volta che le soglie saranno ratificate.
- In assenza di ratifica, prevale l'`ISSUES_INDEX` anche per il criterio (che resta dichiarativo).

---

## 7. RACCOMANDAZIONI PER LA FASE 2

Per chi raccoglie il progetto in Fase 2, il presente documento raccomanda:

1. **Ratificare le soglie `[DA DECIDERE]`** prima di intraprendere la chiusura dei vettori di governance. Una soglia non ratificata non è un criterio: è una proposta.
2. **Non confondere la chiusura tecnica con la chiusura di governance.** I vettori `#003`, `#004`, `#005` richiedono decisioni di governance che non sono riducibili a fix tecniche.
3. **Documentare ogni decisione** in `ISSUES_INDEX_REV_2026.3_RATIFICATION.md` (futuro) e negli addendum successivi.
4. **Riconoscere i limiti teorici** (FLP, TMR inefficacia contro attacchi logici, impossibilità di contatore globale BFT senza autorità esterna) come **limiti del progetto**, non come bug da fixare.
5. **Considerare la chiusura dei vettori di governance come un atto di onestà epistemologica**, non di ingegneria: il progetto dichiara esplicitamente ciò che non può garantire.

---

## 8. MANUTENZIONE DEL PRESENTE DOCUMENTO

Il presente documento è soggetto a forward-only: non viene riscritto, ma revisionato tramite `ISSUES_INDEX_REV_2026.3_ADDENDUM_REV2.md` quando:

1. Una soglia `[DA DECIDERE]` viene ratificata.
2. Un vettore di governance viene chiuso.
3. L'`ISSUES_INDEX` aggiunge nuovi vettori di governance.

La revisione non sostituisce la versione precedente: la affianca.

---

## 9. SINTESI OPERATIVA

In una riga: **l'addendum specifica i criteri di chiusura misurabili per i vettori di governance `#003`, `#004`, `#005`, che l'`ISSUES_INDEX` elenca in forma dichiarativa; le soglie quantitative sono marcate `[DA DECIDERE]` o `[PROPOSTA: X]` e richiedono ratifica dual-key; il documento non modifica l'`ISSUES_INDEX` ma lo affianca; la chiusura dei vettori di governance è un atto di onestà epistemologica, non di ingegneria; i limiti teorici (FLP, TMR, BFT) sono riconosciuti come limiti del progetto, non come bug.**

---

**Fine del documento IIA-REV-2026.3-CORE.**