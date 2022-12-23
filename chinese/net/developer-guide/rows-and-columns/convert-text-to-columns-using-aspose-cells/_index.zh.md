---
title: 使用 Aspose.Cells 将文本转换为列
type: docs
weight: 30
url: /zh/net/convert-text-to-columns-using-aspose-cells/
---
## **可能的使用场景**

您可以使用 Microsoft Excel 将文本转换为列。此功能可从*数据工具*在下面*数据*标签。为了将一列的内容拆分为多列，数据应包含特定的分隔符，例如逗号（或任何其他字符），Microsoft Excel 将一个单元格的内容拆分为多个单元格。 Aspose.Cells 也通过以下方式提供此功能[**工作表.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法。

## **使用 Aspose.Cells 将文本转换为列**

下面的示例代码解释了[**工作表.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)方法。该代码首先在第一个工作表的 A 列中添加一些人名。名字和姓氏由空格字符分隔。然后它适用[**工作表.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) 列上的方法并将其保存为输出 excel 文件。如果你打开[输出excel文件](25395213.xlsx)，您会看到，名字在 A 列中，而姓氏在 B 列中，如屏幕截图所示。

![待办事项：图片_替代_文本](convert-text-to-columns-using-aspose-cells_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
