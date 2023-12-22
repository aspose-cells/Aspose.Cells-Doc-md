---
title: 如何创建旭日图
description: 了解如何在 Aspose.Cells for .NET 中创建旭日图，该图表以圆圈形式显示数据。我们的指南将帮助您设置图表的各种属性和格式，包括数据标签、图例、颜色等。
keywords: Aspose.Cells for .NET, sunburst chart, create, set properties, data labels, legend, format, color, circle, data rendering.
type: docs
weight: 162
url: /zh/net/creating-sunburst-chart/
---
##  **可能的使用场景**
树形图非常适合比较层次结构内的比例，但是树形图不太适合显示最大类别和每个数据点之间的层次结构级别。旭日图是显示这一点的更好的可视化图表。旭日图非常适合显示分层数据。层次结构的每一层都由一个环或圆圈表示，最里面的圆圈作为层次结构的顶部。没有任何分层数据（一级类别）的旭日图看起来类似于圆环图。然而，具有多个类别级别的旭日图显示了外环与内环的关系。旭日图最能有效地显示一个环如何分解成其贡献的部分，而另一种类型的分层图表（树状图）则非常适合比较相对大小。

![待办事项：图像_替代_文本](sample.png)
##  **旭日图**
运行下面的代码后，您将看到如下所示的旭日图。

![待办事项：图像_替代_文本](result.png)
##  **示例代码**
以下示例代码加载[Excel 文件示例](sunburst.xlsx)并生成[输出Excel文件](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-sunburst-chart.cs" >}}
