---
title: 从 Cell 访问表并使用行和列偏移量在其中添加值
type: docs
weight: 110
url: /zh/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

通常，您在表或列表对象中添加值使用[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)） 方法。但有时，您可能需要使用行和列偏移量在表或列表对象中添加值。

为了从单元格访问表或列表对象，使用[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ） 方法。并使用行和列偏移量在其中添加值，使用[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)） 方法。

{{% /alert %}}

## 例子

### 比较源文件和输出文件的屏幕截图

以下屏幕截图显示了代码中使用的源 Excel 文件。它包含空表并突出显示位于表内的单元格 D5。我们将从单元格 D5 使用访问此表[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() 方法，然后使用两者添加其中的值[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)） 和[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)） 方法。

![待办事项：图像_替代_文本](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

以下屏幕截图显示了代码生成的输出 Excel 文件。如您所见，单元格 D5 有一个值，而位于表格偏移量 2,2 处的单元格 F6 有一个值。

![待办事项：图像_替代_文本](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java 从单元格访问表格并使用行和列偏移量在其中添加值的代码

以下示例代码加载如上图所示的源 Excel 文件，并在表内添加值并生成如上所示的输出 Excel 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
