---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/net/autofit-rows-and-columns/
description: 本文介绍了如何使用Aspose.Cells for .NET API自动调整行、列、合并单元格的行和单元格范围中的行。
keywords: 自动调整行、自动调整列、自动调整单元格范围中的行、自动调整合并单元格的行
---

{{% alert color="primary" %}}

Microsoft Excel允许用户根据内容自动调整单元格的宽度和高度。Aspose.Cells API也提供此功能，因此开发人员可以在运行时自动调整单元格的维度。

{{% /alert %}}

## **自动适应**

Aspose.Cells 提供了 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类，代表Microsoft Excel文件。该 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问Excel文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了用于管理工作表的各种属性和方法。本文将介绍如何使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类调整行或列。

### **自动调整行 - 简单**

自动调整行宽度和高度的最简单方法是调用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) 方法。 [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) 方法将行索引（要调整大小的行的索引）作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **如何在单元格范围内自动调整行**

一行由许多列组成。Aspose.Cells允许开发人员基于行内单元格范围的内容自动调整行大小，通过调用 [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) 方法的重载版本实现。它接受以下参数：

- **行索引**，要自动调整大小的行的索引。
- **第一列索引**，行的第一列的索引。
- **最后一列索引**，行的最后一列的索引。

 [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) 方法检查行中所有列的内容，然后自动调整行。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **如何在单元格范围内自动调整列**

一列由许多行组成。可以根据列中单元格范围的内容自动调整列大小，通过调用 [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) 方法的重载版本实现，它接受以下参数：

- **列索引**，要自动调整大小的列的索引。
- **第一行索引**，列的第一行的索引。
- **最后一行索引**，列的最后一行的索引。

[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)方法检查列中所有行的内容，然后自动调整列宽。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **如何自动调整合并单元格的行高**

使用Aspose.Cells可以对已合并的单元格自动调整行高，使用[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API。[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)类提供[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)属性，用于对已合并单元格自动调整行高。[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)接受[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype)可枚举，其中包含以下成员。

- None: 忽略合并单元格。
- FirstLine: 仅扩展第一行的高度。
- LastLine: 仅扩展最后一行的高度。
- EachLine: 仅扩展每行的高度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

您也可以尝试使用接受一系列行/列范围和[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)实例的重载版本的[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows)和[**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns)方法，根据您的需要自动调整所选行/列的行高/列宽。

上述方法的签名如下：

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) 选项)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) 选项)

{{% /alert %}}

## **重要知识**

{{% alert color="primary" %}}

如果单元格已合并，则不会应用AutoFit方法，这与Microsoft Excel中的行为相同。您可以通过使用自动筛选API来解决此问题。此外，如果单元格中的文本换行，则也不会应用[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)方法。另一件事情是需要知道*AutoFit*方法是耗时的。因此，为确保应用程序的效率，应尽量少调用这些方法。

{{% /alert %}}

## **高级主题**
- [自动调整合并单元格的行高](/cells/zh/net/autofit-rows-for-merged-cells/)
