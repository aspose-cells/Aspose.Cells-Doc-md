---
title: 使用Aspose.Cells将文本转换为列
type: docs
weight: 30
url: /zh/python-net/convert-text-to-columns-using-aspose-cells/
description: 本文介绍了如何通过 Aspose.Cells for Python via .NET API 进行文本列转换。
keywords: Python Excel库, Python文本列转换, Python中的文本列转换。
---

## **可能的使用场景**

您可以使用Microsoft Excel将文本转换为列。此功能可在*数据*标签下的*数据工具*中找到。要将列的内容拆分为多个列，数据应包含特定的分隔符，例如逗号（或任何其他字符），基于该分隔符，Microsoft Excel将单元格的内容拆分为多个单元格。Aspose.Cells for Python via .NET 也通过 [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) 方法提供此功能。

## **使用 Aspose.Cells for Python Excel库进行文本列转换**

以下示例代码解释了[**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/)方法的用法。代码首先在第一个工作表的列A中添加了一些人名。名和姓由空格字符分隔。然后，它在列A上应用[**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/)方法，并将其保存为输出excel文件。如果打开[输出excel文件](25395213.xlsx)，您将会看到，名字在A列，姓氏在B列，如此屏幕截图所示。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
