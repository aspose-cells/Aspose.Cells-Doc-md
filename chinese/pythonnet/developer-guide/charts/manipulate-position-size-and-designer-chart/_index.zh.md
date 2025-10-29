---
title: 操纵位置大小和设计图表
description: 学习如何用 Aspose.Cells for Python via .NET 有效操作 Microsoft Excel 中的图例位置、大小和设计。我们的指南将展示如何调整这些属性以改善布局和可视化。
keywords: Aspose.Cells for Python via .NET，位置，大小，设计图表，Microsoft Excel，布局，视觉化。
type: docs
weight: 45
url: /zh/python-net/manipulate-position-size-and-designer-chart/
---

## **图表位置和大小**
有时，您希望改变工作表内新建或已存在的图表的位置或大小。Aspose.Cells for Python via .NET 提供了 [Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object) 属性来实现。您可以使用其子属性重新调整图表的**高度**和**宽度**，或使用**X**和**Y**坐标重新定位。
### **控制图表的位置和大小**
要更改图表的位置（X、Y坐标）或大小（高度，宽度），请使用以下属性：

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

以下示例说明了上述 API 的用法，它加载了一个包含图表的现有工作簿，该图表位于第一个工作表中。然后使用 Aspose.Cells for Python via .NET 重新调整图表的大小和位置。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **操作设计图表**
有时你需要操作或修改设计器模板文件中的图表。Aspose.Cells for Python via .NET 完全支持操作设计器图表内容和元素。数据、图表内容、背景图片和格式可以准确保持。
### **在模板文件中操纵设计图表**
要在模板文件中操纵设计图表，请使用与图表相关的API。例如，您可以使用Worksheet.Charts属性获取模板文件中现有的图表集合。
#### **创建图表**
以下示例显示了如何创建金字塔图表。稍后我们将操纵此图表。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **操作图表**
以下示例显示了如何操纵现有的图表。在此示例中，我们修改了上面创建的图表。请注意，在生成的输出中，一个数据点的日期标签已设置为“United Kingdom, 30K”。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **在设计师模板中操作折线图**
在这个例子中，我们将操作一个折线图。我们将向现有图表添加一些数据系列，并改变它们的线条颜色。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
