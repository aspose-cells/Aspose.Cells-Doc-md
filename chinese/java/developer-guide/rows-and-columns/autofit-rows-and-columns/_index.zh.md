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
调整行的宽度和高度最直接的方法是调用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类的[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\))方法。[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\))方法将行索引（要调整大小的行）作为参数。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **在单元格范围内自动调整行**
一行由许多列组成。Aspose.Cells允许开发人员根据行内单元格范围中的内容自动调整行的大小，通过调用[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\))方法的重载版本。它接受以下参数：

- **行索引**，即要自动调整的行的索引。
- **第一个列索引**，即行的第一个列的索引。
- **最后列索引**，指行的最后一列的索引。

[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\))方法检查行中所有列的内容，然后自动调整行的大小。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **自动调整列 - 简单**
调整列宽度和高度最简单的方法是调用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类的[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\))方法。[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\))方法将列索引（要调整大小的列）作为参数。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **自动调整单元格范围中的列宽**
一列由许多行组成。可以调用 [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) 的重载版本方法，根据列中单元格范围的内容自动调整列的宽度，该方法接受以下参数:

- **列索引**，表示需要自动调整内容的列的索引
- **第一行索引**，表示列的第一行的索引
- **最后一行索引**，表示列的最后一行的索引

[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) 方法检查列中所有行的内容，然后自动调整列的宽度。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **为合并单元格自动调整行高**
使用 Aspose.Cells，甚至可以对已经合并的单元格进行行的自动调整，使用 [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API。[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) 类提供 [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) 属性，可以用于合并单元格的自动调整行。[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) 接受 [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) 枚举，其包括以下成员。

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): 忽略已合并的单元格。
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): 只扩展第一行的高度。
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): 只扩展最后一行的高度。
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): 只扩展每行的高度。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

您也可以使用 [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) 和 [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)) 方法的重载版本，接受一系列行/列和 [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) 的实例，根据所需的 [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) 自动调整所选行/列。

上述方法的签名如下:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **重要知识**
{{% alert color="primary" %}} 

如果单元格已合并，则不会应用 *自动调整* 方法，这与 Microsoft Excel 中的行为相同。此外，如果单元格中的文本已换行，则 [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) 方法也不会应用。您还需要知道的一件事是，*自动调整* 方法会耗费时间。因此，您应该尽可能少地调用这些方法，以确保应用程序的效率。

{{% /alert %}}
