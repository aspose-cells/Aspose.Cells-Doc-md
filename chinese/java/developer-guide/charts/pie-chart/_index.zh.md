---
title: 创建带引导线的饼图
linktitle: 饼形图
type: docs
weight: 170
url: /zh/java/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

本文介绍了如何使用 Aspose.Cells for Java API 从头开始创建带引导线的饼图。在 Excel 中，默认设置“显示引导线”选项，因此当您在 Excel 中创建饼图时，会显示引导线。但是，在使用 Aspose.Cells API 创建类似图表时，您必须显式设置[**系列.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines)财产。

{{% /alert %}}

## **创建带引导线的饼图**

为了演示 Aspose.Cells for Java API 创建带引导线的饼图的用法，我们将首先创建一个新的[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)并输入一些数据作为系列数据源。一旦数据到位，我们将添加一个[**图表**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)类型[**馅饼**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE)到图表集合并设置它的不同方面以获得所需的图表视图。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**结果饼图**

![待办事项：图像_替代_文本](creating-pie-chart-with-leader-lines_1.png)

## 相关文章

- [创建和自定义图表](/cells/zh/java/creating-and-customizing-charts/)
- [图表格式](/cells/zh/java/chart-formatting/)
