---
title: 创建带引导线的饼图
linktitle: 饼图
type: docs
weight: 170
url: /zh/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

本文解释了如何使用 Aspose.Cells for Java API 从头开始创建带有引导线的饼图。在 Excel 中，“显示引导线”选项默认设置为显示引导线。然而，在使用 Aspose.Cells APIs 创建类似图表时，您必须明确设置 [**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines) 属性。

{{% /alert %}}

## **使用带有引线的饼图**

为了演示使用 Aspose.Cells for Java API 创建带有引导线的饼图，我们首先将创建一个新的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，并输入一些数据作为系列数据源。一旦数据就绪，我们将向图表集合中添加 [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) 类型 [**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE) 的图表，并设置其不同方面以获得所需的图表视图。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**生成的饼图**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## 相关文章

- [创建和自定义图表](/cells/zh/java/creating-and-customizing-charts/)
- [图表格式设置](/cells/zh/java/chart-formatting/)
