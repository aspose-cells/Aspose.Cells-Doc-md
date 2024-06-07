---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel提供了一个良好的功能，根据其内容自动调整单元格的宽度和高度。Aspose.Cells用户也可以借助动态调整单元格尺寸的功能，实现单元格尺寸的自动调整。

{{% /alert %}} 
## **自动适应**
Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个允许访问Excel文件中每个工作表的[Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)集合。

工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了用于管理工作表的宽泛属性和方法。本文介绍了如何使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类自动调整行或列。
### **自动调整行 - 简单**
自动调整行和列的最直接方法是调用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类的[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\))方法。[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\))方法将行索引（要调整大小的行的索引）作为参数。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **在单元格范围内自动调整行高**
一行由许多列组成。Aspose.Cells允许开发人员根据行内的一组单元格内的内容自动调整行的大小。方法是调用[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\))方法中的一个重载版本。它采用以下参数：

- **行索引**，要自动调整大小的行的索引。
- **第一列索引**，行的第一列的索引。
- **最后一列索引**，行的最后一列的索引。

[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\))方法检查行中所有列的内容然后自动调整行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **简单的自动调整列**
自动调整列宽度和高度的最简单方法是调用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类的[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\))方法。[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\))方法将列索引（将调整大小的列的索引）作为参数。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **在一组单元格中自动调整列的大小**
一列由许多行组成。可以根据列中一组单元格的内容自动调整列的大小。方法是调用[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\))方法的重载版本。它采用以下参数：

- **列索引**，表示需要自动调整其内容的列的索引
- **第一行索引**，表示列的第一行的索引
- **最后一行索引**，表示列的最后一行的索引

[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\))方法检查列中所有行的内容，然后自动调整列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **自动调整合并单元格的行高**
使用Aspose.Cells，即使使用[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API对已合并的单元格进行了自适应，也可以自适应行。[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)类提供了[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)属性，可用于合并单元格的自适应行。[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)接受[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)枚举，具有以下成员。

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE)：忽略合并单元格。
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE)：仅展开第一行的高度。
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE)：仅展开最后一行的高度。
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE)：仅展开每行的高度。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

您还可以使用[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\))和[autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\))方法的重载版本，接受一个范围的行/列和[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)实例，根据需要的[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)自动调整所选行/列。

上述方法的签名如下:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **重要知识**
{{% alert color="primary" %}} 

如果单元格已合并，则*AutoFit*方法不会应用，这与Microsoft Excel的行为相同。此外，如果单元格中的文本已换行，则[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\))方法也不会应用。您还需要知道的是*AutoFit*方法耗时。因此，为了确保应用程序的效率，应尽可能少地调用这些方法。

{{% /alert %}}
