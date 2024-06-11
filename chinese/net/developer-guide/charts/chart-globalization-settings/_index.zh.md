---
title: 使用ChartGlobalizationSettings类设置图表组件的不同语言 
description: 学习如何在 Aspose.Cells for .NET 中使用 ChartGlobalizationSettings 类设置不同语言的图表组件。我们的指南将帮助您理解如何将图表元素、标签和图例本地化为不同语言，使您能够以符合文化习惯的方式呈现您的数据。
keywords: Aspose.Cells for .NET，图表制作，图表全球化，语言，本地化，ChartGlobalizationSettings，元素，标签，图例。
type: docs
weight: 2200
url: /zh/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能的使用场景**

Aspose.Cells API 已经暴露了 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) 类，以处理用户希望将图表组件设置为不同语言的场景。电子表格中自定义小计的标签。 

## **ChartGlobalizationSettings类介绍**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) 类目前提供以下8个方法，可以在自定义类中进行重写，以将轴标题名称、轴单位名称、图表标题名称等翻译成不同的语言。
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/)：获取轴的标题名称。
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/)：获取轴单位的名称。
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/)：获取图表标题的名称。
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/)：获取图例减少的名称。
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/)：获取图例增加的名称。
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/)：获取图例的总名称。
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/)：获取图表中“其他”标签的名称。
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/)：获取图表中系列的名称。

### **自定义语言翻译**
在这里，我们将根据以下数据创建瀑布图。图表中将以英语显示图表组件的名称。我们将使用土耳其语示例来展示如何在图表中显示图表标题、图例增加/减少名称、总计名称和轴标题。

![todo:image_alt_text](sample.png)

## **示例代码**
以下示例代码加载了[示例Excel文件](waterfall.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
