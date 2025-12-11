---  
title: Manage formulas of Excel files with JavaScript via C++  
linktitle: Formulas  
type: docs  
weight: 122  
url: /javascript-cpp/using-formulas-or-functions-to-process-data/  
description: Learn how to manage formulas of Excel files through Aspose.Cells for JavaScript via C++. Aspose.Cells can simply get, set, and calculate formulas of Excel files.  
keywords: How to calculate formulas in JavaScript via C++, Formulas and Functions using JavaScript via C++, JavaScript via C++ Manage Built-in Functions, How to Use Add-in Functions with JavaScript via C++, How to Use Array Formula via JavaScript via C++, How to Use R1C1 Formula in JavaScript via C++.  
---  

## **Introduction**  

One of Microsoft Excel's compelling features is its ability to process data with formulas and functions. Microsoft Excel provides a set of built-in functions and formulas that help users perform complex calculations quickly. Aspose.Cells also provides a huge set of built-in functions and formulas that help developers compute values easily. Aspose.Cells also supports add‑in functions. Moreover, Aspose.Cells supports array and R1C1 formulas.  

## **How to Use Formulas and Functions**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) collection. Each item in the Cells collection represents an object of the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class.  

It is possible to apply formulas to cells using properties and methods offered by the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class, discussed in more detail below.  

- Using built-in functions.  
- Using add‑in functions.  
- Working with array formulas.  
- Creating an R1C1 formula.  

## **How to Use Built-in Functions**  

Built-in functions or formulas are provided as ready‑made functions to reduce developers' effort and time. See [a list of built-in functions](/cells/javascript-cpp/supported-formula-functions/) supported by Aspose.Cells. The functions are listed in alphabetical order. More functions will be supported in the future.  

Aspose.Cells supports most of the formulas or functions offered by Microsoft Excel. Developers can use these formulas through the API or a designer spreadsheet. Aspose.Cells supports a huge set of mathematical, string, Boolean, date/time, statistical, database, lookup, and reference formulas.  

Use the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class' **formula** property to add a formula to a cell. **Complex formulas**, for example  

{{< highlight java >}}  

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))  

{{< /highlight >}}  

are also supported in Aspose.Cells. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.  

In the example below, a complex formula is applied to the first cell of a worksheet's [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) collection. The formula uses a built-in **IF** function provided by Aspose.Cells.  

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```  

## **How to Use Add-in Functions**  

We can have some user‑defined formulas that we want to include as an Excel add‑in. When setting the `cell.formula`, built‑in functions work fine; however, there is a need to set custom functions or formulas using the add‑in functions.  

Aspose.Cells provides features to register add‑in functions using [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Afterwards, when we set `cell.formula = anyFunctionFromAddIn`, the output Excel file contains the calculated value from the add‑in function.  

The following XLAM file should be downloaded for registering the add‑in function in the sample code below. Similarly, the output file `test_udf.xlsx` can be downloaded to check the result.  

[TestUDF.xlam](81920908.xlam)  

[test_udf.xlsx](81920909.xlsx)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In &amp; Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro‑enabled add‑in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add‑in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add‑in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```  

## **How to Use Array Formula**  

Array formulas are formulas that take arrays, instead of individual numbers, as arguments to the functions that make up the formula. When an array formula is displayed, it is surrounded by braces ({}).  

Some Microsoft Excel functions return arrays of values. To calculate multiple results with an array formula, enter the array into a range of cells with the same number of rows and columns as the array arguments.  

It is possible to apply an array formula to a cell by calling the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class' [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) method. The method takes the following parameters:  

- **Array Formula** – the array formula.  
- **Number of Rows** – the number of rows to populate the result of the array formula.  
- **Number of Columns** – the number of columns to populate the result of the array formula.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```  

## **How to Use R1C1 Formula**  

Add an **R1C1** reference‑style formula to a cell with the [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) class' **r1C1Formula** property.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and column indices are relative to the destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Advanced topics**  
- [Precedents and Dependents](/cells/javascript-cpp/precedents-and-dependents/)  
- [Set External Links in Formulas](/cells/javascript-cpp/set-external-links-in-formulas/)  
- [Propagate Formula in Table or List Object automatically while entering data in new rows](/cells/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)  
- [Setting Formula for Named Range](/cells/javascript-cpp/setting-formula-for-named-range/)  
- [Setting Formulas - Notice for Non English Users](/cells/javascript-cpp/setting-formulas-notice-for-non-english-users/)  
- [Setting Shared Formula](/cells/javascript-cpp/setting-shared-formula/)  
- [Specify Maximum Rows of Shared Formula](/cells/javascript-cpp/specify-maximum-rows-of-shared-formula/)  
- [Supported Excel Functions](/cells/javascript-cpp/supported-formula-functions/)  