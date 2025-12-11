---  
title: Split Screen of Excel Worksheet with JavaScript via C++  
linktitle: Split Screen  
type: docs  
weight: 190  
url: /javascript-cpp/how-to-split-screen-of-excel-worksheet  
description: In this article, you'll learn how to display certain rows and/or columns in separate panes by splitting the worksheet into two or four parts programmatically using JavaScript via C++ Addon.  
keywords: Freeze top rows, Freeze top row.  
---  

## **Introduction**  

In this article, we will learn how to display certain rows and/or columns in separate panes by splitting the worksheet into two or four parts. When working with large datasets, we need to see a few areas of the same worksheet at a time to compare different subsets of data. The split screen function can meet your needs.  

## **How to split screen in Excel**  
To split up a worksheet into two or four parts, do the following:  

1. Select the row/column/cell before which you want to place the split.  
2. On the **View** tab, in the **Window** group, click the **Split** button.  

**![Split Screen](Split-Screen.png)**  

## **Split worksheet vertically on columns**  

To separate two areas of the spreadsheet vertically, select the column to the right of the column where you wish the split to appear and click the **Split** button in Excel.  

It's easy to split a worksheet vertically on columns programmatically with Aspose.Cells for JavaScript via C++; we only need to select a cell in the top row as the active cell, then split with the [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--) method.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;
        
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set the C1 cell in the top row as the active cell.
            sheet.activeCell = "C1";

            // Split worksheet vertically on columns
            sheet.split();

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Split worksheet horizontally on rows**  

To separate your Excel window horizontally, select the row below the row where you want the split to occur in Excel.  

It's easy to split a worksheet horizontally on rows programmatically with Aspose.Cells for JavaScript via C++; we only need to select a cell in the left column as the active cell, then split with the [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--) method.  

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Set the A6 cell in the left column as the active cell.
            sheet.activeCell = "A6";

            // Split worksheet horizontally on rows
            sheet.split();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Split worksheet into four parts**  

To view four different sections of the same worksheet simultaneously, split your screen both vertically and horizontally in Excel.  

It's easy to split a worksheet into four parts programmatically with Aspose.Cells for JavaScript via C++; we only need to select a cell that is not in the first row or column as the active cell, then split with the [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--) method.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Active Cell and Split Worksheet Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
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
            
            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);
            
            // Set the E6 cell as the active cell.
            sheet.activeCell = "E6";
            
            // Split worksheet into four parts
            sheet.split();
            
            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **How to remove split**  

To remove the worksheet splitting, just click the **Split** button again.  

Aspose.Cells for JavaScript via C++ provides a [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--) method to remove the split setting.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Worksheet Example</title>
    </head>
    <body>
        <h1>Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Remove split and then split the worksheet into four parts
            sheet.removeSplit();
            sheet.split();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet split operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```