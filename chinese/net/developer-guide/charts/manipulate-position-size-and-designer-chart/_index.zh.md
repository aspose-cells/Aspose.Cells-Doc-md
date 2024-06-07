---
title: 操作位置大小和设计图表
description: 学习如何使用Aspose.Cells for .NET来有效地操纵Microsoft Excel中的位置、大小和设计图表。我们的指南将展示如何调整这些属性以获得更好的布局和视觉效果。
keywords: Aspose.Cells for .NET、位置、大小、设计图表、Microsoft Excel、布局、可视化。
type: docs
weight: 45
url: /zh/net/manipulate-position-size-and-designer-chart/
---

## **图表位置和大小**
有时，您可能希望更改工作表内的新图表或现有图表的位置或大小。Aspose.Cells提供了[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject)属性来实现这一点。您可以使用其子属性来重新调整图表的新**高度**和**宽度**，或者使用新的**X**和**Y**坐标来重新定位它。
### **控制图表的位置和大小**
要更改图表的位置（X、Y坐标）或大小（高度、宽度），请使用这些属性：

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells/drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells/drawing/shape/properties/width)

以下示例解释了上述API的用法，它加载了包含图表的现有工作簿的文件。然后使用Aspose.Cells重新调整图表的大小和位置。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **操纵设计图表**
有时，您需要操纵或修改设计模板文件中的图表。Aspose.Cells完全支持操纵设计图表内容和元素。数据、图表内容、背景图像和格式可以准确地保留。
### **在模板文件中操作设计图表**
要在模板文件中操作设计图表，请使用与图表相关的API。 例如，您可以使用Worksheet.Charts属性获取模板文件中现有的图表集合。
#### **创建图表**
以下示例显示如何创建金字塔图表。 我们稍后将操作此图表。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **操作图表**
以下示例显示如何操作现有图表。 在此示例中，我们修改了上面创建的图表。 在生成的输出中，请注意一个数据点的日期标签已设置为“United Kingdom，30K”。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **在设计模板中操作折线图**
在此示例中，我们将操作一条折线图。 我们将向现有图表添加一些数据系列并更改它们的线条颜色。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

