---
title: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for .NET
description: "Lär dig att uppdatera pivottabeller i Aspose.Cells for .NET med hjälp av pivot-uppdaterings-API,t från och med v26.7. Artikeln behandlar RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel."
linktitle: Uppdatera pivottabeller
keywords: Aspose.Cells, .NET, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells tillhandahåller ett skiktat uppdaterings-API som låter dig läsa in pivotdata igen på fyra olika nivåer — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for .NET v26.7** är den äldre metoden `PivotTable.RefreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i den här artikeln.
{{% /alert %}}

## Introduktion
Att uppdatera en pivottabell är sällan en enda åtgärd. Bakom kulisserna underhåller Aspose.Cells en skiktad datakedja som kopplar ihop din ursprungliga datakälla med de renderade värdena du ser i kalkylbladet. Att förstå den här kedjan är nyckeln till att välja rätt uppdaterings-API för varje situation.
Den fyrskiktade datakedjan är:
1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågorna eller konsolideringsintervallen där råvärdena finns.
2. **PivotCache** — ögonblicksbilden i minnet av källdatan. Varje pivottabell byggs ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **Pivottabell** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Celler** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) anger var cachedatan kom ifrån. Från och med v26.7 stöder `PivotCache.Refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) är ännu inte möjliga att uppdatera via cache-API:t.
{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.CalculateData()`** — beräknar om en `PivotTable`s vy från redan cachelagrad data, utan att gå tillbaka till datakällan.
Alla scenarier i den här artikeln använder kalkylbladsceller som datakälla, så källtypen är `Sheet` och uppdateringsåtgärderna fungerar enligt beskrivningen.

## Snabbstart
Om du bara behöver den kortaste möjliga koden som uppdaterar varje pivot i arbetsboken räcker det med ett enda anrop:

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Allt annat i den här artikeln förklarar när du bör välja ett smalare API istället.

## Nödvändiga Using-direktiv
Alla C#-exempel i den här artikeln börjar med följande tre using-direktiv eftersom pivottyperna finns i namnrymden `Aspose.Cells.Pivot`:
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Uppdatera alla pivottabeller i arbetsboken
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest heltäckande API:t `Workbook.RefreshAll()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från sin källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett problem.
Följande exempel bygger en arbetsbok med ett källintervall för Fruit/Year/Amount, skapar en pivottabell, ändrar några källvärden och använder sedan `RefreshAll()` för att uppdatera allt i ett enda anrop.

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
// Skriv datarader i cellerna A2:C9 (8 rader fruktdata för 2020 och 2021)
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
// Lägg till en pivottabell: källområde "A1:C9", destinationscell "E3", namn "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Tilldela pivotfält: Fruit till Rader, Year till Kolumner, Amount till Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Ändra flera Amount-värden i källdatan för att simulera förändringar
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// Uppdatera alla pivottabeller / pivotcache i arbetsboken
workbook.RefreshAll();
// Spara arbetsboken
workbook.Save("output.xlsx");
```

## Uppdatera alla pivottabeller på ett enskilt kalkylblad
Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.RefreshPivotTables()`, som är begränsat till en enskild `Worksheet`-instans.

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
När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:t dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: den underliggande källdatan, eller bara visnings-/layoutinställningarna för själva pivottabellen.

### Källdata har ändrats — använd `PivotCache.Refresh()`
Om den underliggande källdatan har ändrats är rätt startpunkt `pivotTable.PivotCache.Refresh()`. Detta anrop läser in källdatan i cachen igen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

### Endast vy/layout har ändrats — använd `CalculateData()`
Om källdatan *inte* har ändrats utan bara pivottabellens visnings- eller layoutinställningar har modifierats (till exempel att ett fält har flyttats till ett annat område, eller att en inställning för uppdatering vid öppning har växlats), finns det inget behov av att gå tillbaka till datakällan. Cachen har redan rätt data; det är bara den renderade `PivotTable` som behöver beräknas om. I detta fall är `pivotTable.CalculateData()` rätt val.
Följande exempel ändrar en egenskap som inte är kopplad till källan i pivottabellen och anropar sedan `CalculateData()` för att rendera om den från den befintliga cachen.

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
// Lägg till en pivottabell med namnet "Pivot1" placerad i målcell E3, med källa från A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// Tilldela fält: Frukt till Rad, År till Kolumn, Belopp till Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Ändra en visnings-/layout-egenskap — detta är enbart en presentationsändring,
// så den kräver INTE att källdata läses på nytt via PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() renderar om DENNA pivottabells visning (data + stil) från de
// data som redan finns i PivotCache. Eftersom källdata inte ändrades,
// utförs ingen rundtur till källan — endast de cachade värdena beräknas om
// till kalkylbladsceller.
pivotTable.CalculateData();
// Spara arbetsboken till disk
workbook.Save("output.xlsx");
```

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.GetPivotTables()`. Den här metoden returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

## Migrera från den föråldrade `PivotTable.RefreshData()`
Före Aspose.Cells for .NET v26.7 var det standardmässiga sättet att uppdatera en pivottabell att anropa `PivotTable.RefreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.
Det finns två skäl till att metoden `RefreshData()` per tabell är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
De rekommenderade ersättningarna är:
Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Vilket uppdaterings-API bör jag använda?
Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du bör välja var och en av dem.
| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.RefreshAll()` | Ett anrop; täcker alla cacheminnen och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.RefreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.PivotCache.Refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy/layoutinställningar har ändrats | `pivotTable.CalculateData()` | Hoppar över onödig källhämtning. |
| Lista alla pivottabeller på en delad cache | `pivotCache.GetPivotTables()` | Använd för att räkna upp före bulkuppdatering. |
I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade `RefreshData()` per tabell. De är medvetna om delade cacheminnen, de undviker redundanta källhämtningar, och de låter dig välja den minsta omfattning som uppfyller ditt uppdateringsbehov.

## Vanliga fallgropar
- **Glömmer att uppdatera innan sparning.** En pivottabell skriver endast sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du ändrar källceller, anropa `PivotCache.Refresh()` (eller `Workbook.RefreshAll()`) före `Workbook.Save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Anropar den föråldrade `RefreshData()` per tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som föråldrad och hämtar källan för varje anrop. Med flera pivottabeller som delar en cache innebär detta N redundanta källhämtningar. Ersätt med ett enda `PivotCache.Refresh()` följt av `CalculateData()` per tabell.
- **Uppdaterar när bara layouten har ändrats.** Om du bara ändrade en pivottabells vy (kolumnordning, `ConsolidationFunction` osv.) utan att röra källdatan är `PivotCache.Refresh()` onödig och långsam. Anropa `pivotTable.CalculateData()` för att rendera om från den befintliga cachen.
- **Extern källa stöds inte av `PivotCache.Refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub osv.) kan `PivotCache.Refresh()` inte uppdatera den i v26.7 — den stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor, öppna arbetsboken igen eller bygg om cachen från källan.

{{< app/cells/assistant language="csharp" >}}