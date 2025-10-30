---
title: Hantera kalkylblad i Microsoft Excel filer med JavaScript via C++
linktitle: Arbetsblad
type: docs
weight: 90
url: /sv/javascript-cpp/manage-worksheets/
description: Lägg till, ta bort och aktivera kalkylblad med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med hjälp av Aspose.Cells flexibla API. Denna ämne beskriver tillvägagångssätt för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.
{{% /alert %}}

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad uttrycks av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) erbjuder ett brett utbud av egenskaper och metoder för att hantera kalkylblad.

## **Lägga till kalkylblad i en ny Excelfil**

För att skapa en ny Excel-fil programmatiskt:

1. Skapa ett objekt av klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).  
2. Anropa [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#add-sheettype-)-metoden för [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)-klassen. Ett tomt kalkylblad läggs automatiskt till i Excel-filen. Det kan refereras till genom att passera det nya kalkylbladets index till [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samlingen.  
3. Få en referens till ett kalkylblad.  
4. Utför arbete på kalkylbladen.  
5. Spara den nya Excel-filen med nya kalkylblad genom att anropa [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)-metoden i [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Worksheet Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Get current worksheet count (converted from getWorksheets().getCount())
            const i = workbook.worksheets.count;

            // Add a new worksheet (converted from getWorksheets().add())
            workbook.worksheets.add();

            // Obtain the newly added worksheet by index (converted from getWorksheets().get(i))
            const worksheet = workbook.worksheets.get(i);

            // Set the name of the newly added worksheet (converted from setName)
            worksheet.name = "My Worksheet";

            // Save the workbook to XLS format and prepare download
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Lägga till kalkylblad i ett designerkalkylblad**

Processen för att lägga till kalkylblad i ett designad kalkylark är densamma som att lägga till ett nytt kalkylblad, förutsatt att Excel-filen redan finns och ska öppnas innan kalkylblad läggs till. En designer-kalkylark kan öppnas med klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Worksheet</title>
    </head>
    <body>
        <h1>Add Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Setting the name of the newly added worksheet
            worksheet.name = "My Worksheet";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Tillgång till kalkylblad med hjälp av kalkylbladsnamn**

Få tillgång till vilket kalkylblad som helst genom att ange dess namn eller index.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example: Read Cell Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing a worksheet using its sheet name
            const worksheet = workbook.worksheets.get("Sheet1");
            const cell = worksheet.cells.get("A1");

            console.log(cell.value);
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.value}</p>`;
        });
    </script>
</html>
```

## **Ta bort kalkylblad med hjälp av kalkylbladsnamn**

För att ta bort kalkylblad från en fil, anropa metoden [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) för klassen [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection). Passa kalkylbladets namn till metoden [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) för att ta bort ett specifikt kalkylblad.

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Removing a worksheet using its sheet name
            workbook.worksheets.removeAt("Sheet1");

            // Save workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ta bort kalkylblad med hjälp av kalkylbladsindex**

Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte känner till kalkylbladets namn, använd en överbelastad version av metoden [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) som tar kalkylbladets index istället för dess namn.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Remove First Worksheet</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Removing a worksheet using its sheet index
            workbook.worksheets.removeAt(0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Aktivera kalkylblad och gör en aktiv cell i kalkylbladet**

Ibland behöver du ett specifikt arbetsblad att vara aktivt och visas när en användare öppnar en Microsoft Excel-fil i Excel. På samma sätt kan du vilja aktivera en specifik cell och ställa in rullningslisterna för att visa den aktiva cellen. Aspose.Cells kan utföra alla dessa uppgifter.

Ett **aktivt kalkylblad** är ett kalkylblad du arbetar med: det aktiva kalkylbladets namn på fliken är fetstil som standard.

En **aktiv cell** är en markerad cell, den cell där data matas in när du börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen är markerad med en tjock kantlinje.

### **Aktivera blad och göra en cell aktiv**

Aspose.Cells tillhandahåller specifika API-anrop för att aktivera ett blad och en cell. Till exempel är [**WorksheetCollection.activeSheetIndex**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#activeSheetIndex--)-egenskapen användbar för att ställa in det aktiva bladet i en arbetsbok. På samma sätt används [**Worksheet.activeCell**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#activeCell--)-egenskapen för att ställa in och hämta en aktiv cell i arbetsbladet.

För att säkerställa att de horisontella eller vertikala rullningslisterna är vid den rad- och kolumnindexposition du vill visa specifika data, använd egendoms [**Worksheet.firstVisibleRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleRow--) och [**Worksheet.firstVisibleColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleColumn--).

Följande exempel visar hur du aktiverar ett kalkylblad och gör en cell aktiv i det. I den genererade utdatan kommer rullningsfälten att skrollas för att göra den 2: a raden och den 2: a kolumnen som deras första synliga rad och kolumn.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Add a worksheet if collection is empty
            const worksheets = workbook.worksheets;
            if (worksheets.count === 0) {
                worksheets.add();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = worksheets.get(0);

            // Get the cells in the worksheet.
            const cells = worksheet1.cells;

            // Input data into B2 cell.
            const cell = cells.get(1, 1);
            cell.value = "Hello World!";

            // Set the first sheet as an active sheet.
            worksheets.activeSheetIndex = 0;

            // Set B2 cell as an active cell in the worksheet.
            worksheet1.activeCell = "B2";

            // Set the B column as the first visible column in the worksheet.
            worksheet1.firstVisibleColumn = 1;

            // Set the 2nd row as the first visible row in the worksheet.
            worksheet1.firstVisibleRow = 1;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Kopiera och flytta arbetsblad](/cells/sv/javascript-cpp/copying-and-moving-worksheets/)  
- [Räkna antalet celler i kalkylbladet](/cells/sv/javascript-cpp/count-number-of-cells-in-the-worksheet/)  
- [Upptäcka tomma kalkylblad](/cells/sv/javascript-cpp/detecting-empty-worksheets/)  
- [Ta reda på om kalkylbladet är Dialog sheet](/cells/sv/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Få arbetsbladets unika id](/cells/sv/javascript-cpp/get-worksheet-unique-id/)  
- [Skapa, manipulera eller ta bort scenarier från kalkylblad](/cells/sv/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Hantera sidbrytningar](/cells/sv/javascript-cpp/managing-page-breaks/)  
- [Sidlayoutfunktioner](/cells/sv/javascript-cpp/page-setup-features/)  
- [Använd Sheet.SheetId-egenskapen i OpenXml med hjälp av Aspose.Cells](/cells/sv/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Kalkylbladsvyer](/cells/sv/javascript-cpp/worksheet-views/)
