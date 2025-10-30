---
title: Hantera område med JavaScript via C++
linktitle: Områden
type: docs
weight: 105
url: /sv/javascript-cpp/managing-ranges/
description: Lär dig hur du hanterar områden i Excel med Aspose.Cells for JavaScript via C++. Skapa områden, ställ in värden, stilar och utför olika operationer.
---

## **Introduktion**

I Excel kan du välja flera celler med hjälp av ett musklick; det valda området kallas "Range".

Till exempel kan du klicka på vänster musknapp i Cell "A1" i Excel och sedan dra till cell "C4". Det rektangulära området du valde kan också enkelt skapas som ett objekt med hjälp av Aspose.Cells for JavaScript via C++.

Så här skapar du ett område, sätter ett värde, tilldelar en stil och utför fler operationer på "Range"-objektet.

## **Hantera områden med hjälp av Aspose.Cells for JavaScript via C++**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samling.

### **Skapa område**

När du vill skapa ett rektangulärt område som sträcker sig över A1:C4 kan du använda följande kod:

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells (converted from getWorksheets().get(0).getCells() to properties)
            const cells = workbook.worksheets.get(0).cells;

            // Create Range A1:C4
            const range = cells.createRange("A1:C4");

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Range A1:C4 created successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Sätt värde i cellerna i området**

Säg att du har ett område med celler som sträcker sig över A1:C4. Matrisen gör 4 * 3 = 12 celler. De individuella områdscellerna är arrangerade sekventiellt: Område[0,0], Område[0,1], Område[0,2], Område[1,0], Område[1,1], Område[1,2], Område[2,0], Område[2,1], Område[2,2], Område[3,0], Område[3,1], Område[3,2].

Följande exempel visar hur man anger värden i cellerna i området.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Range Value Example</title>
    </head>
    <body>
        <h1>Range Value Example</h1>
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

            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            const range = cells.createRange("A1:C4");

            range.get(0, 0).value = "A1";
            range.get(0, 1).value = "B1";
            range.get(0, 2).value = "C1";
            range.get(3, 0).value = "A4";
            range.get(3, 1).value = "B4";
            range.get(3, 2).value = "C4";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeValueTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **Ställ in stil på cellerna i området**

Följande exempel visar hur man sätter stil på cellerna i intervallet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Range Style Example</h1>
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
            const resultDiv = document.getElementById('result');

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Gets Cells
            const cells = workbook.worksheets.get(0).cells;
            // Creates Range
            const range = cells.createRange("A1:C4");
            // Puts value
            range.get(0, 0).value = "A1";
            range.get(3, 2).value = "C4";
            // Sets Style
            let style00 = workbook.createStyle();
            style00.pattern = AsposeCells.BackgroundType.Solid;
            style00.foregroundColor = new AsposeCells.Color(255, 0, 0); // Red
            range.get(0, 0).style = style00;
            let style32 = workbook.createStyle();
            style32.pattern = AsposeCells.BackgroundType.HorizontalStripe;
            style32.foregroundColor = new AsposeCells.Color(0, 255, 0); // Green
            range.get(3, 2).style = style32;
            // Saves the Workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeStyleTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **Hämta aktuellt område av området**

CurrentRegion är en egenskap som returnerar ett områdesobjekt som representerar det aktuella området. 

Det aktuella området är ett område som begränsas av en kombination av tomma rader och tomma kolumner. Endast läsbar.

I Excel kan du få området CurrentRegion genom:
1. Välj ett område (range1) med musen.
2. Klicka på "Hem - Redigering - Sök & välj - Gå till special - Nuvarande område", eller använd "Ctrl+Shift+*", du kommer att se att Excel automatiskt hjälper dig att välja ett område (range2). Nu har du gjort det, range2 är Nuvarande område av range1.

Var god ladda ner följande testfil, öppna den i Excel, använd musen för att markera ett område "A1:D7", klicka sedan på "Ctrl+Shift+*", du kommer att se området "A1:C3" markerat.

[current_region.xlsx](current_region.xlsx)

Nu, vänligen kör följande exempel för att se hur det fungerar i Aspose.Cells:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Current Region Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Cells
            const cells = worksheet.cells;

            // Create Range
            const src = cells.createRange("A1:D7");

            // Get CurrentRegion (converted from getCurrentRegion())
            const A1C3 = src.currentRegion;

            // Save the workbook (no modifications were required by original code)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.current_region.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Current region obtained successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```


## **Fortsatta ämnen**
- [Autofyllt område i Excel-fil](/cells/sv/javascript-cpp/autofill-ranges/)
- [Kopiera områden i Excel](/cells/sv/javascript-cpp/copy-ranges-of-Excel/)
- [Kopiera områdesdata endast](/cells/sv/javascript-cpp/copy-range-data-only/)
- [Kopiera områdesdata med stil](/cells/sv/javascript-cpp/copy-range-data-with-style/)
- [Kopiera områdesstil endast](/cells/sv/javascript-cpp/copy-range-style-only/)
- [Skapa unionsspann](/cells/sv/javascript-cpp/create-union-range/)
- [Klipp och klistra område](/cells/sv/javascript-cpp/cut-and-paste-cells/)
- [Radera områden](/cells/sv/javascript-cpp/delete-ranges-from-Excel/)
- [Få adresscellsantal offset hela kolumnen och hela raden för området](/cells/sv/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Infoga områden](/cells/sv/javascript-cpp/insert-ranges-to-Excel/)
- [Sammanfoga eller dela upp cellområde](/cells/sv/javascript-cpp/merge-or-unmerge-range-of-cells/)
- [Flytta cellområde i ett kalkylblad](/cells/sv/javascript-cpp/move-range-of-cells-in-a-worksheet/)
- [Skapa arbetsbok och arbetsbladsspecifika namngivna områden](/cells/sv/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Sök och ersätt data i ett område](/cells/sv/javascript-cpp/search-and-replace-data-in-a-range/)
