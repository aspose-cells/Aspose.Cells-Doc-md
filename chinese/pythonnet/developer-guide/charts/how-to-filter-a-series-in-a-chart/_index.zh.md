---
title: 过滤图表数据的三种方法
description: 学习如何使用 Aspose.Cells for Python via .NET 在Excel中筛选图表。我们的全面指南将演示如何对图表应用筛选、自定义图表元素，以及使用数据分析工具获取更好的见解和做出明智决策。
keywords: Aspose.Cells for Python via .NET、Excel中的筛选图表、数据分析、决策制定、数据可视化。
type: docs
weight: 2210
url: /zh/python-net/filtering-charts-in-excel/
---


## **1. 过滤以渲染图表的系列**

### **在Excel中，我们可以过滤掉图表中的特定系列，导致这些被过滤的系列不会显示在图表中。 原始图表显示在**图1**中。然而，当我们过滤掉**Testseries2**和**Testseries4**时，图表将会如**图2**所示。**
在Excel中，我们可以过滤掉图表中的特定系列，导致被过滤的系列不会显示在图表中。原始图表如**图1**所示。然而，当我们过滤掉**Testseries2**和**Testseries4**时，图表将如**图2**所示。

在 Aspose.Cells for Python via .NET 中，我们可以执行类似操作。对于一个[示例](seriesFiltered.xlsx)文件，如果想筛选掉 **Testseries2** 和 **Testseries4**，可以运行以下代码。同时，我们还将维护两个列表：一个（[n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)）用来存储所有选择的系列，另一个（[filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)）用来存储筛选后的系列。

请**注意**，在代码中，当我们设置 **chart.nSeries[0].is_filtered = TRUE;** 时，列表[ n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)中的第一组将被删除，并放入[ filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)的适当位置。随后，原本的 **nSeries[1]** 将成为新列表中的第一个项目，所有后续系列也会向前移。这意味着如果接着运行 **chart.nSeries[1].is_filtered = TRUE;**，实际是在删除原本的第三个系列。此操作有时会引起混淆，因此建议按照代码中的顺序，从后向前删除系列。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](seriesFiltered.xlsx)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-seriesFiltered.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DataFilters.py" >}}

## **3. 使用表格过滤数据并使图表发生变化**

使用表格类似于方法2，使用范围，但表格比范围有优势。当您将范围更改为表格并添加数据时，图表会自动更新。使用范围时，您将不得不更改数据源。

### **在Excel中格式化为表格**

单击数据内部并使用**CTRL + T**或使用主页选项卡，**格式为表格**

![todo:image_alt_text](Figure4.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](TableFilters.xlsx)展示了使用Aspsoe.Cells相同的功能。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TableFilters.py" >}}
{{< app/cells/assistant language="python-net" >}}
