---
title: 使用 Golang 通过 C++ 将 Excel 转换为 CSV、TSV 和 Txt
linktitle: 另存为CSV、TSV和Txt
type: docs
weight: 40
url: /zh/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: 轻松使用 Aspose.Cells 通过 C++ 将 Excel 文件转换为 CSV、TSV 和 Txt 格式
---

{{% alert color="primary" %}}

Aspose.Cells支持将Excel、ODS、JSON及其他格式文件转换为CSV、TSV和TXT。

{{% /alert %}}

## **将工作簿保存为文本或CSV格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells都仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何Microsoft Excel或OpenOffice电子表格文件（例如XLS、XLSX、XLSM、XLSB、ODS等），并且可以具有任意数量的工作表。

执行代码后，将会将工作簿中所有工作表的数据转换为TXT格式。

你可以修改相同的示例，将文件保存为CSV格式。默认情况下，[**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/)为逗号，所以在保存为CSV格式时无需指定分隔符。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **使用自定义分隔符保存文本文件**

文本文件包含无格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **高级主题**
- [在将电子表格导出为CSV格式时保留空行的分隔符](/cells/zh/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [导出电子表格到CSV格式时修剪前导空白行和列](/cells/zh/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
