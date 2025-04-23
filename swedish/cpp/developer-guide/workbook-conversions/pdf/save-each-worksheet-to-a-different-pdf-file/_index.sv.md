---
title: Spara varje arbetsblad till en separat PDF fil med C++
linktitle: Spara varje kalkylblad i en separat PDF fil
type: docs
weight: 130
url: /sv/cpp/save-each-worksheet-to-a-different-pdf-file/
description: Lär dig hur man sparar varje arbetsblad i en Excel fil till en separat PDF fil med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells stöder konvertering av XLS-filer (som innehåller bilder, diagram, etc.) till PDF-dokument. Aspose.Cells for C++ kan arbeta självständigt för att konvertera ett kalkylblad till PDF utan att behöva använda Aspose.PDF för C++. Konverteringen kräver inte att programvaran skapar eller använder tillfälliga filer eftersom hela processen kan göras i minnet.

{{% /alert %}} 

## **Spara varje arbetsblad i en separat PDF-fil**
Om du behöver spara varje arbetsblad i din mall-Excel-fil för att generera olika PDF-filer kan du enkelt göra detta. Du kan försöka att ställa in ett arbetsbladsvänteläge till [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) åt gången för att rendera till PDF.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) precis innan du renderar kalkylbladet till PDF-format. Detta säkerställer att formelberoende värden beräknas om och att de korrekta värdena visas i PDF-filen.

{{% /alert %}}
