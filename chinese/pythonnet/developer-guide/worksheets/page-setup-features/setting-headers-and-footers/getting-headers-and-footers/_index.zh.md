---
title: 获取页眉或页脚
type: docs
weight: 30
url: /zh/python-net/get-headers-or-footers/
description: 本文解释了如何以编程方式使用 Aspose.Cells for Python via .NET API 从 Excel 或 OpenOffice 文件中获取页眉和页脚。
keywords: Python Excel 库，Python 获取页眉和页脚，使用 Python 将页眉和页脚解析为命令列表。
---

{{% alert color="primary" %}}

页眉和页脚只出现在页面布局视图、打印预览和打印页面上。 

如果要同时查看多个工作表的页眉或页脚，也可以使用页面设置对话框。 

对于其他工作表类型，如图表工作表或图表，只能通过使用页面设置对话框来插入页眉和页脚。

{{% /alert %}}

## **如何在 MS Excel 中获取页眉和页脚**
1. 单击要查看或更改页眉或页脚的工作表。
2. 在“查看”选项卡的“工作簿视图”组中，单击“页面布局”。
  Excel会以页面布局视图显示工作表。
3. 要查看或编辑页眉或页脚，请单击工作表页面顶部或底部的左侧、中间或右侧页眉或页脚文本框（在页眉下方或在页脚上方）。


## **使用 Aspose.Cells for Python Excel 库获取页眉和页脚**
通过[**Worksheet.page_setup.get_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_header/#int)和[**Worksheet.page_setup.get_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_footer/#int)方法，.Net开发人员可以轻松从文件中获取页眉或页脚。

1.构建工作簿以打开文件。
2. 获取要从中获取页眉或页脚的工作表。
3. 获取具有特定部分ID的页眉或页脚。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Gets-Header-Footer.py" >}}

## **如何将页眉和页脚解析为命令列表**
页眉或页脚文本可以包含特殊命令，例如页码的占位符，当前日期或文本格式属性。

特殊命令由前导和号（"&"）的单个字母表示。

头部和底部字符串使用ABNF语法构建。没有查看器很难理解。

Aspose.Cells for Python via .NET 提供了 [**Worksheet.page_setup.get_commands**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_commands/#str) 方法来将页眉和页脚解析为命令列表。

以下是如何解析页眉或页脚为命令列表并处理命令的代码：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Parses-Header-Footer.py" >}}
