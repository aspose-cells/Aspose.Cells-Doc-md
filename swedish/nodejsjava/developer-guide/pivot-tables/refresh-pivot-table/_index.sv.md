---
title: Uppdatera pivottabeller i Aspose.Cells for Node.js via Java
linktitle: Uppdatera pivottabeller i Aspose.Cells for Node.js via Java
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Node.js via Java med v26.7+ pivot-uppdaterings-API,t. Den här artikeln behandlar RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, Node.js, Java, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller ett skiktat uppdaterings-API som låter dig läsa in pivotdata igen i fyra olika omfång — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Aspose.Cells for Node.js via Java v26.7** är den äldre metoden `PivotTable.RefreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i den här artikeln.

{{% /alert %}}

## Introduktion

Att uppdatera en pivottabell är sällan en enda åtgärd. Bakom kulisserna underhåller Aspose.Cells en skiktad datakedja som kopplar samman dina ursprungliga källdata med de renderade värden du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.

Datakedjan i fyra lager är:

1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — den minnesbaserade ögonblicksbilden av källdatan. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

Ett särskilt viktigt koncept är den **delade cachen**. När flera pivottabeller i en arbetsbok refererar till samma källintervall delar de *en* `PivotCache`-instans. En enskild `PivotCache` kan refereras av många pivottabeller, och att uppdatera denna cache uppdaterar varje beroende `PivotTable` på en gång.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) anger varifrån cachedatan kom. Från och med v26.7 stödjer `PivotCache.Refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) är ännu inte möjliga att uppdatera via cache-API:t.

{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:

- **`PivotCache.Refresh()`** — läser in källan → cache OCH beräknar om alla beroende `PivotTable`s i en enda åtgärd.
- **`PivotTable.CalculateData()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.

Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsåtgärderna fungerar enligt beskrivningen.

## Obligatoriska importer

Alla JavaScript-exempel i den här artikeln kräver Aspose.Cells for Node.js via Java-modulen. Pivottyperna finns i namnrymden `Aspose.Cells.Pivot`, som är en del av samma modul:

- `const aspose = require('aspose.cells');`
- Eller för specifika importer: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Uppdatera alla pivottabeller i arbetsboken

När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest heltäckande API:t `Workbook.RefreshAll()`. Ett enda anrop traverserar hela arbetsboken — varje `PivotCache` uppdateras från sin källa och sedan beräknas varje beroende `PivotTable` om. Detta är den rekommenderade metoden för generella, heltäckande dokumentuppdateringar där prestanda inte är ett problem.

Följande exempel bygger en arbetsbok med ett Fruit/Year/Amount-källintervall, skapar en pivottabell, ändrar några källvärden och använder sedan `RefreshAll()` för att uppdatera allt i ett enda anrop.

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

Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.RefreshPivotTables()`, som är begränsat till en enskild `Worksheet`-instans.

Detta är mer selektivt än `Workbook.RefreshAll()`: endast pivottabellerna på det riktade kalkylbladet uppdateras, medan pivottabeller på andra kalkylblad lämnas orörda.

Följande exempel fyller i samma Fruit/Year/Amount-källdata, lägger till en pivottabell på det första kalkylbladet, ändrar några källvärden och uppdaterar sedan bara pivottabellerna på det kalkylbladet.

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

När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:t dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: den underliggande källdatan, eller bara pivottabellens visnings-/layoutinställningar.

### Källdata har ändrats — Använd `PivotCache.Refresh()`

Om den underliggande källdatan har ändrats är rätt ingångspunkt `pivotTable.PivotCache.Refresh()`. Detta anrop läser in källdatan i cachen igen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

{{% alert color="primary" %}}

Eftersom pivottabeller delar en enda `PivotCache`-instans beräknar ett anrop till `PivotCache.Refresh()` om **alla** pivottabeller som är byggda på samma cache — inte bara den du refererar till. Om två pivottabeller delar samma källintervall, uppdateras båda när den ena cachen uppdateras.

{{% /alert %}}

Följande exempel skapar två pivottabeller på samma källintervall för att demonstrera detta delade cache-beteende, ändrar några källvärden och uppdaterar sedan genom en cachereferens.

```javascript
const AsposeCells = require("aspose.cells");

// Skapa en ny arbetsbok och öppna det första kalkylbladet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Skriv rubrikrad: Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Skriv ungefär 9 datarader (druva / blåbär / kiwi / körsbär över 2020-2021)
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Lägg till den första pivottabellen "Pivot1" förankrad vid cell E3, källområde A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Tilldela fält för Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Lägg till en ANDRA pivottabell "Pivot2" förankrad vid E15 med SAMMA källområde A1:C9
// Både Pivot1 och Pivot2 delar en enda PivotCache eftersom källområdet är identiskt.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Tilldela samma fält för Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Ändra flera beloppscellvärden i källdatan för att simulera en dataändring
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Uppdatera den delade PivotCache.
// Eftersom Pivot1 och Pivot2 delar samma PivotCache, uppdaterar detta enda anrop
// BÅDA pivottabellerna (data + stil) från den uppdaterade källan.
pivotTable1.getPivotCache().refresh();

// Spara arbetsboken
workbook.save("output.xlsx");
```

### Endast visning/layout har ändrats — Använd `CalculateData()`

Om källdatan *inte* har ändrats men bara pivottabellens visnings- eller layoutinställningar har modifierats (till exempel att ett fält har flyttats till ett annat område, eller en inställning för uppdatering vid öppning har växlats), finns det inget behov av att gå tillbaka till datakällan. Cachen innehåller redan rätt data; det är bara den renderade `PivotTable` som behöver beräknas om. I detta fall är `pivotTable.CalculateData()` rätt val.

Detta undviker det onödiga källhämtningen och är avsevärt snabbare när många pivottabeller delar samma cache.

Följande exempel modifierar en egenskap som inte är källrelaterad för pivottabellen och anropar sedan `CalculateData()` för att rendera om den från den befintliga cachen.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Skriv rubrikrad för Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Skriv 8 datarader (raderna 2-9, som passar källintervallet A1:C9)
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Ändra en visnings-/layout-egenskap — detta är en ändring som endast påverkar presentationen,
// så den kräver INTE att källdata läses igen via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() renderar DENNA pivottabells visning (data + stil) från de
// data som redan finns i PivotCache. Eftersom källdata inte ändrades,
// görs ingen tur och retur till källan — endast de cachade värdena beräknas om
// till kalkylbladsceller.
pivotTable.calculateData();

// Spara arbetsboken till disk
workbook.save("output.xlsx");
```

## Hämta alla pivottabeller som delar samma PivotCache

En arbetsbok innehåller ofta många pivottabeller som alla vilar på en enda delad cache. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera delad cache-påverkan — använd `PivotCache.GetPivotTables()`. Denna metod returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

Detta är också det mest direkta sättet att bekräfta att två pivottabeller verkligen delar samma `PivotCache`-instans: du kan jämföra cachereferenser, eller helt enkelt iterera över samlingen som returneras av `GetPivotTables()` och observera vilka pivottabeller som finns i den.

Följande exempel skapar två pivottabeller på samma källintervall, verifierar att de delar samma cache-instans och räknar sedan upp cachens pivottabeller.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Migrera från den föråldrade `PivotTable.RefreshData()`

Före Aspose.Cells for Aspose.Cells for Node.js via Java v26.7 var standardmetoden för att uppdatera en pivottabell att anropa `PivotTable.RefreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.

Det finns två anledningar till att den per-tabell-baserade `RefreshData()`-metoden är problematisk i verkliga arbetsböcker:

- Den hämtar data från källan *varje gång* den anropas, även när källan inte har ändrats.
- Varje anrop uppdaterar hela den delade cachen. När många pivottabeller delar en cache, gör upprepade anrop till `RefreshData()` per pivottabell att samma cache hämtas om och om igen, vilket är mycket långsamt.

De rekommenderade ersättningarna är:

- **Uppdatera ALLA pivottabeller i arbetsboken** → använd `workbook.refreshAll();`
- **Uppdatera NÅGRA av dem** → använd `pivotTable.getPivotCache().refresh();` för en cache. Eftersom cachen är delad uppdaterar detta enda anrop varje pivottabell som är byggd ovanpå den cachen. Andra pivottabeller som vilar på en redan uppdaterad cache kan hoppas över.
- **Endast pivotvisningen/layouten har ändrats** → använd `pivotTable.calculateData();` för att rendera om från den befintliga cachen utan att hämta från källan.

Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Bygg källdata: Frukt / År / Belopp (rubrik + 9 rader) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Lägg till den första pivottabellen (Pivot1) vid målcell E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Lägg till den ANDRA pivottabellen (Pivot2) på SAMMA källintervall ---
// Både Pivot1 och Pivot2 delar ETT underliggande PivotCache.
// Detta är exakt scenariot där det äldre per-tabell RefreshData()
// tillvägagångssättet blir ineffektivt: att uppdatera en tabell hämtar hela
// delade cachen på nytt, så att uppdatera N tabeller gör samma dyra hämtning N gånger.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Ändra flera Belopp-värden i källdatan ---
sheet.getCells().get("C2").putValue(5000);   // Druva  2020
sheet.getCells().get("C5").putValue(7500);   // Körsbär 2020
sheet.getCells().get("C9").putValue(9500);   // Körsbär 2021

// --- FÖRÅLDRAT mönster (före 26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // hämtar från källan på nytt, uppdaterar hela cachen
// pivotTable2.refreshData();  // hämtar IGEN — cachen är redan färsk!
// Varje anrop bygger om den delade cachen, så N tabeller = N redundanta hämtningar.

// --- NYTT v26.7+ mönster: uppdatera cachen EN gång, rendera sedan om vid behov ---
// Ett anrop till PivotCache.Refresh() hämtar de modifierade värdena till den delade
// cachen OCH beräknar om visningen för VARJE pivottabell som refererar till den.
// Eftersom Pivot1 och Pivot2 delar en PivotCache, uppdaterar detta enda anrop
// båda tabellerna — ingen andra källtur krävs.
pivotTable1.getPivotCache().refresh();

// CalculateData() återrenderar bara en pivottabells vy (data + stil)
// från data som redan finns i cachen — den rör INTE källan.
// Vi anropar den på Pivot2 här enbart för att demonstrera API:et: efter att cachen
// har uppdaterats en gång kan vilken beroende tabell som helst renderas om utan
// att gå tillbaka till källan. Använd CalculateData() på egen hand när bara
// pivottabellens vy/layout-inställningar har ändrats och cachen är aktuell.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Vilket uppdaterings-API bör jag använda?

Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja var och en.

| Mål | Rekommenderat API | Anteckningar |
|------|-------------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.RefreshAll()` | Ett anrop; täcker alla cachar och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.RefreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.PivotCache.Refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast visnings-/layoutinställningar har ändrats | `pivotTable.CalculateData()` | Hoppar över onödig källhämtning. |
| Lista alla pivottabeller på en delad cache | `pivotCache.GetPivotTables()` | Använd för att räkna upp före bulkuppdatering. |

I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade per-tabell-baserade `RefreshData()`. De är medvetna om delade cachar, de undviker redundanta källhämtningar och de låter dig välja det minsta omfånget som uppfyller ditt uppdateringskrav.

{{< app/cells/assistant language="javascript" >}}