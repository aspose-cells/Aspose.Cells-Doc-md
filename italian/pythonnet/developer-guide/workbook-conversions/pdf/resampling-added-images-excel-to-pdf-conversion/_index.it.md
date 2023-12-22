---
title: "Ricampiona le immagini aggiunte: conversione da Excel a PDF"
type: docs
weight: 150
url: /it/python-net/resample-added-images-excel-to-pdf-conversion/
description: Scopri come ricampionare le immagini aggiunte durante la conversione di Excel in PDF con Aspose.Cells for Python via .NET API.
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

Mentre lavori con file Excel Microsoft di grandi dimensioni con molte immagini, potrebbe essere necessario comprimere le immagini che sono state aggiunte per ridurre le dimensioni del file di output PDF e migliorare le prestazioni complessive di conversione. Aspose.Cells for Python via .NET supporta il ricampionamento delle immagini aggiunte per ridurre la dimensione del file di output PDF e migliorare leggermente le prestazioni.

{{% /alert %}}

Consulta il seguente codice di esempio che descrive come eseguire l'attività utilizzando Aspose.Cells for Python via .NET API. L'esempio converte un file Excel Microsoft in un file PDF durante la compressione delle immagini nel file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

 Utilizzando il[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)L'opzione riduce al minimo la dimensione dell'output PDF ma potrebbe influire leggermente sulla qualità dell'immagine.

{{% /alert %}} {{% alert color="primary" %}}

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) appena prima di convertire il foglio di calcolo nel formato PDF. In questo modo si garantirà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}
