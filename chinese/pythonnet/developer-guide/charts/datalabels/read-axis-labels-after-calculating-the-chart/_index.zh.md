---
title: 在计算图表后读取轴标签
description: 学习如何在Aspose.Cells for Python via .NET中读取图表的轴标签。我们的指南将向您展示如何访问和检索轴标签，包括其格式和位置。
keywords: Aspose.Cells for Python via .NET，制图，轴标签，计算，读取，访问，检索，格式，位置。
type: docs
weight: 90
url: /zh/python-net/read-axis-labels-after-calculating-the-chart/
---

## **可能的使用场景**

您可以使用[**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/)方法在计算图表的值后读取其轴标签。请使用[**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts)方法，它将返回轴标签的列表。

## **计算图表后读取轴标签**

请参阅以下示例代码，加载[sample Excel file]（ReadAxisLabels.xlsx）并读取第一个工作表中图表的类别轴标签。然后在控制台上打印轴标签的值。请参阅下面的示例代码的控制台输出进行参考。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

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
