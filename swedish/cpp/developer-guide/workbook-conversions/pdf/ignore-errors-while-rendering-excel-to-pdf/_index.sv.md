---
title: Ignorera fel vid rendering av Excel till PDF med C++
linktitle: Ignorera fel vid rendering av Excel till PDF
type: docs
weight: 80
url: /sv/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Lär dig hur du ignorerar fel under konvertering av Excel till PDF med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland kan fel eller undantag uppstå när du konverterar din Excel-fil till PDF, och konverteringsprocessen avbryts. Du kan ignorera alla sådana fel under konverteringen genom att använda egenskapen [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). På så sätt kommer konverteringsprocessen att slutföras smidigt utan att kasta något fel eller undantag, men en förlust av data kan inträffa. Använd därför denna egenskap endast om dataloss är ofarligt för dig.

## **Ignorera fel vid rendering av Excel till PDF**

Följande kod laddar [exempel Excel-fil](55541778.xlsx), men filen är felaktig och ger ett fel under [konverteringen till PDF](55541779.pdf) i 17.11 men eftersom vi använder egenskapen [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) så kastas inget fel. Men en *rundad röd pil-liknande form* som visas i skärmbilden förloras.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
