---
title: 创建动态图表
type: docs
weight: 240
url: /zh/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

动态（或交互式）图表能够在您更改数据范围时进行更改。换句话说，动态图表可以在数据源发生变化时自动反映变化。为了触发数据源的变化，可以使用 Excel 表格的过滤选项或使用 ComboBox 或 Dropdown 列表等控件。

本文演示了使用 Aspose.Cells for .NET API 使用上述两种方法创建动态图表。

{{% /alert %}}

## **使用 Excel 表格**

{{% alert color="primary" %}}

 Excel 表格在 Aspose.Cells 的视角中称为 ListObjects，因此，为了清楚起见，我们将使用术语“ListObject”而不是“Table”。请详细阅读如何操作[创建列表对象](/cells/zh/net/create-and-format-table/)与 Aspose.Cells for .NET API。

{{% /alert %}}

ListObjects 提供了内置功能，可根据用户交互对数据进行排序和过滤。排序和过滤选项都是通过下拉列表提供的，这些列表会自动添加到标题行[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).由于这些功能（排序和过滤），[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)似乎是充当动态图表数据源的完美候选者，因为当排序或过滤发生变化时，图表中数据的表示将发生变化以反映当前状态[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

为了使演示简单易懂，我们将创建[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)从头开始，然后按照下面的概述逐步前进。

1. 创建一个空[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 访问[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)第一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)在里面[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 向单元格中插入一些数据。
1. 创造[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)基于插入的数据。
1. 创造[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)基于的数据范围[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. 将结果保存在光盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **使用动态公式**

如果您不想使用[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)作为动态图表的数据源，另一种选择是使用 Excel 函数（或公式）创建动态范围的数据，并使用控件（如 ComboBox）来触发数据的变化。在这种情况下，我们将使用 VLOOKUP 函数根据 ComboBox 的选择获取适当的值。选择更改时，VLOOKUP 函数将刷新单元格值。如果单元格范围使用 VLOOKUP 函数，整个范围可以在用户交互时刷新，因此它可以用作动态图表的来源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按如下所述逐步进行。

1. 创建一个空[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 访问[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)第一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)在里面[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 通过创建命名范围向单元格插入一些数据。此数据将用作动态图表的系列。
1. 创造[**组合框**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)基于在上一步中创建的命名范围。
1. 将更多数据插入将用作 VLOOKUP 函数源的单元格。
1. 将 VLOOKUP 函数（使用适当的参数）插入到一系列单元格中。这个范围将作为动态图表的来源。
1. 创造[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)基于在上一步中创建的范围。
1. 将结果保存在光盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
