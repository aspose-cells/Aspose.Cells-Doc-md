---  
title: Save Specified Worksheets to PDF with C++  
linktitle: Save Specified Worksheets to PDF  
type: docs  
weight: 140  
url: /cpp/save-specified-worksheets-to-pdf/  
description: Export specific worksheets to PDF using Aspose.Cells with C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

By default, Aspose.Cells saves all **visible** worksheets in a workbook to a PDF file. With the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) option, you can save specified worksheets to a PDF file. For example, you can save the active worksheet to PDF, save all worksheets (both visible and hidden) to PDF, or save custom multiple worksheets to PDF.

## **Save Active Worksheet to PDF**

If you want to export only the active sheet to PDF, you can achieve this by passing [**SheetSet.GetActive()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getactive/) to the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) option.

The sheet `Sheet2` is the active sheet of the source file [sheetset-example.xlsx](sheetset-example.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set active sheet to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetActive());

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Save All Worksheets to PDF**

[**SheetSet.GetVisible()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getvisible/) indicates visible sheets in a workbook, and [**SheetSet.GetAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) indicates all sheets, including both visible sheets and hidden/invisible sheets in a workbook. If you want to export all sheets to PDF, you can simply pass [**SheetSet.GetAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) to the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) option.

The source file [sheetset-example.xlsx](sheetset-example.xlsx) contains all four sheets, with hidden sheet `Sheet3`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set all sheets to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetAll());

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Save Specified Worksheets to PDF**

If you want to export desired/custom multiple sheets to PDF, you can achieve this by passing multiple sheet indices to the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) option.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    U16String inputFilePath(u"sheetset-example.xlsx");
    Workbook workbook(inputFilePath);

    // Set custom multiple sheets (Sheet1, Sheet3) to output
    Vector<int32_t> sheetIndexes = {0, 2};
    SheetSet sheetSet(sheetIndexes);
    
    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the PDF file with PdfSaveOptions
    U16String outputFilePath(u"output.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Excel file saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Reorder Worksheets to PDF**

If you want to reorder sheets (e.g., in reverse order) to PDF without modifying the source file, you can achieve this by passing reordered sheet indices to the [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) option.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Reorder sheets (Sheet1, Sheet2, Sheet3, Sheet4) to (Sheet4, Sheet3, Sheet2, Sheet1)
    Vector<int32_t> sheetIndexes = { 3, 2, 1, 0 };
    SheetSet sheetSet(sheetIndexes);

    // Create PdfSaveOptions and assign the sheet set
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
