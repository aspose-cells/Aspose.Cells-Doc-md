---
title: Chart to PDF with JavaScript via C++
linktitle: Chart to PDF
description: Learn how to use Aspose.Cells for JavaScript via C++ to convert a chart to a PDF document. Our guide will demonstrate how to export a chart from Microsoft Excel and save it as a PDF for further distribution and archiving.
keywords: Aspose.Cells for JavaScript via C++, Chart to PDF, Microsoft Excel, PDF Conversion, Export, Distribution, Archiving.
type: docs
weight: 47
url: /javascript-cpp/chart-to-pdf/
---

## **Rendering Chart to PDF**

In order to render the chart to PDF format, the Aspose.Cells APIs have exposed the [**Chart.toPdf(string)**](https://reference.aspose.com/cells/javascript-cpp/chart/#toPdf-string-) method with the ability to store the resultant PDF on a disk path or stream.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart to PDF</title>
    </head>
    <body>
        <h1>Chart to PDF Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();
            // Add a new worksheet
            const sheetIndex = workbook.worksheets.add();
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 20;
            worksheet.cells.get("B3").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);
            const chart = worksheet.charts.get(chartIndex);

            // Adding Series Collection (chart data source) to the chart ranging from the "A1" cell to "B3"
            chart.nSeries.add("A1:B3", true);

            // Converting chart to PDF
            const outputData = chart.toPdf();
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chartPDF_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to PDF successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **Create Chart PDF with Desired Page Size**  
You can create a chart PDF with your desired page size using Aspose.Cells and specify how you want to align the chart inside the page—as top, bottom, center, left, right, etc. Besides, the output chart can be created in a stream or on disk. Please see the following sample code that loads the [sample Excel file](64716906.xlsx), accesses the first chart inside the worksheet, and then converts it into [output PDF](64716907.pdf) with the desired page size. The following screenshot shows that the page size in the output PDF is 7 × 7 as specified inside the code, and the chart is center‑aligned both horizontally and vertically.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Sample Code**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Chart PDF With Desired Page Size</title>
    </head>
    <body>
        <h1>Create Chart PDF With Desired Page Size</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart inside the worksheet.
            const chart = worksheet.charts.get(0);

            // Create chart PDF with desired page size.
            // Note: In browser API omit file path and receive output data (Uint8Array / ArrayBuffer)
            const outputData = chart.toPdf(7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateChartPDFWithDesiredPageSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```