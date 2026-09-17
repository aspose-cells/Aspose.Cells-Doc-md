---
title: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for Node.js via Java
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Node.js via Java med hjälp av pivot-uppdaterings-API,et från v26.7+. Den här artikeln täcker RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
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
`PivotCache.SourceType` (enum `PivotTableSourceType`) anger var cache-datan kom ifrån. Från och med v26.7 stödjer `PivotCache.Refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) kan ännu inte uppdateras via cache-API:et.
{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.CalculateData()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.
Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsåtgärderna fungerar enligt beskrivningen.

## Snabbstart
Om du bara behöver den kortaste möjliga kod som uppdaterar varje pivot i arbetsboken räcker det med ett enda anrop:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Allt annat i den här artikeln förklarar när du istället bör välja ett mer avgränsat API.

## Nödvändiga importer
- `const aspose = require('aspose.cells');`
- Eller för specifika importer: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Uppdatera alla pivottabeller i arbetsboken
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest omfattande API:et `Workbook.RefreshAll()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från dess källa och beräknar sedan om varje beroende `PivotTable`. Det här är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett problem.
Följande exempel bygger en arbetsbok med ett källintervall för Fruit/Year/Amount, skapar en pivottabell, ändrar några källvärden och använder sedan `RefreshAll()` för att uppdatera allt i ett enda anrop.

```javascript
const AsposeCells = require("aspose.cells");
// Skapa en ny arbetsbok
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
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
// Lägg till en pivottabell: källintervall "A1:C9", målcell "E3", namn "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
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

## Uppdatera alla pivottabeller på ett enskilt kalkylblad
Ibland behöver du bara uppdatera de pivottabeller som finns på ett visst kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.RefreshPivotTables()`, som är begränsad till en enda `Worksheet`-instans.

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

## Uppdatera en enskild pivottabell
När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: den underliggande källdatan, eller bara visnings-/layoutinställningarna för pivottabellen i sig.

### Källdata har ändrats — använd `PivotCache.Refresh()`
Om den underliggande källdatan har ändrats är rätt startpunkt `pivotTable.PivotCache.Refresh()`. Det här anropet läser om källdatan till cacheminnet och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

### Endast vy/layout har ändrats — använd `CalculateData()`
Om källdatan *inte* har ändrats men bara pivottabellens visnings- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en refresh-on-open-inställning har växlats) behöver du inte gå tillbaka till datakällan. Cacheminnet innehåller redan rätt data. Det är bara den renderade `PivotTable` som behöver beräknas om. I det här fallet är `pivotTable.CalculateData()` rätt val.
Följande exempel modifierar en icke-käll-egenskap hos pivottabellen och anropar sedan `CalculateData()` för att rendera om den från den befintliga cachen.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Skriv rubrikraden Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Skriv 8 datarader (raderna 2–9, som passar källintervallet A1:C9)
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
// Lägg till en pivottabell med namnet "Pivot1" placerad i destinationscellen E3, med källa från A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Tilldela fält: Fruit till Rad, Year till Kolumn, Amount till Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Ändra en egenskap för vy/layout — detta är enbart en presentationsändring,
// så det kräver INTE att källdatan läses in på nytt via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() renderar om DEN HÄR pivottabellens visning (data + stil) från
// datan som redan finns i PivotCache. Eftersom källdatan inte ändrades
// görs ingen tur och retur till källan — endast de cachade värdena beräknas om
// till celler i kalkylbladet.
pivotTable.calculateData();
// Spara arbetsboken till disk
workbook.save("output.xlsx");
```

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.GetPivotTables()`. Den här metoden returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

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
| Uppdatera allt i arbetsboken | `Workbook.RefreshAll()` | Ett anrop; täcker alla cacheminnen och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.RefreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata ändrades för en cache | `pivotTable.PivotCache.Refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast visnings-/layoutinställningar ändrades | `pivotTable.CalculateData()` | Hoppar över onödig källåterhämtning. |
| Lista alla pivottabeller på en delad cache | `pivotCache.GetPivotTables()` | Använd för att räkna upp före bulkuppdatering. |
I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade `RefreshData()` per tabell. De är medvetna om delade cacheminnen, de undviker redundanta källhämtningar och de låter dig välja det minsta omfånget som uppfyller ditt uppdateringskrav.

## Vanliga fallgropar
- **Glömmer att uppdatera innan du sparar.** En pivottabell skriver bara sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du ändrar källceller, anropa `PivotCache.Refresh()` (eller `Workbook.RefreshAll()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Anropar den föråldrade `RefreshData()` per tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som föråldrad och hämtar om källan vid varje anrop. Med flera pivottabeller som delar en cache innebär detta N redundanta källhämtningar. Ersätt med en enda `PivotCache.Refresh()` följt av `CalculateData()` per tabell.
- **Uppdaterar när bara layouten ändrades.** Om du bara ändrade en pivottabells vy (kolumnordning, `ConsolidationFunction` osv.) utan att röra källdatan är `PivotCache.Refresh()` onödigt och långsamt. Anropa `pivotTable.CalculateData()` för att rendera om från den befintliga cachen.
- **Extern källa stöds inte av `PivotCache.Refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub osv.) kan `PivotCache.Refresh()` inte uppdatera den i v26.7 — den stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor, öppna arbetsboken igen eller bygg om cacheminnet från källan.

{{< app/cells/assistant language="nodejs-java" >}}