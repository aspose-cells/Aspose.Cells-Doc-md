---
title: Usa intervalli denominati
type: docs
weight: 110
url: /it/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop, intervalli denominati, nomi
description: Questo articolo introduce gli intervalli denominati in GridDesktop.
---

{{% alert color="primary" %}} 

Normalmente si utilizzano le etichette delle colonne e delle righe in un foglio di lavoro per fare riferimento alle celle all'interno di quelle colonne e righe. Ma è possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola **Nome** può fare riferimento a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Ad esempio, utilizzare nomi di facile comprensione, come Prodotti, per fare riferimento a intervalli difficili da capire, come Vendite!C20:C30 per rappresentare una cella, un intervallo di celle, una formula o un valore costante. Le etichette possono essere utilizzate in formule che fanno riferimento ai dati sullo stesso foglio di lavoro; se si desidera rappresentare un intervallo su un altro foglio di lavoro, è possibile utilizzare un nome. Gli **intervalli denominati** sono tra le funzionalità più potenti di Microsoft. Gli utenti possono assegnare un nome a un intervallo denominato in modo che questo intervallo di celle possa essere referenziato con il suo nome nelle formule. **Aspose.Cells.GridDesktop** supporta questa funzionalità.

{{% /alert %}} 
## **Aggiunta/Riferimento degli Intervalli Nominati nelle Formule**
Il controllo GridDesktop supporta l'importazione/esportazione di intervalli denominati nei file Excel, fornisce due classi (**Name** e **NameCollection**) per lavorare con gli intervalli denominati.

Il seguente frammento di codice ti aiuterà a capire come utilizzarli.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
