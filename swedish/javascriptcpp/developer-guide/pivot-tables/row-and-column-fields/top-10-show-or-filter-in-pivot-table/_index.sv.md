---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig att endast visa de högst eller lägst rankade objekten i ett pivotfält med Aspose.Cells for JavaScript via C++. Artikeln beskriver AutoShow-egenskaperna i Excel 97-2003 (isAutoShow och andra egenskaper), hur du läser tillbaka alternativen och Top 10-filtret i Excel 2007-365 via filterTop10.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, pivottabell, topp 10, AutoShow, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /sv/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar alla objekt i ett radfält kan vara svårläst när fältet har flera tiotal medlemmar. En topp 10-rapport behåller endast de högst eller lägst rankade objekten, vilket är exakt vad rankningsrapporter behöver – ”topp 5 produkter per intäkt” eller ”de 3 regionerna med lägst försäljningsantal”. Aspose.Cells stöder två mekanismer för detta, och de motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** – de fyra `PivotField`-egenskaperna `isAutoShow`, `isAscendShow`, `autoShowCount` och `autoShowField`. Detta är den klassiska inställningen ”Visa de bästa/sämsta N objekten” som lagras direkt på pivotfältet. Den fungerar i alla Excel-versioner, både gamla och nya, eftersom den ingår i det ursprungliga pivottabellformatet.
- **Excel 2007-365 Topp 10-filter** – metoden `PivotField.filterTop10()`. Detta är det moderna värdefiltret Topp 10 som finns under Värdefiltrar i fältmenyn. Det lagras som ett `PivotFilter`-objekt kopplat till fältet och erbjuder rankning baserad på antal objekt och procent.

## **Visa topp 10 i Excel 97-2003 (AutoShow)**
Den klassiska AutoShow-funktionen konfigureras genom att tilldela fyra egenskaper på `PivotField`:
- `isAutoShow` – aktiverar eller inaktiverar AutoShow-inställningen på fältet.
- `isAscendShow` – `false` behåller de högst rankade objekten (Topp), `true` behåller de lägst rankade objekten (Botten).
- `autoShowCount` – antalet objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `autoShowField` – det nollbaserade indexet för det **datafält** vars värden rangordnar objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rankningen kan baseras på ett värdefält eller på fältet självt. Det finns två naturliga varianter, som visas nedan.

### **Rangordna efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel ”Summa av försäljning”. Följande exempel skapar en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`) och visar sedan de två sportgrupperna med högst försäljning. `rankBy` är 0 eftersom ”Summa av försäljning” är datafältet med index 0.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Visa de två översta objekten, rankade efter "Sum of Sales" (index 0 för datafältet)
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Rangordna efter fältet självt**
Ett fält kan också användas för att rangordna sina egna objekt – ange -1 för `autoShowField`. Den här varianten kräver inget extra datafält; fältet behöver bara finnas i rad- eller kolumnområdet. Följande exempel visar de tre lägst rankade sportgrupperna. När inställningen sparas utelämnas attributet `rankBy` från pivottabellens XML eftersom -1 är standardvärdet för formatet, och `autoShowField` läses tillbaka som -1.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Visa de 3 lägsta objekten rankade efter fältet självt (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Läsa aktuella AutoShow-inställningar**
De `PivotField`-egenskaperna `isAutoShow`, `isAscendShow`, `autoShowCount` och `autoShowField` visar vilka AutoShow-inställningar som för närvarande lagras på fältet. Använd dem för att kontrollera hur en befintlig arbetsbok eller en pivottabell som du nyss har konfigurerat kommer att presentera sina objekt. Det gäller även arbetsböcker som har lästs in från en fil.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

De fyra egenskaperna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), så att de värden som läses tillbaka är de värden som alla Excel-versioner kommer att använda.

## **Obs**

{{% alert color="primary" %}}
- När du har ändrat någon av AutoShow-egenskaperna ska du anropa `pivotTable.calculateData()` igen – inställningarna träder först i kraft i den renderade layouten efter nästa omberäkning.
- AutoShow-inställningarna fungerar med rad- och kolumnfält. Ett fält som endast finns i sidområdet (filterområdet) kan inte rangordnas på det här sättet, eftersom dess objekt inte visas i pivottabellens innehåll.
{{% /alert %}}

## **Excel 2007-365: Topp 10-filter (filterTop10)**
Moderna Excel-versioner erbjuder Topp 10 som ett värdefilter i fältmenyn (Värdefiltrar, Topp 10...). Aspose.Cells modellerar det med metoden `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` – det nollbaserade indexet för datafältet vars aggregerade värden rangordnar objekten.
- `type` – anger hur `itemCount` ska tolkas. `PivotFilterType.Count` behåller ett fast antal objekt (alternativet Objekt i dialogrutan). `PivotFilterType.Percent` behåller en procentandel av objekten, så att `itemCount` i själva verket är procentandelen – 30 behåller de bästa 30 procenten. `PivotFilterType.Sum` rangordnar objekt efter täckningen av ackumulerade värden.
- `isTop` – `true` för Topp, `false` för Botten.
- `itemCount` – talet N i Topp N; enheten beror på `type`.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
AutoShow-egenskaperna och `filterTop10` är två separata funktioner. AutoShow skriver de klassiska AutoShow-attributen på pivotfältet, bland dem `autoShow`. De tillämpas av alla Excel-versioner från Excel 97 och senare. `filterTop10` skriver en modern `PivotFilter`-post, som kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version visas alla objekt i en pivottabell som använder det moderna filtret. För dokument som måste bearbetas fram och tillbaka med äldre verktyg bör du använda AutoShow-egenskaperna; för moderna arbetsböcker bör du använda `filterTop10` eftersom filtret kan kombineras med de övriga värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}