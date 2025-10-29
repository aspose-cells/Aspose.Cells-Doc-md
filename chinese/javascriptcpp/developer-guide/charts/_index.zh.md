---
title: 用JavaScript通过C++创建和管理图表
linktitle: 图表
description: 学习如何使用Aspose.Cells for JavaScript via C++在微软Excel中创建图表。我们的指南将演示各种图表类型以及如何自定义其外观和格式。
keywords: Aspose.Cells for JavaScript通过C++，图表创建，微软Excel，图表类型，定制，外观，格式化。
type: docs
weight: 130
url: /zh/javascript-cpp/creating-charts/
---

{{% alert color="primary" %}}

使用Aspose.Cells可以向电子表格添加各种图表。 Aspose.Cells提供许多灵活的图表对象。 本主题讨论了Aspose.Cells的图表对象。

{{% /alert %}}

## **创建图表**

### **创建图表很简单**
使用以下示例代码轻松创建一个Aspose.Cells的图表：
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding sample values to cells
            worksheet.cells.get("A2").value = "Category1";
            worksheet.cells.get("A3").value = "Category2";
            worksheet.cells.get("A4").value = "Category3";

            worksheet.cells.get("B1").value = "Column1";
            worksheet.cells.get("B2").value = 4;
            worksheet.cells.get("B3").value = 20;
            worksheet.cells.get("B4").value = 50;

            worksheet.cells.get("C1").value = "Column2";
            worksheet.cells.get("C2").value = 50;
            worksheet.cells.get("C3").value = 100;
            worksheet.cells.get("C4").value = 150;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Setting chart data source as the range "A1:C4"
            chart.chartDataRange = { range: "A1:C4", isSeriesInRows: true };

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
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

使用 [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) 集合在工作表中添加任何类型的图表。每个 [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) 集合中的项代表一个 [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) 对象。[**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) 对象封装了所有必要的图表对象，以自定义图表的外观。下一节将介绍如何使用一些基本的图表对象创建简单的图表。

### **使用 Aspose.Cells 创建图表**



1. 使用 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/) 对象的 [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-) 方法向工作表单元添加数据。
   这将被用作图表的数据源。
2. 通过调用[**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)集合的[**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-)方法，将图表添加到工作表中，封装在[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/)对象中。
3. 使用[**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)枚举指定图表的类型。
   例如，下面的示例使用[**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype)值作为图表类型。
4. 通过传递索引，访问来自[**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection)集合的新[**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)对象。
5. 使用封装在[**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/)对象中的任何图表对象来管理图表。
   下例使用[**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/)图表对象指定图表的数据源。

向图表添加源数据时，数据源可以是单元格范围（例如“ A1：C3”），也可以是不连续单元格序列（例如“ A1，A3，A5”）或值序列（例如“ 1，2，3”）。

这些一般步骤可以帮助您创建任何类型的图表。使用不同的绘图对象创建不同的图表。

使用 Aspose.Cells 可以创建许多不同类型的图表。Aspose.Cells 支持的所有标准图表都预先定义在名为 [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) 的枚举中。

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

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Chart and Download</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Pyramid, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and chart added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **折线图**

在上面的示例中，只需将[**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)更改为*Line*即可创建折线图。完整源代码如下。当代码执行时，将在工作表中添加折线图。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Chart</title>
    </head>
    <body>
        <h1>Add Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **气泡图**

为了创建气泡图，必须将[**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)设置为[**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype)，并相应设置一些额外的属性，如BubbleSizes、Values和XValues。执行以下代码后，气泡图将添加到工作表中。

#### **带有数据标记的折线图**

为了创建带数据标记的折线图，必须将[**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/)设置为*ChartType.LineWithDataMarkers*，并相应设置一些额外的属性，如背景区域、系列标记、Values和XValues。执行以下代码后，带数据标记的折线图将添加到工作表中。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Line With Data Marker Chart</title>
    </head>
    <body>
        <h1>Line With Data Marker Chart Example</h1>
        <p>You may optionally select an existing Excel file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (fileInput.files.length === 0) {
                // Proceed with a new workbook if no file selected
            }

            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set columns title 
            worksheet.cells.get(0, 0).putValue("X");
            worksheet.cells.get(0, 1).putValue("Y");

            // Random data shall be used for generating the chart
            // Create random data and save in the cells
            for (let i = 1; i < 21; i++) {
                worksheet.cells.get(i, 0).putValue(i);
                worksheet.cells.get(i, 1).putValue(0.8);
            }

            for (let i = 21; i < 41; i++) {
                worksheet.cells.get(i, 0).putValue(i - 20);
                worksheet.cells.get(i, 1).putValue(0.9);
            }

            // Add a chart to the worksheet
            const idx = worksheet.charts.add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

            // Access the newly created chart
            const chart = worksheet.charts.get(idx);

            // Set chart style
            chart.style = 3;

            // Set autoscaling value to true
            chart.autoScaling = true;

            // Set foreground color white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set Properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set Properties of categoryaxis title
            chart.categoryAxis.title.text = "Units";

            //Set Properties of nseries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set IsColorVaried to true for varied points color
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers
            const series2 = chart.nSeries.get(s2_idx);
            series2.area.formatting = AsposeCells.FormattingType.Custom;
            series2.marker.area.foregroundColor = AsposeCells.Color.Yellow;
            series2.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series2.xValues = "A2:A21";
            series2.values = "B2:B21";

            // Set properties of background area and series markers for series3
            const series3 = chart.nSeries.get(s3_idx);
            series3.area.formatting = AsposeCells.FormattingType.Custom;
            series3.marker.area.foregroundColor = AsposeCells.Color.Green;
            series3.marker.border.isVisible = false;

            // Set X and Y values of series chart
            series3.xValues = "A22:A41";
            series3.values = "B22:B41";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'LineWithDataMarkerChart.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [读取和操作Excel 2016图表](/cells/zh/javascript-cpp/read-and-manipulate-excel-2016-charts/)
- [管理Excel图表的坐标轴](/cells/zh/javascript-cpp/chart-axes/)
- [设置图表外观](/cells/zh/javascript-cpp/setting-chart-appearance/)
- [图表类型](/cells/zh/javascript-cpp/chart-types/)
- [自定义图表](/cells/zh/javascript-cpp/customizing-charts/)
- [为图表设置数据源](/cells/zh/javascript-cpp/data-formatting-in-charts/)
- [管理Excel图表的数据标签](/cells/zh/javascript-cpp/insert-datalabels-to-chart/)
- [获取图表的工作表](/cells/zh/javascript-cpp/get-worksheet-of-the-chart/)
- [管理Excel图表的图例](/cells/zh/javascript-cpp/chart-legend/)
- [操纵位置大小和设计者图表](/cells/zh/javascript-cpp/manipulate-position-size-and-designer-chart/)
- [使用带有引线的饼图](/cells/zh/javascript-cpp/creating-pie-chart-with-leader-lines/)
- [图表中的形状](/cells/zh/javascript-cpp/controls-in-charts/)
- [管理Excel图表的标题](/cells/zh/javascript-cpp/chart-and-axis-titles/)
- [图表渲染](/cells/zh/javascript-cpp/chart-rendering/)
- [获取图表趋势线的方程文本](/cells/zh/javascript-cpp/get-equation-text-of-chart-trendline/)
