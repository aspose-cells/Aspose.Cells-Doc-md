---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig hur du endast visar de objekt som har högst eller lägst rang i ett pivotfält i Aspose.Cells for Node.js via Java. Den här artikeln beskriver metoden Top10AutoShow för Excel 97-2003, hur du läser alternativ med Top10AutoShowSettings och filtret Top 10 för Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Node.js via Java, pivottabell, topp 10, automatisk visning, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /sv/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar varje objekt i ett radfält kan vara svår att läsa när fältet har dussintals medlemmar. En topp 10-rapport behåller endast de objekt som har högst eller lägst rang, vilket är precis vad rankningsrapporter behöver – "topp 5 produkter efter intäkt" eller "de tre regionerna med lägst försäljningsantal". Aspose.Cells stöder två mekanismer för detta, som motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** – metoden `PivotField.top10AutoShow()`. Det är den klassiska inställningen "Visa de översta/understa N objekten" som lagras direkt i pivotfältet. Den fungerar i alla Excel-versioner, äldre och nyare, eftersom den ingår i det ursprungliga pivottabellformatet.
- **Excel 2007-365 Top 10-filter** – metoden `PivotField.filterTop10()`. Det är det moderna värdefiltret för topp 10 som finns under Värdefiltrar i fältmenyn. Det lagras som ett `PivotFilter`-objekt kopplat till fältet och erbjuder rankning baserad på antal objekt respektive procentandel.

## **Visa topp 10 i Excel 97-2003 (Top10AutoShow)**
Den klassiska AutoShow-funktionen konfigureras med ett enda anrop till `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` – aktiverar eller inaktiverar AutoShow-inställningen på fältet.
- `isTop` – `true` behåller de objekt med högst rang (topp), medan `false` behåller de objekt med lägst rang (botten).
- `count` – hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rankBy` – det nollbaserade indexet för **datafältet** vars värden används för att rangordna objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rankningen kan baseras på ett värdefält eller på fältet självt. Det finns två möjliga varianter, som visas nedan.

### **Rankning efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel Sum of Sales. Följande exempel bygger en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`) och visar sedan de två sporten med högst försäljning. `rankBy` är 0 eftersom "Sum of Sales" är datafältet på index 0.

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Rankning efter fältet självt**
Ett fält kan också rangordna sina egna objekt – ange -1 som `rankBy`. Inget extra datafält behövs för denna variant; fältet behöver endast ligga i rad- eller kolumnområdet. Följande exempel visar de tre sporten med lägst rang. När inställningen sparas utelämnas attributet `rankBy` från pivottabellens XML eftersom -1 är standardvärdet för formatet, och `getTop10AutoShowSettings().getRankBy()` läser tillbaka värdet -1.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Läsa aktuella alternativ (Top10AutoShowSettings)**
Metoden `PivotField.getTop10AutoShowSettings()` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som exponerar de AutoShow-alternativ som för närvarande lagras på fältet. Använd den för att kontrollera hur objekten i en befintlig arbetsbok eller i en pivottabell som du nyligen har konfigurerat kommer att visas. Det gäller även arbetsböcker som har lästs in från en fil.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Gettermetoderna `isAutoShow()`, `isTop()`, `getAutoShowCount()` och `getRankBy()` motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). De lästa värdena är därför de värden som alla Excel-versioner respekterar.

## **Obs**

{{% alert color="primary" %}}
- De direkta `PivotField`-gettermetoderna `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` och `getAutoShowField()` är föråldrade. Använd i stället det objekt som returneras av `getTop10AutoShowSettings()`: `isAutoShow()` motsvaras av `getTop10AutoShowSettings().isAutoShow()`, `isAscendShow()` motsvaras av `getTop10AutoShowSettings().isTop()`, `getAutoShowCount()` motsvaras av `getTop10AutoShowSettings().getAutoShowCount()` och `getAutoShowField()` motsvaras av `getTop10AutoShowSettings().getRankBy()`. Den metod som stöds för att ändra inställningarna är `top10AutoShow()`.
- `top10AutoShow()` fungerar med rad- och kolumnfält. Ett fält som endast finns i sidoområdet (filterområdet) kan inte rangordnas på det här sättet, eftersom dess objekt inte placeras i pivottabellens huvudområde.
{{% /alert %}}

## **Excel 2007-365: Top 10-filter (FilterTop10)**
I moderna Excel-versioner finns topp 10 som ett värdefilter i fältmenyn (Värdefiltrar, Topp 10...). Aspose.Cells modellerar det med metoden `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` – det nollbaserade indexet till det datafält vars aggregerade värden används för att rangordna objekten.
- `type` – vad `itemCount` betyder. `PivotFilterType.COUNT` behåller ett fast antal objekt (dialogens alternativ Objekt). `PivotFilterType.PERCENT` behåller en procentandel av objekten, så `itemCount` själva är procenttalet – 30 behåller de översta 30 procenten. `PivotFilterType.SUM` rangordnar posterna efter den kumulativa värdeandelen.
- `isTop` – `true` väljer topp, `false` väljer botten.
- `itemCount` – N i topp N; enheten beror på `type`.

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` och `filterTop10()` är två separata funktioner. AutoShow skriver det klassiska `autoShow`-attributet på pivotfältet. Inställningen tillämpas av alla Excel-versioner från Excel 97 och framåt. `filterTop10()` skriver en modern `PivotFilter`-post, vilket kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version visas alla objekt i en pivottabell som använder det moderna filtret. För dokument som måste passera fram och tillbaka via äldre verktyg bör du föredra `top10AutoShow()`; för moderna arbetsböcker bör du föredra `filterTop10()` eftersom det kan kombineras med de andra värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/nodejs-java/refresh-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}