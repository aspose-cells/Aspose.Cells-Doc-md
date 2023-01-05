---
title: Aggiungere e fare riferimento a intervalli denominati
type: docs
weight: 120
url: /it/net/add-and-reference-named-ranges/
---
{{% alert color="primary" %}} 

 Normalmente, le etichette di colonna e riga vengono utilizzate per fare riferimento in modo univoco alle celle. Ma puoi creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola**Nome**può fare riferimento a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Ad esempio, utilizza nomi di facile comprensione, come Prodotti, per fare riferimento a intervalli di difficile comprensione, come Vendite!C20:C30. Le etichette possono essere utilizzate in formule che fanno riferimento a dati sullo stesso foglio di lavoro; se vuoi rappresentare un intervallo su un altro foglio di lavoro, puoi usare un nome.**Intervalli denominati** è una delle funzionalità più potenti di Microsoft Excel. Gli utenti possono assegnare un nome a un intervallo e utilizzare tale nome nelle formule. Aspose.Cells.GridWeb supporta questa funzione.

{{% /alert %}} 
## **Aggiunta/riferimento a intervalli denominati nelle formule**
Il controllo GridWeb fornisce due classi (GridName e GridNameCollection) per lavorare con intervalli denominati. Il seguente frammento di codice ti aiuterà a capire come creare l'intervallo denominato e accedervi nelle formule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
