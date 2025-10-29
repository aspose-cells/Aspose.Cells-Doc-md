---
title: 使用Aspose.Cells将文本转换为列
type: docs
weight: 70
url: /zh/java/convert-text-to-columns-using-aspose-cells/
---

## **可能的使用场景**
你可以使用 Microsoft Excel 将文本转换为列。此功能在 *Data Tools* 下的 *Data* 选项卡中。为了将列内容拆分为多列，数据应包含特定分隔符，如逗号（或任何其他字符），Microsoft Excel 根据此字符将单元格内容拆分到多个单元格。Aspose.Cells 也提供此功能，使用 [TextToColumns](https://reference.aspose.com/cells/zh/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) 方法。
## **使用Aspose.Cells将文本转换为列**
以下示例代码说明了 [TextToColumns](https://reference.aspose.com/cells/zh/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) 方法的用法。代码首先在第一个工作表的列A中添加一些人名，名字和姓氏用空格字符分隔。然后对A列应用 [TextToColumns](https://reference.aspose.com/cells/zh/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) 方法，并将其保存为输出Excel文件。如果你打开 [输出Excel文件](25395230.xlsx)，你会看到，名放在A列，姓放在B列，如截图所示。

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}
