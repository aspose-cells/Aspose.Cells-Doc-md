---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/python-net/autofit-rows-and-columns/
description: 本文展示如何自动调整行、列、合并单元格的行和单元格范围内的行，通过Aspose.Cells for Python via .NET API实现。
keywords: Python Excel库，Python自动调整行，Python自动调整列，Python自动调整单元格范围内的行，Python自动调整合并单元格的行。
---

{{% alert color="primary" %}}

Microsoft Excel允许用户根据内容自动调整单元格的宽度和高度。通过Aspose.Cells for Python via .NET，开发人员也可以在运行时自动调整单元格的尺寸。

{{% /alert %}}

## **自动调整**

Aspose.Cells for Python via .NET提供了一个表示Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了广泛的属性和方法，用于管理工作表。本文讨论了使用[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类来自动调整行或列。

### **自动调整行 - 简单**

自动调整行宽度和高度最直接的方法是调用 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) 方法。[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) 方法以要调整行的索引作为参数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **如何在单元格范围内自动调整行**

一行由多个列组成。Aspose.Cells for Python via .NET允许开发人员通过调用[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int)方法的重载版本来根据行内单元格范围内容自动调整行。它接受以下参数：

- **行索引**，即要自动调整的行的索引。
- **第一个列索引**，即行的第一个列的索引。
- **最后列索引**，指行的最后一列的索引。

[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) 方法检查行中所有列的内容，然后自动调整行。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **如何在一系列单元格中自动调整列**

一列由许多行组成。通过调用重载版本的[**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) 方法，可以根据列中单元格范围中的内容自动调整列，该方法接受以下参数：

- **列索引**，要自动调整的列的索引。
- **第一行索引**，列的第一行的索引。
- **最后行索引**，列的最后一行的索引。

[**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) 方法检查列中所有行的内容，然后自动调整列。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **如何为合并单元格自动调整行高**

使用 Aspose.Cells for Python via .NET 可以自动调整合并单元格的行高，甚至对使用 [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) API 进行合并的单元格也可以。[**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions)类提供了[**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/)属性，可用于自动调整合并单元格的行高。[**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/)接受[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype)枚举，其包含以下成员。

- NONE: 忽略合并单元格。
- FIRST_LINE: 仅扩展第一行的高度。
- LAST_LINE: 仅扩展最后一行的高度。
- EACH_LINE: 仅扩展每行的高度。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

您还可以尝试使用重载版本的[**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) 和[**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions) 方法，这些方法接受一系列行/列和[**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions)实例，以根据您的要求自动调整所选行/列。[**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions)。

上述方法的签名如下：

1. auto_fit_rows(start_row, end_row, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) 选项)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **重要知识**

{{% alert color="primary" %}}

如果单元格已合并，则不会应用AutoFit方法，这与Microsoft Excel的行为相同。您可以通过使用自动筛选API来解决此问题。此外，如果单元格中的文本换行，则也不会应用[**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) 方法。您还需要知道的另一件事是，自动调整方法需要很长时间。因此，为了确保应用程序的效率，应该尽可能少地调用这些方法。

{{% /alert %}}

## **高级主题**
- [为合并单元格自动调整行高](/cells/zh/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
