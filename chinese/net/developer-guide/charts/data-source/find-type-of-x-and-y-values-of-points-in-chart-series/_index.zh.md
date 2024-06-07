---
title: 查找图表系列中点的 X 和 Y 值的类型
description: 学习如何使用 Aspose.Cells for .NET 中的 Chart 类确定图表系列点的 X 和 Y 值的类型。我们的指南将解释不同类型的数据值，并演示如何访问并处理它们。
keywords: Aspose.Cells for .NET, 图表化, X 值, Y 值, 数据类型, 访问, 处理, 图表系列。
type: docs
weight: 150
url: /zh/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能的使用场景**
有时候，您想确定系列中图表点的 X 和 Y 值的类型。Aspose.Cells 提供 ChartPoint.XValueType 和 ChartPoint.YValueType 属性，可用于此目的。请注意，在使用这些属性之前，您必须调用 Chart.Calculate() 方法。
## **查找图表系列中X和Y值的类型**
以下示例代码加载了 [示例Excel文件](64716905.xlsx)，并访问了第一个工作表中的第一个图表。然后调用 Chart.Calculate() 方法，并查找第一个图表点的 X 和 Y 值的类型，并在控制台上打印它们。请参考下面显示的控制台输出。
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **控制台输出**
{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
