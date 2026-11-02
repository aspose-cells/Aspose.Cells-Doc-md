---
title: Ändra sidfältens layout i pivottabell
linktitle: Ändra sidfältens layout i pivottabell
description: Lär dig hur du styr layouten för sidfältsområdet i en pivottabell med Aspose.Cells for JavaScript via C++, inklusive hur du anger visningsordningen, brytningsantalet och sidfältens ordning längst upp i pivottabellen.
keywords: Aspose.Cells for JavaScript via C++, kalkylblad, pivottabell, sidfält, sidfältsordning, brytningsantal för sidfält, flytta sidfält
type: docs
weight: 191
url: /sv/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Den här artikeln bygger vidare på ämnet **Lägg till sidfält i pivottabell**. Den visar hur du styr layouten för sidfältsområdet – remsan med filterkontroller längst upp i en pivottabell – inklusive visningsordning, brytningsantal och omordning av sidfält.
{{% /alert %}}

## **Introduktion**
En pivottabell i Microsoft Excel har ett dedikerat **sidfältsområde** ovanför tabellens rad-, kolumn- och dataområde. Området visas som en remsa med filterkontroller med rullmeny, en per sidfält. Via dessa kontroller kan slutanvändarna filtrera pivottabellen efter kriterier som år eller region. Aspose.Cells representerar det här området med samlingen `pivotTable.pageFields` och exponerar tre egenskaper som styr den visuella layouten av remsan:
- `pivotTable.pageFieldOrder` (ett `Aspose.Cells.PrintOrderType`-värde) avgör om ytterligare sidfält ska placeras *bredvid* de befintliga eller *under* dem.
- `pivotTable.pageFieldWrapCount` anger hur många sidfält som placeras per rad eller kolumn innan en brytning sker.
- `pivotTable.pageFields.move(currIndex, destIndex)` ordnar om sidfälten utan att ändra ordningsläget.
Den här artikeln går igenom tre kodexempel som med samma datamängd visar respektive åtgärd, så att du kan jämföra resultaten sida vid sida.

## **Källdata**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alla åtta raderna innehåller data i varje kodexempel och är ordnade på samma sätt. Därför är källdatan identisk mellan scenarierna; endast layoutegenskaperna för sidfälten skiljer sig åt.

## **Exempel 1: Överst och sedan nedan**
I det första scenariet konfigurerar vi de två sidfälten (`Year`, `Region`) så att de visas **bredvid varandra i en enda rad** längst upp i pivottabellen. Vi placerar `Fruit` på radaxeln och lägger till `Year` först och `Region` sedan som sidfält. Ordningen på anropen till `addFieldToArea` bestämmer startindexet. Därefter lägger vi till `Amount` (Sum) som datafält och anger `pivotTable.pageFieldOrder` till `PrintOrderType.OverThenDown` med `pivotTable.pageFieldWrapCount = 2`. Med `OverThenDown` och ett brytningsantal på 2 placeras de två sidfälten horisontellt bredvid varandra i en enda rad längst upp i pivottabellen. Remsan upptar då en rad med två fält.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // Rubriker (rad 0)
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // Rad 1: Apple, 2022, North, 150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // Rad 2: Apple, 2023, North, 180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // Rad 3: Banana, 2022, South, 120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // Rad 4: Banana, 2023, South, 140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // Rad 5: Cherry, 2022, East, 200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // Rad 6: Cherry, 2023, East, 220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // Rad 7: Grape, 2022, West, 90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // Rad 8: Grape, 2023, West, 110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // Lägg till kalkylbladet PivotTableReport
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // Skapa pivottabell med källan PivotData!A1:D9, placerad på A1 i PivotTableReport
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Lägg till fält
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // Konfigurera layouten för sidfältsområdet: placera sidfälten horisontellt först, radbryt efter varannat
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // Uppdatera och beräkna
            pivotTable.calculateData();
            // Spara
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Exempel 2: Nedan och sedan överst**
I det här exemplet placerar vi `Fruit` på radaxeln, `Year` och `Region` som sidfält (med `Year` först) och `Amount` (Sum) som datafält – exakt som i Exempel 1. Vi anger sedan `pivotTable.pageFieldOrder` till `PrintOrderType.DownThenOver` och `pivotTable.pageFieldWrapCount` till `2`. Med `DownThenOver` och ett brytningsantal på 2 placeras de två sidfälten vertikalt, med `Year` överst och `Region` direkt under, så att de bildar en enda kolumn längst upp i pivottabellen. Remsan upptar därför två rader med ett fält vardera, till skillnad från Exempel 1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Exempel 3: Flytta ett sidfält**
I det tredje scenariet behåller vi samma datamängd och fältfördelning. Vi anger ett neutralt layoutläge (`OverThenDown` med brytningsantal `2`) och visar sedan hur `pivotTable.pageFields.move` fungerar. Anropet `move(0, 1)` flyttar sidfältet vid index 0 (`Year`) till position 1, och sidfältet på position 1 (`Region`) förskjuts till position 0. Efter anropet är `Region` det första sidfältet och `Year` det andra. Brytningsantalet och ordningsläget är oförändrade, så att remsan fortfarande visas horisontellt, med fälten bredvid varandra. Endast ordningen mellan de två rullmenyerna har ändrats.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Relaterade artiklar**
- [Lägg till sidfält i pivottabell](/cells/sv/javascript-cpp/add-page-field-in-pivot-table/) – huvudartikeln som introducerar hur sidfält läggs till i en pivottabell.
- [Hantera värdefält i pivottabell](/cells/sv/javascript-cpp/manage-value-fields/) – beskriver hur dataområdet (värdeområdet) konfigureras, inklusive aggregeringen `Sum` som används i den här artikeln.
- [Tillämpa en stil på pivottabell](/cells/sv/javascript-cpp/apply-style-to-pivot-table/) – visar hur du formaterar den renderade pivottabellen efter att sidfältsremsan har fått sin layout.

{{< app/cells/assistant language="javascript-cpp" >}}