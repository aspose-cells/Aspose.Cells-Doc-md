---
title: Copia intervallo dati con stile.
type: docs
weight: 610
url: /it/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Copia Dati Intervallo Solo](/cells/it/net/copiare-dati-intervallo-solo/) spiega come copiare i dati da un intervallo di celle a un altro intervallo. In particolare, si applica un nuovo set di stili alle celle copiate. Aspose.Cells può anche copiare un intervallo completo con la formattazione. Questo articolo spiega come.

{{% /alert %}}

Aspose.Cells fornisce una serie di classi e metodi per lavorare con gli intervalli, ad esempio, [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) e [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Questo esempio:

1. Crea un workbook.
1. Riempie un certo numero di celle nel primo foglio di lavoro con dati.
1. Crea un [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Crea un oggetto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) con attributi di formattazione specificati.
1. Applica lo stile all'intervallo di dati.
1. Crea un secondo intervallo di celle.
1. Copia i dati con la formattazione dal primo intervallo al secondo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
