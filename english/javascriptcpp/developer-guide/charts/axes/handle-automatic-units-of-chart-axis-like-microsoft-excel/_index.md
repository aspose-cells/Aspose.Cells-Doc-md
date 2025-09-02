---
title: Handle Automatic Units of Chart Axis like Microsoft Excel with JavaScript via C++
linktitle: Handle Automatic Units of Chart Axis like Microsoft Excel
description: Learn how to handle automatic units on chart axes in Aspose.Cells for JavaScript via C++. Our guide will show you how to configure and customize automatic units on a chart axis, including the display of scientific notation and adjusting the scale.
keywords: Aspose.Cells for JavaScript via C++, chart axes, automatic units, Microsoft Excel, configuration, customization, scientific notation, scaling.
type: docs
weight: 120
url: /javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Possible Usage Scenarios**  
Early versions of Aspose.Cells for JavaScript via C++ were not able to handle automatic units of the chart axis properly when the chart is rendered to image or PDF. Now, Aspose.Cells for JavaScript via C++ supports the handling of automatic units of the chart axis. There is no code change. Just convert your chart into an image or PDF and it will render the chart axis just like Microsoft Excel renders it.  

## **Handle Automatic Units of Chart Axis like Microsoft Excel**  
The following sample code loads the [sample Excel file](61767755.xlsx) and generates the [output PDF chart](61767752.pdf). The screenshot shows the automatic units of the chart axis in red rectangles and also compares the sample Excel file chart with the output PDF chart. Both are exactly similar.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Sample Code**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;
        
        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```