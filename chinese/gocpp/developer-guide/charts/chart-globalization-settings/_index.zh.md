---
title: 使用 ChartGlobalizationSettings 类通过 Golang 和 C++ 设置图表组件的不同语言
linktitle: 使用 ChartGlobalizationSettings 类
description: 学习如何在 Aspose.Cells for C++ 中使用 ChartGlobalizationSettings 类为图表组件设置不同的语言。我们的指南将帮助你理解如何将图表元素、标签和图例本地化成不同语言，以便以符合文化习惯的方式展现数据。
keywords: Aspose.Cells for C++，图表，全球化，语言，本地化，ChartGlobalizationSettings，元素，标签，图例。
type: docs
weight: 2200
url: /zh/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能的使用场景**

Aspose.Cells API 已经暴露了 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) 类，以处理用户希望将图表组件设置为不同语言的场景。电子表格中自定义小计的标签。 

## **ChartGlobalizationSettings类介绍**

 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) 类目前提供以下8个可被重写的方法，用于自定义类中实现如轴标题名、轴单位名、图表标题名等的不同语言翻译。

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/)：获取轴的标题名称。
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/)：获取轴单位的名称。
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/)：获取图表标题的名称。
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/)：获取图例减少的名称。
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/)：获取图例增加的名称。
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/)：获取图例的总名称。
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/)：获取图表中“其他”标签的名称。
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/)：获取图表中系列的名称。

### **自定义语言翻译**
在这里，我们将根据以下数据创建瀑布图。图表中将以英语显示图表组件的名称。我们将使用土耳其语示例来展示如何在图表中显示图表标题、图例增加/减少名称、总计名称和轴标题。

![todo:image_alt_text](sample.png)

## **示例代码**
以下示例代码加载了[示例Excel文件](waterfall.xlsx)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
