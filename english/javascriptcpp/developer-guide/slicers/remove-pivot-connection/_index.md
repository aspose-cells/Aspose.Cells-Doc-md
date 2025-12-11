---
title: Remove Pivot Connection with JavaScript via C++
linktitle: Remove Pivot Connection
type: docs
weight: 30
url: /javascript-cpp/remove-pivot-connection/
description: Learn how to remove a pivot connection using Aspose.Cells for JavaScript via C++.
keywords: Remove pivot connection without Office 2013, Office 2016, Office 2019, and Office 365 JavaScript via C++.
---

## **Possible Usage Scenarios**

If you want to disassociate a slicer from a pivot table in Excel, you need to right‑click the slicer and select the **“Report Connections…”** item. In the options list, you can toggle the checkbox. Similarly, if you want to disassociate a slicer from a pivot table using the Aspose.Cells for JavaScript via C++ API programmatically, please use the [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-) method. It will disassociate the slicer from the pivot table.

## **Disassociate a slicer and a pivot table**

The following sample code loads the [sample Excel file](remove-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicers and then disassociates the slicer from the pivot table. Finally, it saves the workbook as the [output Excel file](remove-pivot-connection-out.xlsx).

## **Sample Code**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove the PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in the output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```