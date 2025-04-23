---
title: 设置图表外观
description: 学习如何在Aspose.Cells for Python via .NET中配置图表的外观。我们的指南将向你展示如何修改图表布局、颜色、字体和效果，以达成理想的视觉风格，提升你的工作表。
keywords: Aspose.Cells for Python via .NET，图表制作，图表外观，布局，颜色，字体，效果，工作表。
linktitle: 图表格式
type: docs
weight: 20
url: /zh/python-net/setting-chart-appearance/
---

## **设置图表外观**
在“如何创建图表”中，我们简要介绍了Aspose.Cells for Python via .NET提供的图表类型及图表对象，并描述了如何创建一个。本文将讨论如何通过设置其属性来自定义图表的外观：

- 设置图表区域。
- 设置图表线条。
- 应用主题。
- 为图表和轴设置标题。
- 使用网格线。
### **设置图表区域**
图表中有不同类型的区域，Aspose.Cells for Python via .NET提供了修改每个区域外观的灵活性。开发者可以通过改变前景色、背景色和填充格式等，对区域应用不同的格式设置。

在下面的示例中，我们在图表的不同区域应用了不同的格式设置。这些区域包括：

- 绘图区域
- 图表区域
- SeriesCollection区域
- SeriesCollection中单个点的区域

以下代码段演示了如何设置图表区域。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartArea-1.py" >}}

### **设置图表线条**
开发者还可以对[SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)的线条或数据标记应用不同的样式。下面的代码片段演示了如何使用Aspose.Cells for Python via .NET API设置图表线条。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartLines-1.py" >}}

### **将Microsoft Excel 2007/2010主题应用于图表**
开发者还可以对[SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)或其他图表对象应用不同的Microsoft Excel主题/颜色，如示例所示。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ApplyingThemes-1.py" >}}

### **设置图表或坐标轴的标题**
你可以使用Microsoft Excel在可视化环境中设置图表及其坐标轴的标题。Aspose.Cells for Python via .NET也允许开发者在运行时设置图表及其坐标轴的标题。所有图表及其坐标轴都包含一个[Chart.title](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/title)属性，可用于设置它们的标题，具体示例如下。

以下代码段演示了如何设置图表和轴的标题。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingTitlesAxes-1.py" >}}

### **使用主要网格线**
可以自定义主要网格线的外观。隐藏或显示网格线，或定义它们的颜色和其他设置。下面，我们展示如何隐藏网格线以及如何更改它们的颜色。

#### **隐藏主要网格线**
开发者可以通过设置[Line](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible)对象的[is_visible](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible)属性为**true**或**false**，控制主要网格线的显示。

以下代码片段演示如何隐藏主要网格线。隐藏主要网格线后，工作表将添加一个没有网格线的柱状图。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-MajorGridlines-1.py" >}}

#### **更改主要网格线设置**
开发人员不仅可以控制主要网格线的可见性，还可以控制其他属性，包括颜色等。

以下代码片段演示如何更改主要网格线的颜色。设置主要网格线的颜色后，工作表将添加一个具有修改网格线的柱状图。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ChangingMajorGridlines-1.py" >}}

## **高级主题**
- [设置图表系列的值格式代码](/cells/zh/python-net/set-the-values-format-code-of-chart-series/)
- [在图表中将图片设置为背景填充](/cells/zh/python-net/set-picture-as-background-fill-in-the-chart/)
