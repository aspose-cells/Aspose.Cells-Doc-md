---
title: Show and Hide Gridlines and Row Column Headers with JavaScript via C++
linktitle: Show and Hide Gridlines and Row Column Headers
type: docs
weight: 30
url: /javascript-cpp/show-and-hide-gridlines-and-row-column-headers/
description: This article provides sample code for using the JavaScript API via C++ to programmatically hide or show gridlines, row, and column headers of an Excel worksheet.
---

{{% alert color="primary" %}}  
Aspose.Cells supports hiding and showing gridlines of the worksheet, which are visible by default. It also provides control over the visibility of row and column headers of the worksheet.  
{{% /alert %}}  

## **Show and Hide Gridlines**  

All Excel worksheets have gridlines by default. They help delineate cells so that it is easy to enter data into particular cells. Gridlines enable us to view a worksheet as a collection of cells, where each cell is easily identifiable.  

### **Controlling the Visibility of the Gridlines**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of gridlines, use the [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) property. [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) is a Boolean property, which means that it can only store a **true** or **false** value.  

#### **Making Gridlines Visible**  

Make the gridlines visible by setting the [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) property to **true**.  

#### **Hiding Gridlines**  

Hide gridlines by setting the [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) property to **false**.  

A complete example is given below that demonstrates the use of the [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isGridlinesVisible--) property by opening an Excel file (book1.xls), hiding the gridlines on the first worksheet, and saving the modified file as output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Gridlines Example</title>
    </head>
    <body>
        <h1>Hide Gridlines Example</h1>
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            // Opening the Excel file through the file data
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the grid lines of the first worksheet of the Excel file
            worksheet.isGridlinesVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Gridlines hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Show and Hide Row Column Headers**  

All worksheets in an Excel file are composed of cells that are arranged in rows and columns. All rows and columns have unique values that are used to identify them and to identify individual cells. For example, rows are numbered – 1, 2, 3, 4, etc. – and columns are ordered alphabetically – A, B, C, D, etc. The row and column values are displayed in the headers. Using Aspose.Cells, developers can control the visibility of these row and column headers.  

### **Controlling the Visibility of the Worksheets**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a wide range of properties and methods for managing a worksheet. To control the visibility of row and column headers, use the [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) property. [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) is a Boolean property, which means that it can only store a **true** or **false** value.  

#### **Making Row/Column Headers Visible**  

Make row and column headers visible by setting the [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) property to **true**.  

#### **Hiding Row/Column Headers**  

Hide row and column headers by setting the [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) property to **false**.  

A complete example is given below that shows how to use the [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isRowColumnHeadersVisible--) property by opening an Excel file (book1.xls), hiding the row and column headers on the first worksheet, and saving the modified file as output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Row/Column Headers</title>
    </head>
    <body>
        <h1>Hide Row and Column Headers Example</h1>
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the headers of rows and columns
            worksheet.isRowColumnHeadersVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
It is also possible to use the [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) and [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) methods of the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) class to make multiple rows and columns visible.  
{{% /alert %}}