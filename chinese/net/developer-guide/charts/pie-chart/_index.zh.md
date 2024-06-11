---
title: 创建带引导线的饼图
description: 学习如何使用 Aspose.Cells for .NET 在 Microsoft Excel 中创建带引导线的饼图。我们的指南将演示如何添加连接数据点到图例的引导线，以提高图表的整体清晰度。
keywords: Aspose.Cells for .NET，饼图，引导线，Microsoft Excel，数据可视化，图表自定义。
linktitle: 饼图
type: docs
weight: 45
url: /zh/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

本文解释了如何使用 Aspose.Cells for .NET API 从头开始创建带引导线的饼图。在 Excel 中，“显示引导线”选项默认设置为启用，因此创建 Excel 中的饼图时会显示引导线。然而，在使用 Aspose.Cells API 创建类似图表时，必须显式设置 [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) 属性。

{{% /alert %}}

为了演示使用 Aspose.Cells for .NET API 创建带引导线的饼图，我们首先将创建一个新的 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 并输入一些数据作为系列数据源。一旦数据就位，我们将向图表集合中添加一个 [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) 类型的 [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) 并设置其不同方面以获得所需的图表视图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

到目前为止，我们已经创建了饼图并设置了其不同的方面。现在我们将为图表打开引导线。请注意，为了显示引导线，我们必须稍微移动数据标签的位置。

以下代码片段打开了引导线，刷新了图表，然后计算数据标签的位置，以相应地移动它们。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

最后，以下代码将图表保存为图像格式，将工作簿保存为XLSX格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**结果饼图**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高级主题**
- [饼图中自定义切片或区块颜色](/cells/zh/net/custom-slice-or-sector-colors-in-pie-chart/)
- [查找数据点是否在饼图的第二个饼图或柱状图的柱状图上](/cells/zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 相关文章

- [创建图表](/cells/zh/net/creating-charts/)
- [自定义图表](/cells/zh/net/customizing-charts/)
- [图表中的数据格式化](/cells/zh/net/data-formatting-in-charts/)
- [设置图表外观](/cells/zh/net/setting-chart-appearance/)

