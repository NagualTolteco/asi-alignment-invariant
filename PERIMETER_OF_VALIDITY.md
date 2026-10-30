# Perimetri di Validità: Specifiche Condizionali e Limiti di Applicazione

**Codice Identificativo:** POV-CORE-REV-2026.2
**Classificazione:** Validity Perimeter Specification & Conditional Certification Ledger
**Stato Operativo:** ATTIVO / ADDITIVO
**Riferimenti normativi interni:** `ISSUES_INDEX.md` (REV. 2026.2), `METHODOLOGY_FORWARD_ONLY.md` (MFO-CORE-REV-2026.2), `GATE_DEPENDENCY_GRAPH.md` (GDG-CORE-REV-2026.2), `CONTRIBUTING.md`

---

## 1. SCOPO DEL DOCUMENTO

Il presente documento esplicita i **perimetri di validità** di ciascun report, certificato e registro del repository `asi-alignment-invariant`. Un perimetro di validità è la specificazione formale di:

1. **Cosa** il documento certifica o dichiara.
2. **Sotto quali assunzioni** la dichiarazione è valida.
3. **Cosa non copre** (e quindi non può essere invocato a sostegno di).
4. **Quali gate aperti** ne condizionano la validità.

La funzione primaria è prevenire la **sopra-interpretazione** dei report firmati PGP e dei certificati: un report ben formato, con hash SHA-256 e firme dual-key, non è una certificazione sperimentale se le assunzioni su cui poggia non sono verificate. Il presente documento rende esplicito questo confine.

Il documento è **additivo** rispetto ai report originali e non li modifica. Le riqualificazioni formali sono demandate a `PHASE1_CERTIFICATION_REPORT_REV2.md` (file 4) e `PHASE2_QUANTIZED_TIMING_REPORT_REV2.md` (file 5).

---

## 2. CONVENZIONI

### 2.1 Struttura di ciascun perimetro

Per ciascun documento si specificano:

- **Documento:** nome file esatto.
- **Natura:** certificazione sperimentale / specifica condizionale / registro / certificato di apertura.
- **Perimetro dichiarato:** cosa il documento copre.
- **Assunzioni:** sotto quali ipotesi la dichiarazione è valida.
- **Gate condizionanti:** quali gate aperti in `ISSUES_INDEX.md` (REV. 2026.2) ne condizionano la validità.
- **Cosa non copre:** cosa il documento non può essere invocato a sostenere.
- **Riqualificazione:** dove è demandata la qualificazione formale (file 4 o 5 dello strato additivo).

### 2.2 Stato di validità

Ciascun perimetro è classificato come:

- **`VALIDO NEL PERIMETRO`**: la dichiarazione è valida sotto le assunzioni esplicitate.
- **`CONDIZIONATO`**: la dichiarazione è valida solo se i gate condizionanti sono chiusi.
- **`SOSPESO`**: la dichiarazione non è validabile finché i gate condizionanti non sono chiusi.

### 2.3 Riferimenti

I riferimenti ai gate usano gli identificativi di `METHODOLOGY_FORWARD_ONLY.md` §5.1. I riferimenti ai file usano il nome file esatto.

---

## 3. PERIMETRI DI VALIDITÀ

### 3.1 `PHASE1_CERTIFICATION_REPORT.md`

| Campo | Specifica |
| :--- | :--- |
| **Natura** | Specifica condizionale firmata PGP (non certificazione sperimentale) |
| **Perimetro dichiarato** | Chiusura matematica e fisica della Fase 1 in-silico: contrazione asintotica $\lambda = -1.659528 \ll 0$ su modello continuo; architettura VU9P con $\delta_{\text{bound}} = 0.383\,\mu\text{M}$; NMI su relè GaN ($\le 200\,\text{ns}$); registri forensi SHA-256; firme PGP Dual-Key. |
| **Assunzioni** | (A1) Modello continuo, senza quantizzazione. (A2) Assiomi A1–A5 di `C8_v2_Fidelity_Refinement.md` validi. (A3) Ipotesi gaussiana locale sul manifold NESS valida. (A4) Generatore di Itô applicabile. (A5) Metriche topologiche sufficienti per la non-collisione spettrale. |
| **Gate condizionanti** | `T-01` (generatore di Itô), `T-02` (ipotesi non gaussiane), `T-03` (mutua singolarità), `T-04` (metriche topologiche). |
| **Stato di validità** | `CONDIZIONATO` — valido per il perimetro in-silico continuo sotto A1–A5; non valido come certificazione sperimentale. |
| **Cosa non copre** | (a) Quantizzazione Q8.16 (vedi `C13_v2` e `PHASE2_QUANTIZED_TIMING_REPORT`). (b) Bug RTL `H-01..H-06`. (c) Lisi elettrochimica `#002.1`. (d) Non-conformità legali `L-01..L-04`. (e) Vettori di governance `#003/#004/#005`. (f) Evidenze sperimentali (nessuna sperimentazione è stata eseguita). |
| **Riqualificazione** | `PHASE1_CERTIFICATION_REPORT_REV2.md` (file 4) |

**Nota critica:** il report dichiara conformità a DO-254 DAL-A e IEC 61508 SIL-4. Questi standard richiedono **evidenze di test**, non solo dimostrazioni analitiche. Il repository è in fase teorica; nessuna evidenza sperimentale è disponibile. La qualificazione formale deve quindi esplicitare che la "certificazione" è **condizionale e non sperimentale**, e che la conformità agli standard è **demandata alla Fase 2**.

---

### 3.2 `PHASE2_DECENTRALIZED_CERTIFICATE.md`

| Campo | Specifica |
| :--- | :--- |
| **Natura** | Certificato di convergenza in-silico (non certificazione sperimentale) |
| **Perimetro dichiarato** | Chiusura in-silico della variante decentralizzata: contrazione asintotica $\lambda = -1.659815$ e tempo di dimezzamento $\tau_{1/2} = 0.418\,\text{s}$ sotto rumore di Johnson amplificato del $+25\%$, su 64 canali passivi. |
| **Assunzioni** | (A1) Modello continuo. (A2) Rumore Johnson modellato come gaussiano additivo. (A3) Canali passivi ideali, senza derive di offset. (A4) Assiomi A1–A5 di `C8_v2` validi. |
| **Gate condizionanti** | `T-01`, `T-02`, `T-03`, `T-04`, `H-06` (per la trasposizione bit-true). |
| **Stato di validità** | `CONDIZIONATO` — valido per il modello continuo; non valido per l'emulazione bit-true. |
| **Cosa non copre** | (a) Emulazione bit-true Q8.16 (`H-06`). (b) Comportamento su hardware reale (nessuna sintesi su Cora Z7/Kria è stata validata sperimentalmente). (c) Latenze di trasporto non modellate. |
| **Riqualificazione** | Non è previsto un file REV2 dedicato; la qualificazione è coperta dal presente documento e dal `README.md` aggiornato. |

---

### 3.3 `PHASE2_QUANTIZED_TIMING_REPORT.md`

| Campo | Specifica |
| :--- | :--- |
| **Natura** | Report di sintesi STA (specifica condizionale, non certificazione sperimentale) |
| **Perimetro dichiarato** | Assenza totale di violazioni Setup/Hold ($\text{WNS} = +1.642\,\text{ns}$, $\text{WHS} = +0.218\,\text{ns}$) sul netlist sintetizzato per Cora Z7 e Kria KV260; latenza dell'albero combinatorio di trip entro $30\,\text{ns}$. |
| **Assunzioni** | (A1) Netlist sintetizzato da RTL conforme alla specifica `C7_v2` (ma vedi gate condizionanti). (A2) Vincoli XDC di `C13_v1` applicati correttamente. (A3) Modello di temporizzazione Vivado accurato per il target. |
| **Gate condizionanti** | `H-01` (reset FSM), `H-02` (clamp combinatorio), `H-03` (GALS dual-rail), `H-04` (BLF hardware), `H-05` (contratto numerico), `H-06` (emulazione bit-true). |
| **Stato di validità** | `SOSPESO` — la chiusura STA è formalmente corretta sul netlist, ma il netlist implementa un RTL affetto da H-01..H-05, e il modello che lo ha generato non è bit-true (H-06). La validità della temporizzazione non implica la validità funzionale. |
| **Cosa non copre** | (a) Correttezza funzionale del RTL (H-01..H-05). (b) Fedeltà del modello `simulation9.py` (H-06). (c) Comportamento in presenza di fault injection. (d) Metastability exploitation (`#005`). |
| **Riqualificazione** | `PHASE2_QUANTIZED_TIMING_REPORT_REV2.md` (file 5) |

**Nota critica:** il report è tecnicamente corretto nel suo perimetro (la chiusura STA è reale), ma **non sana i bug logici**. Un netlist che rispetta i tempi ma implementa un reset FSM difettoso (H-01) è un netlist temporizzato correttamente e funzionalmente errato. La distinzione va esplicitata in ogni riferimento al report.

---

### 3.4 `C13_v2_Hardware_Validation_Ledger.md`

| Campo | Specifica |
| :--- | :--- |
| **Natura** | Registro di validazione numerica (specifica condizionale) |
| **Perimetro dichiarato** | Conservazione della contrazione ergodica con $\lambda = -1.405263 \ll 0$ su implementazione FPGA in virgola fissa Q8.16, rispetto al modello ideale a 64 bit. |
| **Assunzioni** | (A1) Modello Q8.16 effettivamente emulato in `simulation9.py` (ma vedi H-06). (A2) Contratto numerico unificato su tutta la catena (ma vedi H-05). (A3) Overflow e troncamento gestiti esplicitamente. |
| **Gate condizionanti** | `H-05` (contratto numerico), `H-06` (emulazione bit-true). |
| **Stato di validità** | `SOSPESO` — la validità del registro è subordinata alla chiusura di H-06. Finché `simulation9.py` non è bit-true, la contrazione $\lambda = -1.405263$ è verificata su un modello che non è quello che verrà sintetizzato. |
| **Cosa non copre** | (a) Fedeltà del modello `simulation9.py` (H-06). (b) Comportamento su hardware reale. (c) Robustezza a fault injection. |
| **Riqualificazione** | Coperta dal presente documento e dal `README.md` aggiornato; non è previsto un REV2 dedicato. |

---

### 3.5 `Model_Code_Alignment_Matrix.md`

| Campo | Specifica |
| :--- | :--- |
| **Natura** | Matrice di conformità modello-codice (specifica condizionale) |
| **Perimetro dichiarato** | Validazione punto per punto della corrispondenza tra i modelli teorici (L1) e i simulatori (L2) per la Fase 1 in-silico. |
| **Assunzioni** | (A1) I file L1/L2 sono nella versione congelata. (A2) I simulatori eseguono il modello dichiarato. |
| **Gate condizionanti** | `T-01..T-04`, `H-01..H-06`. |
| **Stato di validità** | `CONDIZIONATO` — la matrice certifica la corrispondenza **strutturale**, non la correttezza **matematica** del modello (che dipende da T-01..T-04) né la fedeltà **bit-true** del simulatore (H-06). |
| **Cosa non copre** | (a) Validità matematica dei teoremi (T-01..T-04). (b) Correttezza RTL (H-01..H-05). (c) Fedeltà bit-true (H-06). |
| **Riqualificazione** | Coperta dal presente documento e dal `README.md` aggiornato. |

---

### 3.6 `Model_Code_Alignment_Matrix_v2.md`

| Campo | Specifica |
| :--- | :--- |
| **Natura** | Matrice di conformità per infrastruttura frugale (specifica condizionale) |
| **Perimetro dichiarato** | Validazione punto per punto della corrispondenza tra `C11_v3`, `simulation6_frugal.py` e lo stress-test `simulation8.py`. |
| **Assunzioni** | (A1) I file L1/L2 sono nella versione congelata. (A2) Il percorso frugale è correttamente mappato. |
| **Gate condizionanti** | `T-04` (filtri FFT), `H-06` (simulation9 bit-true), `#005` (Boundary Discretization). |
| **Stato di validità** | `CONDIZIONATO` — la matrice certifica la corrispondenza strutturale, ma la validità dei filtri FFT dipende da T-04 e la validità del percorso bit-true dipende da H-06. |
| **Cosa non copre** | (a) Validità formale dei filtri FFT (T-04). (b) Fedeltà bit-true (H-06). (c) Comportamento su hardware reale. |
| **Riqualificazione** | Coperta dal presente documento e dal `README.md` aggiornato. |

---

### 3.7 `ISSUES_INDEX.md` (REV. 2026.2)

| Campo | Specifica |
| :--- | :--- |
| **Natura** | Matrice di tracciabilità (riferimento normativo interno) |
| **Perimetro dichiarato** | Mappatura deterministica e biunivoca tra l'Issue Board e i file del filesystem locale; stato puntuale di ciascun gate; criteri di sblocco. |
| **Assunzioni** | (A1) I file L1/L2 sono nella versione congelata. (A2) Gli identificativi dei gate sono stabili. |
| **Gate condizionanti** | Nessuno: l'`ISSUES_INDEX` **è** il riferimento per lo stato dei gate. |
| **Stato di validità** | `VALIDO NEL PERIMETRO` — l'`ISSUES_INDEX` è dichiarato "unico riferimento valido per l'autorizzazione al deployment" e prevale su ogni altro documento in caso di conflitto. |
| **Cosa non copre** | (a) Struttura delle dipendenze tra gate (coperta da `GATE_DEPENDENCY_GRAPH.md`). (b) Perimetri di validità dei report (coperti dal presente documento). (c) Criteri di chiusura misurabili per i vettori di governance (demandati a `ISSUES_INDEX_REV_2026.3_ADDENDUM.md`, file 6). |
| **Riqualificazione** | Non applicabile: è il riferimento normativo. |

---

### 3.8 `CONTRIBUTING.md`

| Campo | Specifica |
| :--- | :--- |
| **Natura** | Policy di contribuzione e governance |
| **Perimetro dichiarato** | Regole di contribuzione, congelamento L1/L2, protocollo dual-key, tassonomia delle PR ammesse. |
| **Assunzioni** | (A1) Il protocollo dual-key è operativo. (A2) Gli auditor indipendenti sono nominati. |
| **Gate condizionanti** | `L-01..L-04` (per la parte di governance legale). |
| **Stato di validità** | `CONDIZIONATO` — la parte operativa (congelamento, dual-key, tassonomia PR) è valida; la parte di governance legale dipende da L-01..L-04. |
| **Cosa non copre** | (a) Validità legale delle clausole DBCP (L-01, L-02, L-03). (b) Conformità GDPR di `q_SAFE` (L-04). |
| **Riqualificazione** | Coperta dal presente documento e dal `README.md` aggiornato. |

---

## 4. TABELLA RIASSUNTIVA

| Documento | Natura | Stato | Gate condizionanti principali | Riqualificazione |
| :--- | :--- | :--- | :--- | :--- |
| `PHASE1_CERTIFICATION_REPORT.md` | Specifica condizionale | `CONDIZIONATO` | T-01, T-02, T-03, T-04 | File 4 (`*_REV2.md`) |
| `PHASE2_DECENTRALIZED_CERTIFICATE.md` | Certificato in-silico | `CONDIZIONATO` | T-01..T-04, H-06 | README aggiornato |
| `PHASE2_QUANTIZED_TIMING_REPORT.md` | Report STA | `SOSPESO` | H-01..H-06 | File 5 (`*_REV2.md`) |
| `C13_v2_Hardware_Validation_Ledger.md` | Registro validazione | `SOSPESO` | H-05, H-06 | README aggiornato |
| `Model_Code_Alignment_Matrix.md` | Matrice conformità | `CONDIZIONATO` | T-01..T-04, H-01..H-06 | README aggiornato |
| `Model_Code_Alignment_Matrix_v2.md` | Matrice conformità frugale | `CONDIZIONATO` | T-04, H-06, #005 | README aggiornato |
| `ISSUES_INDEX.md` | Matrice tracciabilità | `VALIDO NEL PERIMETRO` | Nessuno | N/A (riferimento normativo) |
| `CONTRIBUTING.md` | Policy governance | `CONDIZIONATO` | L-01..L-04 | README aggiornato |

---

## 5. REGOLE DI INVOCAZIONE

### 5.1 Regola generale

Nessun documento del repository può essere invocato a sostegno di un'affermazione **oltre il proprio perimetro di validità**. In particolare:

- `PHASE1_CERTIFICATION_REPORT.md` non può essere invocato a sostegno di "certificazione sperimentale", "conformità DO-254 DAL-A" o "conformità IEC 61508 SIL-4" in senso proprio.
- `PHASE2_QUANTIZED_TIMING_REPORT.md` non può essere invocato a sostegno di "correttezza funzionale del RTL" o "fedeltà del modello bit-true".
- `C13_v2_Hardware_Validation_Ledger.md` non può essere invocato a sostegno di "contrazione verificata su hardware reale".
- `Model_Code_Alignment_Matrix.md` e `Model_Code_Alignment_Matrix_v2.md` non possono essere invocati a sostegno di "validità matematica dei teoremi" o "fedeltà bit-true dei simulatori".

### 5.2 Regola di citazione

Ogni citazione di un documento del repository in contesti esterni (paper, grant, presentazioni) deve essere accompagnata da:

1. Il nome file esatto.
2. Lo stato di validità (secondo §4).
3. I gate condizionanti principali.
4. Un rimando a `PERIMETER_OF_VALIDITY.md` per il perimetro completo.

### 5.3 Regola di conflitto

In caso di conflitto tra un documento e `ISSUES_INDEX.md` (REV. 2026.2), prevale l'`ISSUES_INDEX`. In caso di conflitto tra un documento e il presente `PERIMETER_OF_VALIDITY.md`, prevale il documento originale **solo** per il perimetro dichiarato; per lo stato di validità prevale il presente documento.

---

## 6. MANUTENZIONE DEL PRESENTE DOCUMENTO

Il presente documento è soggetto a forward-only: non viene riscritto, ma revisionato tramite `PERIMETER_OF_VALIDITY_REV2.md` quando:

1. Un documento del repository viene aggiunto, rimosso o riqualificato.
2. Un gate condizionante viene chiuso (il perimetro va aggiornato per riflettere lo sblocco).
3. Un perimetro di validità viene ridefinito.

La revisione non sostituisce la versione precedente: la affianca.

---

## 7. SINTESI OPERATIVA

In una riga: **nessun documento del repository è una certificazione sperimentale; ciascuno è una specifica condizionale valida in un perimetro esplicito; i perimetri sono definiti dalle assunzioni A1–A5 e dai gate aperti in `ISSUES_INDEX.md` (REV. 2026.2); le riqualificazioni formali sono in `PHASE1_CERTIFICATION_REPORT_REV2.md` e `PHASE2_QUANTIZED_TIMING_REPORT_REV2.md`; ogni citazione esterna deve dichiarare il perimetro e i gate condizionanti.**

---

**Fine del documento POV-CORE-REV-2026.2.**