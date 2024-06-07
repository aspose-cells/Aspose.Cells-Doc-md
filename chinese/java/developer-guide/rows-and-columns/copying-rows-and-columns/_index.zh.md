---
title: 复制行和列
type: docs
weight: 30
url: /zh/java/copying-rows-and-columns/
---

## **介绍**
有时，您需要在工作表中复制行和列，而无需复制整个工作表。使用Aspose.Cells，可以在工作簿内部或之间复制行和列。

复制行（或列）时，其中包含的数据，包括更新后的引用、值、注释、格式、隐藏单元格、图片和其他绘图对象也会被复制。
## **使用 Microsoft Excel 复制行和列**
1. 选择要复制的行或列。
1. 要复制行或列，单击**标准**工具栏上的**复制**，或按下**CTRL**+**C**。
1. 选择要复制所选内容下方或右侧的行或列。
1. 在复制行或列时，单击**插入**菜单上的**复制的单元格**。

{{% alert color="primary" %}} 

如果您单击**标准**工具栏上的**粘贴**，或按**CTRL**+**V**，而不是在**插入**菜单上单击命令，则目标单元格的任何内容都将被替换。

{{% /alert %}} 

## **复制单行**

Aspose.Cells提供[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)类的[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\))方法。此方法从源行复制包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象在内的所有类型的数据到目标行。

[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\))方法采用以下参数：

- 源[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)对象，
- 源行索引，以及
- 目标行索引。

使用此方法将行复制到工作表中或者复制到另一个工作表中。 [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) 方法的工作方式类似于 Microsoft Excel。例如，您不需要显式设置目标行的高度，该数值也会被复制。

以下示例显示了如何在工作表中复制一行。它使用一个模板 Microsoft Excel 文件，将第二行（包括数据、格式、注释、图像等等）复制并粘贴到同一工作表的第12行。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



使用此方法在工作表内或到另一个工作表上复制行。[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\))方法的工作方式类似于Microsoft Excel。因此，例如，您不需要显式设置目标行的高度，该值也会被复制。

**执行以下代码片段后生成以下输出。** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

在复制行时，重要注意相关图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为 5，则图像、图表等会被复制，如果它们在三行中（起始行索引为 4，结束行索引为 6）。
1. 目标行中现有的图像、图表等不会被移除。

{{% /alert %}} 

## **复制多行**

**行被以最高的精度和准确度复制**

还可以在使用{0})方法时将多行复制到新目的地，该方法还接受一个整数类型的参数，用于指定要复制的源行数。

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

以下是包含3行数据的输入电子表格快照，而下面提供的代码片段将所有3行复制到从第7行开始的新位置。

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **复制单列**

执行上述代码片段后产生的电子表格视图。

Aspose.Cells提供[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)类的[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\))方法，该方法从源列复制包括包含更新后引用的公式和值、注释、单元格格式、隐藏单元格、图像和其他绘图对象在内的所有类型的数据到目标列。

- 源[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)对象，
- 源列索引，以及
- 目标列索引。

使用[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\))方法在工作表内或到另一个工作表上复制列。

此示例将工作表中的一列复制并粘贴到另一个工作簿的工作表中。

**从一个工作簿复制列到另一个工作簿** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **复制多列**

与[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)）方法类似，Aspose.Cells API 还提供[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)）方法，以便将多个源列复制到新位置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

这是在 Excel 中源和结果电子表格的外观。

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **粘贴行/列与粘贴选项**
Aspose.Cells 现在在使用 [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\)) 和 [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)) 函数时提供 [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions)。它允许设置与 Excel 类似的适当粘贴选项。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

