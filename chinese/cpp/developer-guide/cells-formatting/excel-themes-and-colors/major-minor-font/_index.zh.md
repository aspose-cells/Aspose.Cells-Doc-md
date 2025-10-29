---
title: 使用 C++ 设置标题和正文主题字体
linktitle: 标题和正文主题字体
description: Aspose.Cells 是一个用于操作电子表格文件的 C++ 库。它支持在 Excel 文档中设置标题和正文主题字体，帮助用户自定义文档的外观和样式。本文介绍如何使用 Aspose.Cells 库处理 Excel 文档中的标题和正文主题字体。
keywords: Aspose.Cells, Excel 文档, 标题, 正文, 主题字体, 外观, 样式
type: docs
weight: 120
url: /zh/cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

当区域设置改变时，默认字体会自动变化。

如果默认字体更改，行高和列宽也会更改，甚至可能会搅乱页面布局。

是什么导致默认字体更改？

如果设置了 Excel 主题字体，Excel 将根据当前语言环境自动在不同字体之间切换。

{{% /alert %}}

## **在Excel中设置标题和正文主题字体**

在 Excel 中，选择“开始”标签，点击字体下拉框，你将看到“主题字体”，其中包括两个主题字体：Calibri Light（标题）和 Calibri（正文），位于顶部并具有英文区域设置。

**![主题字体](Theme-Fonts.png)**

如果选择了主题字体，字体名称在不同区域会显示不同。
如果你不希望字体在不同区域自动变化，不要选择这两个主题字体。

## **程序matically 更改标题和正文字体**
有了 Aspose.Cells for C++，我们可以检查默认字体是否为主题字体，或通过 [**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/) 属性设置主题字体。

以下示例代码展示了如何操纵主题字体。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **动态以编程方式获取本地主题字体**
有时，我们的服务器和用户的机器不在同一区域。我们如何获取用户希望进行文件处理的相同字体？

在加载文件之前，需要设置系统区域设置，使用 [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/) 属性。

以下示例代码演示如何获取本地区域的主题字体。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
