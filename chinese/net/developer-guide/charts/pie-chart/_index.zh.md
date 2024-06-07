---
title: 创建带有引线的饼图
description: 了解如何使用Aspose.Cells for .NET在Microsoft Excel中创建带有引线的饼图。 我们的指南将演示如何添加引线，将数据点连接到图例，并增强图表的整体清晰度。
keywords: Aspose.Cells for .NET，饼图，引线，Microsoft Excel，数据可视化，图表定制。
linktitle: 饼图
type: docs
weight: 45
url: /zh/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

本文介绍如何使用Aspose.Cells for .NET API从头开始创建带有引线的饼图。 在Excel中，默认情况下设置“显示引导线”选项，因此在Excel中创建饼图时会显示引导线。 但是，在使用Aspose.Cells API创建类似图表时，您必须显式设置[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines)属性。

{{% /alert %}}

为了演示如何使用Aspose.Cells for .NET API创建带有引线的饼图，我们将首先创建一个新的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，并输入一些数据作为系列数据源。 一旦数据就位，我们将向图表集合中添加一个类型为[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)的[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)，并设置其不同方面以获取所需的图表视图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

到目前为止，我们已经创建了一个饼图并设置了其不同方面。 现在我们将打开图表的引线。 请注意，为了显示引导线，我们必须将数据标签移动一点。

以下代码段打开了引线，刷新了图表，然后计算数据标签的位置以相应移动它们。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

最后，以下代码将图表保存为图像格式，并将工作簿保存为XLSX格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**生成的饼图**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高级主题**
- [在饼图中自定义片段或扇区颜色](/cells/zh/net/custom-slice-or-sector-colors-in-pie-chart/)
- [查找在饼图或饼图的第二个饼或柱中的数据点](/cells/zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 相关文章

- [创建图形](/cells/zh/net/creating-charts/)
- [自定义图表](/cells/zh/net/customizing-charts/)
- [图表中的数据格式](/cells/zh/net/data-formatting-in-charts/)
- [设置图表外观](/cells/zh/net/setting-chart-appearance/)

