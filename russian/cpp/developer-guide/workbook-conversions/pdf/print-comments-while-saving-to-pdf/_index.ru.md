---
title: Печатать комментарии при сохранении в PDF с помощью C++
linktitle: Печать комментариев при сохранении в формат PDF
type: docs
weight: 10
url: /ru/cpp/print-comments-while-saving-to-pdf/
description: Узнайте, как печатать комментарии при сохранении файлов Excel в PDF с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel позволяет печатать комментарии при печати или сохранении в формат PDF с следующими опциями:

- Нет
- В конце листа
- Как отображено на листе

Aspose.Cells предоставляет перечисление [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/), чтобы поддерживать ту же функцию. Перечисление [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) содержит следующих участников:

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **Печать комментариев при сохранении в формат PDF**

Следующий пример кода показывает, как использовать [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) для печати комментариев при сохранении в PDF.

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
