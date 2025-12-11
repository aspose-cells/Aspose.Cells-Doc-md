---
title: Loading and managing Excel, OpenOffice, JSON, CSV and HTML files
linktitle: Open Files
type: docs
weight: 20
url: /javascript-cpp/loading-saving-and-managing/
description: With Aspose.Cells, it is simple to create, open, and manage Excel, CSV, TSV, ODS, HTML, Numbers, JSON, XML, PDF, JPG, TIFF, Image, MHT, and XPS files using JavaScript via C++.
---

{{% alert color="primary" %}}

With Aspose.Cells, it is simple to create, open, and manage Excel files, for example, to retrieve data, or to use a designer template to speed up the development process.

{{% /alert %}}

## **Creating a New Workbook**
The following example creates a new workbook from scratch.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into cell A1
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Opening and Saving a File**
With Aspose.Cells, it is simple to open, save, and manage Excel files.

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook object and opening an Excel file from its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting the active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values:
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting date and time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Advanced Topics**
- [Different Ways to Open Files](/cells/javascript-cpp/different-ways-to-open-files/)
- [Filter Defined Names while loading Workbook](/cells/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [Filter Objects while loading Workbook or Worksheet](/cells/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtering the kind of data while loading the workbook from template file](/cells/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Get Warnings while Loading Excel File](/cells/javascript-cpp/get-warnings-while-loading-excel-file/)
- [Load Source Excel File Without Charts](/cells/javascript-cpp/load-source-excel-file-without-charts/)
- [Load Specific Worksheets in a Workbook](/cells/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [Load Workbook with specified Printer Paper Size](/cells/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [Opening Different Microsoft Excel Versions Files](/cells/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [Opening Files with Different Formats](/cells/javascript-cpp/opening-files-with-different-formats/)
- [Optimizing Memory Usage while Working with Big Files having Large Datasets](/cells/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells](/cells/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Stop conversion or loading using InterruptMonitor when it is taking too long](/cells/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Using LightCells API](/cells/javascript-cpp/using-lightcells-api/)
- [Convert CSV to JSON](/cells/javascript-cpp/convert-csv-to-json/)
- [Convert Excel to JSON](/cells/javascript-cpp/convert-excel-to-json/)
- [Convert JSON to CSV](/cells/javascript-cpp/convert-json-to-csv/)
- [Convert JSON to Excel](/cells/javascript-cpp/convert-json-to-excel/)
- [Convert Excel to HTML](/cells/javascript-cpp/convert-excel-to-html/)