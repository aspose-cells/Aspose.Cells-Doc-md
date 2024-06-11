---
title: 查找图表系列中点的X和Y值类型
description: 学习如何使用 Aspose.Cells for .NET 确定图表系列点中 X 和 Y 值的类型。我们的指南将解释不同类型的数据值，并向您展示如何访问和处理它们以在您的图表中使用。
keywords: Aspose.Cells for .NET，制图，X 值，Y 值，数据类型，访问，处理，图表系列。
type: docs
weight: 150
url: /zh/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能的使用场景**
有时，您希望了解系列中图表点的X和Y值的类型。Aspose.Cells提供了ChartPoint.XValueType和 ChartPoint.YValueType属性，可用于此目的。请注意，在有效使用这些属性之前，您必须调用Chart.Calculate()方法。
## **查找图表系列中点的X和Y值类型**
以下示例代码加载[示例Excel文件](64716905.xlsx)并访问第一个工作表中的第一个图表。然后调用Chart.Calculate()方法，并找到第一个图表点的X和Y值的类型，并将它们打印到控制台。请参阅下面显示的控制台输出进行参考。
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **控制台输出**
{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
