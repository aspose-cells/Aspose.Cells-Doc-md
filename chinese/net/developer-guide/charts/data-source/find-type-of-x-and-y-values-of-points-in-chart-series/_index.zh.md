---
title: 查找图表系列中点的 X 和 Y 值类型
description: 了解如何使用 Aspose.Cells for .NET 确定图表系列点中 X 和 Y 值的类型。我们的指南将解释不同类型的数据值，并向您展示如何在图表中访问和使用它们。
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /zh/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **可能的使用场景**
有时，您想知道系列中图表点的 X 和 Y 值的类型。 Aspose.Cells 提供了可用于此目的的 ChartPoint.XValueType 和 ChartPoint.YValueType 属性。请注意，您必须调用 Chart.Calculate() 方法才能有效地使用这些属性。
##  **查找图表系列中点的 X 和 Y 值类型**
以下示例代码加载[Excel 文件示例](64716905.xlsx)并访问第一个工作表中的第一个图表。然后它调用 Chart.Calculate() 方法并查找第一个图表点的 X 和 Y 值的类型并将它们打印在控制台上。请参阅下面显示的控制台输出以供参考。
##  **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **控制台输出**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
