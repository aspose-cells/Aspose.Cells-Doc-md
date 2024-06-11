---
title: 使用Aspose.Cells将文本转换为列
type: docs
weight: 70
url: /zh/java/convert-text-to-columns-using-aspose-cells/
---

## **可能的使用场景**
您可以使用 Microsoft Excel 将文本转换为列。此功能可从 *数据* 选项卡的 *数据工具* 下使用。为了将一列内容拆分为多个列，数据应该包含特定分隔符，例如逗号（或其他字符），根据此分隔符 Microsoft Excel 将单元格的内容拆分为多个单元格。Aspose.Cells 也通过 [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) 方法提供了此功能。
## **使用Aspose.Cells将文本转换为列**
以下示例代码说明了使用[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\))方法。 该代码首先将一些人名添加到第一个工作表的A列中。 名字由空格分隔为名和姓。 然后，在A列上应用[TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\))方法，并将其保存为输出Excel文件。 如果您打开[输出Excel文件](25395230.xlsx)，您将看到名字在A列中，姓在B列中，如此屏幕截图所示。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
