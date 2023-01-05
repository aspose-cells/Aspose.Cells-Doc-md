---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel 提供了一个很好的功能，可以根据内容自动调整单元格的宽度和高度。此功能也可供 Aspose.Cells 用户使用，具有在运行时自动调整单元格尺寸的能力。

{{% /alert %}} 
## **汽车配件**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了广泛的属性和方法来管理工作表。本文着眼于使用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)自动调整行或列的类。
### **自动调整行 - 简单**
自动调整行的宽度和高度的最直接的方法是调用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级'[自动调整行](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)） 方法。这[自动调整行](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)方法将（要调整大小的行的）行索引作为参数。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Cells 范围内的 AutoFit 行**
一行由许多列组成。 Aspose.Cells 允许开发人员通过调用[自动调整行](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)） 方法。它采用以下参数：

- **行索引**，即将被自动调整的行的索引。
- **第一列索引**，该行第一列的索引。
- **最后一列索引**，该行最后一列的索引。

这[自动调整行](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) 方法检查行中所有列的内容，然后自动调整行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **自动调整列 - 简单**
自动调整列的宽度和高度的最简单方法是调用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级'[自动调整列](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)） 方法。这[自动调整列](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)方法将（即将调整大小的列的）列索引作为参数。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Cells 范围内的 AutoFit 列**
一列由许多行组成。通过调用重载版本，可以根据列中单元格范围内的内容自动调整列[自动调整列](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)采用以下参数的方法：

- **列索引**代表内容需要自动适应的列的索引
- **第一行索引**代表该列第一行的索引
- **最后一行索引**代表该列最后一行的索引

这[自动调整列](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)方法检查列中所有行的内容，然后自动调整列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **合并的 AutoFit 行 Cells**
使用 Aspose.Cells，即使对于已使用合并的单元格，也可以自动调整行[AutoFitter选项](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitter选项](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)类提供[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)可用于自动调整合并单元格行的属性。[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)接受[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)具有以下成员的可枚举。

- [没有任何](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE)：忽略合并的单元格。
- [第一行](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE)：只扩展第一行的高度。
- [最后一行](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE)：只扩展最后一行的高度。
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE)：只扩展每行的高度。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

您也可以使用的重载版本[自动调整行](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [自动调整列](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) 方法接受一系列的行/列和一个实例[AutoFitter选项](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)使用所需的自动调整选定的行/列[AutoFitter选项](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)因此。

上述方法的签名如下：

1.  autoFitRows（int startRow，int endRow，[AutoFitter选项](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)选项）
1.  autoFitColumns（int firstColumn，int lastColumn，[AutoFitter选项](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)选项）
## **重要须知**
{{% alert color="primary" %}} 

如果合并单元格，则*自动调整*将不会应用方法，这与 Microsoft Excel 中的行为相同。此外，如果单元格中的文本被换行，[自动调整列](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) 方法也不会被应用。您需要知道的另一件事是*自动调整*方法很费时间。因此，您应该尽可能少地调用这些方法，以确保您的应用程序的效率。

{{% /alert %}}
