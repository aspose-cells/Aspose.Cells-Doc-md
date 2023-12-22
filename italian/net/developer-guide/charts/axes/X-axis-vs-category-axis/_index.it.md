---
title: Asse X vs. Asse di categoria
description: Scopri come distinguere tra l'asse X e l'asse delle categorie in Aspose.Cells for .NET. La nostra guida ti aiuterà a comprendere le differenze nel loro utilizzo e proprietà e come configurarli in base alle tue esigenze.
keywords: Aspose.Cells for .NET, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /it/net/X-axis-vs-category-axis/
---
##  **Possibili scenari di utilizzo**
Esistono diversi tipi di assi X. Mentre l'asse Y è un asse di tipo Valore, l'asse X può essere un asse di tipo Categoria o un asse di tipo Valore. Utilizzando un asse valore, i dati vengono trattati come dati numerici che variano continuamente e il contrassegno viene posizionato in un punto lungo l'asse che varia in base al relativo valore numerico. Utilizzando un asse Categoria, i dati vengono trattati come una sequenza di etichette di testo non numeriche e il contrassegno viene posizionato in un punto lungo l'asse in base alla sua posizione nella sequenza. L'esempio seguente illustra la differenza tra gli assi dei valori e delle categorie.
 I nostri dati di esempio sono mostrati nel file[file di tabella di esempio](sample.png) sotto. La prima colonna contiene i dati dell'asse X, che possono essere trattati come Categorie o come Valori. Tieni presente che i numeri non sono equidistanti e non appaiono nemmeno in ordine numerico.

![cose da fare:immagine_alt_testo](sample.png)
##  **Gestisci gli assi X e Categoria come Microsoft Excel**
Visualizzeremo questi dati su due tipi di grafico, il primo grafico è il grafico XY (a dispersione) X come asse dei valori, il secondo grafico è il grafico a linee X come asse delle categorie.

![cose da fare:immagine_alt_testo](compare.png)
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
