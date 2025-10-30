---
title: Immagini Aggiunte Campionate  Conversione da Excel a PDF
type: docs
weight: 150
url: /it/python-net/resample-added-images-excel-to-pdf-conversion/
description: Scopri come campionare le immagini aggiunte durante la conversione da excel a pdf con Aspose.Cells for Python via .NET API.
keywords: Python Campiona Immagini Aggiunte durante la Conversione da Excel a PDF
---

{{% alert color="primary" %}}

Mentre lavori con grandi file di Microsoft Excel con molte immagini, potresti aver bisogno di comprimere le immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare le prestazioni complessive della conversione. Aspose.Cells for Python via .NET supporta il campionamento delle immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare leggermente le prestazioni.

{{% /alert %}}

Consulta il codice di esempio seguente che descrive come eseguire il compito utilizzando Aspose.Cells for Python via .NET API. L'esempio converte un file di Microsoft Excel in un file PDF mentre comprime le immagini nel file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

Utilizzando l'opzione [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) si riduce le dimensioni del PDF di output ma potrebbe influire leggermente sulla qualità dell'immagine.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
