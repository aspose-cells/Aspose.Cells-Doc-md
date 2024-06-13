---
title: 在将电子表格导出为CSV格式时保留空行的分隔符
type: docs
weight: 160
url: /zh/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: 通过使用Aspose.Cells for Python via .NET API，在将电子表格导出为CSV格式时保留空行的分隔符。
keywords: 在Python中，在将电子表格导出为CSV格式时，通过使用Python via NET保留空行的分隔符，在将Excel保存为CSV格式时，通过Python保留空行的分隔符。
---

## **在将电子表格导出为CSV格式时保留空行的分隔符**

Aspose.Cells for Python via .NET 具有将行分隔符保留在将电子表格转换为 CSV 格式时的功能。为此，您可以使用 [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) 类的 [**TxtSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/) 属性。[**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) 是一个布尔属性。要在将 Excel 文件转换为 CSV 时保留空行的分隔符，请将 [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) 属性设置为 **true**。

以下示例代码加载了 [源 Excel 文件](84378743.xlsx)，将 [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) 属性设置为 **true** 并将其保存为 [output.csv](84378744.csv)。截图显示了源 Excel 文件，将电子表格转换为 CSV 时生成的默认输出以及将 [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) 设置为 **true** 时生成的输出的比较。

![todo:image_alt_text](result.jpg)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
