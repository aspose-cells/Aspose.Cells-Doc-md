---
title: 将Excel转换为CSV、TSV和Txt
linktitle: 另存为CSV，TSV和Txt
type: docs
weight: 40
url: /zh/net/convert-excel-to-csv-tsv-and-txt/
---

{{% alert color="primary" %}}

Aspose.Cells使将Excel、ods、json和其他格式文件转换为CSV、TSV和TXT成为可能。

{{% /alert %}}

## **将工作簿保存为文本或CSV格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何包含任意工作表数量的Microsoft Excel或OpenOffice电子表格文件（如XLS、XLSX、XLSM、XLSB、ODS等）。

当代码执行时，它将工作簿中所有工作表的数据转换为TXT格式。

您可以修改相同示例以将文件保存为CSV。默认情况下，**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)** 为逗号，因此如果保存为CSV格式，则不要指定分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **以自定义分隔符保存文本文件**

文本文件包含没有格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **高级主题**
- [在将电子表格导出为CSV格式时保留空白行的分隔符](/cells/zh/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [在将电子表格导出为CSV格式时修剪前导空白行和列](/cells/zh/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
