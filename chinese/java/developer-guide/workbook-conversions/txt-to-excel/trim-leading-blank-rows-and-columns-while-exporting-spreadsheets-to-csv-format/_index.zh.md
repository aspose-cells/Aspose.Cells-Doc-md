---
title: 导出电子表格到CSV格式时修剪前导空白行和列
type: docs
weight: 50
url: /zh/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **可能的使用场景**

有时，您的Excel或CSV文件具有前导空白列或行。例如，考虑这条线

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

这里的前三个单元格或列是空白的。当您在Microsoft Excel中打开这样的CSV文件时，Microsoft Excel会丢弃这些前导空白行和列。

默认情况下，Aspose.Cells在保存时不会丢弃前导空白列和行，但是如果您想要像Microsoft Excel那样删除它们，那么Aspose.Cells提供**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**属性。请将其设置为**true**，然后所有前导空白行和列都将在保存时被丢弃。

{{% alert color="primary" %}}

在发布 Aspose.Cells for .NET 20.4之前，默认值为 **[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** 是 **false**。 自20.4版本以来， **[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** 的默认值为 **true**。

{{% /alert %}}

## **导出电子表格到CSV格式时修剪前导空白行和列**

以下示例代码加载具有两个前导空白列的源excel文件。它首先保存不做任何更改的excel文件为CSV格式，然后将**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**属性设置为**true**，再次保存。屏幕截图显示了[源excel文件](sampleTrimBlankColumns.xlsx)，[未修剪的输出CSV文件](outputWithoutTrimBlankColumns.csv)，以及[修剪后的输出CSV文件](outputTrimBlankColumns.csv)。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
