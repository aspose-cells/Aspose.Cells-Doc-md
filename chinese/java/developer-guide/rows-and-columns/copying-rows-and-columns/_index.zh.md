---
title: 复制行和列
type: docs
weight: 30
url: /zh/java/copying-rows-and-columns/
---

## **介绍**
有时，您需要在不复制整个工作表的情况下复制工作表中的行和列。使用Aspose.Cells，可以在工作簿内部或工作簿之间复制行和列。

复制行（或列）时，其中包含的数据，包括更新的引用的公式和值，注释，格式，隐藏单元格，图像以及其他绘图对象也会被复制。
## **使用Microsoft Excel复制行和列**
1. 选择要复制的行或列。
1. 要复制行或列，请单击 **标准** 工具栏上的 **复制**，或按 **CTRL**+**C**。
1. 选择要复制所选内容下方或右侧的行或列。
1. 复制行或列时，单击 **已复制的单元格** 在 **插入** 菜单上。

{{% alert color="primary" %}} 

如果您在**标准**工具栏上单击**粘贴**，或者按**Ctrl**+**V**键，而不是在**插入**菜单上单击命令，则目标单元格的任何内容都将被替换。

{{% /alert %}} 

## **复制单行**

Aspose.Cells提供了[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) 方法，用于[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 类。 该方法将源行中的所有类型数据（包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象）复制到目标行。

[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) 方法需要以下参数：

- 源[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)对象,
- 源行索引, 和
- 目标行索引.

使用此方法在工作表内或者工作表之间复制行。 [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) 方法的工作方式与Microsoft Excel类似。 例如，您不需要显式设置目标行的高度，该值也会被复制。

以下示例显示如何在工作表中复制一行。它使用一个模板 Microsoft Excel 文件，将第二行（包括数据、格式、注释、图像等）复制并粘贴到同一工作表的第12行。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



执行下面代码后生成以下输出。

**行被以最高程度的精度和准确性复制** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

在复制行时，重要的是注意相关的图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为5，则如果它包含在三行内（起始行索引为4，结束行索引为6），则图像、图表等会被复制。
1. 目标行中现有的图像、图表等不会被移除。

{{% /alert %}} 

## **复制多行**

您还可以使用[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int))方法将多行复制到新目标位置，该方法还接受一个整数类型的额外参数，用于指定要复制的源行数。

以下是包含3行数据的输入电子表格快照，而下面提供的代码片段将所有3行复制到从第7行开始的新位置。

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

在执行上述代码片段后，以下是结果电子表格视图。

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **复制单列**

Aspose.Cells提供了[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\))方法，该方法可将源列中的所有类型数据（包括更新引用的公式和值，注释，单元格格式，隐藏单元格，图像和其他绘图对象）复制到目标列。

[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\))方法接受以下参数:

- 源[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)对象,
- 源列索引, 和
- 目标列索引.

使用[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\))方法在工作表内部或其他工作表之间复制列。

该示例将一个工作表中的列复制到另一个工作簿的工作表中。

**从一个工作簿复制列到另一个工作簿** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **复制多个列**

与[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int))方法类似，Aspose.Cells API还提供了[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int))方法，以便将多个源列复制到新位置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

以下是Excel中的源和结果电子表格的外观。

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **使用粘贴选项粘贴行/列**
Aspose.Cells现在在使用[CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\))和[CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\))函数时提供[PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions)。它允许设置类似于Excel的适当粘贴选项。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

