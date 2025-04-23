---
title: 创建带引导线的饼图
description: 了解如何使用 Aspose.Cells for Python via .NET 在 Microsoft Excel 中创建带引线的饼图。我们的指南将演示如何添加连接数据点到图例的引线，从而增强图表的整体清晰度。
keywords: Aspose.Cells for Python via .NET，饼图，引线，Microsoft Excel，数据可视化，图表定制。
linktitle: 饼图
type: docs
weight: 45
url: /zh/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

本文介绍了如何在使用 Aspose.Cells for Python via .NET API 时，从头开始创建带引线的饼图。在 Excel 中，默认启用“显示引线”选项，因此在Excel中创建饼图时会显示引线。然而，在使用 Aspose.Cells for Python via .NET API 创建类似图表时，需显式设置 [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines) 属性。

{{% /alert %}}

为了演示如何使用 Aspose.Cells for Python via .NET API 创建带引线的饼图，我们将首先创建一个新的 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 并输入一些作为系列数据源的数据。一旦数据准备就绪，我们将添加一个类型为 [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) 的 [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) 图表到集合中，并设置其不同方面以达到预期的图表效果。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

到目前为止，我们已经创建了饼图并设置了其不同的方面。现在我们将为图表打开引导线。请注意，为了显示引导线，我们必须稍微移动数据标签的位置。

以下代码片段打开了引导线，刷新了图表，然后计算数据标签的位置，以相应地移动它们。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

最后，以下代码将图表保存为图像格式，将工作簿保存为XLSX格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**结果饼图**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高级主题**
- [饼图中自定义切片或区块颜色](/cells/zh/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [查找数据点是否在饼图的第二个饼图或柱状图的柱状图上](/cells/zh/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 相关文章

- [创建图表](/cells/zh/python-net/creating-charts/)
- [自定义图表](/cells/zh/python-net/customizing-charts/)
- [图表中的数据格式化](/cells/zh/python-net/data-formatting-in-charts/)
- [设置图表外观](/cells/zh/python-net/setting-chart-appearance/)

