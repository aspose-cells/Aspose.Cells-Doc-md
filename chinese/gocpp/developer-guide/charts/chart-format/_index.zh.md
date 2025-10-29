---
title: 通过 C++ 在 Golang 中设置图表外观
linktitle: 图表格式
description: 学习如何在Aspose.Cells for C++中配置图表的外观。我们的指南将展示如何修改图表布局、颜色、字体和效果，以实现理想的视觉风格，提升工作表的美观度。
keywords: Aspose.Cells for C++，图表，外观，布局，颜色，字体，效果，工作表。
type: docs
weight: 20
url: /zh/go-cpp/setting-chart-appearance/
---

## **设置图表外观**
在《如何创建图表》中，我们简要介绍了Aspose.Cells提供的图表类型和图表对象，并描述了如何创建一个图表。本文讨论了如何通过设置图表属性来自定义图表的外观：

- 设置图表区域。
- 设置图表线条。
- 应用主题。
- 为图表和轴设置标题。
- 使用网格线。

### **设置图表区域**
图表中有不同类型的区域，Aspose.Cells提供了修改每个区域外观的灵活性。开发人员可以通过改变前景色、背景色和填充格式等设置，在一个区域上应用不同的格式设置。

在下面的示例中，我们在图表的不同区域应用了不同的格式设置。这些区域包括：

- 绘图区域
- 图表区域
- SeriesCollection区域
- SeriesCollection中单个点的区域

以下代码段演示了如何设置图表区域。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat.go" >}}
### **设置图表线条**
开发者还可以对 [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) 的线条或数据标记应用不同的样式。以下代码示例演示了如何使用 Aspose.Cells API 设置图表线条。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-1.go" >}}
### **将Microsoft Excel 2007/2010主题应用于图表**
开发者可以将不同的微软 Excel 主题/颜色应用于 [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) 或其他图表对象，具体示例如下。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-2.go" >}}
### **设置图表或坐标轴的标题**
你可以使用微软 Excel 在 WYSIWYG 环境中设置图表及其轴的标题。Aspose.Cells 还允许开发者在运行时设置图表及其轴的标题。所有图表及其轴都包含一个 [Title](https://reference.aspose.com/cells/go-cpp/title/) 属性，可以用来设置它们的标题，以下是示例。

以下代码段演示了如何设置图表和轴的标题。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-3.go" >}}
### **使用主要网格线**
可以自定义主要网格线的外观。隐藏或显示网格线，或定义它们的颜色和其他设置。下面，我们展示如何隐藏网格线以及如何更改它们的颜色。

#### **隐藏主要网格线**
开发者可以通过将 Line 对象的 [IsVisible](https://reference.aspose.com/cells/go-cpp/line/isvisible/) 属性设置为 **true** 或 **false** 来控制主要网格线的显示与隐藏。

以下代码片段演示如何隐藏主要网格线。隐藏主要网格线后，工作表将添加一个没有网格线的柱状图。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-4.go" >}}
#### **更改主要网格线设置**
开发人员不仅可以控制主要网格线的可见性，还可以控制其他属性，包括颜色等。

以下代码片段演示如何更改主要网格线的颜色。设置主要网格线的颜色后，工作表将添加一个具有修改网格线的柱状图。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-5.go" >}}
## **高级主题**
- [设置图表系列的值格式代码](/cells/zh/cpp/set-the-values-format-code-of-chart-series/)
- [在图表中将图片设置为背景填充](/cells/zh/cpp/set-picture-as-background-fill-in-the-chart/)
