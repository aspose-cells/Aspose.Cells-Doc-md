---
title: 使用Golang通过C++查找图表系列中点的X和Y值的类型
linktitle: 查找图表系列中点的X和Y值类型
description: 学习如何使用 Aspose.Cells for C++ 确定图表系列点的 X 和 Y 值的类型。我们的指南将解释不同类型的数据值，并向您展示如何在图表中访问和处理它们。
keywords: Aspose.Cells for C++，图表，X 值，Y 值，数据类型，访问，处理，图表系列。
type: docs
weight: 150
url: /zh/go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能的使用场景**
有时，您想知道图表系列中点的 X 和 Y 值的类型。Aspose.Cells 提供了 `ChartPoint::get_XValueType` 和 `ChartPoint::get_YValueType` 方法用于此目的。请注意，在有效使用这些属性之前，您需要调用 `Chart::Calculate()` 方法。

## **查找图表系列中点的X和Y值类型**
以下示例代码加载了 [示例 Excel 文件](64716905.xlsx)，并访问了第一个工作表中的第一个图表。然后调用 `Chart::Calculate()` 方法，找到第一个图表点的 X 和 Y 值的类型，并在控制台输出。请参阅下面的控制台输出作为参考。

## **示例代码**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}
## **控制台输出**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
