---
title: Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion with C++
type: docs
weight: 100
url: /cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Convert Excel worksheets into PDF format with one page for each worksheet using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

When working with large Microsoft Excel files (for example, a workbook that has many sheets, each with 50 columns and 300 or more rows of data), you might want the PDF output to show one page per worksheet, regardless of the size of the worksheet. This would mean that each page is likely to have a radically different page size. This can be achieved by using Aspose.Cells for C++.

{{% /alert %}} 

Please see the following sample code that converts an Excel file with multiple worksheets to PDF.

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

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

If the [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) option is set to **true**, all sheet content will be rendered to one PDF page.

{{% /alert %}} {{% alert color="primary" %}} 

If your spreadsheet contains formulas, it is best to call [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) just before rendering the spreadsheet to PDF. This ensures that the formula‑dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
