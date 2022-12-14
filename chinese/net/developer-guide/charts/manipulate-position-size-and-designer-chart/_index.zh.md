---
title: 操纵头寸规模和设计师图表
type: docs
weight: 45
url: /zh/net/manipulate-position-size-and-designer-chart/
---
## **图表位置和大小**
有时，您想要更改工作表中新图表或现有图表的位置或大小。 Aspose.Cells 提供了[图表.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject)财产来实现这一点。您可以使用它的子属性来重新调整图表的大小**高度**和**宽度**或用新的重新定位**X** 和**Y** 坐标。
### **控制图表位置和大小**
要更改图表的位置（X、Y 坐标）或大小（高度、宽度），请使用以下属性：

1. [图表.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [图表.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.高度](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.宽度](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

以下示例解释了上述 API 的用法，它加载了现有工作簿，该工作簿的第一个工作表中包含一个图表。然后它使用 Aspose.Cells 重新调整图表的大小和位置。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **操纵设计师图表**
有时您需要操作或修改设计器模板文件中的图表。 Aspose.Cells 完全支持操纵设计器图表内容和元素。可以准确保存数据、图表内容、背景图像和格式。
### **在模板文件中操作设计器图表**
要在模板文件中操作设计器图表，请使用图表相关的 API。例如，您可以使用 Worksheet.Charts 属性来获取模板文件中现有的图表集合。
#### **创建图表**
以下示例显示了如何创建金字塔图。稍后我们将操作此图表。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **操纵图表**
以下示例显示如何操作现有图表。在这个例子中，我们修改上面创建的图表。在生成的输出中，请注意一个数据点的日期标签已设置为“英国，30K”。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **在设计器模板中操作折线图**
在这个例子中，我们将操作一个折线图。我们将向现有图表添加一些数据系列并更改它们的线条颜色。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

