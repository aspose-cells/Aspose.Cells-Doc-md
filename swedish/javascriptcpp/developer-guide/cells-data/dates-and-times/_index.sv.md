---
title: Komma åt och hantera datum och tider
type: docs
weight: 600
url: /sv/javascript-cpp/how-to-manage-dates-and-times/
description: Lär dig att hantera datum och tidsangivelser med hjälp av Aspose.Cells for JavaScript via C++ API.
keywords: Komma åt och hantera datum och tider, 1900 datumsystemet, 1904 datumsystemet, Ange datum och tider, Hämta datum och tider, Hantera datum och tider, Lagra datum och tider i Excel, Visa datum och tider i celler.
---

## **Hur man lagrar datum och tider i Excel**  
Datum och tider lagras i celler som nummer. Värdena i celler som innehåller datum och tider är av numerisk typ. En siffra som anger ett datum och en tid består av datum (heltal) och tidskomponenter (fraktionellt). Egenskapen Cell.doubleValue returnerar detta nummer.  

## **Hur man visar datum och tider i Aspose.Cells**  
För att visa ett nummer som ett datum och tid, tillämpa det nödvändiga datum- och tidsformatet på en cell via egenskapen [Style.number](https://reference.aspose.com/cells/javascript-cpp/style/#number--) eller [Style.Custom]() Egenskapen CellValue.dateTimeValue returnerar DateTime-objektet, som anger det datum och den tid som representeras av numret i cellen.  
<br>  
<image src="1.png" width="70%" />  

## **Hur man växlar mellan två datum system i Aspose.Cells**  
MS-Excel lagrar datum som nummer som kallas seriella värden. Ett seriellt värde är ett heltal som är antalet passerade dagar från den första dagen i datum systemet. Excel stöder följande datum system för seriella värden:  

1. 1900-datum systemet. Det första datumet är den 1 januari 1900 och dess seriella värde är 1. Det sista datumet är den 31 december 9999 och dess seriella värde är 2 958 465. Detta datum system används som standard i arbetsboken.  
1. Det 1904-datumsystemet. Den första datumet är den 1 januari 1904, och dess serienummer är 0. Den sista datumet är den 31 december 9999, och dess serienummer är 2 957 003. För att använda detta datumsystem i arbetsboken, ställ in egenskapen [WorkbookSettings.date1904](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#date1904--) till true.  

Detta exempel visar att de seriella värden som lagras på samma datum i olika datum system är olika.  

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


Resultat av utmatning:  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **Hur man anger datumvärde i Aspose.Cells**  
Detta exempel anger ett DateTime-värde i cell A1 och A2, ställer in anpassat format för A1 och nummerformat för A2, och sedan skriver ut värdetyperna.  

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
            // Set custom Datetime style
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


Resultat av utmatning:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **Hur man får DateTime-värde i Aspose.Cells**  
Detta exempel anger ett DateTime-värde i cell A1 och A2, ställer in anpassat format för A1 och nummerformat för A2, kontrollerar värdetyperna för två celler, och sedan skriver ut DateTime-värdet och formaterad sträng.  

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
            // Set custom Datetime style
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


Resultat av utmatning:  
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
