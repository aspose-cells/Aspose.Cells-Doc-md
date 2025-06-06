---
title: 创建动态图表
description: 学习如何在 Aspose.Cells for .NET中创建动态图表。我们的指南将向您展示如何根据您的需求动态更新图表数据、系列和格式，使您能够在工作表中以视觉方式呈现变化的数据。
keywords: Aspose.Cells for .NET，制图，动态图表，数据，系列，格式，工作表，更新。
type: docs
weight: 240
url: /zh/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

动态（或交互式）图表在更改数据范围时具有更改的能力。换句话说，当数据源更改时，动态图表可以自动反映更改。为了触发数据源的更改，可以使用Excel表的筛选选项，或者使用控件如下拉列表或下拉菜单。

本文演示了使用 Aspose.Cells for .NET API创建动态图表的用法。

{{% /alert %}}

## **使用Excel表**

{{% alert color="primary" %}}

在 Aspose.Cells 的视角中，Excel 表被称为 ListObjects，因此，我们将使用术语“ListObject”而不是“表”以确保清晰。请详细阅读如何使用 Aspose.Cells for .NET API创建 ListObjects。

{{% /alert %}}

ListObjects提供了内置功能，可根据用户交互来对数据进行排序和过滤。排序和过滤选项都是通过下拉列表在添加到[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)的标头行中自动提供的。由于这些特性（排序和过滤），[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)似乎是作为动态图表数据源的完美候选，因为当排序或过滤发生变化时，图表中的数据表示将变化以反映[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)的当前状态。

为了使演示简单易懂，我们将从头开始创建[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，并按照下面概述的步骤逐步进行。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。
1. 访问[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)中第一个[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)的[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)。
1. 向单元格插入一些数据。
1. 根据插入的数据创建[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)。
1. 根据[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)的数据范围创建[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)。
1. 将结果保存在磁盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **使用动态公式**

如果您不希望将[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)作为动态图表的数据源，则另一个选项是使用Excel函数（或公式）创建动态数据范围，并使用控件（如下拉列表）触发数据更改。在这种情况下，我们将使用VLOOKUP函数根据下拉列表的选择来获取适当的值。选择更改时，VLOOKUP函数将刷新单元格值。如果一系列单元格使用VLOOKUP函数，则用户交互时可以刷新整个范围，因此它可以用作动态图表的数据源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按照下面的步骤一步步地前进。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。
1. 访问[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)中第一个[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)的[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)。
1. 通过创建命名范围在单元格中插入一些数据。这些数据将作为动态图表的系列。
1. 根据先前步骤中创建的命名范围创建[**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)。
1. 在作为VLOOKUP函数源的单元格中插入更多数据。
1. 插入VLOOKUP函数（带适当参数）以一系列单元格。该范围将作为动态图表的数据源。
1. 根据先前步骤中创建的范围创建[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)。
1. 将结果保存在磁盘上。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
