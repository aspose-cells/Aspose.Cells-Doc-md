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

默认情况下，Aspose.Cells 在保存时不会丢弃前导空白列和行，但如果您希望像 Microsoft Excel 一样移除它们，Aspose.Cells 提供了 [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) 属性。请将其设置为 **true**，然后在保存时所有前导空白行和列将被丢弃。

{{% alert color="primary" %}}

在 Aspose.Cells for .NET 20.4 版本发布之前，默认值为 [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) 的是 **false**。自 20.4 版本发布以来，[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) 的默认值为 **true**。

{{% /alert %}}

## **导出电子表格到CSV格式时修剪前导空白行和列**

以下示例代码加载了具有两个前导空白列的源 Excel 文件。首先在不进行任何更改的情况下将 excel 文件保存为 CSV 格式，然后将 [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) 属性设置为 **true** 并再次保存。截图展示了 [源 Excel 文件](sampleTrimBlankColumns.xlsx)、[没有修剪的输出 CSV 文件](outputWithoutTrimBlankColumns.csv) 和 [修剪后的输出 CSV 文件](outputTrimBlankColumns.csv)。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}
