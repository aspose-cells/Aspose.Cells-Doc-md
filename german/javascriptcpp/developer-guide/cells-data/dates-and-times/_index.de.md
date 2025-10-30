---
title: Wie man Daten und Zeiten verwaltet
type: docs
weight: 600
url: /de/javascript-cpp/how-to-manage-dates-and-times/
description: Erfahren Sie, wie Sie Daten und Zeiten mit dem Aspose.Cells for JavaScript über C++ API verwalten.
keywords: Wie man Daten und Zeiten verwaltet, das 1900 Datensystem, das 1904 Datensystem, Daten und Zeiten setzen, Daten und Zeiten abrufen, Daten und Zeiten verwalten, Daten und Zeiten in Excel speichern, Daten und Zeiten in Zellen anzeigen.
---

## **Wie man Daten und Zeiten in Excel speichert**  
Daten und Zeiten werden in Zellen als Zahlen gespeichert. Somit sind die Werte von Zellen, die Daten und Zeiten enthalten, vom numerischen Typ. Eine Zahl, die Datum und Uhrzeit angibt, besteht aus Datum (Ganzzahlteil) und Zeit (Bruchteil). Die Eigenschaft Cell.doubleValue gibt diese Zahl zurück.  

## **Wie man Daten und Zeiten in Aspose.Cells anzeigt**  
Um eine Zahl als Datum und Uhrzeit anzuzeigen, wenden Sie das erforderliche Datums- und Zeitformat auf eine Zelle an, entweder über die Style.number() Methode oder die Style.Custom() Methode. Die Eigenschaft CellValue.dateTimeValue gibt das DateTime-Objekt zurück, das das Datum und die Zeit angibt, die durch die Zahl in der Zelle repräsentiert werden.  
<br>  
<image src="1.png" width="70%" />  

## **Wie man zwischen zwei Datumsystemen in Aspose.Cells wechselt**  
MS-Excel speichert Daten als Zahlen, die als Serienwerte bezeichnet werden. Ein Serienwert ist eine Ganzzahl, die die Anzahl der vergangenen Tage seit dem ersten Tag im Datensystem angibt. Excel unterstützt die folgenden Datensysteme für Serienwerte:  

1. Das 1900-Datensystem. Das erste Datum ist der 1. Januar 1900 und sein Serienwert ist 1. Das letzte Datum ist der 31. Dezember 9999 und sein Serienwert beträgt 2.958.465. Dieses Datensystem wird standardmäßig in der Arbeitsmappe verwendet.  
1. Das 1904-Datumsystem. Das erste Datum ist der 1. Januar 1904 und sein Serienwert ist 0. Das letzte Datum ist der 31. Dezember 9999 und sein Serienwert ist 2.957.003. Um dieses Datumssystem im Arbeitsbuch zu verwenden, setzen Sie die Eigenschaft WorkbookSettings.date1904 auf true.  

Dieses Beispiel zeigt, dass die in verschiedenen Datensystemen gespeicherten Serienwerte für dasselbe Datum unterschiedlich sind.  

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


Ausgabenergebnis:  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **So legen Sie den DateTime-Wert in Aspose.Cells fest**  
Dieses Beispiel legt einen DateTime-Wert in Zelle A1 und A2 fest, legt ein benutzerdefiniertes Format für A1 und ein Zahlenformat für A2 fest und gibt dann die Werttypen aus.  

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


Ausgabenergebnis:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **So erhalten Sie den DateTime-Wert in Aspose.Cells**  
Dieses Beispiel legt einen DateTime-Wert in Zelle A1 und A2 fest, legt ein benutzerdefiniertes Format für A1 und ein Zahlenformat für A2 fest, überprüft die Werttypen von zwei Zellen und gibt dann den DateTime-Wert und den formatierten String aus.  

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


Ausgabenergebnis:  
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
