---
title: Accessing Cells of a Worksheet
type: docs
weight: 10
url: /javascript-cpp/accessing-cells-of-a-worksheet/
description: This article shows how to get the maximum display range of a worksheet and access cells through the Aspose.Cells for JavaScript via C++ API.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---

{{% alert color="primary" %}}

We know that all worksheets contain data that is stored in cells, which make up a worksheet. A cell is a basic part of a worksheet that is used to construct the whole worksheet as a sequence of rows and columns. Before we try to access data from a worksheet, we need to get access to its cells. So, in this topic, we will discuss some basic approaches to access worksheet cells at runtime using Aspose.Cells for JavaScript via C++.

{{% /alert %}}

## **How to Access Cells**

Aspose.Cells for JavaScript via C++ provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection that represents all cells in the worksheet.

We can use the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection to access cells in a worksheet. Aspose.Cells for JavaScript via C++ provides three basic approaches to access cells in a worksheet:

1. Using the cell name.  
2. Using a cell's row and column index.  
3. Using a cell index in the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection.

We have mentioned that the 3rd approach is the fastest and the 1st approach is the slowest. The performance difference between the approaches is very small, so don't worry about performance degradation regardless of the approach you use.

### **How to Get Cell Object by Cell Name**

Developers can access any specific cell by passing its cell name to the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection of the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class as an index.

If you create a blank worksheet at the start, the count of the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection is zero. When you use this approach to access a cell, it will check whether this cell exists in the collection. If yes, it returns the cell object in the collection; otherwise, it creates a new [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) object, adds it to the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection, and then returns the object. This approach is the easiest way to access a cell if you are familiar with Microsoft Excel, but it is the slowest compared to the other approaches.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **How to Get Cell Object by Row & Column Index of the Cell**

Developers can access any specific cell by passing the indices of its row and column to the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection of the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class.

This approach works in the same way as the first approach.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **How to Get Cell Object by Cell Index in Cells Collection**

A cell can also be accessed by passing the cell's numeric index to the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection.

If you use this approach to access cells, an exception can be thrown if the numeric index of the cell is out of range. This approach is the fastest way to access cells, but an important thing to know is that the numeric index may change after new cells are added to the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection. The cell objects in the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection are internally sorted by row and column indices.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **How to Get Maximum Display Range of Worksheet**

Aspose.Cells for JavaScript via C++ allows developers to access a worksheet's maximum display range. The maximum display range—the range of cells between the first and last cell with content—is useful when you need to copy, select, or display the entire contents of a worksheet in an image.

You can access a worksheet's maximum display range using [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--). The following sample code illustrates how to access the [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) property.

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```