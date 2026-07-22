---
title: Uppdatera pivottabeller i Aspose.Cells for .NET
linktitle: Uppdatera pivottabeller
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for .NET med hjälp av v26.7+ pivot-uppdaterings-API,et. Den här artikeln täcker RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, .NET, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller ett lagerbaserat uppdaterings-API som låter dig läsa in pivotdata igen på fyra olika omfång — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for .NET v26.7** är den äldre metoden `PivotTable.RefreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i den här artikeln.

{{% /alert %}}

## Introduktion

Att uppdatera en pivottabell är sällan en enskild operation. Bakom kulisserna upprätthåller Aspose.Cells en lagerbaserad datakedja som kopplar samman dina ursprungliga källdata med de renderade värden du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.

Den fyra lager djupa datakedjan är:

1. **Datakälla** — de ursprungliga kalkylbladens intervall, databasfråga eller konsolideringsintervall där de råa värdena finns.
2. **PivotCache** — ögonblicksbilden i minnet av källdatan. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyn som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

Ett särskilt viktigt koncept är den **delade cachen**. När flera pivottabeller i en arbetsbok refererar till samma källintervall delar de *en* `PivotCache`-instans. En enskild `PivotCache` kan refereras av många pivottabeller, och att uppdatera den cachen uppdaterar varje beroende `PivotTable` på en gång.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) anger var cachedatan kom ifrån. Från och med v26.7 stöder `PivotCache.Refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladens intervall. Externa källor (databaser, externa anslutningar etc.) är ännu inte möjliga att uppdatera via cache-API:et.

{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:

- **`PivotCache.Refresh()`** — läser in källan → cache igen OCH beräknar om alla beroende `PivotTable`s i en enda operation.
- **`PivotTable.CalculateData()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.

Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsoperationerna beter sig enligt beskrivningen.

## Nödvändiga Using-direktiv

Alla C#-exempel i den här artikeln börjar med följande tre using-direktiv eftersom pivottyperna ligger i namnrymden `Aspose.Cells.Pivot`:

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Uppdatera alla pivottabeller i arbetsboken

När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest heltäckande API:et `Workbook.RefreshAll()`. Ett enda anrop traverserar hela arbetsboken — varje `PivotCache` uppdateras från sin källa och sedan beräknas varje beroende `PivotTable` om. Detta är den rekommenderade metoden för allmänna, dokumentövergripande uppdateringar där prestanda inte är ett problem.

Följande exempel bygger en arbetsbok med ett Fruit/Year/Amount-källintervall, skapar en pivottabell, ändrar några källvärden och använder sedan `RefreshAll()` för att uppdatera allt i ett enda anrop.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Skapa en ny arbetsbok
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Skriv rubrikrad i cellerna A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Skriv datarader i cellerna A2:C9 (8 rader med fruktdata för 2020 och 2021)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);

// Lägg till en pivottabell: källområde "A1:C9", målcell "E3", namn "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Tilldela pivotfält: Fruit till Rader, Year till Kolumner, Amount till Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Ändra flera Amount-värden i källdatan för att simulera ändringar
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// Uppdatera alla pivottabeller / pivotcachar i arbetsboken
workbook.RefreshAll();

// Spara arbetsboken
workbook.Save("output.xlsx");
```

## Uppdatera alla pivottabeller på ett enskilt kalkylblad

Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.RefreshPivotTables()`, som är begränsat till en enskild `Worksheet`-instans.

Detta är mer selektivt än `Workbook.RefreshAll()`: endast pivottabellerna på det riktade kalkylbladet uppdateras, medan pivottabeller på andra kalkylblad förblir orörda.

Följande exempel fyller i samma Fruit/Year/Amount-källdata, lägger till en pivottabell på det första kalkylbladet, ändrar några källvärden och uppdaterar sedan endast pivottabellerna på det kalkylbladet.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);

int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);

worksheet.RefreshPivotTables();

workbook.Save("output.xlsx");
```

## Uppdatera en enskild pivottabell

När du vill ha finkornig kontroll över en enskild pivottabell ger det cachebaserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: underliggande källdata eller bara vy-/layoutinställningarna för själva pivottabellen.

### Källdata har ändrats — Använd `PivotCache.Refresh()`

Om den underliggande källdatan har ändrats är rätt startpunkt `pivotTable.PivotCache.Refresh()`. Detta anrop läser om källdatan in i cachen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

{{% alert color="primary" %}}

Eftersom pivottabeller delar en enda `PivotCache`-instans beräknar ett anrop till `PivotCache.Refresh()` om **alla** pivottabeller som är byggda på samma cache — inte bara den du refererar till. Om två pivottabeller delar samma källintervall uppdaterar ett anrop till en cache båda.

{{% /alert %}}

Följande exempel skapar två pivottabeller på samma källintervall för att demonstrera detta delade cache-beteende, ändrar några källvärden och uppdaterar sedan genom en cachereferens.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Skapa en ny arbetsbok och hämta det första kalkylbladet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Skriv rubrikrad: Frukt / År / Belopp
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Skriv ungefär 9 datarader (druva / blåbär / kiwi / körsbär över 2020-2021)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// Lägg till den första pivottabellen "Pivot1" förankrad vid cell E3, källområde A1:C9
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// Tilldela fält för Pivot1
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// Lägg till en ANDRA pivottabell "Pivot2" förankrad vid E15 med SAMMA källområde A1:C9
// Både Pivot1 och Pivot2 delar en enda PivotCache eftersom källområdet är identiskt.
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// Tilldela samma fält för Pivot2
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// Ändra flera cellvärden för Belopp i källdatan för att simulera en dataändring
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// Uppdatera den delade PivotCache.
// Eftersom Pivot1 och Pivot2 delar samma PivotCache, uppdaterar detta enda anrop
// BÅDA pivottabellerna (data + stil) från den uppdaterade källan.
pivotTable1.PivotCache.Refresh();

// Spara arbetsboken
workbook.Save("output.xlsx");
```

### Endast vy/layout har ändrats — Använd `CalculateData()`

Om källdatan *inte* har ändrats men bara pivottabellens vy- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en inställning för uppdatering-vid-öppning har växlats), finns det ingen anledning att gå tillbaka till datakällan. Cachen innehåller redan rätt data; bara den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.CalculateData()` rätt val.

Detta undviker det onödiga källhämtandet och är avsevärt snabbare när många pivottabeller delar samma cache.

Följande exempel modifierar en icke-källrelaterad egenskap hos pivottabellen och anropar sedan `CalculateData()` för att rendera om den från den befintliga cachen.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Skriv rubrikrad för Frukt / År / Belopp
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Skriv 8 datarader (raderna 2-9, som passar källintervallet A1:C9)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);

// Lägg till en pivottabell med namnet "Pivot1" placerad i destinationscell E3, med källa från A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// Tilldela fält: Frukt till Rad, År till Kolumn, Belopp till Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Ändra en visnings-/layout-egenskap — detta är en presentationsändring,
// så den kräver INTE att källdatan läses igen via PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() renderar om DEN HÄ pivottabellens visning (data + stil) från den
// data som redan finns i PivotCache. Eftersom källdatan inte ändrades,
// utförs ingen tur och retur till källan — endast de cachelagrade värdena beräknas om
// till arbetsbladsceller.
pivotTable.CalculateData();

// Spara arbetsboken till disk
workbook.Save("output.xlsx");
```

## Hämta alla pivottabeller som delar samma PivotCache

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan en batchuppdatering utförs, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.GetPivotTables()`. Denna metod returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

Detta är också det mest direkta sättet att bekräfta att två pivottabeller verkligen delar samma `PivotCache`-instans: du kan jämföra cachereferenser, eller helt enkelt iterera genom samlingen som returneras av `GetPivotTables()` och observera vilka pivottabeller som finns i den.

Följande exempel skapar två pivottabeller på samma källintervall, verifierar att de delar samma cache-instans och räknar sedan upp cachens pivottabeller.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Sheet1";

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

int pivot1Index = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivot1Index];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivot2Index];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

bool sameCache = object.ReferenceEquals(pivotTable1.PivotCache, pivotTable2.PivotCache);
Console.WriteLine("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.PivotCache.GetPivotTables();
Console.WriteLine("Number of pivot tables sharing the cache: " + sharedPivotTables.Length);

foreach (PivotTable pt in sharedPivotTables)
{
    Console.WriteLine("Pivot table name: " + pt.Name);
}

workbook.Save("output.xlsx");
```

## Migrera från den föråldrade `PivotTable.RefreshData()`

Före Aspose.Cells for .NET v26.7 var standardsättet att uppdatera en pivottabell att anropa `PivotTable.RefreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.

Det finns två anledningar till att metoden `RefreshData()` per tabell är problematisk i verkliga arbetsböcker:

- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
- Varje anrop uppdaterar hela den delade cachen. När många pivottabeller delar en cache innebär upprepade anrop till `RefreshData()` per pivottabell att samma cache hämtas om och om igen, vilket är mycket långsamt.

De rekommenderade ersättningarna är:

- **Uppdatera ALLA pivottabeller i arbetsboken** → använd `workbook.RefreshAll();`
- **Uppdatera NÅGRA av dem** → använd `pivotTable.PivotCache.Refresh();` för en cache. Eftersom cachen delas uppdaterar detta enda anrop varje pivottabell som är byggd ovanpå den cachen. Andra pivottabeller som ligger på en redan uppdaterad cache kan säkert hoppas över.
- **Endast pivotvyn/layouten har ändrats** → använd `pivotTable.CalculateData();` för att rendera om från den befintliga cachen utan någon källhämtning.

Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- Build the source data: Fruit / Year / Amount (header + 9 rows) ---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- Add the first pivot table (Pivot1) at destination cell E3 ---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Add the SECOND pivot table (Pivot2) on the SAME source range ---
// Both Pivot1 and Pivot2 share ONE underlying PivotCache.
// This is exactly the scenario where the legacy per-table RefreshData()
// approach becomes inefficient: refreshing one table re-fetches the whole
// shared cache, so refreshing N tables does the same expensive fetch N times.
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Modify several Amount values in the source data ---
sheet.Cells["C2"].PutValue(5000);   // Grape  2020
sheet.Cells["C5"].PutValue(7500);   // Cherry 2020
sheet.Cells["C9"].PutValue(9500);   // Cherry 2021

// --- OBSOLETE pattern (pre-26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // re-fetches from source, refreshes whole cache
// pivotTable2.RefreshData();  // re-fetches AGAIN — the cache is already fresh!
// Each call rebuilds the shared cache, so N tables = N redundant fetches.

// --- NEW v26.7+ pattern: refresh the cache ONCE, then re-render as needed ---
// One call to PivotCache.Refresh() pulls the modified values into the shared
// cache AND recalculates the display of EVERY pivot table that references it.
// Because Pivot1 and Pivot2 share one PivotCache, this single call updates
// both tables — no second source round-trip is required.
pivotTable1.PivotCache.Refresh();

// CalculateData() only re-renders a pivot table's display (data + style)
// from the data already held in the cache — it does NOT touch the source.
// We call it on Pivot2 here purely to demonstrate the API: after the cache
// has been refreshed once, any dependent table can be re-rendered without
// going back to the source. Use CalculateData() on its own when only the
// pivot table's view/layout settings have changed and the cache is current.
pivotTable2.CalculateData();

workbook.Save("output.xlsx");
```

## Vilket uppdaterings-API ska jag använda?

Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja var och en av dem.

| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.RefreshAll()` | Ett anrop; täcker alla cacheminnen och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.RefreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.PivotCache.Refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy-/layoutinställningar har ändrats | `pivotTable.CalculateData()` | Hoppar över onödig källhämtning. |
| Lista alla pivottabeller på en delad cache | `pivotCache.GetPivotTables()` | Använd för att räkna upp före massuppdatering. |

I praktiken bör du föredra de cachebaserade API:erna framför den föråldrade `RefreshData()` per tabell. De är medvetna om delade cacheminnen, de undviker redundanta källhämtningar, och de låter dig välja det minsta omfånget som uppfyller ditt uppdateringskrav.

{{< app/cells/assistant language="csharp" >}}