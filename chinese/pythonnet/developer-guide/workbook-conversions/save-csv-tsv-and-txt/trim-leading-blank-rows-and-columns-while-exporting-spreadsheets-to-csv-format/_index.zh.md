---
title: 将电子表格导出为 CSV 格式时修剪前导空白行和列
type: docs
weight: 100
url: /zh/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: 使用 Aspose.Cells for Python via .NET API 将电子表格导出为 CSV 格式时修剪前导空白行和列。
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **可能的使用场景**

有时，您的 Excel 或 CSV 文件具有前导空白列或行。例如，考虑这一行

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

这里前三个单元格或列是空白的。当您在 Microsoft Excel 中打开这样的 CSV 文件时，Microsoft Excel 会丢弃这些前导空白行和列。

默认情况下， Aspose.Cells for Python via .NET 在保存时不会丢弃前导空白列和行，但如果您想像 Microsoft Excel 一样删除它们，则 Aspose.Cells for Python via .NET 提供**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**财产。请设置为**真的**然后所有前导空白行和列将在保存时被丢弃。

{{% alert color="primary" %}}

在Aspose.Cells for Python via .NET 20.4发布之前，默认值为**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**曾是**错误的**。自 20.4 版本以来，默认值 **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**是**真的。**

{{% /alert %}}

##  **将电子表格导出为 CSV 格式时修剪前导空白行和列**

以下示例代码加载[源 Excel 文件](sampleTrimBlankColumns.xlsx)其中有两个前导空白列。它首先将excel文件保存为CSV格式，不进行任何更改，然后设置**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**财产给**真的**并再次保存。屏幕截图显示[源 Excel 文件](sampleTrimBlankColumns.xlsx), [输出 CSV 文件而不进行修剪](outputWithoutTrimBlankColumns.csv)，以及[输出 CSV 文件并进行修剪](outputTrimBlankColumns.csv).

![待办事项：图像_替代_文本](result.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
