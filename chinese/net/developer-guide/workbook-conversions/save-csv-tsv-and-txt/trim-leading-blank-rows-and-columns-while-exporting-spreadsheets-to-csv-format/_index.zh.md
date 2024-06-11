---
title: 导出电子表格到CSV格式时修剪前导空白行和列
type: docs
weight: 100
url: /zh/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **可能的使用场景**

有时，您的Excel或CSV文件具有前导空白列或行。例如，考虑这条线

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

这里的前三个单元格或列是空白的。当您在Microsoft Excel中打开这样的CSV文件时，Microsoft Excel会丢弃这些前导空白行和列。

默认情况下，Aspose.Cells在保存时不会丢弃前导的空白列和行，但如果您想要像Microsoft Excel一样删除它们，则Aspose.Cells提供了**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)**属性。请将其设置为**true**，然后所有前导的空白行和列都将在保存时被丢弃。

{{% alert color="primary" %}}

在Aspose.Cells for .NET 20.4版本发布之前，默认值的**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)**为**false**。自20.4版本发布以来，**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)**的默认值为**true**。

{{% /alert %}}

## **导出电子表格到CSV格式时修剪前导空白行和列**

以下示例代码加载了包含两个前导空白列的**[源excel文件](sampleTrimBlankColumns.xlsx)**。它首先以不做任何更改的方式将Excel文件保存为CSV格式，然后将**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)**属性设置为**true**，并再次保存。屏幕截图显示了**[源excel文件](sampleTrimBlankColumns.xlsx)**，未修剪空白列的输出CSV文件以及修剪后的输出CSV文件。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
