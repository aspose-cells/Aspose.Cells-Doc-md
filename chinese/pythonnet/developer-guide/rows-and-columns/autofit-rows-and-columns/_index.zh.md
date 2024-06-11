---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/python-net/autofit-rows-and-columns/
description: 本文介绍了如何利用 Aspose.Cells for Python 通过 .NET API 自动调整行、列、合并单元格的行和一系列单元格的宽度。
keywords: Python Excel库，Python自动调整行、Python自动调整列、Python自动调整一系列单元格的行、Python自动调整合并单元格的行。
---

{{% alert color="primary" %}}

Microsoft Excel允许用户根据内容自动调整单元格的宽度和高度。通过 Aspose.Cells for Python 通过 .NET 也可以通过此功能调整单元格在运行时的维度。

{{% /alert %}}

## **自动适应**

Aspose.Cells for Python 通过 .NET 提供了一个表示Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)集合，允许访问Excel文件中的每个工作表。 工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了一系列属性和方法来管理工作表。本文介绍了如何使用[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类来自动调整行或列。

### **自动调整行 - 简单**

自动调整行宽度和高度的最简单方法是调用 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类的 [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) 方法。 [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) 方法将行索引（要调整大小的行的索引）作为参数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **如何在单元格范围内自动调整行**

一行由许多列组成。Aspose.Cells for Python 通过 .NET 允许开发人员根据行内的一系列单元格中的内容自动调整行大小，方法是调用[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int)方法的重载版本。它接受以下参数：

- **行索引**，要自动调整大小的行的索引。
- **第一列索引**，行的第一列的索引。
- **最后一列索引**，行的最后一列的索引。

 [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) 方法检查行中所有列的内容，然后自动调整行。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **如何在单元格范围内自动调整列**

一列由许多行组成。可以根据列中单元格范围的内容自动调整列大小，通过调用 [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) 方法的重载版本实现，它接受以下参数：

- **列索引**，要自动调整大小的列的索引。
- **第一行索引**，列的第一行的索引。
- **最后一行索引**，列的最后一行的索引。

[**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int)方法检查列中所有行的内容，然后自动调整列宽。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **如何自动调整合并单元格的行高**

通过 Aspose.Cells for Python 通过 .NET，甚至可以对使用[**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) API合并的单元格进行自动调整行的操作。[**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions)类提供了一个可用于合并单元格的自动拟合行的属性。 [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/)接受[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype)枚举，该枚举具有以下成员。

- NONE：忽略合并的单元格。
- FIRST_LINE：仅展开第一行的高度。
- LAST_LINE：仅展开最后一行的高度。
- EACH_LINE：仅展开每一行的高度。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

您也可以尝试使用接受一系列行/列范围和[**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions)实例的重载版本的[**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions)和[**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions)方法，根据您的需要自动调整所选行/列的行高/列宽。

上述方法的签名如下：

1. 自动调整行高（起始行，结束行，[**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) 选项）
1. 自动调整列宽（第一列，最后一列，[**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions)）

{{% /alert %}}

## **重要知识**

{{% alert color="primary" %}}

如果单元格已合并，则不会应用AutoFit方法，这与Microsoft Excel中的行为相同。您可以通过使用自动筛选API来解决此问题。此外，如果单元格中的文本换行，则也不会应用[**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int)方法。另一件事情是需要知道*AutoFit*方法是耗时的。因此，为确保应用程序的效率，应尽量少调用这些方法。

{{% /alert %}}

## **高级主题**
- [自动调整合并单元格的行高](/cells/zh/python-net/autofit-rows-for-merged-cells/)
