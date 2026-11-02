---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig hur du endast visar de högst eller lägst rangordade objekten i ett pivotfält med Aspose.Cells for Node.js via C++. Artikeln beskriver metoden Top10AutoShow för Excel 97-2003, hur alternativ läses med Top10AutoShowSettings och filtret för topp 10 i Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Node.js via C++, pivottabell, topp 10, automatisk topp 10-visning, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /sv/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar varje objekt i ett radfält kan vara svårläst när fältet har dussintals medlemmar. En topp 10-rapport behåller endast de högst eller lägst rangordade objekten, vilket är precis vad rangordningsrapporter behöver — "topp 5 produkter efter intäkter" eller "de 3 lägsta regionerna efter antal försäljningar". Aspose.Cells stöder två mekanismer för detta, och de motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** — metoden `pivotField.top10AutoShow()`. Detta är den klassiska inställningen "Visa de översta/nedersta N objekten" som lagras direkt i pivotfältet. Den fungerar i alla versioner av Excel, oavsett hur gamla eller nya de är, eftersom den ingår i det ursprungliga formatet för pivottabeller.
- **Excel 2007-365 topp 10-filter** — metoden `pivotField.filterTop10()`. Detta är det moderna värdefiltret för topp 10 som finns under Värdefilter i fältmenyn. Det lagras som ett `PivotFilter`-objekt kopplat till fältet och erbjuder rangordning efter antal objekt eller procent.

## **Visa topp 10 i Excel 97-2003 (top10AutoShow)**
Den klassiska AutoShow-inställningen konfigureras med ett enda anrop till `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)`:
- `isAutoShow` — aktiverar eller inaktiverar AutoShow-inställningen för fältet.
- `isTop` — `true` behåller de högst rangordade objekten (Topp), `false` de lägst rangordade (Nederst).
- `count` — hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rankBy` — det nollbaserade indexet för **datafältet** vars värden används för att rangordna objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rangordningen kan styras av ett värdefält eller av fältet självt. Det finns två naturliga varianter, som visas nedan.

### **Rangordning efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel "Sum of Sales". Följande exempel skapar en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`) och visar sedan de två sporterna med högst försäljning. `rankBy` är 0 eftersom "Sum of Sales" är datafältet på index 0.

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Rangordning efter fältet självt**
Ett fält kan också rangordnas efter sig självt – ange -1 som `rankBy`. Inga ytterligare datafält behövs för denna variant; fältet behöver bara placeras i rad- eller kolumnområdet. Följande exempel visar de tre lägst rangordade sporterna när rangordningen görs efter fältet självt. När inställningen sparas utelämnas attributet `rankBy` i pivottabellens XML eftersom -1 är formatets standardvärde, och `top10AutoShowSettings.getRankBy()` returnerar -1.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Läsa aktuella alternativ (Top10AutoShowSettings)**
Metoden `pivotField.getTop10AutoShowSettings()` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som exponerar de AutoShow-alternativ som för närvarande lagras på fältet. Använd det för att kontrollera hur en befintlig arbetsbok eller en pivottabell som du nyligen har konfigurerat kommer att presentera sina objekt – inklusive arbetsböcker som har lästs in från en fil.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

De fyra egenskaperna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), så att de värden som läses tillbaka är de värden som tillämpas av alla Excel-versioner.

## **Obs**

{{% alert color="primary" %}}
- De direkta åtkomstmetoderna `isAutoShow`, `getIsAscendShow()`, `getAutoShowCount()` och `getAutoShowField()` för `PivotField` är markerade som föråldrade. Använd `Top10AutoShowSettings`-objektet i stället: `pivotField.isAutoShow` ersätts av `top10AutoShowSettings.isAutoShow`, `pivotField.getIsAscendShow()` ersätts av `top10AutoShowSettings.isTop`, `pivotField.getAutoShowCount()` ersätts av `top10AutoShowSettings.getAutoShowCount()`, och `pivotField.getAutoShowField()` ersätts av `top10AutoShowSettings.getRankBy()`. Metoden `pivotField.top10AutoShow()` är det sätt som stöds för att ändra inställningarna.
- `top10AutoShow()` fungerar för rad- och kolumnfält. Ett fält som endast finns i sidområdet (filterområdet) kan inte rangordnas på detta sätt, eftersom dess objekt inte placeras i pivottabellens kropp.
{{% /alert %}}

## **Excel 2007-365: topp 10-filter (filterTop10)**
Moderna Excel-versioner visar topp 10 som ett värdefilter i fältmenyn (Värdefilter, topp 10...). Aspose.Cells modellerar det med metoden `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` — det nollbaserade indexet för datafältet vars aggregerade värden rangordnar objekten.
- `type` — vad `itemCount` betyder. `PivotFilterType.Count` behåller ett bestämt antal objekt (dialogens alternativ för antal objekt). `PivotFilterType.Percent` behåller en viss procentandel av objekten, så att `itemCount` är procentandelen – 30 behåller de översta 30 procenten. `PivotFilterType.SUM` rangordnar efter hur stor del av det ackumulerade värdet som omfattas.
- `isTop` — `true` för Topp, `false` för Nederst.
- `itemCount` — N-värdet i topp N; enheten beror på `type`.

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` och `filterTop10` är två separata funktioner. AutoShow skriver den klassiska uppsättningen av attribut, inklusive `autoShow`, på pivotfältet och stöds av alla Excel-versioner från Excel 97 och framåt. `filterTop10` skriver en modern `PivotFilter`-post, som kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version återgår en pivottabell som använder det moderna filtret till att visa alla objekt. För dokument som måste skapas och återläses med äldre bearbetningsverktyg bör du välja `top10AutoShow`; för moderna arbetsböcker bör du välja `filterTop10` eftersom topp 10-filtret kan kombineras med de andra värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/nodejs-cpp/refresh-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}