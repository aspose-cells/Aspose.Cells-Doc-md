---
title: 将Excel转换为CSV、TSV和Txt
linktitle: 另存为CSV，TSV和Txt
type: docs
weight: 40
url: /zh/python-net/convert-excel-to-csv-tsv-and-txt/
description: 使用Aspose.Cells for Python via .NET API将Excel转换为CSV、TSV和Txt。
keywords: Python将Excel转换为CSV、TSV和Txt，在Python via .NET中将Excel转换为CSV、TSV和Txt，Python将工作簿转换为CSV、TSV和Txt。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET使得将Excel、ods、json和其他格式文件转换为CSV、TSV和TXT成为可能。

{{% /alert %}}

## **将工作簿保存为文本或CSV格式**

有时，您可能希望将包含多个工作表的工作簿转换为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells for Python via .NET仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何包含任意工作表数量的Microsoft Excel或OpenOffice电子表格文件（如XLS、XLSX、XLSM、XLSB、ODS等）。

当代码执行时，它将工作簿中所有工作表的数据转换为TXT格式。

您可以修改相同的示例以将文件保存为CSV。默认情况下，**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)** 为逗号，因此在保存为CSV格式时不需要指定分隔符。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **以自定义分隔符保存文本文件**

文本文件包含没有格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **高级主题**
- [在将电子表格导出为CSV格式时保留空白行的分隔符](/cells/zh/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [在将电子表格导出为CSV格式时修剪前导空白行和列](/cells/zh/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
