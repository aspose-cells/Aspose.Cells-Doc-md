---
title: 在单元格中显示前导撇号
type: docs
weight: 20
url: /zh/java/show-leading-apostrophe-in-cells/
---
## **在单元格中显示前导撇号**

在 Microsoft Excel 中，单元格值中的前导撇号被隐藏。 Aspose.Cells 提供默认显示撇号的功能。为此，API 提供[**工作簿.设置.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)财产。该属性表示是否设置[**引用前缀**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)向单元格输入以单引号开头的字符串值时的属性。设定[**工作簿.设置.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)财产给**错误的**将在输出 excel 文件中显示前导撇号。

以下屏幕截图显示了带有可见撇号的输出 excel 文件。

![待办事项：图像_替代_文本](show-leading-apostrophe-in-cells_1.jpg)

以下代码片段通过在源 excel 文件中添加带有智能标记的数据来演示这一点。附上源文件和输出 excel 文件以供参考。

[源文件](AllowLeadingApostropheSample.xlsx)

[输出文件](AllowLeadingApostropheSample_out.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

实施*数据对象*课程如下

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
