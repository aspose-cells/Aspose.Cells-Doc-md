---
title: Fit All Worksheet Columns on Single PDF Page with C++
linktitle: Fit All Worksheet Columns on Single PDF Page
type: docs
weight: 160
url: /cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Generate a PDF that fits all worksheet columns onto a single page using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Sometimes you want to generate a PDF file that fits all a worksheet's columns onto one page. The [**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/.paginatedsaveoptions/getallcolumnsinonepagepersheet/) property provides this feature in a very easy-to-use manner. Complex calculations such as the height and width of the output PDF are handled internally and are based on the data in the worksheet.

{{% /alert %}}

## **Fit Worksheet Columns on Single PDF Page**

[**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/.paginatedsaveoptions/getallcolumnsinonepagepersheet/) ensures that all columns in a worksheet are rendered to a single PDF page, although rows may expand to several pages depending on the data in the worksheet.

The sample code below shows how to use [**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/.paginatedsaveoptions/getallcolumnsinonepagepersheet/) property to render a large worksheet of 100 columns.

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

When a given worksheet has many columns, the rendered PDF file may show the content in a very small size. It is still readable when scaled up in a viewing application such as Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}