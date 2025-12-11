---
title: How to manage PivotChart with PivotOptions for JavaScript via C++
linktitle: Pivot Options
type: docs
weight: 10
url: /javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: How to manage PivotChart with PivotOptions in JavaScript via C++.
keywords: PivotChart JavaScript via C++
---

## What is PivotChart

A PivotChart in Excel is a graphical representation of data created from a PivotTable. It allows users to visualize and analyze data dynamically by summarizing and displaying information in chart form. PivotCharts are interactive and can be easily modified to show different perspectives of the data, making it a powerful tool for data analysis and presentation in Excel.

## How to manage PivotChart with PivotOptions

By using Aspose.Cells for JavaScript via C++, you can use [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/) to manage PivotChart.

Sample file and code:
[Sample File](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
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
            
            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;
            
            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter
            
            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

With the example code above, you can see the resulting file with the effect shown in the figure:

**![Output](Output.png)**