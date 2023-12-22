---
title: 标题和正文主题字体
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库。它支持在Excel文档中设置标题和正文主题字体，使用户能够自定义文档的外观和风格。本文将介绍如何使用 Aspose.Cells 库来处理 Excel 文档中的标题和正文主题字体。
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /zh/net/headings-and-body-theme-font/
---
{{% alert color="primary" %}}

当重新设置设置更改时，默认字体将自动更改。

如果更改默认字体，行高和列宽也会更改，甚至可能会弄乱页面布局。

是什么导致默认字体发生变化？

如果设置了Excel主题字体，Excel会根据当前语言环境自动切换不同字体。


{{% /alert %}}

##  **Excel 中的标题和正文主题字体**

在Excel中，选择“开始”选项卡，单击字体下拉框，您将看到“主题字体”，有两种主题字体：顶部的Calibri Light（标题）和Calibri（正文），并带有英文区域设置。

**![主题字体](Theme-Fonts.png)**

如果选择主题字体，不同地区的字体名称会显示不同。
如果您不希望不同地区的字体自动变化，请不要选择这两个主题字体。


##  **以编程方式更改标题和正文字体**
使用 Aspose.Cells for .Net ，我们可以检查默认字体是否为主题字体或设置主题字体[**字体方案类型**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/)财产。

以下示例代码展示了如何操作主题字体。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


##  **通过编程动态获取本地主题字体**
有时，我们的服务器和用户的机器不在同一个区域。如何才能获得与用户想要的文件处理相同的字体呢？

我们必须在加载文件之前设置系统区域设置[**加载选项.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/)财产

以下示例代码展示了如何获取本地主题字体。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}