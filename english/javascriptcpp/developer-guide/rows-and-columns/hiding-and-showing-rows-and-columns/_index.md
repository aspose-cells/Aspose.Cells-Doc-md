---
title: Hiding and Showing Rows and Columns with JavaScript via C++
linktitle: Hiding and Showing Rows and Columns
type: docs
weight: 60
url: /javascript-cpp/hiding-and-showing-rows-and-columns/
description: Learn how to hide and show rows and columns in a worksheet using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Sometimes, it makes sense to hide certain rows or columns in a worksheet and display them later. Microsoft Excel provides this feature and so does Aspose.Cells.

{{% /alert %}}

## **Controlling the Visibility of Rows and Columns**

Aspose.Cells for JavaScript via C++ provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

### **Hiding Rows and Columns**

Developers can hide a row or column by calling the [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) and [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) methods of the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection respectively. Both methods take a row or column index as a parameter to hide the specific row or column.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Row and Column Example</h1>
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
            
            // Instantiating a Workbook object with Uint8Array
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);
            
            // Hiding the 3rd row of the worksheet
            worksheet.cells.hideRow(2);
            
            // Hiding the 2nd column of the worksheet
            worksheet.cells.hideColumn(1);
            
            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Row and column hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

It is also possible to hide a row or column by setting the row height or column width to 0 respectively.

{{% /alert %}}

### **Showing Rows and Columns**

Developers can show any hidden row or column by calling the [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) and [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) methods of the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection respectively. Both methods take two parameters:

- **Row or column index** – the index of a row or column that is used to show the specific row or column.  
- **Row height or column width** – the row height or column width assigned to the row or column after unhiding.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Unhide Rows and Columns Example</title>
    </head>
    <body>
        <h1>Unhide Rows and Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unhiding the 3rd row and setting its height to 13.5
            worksheet.cells.unhideRow(2, 13.5);

            // Unhiding the 2nd column and setting its width to 8.5
            worksheet.cells.unhideColumn(1, 8.5);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

While making a hidden column visible, if you need to restore it to its previously assigned width or to its original width, use a negative width. For example: `worksheet.cells.unhideColumn(5, -1)`

{{% /alert %}}

### **Hiding Multiple Rows and Columns**

Developers can hide multiple rows or columns at once by calling the [**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-) and [**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-) methods of the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Rows and Columns</title>
    </head>
    <body>
        <h1>Hide Rows and Columns Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            
            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);
            
            // Hiding 3, 4, and 5 rows in the worksheet (rows are zero‑based index)
            worksheet.cells.hideRows(2, 3);
            
            // Hiding 2 and 3 columns in the worksheet (columns are zero‑based index)
            worksheet.cells.hideColumns(1, 2);
            
            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            
            resultDiv.innerHTML = '<p style="color: green;">Rows and columns hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

It is also possible to use the **Cells** class’s [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) and [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) methods to make multiple rows and columns visible.

{{% /alert %}}