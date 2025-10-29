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

默认情况下，Aspose.Cells for Python via .NET 在保存时不会丢弃前导空白列和行，但如果您希望像 Microsoft Excel 一样删除它们，那么 Aspose.Cells for Python via .NET 提供了 [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) 属性。请将其设置为 **true**，那么所有前导空白行和列在保存时都将被丢弃。

{{% alert color="primary" %}}

在 Aspose.Cells for Python via .NET 20.4 版本之前，[**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) 的默认值为 **false**。自 20.4 版本以来，[**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) 的默认值为 **true**。

{{% /alert %}}

## **导出电子表格到CSV格式时修剪前导空白行和列**

以下示例代码加载了具有两个前导空白列的 [源 Excel 文件](sampleTrimBlankColumns.xlsx)。首先保存 Excel 文件为 CSV 格式而不进行任何更改，然后将 [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) 属性设置为 **true** 并再次保存。截图显示了 [源 Excel 文件](sampleTrimBlankColumns.xlsx)，[未修剪的输出 CSV 文件](outputWithoutTrimBlankColumns.csv) 和 [修剪后的输出 CSV 文件](outputTrimBlankColumns.csv)。

![todo:image_alt_text](result.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
