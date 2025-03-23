---
title: Save Each Worksheet to a Different PDF File with C++
linktitle: Save Each Worksheet to a Different PDF File
type: docs
weight: 130
url: /cpp/save-each-worksheet-to-a-different-pdf-file/
description: Learn how to save each worksheet in an Excel file to a separate PDF file using Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells supports converting XLS files (that contain images, charts, etc.) to PDF documents. Aspose.Cells for C++ can work independently to convert a spreadsheet to PDF and you do not need to use Aspose.PDF for C++ for the conversion. The conversion does not require the software to create or use any temporary files as the whole process can be done in memory.

{{% /alert %}} 

## **Save Each Worksheet to a Different PDF File**
If you need to save each worksheet in your template Excel file to generate different PDF files, you can achieve this easily. You may try to set one sheet index to [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) option at a time to render to PDF.

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

If your spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula-dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}