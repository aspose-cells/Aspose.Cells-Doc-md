---
title: 创建带有引线的饼图
linktitle: 饼图
type: docs
weight: 170
url: /zh/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

本文介绍了如何使用Aspose.Cells for Java API从头开始创建带有引导线的饼图。在Excel中，“显示引导线”选项默认设置为打开，因此在Excel中创建饼图时会显示引导线。但是，在使用Aspose.Cells API创建类似图表时，您必须显式设置[**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines)属性。

{{% /alert %}}

## **使用引导线创建饼图**

为了演示如何使用Aspose.Cells for Java API创建带有引导线的饼图，我们首先将创建一个新的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，输入一些数据作为系列数据源。一旦数据就位，我们将向图表集合中添加一个类型为[**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE)的[**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)，并设置它的不同方面以获得所需的图表视图。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**结果饼图**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## 相关文章

- [创建和定制图表](/cells/zh/java/creating-and-customizing-charts/)
- [图表格式化](/cells/zh/java/chart-formatting/)
