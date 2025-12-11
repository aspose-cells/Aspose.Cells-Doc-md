---
title: Create Volume-High-Low-Close (VHLC) Stock Chart with JavaScript via C++
linktitle: Create Volume-High-Low-Close (VHLC) Stock Chart
description: Learn how to create a volume-high-low-close stock chart using Aspose.Cells for JavaScript via C++. Our guide will demonstrate how to plot stock market data, including volume, high, low, and close prices, onto a chart for better analysis and visualization.
keywords: Aspose.Cells for JavaScript via C++, Volume-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 183
url: /javascript-cpp/create-volume-high-low-close-stock-chart/
---

## **Possible Usage Scenarios**
The third stock chart we will look at is the Volume High Low Close chart.  Again, it is important to emphasize that you must have the data in the correct order.  If you need to rearrange your data table, you should do it before you set up your chart.  
This chart includes a column for volume immediately after the first (category) column, and includes a column chart on the primary axis showing this volume, while the prices are moved to the secondary axis.

![todo:image_alt_text](data.png)

## **Volume-High-Low-Close (VHLC) stock chart**

![todo:image_alt_text](sample.png)

## **Sample Code**
The following sample code loads the [sample Excel file](Volume-High-Low-Close.xlsx) and generates the [output Excel file](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Volume-High-Low-Close Stock Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;
        
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

            // Create an instance of Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Create Volume-High-Low-Close Stock Chart
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(pieIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title name 
            chart.title.text = "Volume-High-Low-Close Stock";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = AsposeCells.LegendPositionType.Bottom;
            // Set data range (converted from setChartDataRange(range, isVertical))
            chart.chartDataRange = ["A1:E9", true];
            // Set category data 
            chart.nSeries.categoryData = "A2:A9";
            // Set the color for the first series (Volume) data 
            chart.nSeries.get(0).area.foregroundColor = new AsposeCells.Color(79, 129, 189);
            // Fill the PlotArea with nothing 
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```