---
title: 在将电子表格导出为CSV格式时修剪前导空行和列
type: docs
weight: 100
url: /zh/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: 通过使用Aspose.Cells for Python通过.NET API在将电子表格导出为CSV格式时修剪前导空行和列
keywords: Python在将电子表格导出为CSV格式时修剪前导空行和列，在Python via NET中将电子表格保存为CSV格式时修剪前导空行和列，导出excel时修剪前导空行和列。
---

## **可能的使用场景**

有时，您的Excel或CSV文件具有前导的空列或行。例如，考虑这行

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

默认情况下，Aspose.Cells在保存时不会丢弃前导的空列和行，但如果您想要像Microsoft Excel一样删除它们，则Aspose.Cells提供了[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)属性。请将它设置为true，然后在保存时所有前导的空行和列都将被丢弃。

默认情况下，Aspose.Cells for Python通过.NET在保存时不会丢弃前导空列和行，但是如果您想要像Microsoft Excel一样将它们删除，则Aspose.Cells for Python通过.NET提供了**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** 属性。请将其设置为**true**，然后保存时所有前导空行和列将被丢弃。

{{% alert color="primary" %}}

在Aspose.Cells for Python通过.NET 20.4版本发布之前，**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** 的默认值为**false**。自20.4版本以来，**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** 的默认值为**true**。

{{% /alert %}}

## **在将电子表格导出为CSV格式时修剪前导空白行和列**

以下示例代码加载了具有两个前导空白列的“源Excel文件（sampleTrimBlankColumns.xlsx）”。首先将Excel文件保存为CSV格式，不做任何更改，然后将**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**属性设置为**true**，并再次保存。屏幕截图显示了“源Excel文件（sampleTrimBlankColumns.xlsx）”、“未修整的输出CSV文件（outputWithoutTrimBlankColumns.csv）”和“修整后的输出CSV文件（outputTrimBlankColumns.csv）”。

![todo:image_alt_text](result.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
