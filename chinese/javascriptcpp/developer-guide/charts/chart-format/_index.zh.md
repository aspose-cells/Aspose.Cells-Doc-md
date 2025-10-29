---
title: 使用C++通过JavaScript设置图表外观
description: 了解如何在Aspose.Cells for Java脚本通过C++中配置图表的外观。我们的指南将向你展示如何修改图表布局、颜色、字体和效果，以实现理想的视觉风格，并增强你的工作表。
keywords: Aspose.Cells for Java脚本通过C++，绘图，图表外观，布局，颜色，字体，效果，工作表。
linktitle: 图表格式
type: docs
weight: 20
url: /zh/javascript-cpp/setting-chart-appearance/
---

## **设置图表外观**
在《如何创建图表》中，我们简要介绍了Aspose.Cells提供的图表类型和图表对象，并描述了如何创建一个图表。本文讨论了如何通过设置图表属性来自定义图表的外观：

- 设置图表区域。
- 设置图表线条。
- 应用主题。
- 为图表和轴设置标题。
- 使用网格线。

### **设置图表区域**
图表中有不同类型的区域，Aspose.Cells提供了修改每个区域外观的灵活性。开发人员可以通过改变前景色、背景色和填充格式等设置，在一个区域上应用不同的格式设置。

在下面的示例中，我们在图表的不同区域应用了不同的格式设置。这些区域包括：

- 绘图区域
- 图表区域
- SeriesCollection区域
- SeriesCollection中单个点的区域

以下代码段演示了如何设置图表区域。

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
            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 60;
            worksheet.cells.get("B2").value = 32;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = new AsposeCells.Color(0, 0, 255);

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = new AsposeCells.Color(255, 255, 0);

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(255, 0, 0);

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = new AsposeCells.Color(0, 255, 255);

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **设置图表线条**
开发者还可以对[SeriesCollection](https://reference.aspose.com/cells/javascript-cpp/seriescollection/)中的线条或数据标记应用不同类型的样式。以下代码片段演示了如何使用Aspose.Cells API设置图表线条。

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Applying a dotted line style on the lines of a SeriesCollection
            chart.nSeries.get(0).border.style = AsposeCells.LineType.Dot;

            // Applying a triangular marker style on the data markers of a SeriesCollection
            chart.nSeries.get(0).marker.markerStyle = AsposeCells.ChartMarkerType.Triangle;

            // Setting the weight of all lines in a SeriesCollection to medium
            chart.nSeries.get(1).border.weight = AsposeCells.WeightType.MediumLine;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **将Microsoft Excel 2007/2010主题应用于图表**
开发者可以将不同的Microsoft Excel主题/颜色应用于[SeriesCollection](https://reference.aspose.com/cells/javascript-cpp/seriescollection/)或其他图表对象，如下面的示例所示。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Chart Series Fill Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FillType, ThemeColor, ThemeColorType } = AsposeCells;

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

            // Loads the workbook containing the chart
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the first chart in the sheet
            const chart = worksheet.charts.get(0);

            // Specify the FillFormat's type to Solid Fill of the first series
            const series = chart.nSeries.get(0);
            series.area.fillFormat.fillType = FillType.Solid;

            // Get the CellsColor of SolidFill
            const cc = series.area.fillFormat.solidFill.cellsColor;

            // Create a theme in Accent style
            cc.themeColor = new ThemeColor(ThemeColorType.Accent6, 0.6);

            // Apply the theme to the series
            series.area.fillFormat.solidFill.cellsColor = cc;

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart series fill updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **设置图表或坐标轴的标题**
你可以使用Microsoft Excel在WYSIWYG环境中设置图表及其轴的标题。Aspose.Cells还允许开发者在运行时设置图表及其轴的标题。所有图表及其轴都包含一个[Title](https://reference.aspose.com/cells/javascript-cpp/title/)属性，可以用来设置它们的标题，如下示例所示。

以下代码片段演示了如何为图表和轴设置标题。

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
        const { Workbook, SaveFormat, ChartType, GradientStyleType, Color } = AsposeCells;

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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [Color.Lime, 1, GradientStyleType.Horizontal, 1];

            // Setting the title of a chart
            chart.title.text = "Title";

            // Setting the font color of the chart title to blue
            chart.title.font.color = Color.Blue;

            // Setting the title of category axis of the chart
            chart.categoryAxis.title.text = "Category";

            // Setting the title of value axis of the chart
            chart.valueAxis.title.text = "Value";

            // Saving the Excel file and creating a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **使用主要网格线**
可以自定义主要网格线的外观。隐藏或显示网格线，或定义它们的颜色和其他设置。下面，我们展示如何隐藏网格线以及如何更改它们的颜色。

#### **隐藏主要网格线**
开发者可以通过设置[Line](https://reference.aspose.com/cells/javascript-cpp/line/)对象的[isVisible()](https://reference.aspose.com/cells/javascript-cpp/line/#isVisible--)属性，将主网格线的可见性控制为**true**或**false**。

 以下代码演示了如何隐藏主网格线。隐藏主网格线后，工作表将添加一个柱状图并且没有网格线。

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").putValue(50);
            worksheet.cells.get("A2").putValue(100);
            worksheet.cells.get("A3").putValue(150);
            worksheet.cells.get("B1").putValue(60);
            worksheet.cells.get("B2").putValue(32);
            worksheet.cells.get("B3").putValue(50);

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Setting the foreground color of the plot area
            chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

            // Setting the foreground color of the chart area
            chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the foreground color of the 1st SeriesCollection area
            chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

            // Setting the foreground color of the area of the 1st SeriesCollection point
            chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

            // Filling the area of the 2nd SeriesCollection with a gradient
            chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

            // Hiding the major gridlines of Category Axis
            chart.categoryAxis.majorGridLines.isVisible = false;

            // Hiding the major gridlines of Value Axis
            chart.valueAxis.majorGridLines.isVisible = false;

            // Saving the Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **更改主要网格线设置**
开发人员不仅可以控制主要网格线的可见性，还可以控制其他属性，包括颜色等。

 以下代码演示了如何更改主网格线的颜色。设置主网格线颜色后，工作表中将添加一个具有修改后网格线的柱状图。

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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Creating a new Workbook object
                const workbook = new Workbook();

                // Adding a new worksheet to the Workbook object
                const sheetIndex = workbook.worksheets.add();

                // Obtaining the reference of the newly added worksheet by passing its sheet index
                const worksheet = workbook.worksheets.get(sheetIndex);

                // Adding sample values to cells
                worksheet.cells.get("A1").value = 50;
                worksheet.cells.get("A2").value = 100;
                worksheet.cells.get("A3").value = 150;
                worksheet.cells.get("B1").value = 60;
                worksheet.cells.get("B2").value = 32;
                worksheet.cells.get("B3").value = 50;

                // Adding a chart to the worksheet
                const chartIndex = worksheet.charts.add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

                // Accessing the instance of the newly added chart
                const chart = worksheet.charts.get(chartIndex);

                // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
                chart.nSeries.add("A1:B3", true);

                // Setting the foreground color of the plot area
                chart.plotArea.area.foregroundColor = AsposeCells.Color.Blue;

                // Setting the foreground color of the chart area
                chart.chartArea.area.foregroundColor = AsposeCells.Color.Yellow;

                // Setting the foreground color of the 1st SeriesCollection area
                chart.nSeries.get(0).area.foregroundColor = AsposeCells.Color.Red;

                // Setting the foreground color of the area of the 1st SeriesCollection point
                chart.nSeries.get(0).points.get(0).area.foregroundColor = AsposeCells.Color.Cyan;

                // Filling the area of the 2nd SeriesCollection with a gradient
                chart.nSeries.get(1).area.fillFormat.oneColorGradient = [AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1];

                // Setting the color of Category Axis' major gridlines to silver
                chart.categoryAxis.majorGridLines.color = AsposeCells.Color.Silver;

                // Setting the color of Value Axis' major gridlines to red
                chart.valueAxis.majorGridLines.color = AsposeCells.Color.Red;

                // Saving the Excel file and creating download link
                const outputData = workbook.save(SaveFormat.Excel97To2003);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'book1.out.xls';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
            });
        });
    </script>
</html>
```

## **高级主题**
- [设置图表系列的值格式代码](/cells/zh/javascript-cpp/set-the-values-format-code-of-chart-series/)
- [在图表中将图片设置为背景填充](/cells/zh/javascript-cpp/set-picture-as-background-fill-in-the-chart/)
