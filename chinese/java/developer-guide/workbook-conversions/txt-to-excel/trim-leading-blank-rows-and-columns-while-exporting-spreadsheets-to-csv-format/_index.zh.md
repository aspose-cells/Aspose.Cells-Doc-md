---
title: 在将电子表格导出为CSV格式时修剪前导空行和列
type: docs
weight: 50
url: /zh/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **可能的使用场景**

有时，您的Excel或CSV文件具有前导的空列或行。例如，考虑这行

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

默认情况下，Aspose.Cells在保存时不会丢弃前导的空列和行，但如果您想要像Microsoft Excel一样删除它们，则Aspose.Cells提供了[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)属性。请将它设置为true，然后在保存时所有前导的空行和列都将被丢弃。

默认情况下，Aspose.Cells在保存时不会丢弃前导空白列和行，但如果您希望像Microsoft Excel一样将它们删除，Aspose.Cells提供**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** 属性。请将其设置为**true**，然后在保存时将会丢弃所有前导空白行和列。

{{% alert color="primary" %}}

在Aspose.Cells for .NET 20.4发布之前，**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**的默认值为**false**。自20.4版本以来，**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**的默认值为**true**。

{{% /alert %}}

## **在将电子表格导出为CSV格式时修剪前导空白行和列**

以下示例代码加载具有两个前导空白列的源Excel文件。它首先以无任何更改的CSV格式保存Excel文件，然后将**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** 属性设置为**true**，再次保存。截图显示了[源Excel文件](sampleTrimBlankColumns.xlsx)，[不修剪的输出CSV文件](outputWithoutTrimBlankColumns.csv)和 [修剪后的输出CSV文件](outputTrimBlankColumns.csv)。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
