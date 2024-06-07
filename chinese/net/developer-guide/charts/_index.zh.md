---
title: 创建和管理图表
description: 了解如何使用Aspose.Cells for .NET在Microsoft Excel中创建图表。我们的指南将演示可以创建的不同类型的图表，以及如何自定义其外观和格式。
keywords: Aspose.Cells for .NET，图表创建，Microsoft Excel，图表类型，自定义，外观，格式。
linktitle: 图表
type: docs
weight: 130
url: /zh/net/creating-charts/
description: 在CSharp为Excel和ODS文件中创建图表。
keywords: 创建图表，绘制图形 
---

{{% alert color="primary" %}}

可以使用Aspose.Cells向电子表格添加多种图表。 Aspose.Cells提供许多灵活的图表对象。 本主题讨论了Aspose.Cells的图表对象。

{{% /alert %}}

## **创建图形**

### **简单创建图表**
使用以下示例代码简单创建Aspose.Cells图表：
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **创建图表的注意事项**

在创建图表之前，了解一些基本概念对于使用Aspose.Cells创建图表很有帮助。

#### **图表对象**

Aspose.Cells提供了[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)命名空间中一组特殊的类，用于创建Aspose.Cells支持的图表。 这些类用于创建**图表对象**，充当图表构建模块。 下面列出了图表对象:

- 系列，图表中的单个数据系列。
- 轴，图表的轴。
- 图表，一个Excel图表。
- ChartArea，工作表中的图表区域。
- ChartDataTable，图表数据表。
- ChartFrame，图表中的边框对象。
- ChartPoint，图表系列中的单个点。
- ChartPointCollection，包含一个系列中所有点的集合。
- Charts，Chart对象的集合。
- DataLabels，指定系列的所有DataLabel对象的集合。
- FillFormat，形状的填充格式。
- Floor，3D图表的底板。
- Legend，图表图例。
- Line，图表线条。
- SeriesCollection，Series对象的集合。
- TickLabels，与图表轴上刻度标签关联的刻度标签。
- Title，图表或轴的标题。
- Trendline，图表中的趋势线。
- TrendlineCollection，指定数据系列的所有趋势线对象的集合。
- Walls，3D图表的墙壁。

#### **使用图表对象**

如上所述，所有图表对象都是它们各自类的实例，并提供特定属性和方法来执行特定任务。使用图表对象创建图表。

使用[**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)集合将任何类型的图表添加到工作表。 [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)集合中的每个项目表示一个[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)对象。 [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)对象封装了所有其他用于自定义图表外观的图表对象。下一节将展示如何使用一些基本的图表对象创建一个简单的图表。

### **使用Aspose.Cells创建图表**

**步骤:**

1. 使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)对象的[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法向工作表单元格添加一些数据。
   这将用作图表的数据源。
1. 通过调用[**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)集合的[**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add)方法在工作表中添加一个图表，封装在[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)对象中。
1. 使用[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)枚举指定图表类型。
   例如，下面的示例将[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)值用作图表类型。
1. 通过传递索引从[**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)集合中获取新的[**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)对象。
1. 使用 [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) 封装的任何图表对象来管理图表。
   下面的示例使用 [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) 图表对象指定图表的数据源。

在向图表添加源数据时，数据源可以是一系列单元格（例如"A1:C3"），或者是一系列不相邻的单元格（例如"A1, A3, A5"），或者是一系列值（例如"1,2,3"）。

这些一般步骤允许您创建任何类型的图表。使用不同的图表对象来创建不同的图表。

利用 Aspose.Cells 可以创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表在名为 [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) 的枚举中预定义。

预定义的图表类型为：

|**图表类型**|**描述**|
| :- | :- |
|Column|表示分组柱状图|
|ColumnStacked|代表堆叠柱形图|
|Column100PercentStacked|代表百分比堆叠柱形图|
|Column3DClustered|代表3D分组柱形图|
|Column3DStacked|代表3D堆叠柱形图|
|Column3D100PercentStacked|代表3D百分比堆叠柱形图|
|Column3D|代表3D柱形图|
|Bar|代表分组条形图|
|BarStacked|代表堆叠条形图|
|Bar100PercentStacked|代表百分比堆叠条形图|
|Bar3DClustered|代表3D分组条形图|
|Bar3DStacked|代表3D堆叠条形图|
|Bar3D100PercentStacked|代表3D百分比堆叠条形图|
|Line|代表折线图|
|LineStacked|代表堆叠折线图|
|Line100PercentStacked|代表百分比堆叠折线图|
|LineWithDataMarkers|代表带数据标记的折线图|
|LineStackedWithDataMarkers|代表带数据标记的堆叠折线图|
|Line100PercentStackedWithDataMarkers|代表带数据标记的百分比堆叠折线图|
|Line3D|代表3D折线图|
|Pie|代表饼图|
|Pie3D|代表3D饼图|
|PiePie|代表饼状图的饼状图|
|PieExploded|代表分裂的饼图|
|Pie3DExploded|代表3D分裂的饼图|
|PieBar|代表饼图的柱状图|
|Scatter|代表散点图|
|ScatterConnectedByCurvesWithDataMarker|代表通过曲线连接的带数据标记的散点图|
|ScatterConnectedByCurvesWithoutDataMarker|代表通过曲线连接的不带数据标记的散点图|
|ScatterConnectedByLinesWithDataMarker|代表通过线段连接的带数据标记的散点图|
|ScatterConnectedByLinesWithoutDataMarker|代表通过线段连接的不带数据标记的散点图|
|Area|代表面积图表|
|AreaStacked|代表堆积面积图表|
|Area100PercentStacked|代表100%堆积面积图表|
|Area3D|代表3D面积图表|
|Area3DStacked|代表3D堆积面积图表|
|Area3D100PercentStacked|代表3D 100%堆积面积图表|
|Doughnut|代表环形图|
|DoughnutExploded|代表爆裂环形图|
|Radar|代表雷达图|
|RadarWithDataMarkers|代表带数据标记的雷达图|
|RadarFilled|代表填充雷达图|
|Surface3D|代表3D曲面图|
|SurfaceWireframe3D|代表线框3D曲面图|
|SurfaceContour|代表等高线图|
|SurfaceContourWireframe|代表线框等高线图|
|Bubble|代表气泡图|
|Bubble3D|代表3D气泡图|
|Cylinder|代表圆柱图|
|CylinderStacked|代表堆积圆柱图|
|Cylinder100PercentStacked|代表100%堆积圆柱图|
|CylindericalBar|代表圆柱条形图|
|CylindericalBarStacked|代表堆积圆柱条形图|
|CylindericalBar100PercentStacked|代表100%堆积圆柱条形图|
|CylindericalColumn3D|代表3D圆柱柱形图|
|Cone|代表圆锥图|
|ConeStacked|代表堆积圆锥图|
|Cone100PercentStacked|代表100%堆积圆锥图|
|ConicalBar|代表圆锥条形图|
|ConicalBarStacked|代表堆积圆锥条形图|
|ConicalBar100PercentStacked|代表100%堆积圆锥条形图|
|ConicalColumn3D|表示3D圆锥形柱状图|
|Pyramid|表示金字塔图|
|PyramidStacked|表示堆叠金字塔图|
|Pyramid100PercentStacked|表示百分比堆叠金字塔图|
|PyramidBar|表示金字塔柱状图|
|PyramidBarStacked|表示堆叠金字塔柱状图|
|PyramidBar100PercentStacked|表示百分比堆叠金字塔柱状图|
|PyramidColumn3D|表示3D金字塔柱状图|
{{% alert color="primary" %}}

当你将一组单元格指定为数据源时，只能设置从左上到右下的范围。 例如，"A1:C3" 是有效的，而"C3:A1" 是无效的。

{{% /alert %}}

#### **金字塔图**

当执行示例代码时，会在工作表中添加一个金字塔图表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **折线图**

在上面的示例中，简单地将[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)更改为*Line*会创建一条线图。完整源码如下。执行代码时，会在工作表中添加一个折线图。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **气泡图**

为了创建一个气泡图，必须将[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)设置为[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)，并设置一些额外的属性，如BubbleSizes，Values和XValues。 执行以下代码后，将在工作表中添加一个气泡图。

#### **带数据标记的折线图表**

要创建带数据标记的折线图表，[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)必须设置为*ChartType.LineWithDataMarkers*，并设置一些额外的属性，如背景区域，数据系列标记，Values和XValues。 在执行以下代码后，将在工作表中添加带数据标记的折线图表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **高级主题**
- [读取和操作 Excel 2016 图表](/cells/zh/net/read-and-manipulate-excel-2016-charts/)
- [管理Excel图表的轴](/cells/zh/net/chart-axes/)
- [设置图表外观](/cells/zh/net/setting-chart-appearance/)
- [图表类型](/cells/zh/net/chart-types/)
- [自定义图表](/cells/zh/net/customizing-charts/)
- [为图表设置数据源](/cells/zh/net/data-formatting-in-charts/)
- [管理 Excel 图表的数据标签](/cells/zh/net/insert-datalabels-to-chart/)
- [通过处理智能标记生成图表](/cells/zh/net/generate-chart-by-processing-smart-markers/)
- [获取图表的工作表](/cells/zh/net/get-worksheet-of-the-chart/)
- [管理 Excel 图表的图例](/cells/zh/net/chart-legend/)
- [操作位置大小和设计图表](/cells/zh/net/manipulate-position-size-and-designer-chart/)
- [使用引导线创建饼图](/cells/zh/net/creating-pie-chart-with-leader-lines/)
- [图表中的形状](/cells/zh/net/controls-in-charts/)
- [管理 Excel 图表的标题](/cells/zh/net/chart-and-axis-titles/)
- [图表渲染](/cells/zh/net/chart-rendering/)
- [获取图表趋势线的方程文本](/cells/zh/net/get-equation-text-of-chart-trendline/)
