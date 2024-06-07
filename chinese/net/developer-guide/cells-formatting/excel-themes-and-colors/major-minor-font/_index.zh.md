---
title: 标题和正文主题字体
description: Aspose.Cells是一个用于处理电子表格文件的.NET库。它支持在Excel文档中设置标题和正文主题字体，使用户可以自定义文档的外观和样式。本文将介绍如何使用Aspose.Cells库在Excel文档中使用标题和正文主题字体。
keywords: Aspose.Cells、Excel文档、标题、正文、主题字体、外观、样式
type: docs
weight: 120
url: /zh/net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

当区域设置更改时，默认字体将自动更改。 

如果更改默认字体，行高度和列宽度也会更改，甚至可能混乱页面布局。

导致默认字体更改的原因是什么？

如果设置了Excel主题字体，Excel将根据当前的语言环境自动切换不同的字体。


{{% /alert %}}

## **Excel中的标题和正文主题字体**

在Excel中，选择“主页”选项卡，单击字体下拉框，您将看到“主题字体”，其中包含两种主题字体：Calibri Light（标题）和Calibri（正文），在英文区域设置的顶部。

**![主题字体](Theme-Fonts.png)**

如果选择了主题字体，字体名称在不同区域显示将不同。
如果您不希望字体在不同区域自动更改，请不要选择这两种主题字体。


## **程序更改标题和正文字体**
使用Aspose.Cells for .Net，我们可以使用[**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/)属性检查默认字体是否为主题字体，或设置主题字体。

以下示例代码演示了如何操作主题字体。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **动态地以编程方式获取本地主题字体**
有时，我们的服务器和用户的机器不在相同的区域。我们如何获取用户在文件处理中想要的相同字体？

在加载文件之前，我们必须使用[**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/)属性设置系统区域设置。

以下示例代码展示了如何获取本地主题字体。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
