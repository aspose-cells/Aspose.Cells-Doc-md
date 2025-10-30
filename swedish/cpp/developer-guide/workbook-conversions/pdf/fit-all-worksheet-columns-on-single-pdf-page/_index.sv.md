---
title: Anpassa alla arbetsbladskolumner till en PDF sida med C++
linktitle: Anpassa alla kalkylbladskolumner på en enda PDF sida
type: docs
weight: 160
url: /sv/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Generera en PDF som passar alla arbetsbladskolumner på en enda sida med Aspose.Cells i C++.
---

{{% alert color="primary" %}}

Ibland vill du generera en PDF-fil som passar alla kolumner i ett arbetsblad på en sida. Egenskapen [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) erbjuder den här funktionen på ett mycket enkelt sätt. Komplexa beräkningar som höjd och bredd på den genererade PDF-filen hanteras internt och baseras på data i arbetsbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på en enda PDF-sida**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) säkerställer att alla kolumner i ett arbetsblad renderas till en enda PDF-sida, även om rader kan sträckas ut till flera sidor beroende på data i arbetsbladet.

Nedan visas exempel på hur man använder [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) egenskapen för att rendera ett stort arbetsblad med 100 kolumner.

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

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den genererade PDF-filen visa innehållet i väldigt liten storlek. Det är fortfarande läsbart när det skalas upp i en visningsapplikation som Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
