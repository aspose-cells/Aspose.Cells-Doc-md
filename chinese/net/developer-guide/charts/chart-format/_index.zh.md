---
title: 设置图表外观
description: 了解如何配置图表的外观 Aspose.Cells for .NET。我们的指南将向您展示如何修改图表布局、颜色、字体和效果，以实现所需的视觉风格并增强您的工作表。
keywords: Aspose.Cells for .NET, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
linktitle: 图表格式
type: docs
weight: 20
url: /zh/net/setting-chart-appearance/
---
##  **设置图表外观**
在如何创建图表中，我们简要介绍了Aspose.Cells提供的图表类型和图表对象，并描述了如何创建图表。本文讨论如何通过设置图表属性来自定义图表的外观：

- 设置图表区域。
- 设置图表线。
- 应用主题。
- 设置图表和坐标轴的标题。
- 使用网格线。
###  **设置图表区域**
图表中有不同类型的区域，Aspose.Cells 提供了修改每个区域的外观的灵活性。开发人员可以通过更改前景色、背景色和填充格式等来对某个区域应用不同的格式设置。

在下面给出的示例中，我们在图表的不同类型区域应用了不同的格式设置。这些领域包括：

- 地块面积
- 图表区
- 系列收藏区
- SeriesCollection 中单个点的面积

以下代码片段演示了如何设置图表区域。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
###  **设置图表线**
开发人员还可以在线条或数据标记上应用不同类型的样式[系列合集](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)。以下代码片段演示了如何使用 Aspose.Cells API 设置图表线。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
###  **将 Microsoft Excel 2007/2010 主题应用于图表**
开发人员可以应用不同的 Microsoft Excel 主题/颜色[系列合集](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)或其他图表对象，如下例所示。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
###  **设置图表或轴的标题**
您可以使用 Microsoft Excel 在所见即所得环境中设置图表的标题及其轴。 Aspose.Cells 还允许开发人员在运行时设置图表的标题及其轴。所有图表及其轴都包含[标题](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)属性可用于设置其标题，如下面的示例所示。

以下代码片段演示了如何设置图表和坐标轴的标题。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
###  **使用主要网格线**
可以自定义主要网格线的外观。隐藏或显示网格线，或定义其颜色和其他设置。下面，我们展示如何隐藏网格线以及如何更改其颜色。
####  **隐藏主要网格线**
开发人员可以通过设置来控制主要网格线的可见性[可见](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible)的财产[线](https://reference.aspose.com/cells/net/aspose.cells.drawing/line)反对**真的**或*假**。

以下代码片段演示了如何隐藏主要网格线。隐藏主要网格线后，将添加到工作表中的柱形图将没有网格线。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
####  **更改主要网格线设置**
开发人员不仅可以控制主要网格线的可见性，还可以控制其他属性，包括其颜色等。

以下代码片段演示了如何更改主要网格线的颜色。设置主要网格线的颜色后，柱形图将添加到具有修改网格线的工作表中。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

##  **高级主题**
- [设置图表系列的数值格式代码](/cells/zh/net/set-the-values-format-code-of-chart-series/)
- [设置图片为背景填写图表](/cells/zh/net/set-picture-as-background-fill-in-the-chart/)
