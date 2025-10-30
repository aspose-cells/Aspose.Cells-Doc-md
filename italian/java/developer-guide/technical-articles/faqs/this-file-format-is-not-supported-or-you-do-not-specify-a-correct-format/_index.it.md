---
title: Questo formato file non è supportato o non hai specificato un formato corretto
type: docs
weight: 10
url: /it/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **Questo formato file non è supportato o non hai specificato un formato corretto**
Se l'utente ha specificato il formato del file durante la creazione del libro di lavoro da un file modello, comunemente questo errore si verifica perché il formato del file specificato non corrisponde al reale formato del file modello. Se l'utente non ha specificato il formato del file, comunemente ciò accade perché l'estensione del nome del file non rappresenta il reale formato del file e il formato del file non può essere rilevato automaticamente, come nel caso del file csv/tsv che non ha identificatori speciali. Naturalmente, anche i formati di file non supportati da Cells segnaleranno questo errore.
{{< app/cells/assistant language="java" >}}
