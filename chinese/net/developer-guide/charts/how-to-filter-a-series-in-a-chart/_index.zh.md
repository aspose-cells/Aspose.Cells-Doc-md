---
title: 过滤图表数据的三种方法
description: 了解如何使用 Aspose.Cells for .NET 在 Excel 中筛选图表。我们的综合指南将演示如何将筛选器应用于图表、自定义图表元素以及使用数据分析工具以获得更好的见解和明智的决策。
keywords: Aspose.Cells for .NET, Filtering Charts in Excel, Data Analysis, Decision Making, Visualization.
type: docs
weight: 2210
url: /zh/net/filtering-charts-in-excel/
---
{{% alert color="primary" %}}

##  **1. 过滤出系列来渲染图表**

###  **从 Excel 图表中筛选系列的步骤**
在Excel中，我们可以从图表中过滤掉特定的系列，导致这些过滤后的系列不显示在图表中。原始图表如图所示**图1**。然而，当我们过滤掉 **Testseries2**和*Testseries4**，图表将如图*图2**所示。

在Aspose.Cells中，我们可以进行类似的操作。为一个[样本](seriesFiltered.xlsx)像这样的文件，如果我们想过滤掉**测试系列2**和*Testseries4**，我们可以执行以下代码。此外，我们将维护两个列表：一个（[N系列](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)列表来存储所有选定的系列和另一个 ([过滤N系列](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)）来存储过滤后的系列。

请**笔记**在代码中，当我们设置**Chart.NSeries[0].IsFiltered = true;**，[NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) 中的第一个系列将被删除并放置在 [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/) 内的适当位置。随后，之前的**N系列[1]**将成为列表中新的第一项，并且所有后续系列将向前移动一个位置。这意味着，如果我们随后运行 *chart.NSeries[1].IsFiltered = true;**，我们将有效删除原始的第三个系列。这有时会导致混乱，因此我们建议按照代码中的操作，从末尾到开头删除系列。

![待办事项：图像_替代_文本](Figure1.png)

![待办事项：图像_替代_文本](Figure2.png)

###  **示例代码**
以下示例代码加载[Excel 文件示例](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

##  **2.过滤数据，让图表发生变化**

过滤数据是处理包含大量数据的图表过滤器的好方法。当您过滤数据时，图表会发生变化。我们必须解决的一个问题是确保图表保留在屏幕上。当您进行筛选时，您会得到隐藏行，有时图表将位于这些隐藏行中。

![待办事项：图像_替代_文本](Figure3.png)

###  **使用数据过滤器更改 Excel 中的图表的步骤**

1. 在数据范围内单击。
 2. 单击**数据**选项卡，然后单击过滤器打开过滤器。您的标题行将有下拉箭头。
 3. 创建图表：**插入**选项卡并选择柱形图。
4. 现在使用数据中的下拉箭头过滤数据。不要使用图表过滤器。

###  **示例代码**
以下示例代码使用 Aspsoe.Cells 显示了相同的功能。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

##  **3. 使用表格过滤数据并让图表发生变化**

使用表与方法 2 类似，使用范围，但使用表比范围更有优势。当您将范围更改为表格并添加数据时，图表会自动更新。对于范围，您将必须更改数据源。

###  **将格式设置为 Excel 中的表格**

单击您的数据并使用**CTRL + T**或使用“主页”选项卡，**设置为表格格式**

![待办事项：图像_替代_文本](Figure4.png)

###  **示例代码**
以下示例代码加载[Excel 文件示例](TableFilters.xlsx)使用 Aspsoe.Cells 显示相同的功能。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}