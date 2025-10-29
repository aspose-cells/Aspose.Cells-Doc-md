---
title: 创建动态图表
description: 学习如何在Aspose.Cells for Python via .NET中创建动态图表。我们的指南将向您展示如何根据需求动态更新图表的数据、系列和格式，让您可以在工作表中直观呈现变化的数据。
keywords: Aspose.Cells for Python via .NET，制图，动态图表，数据，系列，格式，工作表，更新。
type: docs
weight: 240
url: /zh/python-net/create-dynamic-charts/
---

{{% alert color="primary" %}}

动态（或交互式）图表在更改数据范围时具有更改的能力。换句话说，当数据源更改时，动态图表可以自动反映更改。为了触发数据源的更改，可以使用Excel表的筛选选项，或者使用控件如下拉列表或下拉菜单。

本文演示了如何使用Aspose.Cells for Python via .NET的API，通过上述两种方法创建动态图表。

{{% /alert %}}

## **使用Excel表**

{{% alert color="primary" %}}

在Aspose.Cells视角中，Excel表格被称为ListObjects，因此，为了清晰起见，我们将使用“ListObject”一词代替“表”。请详细了解如何使用Aspose.Cells for Python via .NET API[创建并格式化表格](/cells/zh/python-net/create-and-format-table/)。

{{% /alert %}}

ListObjects提供了以内置功能进行排序和筛选数据的能力。排序和筛选选项都通过自动添加到表头行的下拉列表提供。由于这些功能（排序和筛选），[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)似乎是充当动态图表数据源的理想候选，因为当排序或筛选改变时，图表中的数据表现也将反映当前状态。

为了使演示简单易懂，我们将从头开始创建[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，并按照下面概述的步骤逐步进行。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。
1. 访问[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)中第一个[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)的[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)。
1. 向单元格插入一些数据。
1. 根据插入的数据创建[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)。
1. 根据[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)的数据范围创建[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)。
1. 将结果保存在磁盘上。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicCharts.py" >}}

## **使用动态公式**

如果您不希望将[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)作为动态图表的数据源，则另一个选项是使用Excel函数（或公式）创建动态数据范围，并使用控件（如下拉列表）触发数据更改。在这种情况下，我们将使用VLOOKUP函数根据下拉列表的选择来获取适当的值。选择更改时，VLOOKUP函数将刷新单元格值。如果一系列单元格使用VLOOKUP函数，则用户交互时可以刷新整个范围，因此它可以用作动态图表的数据源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按照下面的步骤一步步地前进。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)。
1. 访问[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)中第一个[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)的[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)。
1. 通过创建命名范围在单元格中插入一些数据。这些数据将作为动态图表的系列。
1. 根据先前步骤中创建的命名范围创建[**ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox)。
1. 在作为VLOOKUP函数源的单元格中插入更多数据。
1. 插入VLOOKUP函数（带适当参数）以一系列单元格。该范围将作为动态图表的数据源。
1. 根据先前步骤中创建的范围创建[**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)。
1. 将结果保存在磁盘上。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateDynamicChartsUsingDynamicFormula.py" >}}
{{< app/cells/assistant language="python-net" >}}
