---
title: 使用 ChartGlobalizationSettings 类为图表组件设置不同的语言
type: docs
weight: 2200
url: /zh/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **可能的使用场景**

Aspose.Cells API暴露了[**图表全球化设置**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)类以处理用户希望将图表组件设置为不同语言的场景。电子表格中小计的自定义标签。

##  **ChartGlobalizationSettings 类介绍**

这[**图表全球化设置**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)类目前提供以下 8 种方法，可以在自定义类中重写这些方法，以将 AxisTitle 名称、AxisUnit 名称、ChartTitle 名称等翻译成不同的语言。
1. [**获取轴标题名称**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/)获取坐标轴的标题名称。
1. [**获取轴单位名称**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/)：获取轴单位的名称。
1. [**获取图表标题名称**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/)：获取图表标题的名称。
1. [**获取图例减少名称**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/)获取 Legend 的 Decrease 名称。
1. [**获取图例增量名称**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/)：获取Legend增加的名称。
1. [**获取图例总数**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/)获取 Total for Legend 的名称。
1. [**获取其他名称**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/)获取图表“其他”标签的名称。
1. [**获取系列名称**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/)：获取图表中Series的名称。

###  **自定义语言翻译**
在这里，我们将根据以下数据创建一个瀑布图。图表组件的名称将在图表中以英文显示。我们将使用土耳其语示例来展示如何以土耳其语显示图表标题、图例增加/减少名称、总计名称和轴标题。

![待办事项：image_alt_text](sample.png)

##  **示例代码**
下面的示例代码加载[示例 Excel 文件](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
