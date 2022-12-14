---
title: 查找图表系列中点的 X 和 Y 值类型
type: docs
weight: 110
url: /zh/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **可能的使用场景**

有时，您想知道系列中图表点的 X 和 Y 值的类型。 Aspose.Cells提供[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)和[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)可用于此目的的属性。请注意，您必须致电[**图表.计算()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) 方法，然后才能有效地使用这些属性。

## **查找图表系列中点的 X 和 Y 值类型**

下面的示例代码加载[示例 Excel 文件](64716920.xlsx)并访问第一个工作表中的第一个图表。然后它调用[**图表.计算()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()方法并找到第一个图表点的 X 和 Y 值的类型，并将它们打印在控制台上。请参阅下面显示的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **控制台输出**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
