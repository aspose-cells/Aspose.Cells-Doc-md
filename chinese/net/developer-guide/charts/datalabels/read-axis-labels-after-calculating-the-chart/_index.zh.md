---
title: 计算图表后读取轴标签
description: 了解如何在计算图表后读取 Aspose.Cells for .NET 中的轴标签。我们的指南将向您展示如何访问和检索轴标签，包括它们的格式和位置。
keywords: Aspose.Cells for .NET, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /zh/net/read-axis-labels-after-calculating-the-chart/
---
##  **可能的使用场景**

您可以在使用以下命令计算图表的值后读取图表的轴标签[**图表.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)方法。请使用[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/)用于此目的的方法将返回轴标签列表。

##  **计算图表后读取轴标签**

请参阅以下加载示例代码[Excel 文件示例](ReadAxisLabels.xlsx)并读取第一个工作表中图表的类别轴标签。然后它在控制台上打印轴标签的值。请参阅下面给出的示例代码的控制台输出以供参考。

##  **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

##  **控制台输出**

{{< highlight "csharp" >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
