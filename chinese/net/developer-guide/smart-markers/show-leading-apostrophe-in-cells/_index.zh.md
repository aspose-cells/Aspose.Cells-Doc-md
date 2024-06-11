---
title: 在单元格中显示前导撇号
type: docs
weight: 70
url: /zh/net/show-leading-apostrophe-in-cells/
---

在Microsoft Excel中，单元格值的前导'是隐藏的。Aspose.Cells提供了默认显示撇号的功能。为此，API提供了[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) 属性。此属性指示在输入以单引号开头的字符串值时是否设置 [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) 。将[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) 属性设置为**false** 将在输出的excel文件中显示前导'。 

以下屏幕截图显示了带有可见撇号的输出Excel文件。

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

以下代码片段演示了通过在源Excel文件中添加带有智能标记的数据来实现此目的。 源文件和输出文件已附上以供参考。

[源文件](98107425.xlsx)

[输出文件](98107426.xlsx)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

*DataObject*类的实现如下

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
