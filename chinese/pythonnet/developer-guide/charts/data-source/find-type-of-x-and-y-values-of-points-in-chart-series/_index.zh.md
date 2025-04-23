---
title: 查找图表系列中点的X和Y值类型
description: 学习如何使用Aspose.Cells for Python via .NET确定图表系列点中X值和Y值的类型。我们的指南将解释不同类型的数据值，并向您展示如何在图表中访问和处理它们。
keywords: Aspose.Cells for Python via .NET，制图，X值，Y值，数据类型，访问，处理，系列。
type: docs
weight: 150
url: /zh/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能的使用场景**
有时，您希望了解图表系列中点的X和Y值的类型。Aspose.Cells for Python via .NET提供[**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/)和[**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/)属性，可以用来实现此目的。请注意，在有效使用这些属性之前，您必须调用[**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#)方法。

## **查找图表系列中点的X和Y值类型**
以下示例代码加载了[示例Excel文件](64716905.xlsx)，访问第一个工作表中的第一个图表，然后调用[**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#)方法，找出第一个图表点的X和Y值类型，并在控制台打印出来。请参见下方的控制台输出作为参考。

## **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **控制台输出**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
