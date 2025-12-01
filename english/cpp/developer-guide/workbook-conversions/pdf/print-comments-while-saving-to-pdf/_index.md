---
title: Print Comments while saving to PDF with C++
linktitle: Print Comments while saving to PDF
type: docs
weight: 10
url: /cpp/print-comments-while-saving-to-pdf/
description: Learn how to print comments while saving Excel files to PDF using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel allows you to print comments while printing or saving to PDF format with the following options:

- None
- At end of sheet
- As displayed on sheet

Aspose.Cells provides the [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) enum to support the same feature. The [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) enum has the following members:

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **Print Comments while saving to PDF**

The following sample code illustrates how to use [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) to print comments while saving to PDF.

```cpp
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
    U16String inputFilePath = srcDir + u"SampleWorkbookWithComments.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"PrintCommentWhileSavingToPdf_out.pdf";

    // Create a workbook from source Excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    /*
     * For print no comments use "PrintCommentsType::PrintNoComments"
     * and for print the comments as displayed on sheet use "PrintCommentsType::PrintInPlace"
     * For Print the comments at the end of sheet we use "PrintCommentsType::PrintSheetEnd"
    */
    worksheet.GetPageSetup().SetPrintComments(PrintCommentsType::PrintSheetEnd);

    // Save workbook in pdf format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with comments printed at the end of the sheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
