---
title: Uppdatera pivottabeller och pivottillgångar i Aspose.Cells för Node.js via C++
linktitle: Uppdatera pivottabeller och pivottillgångar i Aspose.Cells för Node.js via C++
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells för Node.js via C++ med v26.7+ för pivottabeller, Den här artikeln täcker refreshAll, refreshPivotTables, PivotCache.refresh, calculateData och getPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, Node.js via C++, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells tillhandahåller ett lagerat uppdaterings-API som låter dig ladda om pivottabelldata i fyra olika omfattningar — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells för Node.js via C++ v26.7** är den äldre metoden `PivotTable.RefreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cachevana API:er som beskrivs i den här artikeln.
{{% /alert %}}

## Introduction
Att uppdatera en pivottabell är sällan en enda åtgärd. I bakgrunden underhåller Aspose.Cells en lagerad dataket som förbinder din ursprungliga källdata med de renderade värden du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.
De fyra lagren i dataket är:
1. **Datakälla** — den ursprungliga kalkylbladsintervallet, databasfrågan eller sammanfogningsintervallet där de råa värdena finns.
2. **PivotCache** — ögonblicksbilden av källdata i minnet. Varje pivottabell är byggd på en `PivotCache`; här samlas all data in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rader, kolumner, värden och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från källdata.
4. **Cells** — kalkylblads-`Cells` som `PivotTable` renderar sina beräknade värden och format till.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) anger var cache-datan kom från. Från och med v26.7 stöder `PivotCache.refresh()` endast **`Sheet`**- och **`Consolidation`**-kältyperna — alltså data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar, etc.) är ännu inte uppdaterbara via cache-API:et.
På grund av denna kedja finns två fundamentala uppdateringsvägar i Aspose.Cells:
- **`PivotTable.calculateData()`** — beräknar om visningen för en `PivotTable` från redan cachad data, utan någon round-trip tillbaka till källdata.
Alla scenario i den här artikeln använder kalkylblads-cell-källdata, så kältypen är `Sheet` och uppdateringsåtgärder beter sig enligt beskrivningen.
{{% /alert %}}

## Quick Start
Om du bara behöver den kortaste möjliga koden som uppdaterar varje pivottabell i arbetsboken räcker en enda anrop:

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Allt annat i den här artikeln förklarar när man bör välja ett mindre omfattande API istället.

## Required Imports
Alla JavaScript-exempel i den här artikeln förutsätter att Aspose.Cells för Node.js via C++-modulen har laddats och att pivottyperna finns i `Aspose.Cells.Pivot`-namnrymden. En typisk inställning är:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (eller åtkomst via `AsposeCells.Pivot.PivotFieldType`)

## Refresh All Pivot Tables in the Workbook
När du behöver säkerställa att varje pivottillgång och varje pivottabell i arbetsboken återspeglar senaste källdata är det enklaste och mest omfattande API:et `Workbook.refreshAll()`. Ett enda anrop går igenom hela arbetsboken — uppdaterar varje `PivotCache` från dess källa och beräknar sedan om varjeberoende `PivotTable`. Detta är den rekommenderade metoden för generella, fullständiga dokumentuppdateringar där prestanda inte är en fråga.
Följande exempel bygger en arbetsbok med en Fruit/Year/Amount-källintervall, skapar en pivottabell, ändrar några källvärden och använder sedan `refreshAll()` för att uppdatera allt i ett enda anrop.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);
// Add a pivot table: source range "A1:C9", destination cell "E3"
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
Ibland behöver du bara uppdatera pivottabellerna som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refreshPivotTables()`, som är begränsad till en enskild `Worksheet`-instans.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
När du vill ha finsteglig kontroll över en enskild pivottabell ger cache-baserade API:et två alternativ. Valet mellan dem beror på vad som faktiskt ändrats: underliggande källdata eller bara vy- eller layoutinställningarna för pivottabellen själv.

### Source Data Changed — Use `PivotCache.refresh()`
Om underliggande källdata har ändrats är rätt ingångspunkt `pivotTable.PivotCache.refresh()`. Det här anropet läser in källdata till cachen igen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

### Only View/Layout Changed — Use `calculateData()`
Om käldata *inte* har ändrats men bara pivottabellets vy- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en uppdateringsvid öppning-inställning har växlats) finns det ingen nödvändighet att göra en round-trip tillbaka till källdata. Cachen har redan rätt data; endast den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.calculateData()` det rätta valet.
Följande exempel modifierar en icke-källegenskap för pivottabellen och anropar sedan `calculateData()` för att rendera om den från befintlig cache.

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);
// Add a pivot table placed at destination cell E3, sourcing from A1:C9
var pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

En arbetsbok innehåller ofta många pivottabeller som alla sitter ovanpå en delad cache. För att räkna upp dem — till exempel före en batchuppdatering, eller för att diagnostisera delad cache-påverkan — använd `PivotCache.getPivotTables()`. Denna metod returnerar samlingen av alla `PivotTable` som är beroende av den givna cachen.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Innan Aspose.Cells för Node.js via C++ v26.7 var det standardvägen att uppdatera en pivottabell att anropa `PivotTable.RefreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med cachevana API:er som beskrivits ovan.
Det finns två skäl till att per-tabell `RefreshData()`-metoden är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
De rekommenderade ersättningarna är:
Följande exempel visar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Which Refresh API Should I Use?
Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när man bör välja varje en.
| Mål | Rekommenderat API | Noteringar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refreshAll()` | Ett anrop; täcker alla cacher och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt kalkylblad | `Worksheet.refreshPivotTables()` | Begränsad till ett enskilt kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.PivotCache.refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy- eller layoutinställningar har ändrats | `pivotTable.calculateData()` | Hoppar över onödig källround-trip. |
| Lista alla pivottabeller på en delad cache | `pivotCache.getPivotTables()` | Använd för att räkna upp före batchuppdatering. |
I praktiken föredrar du cache-baserade API:er framför den föråldrade per-tabell `RefreshData()`. De är medvetna om delade cacher, undviker onödiga källhämtningar och låter dig välja den minsta omfattning som tillfredställer ditt uppdateringskrav.

## Common Pitfalls
- **Glömma att uppdatera före sparande.** En pivottabell skriver bara sina renderade värden till kalkylbladet när dess dataket är uppdaterat. Om du modifierar källceller, anropa `PivotCache.refresh()` (eller `Workbook.refreshAll()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande gamla aggregerade värden.
- **Anropa den föråldrade `RefreshData()` per tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som föråldrad och hämtar källan för varje anrop. Med flera pivottabeller som delar en cache innebär detta N onödiga källhämtningar. Ersätt med ett enda `PivotCache.refresh()` följt av `calculateData()` per tabell.
- **Uppdatera när endast layouten har ändrats.** Om du endast ändrade en pivottabels vy (kolumnordning, `ConsolidationFunction`, etc.) utan att röra källdata är `PivotCache.refresh()` onödig och långsam. Anropa `pivotTable.calculateData()` för att rendera om från befintlig cache.
- **Externa källor stöds inte av `PivotCache.refresh()`.** Om pivottabelns källa kommer från en extern anslutning (databas, OLAP-kub, etc.) kan `PivotCache.refresh()` inte uppdatera den i v26.7 — den stöder för närvarande endast `Sheet`- och `Consolidation`-kältyper. För externa källor bör arbetsboken öppnas igen eller cachen byggas om från källan.

{{< app/cells/assistant language="nodejs-cpp" >}}