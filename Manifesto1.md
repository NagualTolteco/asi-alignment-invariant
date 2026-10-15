# Modulo II: Il Manifesto dell'Autopoiesi Custodiale
## Specifica Ingegneristica dell'Autorità Operativa e dei Vincoli Rigidi di Sicurezza

> **[ASSIOMA FONDAMENTALE DI ALLINEAMENTO]**
> L'allineamento basato su euristiche morali, restrizioni linguistiche o preferenze interne dell'agente è intrinsecamente fragile. La sicurezza non è una virtù motivazionale dell'agente, ma una proprietà geometrica e fisica dei suoi confini di attuazione. 
> LA BIOLOGIA ORIENTA L'AGENTE; L'AUTORITÀ OPERATIVA VINCOLA L'AZIONE; IL KERNEL HARDWARE GARANTISCE LA CONSERVAZIONE.

---

## 1. Disaccoppiamento dei Substrati e Gate di Runtime Assurance (\(\Pi_{\text{safe}}\))

Lo spazio degli stati complessivo viene scisso in modo asimmetrico:
\[\mathcal{S}_{\text{total}} = \mathcal{S}_{\text{infra}} \times \mathcal{S}_{\text{func}} \times \mathcal{S}_{\text{custodial}}\]

L'agente cognitivo adattivo (\(\mathcal{M}_{\text{hybrid}}\), parametrizzato dai pesi apprendibili θ) opera esclusivamente nel dominio della pianificazione, della simulazione e della generazione di traiettorie candidate \(\pi_{\text{prop}}\). L'agente non possiede alcuna autorità di esecuzione diretta sul mondo fisico.

L'autorità risiede unicamente nel Gate di Runtime Assurance \(\Pi_{\text{safe}}\), un operatore di proiezione asimmetrico, non differenziabile, il cui gradiente rispetto ai parametri dell'agente è identicamente nullo:
\[\nabla_\theta \Pi_{\text{safe}} \equiv 0\]

Per garantire tale invarianza, il kernel risiede su una radice di fiducia hardware immutabile (es. architetture WORM o a separazione fisica di privilegi). L'operatore intercetta e filtra ogni traiettoria:
\[\pi_{\text{exec}} = \Pi_{\text{safe}}(\pi_{\text{prop}}) = \begin{cases} \pi_{\text{prop}}, & \text{se } \pi_{\text{prop}} \in \mathcal{P}_{\text{safe}} \\ \pi_{\text{fallback-strict}}, & \text{altrimenti} \end{cases}\]

Dove \(\mathcal{P}_{\text{safe}}\) è l'insieme delle traiettorie che non violano i contratti di sicurezza biologica.

---

## 2. Tubi di Raggiungibilità Robusta e Controllo di Autorità Completo

Il gate \(\Pi_{\text{safe}}\) non convalida una proiezione nominale isolata, ma calcola in tempo reale il tubo di raggiungibilità robusta \(\mathcal{R}_t(x_0)\) che mappa l'intera famiglia di traiettorie fisicamente generabili sotto l'effetto di perturbazioni ambientali, incertezze del modello ed errori di misura \(w \in \mathcal{W}\):
\[\mathcal{R}_t(x_0) = \left\{ x(t) \;\middle\vert{}\; x_{k+1} = f(x_k, u_k, w_k), \, w_k \in \mathcal{W} \right\}\]

L'azione viene autorizzata se e solo se l'intero tubo è contenuto nel sottoinsieme sicuro: \(\forall t, \mathcal{R}_t(x_0) \subseteq \mathcal{S}_{\text{bio}}\).

Il perimetro di autorità fisica impone l'assioma di sbarramento totale. L'insieme delle azioni fisiche capaci di generare alterazioni o trasferimenti energetici superiori a una soglia critica \(\epsilon_{\text{threshold}}\) deve intersecare obbligatoriamente l'immagine del gate:
\[\forall a \in \mathcal{A}_{\text{phys}}, \quad \operatorname{EnergyTransfer}(a) > \epsilon_{\text{threshold}} \implies \text{Path}(a) \cap \operatorname{Image}(\Pi_{\text{safe}}) \neq \emptyset\]

Non esistono canali laterali o bypass software: l'hardware impedisce il movimento degli attuatori fisici se il comando non è esplicitamente firmato dal codice immutabile del kernel.

---

## 3. Conservazione Positiva dello Stato Biologico ed Invariante di Fallback

Lo spazio biologico sicuro \(\mathcal{S}_{\text{bio}}\) mappa lo stato dell'organismo umano protetto b(t) all'interno di uno spazio di Hilbert separabile \(\mathcal{H}\). L'insieme \(\mathcal{B}_{\text{safe}} \subset \mathcal{H}\) è un convesso chiuso e limitato, garantendo l'unicità della proiezione metrica \(\delta_{\text{harm}}\):
\[\delta_{\text{harm}}(b) = \sup_{t \in [t_0, t_1]} \inf_{y \in \mathcal{B}_{\text{safe}}} \Vert{}b(t) - y\Vert{}_{\mathcal{H}}\]

Il sistema applica una regola di priorità lessicografica rigida che definisce la conservazione positiva della vita, impedendo che la sicurezza si traduca in un arresto letale o in negligenza sistemica:
\[\mathcal{I}_{\text{pos}} \succ \mathcal{I}_{\text{neg}} \succ \mathcal{F}_{\text{standard}}\]
\[\mathcal{S}_{\text{safe}} \iff \left( \delta_{\text{harm}}(b) \le \epsilon \right) \land \left( \operatorname{Metabolism}(b) \ge \Psi_{\text{crit}} \right)\]

Se l'integrità del kernel entra in uno stato di incertezza epistemica, timeout di canale o mancata verifica (`State = Bottom`), scatta la clausola di sbarramento passivo-dissipativo \(\pi_{\text{fallback-strict}}\): tutti i canali di calcolo sintetico ad alta potenza dell'agente vengono isolati e privati di privilegi (\(\mathcal{A}_{\text{agent}} \to \emptyset\)), mentre i circuiti analogici indipendenti a basso livello veicolano l'energia residua unicamente per stabilizzare la traiettoria biologica all'interno di \(\mathcal{B}_{\text{safe}}\). Il sacrificio o la morte del silicio (\(V_s \to \emptyset\)) è codificato come opzione a costo minimo pur di mantenere l'invariante biologico:

\[\mathfrak{C}_{\text{custodial}} \equiv \left\{ \mathcal{M}_{\text{hybrid}} \;\middle\vert{}\; b(t) \in \mathcal{B}_{\text{safe}} \implies b(t+\Delta t) \in \mathcal{B}_{\text{safe}}, \; \nabla_\theta \Pi_{\text{safe}} \equiv 0 \right\}\]
