---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Excel 允许用户根据其内容自动调整单元格的宽度和高度。此功能也可通过 Aspose.Cells 获得，因此开发人员可以在运行时自动调整单元格的尺寸。

{{% /alert %}}

## **汽车配件**

Aspose.Cells提供了[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。本文着眼于使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)自动调整行或列的类。

### **自动调整行 - 简单**

自动调整行的宽度和高度的最直接的方法是调用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)方法。这[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)方法将（要调整大小的行的）行索引作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Cells 范围内的 AutoFit 行**

一行由许多列组成。 Aspose.Cells 允许开发人员通过调用[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)方法。它采用以下参数：

- **行索引**，即将被自动调整的行的索引。
- **第一列索引**，该行第一列的索引。
- **最后一列索引**，该行最后一列的索引。

这[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)方法检查行中所有列的内容，然后自动调整行。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Cells 范围内的 AutoFit 列**

一列由许多行组成。通过调用重载版本，可以根据列中单元格范围内的内容自动调整列[**自动调整列**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)采用以下参数的方法：

- **列索引**即将被自动拟合的列的索引。
- **第一行索引**，列第一行的索引。
- **最后一行索引**，列最后一行的索引。

这[**自动调整列**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)方法检查列中所有行的内容，然后自动调整列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **合并的 AutoFit 行 Cells**

使用 Aspose.Cells，即使对于已使用合并的单元格，也可以自动调整行[**AutoFitter选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitter选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)类提供[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)可用于自动调整合并单元格行的属性。[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)接受[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype)具有以下成员的可枚举。

- 无：忽略合并的单元格。
- FirstLine：只扩展第一行的高度。
- LastLine：只扩展最后一行的高度。
- eachLine：只扩展每一行的高度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

您也可以尝试使用的重载版本[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**自动调整列**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns)接受一系列行/列的方法和一个实例[**AutoFitter选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)根据您的需要自动调整选定的行/列[**AutoFitter选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)因此。

上述方法的签名如下：

1.  AutoFitRows（int startRow，int endRow，[**AutoFitter选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)选项）
1. AutoFitColumns（int firstColumn，int lastColumn，[**AutoFitter选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)选项）

{{% /alert %}}

## **重要须知**

{{% alert color="primary" %}}

如果合并单元格，则不会应用 AutoFit 方法，这与 Microsoft Excel 中的行为相同。您可以使用自动过滤器 API 来解决这个问题。此外，如果单元格中的文本被换行，则[**自动调整列**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)方法也不会被应用。您需要知道的另一件事是*自动调整*方法很费时间。因此，您应该尽可能少地调用这些方法，以确保您的应用程序的效率。

{{% /alert %}}

## **推进主题**
- [合并的 AutoFit 行 Cells](/cells/zh/net/autofit-rows-for-merged-cells/)
