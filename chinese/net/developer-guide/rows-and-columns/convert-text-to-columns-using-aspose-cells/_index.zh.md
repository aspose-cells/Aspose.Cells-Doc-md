---
title: 使用Aspose.Cells将文本转换为列
type: docs
weight: 30
url: /zh/net/convert-text-to-columns-using-aspose-cells/
---

## **可能的使用场景**

您可以使用Microsoft Excel将文本转换为列。此功能可从*数据*选项卡下的*数据工具*中获取。为了将一列的内容拆分为多个列，数据应包含特定的分隔符，例如逗号（或其他字符），Microsoft Excel根据其将单元格的内容拆分为多个单元格。Aspose.Cells还提供了通过[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法实现此功能。

## **使用Aspose.Cells将文本转换为列**

以下示例代码解释了[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法的用法。代码首先在第一个工作表的列A中添加了一些人名。名和姓由空格字符分隔。然后，它在列A上应用[**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法，并将其保存为输出excel文件。如果打开[输出excel文件](25395213.xlsx)，您将会看到，名字在A列，姓氏在B列，如此屏幕截图所示。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
{{< app/cells/assistant language="csharp" >}}
