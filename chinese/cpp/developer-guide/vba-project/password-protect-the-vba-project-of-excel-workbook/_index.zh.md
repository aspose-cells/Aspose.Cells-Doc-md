---
title: 用C++为Excel工作簿的VBA项目加密保护
linktitle: 密码保护 Excel 工作簿的 VBA 项目
type: docs
weight: 10
url: /zh/cpp/password-protect-the-vba-project-of-excel-workbook/
description: 了解如何使用Aspose.Cells结合C++为Excel工作簿的VBA项目添加密码保护。
---

## **用C++为Excel工作簿的VBA项目加密保护**

你可以使用[**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/)方法，为工作簿的VBA（Visual Basic for Applications）项目设置密码保护。

## **示例代码**

以下示例代码加载一个[示例Excel文件](43352067.xlsm)，访问其VBA项目，并设置密码保护，最后保存为[输出Excel文件](43352068.xlsm)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"samplePasswordProtectVBAProject.xlsm";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outputPasswordProtectVBAProject.xlsm";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Lock the VBA project for viewing with password
    vbaProject.Protect(true, u"11");

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "VBA project password protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
