---
title: 操纵头寸规模和设计图表
description: 了解如何使用 Aspose.Cells for .NET 有效地操作 Microsoft Excel 中的位置、大小和设计器图表。我们的指南将演示如何调整这些属性以改进布局和可视化。
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /zh/net/manipulate-position-size-and-designer-chart/
---
##  **图表位置和大小**
有时，您想要更改工作表中新图表或现有图表的位置或大小。 Aspose.Cells 提供[图表.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject)财产来实现这一目标。您可以使用其子属性来重新调整图表的大小**高度**和**宽度**或用新的重新定位**X** 和 **Y**坐标。
###  **控制图表位置和大小**
要更改图表的位置（X、Y 坐标）或大小（高度、宽度），请使用以下属性：

1. [图表.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [图表.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

以下示例解释了上述 API 的用法，它加载现有工作簿，其中第一个工作表中包含图表。然后它使用 Aspose.Cells 重新调整图表大小并重新定位图表。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **操作设计图表**
有时您需要操作或修改设计器模板文件中的图表。 Aspose.Cells 完全支持操作设计器图表内容和元素。数据、图表内容、背景图像和格式都可以准确保存。
###  **操作模板文件中的设计器图表**
要操作模板文件中的设计器图表，请使用与 API 相关的图表。例如，您可以使用 Worksheet.Charts 属性来获取模板文件中现有的图表集合。
####  **创建图表**
以下示例展示了如何创建金字塔图。稍后我们将操纵这个图表。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **操纵图表**
以下示例显示如何操作现有图表。在此示例中，我们修改上面创建的图表。在生成的输出中，请注意一个数据点的日期标签已设置为“United Kingdom, 30K”。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **在设计器模板中操作折线图**
在此示例中，我们将操作折线图。我们将向现有图表添加一些数据系列并更改其线条颜色。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

