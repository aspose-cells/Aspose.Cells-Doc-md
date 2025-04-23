---
title: 标题和正文主题字体
linktitle: 标题和正文主题字体
description: Aspose.Cells 是一个用于操作电子表格文件的 Node.js 库。它支持在 Excel 文档中设置标题和正文的主题字体，使用户能够自定义文档的外观和样式。本文将介绍如何使用 Aspose.Cells 库在 Excel 文档中处理标题和正文的主题字体。
keywords: Aspose.Cells，Excel 文档，标题，正文，主题字体，外观，样式，Node.js via C++
type: docs
weight: 120
url: /zh/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

当区域设置改变时，默认字体会自动变化。

如果默认字体更改，行高和列宽也会更改，甚至可能会搅乱页面布局。

是什么导致默认字体更改？

如果设置了 Excel 主题字体，Excel 将根据当前语言环境自动在不同字体之间切换。

{{% /alert %}}

## **在Excel中设置标题和正文主题字体**

在 Excel 中，选择“开始”选项卡，点击字体下拉框，你会看到“主题字体”，顶部显示两个主题字体：Calibri Light（标题），和 Calibri（正文），设置为英语区域。

**![主题字体](Theme-Fonts.png)**

如果选择主题字体，字体名称在不同区域可能会显示不同。如果你不希望字体在不同区域自动变化，请不要选择这两个主题字体。

## **程序matically 更改标题和正文字体**
利用 Aspose.Cells for Node.js via C++，我们可以检查默认字体是否为主题字体，或者使用 [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-) 方法设置主题字体。

以下示例代码展示了如何操作主题字体。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **动态以编程方式获取本地主题字体**
有时，我们的服务器和用户的机器不在同一区域。我们如何获取用户希望进行文件处理的相同字体？

在使用 [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-) 方法加载文件之前，我们必须设置系统区域设置。

以下示例代码展示了如何获取本地主题字体。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

