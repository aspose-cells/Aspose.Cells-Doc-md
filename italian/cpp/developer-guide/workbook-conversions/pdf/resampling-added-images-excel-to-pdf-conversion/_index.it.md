---
title: Risampling di immagini aggiunte  Conversione Excel in PDF con C++
linktitle: Aggiunta di reimmissione delle immagini  Conversione di Excel in PDF
type: docs
weight: 150
url: /it/cpp/resampling-added-images-excel-to-pdf-conversion/
description: Scopri come risamplingare le immagini aggiunte per ridurre la dimensione del PDF utilizzando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Mentre si lavora con grandi file di Microsoft Excel con molte immagini, potrebbe essere necessario comprimere le immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare leggermente le prestazioni complessive della conversione. Aspose.Cells supporta la reimmissione delle immagini aggiunte per ridurre le dimensioni del file PDF di output e migliorare le prestazioni.

{{% /alert %}}

Si prega di consultare il codice di esempio seguente che descrive come eseguire il compito utilizzando l'API Aspose.Cells. L'esempio converte un file Microsoft Excel in un file PDF comprimendo le immagini nel file.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputPath = srcDir + u"input.xlsx";
    Workbook workbook(inputPath);

    // Instantiate the PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set Image Resample properties
    pdfSaveOptions.SetImageResample(300, 70);

    // Save the PDF file
    U16String outputPath = outDir + u"OutputFile_out_pdf.pdf";
    workbook.Save(outputPath, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Utilizzando l'opzione [**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/) si riduce le dimensioni del PDF di output, ma potrebbe influenzare leggermente la qualità dell'immagine.

{{% /alert %}} 

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) proprio prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantisce il ricalcolo dei valori dipendenti dalle formule e la visualizzazione dei valori corretti nel PDF.

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
