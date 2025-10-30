---
title: Kopiera rader och kolumner med JavaScript via C++
linktitle: Kopiera rader och kolumner
type: docs
weight: 40
url: /sv/javascript-cpp/copying-rows-and-columns/
description: Den här artikeln visar hur man kopierar rader och kolumner genom Aspose.Cells for JavaScript via C++ API.
keywords: JavaScript via C++, Hur man kopierar rader och kolumner, Kopiera rader i JavaScript, Kopiera kolumner med JavaScript, Hur man klistrar in rader och kolumner med Aspose.Cells for JavaScript via C++, Klistra in flera rader och kolumner, Hur man kopierar och klistrar in enstaka rad eller kolumn.
---

## **Introduktion**  

Ibland behöver du kopiera rader och kolumner i en arbetsbok utan att kopiera hela arbetsboken. Med Aspose.Cells är det möjligt att kopiera rader och kolumner inom eller mellan arbetsböcker.  
När en rad (eller kolumn) kopieras, kopieras också den data som finns i den, inklusive formler - med uppdaterade referenser - och värden, kommentarer, formatering, dolda celler, bilder och andra ritobjekt.  

## **Hur man kopierar rader och kolumner med Microsoft Excel**  

1. Markera raden eller kolumnen som du vill kopiera.  
1. För att kopiera rader eller kolumner, klicka på **Kopiera** på **Standard** verktygsfältet, eller tryck på **CTRL**+**C**.  
1. Välj en rad eller en kolumn nedanför eller till höger om där du vill kopiera ditt val.  
1. När du kopierar rader eller kolumner, klicka på **Kopierade celler** på menyn **Infoga**.  

{{% alert color="primary" %}}  
Om du klickar på **Klistra in** på **Standard** verktygsfältet eller trycker på **CTRL**+**V** istället för att klicka på en kommando i **Infoga** menyn, ersätts eventuella innehåll i destinationens celler.  
{{% /alert %}}  

## **Hur man klistrar in rader och kolumner med hjälp av klistra in-alternativ med Microsoft Excel**  

1. Välj cellerna som innehåller data eller andra attribut som du vill kopiera.  
1. På fliken Hem, klicka på **Kopiera**.  
1. Klicka på den första cellen i det område där du vill **klistra in** det du kopierade.  
1. På fliken Hem, klicka på pilen bredvid **Klistra in**, och välj sedan **Klistra in** Special.  
1. Välj de **alternativ** du vill.  

## ** Hur man kopierar rader och kolumner med Aspose.Cells for JavaScript via C++**  

## **Hur man kopierar enskilda rader**  

Aspose.Cells tillhandahåller metoden [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) av [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-klassen. Den här metoden kopierar all typ av data, inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till destinationsraden.  

[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-)-metoden tar följande parametrar:  

- källekon,  
- källradens index, och  
- destinationsradens index.  

Använd denna metod för att kopiera en rad inom ett blad, eller till ett annat blad. [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-)-metoden fungerar på ett liknande sätt som Microsoft Excel. Så, till exempel, behöver du inte ange höjden på destinationsraden explicit, det värdet kopieras också.  

Nedan visas ett exempel på hur man kopierar en rad i ett kalkylblad. Det använder en mall Microsoft Excel-fil och kopierar den andra raden (med data, formatering, kommentarer, bilder och så vidare) och klistrar in den på den 12:e raden i samma kalkylblad.  

Du kan hoppa över steget som hämtar kälrradens höjd med [**Cells.rowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-boolean-cellsunittype-)-metoden och sedan sätter höjden på destinationsraden med [**Cells.rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-)-metoden eftersom [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-)-metoden automatiskt tar hand om radens höjd.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Row</title>
    </head>
    <body>
        <h1>Copy Row Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook.
            const wsTemplate = workbook.worksheets.get(0);

            // Copy the second row (index 1) with data, formatting, images and drawing objects
            // To the 16th row (index 15) in the worksheet.
            wsTemplate.cells.copyRow(wsTemplate.cells, 1, 15);

            // Save the excel file in Excel97To2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Vid kopiering av rader är det viktigt att notera relaterade bilder, diagram eller andra ritobjekt eftersom detta är detsamma med Microsoft Excel:  

1. Om källradens index är 5, kopieras bilden, diagrammet osv. om den finns i de tre raderna (startindexet är 4 och slutindexet är 6).  
1. De befintliga bilderna, diagrammen osv. i destinationsraden kommer inte att tas bort.  
{{% /alert %}}  

## **Hur man kopierar flera rader**  

Du kan också kopiera flera rader till ett nytt destination medan du använder [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-)-metoden som tar ett ytterligare parameter av typen heltal för att ange antalet kälrrader som ska kopieras.  

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

            // Instantiate workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Copy the first 3 rows to 7th row (indexes are zero-based)
            cells.copyRows(cells, 0, 6, 3);

            // Save the result and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Hur man kopierar kolumner**  

Aspose.Cells tillhandahåller [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-)-metoden i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-klassen, denna metod kopierar alla typer av data, inklusive formler - med uppdaterade referenser - samt värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källekän i kolumnen till destinationskolumnen.  

[**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-)-metoden tar följande parametrar:  

- källekon,  
- källkolumnens index och  
- destinationskolumnens index.  

Använd [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-)-metoden för att kopiera en kolumn inom ett blad eller till ett annat blad.  

Detta exempel kopierar en kolumn från ett blad och klistrar in den i ett blad i en annan arbetsbok.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Column Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const excelWorkbook1 = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Copy the first column from the first worksheet into the third column of the same worksheet.
            const cells = ws1.cells;
            cells.copyColumn(cells, cells.columns.get(0).index, cells.columns.get(2).index);

            // Autofit the column.
            ws1.autoFitColumn(2);

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Hur man kopierar flera kolumner**  

Liknande [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-)-metoden, ger API:erna Aspose.Cells också [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-)-metoden för att kopiera flera källekolumner till en ny plats.  

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an instance of Workbook class by loading the existing spreadsheet
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Copy the first 3 columns to the 7th column
            cells.copyColumns(cells, 0, 6, 3);

            // Save the result and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Hur man klistrar in rader och kolumner med klistringsalternativ**  

Aspose.Cells tillhandahåller nu [**PasteOptions**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/) medan man använder funktionerna [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) och [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). Det gör det möjligt att ställa in lämpligt klistringsalternativ liknande Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Change Chart Data Source</title>
    </head>
    <body>
        <h1>Change Chart Data Source Example</h1>
        <p>Select an Excel file (sampleChangeChartDataSource.xlsx) from your local machine.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteType, CopyOptions, PasteOptions } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = workbook.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = workbook.worksheets.add("DestSheet");

            // Set CopyOptions.ReferToDestinationSheet to true
            const options = new CopyOptions();
            options.referToDestinationSheet = true;

            // Set PasteOptions
            const pasteOptions = new PasteOptions();
            pasteOptions.pasteType = PasteType.Values;
            pasteOptions.onlyVisibleCells = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options, pasteOptions);

            // Save workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataSource.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
