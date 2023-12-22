---
title: 创建动态图表
description: 了解如何在 Aspose.Cells for .NET 中创建动态图表。我们的指南将向您展示如何根据您的要求动态更新图表数据、系列和格式，使您能够在工作表中直观地呈现不断变化的数据。
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /zh/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

当您更改数据范围时，动态（或交互式）图表能够发生变化。换句话说，当数据源发生变化时，动态图表可以自动反映变化。为了触发数据源的更改，可以使用Excel表格的过滤选项或使用ComboBox或Dropdown列表等控件。

本文演示了如何使用 Aspose.Cells for .NET API 使用上述两种方法创建动态图表。

{{% /alert %}}

##  **使用 Excel 表格**

{{% alert color="primary" %}}

从 Aspose.Cells 的角度来看，Excel 表格被称为 ListObjects，因此，为了清楚起见，我们将使用术语“ListObject”而不是“Table”。请详细阅读如何[创建列表对象](/cells/zh/net/create-and-format-table/)与 Aspose.Cells for .NET API。

{{% /alert %}}

 ListObjects 提供内置功能，可根据用户交互对数据进行排序和过滤。排序和过滤选项都是通过下拉列表提供的，这些列表会自动添加到标题行中[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)。由于这些功能（排序和过滤），[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)似乎是用作动态图表数据源的完美候选者，因为当排序或过滤发生变化时，图表中数据的表示将发生变化以反映动态图表的当前状态[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

为了使演示简单易懂，我们将创建[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)从头开始并逐步向前推进，如下所述。

1. 创建一个空的[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 访问[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)第一个的[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)在里面[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 向单元格中插入一些数据。
1. 创造[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)基于插入的数据。
1. 创造[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)基于数据范围[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. 将结果保存在光盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **使用动态公式**

如果您不想使用[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)作为动态图表的数据源，另一种选择是使用Excel函数（或公式）创建动态范围的数据，并使用控件（例如ComboBox）来触发数据的变化。在这种情况下，我们将使用 VLOOKUP 函数根据 ComboBox 的选择来获取适当的值。当选择更改时，VLOOKUP 函数将刷新单元格值。如果一系列单元格使用VLOOKUP函数，则整个范围可以在用户交互时刷新，因此它可以用作动态图表的源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按如下所述逐步推进。

1. 创建一个空的[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 访问[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)第一个的[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)在里面[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. 通过创建命名范围将一些数据插入到单元格中。该数据将作为动态图表的系列。
1. 创造[**组合框**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)基于上一步中创建的命名范围。
1. 将更多数据插入到将用作 VLOOKUP 函数源的单元格中。
1. 将 VLOOKUP 函数（带有适当的参数）插入单元格区域。该范围将作为动态图表的来源。
1. 创造[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)基于上一步中创建的范围。
1. 将结果保存在光盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
