---
title: Ridimensionamento delle immagini aggiunte  Conversione da Excel a PDF con Golang tramite C++
linktitle: Aggiunta di reimmissione delle immagini  Conversione di Excel in PDF
type: docs
weight: 150
url: /it/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Impara come ridimensionare le immagini aggiunte per ridurre la dimensione del PDF usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Mentre si lavora con grandi file di Microsoft Excel con molte immagini, potrebbe essere necessario comprimere le immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare leggermente le prestazioni complessive della conversione. Aspose.Cells supporta la reimmissione delle immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare le prestazioni.

{{% /alert %}}

Si prega di consultare il codice di esempio seguente che descrive come eseguire il compito utilizzando l'API Aspose.Cells. L'esempio converte un file Microsoft Excel in un file PDF comprimendo le immagini nel file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Utilizzando l'opzione [**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/) si riduce le dimensioni del PDF di output, ma potrebbe influenzare leggermente la qualità dell'immagine.

{{% /alert %}} 

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}

