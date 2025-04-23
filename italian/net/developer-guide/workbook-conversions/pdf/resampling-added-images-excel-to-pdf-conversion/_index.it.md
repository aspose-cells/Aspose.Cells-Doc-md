---
title: Aggiunta di reimmissione delle immagini  Conversione di Excel in PDF
type: docs
weight: 150
url: /it/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Mentre si lavora con grandi file di Microsoft Excel con molte immagini, potrebbe essere necessario comprimere le immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare leggermente le prestazioni complessive della conversione. Aspose.Cells supporta la reimmissione delle immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare le prestazioni.

{{% /alert %}}

Si prega di consultare il codice di esempio seguente che descrive come eseguire il compito utilizzando l'API Aspose.Cells. L'esempio converte un file Microsoft Excel in un file PDF comprimendo le immagini nel file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

Utilizzando l'opzione [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) si riduce le dimensioni del PDF di output ma potrebbe influire leggermente sulla qualità dell'immagine.

{{% /alert %}} {{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
