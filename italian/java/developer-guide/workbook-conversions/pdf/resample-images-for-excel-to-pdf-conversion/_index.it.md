---
title: Risample Immagini per la Conversione da Excel a PDF
type: docs
weight: 250
url: /it/java/resample-images-for-excel-to-pdf-conversion/
description: Questo articolo dimostra come ridurre le dimensioni delle immagini durante la conversione dei file Excel in PDF
keywords: excel to pdf, risampling delle immagini durante la conversione da excel a pdf, compressione delle immagini durante la conversione da excel a pdf, riduzione delle dimensioni delle immagini durante la conversione da excel a pdf, convertire excel in pdf con dimensioni più piccole, conversione da excel a pdf con risampling delle immagini, conversione da excel a pdf con compressione delle immagini, risampling delle immagini durante la conversione da excel a pdf in java
---

{{% alert color="primary" %}}

Mentre lavori con grandi file Microsoft Excel con molte immagini, potresti aver bisogno di comprimere le immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare le prestazioni complessive della conversione. Aspose.Cells supporta il risampling delle immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare le prestazioni.

{{% /alert %}}

## **Risample Immagini per la Conversione da Excel a PDF**

Si prega di consultare il codice di esempio seguente che descrive come eseguire il compito utilizzando l'API Aspose.Cells. L'esempio converte un file Microsoft Excel in un file PDF comprimendo le immagini nel file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

Utilizzando l'opzione [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) si riduce le dimensioni del PDF di output, ma potrebbe influenzare leggermente la qualità dell'immagine.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
