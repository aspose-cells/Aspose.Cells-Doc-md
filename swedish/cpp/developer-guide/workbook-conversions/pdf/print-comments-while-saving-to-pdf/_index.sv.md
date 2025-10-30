---
title: Skriv ut kommentarer när du sparar till PDF med C++
linktitle: Skriv ut kommentarer vid sparning till PDF
type: docs
weight: 10
url: /sv/cpp/print-comments-while-saving-to-pdf/
description: Lär dig hur du skriver ut kommentarer när du sparar Excel filer till PDF med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel tillåter dig att skriva ut kommentarer när du skriver ut eller sparar till PDF-format med följande alternativ:

- Ingen
- I slutet av bladet
- Enligt visad på kalkylbladet

Aspose.Cells tillhandahåller enum [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) för att stödja samma funktion. Enum [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) har följande medlemmar:

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **Skriv ut kommentarer vid sparande till PDF**

Följande exempel kod visar hur man använder [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) för att skriva ut kommentarer när man sparar till PDF.

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
