---
title: 标题和正文主题字体
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库。它支持在 Excel 文档中设置标题和正文主题字体，使用户能够自定义文档的外观和样式。本文将介绍如何使用 Aspose.Cells 库在 Excel 文档中处理标题和正文主题字体。
keywords: Aspose.Cells, Excel 文档, 标题, 正文, 主题字体, 外观, 样式
type: docs
weight: 120
url: /zh/net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

当区域设置更改时，默认字体将自动更改。 

如果默认字体更改，行高和列宽也会更改，甚至可能会搅乱页面布局。

是什么导致默认字体更改？

如果设置了 Excel 主题字体，Excel 将根据当前语言环境自动在不同字体之间切换。


{{% /alert %}}

## **在Excel中设置标题和正文主题字体**

在Excel中，选择“主页”选项卡，点击字体下拉框，您会看到带有两种主题字体：Calibri Light (标题) 和 Calibri (正文) 的“主题字体”，在英文区域设置中显示在顶部。

**![主题字体](Theme-Fonts.png)**

如果选择了主题字体，不同区域的字体名称会显示不同。
如果不希望字体在不同区域自动更改，请不要选择这两种主题字体。


## **程序化更改标题和正文字体**
利用Aspose.Cells for .Net，我们可以检查默认字体是否为主题字体，或者使用[**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/)属性设置主题字体。

以下示例代码展示了如何操纵主题字体。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **动态程序化获取本地主题字体**
有时，我们的服务器和用户的机器不在同一区域。我们如何获取用户希望进行文件处理的相同字体？

在加载文件前，我们需要使用[**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/)属性设置系统区域设置。

以下示例代码展示了如何获取本地主题字体。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
