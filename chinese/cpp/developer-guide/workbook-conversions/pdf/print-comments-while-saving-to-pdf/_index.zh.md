---
title: 在保存为PDF时打印批注与C++
linktitle: 保存为PDF时打印注释
type: docs
weight: 10
url: /zh/cpp/print-comments-while-saving-to-pdf/
description: 了解如何在使用Aspose.Cells for C++将Excel文件保存为PDF时打印批注。
---

{{% alert color="primary" %}}

Microsoft Excel允许您通过以下选项在打印或保存为PDF格式时打印批注：

- 无
- 工作表末尾
- 如在工作表上显示的那样

Aspose.Cells提供了[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)枚举以支持相同的功能。[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)枚举具有以下成员：

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **保存为PDF时打印注释**

以下示例代码说明了如何使用[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)在保存为PDF时打印批注。

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
