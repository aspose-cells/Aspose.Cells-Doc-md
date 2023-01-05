---
title: Copia i dati dell'intervallo con lo stile
type: docs
weight: 610
url: /it/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[Copia solo i dati dell'intervallo](/cells/it/net/copy-range-data-only/) spiegato come copiare i dati da un intervallo di celle a un altro intervallo. In particolare, il processo ha applicato un nuovo set di stili alle celle copiate. Aspose.Cells può anche copiare un intervallo completo di formattazione. Questo articolo spiega come.

{{% /alert %}}

Aspose.Cells fornisce una gamma di classi e metodi per lavorare con gli intervalli, ad esempio,[**CreaRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) e[**Applicastile()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Questo esempio:

1. Crea una cartella di lavoro.
1. Riempie un numero di celle nel primo foglio di lavoro con i dati.
1.  Crea un[**Allineare**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  Crea un[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto con attributi di formattazione specificati.
1. Applica lo stile all'intervallo di dati.
1. Crea un secondo intervallo di celle.
1. Copia i dati con la formattazione dal primo intervallo al secondo intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
