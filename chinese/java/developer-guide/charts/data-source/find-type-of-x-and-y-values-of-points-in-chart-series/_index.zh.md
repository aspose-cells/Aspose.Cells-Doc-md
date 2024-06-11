---
title: 查找图表系列中点的X和Y值类型
type: docs
weight: 110
url: /zh/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能的使用场景**

有时候，您想知道图表系列中点的X和Y值的类型。Aspose.Cells提供了[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)和[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)属性供此目的使用。请注意，您需要在有效地使用这些属性之前调用[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()方法。

## **查找图表系列中点的X和Y值类型**

以下示例代码加载了[sample Excel file](64716920.xlsx)，并访问了第一个工作表中的第一个图表。然后调用了[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()方法，找到了第一个图表点的X和Y值的类型，并在控制台上打印了它们。请参考下面的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **控制台输出**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
