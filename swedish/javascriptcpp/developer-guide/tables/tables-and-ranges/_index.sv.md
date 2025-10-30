---
title: Tabeller och områden med JavaScript via C++
linktitle: Tabeller och Intervall
type: docs
weight: 50
url: /sv/javascript-cpp/tables-and-ranges/
---

## **Introduktion**  

Ibland skapar du en tabell i Microsoft Excel och vill inte fortsätta arbeta med tabellfunktionaliteten den kommer med. Istället vill du ha något som ser ut som en tabell. För att behålla data i en tabell utan att förlora formateringen, konvertera tabellen till en vanlig datamängd.  
Aspose.Cells stöder denna funktion i Microsoft Excel för tabeller och listobjekt.  

## **Använda Microsoft Excel**  

Använd **Konvertera till område**-funktionen för att snabbt konvertera en tabell till en mängd utan att förlora formateringen. I Microsoft Excel 2007/2010:  

1. Klicka var som helst i tabellen för att se till att den aktiva cellen är i en tabellkolumn.  
1. På fliken **Utformning**, i gruppen **Verktyg**, klicka på **Konvertera till område**.  

## **Använda Aspose.Cells**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Table to Range</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet and convert the first table/list object to a normal range
            const worksheet = workbook.worksheets.get(0);
            const listObject = worksheet.listObjects.get(0);
            listObject.convertToRange();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

Tabellfunktionerna är inte längre tillgängliga efter att tabellen har konverterats till en mängd. Till exempel inkluderar radrubrikerna inte längre sorterings- och filterpilar, och strukturerade referenser (referenser som använder tabellnamn) som användes i formler omvandlas till vanliga cellreferenser.  

{{% /alert %}}  

## **Konvertera tabell till område med alternativ.**  

Aspose.Cells tillhandahåller ytterligare alternativ när du konverterar tabell till intervall genom klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/). Klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/) tillhandahåller egenskapen [**lastRow**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/#lastRow--) som gör att du kan ange den sista indexet för tabellraden. Tabellformateringen behålls upp till det angivna radindexet och resten av formateringen tas bort.  

Den angivna provkoden nedan visar användningen av klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Table to Range Example</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TableToRangeOptions, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create TableToRangeOptions and set lastRow property
            const options = new TableToRangeOptions();
            options.lastRow = 5;

            // Convert the first table/list object (from the first worksheet) to normal range
            workbook.worksheets.get(0).listObjects.get(0).convertToRange(options);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
