---
title: 获取页眉或页脚
type: docs
weight: 30
url: /zh/net/get-headers-or-footers/
description: 本文说明了如何使用C# API或.NET库从Excel或OpenOffice文件中以编程方式获取页眉和页脚。
---

{{% alert color="primary" %}}

页眉和页脚仅在页面布局视图，打印预览和打印页面中显示。 

如果要一次查看多个工作表的页眉或页脚，还可以使用页面设置对话框。 

对于其他工作表类型，例如图表工作表或图表，只能使用页面设置对话框插入页眉和页脚。

{{% /alert %}}

## **在MS Excel中获取页眉和页脚**
1. 单击要查看或更改页眉或页脚的工作表。
2. 在"视图"选项卡上，在"工作表视图"组中，单击"页面布局"。
  Excel会将工作表显示为页面布局视图。
3. 要查看或编辑页眉或页脚，请单击工作表页面的顶部或底部的左、中、或右页眉或页脚文本框（在标题下方，或在页脚上方）。


## **使用Aspose.Cells for .Net获取页眉和页脚**
通过[**Worksheet.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/)和[**Worksheet.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/)方法，.Net开发人员可以轻松地从文件中获取页眉或页脚。

1. 构建Workbook打开文件。
2. 获取要获取页眉或页脚的工作表。
3. 使用特定部分ID获取页眉或页脚。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

## **解析页眉和页脚到命令列表**
页眉或页脚文本可以包含特殊命令，例如页码的占位符，当前日期或文本格式属性。

特殊命令以单个字母表示，前面带有和号("&")。

页眉和页脚字符串使用ABNF语法构建。如果没有查看器，将很难理解。

Aspose.Cells for .Net提供了[**Worksheet.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)方法，用于解析页眉和页脚作为命令列表。

以下代码展示了如何解析页眉或页脚作为命令列表并处理命令:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
