---
title: 在将电子表格导出为CSV格式时保留空行的分隔符
type: docs
weight: 160
url: /zh/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: 通过使用Aspose.Cells for Python via .NET API，在将电子表格导出为CSV格式时保留空行的分隔符。
keywords: 在Python中，在将电子表格导出为CSV格式时，通过使用Python via NET保留空行的分隔符，在将Excel保存为CSV格式时，通过Python保留空行的分隔符。
---

## **在将电子表格导出为CSV格式时保留空行的分隔符**

Aspose.Cells for Python via .NET提供了在将电子表格转换为CSV格式时保留行分隔符的功能。为此，您可以使用TxtSaveOptions类的keep_separators_for_blank_row属性。keep_separators_for_blank_row是一个布尔属性。要在将Excel文件转换为CSV时保留空行的分隔符，请将keep_separators_for_blank_row属性设置为true。

以下示例代码加载了源Excel文件84378743.xlsx。将keep_separators_for_blank_row属性设置为true，然后将其另存为输出文件84378744.csv。屏幕截图显示了源Excel文件、将电子表格转换为CSV时生成的默认输出以及将keep_separators_for_blank_row设置为true时生成的输出。

![todo:image_alt_text](result.jpg)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
