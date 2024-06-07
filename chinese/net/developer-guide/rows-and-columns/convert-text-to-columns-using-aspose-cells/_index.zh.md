---
title: 使用Aspose.Cells将文本转换为列
type: docs
weight: 30
url: /zh/net/convert-text-to-columns-using-aspose-cells/
---

## **可能的使用场景**

您可以使用Microsoft Excel将文本转换为列。此功能在*数据*选项卡下的*数据工具*中可用。为了将列的内容拆分为多列，数据应包含特定的分隔符，如逗号（或其他字符），根据该分隔符，Microsoft Excel将单元格的内容拆分为多个单元格。Aspose.Cells还通过[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法提供了此功能。

## **使用 Aspose.Cells 将文本转换为列**

以下示例代码解释了如何使用[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法。代码首先在第一个工作表的列A中添加一些人名。名字和姓氏用空格字符分隔。然后在列A上应用[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法，并将其保存为输出Excel文件。如果您打开[输出的Excel文件](25395213.xlsx)，您会看到，名字在列A中而姓氏在列B中，如此屏幕截图所示。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
