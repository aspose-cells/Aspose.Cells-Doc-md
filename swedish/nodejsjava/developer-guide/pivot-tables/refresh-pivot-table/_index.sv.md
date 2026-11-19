---
title: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for Node.js via Java
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Node.js via Java med hjälp av pivot-uppdaterings-API,et från v26.7+. Den här artikeln täcker refreshAll, refreshPivotTables, PivotCache.refresh, calculateData och getPivotTables med praktiska kodexempel.
linktitle: Uppdatera pivottabeller
keywords: Aspose.Cells, Node.js, Java, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells tillhandahåller ett skiktat uppdaterings-API som låter dig läsa in pivotdata på nytt på fyra olika nivåer — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Node.js via Java v26.7** är den äldre metoden `PivotTable.RefreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i den här artikeln.
{{% /alert %}}

## Introduktion
Att uppdatera en pivottabell är sällan en enstaka åtgärd. Bakom kulisserna underhåller Aspose.Cells en skiktad datakedja som kopplar samman dina ursprungliga källdata med de renderade värdena du ser i kalkylbladet. Att förstå den här kedjan är nyckeln till att välja rätt uppdaterings-API för varje situation.
Den fyrlagriga datakedjan är:
1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — en ögonblicksbild i minnet av källdatan. Varje pivottabell byggs ovanpå en `PivotCache`. Det är här all data samlas in och aggregeras.
3. **Pivottabell** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Celler** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) anger var cache-datan kom ifrån. Från och med v26.7 stödjer `PivotCache.refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) kan ännu inte uppdateras via cache-API:et.
På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.calculateData()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.
Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsåtgärderna fungerar enligt beskrivningen.
{{% /alert %}}

## Snabbstart
Om du bara behöver den kortaste möjliga kod som uppdaterar varje pivot i arbetsboken räcker det med ett enda anrop:

```javascript
const AsposeCells = require('aspose.cells');
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Allt annat i den här artikeln förklarar när du istället bör välja ett mer avgränsat API.

## Nödvändiga importer
- `const AsposeCells = require('aspose.cells');`
- Eller för specifika importer: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Uppdatera alla pivottabeller i arbetsboken
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest omfattande API:et `Workbook.refreshAll()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från dess källa och beräknar sedan om varje beroende `PivotTable`. Det här är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett problem.
Följande exempel bygger en arbetsbok med ett källintervall för Fruit/Year/Amount, skapar en pivottabell, ändrar några källvärden och använder sedan `refreshAll()` för att uppdatera allt i ett enda anrop.

```javascript
const AsposeCells = require("aspose.cells");
// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
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
const pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Uppdatera alla pivottabeller på ett enskilt kalkylblad
Ibland behöver du bara uppdatera de pivottabeller som finns på ett visst kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refreshPivotTables()`, som är begränsad till en enda `Worksheet`-instans.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Uppdatera en enskild pivottabell
När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: den underliggande källdatan, eller bara visnings-/layoutinställningarna för pivottabellen i sig.

### Källdata har ändrats — använd `PivotCache.refresh()`
Om den underliggande källdatan har ändrats är rätt startpunkt `pivotTable.PivotCache.refresh()`. Det här anropet läser om källdatan till cacheminnet och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

### Endast vy/layout har ändrats — använd `calculateData()`
Om källdatan *inte* har ändrats men bara pivottabellens visnings- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en refresh-on-open-inställning har växlats) behöver du inte gå tillbaka till datakällan. Cacheminnet innehåller redan rätt data. Det är bara den renderade `PivotTable` som behöver beräknas om. I det här fallet är `pivotTable.calculateData()` rätt val.
Följande exempel modifierar en icke-käll-egenskap hos pivottabellen och anropar sedan `calculateData()` för att rendera om den från den befintliga cachen.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
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

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.getPivotTables()`. Den här metoden returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

## Migrera från den föråldrade `PivotTable.RefreshData()`
Före Aspose.Cells for Node.js via Java v26.7 var standardsättet att uppdatera en pivottabell att anropa `PivotTable.RefreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.
Det finns två skäl till att `RefreshData()`-metoden per tabell är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje gång* den anropas, även när källan inte har ändrats.
De rekommenderade ersättningarna är:
Följande exempel visar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Vilket uppdaterings-API bör jag använda?
Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja var och en.
| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refreshAll()` | Ett anrop; täcker alla cacheminnen och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.refreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata ändrades för en cache | `pivotTable.PivotCache.refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast visnings-/layoutinställningar ändrades | `pivotTable.calculateData()` | Hoppar över onödig källåterhämtning. |
| Lista alla pivottabeller på en delad cache | `pivotCache.getPivotTables()` | Använd för att räkna upp före bulkuppdatering. |
I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade `RefreshData()` per tabell. De är medvetna om delade cacheminnen, de undviker redundanta källhämtningar och de låter dig välja det minsta omfånget som uppfyller ditt uppdateringskrav.

## Vanliga fallgropar
- **Glömmer att uppdatera innan du sparar.** En pivottabell skriver bara sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du ändrar källceller, anropa `PivotCache.refresh()` (eller `Workbook.refreshAll()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Anropar den föråldrade `RefreshData()` per tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som föråldrad och hämtar om källan vid varje anrop. Med flera pivottabeller som delar en cache innebär detta N redundanta källhämtningar. Ersätt med en enda `PivotCache.refresh()` följt av `calculateData()` per tabell.
- **Uppdaterar när bara layouten ändrades.** Om du bara ändrade en pivottabells vy (kolumnordning, `ConsolidationFunction` osv.) utan att röra källdatan är `PivotCache.refresh()` onödigt och långsamt. Anropa `pivotTable.calculateData()` för att rendera om från den befintliga cachen.
- **Extern källa stöds inte av `PivotCache.refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub osv.) kan `PivotCache.refresh()` inte uppdatera den i v26.7 — den stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor, öppna arbetsboken igen eller bygg om cacheminnet från källan.

{{< app/cells/assistant language="nodejs-java" >}}