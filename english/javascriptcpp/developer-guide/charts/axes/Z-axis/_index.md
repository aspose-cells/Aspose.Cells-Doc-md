---
title: Z Axis with JavaScript via C++
description: Learn how to work with the Z-axis in Aspose.Cells for JavaScript via C++. Our guide will help you understand how to configure and customize the Z-axis, including its scale and labels, to enhance your charts.
keywords: Aspose.Cells for JavaScript via C++, Z-axis, charting, configuration, customization, scale, labels.
type: docs
weight: 210
url: /javascript-cpp/z-axis/
---

## **Possible Usage Scenarios**
For some 3‑D charts such as 3‑D column, 3‑D cone, or 3‑D pyramid, which have a depth (series) axis—also known as the Z axis—that you can modify, you can specify the interval between tick marks, axis labels, and other settings.

## **Handle Primary and Secondary Axis like Microsoft Excel**
Please see the following sample code that creates a new Excel file and puts chart values in the first worksheet. Then we add a chart, set the chart type to Column3D, and you can see the Z Axis, also called the Depth Axis. 

![todo:image_alt_text](excel.png)

## **Sample Code**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Example (ZAxis)</h1>
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
            
            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);
            
            // Put values to cells for creating chart
            worksheet.cells.get("A1").value = "A";
            worksheet.cells.get("B1").value = "B";
            worksheet.cells.get("C1").value = "C";
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 1;
            worksheet.cells.get("B2").value = 2;
            worksheet.cells.get("B3").value = 3;
            worksheet.cells.get("C2").value = 2;
            worksheet.cells.get("C3").value = 3;
            
            // Add a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column3D, 9, 6, 25, 16);
            // Access the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);
            // Calculate the chart
            chart.calculate();
            // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
            chart.setChartDataRange("A2:C3", true);
            // Hide the Category Axis
            chart.categoryAxis.isVisible = false;
            // Hide the Value Axis
            chart.valueAxis.isVisible = false;
            
            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ZAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```