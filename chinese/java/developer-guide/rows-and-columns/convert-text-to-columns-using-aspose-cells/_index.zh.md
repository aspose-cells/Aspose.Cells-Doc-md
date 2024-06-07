---
title: 使用Aspose.Cells将文本转换为列
type: docs
weight: 70
url: /zh/java/convert-text-to-columns-using-aspose-cells/
---

## **可能的使用场景**
您可以使用Microsoft Excel将文本转换为列。此功能在*数据*选项卡下的*数据工具*中可用。为了将列的内容拆分为多个列，数据应包含特定的分隔符，例如逗号(或其他字符)，根据该分隔符，Microsoft Excel将单元格的内容拆分为多个单元格。Aspose.Cells也通过[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\))方法提供此功能。
## **使用 Aspose.Cells 将文本转换为列**
下面的示例代码解释了[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\))方法的用法。代码首先在第一个工作表的列A中添加了一些人名。名字和姓氏之间用空格分隔。然后在列A上应用[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\))方法，并将其另存为输出Excel文件。如果您打开[输出的Excel文件](25395230.xlsx)，您会看到名字在A列，姓氏在B列，如此截图所示。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
