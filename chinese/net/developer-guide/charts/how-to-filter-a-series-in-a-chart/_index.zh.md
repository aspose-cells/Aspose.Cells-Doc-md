---
title: 筛选图表数据的三种方法
description: 学习如何使用Aspose.Cells for .NET在Excel中筛选图表。我们全面的指南将演示如何对图表应用筛选器，自定义图表元素，并使用数据分析工具获得更好的见解和决策。
keywords: Aspose.Cells for .NET，Excel中的图表筛选，数据分析，决策制定，可视化。
type: docs
weight: 2210
url: /zh/net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. 过滤系列以渲染图表**

### **在Excel中筛选图表系列的步骤**
在Excel中，我们可以筛选掉图表中的特定系列，导致这些被筛选的系列在图表中不显示。原始图表如 **图1** 所示。然而，当我们筛选掉 **Testseries2** 和 **Testseries4**时，图表将显示为 **图2** 所示。

在Aspose.Cells中，我们可以执行类似的操作。对于类似于这样的[样本](seriesFiltered.xlsx)文件，如果我们想要筛选掉 **Testseries2** 和 **Testseries4**，我们可以执行以下代码。此外，我们将维护两个列表：一个([NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) 列表来存储所有选定的系列，另一个([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) 来存储被筛选的系列。

请**注意**，在代码中当我们设置 **chart.NSeries[0].IsFiltered = true;** 时，[NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) 中的第一个系列将被移除并放置在 [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/) 中的适当位置。随后，以前的 **NSeries[1]** 将成为列表中的新第一项，并且所有后续系列将向前移动一个位置。这意味着如果我们之后运行 **chart.NSeries[1].IsFiltered = true;**，我们实际上是删除了原始的第三个系列。这有时会导致混乱，因此我们建议按照代码中的操作，从末尾向开头删除系列。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](seriesFiltered.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

## **2. 筛选数据，让图表发生变化**

筛选您的数据是处理大量数据的图表筛选的好方法。当您筛选数据时，图表将发生变化。我们将需要解决的一个问题是确保图表保持在屏幕上。当您筛选时，会出现隐藏的行，有时候图表会位于这些隐藏的行中。

![todo:image_alt_text](Figure3.png)

### **使用数据筛选器更改Excel中的图表的步骤**

1. 点击数据范围内。
2. 单击 **数据** 选项卡，并点击筛选器以开启筛选器。您的标题行将有下拉箭头。
3. 通过转到 **插入** 选项卡并选择柱状图来创建一个图表。
4. 现在使用数据中的下拉箭头来过滤您的数据。不要使用图表过滤器。

### **示例代码**
以下示例代码展示了使用Aspose.Cells的相同功能。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. 使用数据表对数据进行过滤，让图表改变**

使用表格类似于方法2，使用范围，但是表格比范围具有优势。当您将范围更改为表格并添加数据时，图表会自动更新。而在范围中，您将必须更改数据源。

### **在Excel中格式化为表格**

单击数据内部，使用**CTRL + T**或使用主页选项卡，**格式为表格**

![todo:image_alt_text](Figure4.png)

### **示例代码**
以下示例代码加载了[样本Excel文件](TableFilters.xlsx)，展示了使用Aspose.Cells相同的功能。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
