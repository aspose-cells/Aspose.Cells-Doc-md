---
title: Manage data of Excel files
linktitle: Cells Data
type: docs
weight: 110
url: /javascript-cpp/view-and-edit-excel-data/
description: This article describes how to view and edit data of Excel files with Aspose.Cells library for JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---

{{% alert color="primary" %}}

In [Accessing Cells of a Worksheet](/cells/javascript-cpp/accessing-cells-of-a-worksheet/), we discussed basic approaches for accessing cells in a worksheet. This article uses one of those approaches to add different types of data to cells.

{{% /alert %}}

## **How to Add Data to Cells**

Aspose.Cells for JavaScript via C++ provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) collection. Each item in the [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class.

Aspose.Cells allows developers to add data to the cells in worksheets by calling the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class' [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) method. Aspose.Cells provides overloaded versions of the [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) method that lets developers add different kinds of data to cells. Using these overloaded versions of the [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) method, it is possible to add a Boolean, string, double, integer, or date/time, etc. values to the cell.

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **How to Improve Efficiency**

If you use [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) method to put a large amount of data to a worksheet, you should add values to the cells, first by rows and then by columns. This approach greatly improves the efficiency of your applications.

## **How to Retrieve Data from Cells**

Aspose.Cells for JavaScript via C++ provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to worksheets in the file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) collection. Each item in the [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class.

The [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class provides several properties that allow developers to retrieve values from the cells according to their data types. These properties include:

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): returns the string value of the cell.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): returns the double value of the cell.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): returns the boolean value of the cell.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): returns the date/time value of the cell.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): returns the float value of the cell.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): returns the integer value of the cell.

When a field is not filled, cells with [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) or [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) throw an exception.

The type of data contained in a cell can also be checked by using the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class' [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) method. In fact, the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class' [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) method is based on the [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype) enumeration whose pre-defined values are listed below:

|**Cell Value Types**|**Description**|
| :- | :- |
|IsBool|Specifies that cell value is Boolean.|
|IsDateTime|Specifies that cell value is date/time.|
|IsNull|Represents a blank cell.|
|IsNumeric|Specifies that cell value is numeric.|
|IsString|Specifies that cell value is a string.|
|IsUnknown|Specifies that cell value is unknown.|

You can also use the above pre-defined cell value types to compare with the type of data present in each cell.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
                        
            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

While working on worksheets, users may add different types of data in the cells. These data types may include Boolean, integer, floating point, text, or date/time values. With Aspose.Cells, you can get the appropriate values from the cells according to their data types.

{{% /alert %}}

## **Advance topics**
- [Accessing Cells of a Worksheet](/cells/javascript-cpp/accessing-cells-of-a-worksheet/)
- [Convert Text Numeric Data to Number](/cells/javascript-cpp/convert-text-numeric-data-to-number/)
- [Creating Subtotals](/cells/javascript-cpp/creating-subtotals/)
- [Data Filtering](/cells/javascript-cpp/data-filtering/)
- [Data Sorting](/cells/javascript-cpp/sort-data-of-excel/)
- [Data Validation](/cells/javascript-cpp/data-validation/)
- [Find or Search Data](/cells/javascript-cpp/find-or-search-data/)
- [Get Cell String Value with and without Formatting](/cells/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [Adding HTML Rich Text inside the Cell](/cells/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [Insert Hyperlinks into Excel or OpenOffice](/cells/javascript-cpp/insert-hyperlinks-to-excel/)
- [How and Where to Use Enumerators](/cells/javascript-cpp/how-and-where-to-use-enumerators/)
- [Measure the Width and Height of the Cell Value in Unit of Pixels](/cells/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Reading Cell Values in Multiple Threads Simultaneously](/cells/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion between cell name and row/column index](/cells/javascript-cpp/names-and-indices/)
- [Populate Data First by Row then by Column](/cells/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [Preserve Single Quote Prefix of Cell Value or Range](/cells/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Access and Update the Portions of Rich Text of Cell](/cells/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)