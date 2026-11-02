---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig att endast visa de högst eller lägst rankade objekten i ett pivotfält i Aspose.Cells for C++. Den här artikeln beskriver metoden Top10AutoShow för Excel 97-2003, hur du läser alternativ med GetTop10AutoShowSettings och filtret Topp 10 för Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, C++, pivottabell, topp 10, automatisk visning, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /sv/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsfall**
En pivottabell som listar varje objekt i ett radfält kan vara svårläst när fältet har tiotals medlemmar. En topp 10-rapport behåller endast de högst eller lägst rankade objekten, vilket är precis vad rankningsrapporter behöver – ”de 5 produkter som genererar högst intäkt” eller ”de 3 regioner med lägst antal sålda enheter”. Aspose.Cells stöder två mekanismer för detta, och de motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** — metoden `PivotField.Top10AutoShow()`. Detta är den klassiska inställningen ”Visa de översta/nedersta N objekten” som lagras direkt på pivotfältet. Den fungerar i alla Excel-versioner, gamla och nya, eftersom den ingår i pivottabellens ursprungliga format.
- **Excel 2007-365 Topp 10-filter** — metoden `PivotField.FilterTop10()`. Detta är det moderna topp 10-värdefiltret som finns under fältmenyns Värdefilter. Det lagras som ett `PivotFilter`-objekt kopplat till fältet och erbjuder rankning baserad på antal objekt eller procent.

## **Topp 10-visning i Excel 97-2003 (Top10AutoShow)**
Det klassiska AutoShow konfigureras med ett enda anrop till `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)`:
- `isAutoShow` — aktiverar eller inaktiverar AutoShow-inställningen på fältet.
- `isTop` — `true` behåller de högst rankade objekten (överst), `false` de lägst rankade (nederst).
- `count` — hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rankBy` — det nollbaserade indexet för **datafältet** vars värden används för att ranka objekten. Ange -1 för att ranka objekten efter fältet självt.
Rankningen kan drivas av ett värdefält eller av fältet självt. Det finns två naturliga varianter, som visas nedan.

### **Ranka efter ett värdefält**
Ranka radfältets objekt efter ett vanligt värdefält, till exempel Sum of Sales. Följande exempel bygger en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`), och visar sedan de två sporterna med högst försäljningsvärde. `rankBy` är 0 eftersom ”Sum of Sales” är datafältet på index 0.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Visa de 2 översta objekten rankade efter "Sum of Sales" (datafältsindex 0)
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Ranka efter fältet självt**
Ett fält kan också rankas på grundval av sina egna värden – ange -1 som `rankBy`. För den här varianten behövs inget extra datafält; fältet behöver bara placeras i rad- eller kolumnområdet. Följande exempel visar de tre lägst rankade sporterna när de rankas på grundval av sina egna värden. När inställningen sparas utelämnas attributet `rankBy` från pivottabellens XML eftersom -1 är formatets standardvärde, och `GetTop10AutoShowSettings().GetRankBy()` returnerar -1.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Visa de 3 lägsta objekten rankade efter fältet självt (rankBy = -1)
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Läsa aktuella alternativ (GetTop10AutoShowSettings)**
Metoden `PivotField.GetTop10AutoShowSettings()` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som ger åtkomst till de AutoShow-alternativ som för närvarande lagras på fältet. Använd metoden för att kontrollera hur objekt presenteras i en befintlig arbetsbok eller i en pivottabell som du nyligen har konfigurerat, även när arbetsboken har lästs in från en fil.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

De fyra medlemmarna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), så de värden som läses tillbaka är de värden som alla Excel-versioner kommer att respektera.

## **Obs**

{{% alert color="primary" %}}
- De direkta `PivotField`-egenskaperna `IsAutoShow`, `IsAscendShow`, `GetAutoShowCount` och `GetAutoShowField` är föråldrade. Använd i stället objektet `PivotFieldTop10AutoShowSettings`: `IsAutoShow` ersätts av `GetTop10AutoShowSettings().IsAutoShow()`, `IsAscendShow` ersätts av `GetTop10AutoShowSettings().IsTop()`, `GetAutoShowCount` ersätts av `GetTop10AutoShowSettings().GetAutoShowCount()` och `GetAutoShowField` ersätts av `GetTop10AutoShowSettings().GetRankBy()`. `Top10AutoShow()` är den metod som stöds för att ändra inställningarna.
- `Top10AutoShow` fungerar med rad- och kolumnfält. Ett fält som endast finns i sidoområdet (filterområdet) kan inte rankas på det här sättet eftersom dess objekt inte finns i pivottabellens resultatområde.
{{% /alert %}}

## **Excel 2007-365: Topp 10-filter (FilterTop10)**
Moderna Excel-versioner erbjuder Topp 10 som ett värdefilter i fältmenyn (Värdefilter, Topp 10...). Aspose.Cells modellerar det med metoden `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` — det nollbaserade indexet för det datafält vars aggregerade värden används för att ranka objekten.
- `type` — vad `itemCount` betyder. `PivotFilterType::Count` behåller ett bestämt antal objekt (alternativet Objekt i dialogrutan). `PivotFilterType::Percent` behåller en procentandel av objekten, så `itemCount` är självt procentvärdet – 30 behåller de översta 30 procenten. `PivotFilterType::Sum` använder den kumulativa värdetäckningen som grund för rankningen.
- `isTop` — `true` för Topp, `false` för Nederst.
- `itemCount` — talet N i Topp N; enheten beror på `type`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Top 10-filter — behåll de 2 högsta objekten efter "Sum of Sales" (datafältindex 0)
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // För ett procentuellt filter behåller du i stället de 30 högsta procenten av objekten:
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` och `FilterTop10` är två separata funktioner. AutoShow skriver det klassiska `autoShow`-attributet till pivotfältet, och det respekteras av alla Excel-versioner ända tillbaka till Excel 97. `FilterTop10` skriver in en modern `PivotFilter`-post, och den här funktionen kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version visas alla objekt i en pivottabell som använder det moderna filtret. För dokument som måste läsas och skrivas med äldre verktyg bör du välja `Top10AutoShow`; för moderna arbetsböcker bör du välja `FilterTop10` eftersom metoden kan kombineras med de andra värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/cpp/filter-by-label-or-value-of-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/cpp/pivot-table-add-row-and-column-fields/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/cpp/group-pivot-fields-in-the-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/cpp/refresh-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}