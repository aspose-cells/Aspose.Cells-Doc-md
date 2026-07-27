---
title: Uppdatera pivottabeller i Aspose.Cells for C++
linktitle: Uppdatera pivottabeller i Aspose.Cells for C++
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for C++ med hjälp av pivot-uppdaterings-API,et i v26.7+. Den här artikeln täcker RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, C++, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells tillhandahåller ett skiktat uppdaterings-API som låter dig ladda om pivotdata i fyra olika omfattningar — från hela arbetsboken ner till en enda pivottabell. Från och med **Aspose.Cells for C++ v26.7** är den äldre metoden `PivotTable.RefreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i den här artikeln.

{{% /alert %}}

## Introduktion

Att uppdatera en pivottabell är sällan en enskild operation. Bakom kulisserna upprätthåller Aspose.Cells en skiktad datakedja som kopplar samman dina ursprungliga källdata med de renderade värden du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.

Den fyra lager djupa datakedjan är:

1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — ögonblicksbilden i minnet av källdatan. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar i.

Ett särskilt viktigt koncept är den **delade cachen**. När flera pivottabeller i en arbetsbok refererar till samma källintervall delar de *en* `PivotCache`-instans. En enda `PivotCache` kan refereras av många pivottabeller, och att uppdatera denna cache uppdaterar varje beroende `PivotTable` på en gång.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) anger var cache-datan kom ifrån. Från och med v26.7 stöder `PivotCache.Refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar etc.) är ännu inte uppdateringsbara via cache-API:t.

{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:

- **`PivotCache.Refresh()`** — laddar om källa → cache OCH beräknar om alla beroende `PivotTable`s i en enda operation.
- **`PivotTable.CalculateData()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.

Alla scenarier i den här artikeln använder kalkylbladscellskälldata, så källtypen är `Sheet` och uppdateringsoperationer fungerar som beskrivs.

## Nödvändiga inkluderingsdirektiv

Alla C++-exempel i den här artikeln börjar med följande header-inkludering och namespace-direktiv eftersom pivottyperna finns i namespacet `Aspose::Cells::Pivot`:

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Uppdatera alla pivottabeller i arbetsboken

När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan, är det enklaste och mest omfattande API:t `Workbook.RefreshAll()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från sin källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett problem.

Följande exempel bygger en arbetsbok med ett källintervall för Frukt/År/Belopp, skapar en pivottabell, modifierar några källvärden och använder sedan `RefreshAll()` för att uppdatera allt med ett enda anrop.

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

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

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

## Uppdatera alla pivottabeller på ett enskilt kalkylblad

Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör vidröras. För detta fall tillhandahåller Aspose.Cells `Worksheet.RefreshPivotTables()`, som är begränsat till en enskild `Worksheet`-instans.

Detta är mer selektivt än `Workbook.RefreshAll()`: endast pivottabellerna på det riktade kalkylbladet uppdateras, medan pivottabeller på andra kalkylblad förblir orörda.

Följande exempel fyller i samma källdata för Frukt/År/Belopp, lägger till en pivottabell på det första kalkylbladet, modifierar några källvärden och uppdaterar sedan endast pivottabellerna på det kalkylbladet.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

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

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

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

## Uppdatera en enskild pivottabell

När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:t dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: den underliggande källdatan, eller bara visnings-/layoutinställningarna för pivottabellen själv.

### Källdata har ändrats — Använd `PivotCache.Refresh()`

Om den underliggande källdatan har ändrats är rätt startpunkt `pivotTable.GetPivotCache().Refresh()`. Detta anrop läser om källdatan till cachen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

{{% alert color="primary" %}}

Eftersom pivottabeller delar en enda `PivotCache`-instans, beräknar `PivotCache.Refresh()` om **alla** pivottabeller som är byggda på samma cache — inte bara den du refererar till. Om två pivottabeller delar samma källintervall, uppdaterar en cache-uppdatering båda.

{{% /alert %}}

Följande exempel skapar två pivottabeller på samma källintervall för att demonstrera detta delade cache-beteende, modifierar några källvärden och uppdaterar sedan genom en cache-referens.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Huvudrad: Frukt / År / Belopp
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Datarader
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // Lägg till den första pivottabellen "Pivot1" förankrad vid cell E3, källområde A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Tilldela fält för Pivot1
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Lägg till en ANDRA pivottabell "Pivot2" förankrad vid E15 med SAMMA källområde A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Tilldela samma fält för Pivot2
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Ändra flera Belopp-cellvärden i källdatan för att simulera en dataändring
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // Uppdatera den delade PivotCache genom att uppdatera pivottabelldatan
    pivotTable1.RefreshData();

    // Spara arbetsboken
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Endast visning/layout har ändrats — Använd `CalculateData()`

Om källdatan *inte* har ändrats men bara pivottabellens visnings- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en uppdaterings-vid-öppen-inställning har växlats), finns det inget behov av att gå tillbaka till datakällan. Cachen innehåller redan rätt data; endast den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.CalculateData()` rätt val.

Detta undviker det onödiga källhämtandet och är avsevärt snabbare när många pivottabeller delar samma cache.

Följande exempel modifierar en icke-käll-egenskap hos pivottabellen och anropar sedan `CalculateData()` för att rendera om den från den befintliga cachen.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Skriv rubrikrad för Frukt / År / Belopp
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Skriv 8 datarader (raderna 2-9, passar källintervallet A1:C9)
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

    // Lägg till en pivottabell med namnet "Pivot1" placerad i destinationscellen E3, med källa från A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Tilldela fält: Fruit till Rad, Year till Kolumn, Amount till Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Ändra en visnings-/layout-egenskap — detta är en ändring som endast rör presentationen,
    // så den kräver INTE att källdata läses in på nytt via PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() ritar om DENNA pivottabells visning (data + stil) från de
    // data som redan finns i PivotCache. Eftersom källdata inte ändrades
    // görs ingen rundresa till källan — endast de cachade värdena beräknas om
    // till kalkylbladsceller.
    pivotTable.CalculateData();

    // Spara arbetsboken till disk
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Hämta alla pivottabeller som delar samma PivotCache

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan en batchuppdatering utförs, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.GetPivotTables()`. Denna metod returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

Detta är också det mest direkta sättet att bekräfta att två pivottabeller verkligen delar samma `PivotCache`-instans: du kan jämföra cache-referenser, eller helt enkelt iterera samlingen som returneras av `GetPivotTables()` och observera vilka pivottabeller som visas i den.

Följande exempel skapar två pivottabeller på samma källintervall, verifierar att de delar samma cache-instans och räknar sedan upp cachens pivottabeller.


## Migrera från den föråldrade `PivotTable.RefreshData()`

Före Aspose.Cells for C++ v26.7 var standardsättet att uppdatera en pivottabell att anropa `PivotTable.RefreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.

Det finns två anledningar till att metoden `RefreshData()` per tabell är problematisk i verkliga arbetsböcker:

- Den hämtar om data från källan *varje* gång den anropas, även när källan inte har ändrats.
- Varje anrop uppdaterar hela den delade cachen. När många pivottabeller delar en cache, gör upprepade anrop till `RefreshData()` per pivottabell att samma cache hämtas om gång på gång, vilket är mycket långsamt.

De rekommenderade ersättningarna är:

- **Uppdatera ALLA pivottabeller i arbetsboken** → använd `workbook.RefreshAll();`
- **Uppdatera NÅGRA av dem** → använd `pivotTable.GetPivotCache().Refresh();` för en cache. Eftersom cachen är delad, uppdaterar detta enda anrop varje pivottabell som är byggd ovanpå den cachen. Andra pivottabeller som ligger på en redan uppdaterad cache kan säkert hoppas över.
- **Endast pivotvisningen/layouten har ändrats** → använd `pivotTable.CalculateData();` för att rendera om från den befintliga cachen utan att hämta från källan.

Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

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

    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
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

## Vilket uppdaterings-API ska jag använda?

Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja var och en.

| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.RefreshAll()` | Ett anrop; täcker alla cachar och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.RefreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.GetPivotCache().Refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast visnings-/layoutinställningar har ändrats | `pivotTable.CalculateData()` | Hoppar över onödig källhämtning. |
| Lista alla pivottabeller på en delad cache | `pivotCache.GetPivotTables()` | Använd för att räkna upp före bulkuppdatering. |

I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade `RefreshData()` per tabell. De är medvetna om delade cachar, de undviker redundanta källhämtningar, och de låter dig välja den minsta omfattning som uppfyller ditt uppdateringskrav.{{< app/cells/assistant language="cpp" >}}
