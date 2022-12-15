---
title: 创建带引导线的饼图
linktitle: 饼形图
type: docs
weight: 45
url: /zh/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

本文介绍了如何使用 Aspose.Cells for .NET API 从头开始创建带引导线的饼图。在 Excel 中，默认设置“显示引导线”选项，因此当您在 Excel 中创建饼图时，会显示引导线。但是，在使用 Aspose.Cells API 创建类似图表时，您必须显式设置[**系列.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines)财产。

{{% /alert %}}

为了演示 Aspose.Cells for .NET API 的用法来创建带有引导线的饼图，我们将首先创建一个新的[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)并输入一些数据作为系列数据源。一旦数据到位，我们将添加一个[**图表**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)类型[**ChartType.饼图**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)到图表集合并设置其不同方面以获得所需的图表视图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

到目前为止，我们已经创建了一个饼图并设置了它的不同方面。现在我们要打开图表的引导线。请注意，为了显示引导线，我们必须稍微移动数据标签。

以下代码段打开引导线，刷新图表，然后计算数据标签的位置以相应地移动它们。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

最后，以下代码将图表保存为图像格式，将工作簿保存为 XLSX 格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**结果饼图**|
|:- |
|![待办事项：图像_替代_文本](creating-pie-chart-with-leader-lines_1.png)|

## **推进主题**
- [饼图中的自定义切片或扇区颜色](/cells/zh/net/custom-slice-or-sector-colors-in-pie-chart/)
- [查找数据点是否位于饼图饼图或饼图条形图的第二个饼图或条形图中](/cells/zh/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 相关文章

- [创建图表](/cells/zh/net/creating-charts/)
- [自定义图表](/cells/zh/net/customizing-charts/)
- [图表中的数据格式](/cells/zh/net/data-formatting-in-charts/)
- [设置图表外观](/cells/zh/net/setting-chart-appearance/)

