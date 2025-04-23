---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/net/autofit-rows-and-columns/
description: 本文章展示了如何通过 Aspose.Cells for .NET API 自动调整行、列、合并单元格的行和单元格范围。
keywords: 自动调整行，自动调整列，自动调整单元格范围中的行，自动调整合并单元格中的行
---

{{% alert color="primary" %}}

Microsoft Excel 允许用户根据内容自动调整单元格宽度和高度。Aspose.Cells 也提供了这一功能，因此开发人员可以在运行时自动调整单元格的尺寸。

{{% /alert %}}

## **自动调整**

Aspose.Cells 提供了一个 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类，表示 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了一系列属性和方法，用于管理工作表。本文探讨了使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类自动调整行或列。

### **自动调整行 - 简单**

自动调整行宽度和高度最直接的方法是调用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) 方法。[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) 方法以要调整行的索引作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **如何在单元格范围内自动调整行**

一行由许多列组成。Aspose.Cells 允许开发人员调用 [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) 方法的重载版本，根据行内单元格范围中的内容自动调整行。它接受以下参数：

- **行索引**，即要自动调整的行的索引。
- **第一个列索引**，即行的第一个列的索引。
- **最后列索引**，指行的最后一列的索引。

[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) 方法检查行中所有列的内容，然后自动调整行。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **如何在一系列单元格中自动调整列**

一列由许多行组成。通过调用重载版本的[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) 方法，可以根据列中单元格范围中的内容自动调整列，该方法接受以下参数：

- **列索引**，要自动调整的列的索引。
- **第一行索引**，列的第一行的索引。
- **最后行索引**，列的最后一行的索引。

[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) 方法检查列中所有行的内容，然后自动调整列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **如何为合并单元格自动调整行高**

使用Aspose.Cells，甚至可以为已合并的单元格自动调整行高，使用[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API。[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) 类提供了[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)属性，可用于为合并单元格自动调整行高。 [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) 接受[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype)枚举，其中包括以下成员。

- 无：忽略合并单元格。
- 第一行：仅展开第一行的高度。
- 最后一行：仅展开最后一行的高度。
- 每行：仅展开每行的高度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

您还可以尝试使用重载版本的[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) 和[**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) 方法，这些方法接受一系列行/列和[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)实例，以根据您的要求自动调整所选行/列。[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)。

上述方法的签名如下：

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) 选项)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) 选项)

{{% /alert %}}

## **重要知识**

{{% alert color="primary" %}}

如果单元格已合并，则不会应用AutoFit方法，这与Microsoft Excel的行为相同。您可以通过使用自动筛选API来解决此问题。此外，如果单元格中的文本换行，则也不会应用[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) 方法。您还需要知道的另一件事是，自动调整方法需要很长时间。因此，为了确保应用程序的效率，应该尽可能少地调用这些方法。

{{% /alert %}}

## **高级主题**
- [为合并单元格自动调整行高](/cells/zh/net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="csharp" >}}
