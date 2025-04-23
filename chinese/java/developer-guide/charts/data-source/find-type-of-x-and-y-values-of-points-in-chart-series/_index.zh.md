---
title: 查找图表系列中点的X和Y值类型
type: docs
weight: 110
url: /zh/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能的使用场景**

有时，您想了解系列中的图表点的 X 和 Y 值的类型。Aspose.Cells 提供了 [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) 和 [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType) 属性，可用于此目的。请注意，在使用这些属性之前，您必须调用 [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) 方法。

## **查找图表系列中点的X和Y值类型**

以下示例代码加载了 [示例 Excel 文件](64716920.xlsx)，并访问了第一个工作表中的第一个图表。然后调用 [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) 方法，并查找第一个图表点的 X 和 Y 值的类型，并将其打印到控制台。请参阅下面显示的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **控制台输出**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
