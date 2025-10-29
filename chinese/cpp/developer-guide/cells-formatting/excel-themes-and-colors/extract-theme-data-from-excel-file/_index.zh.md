---
title: 使用 C++ 从 Excel 文件中提取主题数据
linktitle: 从 Excel 文件中提取主题数据
description: Aspose.Cells 是一个用于操作电子表格文件的 C++ 库。它支持从 Excel 文件提取主题数据，允许用户获取文档的样式和格式信息。本文将介绍如何使用 Aspose.Cells 库从 Excel 文件中提取主题数据。
keywords: Aspose.Cells, Excel 文件, 主题数据, 样式, 格式
type: docs
weight: 120
url: /zh/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells 允许用户从 Excel 文件中提取与主题相关的数据。例如，你可以提取应用于工作簿的主题名称以及应用于单元格或单元格边框的主题颜色等。

你可以使用 Microsoft Excel 通过“页面布局”>“主题”命令为工作簿应用主题。

{{% /alert %}}

## 用 C++ 提取 Excel 文件主题数据的示例代码

以下示例代码提取应用于源工作簿的主题名称，然后提取应用于单元格 A1 的主题颜色以及应用于该单元格底部边框的主题颜色。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
