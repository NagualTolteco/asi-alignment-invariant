

```markdown
# Phase 2 Quantized Timing Report — Revisione Qualificata REV2

**Codice Identificativo:** P2QTR-REV2-CORE-2026.2
**Classificazione:** Conditional Specification Requalification — Non-Experimental
**Stato Operativo:** ATTIVO / ADDITIVO
**Qualifica:** Specifica condizionale — NON certificazione sperimentale
**Documento originale qualificato:** `PHASE2_QUANTIZED_TIMING_REPORT.md`
**Riferimenti normativi interni:** `ISSUES_INDEX.md` (REV. 2026.2), `METHODOLOGY_FORWARD_ONLY.md` (MFO-CORE-REV-2026.2), `GATE_DEPENDENCY_GRAPH.md` (GDG-CORE-REV-2026.2), `PERIMETER_OF_VALIDITY.md` (POV-CORE-REV-2026.2), `PHASE1_CERTIFICATION_REPORT_REV2.md` (PCR-REV2-CORE-2026.2)

---

## 1. SCOPO DEL DOCUMENTO

Il presente documento è la **revisione qualificata** del `PHASE2_QUANTIZED_TIMING_REPORT.md`. Esso **non sostituisce** il report originale, che resta congelato e valido nel suo perimetro dichiarato. Esso **qualifica** il report originale alla luce di:

1. Le falle RTL scoperte dall'audit di Ottobre 2026 (Issue #1–#2).
2. I gate aperti documentati in `ISSUES_INDEX.md` (REV. 2026.2), in particolare `H-01..H-06`.
3. I perimetri di validità specificati in `PERIMETER_OF_VALIDITY.md` §3.3.
4. Il grafo delle dipendenze specificato in `GATE_DEPENDENCY_GRAPH.md` §4.2.

La funzione primaria è prevenire la **sopra-interpretazione** del report originale: un report che dichiara "assenza totale di violazioni Setup/Hold" e "trip $\le 30\,\text{ns}$" produce un'impressione di correttezza funzionale che **non è garantita**. La chiusura STA certifica il **netlist sintetizzato**, non la **correttezza del RTL** che lo ha generato né la **fedeltà del modello** che ha validato il RTL. Il presente documento esplicita questa distinzione.

---

## 2. STATO DEL REPORT ORIGINALE

### 2.1 Dati identificativi

| Campo | Valore |
| :--- | :--- |
| **Identificativo originale** | `PHASE2_QUANTIZED_TIMING_REPORT.md` |
| **Data di emissione** | 17 Ottobre 2026 |
| **Target di sintesi** | Digilent Cora Z7 (Zynq-7000), AMD-Xilinx Kria KV260 |
| **Tool** | Vivado STA (post-implementation) |
| **Metriche dichiarate** | $\text{WNS} = +1.642\,\text{ns}$, $\text{WHS} = +0.218\,\text{ns}$ |
| **Latenza trip dichiarata** | $\le 30\,\text{ns}$ |

### 2.2 Perimetro dichiarato nel report originale

Il report originale dichiara:

- Assenza totale di violazioni Setup/Hold sul netlist sintetizzato per Cora Z7 e Kria KV260.
- Latenza dell'albero combinatorio di trip entro $30\,\text{ns}$.
- Metastabilità zero (dichiarazione implicita nella chiusura STA).

### 2.3 Valutazione della qualifica

Il report originale **non è una certificazione di correttezza funzionale**. È un **report di temporizzazione** valido per il netlist sintetizzato sotto le assunzioni dichiarate. La differenza è sostanziale:

- Una **certificazione di correttezza funzionale** richiede che il RTL implementi la specifica dichiarata, verificata con testbench formale o simulazione esaustiva.
- Un **report di temporizzazione** certifica che il netlist sintetizzato rispetta i vincoli temporali (setup, hold, latenza), ma **non** che il netlist implementi la funzione corretta.

Il report originale appartiene alla seconda categoria, ma il suo formato (metriche positive, chiusura totale) può indurre il lettore a collocarlo nella prima. La presente revisione corregge questa ambiguità.

---

## 3. ASSUNZIONI SOTTO CUI IL REPORT È VALIDO

Il report originale è valido **solo** sotto le seguenti assunzioni:

| ID | Assunzione | Fonte | Gate condizionante |
| :--- | :--- | :--- | :--- |
| **A1** | Il netlist sintetizzato deriva da RTL conforme alla specifica `C7_v2_Hardware_RHA_Governor_and_RTL_Specifications.md`. | `C7_v2` §Specifica | `H-01`, `H-02`, `H-03`, `H-04`, `H-05` |
| **A2** | I vincoli XDC di `C13_v1_FPGA_Fixed_Point_Constraints.md` sono applicati correttamente. | `C13_v1` §Vincoli Master | Nessuno (vincoli dichiarati) |
| **A3** | Il modello di temporizzazione Vivado è accurato per il target dichiarato. | Tool Vivado | Nessuno (assunzione del tool) |
| **A4** | Il modello che ha validato il RTL (`simulation9.py`) è bit-true. | `C13_v2_Hardware_Validation_Ledger.md` | `H-06` |
| **A5** | Il contratto numerico è unificato (Q8.16). | `C13_v2` §Contratto | `H-05` |

**Nota critica:** le assunzioni A1, A4 e A5 non sono ipotesi di comodo: sono **condizioni la cui validità è oggetto di gate aperti**. Finché H-01..H-06 non sono chiusi, il report originale è valido **solo condizionalmente** su assunzioni non ancora verificate. La qualificazione corretta è quindi: *"Se A1–A5 valgono, allora il report è valido. La validità di A1, A4 e A5 è sospesa fino alla chiusura di H-01..H-06."*

---

## 4. GATE CONDIZIONANTI

### 4.1 Gate RTL

| Gate | Descrizione | Impatto sul report |
| :--- | :--- | :--- |
| **H-01** | Bug reset FSM: bypass lockout 1.50s al boot. | Il netlist sintetizzato implementa una FSM affetta da un bug che ne invalida il comportamento al boot. La chiusura STA è corretta, ma la FSM non è conforme alla specifica dichiarata. |
| **H-02** | Clamp DAC non combinatorio simultaneo. | Il netlist implementa un clamp sequenziale, non combinatorio. La latenza dichiarata ($\le 30\,\text{ns}$) potrebbe non essere rispettata in tutti i casi operativi. |
| **H-03** | Logica GALS dual-rail assente/malformata. | Il netlist non implementa l'isolamento GALS dichiarato. La metastabilità zero è dichiarata per il netlist sintetizzato, ma non per l'isolamento GALS. |
| **H-04** | BLF matematica assente da hardware. | Il netlist implementa comparatori statici, non la $V_{\text{BLF}}(x)$ dichiarata. La garanzia formale di invarianza in avanti non è implementata. |
| **H-05** | Conflitto Q8.16 vs $f=24$. | Il contratto numerico non è unificato. La catena ADC → CBF → DAC → log potrebbe essere incoerente. |
| **H-06** | `simulation9.py` non bit-true. | Il modello che ha validato il RTL opera in `float64`, non in emulazione bit-true. La chiusura STA certifica il netlist, ma non la fedeltà del modello che lo ha generato. |

### 4.2 Gate elettrochimici

| Gate | Descrizione | Impatto sul report |
| :--- | :--- | :--- |
| **#002.1** | Lisi elettrochimica da Gate Clamp Discontinuity & Boundary Riding. | Le remediation R-07.1/R-07.2/R-07.3 non sono implementate né validate. La temporizzazione del trip è corretta, ma la sicurezza elettrochimica del trip non è garantita. |

### 4.3 Gate matematici (indiretti)

Il report originale non dipende direttamente dai gate matematici T-01..T-04, ma la validità del modello che ha generato il RTL dipende da essi (vedi `PHASE1_CERTIFICATION_REPORT_REV2.md` §4.1). La catena è:

```
T-01..T-04 → validità del modello continuo → validità del RTL → validità del netlist → validità della chiusura STA
```

La chiusura STA è l'anello finale di una catena che dipende da gate a monte. Il presente documento rende esplicita questa dipendenza.

---

## 5. COSA IL REPORT ORIGINALE **NON** CERTIFICA

Il report originale **non certifica**:

1. **Correttezza funzionale del RTL.** I gate H-01..H-05 sono aperti: la FSM, il clamp, il GALS, la BLF e il contratto numerico non sono conformi alla specifica.
2. **Fedeltà bit-true.** H-06 è aperto: `simulation9.py` non emula la quantizzazione. La chiusura STA certifica il netlist, ma non la fedeltà del modello che lo ha validato.
3. **Sicurezza elettrochimica.** #002.1 è aperto: la lisi da clamp asimmetrico non è mitigata.
4. **Metastabilità zero in senso assoluto.** La chiusura STA dichiara assenza di violazioni Setup/Hold sul netlist, ma non certifica l'assenza di metastabilità in condizioni di fault injection o di attacco (`#005` Metastability Exploitation è aperto).
5. **Comportamento in condizioni non modellate.** Il report è valido per il netlist sintetizzato sotto le assunzioni A1–A5, non per scenari fuori perimetro (es. attacchi side-channel, guasti non previsti, variazioni di tensione/temperatura non modellate).
6. **Validità dei vettori di governance.** #003/#004/#005 sono aperti: Confused Deputy, Semantic Collapse, Boundary Discretization, TMR Paradox, Metastability non sono mitigati.

---

## 6. COSA IL REPORT ORIGINALE **CERTIFICA** (NEL SUO PERIMETRO)

Nel suo perimetro ristretto, il report originale **certifica**:

1. **Assenza di violazioni Setup/Hold** sul netlist sintetizzato per Cora Z7 e Kria KV260, con $\text{WNS} = +1.642\,\text{ns}$ e $\text{WHS} = +0.218\,\text{ns}$.
2. **Latenza dell'albero combinatorio di trip** entro $30\,\text{ns}$ sul netlist sintetizzato, sotto le assunzioni A1–A5.
3. **Accuratezza del modello di temporizzazione Vivado** per il target dichiarato (assunzione A3).

---

## 7. QUALIFICAZIONE FORMALE

Alla luce di quanto sopra, il report originale va citato con la seguente qualificazione formale:

> *"`PHASE2_QUANTIZED_TIMING_REPORT.md` è una **specifica condizionale** valida per il netlist sintetizzato su Cora Z7 e Kria KV260, sotto le assunzioni A1–A5 dichiarate in `C13_v1_FPGA_Fixed_Point_Constraints.md` e `C13_v2_Hardware_Validation_Ledger.md`. Esso **non costituisce** certificazione di correttezza funzionale del RTL, **non certifica** la fedeltà bit-true del modello (`simulation9.py`, H-06), e **non copre** i gate H-01..H-06, #002.1, #003/#004/#005 documentati in `ISSUES_INDEX.md` (REV. 2026.2). La chiusura STA certifica il netlist, non la correttezza del RTL che lo ha generato né la fedeltà del modello che ha validato il RTL. Il perimetro completo è in `PERIMETER_OF_VALIDITY.md` §3.3."*

Questa qualificazione va inclusa in ogni citazione esterna del report (paper, grant, presentazioni, documentazione di progetto).

---

## 8. RAPPORTO CON IL REPORT ORIGINALE

Il presente documento **non modifica** il report originale. Il report originale resta congelato nel suo perimetro dichiarato. Il presente documento:

- **Affianca** il report originale come strato additivo.
- **Qualifica** il report originale senza sostituirlo.
- **Esplicita** ciò che il report originale già dichiara implicitamente (le assunzioni A1–A5), ma rende esplicito il fatto che A1, A4 e A5 sono oggetto di gate aperti.
- **Rende visibile** ciò che il report originale non dichiara (i gate H-01..H-06, #002.1, #003/#004/#005).

In caso di conflitto tra il presente documento e il report originale, prevale il report originale **solo** per il perimetro dichiarato; per lo stato di validità prevale il presente documento (come stabilito in `PERIMETER_OF_VALIDITY.md` §5.3).

---

## 9. DISTINZIONE CRITICA: TEMPORIZZAZIONE ≠ CORRETTEZZA FUNZIONALE

Questa distinzione merita una sezione dedicata, perché è il cuore della qualificazione.

### 9.1 Cosa significa "chiusura STA"

La chiusura STA (Static Timing Analysis) verifica che il netlist sintetizzato rispetti i vincoli temporali:

- **Setup:** il dato arriva prima del clock edge, con margine sufficiente.
- **Hold:** il dato resta stabile dopo il clock edge, con margine sufficiente.
- **Latenza:** il percorso combinatorio ha una latenza entro il bound dichiarato.

Queste verifiche sono **necessarie** ma **non sufficienti** per la correttezza funzionale del netlist.

### 9.2 Perché la chiusura STA non implica correttezza funzionale

Un netlist può rispettare tutti i vincoli temporali e implementare una funzione **errata**. Esempi concreti nel repository:

- **H-01:** la FSM rispetta i tempi, ma il reset azzera `dwell_counter_reg` e bypassa il lockout. Il netlist è temporizzato correttamente e funzionalmente errato.
- **H-02:** il clamp DAC rispetta i tempi, ma non è combinatorio simultaneo. Il netlist è temporizzato correttamente e funzionalmente errato.
- **H-04:** la BLF è sostituita da comparatori statici. Il netlist è temporizzato correttamente e funzionalmente errato rispetto alla specifica dichiarata.

La chiusura STA è quindi **condizione necessaria ma non sufficiente** per la correttezza.

### 9.3 Implicazione per il report

Il report originale dichiara "metastabilità zero" e "trip $\le 30\,\text{ns}$". Queste dichiarazioni sono **corrette nel loro perimetro** (il netlist sintetizzato), ma **non implicano** che il RTL sia funzionalmente corretto. La qualificazione di §7 rende esplicita questa distinzione.

---

## 10. RACCOMANDAZIONI PER LA FASE 2

Per chi raccoglie il progetto in Fase 2, il presente documento raccomanda:

1. **Non citare il report originale come "certificazione di correttezza"** in contesti esterni senza la qualificazione di §7.
2. **Considerare il report originale come punto di partenza**, non come punto di arrivo: la correttezza funzionale del RTL va verificata con testbench formale (SVA) una volta chiusi H-01..H-05.
3. **Chiudere H-06 prima di ogni altra cosa**: la fedeltà bit-true è la condizione per validare la catena quantizzata.
4. **Riemettere il report in Fase 2** come `PHASE2_QUANTIZED_TIMING_REPORT_REV3.md` (o equivalente) una volta chiusi i gate, con la qualificazione aggiornata.
5. **Eseguire test HIL** per validare la metastabilità in condizioni di fault injection, come richiesto da `#005` Metastability Exploitation.

---

## 11. MANUTENZIONE DEL PRESENTE DOCUMENTO

Il presente documento è soggetto a forward-only: non viene riscritto, ma revisionato tramite `PHASE2_QUANTIZED_TIMING_REPORT_REV3.md` quando:

1. Un gate condizionante (H-01..H-06, #002.1) viene chiuso.
2. Il report originale viene riemesso in Fase 2.
3. La qualificazione formale di §7 viene ridefinita.

La revisione non sostituisce la versione precedente: la affianca.

---

## 12. SINTESI OPERATIVA

In una riga: **il `PHASE2_QUANTIZED_TIMING_REPORT.md` è una specifica condizionale valida per il netlist sintetizzato su Cora Z7 e Kria KV260 sotto le assunzioni A1–A5, non una certificazione di correttezza funzionale; la chiusura STA certifica il netlist, non il RTL né il modello che lo ha validato; la validità è sospesa fino alla chiusura di H-01..H-06; non copre #002.1 né #003/#004/#005; ogni citazione esterna deve includere la qualificazione di §7.**

---

**Fine del documento P2QTR-REV2-CORE-2026.2.**
```
