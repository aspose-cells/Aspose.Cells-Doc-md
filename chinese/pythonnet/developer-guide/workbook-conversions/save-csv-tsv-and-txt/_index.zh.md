---
title: 将Excel转换为CSV,TSV和Txt
linktitle: 另存为 CSV,TSV 和 TXT
type: docs
weight: 40
url: /zh/python-net/convert-excel-to-csv-tsv-and-txt/
description: 使用 Aspose.Cells for Python via .NET API 将 Excel 转换为 CSV,TSV 和 Txt。
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET可以将excel、ods、json等格式文件转换为CSV、TSV和TXT。

{{% /alert %}}

##  **将工作簿保存为文本或 CSV 格式**

有时，您想要将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如 TXT、TabDelim、CSV 等），默认情况下 Microsoft Excel 和 Aspose.Cells for Python via .NET 仅保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何 Microsoft Excel 或 OpenOffice 电子表格文件（例如 XLS、XLSX、XLSM、XLSB、ODS 等）以及任意数量的工作表。

执行代码时，会将工作簿中所有工作表的数据转换为 TXT 格式。

您可以修改相同的示例以将文件保存到 CSV。默认情况下，**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**是逗号，因此如果保存为 CSV 格式，则无需指定分隔符。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **使用自定义分隔符保存文本文件**

文本文件包含未格式化的电子表格数据。该文件是一种纯文本文件，其数据之间可以有一些自定义的分隔符。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **高级主题**
- [将电子表格导出为 CSV 格式时保留空白行分隔符](/cells/zh/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [将电子表格导出为 CSV 格式时修剪前导空白行和列](/cells/zh/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
