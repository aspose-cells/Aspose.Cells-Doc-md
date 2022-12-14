---
title: 将电子表格导出为 CSV 格式时修剪前导空白行和列
type: docs
weight: 50
url: /zh/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **可能的使用场景**

有时，您的 Excel 或 CSV 文件有前导空白列或行。例如，考虑这一行

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

这里前三个单元格或列是空白的。当您在 Microsoft Excel 中打开此类 CSV 文件时，Microsoft Excel 会丢弃这些前导空白行和列。

默认情况下，Aspose.Cells 在保存时不会丢弃前导空白列和行，但如果您想像 Microsoft Excel 那样删除它们，则 Aspose.Cells 提供**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**财产。请设置为**真的**然后所有领先的空白行和列将在保存时被丢弃。

{{% alert color="primary" %}}

 Aspose.Cells for .NET 20.4 发布之前，默认值为**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**曾是**错误的**.自 20.4 版本以来，默认值为**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**是**真的。**

{{% /alert %}}

## **将电子表格导出为 CSV 格式时修剪前导空白行和列**

以下示例代码加载具有两个前导空白列的源 excel 文件。它首先将 excel 文件保存为 CSV 格式，不做任何更改，然后设置**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**财产给**真的**并再次保存。屏幕截图显示[源文件](sampleTrimBlankColumns.xlsx), [输出 CSV 文件而不修剪](outputWithoutTrimBlankColumns.csv)和[输出带修整的 CSV 文件](outputTrimBlankColumns.csv).

![待办事项：图片_替代_文本](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
