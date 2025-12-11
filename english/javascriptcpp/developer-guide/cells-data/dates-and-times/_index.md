---
title: How to Manage Dates and Times
type: docs
weight: 600
url: /javascript-cpp/how-to-manage-dates-and-times/
description: Learn how to manage dates and times through the Aspose.Cells for JavaScript via C++ API.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---

## **How to store Dates and Times in Excel**  
Dates and times are stored in cells as numbers. Thus, the values of cells that contain dates and times are of the numeric type. A number that specifies a date and time consists of the date (integer part) and time (fractional part) components. The Cell.doubleValue property returns this number.  

## **How to Display Dates and Times in Aspose.Cells**  
To display a number as a date and time, apply the required date and time format to a cell via the [Style.number](https://reference.aspose.com/cells/javascript-cpp/style/#number--) or [Style.Custom]() property. The CellValue.dateTimeValue property returns the DateTime object, which specifies the date and time that is represented by the number contained in a cell.  
<br>  
<image src="1.png" width="70%" />  

## **How to switch between two date systems in Aspose.Cells**  
MS-Excel stores dates as numbers that are called serial values. A serial value is an integer that is the number of elapsed days from the first day in the date system. Excel supports the following date systems for serial values:  

1. The 1900 date system. The first date is January 1, 1900, and its serial value is 1. The last date is December 31, 9999, and its serial value is 2,958,465. This date system is used in the workbook by default.  
1. The 1904 date system. The first date is January 1, 1904, and its serial value is 0. The last date is December 31, 9999, and its serial value is 2,957,003. To use this date system in the workbook, set the [WorkbookSettings.date1904](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#date1904--) property to true.  

This example shows that the serial values stored on the same date in different date systems are different.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Date System Example</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Set 1900/1904 date system to false (1900 system)
            workbook.settings.date1904 = false;

            // Obtaining the reference of the newly added worksheet (first worksheet)
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            const dateData = new Date(2023, 10, 23); // JavaScript months are 0-based

            // Setting the DateTime value to the cells (A1)
            const a1 = cells.get("A1");
            a1.value = dateData;

            let resultHtml = '';

            // Check if the cell contains a numeric value
            if (a1.type === AsposeCells.CellValueType.IsNumeric) {
                resultHtml += `<p>A1 is Numeric Value: ${a1.doubleValue}</p>`;
                console.log("A1 is Numeric Value: " + a1.doubleValue);
            } else {
                resultHtml += `<p>A1 is not numeric. Cell type: ${a1.type}</p>`;
            }

            // Use the 1904 date system now
            workbook.settings.date1904 = true;
            console.log("use The 1904 date system====================");

            // Setting the DateTime value to the cells (A2) using setter conversion
            const a2 = cells.get("A2");
            a2.value = dateData;

            // Check if the cell contains a numeric value
            if (a2.type === AsposeCells.CellValueType.IsNumeric) {
                resultHtml += `<p>A2 is Numeric Value: ${a2.doubleValue}</p>`;
                console.log("A2 is Numeric Value: " + a2.doubleValue);
            } else {
                resultHtml += `<p>A2 is not numeric. Cell type: ${a2.type}</p>`;
            }

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully!</p>${resultHtml}`;
        });
    </script>
</html>
```


Output result:  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **How to Set a DateTime Value in Aspose.Cells**  
This example sets a DateTime value in cell A1 and A2, sets a custom format for A1 and a number format for A2, and then outputs the value types.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
                // No file selected - proceed with a new blank workbook (matches original JavaScript behavior)
                document.getElementById('result').innerHTML = '<p>No file selected. A new workbook will be created and modified.</p>';
            }

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            let ws = workbook.worksheets.get(0);
            let cells = ws.cells;

            // Setting the DateTime value to the cell A1
            let a1 = cells.get("A1");
            a1.putValue(new Date());

            // Check if the cell contains a numeric value
            if (a1.type === AsposeCells.CellValueType.IsNumeric) {
                console.log("A1 is Numeric Value: " + a1.isNumericValue());
            }

            let a1Style = a1.style;
            // Set custom DateTime style
            a1Style.custom = "mm-dd-yy hh:mm:ss";
            a1.style = a1Style;

            // Check if the cell contains a DateTime value
            if (a1.type === AsposeCells.CellValueType.IsDateTime) {
                console.log("Cell A1 contains a DateTime value.");
            } else {
                console.log("Cell A1 does not contain a DateTime value.");
            }

            // Setting the DateTime value to the cell A2
            let a2 = cells.get("A2");
            a2.putValue(new Date());

            // Check if the cell contains a numeric value
            if (a2.type === AsposeCells.CellValueType.IsNumeric) {
                console.log("A2 is Numeric Value: " + a2.isNumericValue());
            }

            let a2Style = a2.style;
            // Set the display format of numbers and dates.
            a2Style.number = 22;
            a2.style = a2Style;

            // Check if the cell contains a DateTime value
            if (a2.type === AsposeCells.CellValueType.IsDateTime) {
                console.log("Cell A2 contains a DateTime value.");
            } else {
                console.log("Cell A2 does not contain a DateTime value.");
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


Output result:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **How to Get a DateTime Value in Aspose.Cells**  
This example sets a DateTime value in cell A1 and A2, sets a custom format for A1 and a number format for A2, checks the value types of the two cells, and then outputs the DateTime value and formatted string.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>DateTime Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const arrayBuffer = await fileInput.files[0].arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the DateTime value to cell A1
            const a1 = cells.get("A1");
            a1.putValue(new Date());

            // Check if the cell contains a numeric value
            if (a1.type === AsposeCells.CellValueType.IsNumeric) {
                console.log("A1 is Numeric Value: " + a1.isNumericValue);
                resultDiv.innerHTML += `<p>A1 is Numeric Value: ${a1.isNumericValue}</p>`;
            }

            let a1Style = a1.style;
            // Set custom DateTime style
            a1Style.custom = "mm-dd-yy hh:mm:ss";
            a1.style = a1Style;

            // Check if the cell contains a DateTime value
            if (a1.type === AsposeCells.CellValueType.IsDateTime) {
                console.log("Cell A1 contains a DateTime value.");
                const dateTimeValue = a1.dateTimeValue;
                console.log("A1 DateTime Value: " + dateTimeValue);
                console.log("A1 DateTime String Value: " + a1.stringValue);
                resultDiv.innerHTML += `<p>Cell A1 contains a DateTime value: ${a1.stringValue}</p>`;
            } else {
                console.log("Cell A1 does not contain a DateTime value.");
                resultDiv.innerHTML += `<p>Cell A1 does not contain a DateTime value.</p>`;
            }

            // Setting the DateTime value to cell A2
            const a2 = cells.get("A2");
            a2.putValue(new Date());

            // Check if the cell contains a numeric value
            if (a2.type === AsposeCells.CellValueType.IsNumeric) {
                console.log("A2 is Numeric Value: " + a2.isNumericValue);
                resultDiv.innerHTML += `<p>A2 is Numeric Value: ${a2.isNumericValue}</p>`;
            }

            let a2Style = a2.style;
            // Set the display format of numbers and dates.
            a2Style.number = 22;
            a2.style = a2Style;

            // Check if the cell contains a DateTime value
            if (a2.type === AsposeCells.CellValueType.IsDateTime) {
                console.log("Cell A2 contains a DateTime value.");
                const dateTimeValue = a2.dateTimeValue;
                console.log("A2 DateTime Value: " + dateTimeValue);
                console.log("A2 DateTime String Value: " + a2.stringValue);
                resultDiv.innerHTML += `<p>Cell A2 contains a DateTime value: ${a2.stringValue}</p>`;
            } else {
                console.log("Cell A2 does not contain a DateTime value.");
                resultDiv.innerHTML += `<p>Cell A2 does not contain a DateTime value.</p>`;
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


Output result:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A1 DateTime Value: 11/23/2023 5:59:09 PM  
A1 DateTime String Value: 11-23-23 17:59:09  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
A2 DateTime Value: 11/23/2023 5:59:09 PM  
A2 DateTime String Value: 11/23/2023 17:59  
```