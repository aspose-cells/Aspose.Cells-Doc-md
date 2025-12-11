---
title: Copying Rows and Columns with JavaScript via C++
linktitle: Copying Rows and Columns
type: docs
weight: 40
url: /javascript-cpp/copying-rows-and-columns/
description: This article shows how to copy rows and columns through the Aspose.Cells for JavaScript via C++ API.
keywords: JavaScript via C++, How to Copy Rows and Columns, Copy Rows in JavaScript, Copy Columns using JavaScript, How to Paste Rows and Columns using Aspose.Cells for JavaScript via C++, Paste multiple rows and columns, How to Copy and paste Single Row or Column.
---

## **Introduction**  

Sometimes, you need to copy rows and columns in a worksheet without copying the entire worksheet. With Aspose.Cells, it is possible to copy rows and columns within or between workbooks.  
When a row (or column) is copied, the data contained in it, including formulas — with updated references — and values, comments, formatting, hidden cells, images, and other drawing objects are copied too.  

## **How to Copy Rows and Columns with Microsoft Excel**  

1. Select the row or column that you want to copy.  
1. To copy rows or columns, click **Copy** on the **Standard** toolbar, or press **CTRL**+**C**.  
1. Select a row or column below or to the right of where you want to copy your selection.  
1. When you are copying rows or columns, click **Copied Cells** on the **Insert** menu.  

{{% alert color="primary" %}}  
If you click **Paste** on the **Standard** toolbar or press **CTRL**+**V** instead of clicking a command on the **Insert** menu, any contents of the destination cells are replaced.  
{{% /alert %}}  

## **How to Paste Rows and Columns using Paste Options with Microsoft Excel**  

1. Select the cells that contain the data or other attributes that you want to copy.  
1. On the Home tab, click **Copy**.  
1. Click the first cell in the area where you want to **paste** what you copied.  
1. On the Home tab, click the arrow next to **Paste**, and then select **Paste** Special.  
1. Select the **options** you want.  

## **How to Copy Rows and Columns Using Aspose.Cells for JavaScript via C++**  

## **How to Copy Single Rows**  

Aspose.Cells provides the [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) method of the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) class. This method copies all types of data including formulas, values, comments, cell formats, hidden cells, images and other drawing objects from the source row to the destination row.  

The [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) method takes the following parameters:  

- the source [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) object,  
- the source row index, and  
- the destination row index.  

Use this method to copy a row within a sheet, or to another sheet. The [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) method works in a similar way to Microsoft Excel. So, for example, you don't need to set the height of the destination row explicitly; that value is copied too.  

The following example shows how to copy a row in a worksheet. It uses a template Microsoft Excel file and copies the second row (complete with data, formatting, comments, images and so on) and pastes it to the 12th row in the same worksheet.  

You can skip the step that gets the source row height using the [**Cells.rowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-boolean-cellsunittype-) method and then set the destination row height using the [**Cells.rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) method, as the [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) method automatically takes care of the row height.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Row</title>
    </head>
    <body>
        <h1>Copy Row Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook.
            const wsTemplate = workbook.worksheets.get(0);

            // Copy the second row (index 1) with data, formatting, images and drawing objects
            // To the 16th row (index 15) in the worksheet.
            wsTemplate.cells.copyRow(wsTemplate.cells, 1, 15);

            // Save the excel file in Excel97To2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
When copying rows, it is important to note related images, charts or other drawing objects, as this is the same as Microsoft Excel:  

1. If the source row index is 5, the image, chart, etc., is copied if it is contained in the three rows (the starting row index is 4 and the ending row index is 6).  
1. The existing images, charts, etc., in the destination row will not be removed.  
{{% /alert %}}  

## **How to Copy Multiple Rows**  

You can also copy multiple rows onto a new destination while using the [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) method, which takes an additional integer parameter to specify the number of source rows to be copied.  

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

            // Instantiate workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Copy the first 3 rows to 7th row (indexes are zero-based)
            cells.copyRows(cells, 0, 6, 3);

            // Save the result and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **How to Copy Columns**  

Aspose.Cells provides the [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) method of the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) class. This method copies all types of data, including formulas — with updated references — and values, comments, cell formats, hidden cells, images and other drawing objects from the source column to the destination column.  

The [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) method takes the following parameters:  

- the source [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) object,  
- source column index, and  
- the destination column index.  

Use the [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) method to copy a column within a sheet or to another sheet.  

This example copies a column from a worksheet and pastes it into a worksheet in another workbook.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Column Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const excelWorkbook1 = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Copy the first column from the first worksheet into the third column of the same worksheet.
            const cells = ws1.cells;
            cells.copyColumn(cells, cells.columns.get(0).index, cells.columns.get(2).index);

            // Autofit the column.
            ws1.autoFitColumn(2);

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **How to Copy Multiple Columns**  

Similar to the [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) method, the Aspose.Cells API also provides the [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) method to copy multiple source columns to a new location.  

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
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;
        
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

            // Create an instance of Workbook class by loading the existing spreadsheet
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Copy the first 3 columns to the 7th column
            cells.copyColumns(cells, 0, 6, 3);

            // Save the result and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **How to Paste Rows and Columns with Paste Options**  

Aspose.Cells now provides [**PasteOptions**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/) while using functions [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) and [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). It allows you to set appropriate paste options similar to Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Change Chart Data Source</title>
    </head>
    <body>
        <h1>Change Chart Data Source Example</h1>
        <p>Select an Excel file (sampleChangeChartDataSource.xlsx) from your local machine.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteType, CopyOptions, PasteOptions } = AsposeCells;
        
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = workbook.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = workbook.worksheets.add("DestSheet");

            // Set CopyOptions.ReferToDestinationSheet to true
            const options = new CopyOptions();
            options.referToDestinationSheet = true;

            // Set PasteOptions
            const pasteOptions = new PasteOptions();
            pasteOptions.pasteType = PasteType.Values;
            pasteOptions.onlyVisibleCells = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options, pasteOptions);

            // Save workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataSource.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```