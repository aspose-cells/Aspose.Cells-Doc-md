---
title: Copia i dati dell'intervallo con lo stile
type: docs
weight: 340
url: /it/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[Copia solo i dati dell'intervallo](/cells/it/java/copy-range-data-only/) spiegato come copiare i dati da un intervallo di celle a un altro intervallo. Aspose.Cells può anche copiare un intervallo completo di formattazione. Questo articolo spiega come.

{{% /alert %}} 
## **Copia i dati dell'intervallo con lo stile**
Aspose.Cells fornisce una gamma di classi e metodi per lavorare con gli intervalli, ad esempio,[creaRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applicastile()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), eccetera.

Questo esempio:

1. Crea una cartella di lavoro.
1. Riempie un numero di celle nel primo foglio di lavoro con i dati.
1. Crea un intervallo.
1. Crea un oggetto di stile con gli attributi di formattazione specificati.
1. Applica lo stile all'intervallo di dati.
1. Crea un secondo intervallo di celle.
1. Copia i dati con la formattazione dal primo intervallo al secondo intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

