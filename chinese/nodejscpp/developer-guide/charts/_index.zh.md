---
title: 用Node.js via C++创建和管理图表
linktitle: 图表
description: 学习如何使用Aspose.Cells for Node.js在Microsoft Excel中创建图表。我们的指南将展示各种图表类型以及如何自定义其外观和格式。
keywords: Aspose.Cells for Node.js，图表创建，Microsoft Excel，图表类型，自定义，外观，格式设置。
type: docs
weight: 130
url: /zh/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

使用Aspose.Cells可以向电子表格添加各种图表。 Aspose.Cells提供许多灵活的图表对象。 本主题讨论了Aspose.Cells的图表对象。

{{% /alert %}}

## **创建图表**

### **创建图表很简单**
使用以下示例代码轻松创建一个Aspose.Cells的图表：
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **创建图表的要点**

在创建图表之前，理解一些基本概念很有帮助，尤其是在使用Aspose.Cells创建图表时。

#### **图表对象**

以下列出图表对象：

- Series，图表中的单个数据系列。
- Axis，图表的坐标轴。
- Chart，单个Excel图表。
- ChartArea，工作表中的图表区域。
- ChartDataTable，图表数据表。
- ChartFrame，图表中的框架对象。
- ChartPoint，图表中系列中的单个点。
- ChartPointCollection，包含一个系列中所有点的集合。
- Charts，Chart对象的集合。
- DataLabels，指定系列的所有DataLabel对象的集合。
- FillFormat，形状的填充格式。
- Floor，3D图表的底板。
- Legend，图表图例。
- Line，图表线条。
- SeriesCollection，Series对象的集合。
- TickLabels，与图表轴上的刻度标记相关联的刻度标签。
- Title，图表或坐标轴的标题。
- Trendline，图表中的趋势线。
- TrendlineCollection, 指定数据系列的所有趋势线对象的集合。
- Walls, 3D 图表的墙壁。

#### **使用图表对象**

如上所述，所有的图表对象都是它们各自类的实例，并提供特定的属性和方法来执行特定的任务。使用图表对象来创建图表。

使用 [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) 集合在工作表中添加任何类型的图表。每个 [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) 集合中的项代表一个 [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) 对象。[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) 对象封装了所有必要的图表对象，以自定义图表的外观。下一节将介绍如何使用一些基本的图表对象创建简单的图表。

### **使用 Aspose.Cells 创建图表**

**步骤:**

1. 使用 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/) 对象的 [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-) 方法向工作表单元添加数据。
   这将被用作图表的数据源。
1. 通过调用 [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection) 集合的 [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-) 方法，将图表添加到工作表中，封装在 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) 对象内。
1. 通过 [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) 枚举指定图表类型。
   例如，下面的示例使用[**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype)值作为图表类型。
1. 通过传递索引，从[**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection)集合中访问新的[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)对象。
1. 使用封装在[**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/)对象中的任何图表对象来管理图表。
   下例使用[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/)图表对象指定图表的数据源。

向图表添加源数据时，数据源可以是单元格范围（例如“ A1：C3”），也可以是不连续单元格序列（例如“ A1，A3，A5”）或值序列（例如“ 1，2，3”）。

这些一般步骤可以帮助您创建任何类型的图表。使用不同的绘图对象创建不同的图表。

使用 Aspose.Cells 可以创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表都预先定义在名为 [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) 的枚举中。

预定义的图表类型包括：

|**图表类型**|**描述**|
| :- | :- |
|Column| 表示簇状柱形图表|
|ColumnStacked|代表堆积柱状图
|Column100PercentStacked|代表100%堆积柱状图
|Column3DClustered|代表3D分组柱状图
|Column3DStacked|表示3D堆叠柱形图|
|Column3D100PercentStacked|表示3D 100%堆叠柱形图|
|Column3D|表示3D柱形图|
|Bar|表示分组条形图|
|BarStacked|表示堆叠条形图|
|Bar100PercentStacked|表示100%堆叠条形图|
|Bar3DClustered|表示3D分组条形图|
|Bar3DStacked|表示3D堆叠条形图|
|Bar3D100PercentStacked|表示3D 100%堆叠条形图|
|Line|表示折线图|
|LineStacked|表示堆叠折线图|
|Line100PercentStacked|表示100%堆叠折线图|
|LineWithDataMarkers|表示带有数据标记的折线图|
|LineStackedWithDataMarkers|表示带有数据标记的堆叠折线图|
|Line100PercentStackedWithDataMarkers|表示带有数据标记的100%堆叠折线图|
|Line3D|表示3D折线图|
|Pie|表示饼图|
|Pie3D|表示3D饼图|
|PiePie|表示饼图中的饼图|
|PieExploded|表示爆炸饼图|
|Pie3DExploded|表示3D饼图(爆炸式)|
|PieBar|表示饼图的条形图|
|Scatter|代表散点图
|ScatterConnectedByCurvesWithDataMarker|代表用曲线连接的散点图，带有数据标记
|ScatterConnectedByCurvesWithoutDataMarker|代表用曲线连接的散点图，没有数据标记
|ScatterConnectedByLinesWithDataMarker|代表用线连接的散点图，带有数据标记
|ScatterConnectedByLinesWithoutDataMarker|代表用线连接的散点图，没有数据标记
|Area|表示面积图|
|AreaStacked|表示堆叠面积图|
|Area100PercentStacked|表示百分比堆叠面积图|
|Area3D|表示3D面积图|
|Area3DStacked|表示3D堆叠面积图|
|Area3D100PercentStacked|表示3D百分比堆叠面积图|
|Doughnut|表示圆环图|
|DoughnutExploded|表示爆炸式环形图|
|Radar|代表雷达图
|RadarWithDataMarkers|代表带有数据标记的雷达图
|RadarFilled|表示填充雷达图|
|Surface3D|表示3D曲面图|
|SurfaceWireframe3D|代表三维线框表面图表|
|SurfaceContour|表示等高线图表|
|SurfaceContourWireframe|表示线框等高线图表|
|Bubble|表示气泡图表|
|Bubble3D|表示3D气泡图表|
|Cylinder|表示圆柱图表|
|CylinderStacked|表示堆叠圆柱图表|
|Cylinder100PercentStacked|表示100%堆叠圆柱图表|
|CylindericalBar|代表圆柱棒图表|
|CylindericalBarStacked|代表堆叠圆柱棒图表|
|CylindericalBar100PercentStacked|代表百分比堆叠圆柱棒图表|
|CylindericalColumn3D|代表3D圆柱柱状图表|
|Cone|表示圆锥图表|
|ConeStacked|表示堆叠圆锥图表|
|Cone100PercentStacked|表示100%堆叠圆锥图表|
|ConicalBar|表示圆锥形条形图|
|ConicalBarStacked|表示堆叠圆锥形条形图|
|ConicalBar100PercentStacked|表示100%堆叠圆锥形条形图|
|ConicalColumn3D|表示3D圆锥形柱形图|
|Pyramid|表示金字塔图表|
|PyramidStacked|表示堆叠金字塔图表|
|Pyramid100PercentStacked|代表100%的堆叠金字塔图表|
|PyramidBar|代表金字塔柱状图|
|PyramidBarStacked|代表堆叠金字塔柱状图|
|PyramidBar100PercentStacked|代表100%堆叠金字塔柱状图|
|PyramidColumn3D|代表3D金字塔柱图|
{{% alert color="primary" %}}

当您将一系列单元格指定为数据源时，只能从左上到右下设置范围。例如，“A1:C3”是有效的，而“C3:A1”是无效的。

{{% /alert %}}

#### **金字塔图**

执行示例代码后，将在工作表中添加一个金字塔图表。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **折线图**

在上面的示例中，只需将[**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)更改为*Line*即可创建折线图。完整源代码如下。当代码执行时，将在工作表中添加折线图。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **气泡图**

为了创建气泡图，必须将[**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)设置为[**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype)，并相应设置一些额外的属性，如BubbleSizes、Values和XValues。执行以下代码后，气泡图将添加到工作表中。

#### **带有数据标记的折线图**

为了创建带数据标记的折线图，必须将[**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/)设置为*ChartType.LineWithDataMarkers*，并相应设置一些额外的属性，如背景区域、系列标记、Values和XValues。执行以下代码后，带数据标记的折线图将添加到工作表中。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **高级主题**
- [读取和操作Excel 2016图表](/cells/zh/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [管理Excel图表的坐标轴](/cells/zh/nodejs-cpp/chart-axes/)
- [设置图表外观](/cells/zh/nodejs-cpp/setting-chart-appearance/)
- [图表类型](/cells/zh/nodejs-cpp/chart-types/)
- [自定义图表](/cells/zh/nodejs-cpp/customizing-charts/)
- [为图表设置数据源](/cells/zh/nodejs-cpp/data-formatting-in-charts/)
- [管理Excel图表的数据标签](/cells/zh/nodejs-cpp/insert-datalabels-to-chart/)
- [获取图表的工作表](/cells/zh/nodejs-cpp/get-worksheet-of-the-chart/)
- [管理Excel图表的图例](/cells/zh/nodejs-cpp/chart-legend/)
- [操纵位置大小和设计者图表](/cells/zh/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [使用带有引线的饼图](/cells/zh/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [图表中的形状](/cells/zh/nodejs-cpp/controls-in-charts/)
- [管理Excel图表的标题](/cells/zh/nodejs-cpp/chart-and-axis-titles/)
- [图表渲染](/cells/zh/nodejs-cpp/chart-rendering/)
- [获取图表趋势线的方程文本](/cells/zh/nodejs-cpp/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="nodejs-cpp" >}}
