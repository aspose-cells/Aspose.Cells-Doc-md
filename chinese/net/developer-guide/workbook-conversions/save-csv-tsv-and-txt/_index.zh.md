---
title: 将 Excel 转换为 CSV、TSV 和 Txt
linktitle: 另存为 CSV、TSV 和 Txt
type: docs
weight: 40
url: /zh/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

Aspose.Cells可以将excel、ods、json等格式文件转换为CSV、TSV、TXT。

{{% /alert %}}

## **将工作簿保存为文本或 CSV 格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如 TXT、TabDelim、CSV 等），默认情况下 Microsoft Excel 和 Aspose.Cells 都只保存活动工作表的内容。

下面的代码示例说明了如何将整个工作簿保存为文本格式。加载源工作簿，它可以是任何 Microsoft Excel 或 OpenOffice 电子表格文件（如 XLS、XLSX、XLSM、XLSB、ODS 等）和任意数量的工作表。

代码执行时，将工作簿中所有工作表的数据转换为TXT格式。

您可以修改同一示例以将文件保存为 CSV。默认，**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**是逗号，所以如果保存为 CSV 格式，请不要指定分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **使用自定义分隔符保存文本文件**

文本文件包含未格式化的电子表格数据。该文件是一种纯文本文件，其数据之间可以有一些自定义的分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **推进主题**
- [将电子表格导出为 CSV 格式时保留空白行的分隔符](/cells/zh/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [将电子表格导出为 CSV 格式时修剪前导空白行和列](/cells/zh/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
