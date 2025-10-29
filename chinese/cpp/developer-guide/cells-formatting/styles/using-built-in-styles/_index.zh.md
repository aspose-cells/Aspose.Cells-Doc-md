---
title: 使用内置样式的C++
linktitle: 使用内置样式
type: docs
weight: 80
url: /zh/cpp/using-built-in-styles/
description: 用C++代码使用Excel的内置样式与Aspose.Cells for C++ API
keywords: 用C++使用Excel内置样式，C++程序以编程方式在工作簿中应用样式，以编程方式在工作簿中应用样式，在Excel中应用内置样式，设置工作簿中的内置样式，C++代码应用内置样式到工作簿，C++代码应用内置样式到Excel工作簿
---

{{% alert color="primary" %}}

Aspose.Cells提供了大量可重复使用的样式来格式化电子表格文档中的单元格。我们可以在工作簿中使用内置样式，也可以创建自定义样式。

{{% /alert %}}

## **如何使用内置样式**

方法 [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) 和枚举 [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) 使使用内置样式变得更加方便。以下是所有可能的内置样式列表:

- 20% 强调 1
- 20% 强调 2
- 20% 强调 3
- 20% 强调 4
- 20% 强调 5
- 20% 强调 6
- 40% 强调 1
- 40% 强调 2
- 40% 强调 3
- 40% 强调 4
- 40% 强调 5
- 40% 强调 6
- 60% 强调 1
- 60% 强调 2
- 60% 强调 3
- 60% 强调 4
- 百分之六十重音_5
- 百分之六十重音_6
- 重音_1
- 重音_2
- 重音_3
- 重音_4
- 重音_5
- 重音_6
- 错误
- 计算
- 检查单元格
- 逗号
- 逗号_1
- 货币
- 货币_1
- 说明性文本
- 良好
- 表头_1
- 表头_2
- 表头_3
- 第四标题
- HYPERLINK
- 跟随的超链接
- 输入
- 链接的单元格
- 中立的
- 普通的
- 注释
- 输出
- 百分比
- 标题
- 总计
- 警告文本
- 行级
- 列级

## C++使用内置样式的代码

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
