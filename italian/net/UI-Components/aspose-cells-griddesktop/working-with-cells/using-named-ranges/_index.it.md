---
title: Utilizzo di intervalli denominati
type: docs
weight: 110
url: /it/net/using-named-ranges/
---
{{% alert color="primary" %}} 

 Normalmente, si utilizzano le etichette di colonne e righe su un foglio di lavoro per fare riferimento alle celle all'interno di tali colonne e righe. Ma puoi creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola**Nome**può fare riferimento a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Ad esempio, Usa nomi di facile comprensione, come Prodotti, per fare riferimento a intervalli difficili da capire, come Vendite!C20:C30 per rappresentare una cella, un intervallo di celle, una formula o un valore costante. Le etichette possono essere utilizzate in formule che fanno riferimento a dati sullo stesso foglio di lavoro; se vuoi rappresentare un intervallo su un altro foglio di lavoro, puoi usare un nome.**Intervalli denominati** sono tra le funzionalità più potenti di Microsoft. Gli utenti possono assegnare un nome a un intervallo denominato in modo che questo intervallo di celle possa essere indicato con il suo nome nelle formule.**Aspose.Cells.GridDesktop** supporta questa funzione.

{{% /alert %}} 
## **Aggiunta/riferimento a intervalli denominati nelle formule**
Il controllo GridDesktop supporta l'importazione/esportazione di intervalli denominati nei file Excel, fornisce due classi (**Nome** e**NomeRaccolta**) per lavorare con intervalli denominati.

Il seguente frammento di codice ti aiuterà a usarli.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
