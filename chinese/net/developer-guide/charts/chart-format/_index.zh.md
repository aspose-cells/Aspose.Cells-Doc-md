---
title: 设置图表外观
description: 学习如何在 Aspose.Cells for .NET 中配置图表外观。我们的指南将向您展示如何修改图表布局，颜色，字体和效果，以实现期望的视觉风格，并增强您的工作表。
keywords: Aspose.Cells for .NET，图表制作，图表外观，布局，颜色，字体，效果，工作表。
linktitle: 图表格式
type: docs
weight: 20
url: /zh/net/setting-chart-appearance/
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



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **设置图表线条**
开发人员还可以通过Aspose.Cells API对线条或数据标记的[SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)应用不同类型的样式。以下代码段演示了如何使用Aspose.Cells设置图表线条。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **将Microsoft Excel 2007/2010主题应用于图表**
开发人员可以在下面的示例中为[SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)或其他图表对象应用不同的Microsoft Excel主题/颜色。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **设置图表或坐标轴的标题**
您可以使用Microsoft Excel在所见即所得的环境中设置图表及其轴的标题。Aspose.Cells还允许开发人员在运行时设置图表及其轴的标题。所有图表及其轴都包含一个[Title](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)属性，该属性可用于设置它们的标题，如下面的示例所示。

以下代码段演示了如何设置图表和轴的标题。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **使用主要网格线**
可以自定义主要网格线的外观。隐藏或显示网格线，或定义它们的颜色和其他设置。下面，我们展示如何隐藏网格线以及如何更改它们的颜色。
#### **隐藏主要网格线**
开发人员可以通过将 [Line](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) 对象的 [IsVisible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) 属性设置为 **true** 或 **false** 来控制主要网格线的可见性。

以下代码片段演示如何隐藏主要网格线。隐藏主要网格线后，工作表将添加一个没有网格线的柱状图。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **更改主要网格线设置**
开发人员不仅可以控制主要网格线的可见性，还可以控制其他属性，包括颜色等。

以下代码片段演示如何更改主要网格线的颜色。设置主要网格线的颜色后，工作表将添加一个具有修改网格线的柱状图。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **高级主题**
- [设置图表系列的值格式代码](/cells/zh/net/set-the-values-format-code-of-chart-series/)
- [在图表中将图片设置为背景填充](/cells/zh/net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="csharp" >}}
