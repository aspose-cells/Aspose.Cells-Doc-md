---
title: Uppdatera pivottabeller och pivotcachar i Aspose.Cells for C++
linktitle: Uppdatera pivottabeller och pivotcachar i Aspose.Cells for C++
description: Lär dig att uppdatera pivottabeller i Aspose.Cells for C++ med hjälp av API för pivotuppdatering i version v26.7+. Den här artikeln behandlar RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, C++, pivottabell, uppdatering, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells tillhandahåller ett lagerindelat uppdaterings-API som låter dig läsa in pivotdata inom fyra olika omfattningar – från hela arbetsboken till en enda pivottabell. Från och med **Aspose.Cells for C++ v26.7** är den äldre metoden `PivotTable.RefreshData()` markerad som föråldrad och bör ersättas med de effektivare API:er som tar hänsyn till cachen och beskrivs i den här artikeln.
{{% /alert %}}

## Introduction
Att uppdatera en pivottabell är sällan en enda åtgärd. Under huven underhåller Aspose.Cells en lagerindelad datakedja som kopplar den ursprungliga källdatan till de renderade värden som du ser i kalkylbladet. Att förstå den här kedjan är nyckeln till att välja rätt uppdaterings-API för varje situation.
Den fyralediga datakedjan är:
1. **Datakälla** – de ursprungliga kalkylbladsintervallen, databasfrågorna eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** – ögonblicksbilden av källdatan i minnet. Varje pivottabell byggs ovanpå en `PivotCache`; här samlas och aggregeras all data.
3. **PivotTable** – vyn som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** – kalkylbladets `Cells`, dit `PivotTable` renderar de beräknade värdena och stilarna.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) anger varifrån data i cachen kom. Från och med v26.7 stöder `PivotCache.Refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** – alltså data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar etc.) kan ännu inte uppdateras via cache-API:et.
På grund av den här kedjan finns två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.CalculateData()`** – beräknar om visningen för en `PivotTable` utifrån redan cachad data, utan att göra en tur och retur till datakällan.
Alla scenarier i den här artikeln använder källdata i kalkylbladsceller, så källtypen är `Sheet` och uppdateringsåtgärderna fungerar som beskrivs.
{{% /alert %}}

## Quick Start
Om du bara behöver den kortast möjliga koden för att uppdatera varje pivottabell i arbetsboken räcker ett enda anrop:

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Allt annat i den här artikeln förklarar när du i stället bör välja ett mer begränsat API.

## Required Include Directives
Alla C++-exempel i den här artikeln börjar med följande include- och namespace-direktiv eftersom pivottyperna tillhör namespace `Aspose::Cells::Pivot`:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Refresh All Pivot Tables in the Workbook
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest omfattande API:et `Workbook.RefreshAll()`. Ett enda anrop går igenom hela arbetsboken, uppdaterar varje `PivotCache` från dess källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för generella uppdateringar av hela dokumentet när prestanda inte är en avgörande faktor.
Följande exempel skapar en arbetsbok med ett källintervall för Fruit/Year/Amount, skapar en pivottabell, ändrar vissa källvärden och använder sedan `RefreshAll()` för att uppdatera allt med ett enda anrop.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);
    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);
    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);
    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);
    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);
    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);
    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);
    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);
    pivotTable.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh All Pivot Tables on a Single Worksheet
Ibland behöver du bara uppdatera pivottabellerna som finns på ett visst kalkylblad – till exempel när det är känt att pivottabeller på andra kalkylblad inte hör ihop med dessa och inte ska påverkas. För detta tillfälle tillhandahåller Aspose.Cells `Worksheet.RefreshPivotTables()`, och metoden är begränsad till en enda `Worksheet`-instans.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);
    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);
    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);
    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);
    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);
    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);
    worksheet.RefreshPivotTables();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh a Single Pivot Table
När du vill ha detaljerad kontroll över en enda pivottabell ger det cachebaserade API:et dig två alternativ. Vilket alternativ som passar beror på vad som faktiskt har ändrats: den underliggande källdatan eller endast vy-/layoutinställningarna för pivottabellen.

### Source Data Changed — Use `PivotCache.Refresh()`
Om den underliggande källdatan har ändrats är rätt ingångspunkt `pivotTable.GetPivotCache().Refresh()`. Anropet läser om källdatan till cachen och beräknar sedan om varje `PivotTable` som beror på den cachen.

### Only View/Layout Changed — Use `CalculateData()`
Om källdatan *inte* har ändrats och endast pivottabellens vy- eller layoutinställningar har ändrats (till exempel om ett fält har flyttats till ett annat område eller en inställning för uppdatering vid öppning har aktiverats eller inaktiverats), finns inget behov av att gå tillbaka till datakällan. Cachen innehåller redan rätt data; endast den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.CalculateData()` rätt val.
Följande exempel ändrar en egenskap som inte hör till källan i pivottabellen och anropar sedan `CalculateData()` för att rendra om pivottabellen från den befintliga cachen.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Write Fruit / Year / Amount header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);
 // Add a pivot table placed at destination cell E3, sourcing from A1:C9
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    // Assign fields: Fruit to Row, Year to Column, Amount to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modify a view/layout property — this is a presentation-only change,
    // so it does NOT require re-reading the source data through PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() re-renders THIS pivot table's display (data + style) from the
    // data already held in the PivotCache. Because the source data did not change,
    // no round-trip to the source is performed — only the cached values are recalculated
    // into worksheet cells.
    pivotTable.CalculateData();
    // Save the workbook to disk
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

En arbetsbok innehåller ofta många pivottabeller som alla är byggda på samma delade cache. Om du vill räkna upp dem – till exempel innan du utför en massuppdatering eller för att diagnostisera effekten av en delad cache – använd `PivotCache.GetPivotTables()`. Metoden returnerar listan med alla `PivotTable` som beror på den angivna cachen.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Före Aspose.Cells for C++ v26.7 var standardmetoden att uppdatera en pivottabell att anropa `PivotTable.RefreshData()` på varje pivottabell separat. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cachemedvetna API:er som beskrivs ovan.
Det finns två skäl till att metoden `RefreshData()` för varje tabell är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
Rekommenderade ersättningar är:
Följande exempel visar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");
    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);
    PivotTable pivotTable1 = sheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotTable pivotTable2 = sheet.GetPivotTables().Add(u"A1:C9", 14, 4);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");
    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);
    pivotTable2.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Which Refresh API Should I Use?
Tabellen nedan sammanfattar tillgängliga uppdaterings-API:er och när du bör välja var och en.
| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.RefreshAll()` | Ett anrop; täcker alla cacher och tabeller. |
| Uppdatera endast pivottabeller på ett enda kalkylblad | `Worksheet.RefreshPivotTables()` | Avgränsat till ett kalkylblad. |
| Källdatan har ändrats för en cache | `pivotTable.GetPivotCache().Refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy-/layoutinställningar har ändrats | `pivotTable.CalculateData()` | Hoppar över onödig återgång till källan. |
| Lista alla pivottabeller på en delad cache | `pivotCache.GetPivotTables()` | Använd för att räkna upp dem före massuppdatering. |
I praktiken bör du föredra cachebaserade API:er framför den föråldrade `RefreshData()` per tabell. De tar hänsyn till delade cacher, undviker redundanta hämtningar från källan och låter dig välja den minsta omfattning som uppfyller ditt uppdateringsbehov.

## Common Pitfalls
- **Att glömma att uppdatera före sparning.** En pivottabell skriver endast sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du ändrar källceller ska du anropa `PivotCache.Refresh()` (eller `Workbook.RefreshAll()`) före `Workbook.Save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Att anropa den föråldrade `RefreshData()` för varje tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som föråldrad och hämtar källan igen vid varje anrop. Med flera pivottabeller som delar en cache innebär det N redundanta hämtningar från källan. Ersätt med ett enda anrop till `PivotCache.Refresh()` följt av `CalculateData()` för varje tabell.
- **Att uppdatera när endast layouten har ändrats.** Om du bara har ändrat en pivottabells vy (kolumnordning, `ConsolidationFunction` osv.) utan att röra källdatan är det onödigt och långsamt att anropa `PivotCache.Refresh()`. Anropa `pivotTable.CalculateData()` för att rendra om från den befintliga cachen.
- **Extern källa som inte stöds av `PivotCache.Refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub etc.) kan `PivotCache.Refresh()` inte uppdatera den i v26.7 – metoden stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor kan du öppna arbetsboken igen eller bygga om cachen utifrån källan.

{{< app/cells/assistant language="cpp" >}}