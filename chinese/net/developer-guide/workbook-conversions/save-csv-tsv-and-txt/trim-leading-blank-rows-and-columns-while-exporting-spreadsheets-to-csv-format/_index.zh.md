---
title: 在将电子表格导出为CSV格式时修剪前导空行和列
type: docs
weight: 100
url: /zh/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **可能的使用场景**

有时，您的Excel或CSV文件具有前导的空列或行。例如，考虑这行

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

默认情况下，Aspose.Cells在保存时不会丢弃前导的空列和行，但如果您想要像Microsoft Excel一样删除它们，则Aspose.Cells提供了[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)属性。请将它设置为true，然后在保存时所有前导的空行和列都将被丢弃。

在Aspose.Cells for .NET 20.4发布之前，[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)的默认值为false。自20.4发布以来，[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)的默认值是true。

{{% alert color="primary" %}}

在发布Aspose.Cells for .NET 20.4之前，默认值为**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)**为**false**。自20.4版本以来，默认值为**true**。

{{% /alert %}}

## **在将电子表格导出为CSV格式时修剪前导空白行和列**

以下示例代码加载了[源Excel文件](sampleTrimBlankColumns.xlsx)，它具有两个前导的空列。首先按原样保存电子表格文件，然后将[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)属性设置为true，并再次保存。屏幕截图显示了[源Excel文件](sampleTrimBlankColumns.xlsx)，[不修剪空列的输出CSV文件](outputWithoutTrimBlankColumns.csv)和[修剪后的输出CSV文件](outputTrimBlankColumns.csv)。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
