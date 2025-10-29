---
title: 通过 Golang 使用 C++ 操作位置大小和设计师图表
linktitle: 操纵位置大小和设计图表
description: 学习如何使用Aspose.Cells for C++高效操作Microsoft Excel中的位置、大小和设计图表。我们的指南将演示如何调整这些属性以改善布局和可视化效果。
keywords: Aspose.Cells for C++，位置，大小，设计图表，Microsoft Excel，布局，可视化。
type: docs
weight: 45
url: /zh/go-cpp/manipulate-position-size-and-designer-chart/
---

## **图表位置和大小**
有时，你想改变工作表内新建或已有图表的位置或大小。Aspose.Cells 提供了 [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/) 属性实现此功能。可以使用其子属性调整图表的**高度**和**宽度**，或用新的**X**和**Y**坐标重新定位图表。

### **控制图表的位置和大小**
要更改图表的位置（X、Y坐标）或大小（高度，宽度），请使用以下属性：

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

以下示例解释了上述API的使用方法，它加载包含图表的现有工作簿的第一个工作表。然后使用Aspose.Cells重新调整和重新定位图表。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **操作设计图表**
有时需要在设计模板文件中操纵或修改图表。Aspose.Cells完全支持操纵设计图表内容和元素。数据、图表内容、背景图像和格式可以准确保留。

### **在模板文件中操纵设计图表**
要在模板文件中操纵设计图表，请使用与图表相关的API。例如，您可以使用Worksheet.Charts属性获取模板文件中现有的图表集合。

#### **创建图表**
以下示例显示了如何创建金字塔图表。稍后我们将操纵此图表。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **操作图表**
以下示例显示了如何操纵现有的图表。在此示例中，我们修改了上面创建的图表。请注意，在生成的输出中，一个数据点的日期标签已设置为“United Kingdom, 30K”。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **在设计师模板中操作折线图**
在这个例子中，我们将操作一个折线图。我们将向现有图表添加一些数据系列，并改变它们的线条颜色。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
