---
title: 在计算图表后读取轴标签
description: 了解如何在Aspose.Cells for .NET中计算图表后读取轴标签。 我们的指南将向您展示如何访问和检索轴标签，包括它们的格式和位置。
keywords: Aspose.Cells for .NET, 图表，轴标签，计算，读取，访问，检索，格式，位置。
type: docs
weight: 90
url: /zh/net/read-axis-labels-after-calculating-the-chart/
---

## **可能的使用场景**

您可以在使用[**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/)方法计算其值后读取图表的轴标签。 请为此目的使用[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/)方法，该方法将返回轴标签的列表。

## **在计算图表后读取轴标签**

请参阅以下示例代码，加载第一个工作表中的[sample Excel文件](ReadAxisLabels.xlsx)并读取图表的类别轴标签。 然后在控制台上打印轴标签的值。 请查看下面给出的示例代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

## **控制台输出**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
