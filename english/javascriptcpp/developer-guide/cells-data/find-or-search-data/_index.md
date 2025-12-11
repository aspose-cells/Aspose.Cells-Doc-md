---
title: Find or Search Data
type: docs
weight: 50
url: /javascript-cpp/find-or-search-data/
description: Learn how to find or search cells in a worksheet that contains specified data through the Aspose.Cells for JavaScript via C++ API.
keywords: Find data JavaScript via C++, Search data JavaScript via C++, Find Cells Containing a Formula JavaScript via C++, Search Cells Containing a Formula JavaScript via C++, Find Data or Formulas using FindOptions JavaScript via C++, Search Data or Formulas using FindOptions JavaScript via C++, Find or Search Cells Containing Specified String Value or Number JavaScript via C++, Find or Search cells containing specified data
---

{{% alert color="primary" %}}  
Microsoft Excel allows users to find cells in a worksheet that contain specified data.  
{{% /alert %}}  

## **Finding Cells Containing Specified Data**  

### **Using Microsoft Excel**  

Microsoft Excel allows users to find cells in a worksheet that contain specified data. If you select **Edit** from the **Find** menu in Microsoft Excel, you will see a dialog where you can specify the search value.  

Here, we are looking for the value "Oranges". Aspose.Cells also allows developers to find cells in the worksheet containing specified values.  

### **Using Aspose.Cells for JavaScript via C++**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection provides several methods for finding cells in a worksheet containing user‑specified data. A few of these methods are discussed below in more detail.  

{{% alert color="primary" %}}  
All Find methods return references to the cells containing the specified data.  
{{% /alert %}}  

## **Finding Cells Containing a Formula**  

Developers can find a specified formula in the worksheet by calling the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection's [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) method. Typically, the [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) method accepts three parameters:  

- The object to search for. The type should be int, double, DateTime, string, or bool.  
- Previous cell with the same object. This parameter can be set to null if searching from the start.  
- Options for finding the required object.  

The examples below use worksheet data for practicing find methods:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cell Containing Formula</title>
    </head>
    <body>
        <h1>Find Cell Containing Formula</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, LookInType } = AsposeCells;
        
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Instantiate FindOptions Object and set to look in formulas
            const findOptions = new FindOptions();
            findOptions.lookInType = LookInType.Formulas;

            // Finding the cell containing the specified formula
            const cell = worksheet.cells.find("=SUM(A5:A10)", null, findOptions);

            // Displaying the name of the cell found after searching worksheet
            document.getElementById('result').innerHTML = `<p style="color: green;">Name of the cell containing formula: ${cell.name}</p>`;
        });
    </script>
</html>
```  

## **Finding Data or Formulas using FindOptions**  

It is possible to find specified values using the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection's [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-) method with various [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions). Typically, the [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) method accepts the following parameters:  

- **Search value**, the data or value to be searched for.  
- **Previous cell**, the last cell that contained the same value. This parameter can be set to null when searching from the start.  
- **Find options**, the find options.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Using FindOptions</title>
    </head>
    <body>
        <h1>Find Using FindOptions Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FindOptions, CellArea, LookInType, LookAtType } = AsposeCells;
        
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

            // Calculate formulas in workbook
            workbook.calculateFormula();

            // Get Cells collection from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Instantiate FindOptions Object
            const findOptions = new FindOptions();

            // Create a Cells Area
            const ca = new CellArea();
            ca.startRow = 8;
            ca.startColumn = 2;
            ca.endRow = 17;
            ca.endColumn = 13;

            // Set cells area for find options
            findOptions.range = ca;

            // Set searching properties
            findOptions.searchBackward = false;
            findOptions.searchOrderByRows = true;

            // Set the lookintype, you may specify values, formulas, comments etc.
            findOptions.lookInType = LookInType.Values;

            // Set the lookattype, you may specify Match entire content, endswith, startswith etc.
            findOptions.lookAtType = LookAtType.EntireContent;

            // Find the cell with value
            const cell = cells.find(341, null, findOptions);

            if (cell !== null) {
                document.getElementById('result').innerHTML = `<p>Name of the cell containing the value: ${cell.name}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p>Record not found</p>';
            }
        });
    </script>
</html>
```  

## **Finding Cells Containing Specified String Value or Number**  

It is possible to find specified string values by calling the same [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) method found in the [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection with various [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions).  

Specify the [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) and [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-) properties. The following example code illustrates how to use these properties to find cells with various numbers of strings at the **beginning**, **middle**, or **end** of the cell's string.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Find Examples</h1>
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

            // Instantiate the workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection
            const cells = workbook.worksheets.get(0).cells;

            const opts = new AsposeCells.FindOptions();
            opts.lookInType = AsposeCells.LookInType.Values;
            opts.lookAtType = AsposeCells.LookAtType.EntireContent;

            let messages = '';

            // Find the cell with the input integer or double
            let cell1 = cells.find(205, null, opts);

            if (cell1 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell1.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell with the input string
            let cell2 = cells.find("Items A", null, opts);

            if (cell2 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell2.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell containing the input string (partial match)
            opts.lookAtType = AsposeCells.LookAtType.Contains;
            let cell3 = cells.find("Data", null, opts);

            if (cell3 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell3.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            document.getElementById('result').innerHTML = messages;
        });
    </script>
</html>
``` 

## **Advanced topics**  
- [Find Cells with Specific Style](/cells/javascript-cpp/find-cells-with-specific-style/)  
- [Find if the cell value starts with single quote mark](/cells/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Search Data using Original Values](/cells/javascript-cpp/search-data-using-original-values/)