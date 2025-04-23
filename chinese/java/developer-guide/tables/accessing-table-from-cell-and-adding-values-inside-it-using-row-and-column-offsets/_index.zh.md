---
title: 从单元格访问表格并使用行和列偏移添加值
type: docs
weight: 110
url: /zh/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

通常，您可以使用 [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-) 方法向表格或列表对象中添加值。但有时，您可能需要使用行和列偏移向表格或列表对象中添加值。

要从单元格中访问表格或列表对象，请使用[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--)方法。然后使用行和列的偏移量使用[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-)方法在其中添加值。

{{% /alert %}}

## 示例

### 比较源文件和输出文件的截图

以下截图显示了代码中使用的源Excel文件。它包含了空表格并突出显示了位于表格内的单元格D5。我们将使用[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--) 方法从单元格D5访问这个表格，然后使用[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue-boolean-) 和[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue-int-int-java.lang.Object-) 方法向其中添加值。

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

以下截图显示了代码生成的输出Excel文件。您可以看到单元格D5具有一个值，而位于表格偏移2,2的单元格F6也具有一个值。

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java代码，用于从单元格中访问表格并使用行和列偏移值在其中添加值

以下示例代码加载了上面截图中显示的源Excel文件，并向表格内添加值，并生成了上面所示的输出Excel文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
{{< app/cells/assistant language="java" >}}
