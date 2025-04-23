---
title: 如何创建旭日图表
description: 学习如何在 Aspose.Cells for .NET 中创建一个环形图，即一种以圆圈形式呈现数据的图表。我们的指南将帮助您设置各种属性和格式化图表，包括数据标签、图例、颜色等。
keywords: Aspose.Cells for .NET，环形图，创建，设置属性，数据标签，图例，格式，颜色，圆圈，数据呈现。
type: docs
weight: 162
url: /zh/net/creating-sunburst-chart/
---

## **可能的使用场景**
Treemap图表适用于比较层次结构内的比例，然而，Treemap图表并不擅长显示最大类别和每个数据点之间的层次级别。旭日图表是展示这一点的更好的视觉图表。旭日图表非常适合显示分层数据。层次结构的每个层级由一个环或圆圈表示，最内层的圆圈为层次结构的顶部。没有任何层次数据的旭日图表（一个类别级别），看起来类似于甜甜圈图表。然而，具有多个类别层级的旭日图表显示外部环如何与内部环相关。旭日图表最有效地显示了一个环如何被划分为其组成部分，而另一种类型的层次图表，Treemap图表，则适用于比较相对大小。

![todo:image_alt_text](sample.png)
## **旭日图表**
运行下面的代码后，您将会看到如下所示的旭日图表。

![todo:image_alt_text](result.png)
## **示例代码**
以下示例代码加载 [样本 Excel 文件](sunburst.xlsx) 并生成 [输出 Excel 文件](out.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-sunburst-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
