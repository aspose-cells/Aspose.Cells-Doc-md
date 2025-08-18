---
title: 过滤图表数据的三种方法
description: 学习如何使用Aspose.Cells for .NET在Excel中过滤图表。我们的全面指南将演示如何对图表应用过滤器，自定义图表元素，并使用数据分析工具来获得更好的洞察力和明智的决策。 
keywords: Aspose.Cells for .NET，在Excel中过滤图表，数据分析，决策，可视化。
type: docs
weight: 2210
url: /zh/net/filtering-charts-in-excel/
---


## **1. 过滤以渲染图表的系列**

### **在Excel中，我们可以过滤掉图表中的特定系列，导致这些被过滤的系列不会显示在图表中。 原始图表显示在**图1**中。然而，当我们过滤掉**Testseries2**和**Testseries4**时，图表将会如**图2**所示。**
在Excel中，我们可以过滤掉图表中的特定系列，导致被过滤的系列不会显示在图表中。原始图表如**图1**所示。然而，当我们过滤掉**Testseries2**和**Testseries4**时，图表将如**图2**所示。

在Aspose.Cells中，我们可以执行类似的操作。对于像这样的[示例](seriesFiltered.xlsx)文件，如果想过滤掉**Testseries2**和**Testseries4**，可以执行以下代码。此外，我们会维护两个列表：一个（[NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)）存储所有已选择的系列，另一个（[FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filterednseries/)）存储过滤后的系列。

请**注意**，在代码中，当设置**chart.NSeries[0].IsFiltered = true;**时，**NSeries**中的第一个系列将被移除，并放入**FilteredNSeries**的适当位置。随后，原来的**NSeries[1]**将成为新列表中的第一个项目，之后的系列依次前移。这意味着如果随后运行**chart.NSeries[1].IsFiltered = true;**，实际上就是移除了原始的第三个系列。这有时会引起混淆，因此建议按照代码中的操作，从后向前删除系列。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](seriesFiltered.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

## **2. 过滤数据并使图表发生变化**

过滤数据是处理包含大量数据的图表筛选器的绝佳方法。当您过滤数据时，图表将发生变化。 我们需要解决的一个问题是确保图表保持在屏幕上。当您进行过滤时，会有隐藏行，并且偶尔图表将在这些隐藏行中。

![todo:image_alt_text](Figure3.png)

### **使用数据筛选器更改Excel中图表的步骤**

1. 点击数据范围内部。
2. 单击**数据**选项卡，通过单击筛选器进行筛选。 您的标题行将有下拉箭头。
3. 通过转到**插入**选项卡并选择列图表来创建图表。
4. 现在使用数据中的下拉箭头筛选您的数据。 不要使用图表筛选器。

### **示例代码**
以下示例代码展示了使用Aspsoe.Cells实现相同功能的方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. 使用表格过滤数据并使图表发生变化**

使用表格类似于方法2，使用范围，但表格比范围有优势。当您将范围更改为表格并添加数据时，图表会自动更新。使用范围时，您将不得不更改数据源。

### **在Excel中格式化为表格**

单击数据内部并使用**CTRL + T**或使用主页选项卡，**格式为表格**

![todo:image_alt_text](Figure4.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](TableFilters.xlsx)展示了使用Aspsoe.Cells相同的功能。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
{{< app/cells/assistant language="csharp" >}}
