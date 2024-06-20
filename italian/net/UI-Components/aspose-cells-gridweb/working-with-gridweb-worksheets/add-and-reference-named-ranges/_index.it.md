---
title: Aggiungi e riferimento agli intervalli denominati
type: docs
weight: 120
url: /it/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: Questo articolo introduce come lavorare con gli intervalli denominati in GridWeb. 
---

{{% alert color="primary" %}} 

Normalmente, le etichette di colonna e riga vengono utilizzate per fare riferimento in modo univoco alle celle. Ma è possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola **Nome** può fare riferimento a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Ad esempio, utilizzare nomi facili da capire, come Prodotti, per fare riferimento a intervalli difficili da capire, come Vendite!C20:C30. Le etichette possono essere utilizzate nelle formule che fanno riferimento ai dati nella stessa cartella di lavoro; se si desidera rappresentare un intervallo in un'altra cartella di lavoro, è possibile utilizzare un nome. **Gli intervalli nominati** sono una delle caratteristiche più potenti di Microsoft Excel. Gli utenti possono assegnare un nome a un intervallo e utilizzare tale nome nelle formule. Aspose.Cells.GridWeb supporta questa funzionalità.

{{% /alert %}} 
## **Aggiunta/Riferimento degli Intervalli Nominati nelle Formule**
Il controllo GridWeb fornisce due classi (GridName e GridNameCollection) per lavorare con gli intervalli nominati. Il seguente frammento di codice ti aiuterà a capire come creare l'Intervallo Nominato e accedervi nelle formule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
