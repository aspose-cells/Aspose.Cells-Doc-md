---
title: Uppdatera pivottabeller och pivotcachar i Aspose.Cells for Node.js via C++
linktitle: Uppdatera pivottabeller och pivotcachar i Aspose.Cells for Node.js via C++
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Node.js via C++ med API,t för pivottabellsuppdatering i v26.7+. Den här artikeln beskriver RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, Node.js via C++, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder ett lagerindelat uppdaterings-API som låter dig ladda om pivotdata inom fyra olika omfattningar — från hela arbetsboken till en enda pivottabell. Från och med **Aspose.Cells for Node.js via C++ v26.7** är den äldre metoden `PivotTable.RefreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cachemedvetna API:erna som beskrivs i den här artikeln.
{{% /alert %}}

## Introduktion
Att uppdatera en pivottabell är sällan en enda åtgärd. Bakom kulisserna upprätthåller Aspose.Cells en lagerindelad datakedja som kopplar samman dina ursprungliga källdata med de renderade värden som visas i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.
Den fyrskiktade datakedjan är:
1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — ögonblicksbilden i minnet av källdatan. Varje pivottabell baseras på en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar i.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) anger varifrån cachedata kommer. Från och med v26.7 stöder `PivotCache.Refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor, till exempel databaser och externa anslutningar, kan ännu inte uppdateras via cache-API:t.
{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.CalculateData()`** — beräknar om visningen av en `PivotTable` utifrån redan cachad data, utan att gå tillbaka till datakällan.
Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsoperationerna fungerar som beskrivs.

## Snabbstart
Om du bara vill uppdatera alla pivottabeller i arbetsboken med så lite kod som möjligt räcker det med ett enda anrop:

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Skriv rubrikrad i cellerna A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Skriv datarader i cellerna A2:C9 (8 rader med fruktdata över 2020 och 2021)
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
// Lägg till en pivottabell: källområde "A1:C9", målcell "E3", namn "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Tilldela pivotfält: Fruit till Rader, Year till Kolumner, Amount till Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Ändra flera Amount-värden i källdatan för att simulera ändringar
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Uppdatera varje pivottabell / pivotcache i arbetsboken
workbook.refreshAll();
// Spara arbetsboken
workbook.save("output.xlsx");
```

Allt annat i den här artikeln förklarar när du i stället bör välja ett API med snävare omfattning.

## Nödvändiga importer
Alla JavaScript-exempel i den här artikeln förutsätter att modulen Aspose.Cells for Node.js via C++ har laddats och att pivottyperna finns i namnrymden `Aspose.Cells.Pivot`. En typisk konfiguration är:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (eller kom åt via `AsposeCells.Pivot.PivotFieldType`)

## Uppdatera alla pivottabeller i arbetsboken
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar de senaste källdata är det enklaste och mest omfattande API:t `Workbook.RefreshAll()`. Ett enda anrop går igenom hela arbetsboken — varje `PivotCache` uppdateras från sin källa och därefter beräknas varje beroende `PivotTable` om. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett problem.
Följande exempel bygger en arbetsbok med ett Fruit/Year/Amount-källintervall, skapar en pivottabell, ändrar några källvärden och använder sedan `RefreshAll()` för att uppdatera allt i ett enda anrop.

## Uppdatera alla pivottabeller på ett enskilt kalkylblad
Ibland behöver du bara uppdatera de pivottabeller som finns på ett visst kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara oberoende och inte bör påverkas. För detta ändamål tillhandahåller Aspose.Cells `Worksheet.RefreshPivotTables()`, som är begränsat till en enda `Worksheet`-instans.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Skriv rubrikrad för Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Skriv 8 datarader (raderna 2-9, passar källintervallet A1:C9)
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
// Lägg till en pivottabell med namnet "Pivot1" placerad vid destinationscell E3, med källa från A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Tilldela fält: Frukt till Rad, År till Kolumn, Belopp till Data
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");
// Ändra en visnings-/layout-egenskap — detta är en förändring endast för presentation,
// så det kräver INTE att källdata läses igen via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() renderar denna pivottabells visning (data + stil) från den
// data som redan finns i PivotCache. Eftersom källdata inte ändrades,
// utförs ingen tur och retur till källan — endast de cachade värdena beräknas om
// in i kalkylbladets celler.
pivotTable.calculateData();
// Spara arbetsboken till disk
workbook.save("output.xlsx");
```

## Uppdatera en enskild pivottabell
När du vill ha detaljerad kontroll över en enskild pivottabell erbjuder det cachebaserade API:t två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: underliggande källdata eller bara pivottabellens vy- eller layoutinställningar.

### Källdata har ändrats — använd `PivotCache.Refresh()`
Om underliggande källdata har ändrats är rätt startpunkt `pivotTable.PivotCache.Refresh()`. Detta anrop läser in källdata i cachen igen och beräknar sedan om varje `PivotTable` som beror på den cachen.

### Endast vy/layout har ändrats — använd `CalculateData()`
Om källdatan *inte* har ändrats utan bara pivottabellens vy- eller layoutinställningar har modifierats (till exempel om ett fält har flyttats till ett annat område eller en inställning för uppdatering när filen öppnas har ändrats), finns det inget behov av att gå tillbaka till datakällan. Cachen innehåller redan rätt data; endast den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.CalculateData()` rätt val.
Följande exempel ändrar en egenskap som inte påverkar källdata och anropar sedan `CalculateData()` för att rendera om pivottabellen från den befintliga cachen.
En arbetsbok innehåller ofta många pivottabeller som alla baseras på en och samma cache. För att räkna upp dem — till exempel före en massuppdatering eller för att diagnostisera påverkan från en delad cache — använd `PivotCache.GetPivotTables()`. Den här metoden returnerar en samling med samtliga `PivotTable`-objekt som beror på den angivna cachen.

## Migrera från den föråldrade `PivotTable.RefreshData()`
Innan Aspose.Cells for Node.js via C++ v26.7 var det vanligaste sättet att uppdatera en pivottabell att anropa `PivotTable.RefreshData()` för varje pivottabell. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cachemedvetna API:er som beskrivs ovan.
Det finns två skäl till att metoden `RefreshData()` per tabell är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
Rekommenderade ersättningsalternativ är:
Följande exempel visar det nya, effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Vilket uppdaterings-API ska jag använda?
Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja respektive alternativ.
| Mål | Rekommenderat API | Anteckningar |
|-----|-------------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.RefreshAll()` | Ett anrop; omfattar alla cachar och tabeller. |
| Uppdatera endast pivottabeller på ett enda kalkylblad | `Worksheet.RefreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.PivotCache.Refresh()` | Uppdaterar alla pivottabeller som använder den delade cachen. |
| Endast vy-/layoutinställningar har ändrats | `pivotTable.CalculateData()` | Kringgår en onödig tur och retur till källan. |
| Lista alla pivottabeller som använder en delad cache | `pivotCache.GetPivotTables()` | Använd för att räkna upp dem före en massuppdatering. |
I praktiken bör du föredra de cachebaserade API:erna framför den föråldrade `RefreshData()` per tabell. De hanterar delade cachar, undviker redundanta källhämtningar och låter dig välja den minsta omfattning som uppfyller ditt uppdateringsbehov.

## Vanliga fallgropar
- **Att glömma att uppdatera innan filen sparas.** En pivottabell skriver endast in sina renderade värden i kalkylbladet när dess datakedja har uppdaterats. Om du ändrar källceller ska du anropa `PivotCache.Refresh()` (eller `Workbook.RefreshAll()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Att anropa den föråldrade `RefreshData()` för varje tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som föråldrad och hämtar källan igen för varje anrop. Med flera pivottabeller som delar en cache innebär detta N redundanta källhämtningar. Ersätt detta med ett enda anrop till `PivotCache.Refresh()` följt av `CalculateData()` per tabell.
- **Att uppdatera när bara layouten har ändrats.** Om du endast har ändrat en pivottabells vy (kolumnordning, `ConsolidationFunction` osv.) utan att påverka källdata är `PivotCache.Refresh()` onödig och långsam. Anropa `pivotTable.CalculateData()` för att rendera om pivottabellen från den befintliga cachen.
- **Extern källa stöds inte av `PivotCache.Refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub osv.) kan den inte uppdateras med `PivotCache.Refresh()` i v26.7 — för närvarande stöds endast källtyperna `Sheet` och `Consolidation`. För externa källor kan du öppna arbetsboken igen eller bygga om cachen från källan.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

```javascript
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}