---
title: Dölj och visa rader och kolumner med JavaScript via C++
linktitle: Dölja och visa rader och kolumner
type: docs
weight: 60
url: /sv/javascript-cpp/hiding-and-showing-rows-and-columns/
description: Lär dig hur du döljer och visar rader och kolumner i ett kalkylblad med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Ibland är det meningsfullt att dölja vissa rader eller kolumner i en arbetsbok och sedan visa dem senare. Microsoft Excel tillhandahåller den här funktionen och så gör även Aspose.Cells.

{{% /alert %}}

## **Kontrollera synligheten av rader och kolumner**

Aspose.Cells for JavaScript via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) som låter utvecklare få åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) samling som representerar alla celler i kalkylbladet. Samlingen [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) erbjuder flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

### **Dölja rader och kolumner**

Utvecklare kan dölja en rad eller kolumn genom att anropa metoderna [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) och [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) av [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen respektive. Båda metoder tar rad- och kolumnindex som parameter för att dölja den specifika raden eller kolumnen.

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

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Visa rader och kolumner**

Utvecklare kan visa vilken dold rad eller kolumn som helst genom att anropa metoderna [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) och [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) av [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen respektive. Båda metoder tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.

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

När du gör en dold kolumn synlig, om du behöver återställa den till den tidigare tilldelade bredden eller till dess ursprungliga bredd, avmarkera kolumnen med en negativ bredd. Till exempel: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Dölja flera rader och kolumner**

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa metoderna [**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-) och [**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-) av [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen respektive. Båda metoder tar startrad- eller startkolumnindex och antalet rader eller kolumner som ska döljas som parametrar.

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

            // Hiding 3, 4, and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
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

Det är också möjligt att använda [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) klassens [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) och [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) metoder för att göra flera rader och kolumner synliga.

{{% /alert %}}
