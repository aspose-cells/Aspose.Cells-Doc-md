---
title: 在单元格中显示前导撇号
type: docs
weight: 20
url: /zh/java/show-leading-apostrophe-in-cells/
---

## **在单元格中显示前导撇号**

在Microsoft Excel中，单元格值中的前导撇号是隐藏的。Aspose.Cells提供了按默认方式显示撇号的功能。为此，API 提供了[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)属性。该属性指示是否在输入以单引号开头的字符串值时设置[**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)属性。将[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)属性设置为**false**将在输出的Excel文件中显示前导撇号。

以下屏幕截图显示带有可见撇号的输出excel文件。

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

以下代码片段通过在源excel文件中添加智能标记数据来演示这一点。附有源和输出的excel文件供参考。

[源文件](AllowLeadingApostropheSample.xlsx)

[输出文件](AllowLeadingApostropheSample_out.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

给出*DataObject*类的实现如下

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
