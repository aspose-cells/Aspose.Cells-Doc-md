---
title: 复制行和列
type: docs
weight: 30
url: /zh/java/copying-rows-and-columns/
---
## **介绍**
有时，您需要复制工作表中的行和列而不复制整个工作表。使用 Aspose.Cells，可以在工作簿内或工作簿之间复制行和列。

复制行（或列）时，其中包含的数据，包括公式（具有更新的引用）和值、注释、格式、隐藏的单元格、图像和其他绘图对象也会被复制。
## **使用 Microsoft Excel 复制行和列**
1. 选择要复制的行或列。
1. 要复制行或列，请单击**复制**在**标准**工具栏，或按**CTRL键**+**C**。
1. 选择要复制选择的位置下方或右侧的行或列。
1. 复制行或列时，单击**已复制 Cells**在**插入**菜单。

{{% alert color="primary" %}} 

如果你点击**粘贴**在**标准**工具栏或按**CTRL键**+**V** 而不是单击命令**Insert** 菜单，目标单元格的任何内容都被替换。

{{% /alert %}} 

## **复制单行**

Aspose.Cells 提供了[复制行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)班级。此方法将所有类型的数据（包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象）从源行复制到目标行。

这[复制行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)方法采用以下参数：

- 来源[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)目的，
- 源行索引，和
- 目标行索引。

使用此方法复制工作表中的一行，或复制到另一个工作表。这[复制行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)方法的工作方式与 Microsoft Excel 类似。因此，例如，您不需要明确设置目标行的高度，该值也会被复制。

下面的示例演示如何复制工作表中的一行。它使用模板 Microsoft Excel 文件并复制第二行（包含数据、格式、注释、图像等）并将其粘贴到同一工作表中的第 12 行。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



执行以下代码时会生成以下输出。

**该行以最高的精度和准确度复制** 

![待办事项：图片_替代_文本](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

复制行时，重要的是要注意相关的图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：

1. 如果源行索引为 5，则如果图像、图表等包含在三行中（起始行索引为 4，结束行索引为 6），则复制该图像、图表等。
1. 目标行中的现有图像、图表等不会被删除。

{{% /alert %}} 

## **复制多行**

您还可以在使用[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)方法，它采用整数类型的附加参数来指定要复制的源行数。

下面是包含 3 行数据的输入电子表格的快照，而下面提供的代码片段将所有 3 行复制到从第 7 行开始的新位置。

![待办事项：图片_替代_文本](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

这是执行上述代码片段后生成的电子表格视图。

![待办事项：图片_替代_文本](copy-rows-and-columns_4.png)

## **复制单列**

Aspose.Cells 提供了[复制列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)类，此方法将所有类型的数据，包括公式（具有更新的引用）和值、注释、单元格格式、隐藏单元格、图像和其他绘图对象从源列复制到目标列。

这[复制列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)方法采用以下参数：

- 来源[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)目的，
- 源列索引，和
- 目标列索引。

使用[复制列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) 方法复制工作表中的列或复制到另一个工作表。

本示例从工作表复制一列并将其粘贴到另一个工作簿的工作表中。

**列从一个工作簿复制到另一个工作簿** 

![待办事项：图片_替代_文本](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **复制多列**

如同[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) 方法，Aspose.Cells API 还提供[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)方法以便将多个源列复制到新位置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

以下是源电子表格和生成的电子表格在 Excel 中的外观。

![待办事项：图片_替代_文本](copy-rows-and-columns_7.png)

![待办事项：图片_替代_文本](copy-rows-and-columns_8.png)


## **使用粘贴选项粘贴行/列**
Aspose.Cells现在提供[粘贴选项](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions)在使用功能时[复制行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ） 和[复制列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)).它允许设置类似于 Excel 的适当粘贴选项。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

