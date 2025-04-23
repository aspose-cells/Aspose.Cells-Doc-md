---
title: 用 C++ 隐藏工作表中的零值显示
linktitle: 隐藏工作表中零值的显示
type: docs
weight: 50
url: /zh/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: 本文将展示如何用示例代码通过 C++ 库或 API 编程隐藏 Excel 工作表中的零值。
keywords: 在 C++ 中隐藏 Excel 工作表的零值
---

{{% alert color="primary" %}} 

有时，您需要在电子表格中隐藏零值。这可能是个人偏好或格式化标准。

{{% /alert %}} 

要在Microsoft Excel中隐藏工作表中的零值（例如Microsoft Excel 2003）：

1. 从**工具**菜单中选择**选项**，然后选择**视图**选项卡。
1. 取消选中**零值**选项。
1. 点击**确定**。

请参阅以下演示使用Aspose.Cells隐藏零的示例代码。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
