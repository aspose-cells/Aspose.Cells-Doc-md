---
title: 创建动态图表
type: docs
weight: 200
url: /zh/java/create-dynamic-charts/
---
{{% alert color="primary" %}}

动态（或交互式）图表能够在您更改数据范围时进行更改。换句话说，动态图表可以在数据源发生变化时自动反映变化。为了触发数据源的变化，可以使用 Excel 表格的过滤选项或使用 ComboBox 或 Dropdown 列表等控件。

本文演示了使用 Aspose.Cells for Java API 使用上述两种方法创建动态图表。

{{% /alert %}}

## **使用 Excel 表格**

{{% alert color="primary" %}}

Excel 表在 Aspose.Cells 的视角中称为 ListObjects，因此为了清楚起见，我们将使用术语“ListObject”而不是“Table”。请详细阅读如何操作[创建列表对象](/cells/zh/java/creating-a-list-object/)与 Aspose.Cells for .NET API。

{{% /alert %}}

ListObjects 提供了内置功能，可根据用户交互对数据进行排序和过滤。排序和过滤选项都是通过下拉列表提供的，这些列表会自动添加到 ListObject 的标题行。由于这些功能（排序和过滤），ListObject 似乎是充当动态图表数据源的完美候选者，因为当排序或过滤发生变化时，图表中的数据表示将发生变化以反映当前ListObject 的状态。

为了使演示简单易懂，我们将从头开始创建工作簿，并按如下所述逐步进行。

1. 创建一个空的工作簿。
1. 访问工作簿中第一个工作表的 Cells。
1. 向单元格中插入一些数据。
1. 根据插入的数据创建 ListObject。
1. 根据ListObject的数据范围创建Chart。
1. 将结果保存在光盘上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingExcelTables-UsingExcelTables.java" >}}

## **使用动态公式**

如果您不希望使用 ListObjects 作为动态图表的数据源，另一种选择是使用 Excel 函数（或公式）创建动态数据范围，并使用控件（例如 ComboBox）触发更改在数据中。在这种情况下，我们将使用 VLOOKUP 函数根据 ComboBox 的选择获取适当的值。选择更改时，VLOOKUP 函数将刷新单元格值。如果单元格范围使用 VLOOKUP 函数，整个范围可以在用户交互时刷新，因此可以用作动态图表的源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按如下所述逐步进行。

1. 创建一个空的工作簿。
1. 访问工作簿中第一个工作表的 Cells。
1. 通过创建命名范围向单元格插入一些数据。此数据将用作动态图表的系列。
1. 根据上一步中创建的命名范围创建 ComboBox。
1. 将更多数据插入将用作 VLOOKUP 函数源的单元格。
1. 将 VLOOKUP 函数（使用适当的参数）插入到一系列单元格中。此范围将作为动态图表的来源。
1. 根据上一步中创建的范围创建图表。
1. 将结果保存在光盘上。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDynamicFormulas-UsingDynamicFormulas.java" >}}
