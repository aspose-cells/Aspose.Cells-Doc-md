---
title: 用C++设置工作表标签颜色
linktitle: 设置工作表标签颜色
type: docs
weight: 120
url: /zh/cpp/set-worksheet-tab-color/
description: 本文演示使用C++ API或库编程设置Excel工作表标签颜色的示例代码。
keywords: 设置Excel标签颜色C++代码
---

{{% alert color="primary" %}}

Aspose.Cells允许您更改单个工作表标签的颜色，使其与其他工作表区分开。例如，您可以将支出设置为红色，销售设置为绿色，资产设置为蓝色，等等。

{{% /alert %}}

## **使用Microsoft Excel设置工作表标签颜色**
1. 在当前工作表底部的标签工作表上右键单击。
1. 选择**标签颜色**。
1. 从调色板中选择一种颜色。
1. 点击**确定**。

## **使用Aspose.Cells设置工作表选项卡颜色**
以下示例代码显示如何使用Aspose.Cells来设置选项卡颜色。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
