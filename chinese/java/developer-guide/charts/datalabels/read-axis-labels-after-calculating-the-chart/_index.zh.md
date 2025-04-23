---
title: 在计算图表后读取轴标签
description: 学习如何在计算图表后读取Aspose.Cells for Java中的轴标签。我们的指南将向您展示如何访问和检索轴标签，包括它们的格式和位置。
keywords: Aspose.Cells for Java, 图表, 轴标签, 计算, 读取, 访问, 检索, 格式, 位置。
type: docs
weight: 90
url: /zh/java/read-axis-labels-after-calculating-the-chart/
---

## **可能的使用场景**

您可以在计算图表数值后，使用[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--)方法读取您的图表的轴标签。请为此目的使用[**Axis.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--)方法，它将返回轴标签的列表。

## **计算图表后读取轴标签**

请查看以下示例代码，加载 [示例 Excel文件](64716829.xlsx)，读取第一个工作表中图表的类别轴标签。然后在控制台上打印轴标签的值。请参考下面给出的示例代码的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

## **控制台输出**

{{< highlight java >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
