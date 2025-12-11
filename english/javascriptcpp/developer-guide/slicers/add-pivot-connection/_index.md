---
title: Add Pivot Connection with JavaScript via C++
linktitle: Add Pivot Connection
type: docs
weight: 30
url: /javascript-cpp/add-pivot-connection/
description: Learn how to add a pivot connection using Aspose.Cells for JavaScript via C++.
keywords: Add pivot connection for Office 2013, Office 2016, Office 2019 and Office 365 JavaScript via C++.
---

## **Possible Usage Scenarios**

If you want to associate a slicer and pivot table in Excel, you need to right‑click the slicer and select **“Report Connections…”** item. In the options list, you can check the box. Similarly, if you want to associate a slicer and pivot table using Aspose.Cells API programmatically, please use the [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-) method. It will associate the slicer and pivot table.

## **Associate Slicer and PivotTable**

The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicer and then associates the slicer and pivot table. Finally, it saves the workbook as [output Excel file](add-pivot-connection-out.xlsx).

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```