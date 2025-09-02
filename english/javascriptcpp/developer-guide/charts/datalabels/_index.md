---
title: Manage DataLabels of Excel Charts with JavaScript via C++
description: Learn how to effectively manage data labels in Excel charts using Aspose.Cells for JavaScript via C++. This comprehensive guide covers various management tasks, including adding, removing, and modifying labels to enhance chart readability and usability.
keywords: Aspose.Cells for JavaScript, Excel charts, data labels, management, readability, usability, adding, removing, modifying.
linktitle: DataLabels
type: docs
weight: 50
url: /javascript-cpp/insert-datalabels-to-chart/
---

{{% alert color="primary" %}}  

DataLabels are an important part of a chart.  
We can easily know the value, percentage, etc. of each series  

{{% /alert %}}  

## **DataLabels Options**  
Aspose.Cells for JavaScript via C++ also allows managing chart's datalabels at runtime, with the [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/) object, it's simple to move, update and format datalabels of the chart.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Manage the DataLabels of Chart**  
It's simple to manage datalabels of the chart with Aspose.Cells [DataLabels](https://reference.aspose.com/cells/javascript-cpp/datalabels/).  

The following code snippet demonstrates how to manage DataLabels:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Data Labels Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeReady = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            if (!asposeReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            // Instantiate a new Workbook object
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

            // Show value labels
            chart.nSeries.get(0).dataLabels.showValue = true;
            // Show series name labels
            chart.nSeries.get(1).dataLabels.showSeriesName = true;
            // Move labels to center
            chart.nSeries.get(1).dataLabels.position = AsposeCells.LabelPositionType.Center;

            // Save the file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_datalabels.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Advance topics**  
- [Adding Custom Labels to Data Points in the Series of the Chart](/cells/javascript-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Disable Text Wrapping for Data Labels of the Chart](/cells/javascript-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Resize Chart's Data Label Shape To Fit Text](/cells/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Rich Text Custom Data Label of Chart Point](/cells/javascript-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Set the Shape Type of Data Labels of Chart](/cells/javascript-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Showing Cell Range as the Data Labels](/cells/javascript-cpp/showing-cell-range-as-the-data-labels/)