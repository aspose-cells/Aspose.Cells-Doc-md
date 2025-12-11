---  
title: Create and Manage Chart with JavaScript via C++  
linktitle: Charts  
description: Learn how to use Aspose.Cells for JavaScript via C++ to create charts in Microsoft Excel. Our guide will demonstrate various chart types and how to customize their appearance and formatting.  
keywords: Aspose.Cells for JavaScript via C++, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.  
type: docs  
weight: 130  
url: /javascript-cpp/creating-charts/  
---  

{{% alert color="primary" %}}  

It is possible to add a variety of charts to spreadsheets with Aspose.Cells. Aspose.Cells provides many flexible charting objects. This topic discusses Aspose.Cells' charting objects.  

{{% /alert %}}  

## **Creating Charts**  

### **Simply Creating a Chart**  
It is simple to create a chart with Aspose.Cells with the following example code:  
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

### **Things to Know for Creating a Chart**  

Before creating charts, it is important to understand some basic concepts that are helpful when creating charts using Aspose.Cells.  

#### **Charting Objects**  

The charting objects are listed below:  

- Series, a single data series in a chart.  
- Axis, a chart's axis.  
- Chart, a single Excel chart.  
- ChartArea, the chart area in the worksheet.  
- ChartDataTable, a chart data table.  
- ChartFrame, the frame object in a chart.  
- ChartPoint, a single point in a series in a chart.  
- ChartPointCollection, a collection that contains all the points in one series.  
- Charts, a collection of Chart objects.  
- DataLabels, a collection of all the DataLabel objects for the specified series.  
- FillFormat, fill format for a shape.  
- Floor, the floor of a 3D chart.  
- Legend, the chart legend.  
- Line, the chart line.  
- SeriesCollection, a collection of Series objects.  
- TickLabels, the tick mark labels associated with tick marks on a chart axis.  
- Title, the title of a chart or axis.  
- Trendline, a trendline in a chart.  
- TrendlineCollection, a collection of all Trendline objects for the specified data series.  
- Walls, the walls of a 3D chart.  

#### **Using Charting Objects**  

As mentioned above, all charting objects are instances of their respective classes and provide specific properties and methods to perform specific tasks. Use charting objects to create charts.  

Add any type of chart to a worksheet using the [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) collection. Each item in the [**charts**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#charts--) collection represents a [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) object. A [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) object encapsulates all other charting objects required to customize the appearance of the chart. The next section shows how to use a few basic charting objects to create a simple chart.  

### **Create Chart Using Aspose.Cells**  

1. Add some data to worksheet cells with the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell/) object's [**putValue(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-string-) method. This will be used as the data source for the chart.  
2. Add a chart to the worksheet by calling the [**ChartCollection**](https://reference.aspose.com/cells/javascript-cpp/chartcollection) collection's [**add**](https://reference.aspose.com/cells/javascript-cpp/chartcollection/#add-charttype-number-number-number-number-) method, encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) object.  
3. Specify the type of chart with the [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) enumeration. For example, the example below uses the [**ChartType.Pyramid**](https://reference.aspose.com/cells/javascript-cpp/charttype) value as the chart type.  
4. Access the new [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) object from the [**Charts**](https://reference.aspose.com/cells/javascript-cpp/chartcollection) collection by passing its index.  
5. Use any of the charting objects encapsulated in the [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart/) object to manage the chart. The example below uses the [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection/) charting object to specify the chart's data source.  

When adding source data to the chart, the data source can be a range of cells (such as "A1:C3"), a sequence of non‑contiguous cells (such as "A1, A3, A5"), or a sequence of values (such as "1,2,3").  

These general steps allow you to create any type of chart. Use different charting objects to create different charts.  

It is possible to create many different types of charts with Aspose.Cells. All standard charts supported by Aspose.Cells are pre‑defined in an enumeration named [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/).  

The pre‑defined chart types are:  

|**Chart Types**|**Description**|
| :- | :- |
|Column|Represents Clustered Column Chart|
|ColumnStacked|Represents Stacked Column Chart|
|Column100PercentStacked|Represents 100% Stacked Column Chart|
|Column3DClustered|Represents 3D Clustered Column Chart|
|Column3DStacked|Represents 3D Stacked Column Chart|
|Column3D100PercentStacked|Represents 3D 100% Stacked Column Chart|
|Column3D|Represents 3D Column Chart|
|Bar|Represents Clustered Bar Chart|
|BarStacked|Represents Stacked Bar Chart|
|Bar100PercentStacked|Represents 100% Stacked Bar Chart|
|Bar3DClustered|Represents 3D Clustered Bar Chart|
|Bar3DStacked|Represents 3D Stacked Bar Chart|
|Bar3D100PercentStacked|Represents 3D 100% Stacked Bar Chart|
|Line|Represents Line Chart|
|LineStacked|Represents Stacked Line Chart|
|Line100PercentStacked|Represents 100% Stacked Line Chart|
|LineWithDataMarkers|Represents Line Chart with data markers|
|LineStackedWithDataMarkers|Represents Stacked Line Chart with data markers|
|Line100PercentStackedWithDataMarkers|Represents 100% Stacked Line Chart with data markers|
|Line3D|Represents 3D Line Chart|
|Pie|Represents Pie Chart|
|Pie3D|Represents 3D Pie Chart|
|PiePie|Represents Pie of Pie Chart|
|PieExploded|Represents Exploded Pie Chart|
|Pie3DExploded|Represents 3D Exploded Pie Chart|
|PieBar|Represents Bar of Pie Chart|
|Scatter|Represents Scatter Chart|
|ScatterConnectedByCurvesWithDataMarker|Represents Scatter Chart connected by curves, with data markers|
|ScatterConnectedByCurvesWithoutDataMarker|Represents Scatter Chart connected by curves, without data markers|
|ScatterConnectedByLinesWithDataMarker|Represents Scatter Chart connected by lines, with data markers|
|ScatterConnectedByLinesWithoutDataMarker|Represents Scatter Chart connected by lines, without data markers|
|Area|Represents Area Chart|
|AreaStacked|Represents Stacked Area Chart|
|Area100PercentStacked|Represents 100% Stacked Area Chart|
|Area3D|Represents 3D Area Chart|
|Area3DStacked|Represents 3D Stacked Area Chart|
|Area3D100PercentStacked|Represents 3D 100% Stacked Area Chart|
|Doughnut|Represents Doughnut Chart|
|DoughnutExploded|Represents Exploded Doughnut Chart|
|Radar|Represents Radar Chart|
|RadarWithDataMarkers|Represents Radar Chart with data markers|
|RadarFilled|Represents Filled Radar Chart|
|Surface3D|Represents 3D Surface Chart|
|SurfaceWireframe3D|Represents Wireframe 3D Surface Chart|
|SurfaceContour|Represents Contour Chart|
|SurfaceContourWireframe|Represents Wireframe Contour Chart|
|Bubble|Represents Bubble Chart|
|Bubble3D|Represents 3D Bubble Chart|
|Cylinder|Represents Cylinder Chart|
|CylinderStacked|Represents Stacked Cylinder Chart|
|Cylinder100PercentStacked|Represents 100% Stacked Cylinder Chart|
|CylindricalBar|Represents Cylindrical Bar Chart.|
|CylindricalBarStacked|Represents Stacked Cylindrical Bar Chart|
|CylindricalBar100PercentStacked|Represents 100% Stacked Cylindrical Bar Chart|
|CylindricalColumn3D|Represents 3D Cylindrical Column Chart|
|Cone|Represents Cone Chart|
|ConeStacked|Represents Stacked Cone Chart|
|Cone100PercentStacked|Represents 100% Stacked Cone Chart|
|ConicalBar|Represents Conical Bar Chart|
|ConicalBarStacked|Represents Stacked Conical Bar Chart|
|ConicalBar100PercentStacked|Represents 100% Stacked Conical Bar Chart|
|ConicalColumn3D|Represents 3D Conical Column Chart|
|Pyramid|Represents Pyramid Chart|
|PyramidStacked|Represents Stacked Pyramid Chart|
|Pyramid100PercentStacked|Represents 100% Stacked Pyramid Chart|
|PyramidBar|Represents Pyramid Bar Chart|
|PyramidBarStacked|Represents Stacked Pyramid Bar Chart|
|PyramidBar100PercentStacked|Represents 100% Stacked Pyramid Bar Chart|
|PyramidColumn3D|Represents 3D Pyramid Column Chart|

{{% alert color="primary" %}}  

When you assign a range of cells as the data source, you can only set the range from top left to bottom right. For example, "A1:C3" is valid while "C3:A1" is invalid.  

{{% /alert %}}  

#### **Pyramid Chart**  

When the example code is executed, a pyramid chart is added to the worksheet.  

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

#### **Line Chart**  

In the above example, simply changing the [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) to *Line* creates a line chart. The complete source is provided below. **When** the code is executed, a line chart is added to the worksheet.  

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

#### **Bubble Chart**  

In order to create a bubble chart, the [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) has to be set to [**ChartType.Bubble**](https://reference.aspose.com/cells/javascript-cpp/charttype) and a few extra properties such as BubbleSizes, Values, and XValues need to be set accordingly. Upon executing the following code, a bubble chart is added to the worksheet.  

#### **Line with Data Marker Chart**  

In order to create a line with the data marker chart, [**ChartType**](https://reference.aspose.com/cells/javascript-cpp/charttype/) has to be set to *ChartType.LineWithDataMarkers* and a few extra properties such as background area, series markers, values, and XValues need to be set accordingly. Upon executing the following code, a line with the data marker chart is added to the worksheet.  

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

            // Set foreground color to white
            chart.plotArea.area.foregroundColor = AsposeCells.Color.White;

            // Set properties of chart title
            chart.title.text = "Sample Chart";

            // Set chart type
            chart.type = AsposeCells.ChartType.LineWithDataMarkers;

            // Set properties of category axis title
            chart.categoryAxis.title.text = "Units";

            // Set properties of nSeries
            const s2_idx = chart.nSeries.add("A2:A2", true);
            const s3_idx = chart.nSeries.add("A22:A22", true);

            // Set isColorVaried to true for varied point colors
            chart.nSeries.isColorVaried = true;

            // Set properties of background area and series markers for series2
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

## **Advanced topics**  
- [Read and Manipulate Excel 2016 Charts](/cells/javascript-cpp/read-and-manipulate-excel-2016-charts/)  
- [Manage Axes of Excel Charts](/cells/javascript-cpp/chart-axes/)  
- [Setting Chart Appearance](/cells/javascript-cpp/setting-chart-appearance/)  
- [Chart Types](/cells/javascript-cpp/chart-types/)  
- [Customizing Charts](/cells/javascript-cpp/customizing-charts/)  
- [Set Data source for the chart](/cells/javascript-cpp/data-formatting-in-charts/)  
- [Manage DataLabels of Excel Charts](/cells/javascript-cpp/insert-datalabels-to-chart/)  
- [Get Worksheet of the Chart](/cells/javascript-cpp/get-worksheet-of-the-chart/)  
- [Manage Legend of Excel Charts](/cells/javascript-cpp/chart-legend/)  
- [Manipulate Position Size and Designer Chart](/cells/javascript-cpp/manipulate-position-size-and-designer-chart/)  
- [Creating Pie Chart with Leader Lines](/cells/javascript-cpp/creating-pie-chart-with-leader-lines/)  
- [Shapes in Charts](/cells/javascript-cpp/controls-in-charts/)  
- [Manage Titles of Excel Charts](/cells/javascript-cpp/chart-and-axis-titles/)  
- [Chart Rendering](/cells/javascript-cpp/chart-rendering/)  
- [Get Equation Text of Chart Trendline](/cells/javascript-cpp/get-equation-text-of-chart-trendline/)  