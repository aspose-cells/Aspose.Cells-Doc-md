---
title: Omvandling mellan cellnamn och rad/kolumnindex
linktitle: Cellnamn och Index Omvandling
type: docs
weight: 10
url: /sv/javascript-cpp/names-and-indices/
description: Lär dig hur du får konvertering mellan cellnamn och rad /kolumnindex via Aspose.Cells for JavaScript med C++ API.
keywords: JavaScript via C++ Få cellnamn från rad och kolumnindextal, Få rad och kolumnindextal från cellnamn, Skapa säkra arbetsbladnamn, Lägg till säkra arbetsbladnamn
---

## **Hämta cellnamn från rad- och kolumnindex**
Det är möjligt att hitta ett cells namn med rad- och kolumnindex. Den här artikeln förklarar hur.
Aspose.Cells for JavaScript via C++ tillhandahåller CellsHelper.cellIndexToName-metoden, vilket gör att utvecklare kan få cellens namn om de anger rad- och kolumnindex.

{{% alert color="primary" %}} 

Microsoft Excel börjar räkna rad- och kolumnindex från 1. Till skillnad från Microsoft Excel börjar Aspose.Cells for JavaScript via C++ räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempel visar hur man använder CellsHelper.cellIndexToName för att få tillgång till cellens namn givet ett känt rad- och kolumnindex. Koden genererar följande utdata.



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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **Hämta rad- och kolumnindex från cellens namn**
Det är möjligt att hitta en rad- och kolumnindex för cellen från dess namn. Denna artikel förklarar hur.
Aspose.Cells for JavaScript via C++ tillhandahåller CellsHelper.cellNameToIndex-metoden, vilket gör att utvecklare kan få rad- och kolumnindex från cellens namn.

{{% alert color="primary" %}} 

Microsoft Excel börjar räkna rad- och kolumnindex från 1. Till skillnad från Microsoft Excel börjar Aspose.Cells for JavaScript via C++ räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempel visar hur man använder CellsHelper.cellNameToIndex för att få rad- och kolumnindex från cellnamnet. Koden genererar följande utdata.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **Skapa säkra kalkylbladsnamn**
Ibland finns behov av att tilldela kalkylbladets namn vid körning. I detta scenario kan det finnas bladnamn som innehåller ytterligare tecken som <>+(?”. Det kan vara nödvändigt att ersätta alla sådana tecken, som inte är tillåtna som bladnamn, med ett förutbestämt tecken som tillhandahålls av användaren. Längden kan också öka till mer än 31 tecken och måste då förkortas. Apache POI erbjuder vissa funktioner för att skapa säkra namn, och liknande funktioner tillhandahålls av Aspose.Cells for JavaScript via C++ för att hantera dessa problem. Följande kodexempel visar denna funktion:



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

Utdata:

Det här är det första namnet som skapas

` `< > + (adj.Private _ " Private"
