---
title: Ändra sidfältslayout i pivottabell
linktitle: Ändra sidfältslayout i pivottabell
description: Lär dig hur du styr layouten för sidfältsområdet i en pivottabell med Aspose.Cells for Node.js via C++, inklusive inställning av visningsordning, radbrytningsantal och fältordning för sidfälten högst upp i pivottabellen.
keywords: Aspose.Cells, Node.js via C++-bibliotek, kalkylblad, pivottabell, sidfält, sidfältsordning, radbrytningsantal för sidfält, flytta sidfält
type: docs
weight: 191
url: /sv/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Den här artikeln är en fortsättning på ämnet **Lägg till sidfält i pivottabell**. Den visar hur du styr layouten för sidfältsområdet – remsan med filterkontroller högst upp i en pivottabell – inklusive visningsordning, radbrytningsantal och omordning av fält.
{{% /alert %}}
## **Introduktion**
En pivottabell i Microsoft Excel har ett dedikerat **sidfältsområde** som ligger ovanför tabellens rad-/kolumn-/datakropp. Det här området renderas som en remsa med filterkontroller i form av rullgardiner (en per sidfält) och det är vad slutanvändarna klickar på för att segmentera pivoten efter kriterier som år eller region. Aspose.Cells for Node.js via C++ modellerar detta område via samlingen `pivotTable.pageFields` och exponerar tre egenskaper som styr hur remsan visas visuellt:
- `pivotTable.pageFieldOrder` (ett `Aspose.Cells.PrintOrderType`-värde) avgör om ytterligare sidfält placeras *bredvid* de befintliga eller *under* dem.
- `pivotTable.pageFieldWrapCount` anger hur många sidfält som placeras per rad eller kolumn innan en radbrytning sker.
- `pivotTable.pageFields.move(currIndex, destIndex)` omordnar sidfälten utan att ändra ordningsläget.
Den här artikeln går igenom tre kodexempel som demonstrerar var och en av dessa operationer på en gemensam datamängd, så att du kan jämföra de resulterande layouterna sida vid sida.
## **Källdata**
Alla tre exempel nedan läser in dessa åtta rader med försäljningsdata i ett kalkylblad som heter `PivotData`. Data innehåller två kandidater för sidfält (`Year`, `Region`), en kandidat för radfält (`Fruit`) och ett mått (`Amount`), vilket gör att sidfältsremsan blir meningsfull att undersöka.
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
Alla åtta rader fylls i i varje kodexempel, i identisk ordning, så att källdata aldrig skiljer sig mellan scenarierna – endast layoutegenskaperna för sidfältet gör det.
## **Exempel 1: Över sedan ned**
I det första scenariot konfigurerar vi de två sidfälten (`Year`, `Region`) så att de visas **sida vid sida i en enda rad** högst upp i pivottabellen. Vi tilldelar `Fruit` till radaxeln, placerar `Year` först och `Region` sedan på sidaxeln (ordningen på `addFieldToArea`-anropen avgör startindexet), lägger till `Amount` (Summa) som datafält och anger sedan `pageFieldOrder` till `PrintOrderType.OverThenDown` med `pageFieldWrapCount = 2`. Med `OverThenDown` och ett radbrytningsantal på 2 läggs de två sidfälten ut horisontellt sida vid sida i en enda rad högst upp i pivottabellen, så att remsan upptar en rad med bredden två.
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// Rubriker (rad 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Rad 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Rad 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Rad 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Rad 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Rad 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Rad 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Rad 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Rad 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Lägg till PivotTableReport-blad
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// Skapa pivottabell med källa från PivotData!A1:D9 placerad vid A1 på PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// Lägg till fält
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Frukt
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // År
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Belopp
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// Konfigurera layout för sidfältsområde: placera sidfält först horisontellt, radbryt efter varannan
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// Uppdatera och beräkna
pivotTable.calculateData();

// Spara
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **Exempel 2: Ned sedan över**
I det här exemplet placerar vi `Fruit` på radaxeln, `Year` och `Region` på sidaxeln (med `Year` först) och `Amount` (Summa) som datafält – exakt som i Exempel 1. Vi anger sedan `pageFieldOrder` till `PrintOrderType.DownThenOver` och `pageFieldWrapCount` till `2`. Med `DownThenOver` och ett radbrytningsantal på 2 staplas de två sidfälten vertikalt – `Year` överst, `Region` direkt under – och bildar en enda kolumn högst upp i pivottabellen. Remsan upptar därför två rader med bredden ett, i motsats till Exempel 1.
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);

const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
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
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **Exempel 3: Flytta ett sidfält**
I det tredje scenariot behåller vi denna datamängd och fälttilldelning, anger en neutral layout (`OverThenDown` med radbrytningsantal `2`) och demonstrerar sedan `pageFields.move`-operationen. Anropet `move(0, 1)` flyttar sidfältet på index 0 (`Year`) till position 1, och sidfältet som var på position 1 (`Region`) flyttas till position 0. Efter detta anrop är `Region` det första sidfältet och `Year` det andra. Radbrytning och ordningsläge är oförändrade, så remsan renderas fortfarande horisontellt sida vid sida – bara ordningen på de två rullgardinerna har bytts ut.
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();

const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);

const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **Relaterade artiklar**
- [Lägg till sidfält i pivottabell](/cells/sv/nodejs-cpp/add-page-field-in-pivot-table/) — föräldrasidan som introducerar hur sidfält läggs till i en pivottabell.
- [Rad- och kolumnfält i pivottabell](/cells/sv/nodejs-cpp/row-and-column-fields/) — täcker tilldelning av fält till rad- och kolumnaxlarna, som kompletterar arbetet med sidaxeln som visas här.
- [Hantera värdefält i pivottabell](/cells/sv/nodejs-cpp/manage-value-fields/) — beskriver hur dataområdet (värde) konfigureras, inklusive `Sum`-aggregeringen som används i den här artikeln.
- [Uppdatera pivottabell](/cells/sv/nodejs-cpp/refresh-pivot-table/) — förklarar `refreshData` och `calculateData`, vilka krävs efter omordning av sidfält.
- [Tillämpa stil på pivottabell](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/) — visar hur den renderade pivottabellen formateras efter att sidfältsremsan har lagts ut.
{{< app/cells/assistant language="nodejs-cpp" >}}