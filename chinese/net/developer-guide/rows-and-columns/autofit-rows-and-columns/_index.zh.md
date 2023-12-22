---
title: 自动调整行和列
type: docs
weight: 20
url: /zh/net/autofit-rows-and-columns/
description: 本文介绍如何自动调整行、列、合并单元格的行以及按 Aspose.Cells for .NET API 排列的单元格区域中的行。
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft Excel 允许用户根据单元格的内容自动调整单元格的宽度和高度。此功能还可通过 Aspose.Cells 获得，因此开发人员可以在运行时自动调整单元格的尺寸。

{{% /alert %}}

##  **汽车配件**

Aspose.Cells 提供[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了多种用于管理工作表的属性和方法。本文着眼于使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类自动调整行或列。

###  **自动调整行 - 简单**

自动调整行的宽度和高度的最直接方法是调用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)方法。这[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)方法采用行索引（要调整大小的行的索引）作为参数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **如何在 Cells 范围内自动调整行**

行由许多列组成。 Aspose.Cells 允许开发人员通过调用重载版本来根据行内一系列单元格中的内容自动调整行[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)方法。它需要以下参数：

- *行索引**，即将自动拟合的行的索引。
- *第一列索引**，行第一列的索引。
- *最后一列索引**，该行最后一列的索引。

这[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)方法检查该行中所有列的内容，然后自动调整该行。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **如何在 Cells 范围内自动调整列**

一列由许多行组成。通过调用重载版本，可以根据列中一系列单元格中的内容自动调整列[**自动调整列**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)方法采用以下参数：

- *列索引**，即将自动拟合的列的索引。
- *首行索引**，列第一行的索引。
- *最后一行索引**，该列最后一行的索引。

这[**自动调整列**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)方法检查列中所有行的内容，然后自动调整列。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **如何自动调整行以进行合并 Cells**

使用 Aspose.Cells，即使对于已使用 合并的单元格也可以自动调整行[**自动调整选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**自动调整选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)类提供[**自动调整合并单元格类型**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)属性可用于自动调整合并单元格的行。[**自动调整合并单元格类型**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)接受[**自动调整合并单元格类型**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype)具有以下成员的可枚举。

- 无：忽略合并的单元格。
- FirstLine：仅扩展第一行的高度。
- LastLine：仅扩展最后一行的高度。
- EachLine：仅扩展每行的高度。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

您也可以尝试使用重载版本[**自动调整行**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**自动调整列**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns)接受一系列行/列和实例的方法[**自动调整选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)根据您的需要自动调整选定的行/列[**自动调整选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)因此。

上述方法的签名如下：

1.  AutoFitRows(int startRow, int endRow,[**自动调整选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)选项）
1.  AutoFitColumns(intfirstColumn, intlastColumn,[**自动调整选项**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)选项）

{{% /alert %}}

##  **重要了解**

{{% alert color="primary" %}}

如果合并单元格，则不会应用自动调整方法，这与 Microsoft Excel 中的行为相同。您可以使用自动过滤器 API 来解决这个问题。此外，如果单元格中的文本被换行，则[**自动调整列**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)方法也不会被应用。您需要知道的另一件事是*自动调整*方法很耗时。因此，您应该尽可能少地调用这些方法，以确保应用程序的效率。

{{% /alert %}}

##  **高级主题**
- [用于合并的自动调整行 Cells](/cells/zh/net/autofit-rows-for-merged-cells/)
