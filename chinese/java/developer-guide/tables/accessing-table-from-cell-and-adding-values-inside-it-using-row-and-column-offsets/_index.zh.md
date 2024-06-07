---
title: 访问表单元格并使用行和列偏移量在其中添加值
type: docs
weight: 110
url: /zh/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

通常，您使用 [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) 方法在表格或列表对象内添加值。 但有时，您可能需要使用行和列偏移在表格或列表对象内添加值。

要从单元格访问表格或列表对象，请使用 [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable()) 方法。 然后，使用 [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) 方法使用行和列偏移在其中添加值。

{{% /alert %}}

## 示例

### 比较源文件和输出文件的屏幕截图

下面的屏幕截图显示了代码中使用的源 Excel 文件。 其中包含空表，并突出显示了位于表内的单元格 D5。我们将使用 [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable()) 方法从单元格 D5 访问此表，然后使用 [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) 和 [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) 方法在其中添加值。

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

下面的截图显示了代码生成的输出Excel文件。正如您所看到的，单元格D5有一个值，表格内偏移为2,2的单元格F6也有一个值。

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### 使用行和列偏移访问表格并在其中添加值的 Java 代码

以下示例代码加载了上述截图中显示的源Excel文件，并在表内添加值，生成了如上所示的输出Excel文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
