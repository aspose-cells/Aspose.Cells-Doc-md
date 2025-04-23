---
title: omräkning av tillagda bilder  Excel till PDF konvertering med C++
linktitle: Komprimering av tillagda bilder  Konvertering från Excel till PDF
type: docs
weight: 150
url: /sv/cpp/resampling-added-images-excel-to-pdf-conversion/
description: Lär dig hur man omräknar tillagda bilder för att minska PDF storleken med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med massor av bilder kan du behöva komprimera de tillagda bilderna för att minska storleken på utdata-PDF-filen och förbättra den totala konverteringsprestandan. Aspose.Cells stöder att komprimera tillagda bilder för att minska utdata-PDF-filens storlek och förbättra prestandan något.

{{% /alert %}}

Se följande exempelkod som beskriver hur man utför uppgiften med hjälp av Aspose.Cells API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

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

Att använda [**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/)-alternativet minimerar storleken på utmatnings-PDF-filen men det kan påverka bildkvaliteten lite.

{{% /alert %}} 

{{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}

