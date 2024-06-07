---
title: 使用ChartGlobalizationSettings类为图表组件设置不同语言 
description: 了解如何在Aspose.Cells for .NET中使用ChartGlobalizationSettings类来为图表组件设置不同语言。我们的指南将帮助您了解如何将图表元素、标签和图例本地化到不同的语言，使您能够以符合文化的方式展示数据。
keywords: Aspose.Cells for .NET，图表，图表全球化，语言，本地化，ChartGlobalizationSettings，元素，标签，图例。
type: docs
weight: 2200
url: /zh/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能的使用场景**

Aspose.Cells API已经暴露了[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)类，以处理用户希望将图表组件设置为不同语言的场景，例如在电子表格中为分项小计设置自定义标签。 

## **ChartGlobalizationSettings类简介**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)类目前提供了以下8个方法，可以在自定义类中重写这些方法，以将AxisTitle名称、AxisUnit名称、ChartTitle名称等翻译成不同的语言。
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/)：获取轴标题的名称。
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/)：获取轴单位的名称。
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/)：获取图表标题的名称。
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/)：获取图例的减少名称。
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/)：获取图例的增加名称。
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/)：获取图例的总计名称。
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/)：获取图表中"其他"标签的名称。
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/)：获取图表中系列的名称。

### **自定义语言翻译**
这里，我们将基于以下数据创建一个瀑布图。图表组件的名称将以英语显示在图表中。我们将使用土耳其语示例，以展示如何在土耳其语中显示图表标题、图例的增加/减少名称、总计名称和轴标题。

![todo:image_alt_text](sample.png)

## **示例代码**
以下示例代码加载了[示例Excel文件](waterfall.xlsx)。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## 由示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
