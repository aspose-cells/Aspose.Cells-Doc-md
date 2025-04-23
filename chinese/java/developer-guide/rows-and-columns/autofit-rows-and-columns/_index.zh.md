---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel提供了一个很好的功能，根据内容自动调整单元格的宽度和高度。Aspose.Cells用户也可以通过在运行时自动调整单元格的尺寸来使用这个功能。

{{% /alert %}} 
## **自动调整**
Aspose.Cells提供了一个表示Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了广泛的属性和方法来管理工作表。本文介绍如何使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类来自动调整行或列。
### **自动调整行 - 简单**
自动调整行宽和高度的最简单方法是调用 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类的 [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) 方法。该方法接受要调整的行的索引作为参数。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **在单元格范围内自动调整行**
一行由许多列组成。Aspose.Cells 允许开发人员通过调用 [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) 重载方法，根据行内单元格内容自动调整行高。它接受以下参数：

- **行索引**，即要自动调整的行的索引。
- **第一个列索引**，即行的第一个列的索引。
- **最后列索引**，指行的最后一列的索引。

 [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) 方法会检查行中所有列的内容，然后自动适应行高。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **自动调整列 - 简单**
自动调整列宽和高度的最简单方法是调用 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类的 [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) 方法。该方法接受要调整的列的索引作为参数。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **自动调整单元格范围中的列宽**
一列由许多行组成。可以通过调用 [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) 的重载版本，根据列中单元格内容自动调整列宽，该方法接受以下参数：

- **列索引**，表示需要自动调整内容的列的索引
- **第一行索引**，表示列的第一行的索引
- **最后一行索引**，表示列的最后一行的索引

 [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) 方法会检查列中所有行的内容，然后自动调整列宽。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **为合并单元格自动调整行高**
使用 Aspose.Cells，甚至可以对已经合并的单元格进行行的自动调整，使用 [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API。[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) 类提供 [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) 属性，可以用于合并单元格的自动调整行。[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) 接受 [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) 枚举，其包括以下成员。

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): 忽略已合并的单元格。
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE)：只扩展第一行的高度。
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE)：只扩展最后一行的高度。
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE)：只扩展每一行的高度。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

您还可以使用重载的 [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--) 和 [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--) 方法，接受行／列范围和 [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) 实例，以自动适应所选行/列的 [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)。

上述方法的签名如下:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **重要知识**
{{% alert color="primary" %}} 

如果单元格被合并，则*AutoFit* 方法将不会应用，这与微软 Excel 中的行为相同。此外，如果单元格中的文本被换行，[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) 方法也不会被应用。你还需要知道的是，*AutoFit* 方法耗时较长，因此，应尽可能少调用这些方法，以确保应用程序的效率。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
