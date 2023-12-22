---
title: 获取页眉或页脚
type: docs
weight: 30
url: /zh/net/get-headers-or-footers/
description: 本文介绍如何使用 C# API 或 .NET 库以编程方式从 Excel 或 OpenOffice 文件获取页眉和页脚。
---
{{% alert color="primary" %}}

页眉和页脚仅在页面布局视图、打印预览和打印页面上显示。

如果您想要一次查看多个工作表的页眉或页脚，也可以使用“页面设置”对话框。

对于其他工作表类型（例如图表工作表或图表），您只能使用“页面设置”对话框插入页眉和页脚。

{{% /alert %}}

##  **在 MS Excel 中获取页眉和页脚**
1. 单击要查看或更改页眉或页脚的工作表。
2. 在“视图”选项卡的“工作簿视图”组中，单击“页面布局”。
Excel 在页面布局视图中显示工作表。
3. 要查看或编辑页眉或页脚，请单击工作表页面顶部或底部的左侧、中间或右侧页眉或页脚文本框（页眉下方或页脚上方）。


##  **使用 Aspose.Cells for .Net 获取页眉和页脚**
和[**工作表.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/)和[**工作表.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/)方法，.Net 开发人员可以简单地从文件中获取页眉或页脚。

1. 构造工作簿以打开文件。
2. 获取要获取页眉或页脚的工作表。
3. 获取具有特定部分 ID 的页眉或页脚。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

##  **将页眉和页脚解析为命令列表**
页眉或页脚文本可以包含特殊命令，例如页码、当前日期或文本格式属性的占位符。

特殊命令由带有前导与号（“&”）的单个字母表示。

页眉和页脚字符串是使用 ABNF 语法构造的。如果没有观众，就不容易理解。

 Aspose.Cells 为.Net提供[**工作表.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)将页眉和页脚解析为命令列表的方法。

以下代码如何将页眉或页脚解析为命令列表并处理命令：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
