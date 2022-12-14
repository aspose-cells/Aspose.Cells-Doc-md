---
title: Ricampiona le immagini per la conversione da Excel a PDF
type: docs
weight: 250
url: /it/java/resample-images-for-excel-to-pdf-conversion/
description: Questo articolo illustra la riduzione delle dimensioni delle immagini durante la conversione di file Excel in PDF
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

Mentre si lavora con grandi file Excel Microsoft con molte immagini, potrebbe essere necessario comprimere le immagini che sono state aggiunte per ridurre le dimensioni del file PDF di output e migliorare le prestazioni complessive della conversione. Aspose.Cells supporta il ricampionamento delle immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare le prestazioni.

{{% /alert %}}

## **Ricampiona le immagini per la conversione da Excel a PDF**

Vedere il seguente codice di esempio che descrive come eseguire l'attività utilizzando Aspose.Cells API. L'esempio converte un file Excel Microsoft in un file PDF durante la compressione delle immagini nel file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

 Usando il[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) riduce al minimo le dimensioni del PDF di output, ma potrebbe influire leggermente sulla qualità dell'immagine.

{{% /alert %}} {{% alert color="primary" %}}

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()appena prima di eseguire il rendering del foglio di calcolo in formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}
