---
title: 使用 Aspose.Cells 将文本转换为列
type: docs
weight: 70
url: /zh/java/convert-text-to-columns-using-aspose-cells/
---
## **可能的使用场景**
您可以使用 Microsoft Excel 将文本转换为列。此功能可从*数据工具*在下面*数据*标签。为了将一列的内容拆分为多列，数据应包含特定的分隔符，例如逗号（或任何其他字符），Microsoft Excel 将一个单元格的内容拆分为多个单元格。 Aspose.Cells 也通过以下方式提供此功能[文本到列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)） 方法。
## **使用 Aspose.Cells 将文本转换为列**
下面的示例代码解释了[文本到列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)） 方法。该代码首先在第一个工作表的 A 列中添加一些人名。名字和姓氏由空格字符分隔。然后它应用[文本到列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\) 方法，并将其保存为输出 excel 文件。如果你打开[输出excel文件](25395230.xlsx)，您会看到，名字在 A 列中，而姓氏在 B 列中，如屏幕截图所示。

![待办事项：图像_替代_文本](convert-text-to-columns-using-aspose-cells_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
