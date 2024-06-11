---
title: 使用Aspose.Cells将文本转换为列
type: docs
weight: 30
url: /zh/python-net/convert-text-to-columns-using-aspose-cells/
description: 本文介绍了如何通过 Aspose.Cells for Python 通过 .NET API 将文本转换为列。
keywords: Python Excel库，Python将文本转换为列，在Python中将文本转换为列。
---

## **可能的使用场景**

您可以使用Microsoft Excel将文本转换为列。此功能可从“数据”选项卡下的“数据工具”中使用。为了将列的内容拆分成多个列，数据应包含特定的分隔符，如逗号（或任何其他字符），根据此分隔符，Microsoft Excel将单元格的内容拆分为多个单元格。Aspose.Cells for Python 通过 .NET 也通过 [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) 方法提供此功能。

## **使用 Aspose.Cells for Python Excel库将文本转换为列**

以下示例代码解释了如何使用[**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/)方法。代码首先在第一个工作表的列A中添加一些人名。名字和姓氏用空格字符分隔。然后在列A上应用[**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/)方法，并将其保存为输出Excel文件。如果您打开[输出的Excel文件](25395213.xlsx)，您会看到，名字在列A中而姓氏在列B中，如此屏幕截图所示。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
