---
title: 导出电子表格到CSV格式时修剪前导空白行和列
type: docs
weight: 100
url: /zh/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: 使用Aspose.Cells for Python via .NET API，在导出电子表格到CSV格式时修剪前导空行和列。
keywords: Python导出电子表格到CSV格式时修剪前导空行和列，Python via NET中导出电子表格到CSV格式时修剪前导空行和列，Python导出带有公式的CSV到xlsx，导入带有公式的CSV到Excel文件。
---

## **可能的使用场景**

有时，您的Excel或CSV文件具有前导空白列或行。例如，考虑这条线

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

这里的前三个单元格或列是空白的。当您在Microsoft Excel中打开这样的CSV文件时，Microsoft Excel会丢弃这些前导空白行和列。

默认情况下，Aspose.Cells for Python via .NET在保存时不会丢弃前导空列和行，但如果您想要删除它们，就像Microsoft Excel一样，那么Aspose.Cells for Python via .NET提供了trim_leading_blank_row_and_column属性。请将其设置为true，然后在保存时将丢弃所有前导空行和列。

{{% alert color="primary" %}}

在Aspose.Cells for Python via .NET 20.4发布之前，TxtSaveOptions.trim_leading_blank_row_and_column的默认值为false。自20.4版本以来，TxtSaveOptions.trim_leading_blank_row_and_column的默认值为true。

{{% /alert %}}

## **导出电子表格到CSV格式时修剪前导空白行和列**

以下示例代码加载了包含两个前导空列的源Excel文件sampleTrimBlankColumns.xlsx。首先将Excel文件另存为CSV格式，然后将trim_leading_blank_row_and_column属性设置为true，并再次保存。屏幕截图显示了源Excel文件、不修剪的输出CSV文件和修剪后的输出CSV文件。

![todo:image_alt_text](result.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
