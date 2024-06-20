---
title: Copia intervallo dati con stile.
type: docs
weight: 610
url: /it/python-net/copy-range-data-with-style/
description: Questo articolo descrive come copiare i dati del range con lo stile con la libreria Aspose.Cells per Python via .NET.
keywords: Libreria Excel di Python, Python Come Copiare Dati di Intervallo con Stile, Python Come Copiare Dati di Intervallo con Stile con la libreria excel di Python.
---

{{% alert color="primary" %}}

[Copia Solo Dati dell'Intervallo](/cells/it/python-net/copia-solo-dati-dell'intervallo/) spiega come copiare i dati da un intervallo di celle in un altro intervallo. In particolare, il processo ha applicato un nuovo set di stili alle celle copiate. Aspose.Cells per Python via .NET può anche copiare un intervallo completo con la formattazione. Questo articolo spiega come.

{{% /alert %}}

Aspose.Cells per Python via .NET fornisce una serie di classi e metodi per lavorare con gli intervalli, ad esempio, [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) e [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag).

Questo esempio:

1. Crea un workbook.
1. Riempie un certo numero di celle nel primo foglio di lavoro con dati.
1. Crea un [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Crea un oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) con attributi di formattazione specificati.
1. Applica lo stile all'intervallo di dati.
1. Crea un secondo intervallo di celle.
1. Copia i dati con la formattazione dal primo intervallo al secondo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
