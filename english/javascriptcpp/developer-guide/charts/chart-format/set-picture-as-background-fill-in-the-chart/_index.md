---
title: Set Picture as Background Fill in the Chart with JavaScript via C++
linktitle: Set Picture as Background Fill in the Chart
description: Learn how to set a picture as the background fill in a chart using Aspose.Cells for JavaScript via C++. Our guide will show you how to import and position the picture, adjust its size and color, and apply formatting options to enhance your chart's appearance.
keywords: Aspose.Cells for JavaScript via C++, charting, background fill, picture, import, positioning, size, color, formatting.
type: docs
weight: 30
url: /javascript-cpp/set-picture-as-background-fill-in-the-chart/
---

{{% alert color="primary" %}}

Aspose.Cells allows you to set a gradient, texture, pattern, or picture as fill effects for different objects, such as the plot area, chart area, or legend box of a chart. This document shows how to add an image to a chart's background.

{{% /alert %}}

To achieve this, Aspose.Cells provides the [**Chart.plotArea**](https://reference.aspose.com/cells/javascript-cpp/chart/#plotArea--) property. The following code sample demonstrates the use of [**Chart.plotArea**](https://reference.aspose.com/cells/javascript-cpp/chart/#plotArea--) property to set a picture as a background fill in the chart.

## JavaScript code to set picture as background fill in the chart

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Column Chart Example</h1>
        <p>
            Select an Excel file (sample.xlsx) and an optional image (aspose.png) for chart fill:
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read Excel file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet and set its name to "Data"
            let sheet = workbook.worksheets.get(0);
            sheet.name = "Data";

            // Get the cells collection in the sheet.
            const cells = workbook.worksheets.get(0).cells;

            // Put some values into cells of the Data sheet.
            let cell;
            cell = cells.get("A1"); cell.value = "Region";
            cell = cells.get("A2"); cell.value = "France";
            cell = cells.get("A3"); cell.value = "Germany";
            cell = cells.get("A4"); cell.value = "England";
            cell = cells.get("A5"); cell.value = "Sweden";
            cell = cells.get("A6"); cell.value = "Italy";
            cell = cells.get("A7"); cell.value = "Spain";
            cell = cells.get("A8"); cell.value = "Portugal";
            cell = cells.get("B1"); cell.value = "Sale";
            cell = cells.get("B2"); cell.value = 70000;
            cell = cells.get("B3"); cell.value = 55000;
            cell = cells.get("B4"); cell.value = 30000;
            cell = cells.get("B5"); cell.value = 40000;
            cell = cells.get("B6"); cell.value = 35000;
            cell = cells.get("B7"); cell.value = 32000;
            cell = cells.get("B8"); cell.value = 10000;

            // Add a chart sheet.
            let sheetIndex = workbook.worksheets.add(AsposeCells.SheetType.Chart);
            sheet = workbook.worksheets.get(sheetIndex);

            // Set the name of worksheet
            sheet.name = "Chart";

            // Create chart
            let chartIndex = sheet.charts.add(AsposeCells.ChartType.Column, 1, 1, 25, 10);
            const chart = sheet.charts.get(chartIndex);

            // Set some properties of chart plot area.
            // If an image was provided, set it as fill format and make the border invisible.
            if (imageInput.files.length) {
                const imgFile = imageInput.files[0];
                const imgBuffer = await imgFile.arrayBuffer();
                const imgBytes = new Uint8Array(imgBuffer);
                chart.plotArea.area.fillFormat.imageData = imgBytes;
            }
            chart.plotArea.border.isVisible = false;

            // Set properties of chart title
            chart.title.text = "Sales By Region";
            chart.title.font.color = AsposeCells.Color.Blue;
            chart.title.font.isBold = true;
            chart.title.font.size = 12;

            // Set properties of nseries
            chart.nSeries.add("Data!B2:B8", true);
            chart.nSeries.categoryData = "Data!A2:A8";
            chart.nSeries.isColorVaried = true;

            // Set the Legend.
            const legend = chart.legend;
            legend.position = AsposeCells.LegendPositionType.Top;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'column_chart_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```