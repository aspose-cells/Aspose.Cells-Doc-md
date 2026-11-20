---
title: Diskret gruppering av objekt i pivotfält
linktitle: Diskret gruppering
description: Lär dig hur du grupperar objekt i pivotfält i anpassade grupper med egna namn, till exempel frukt och grönsaker, med hjälp av DiscreteGroupItem och PivotFieldGroupOptions.DiscreteGroupItems i Aspose.Cells for C++.
keywords: Aspose.Cells for C++, pivottabell, diskret gruppering, DiscreteGroupItem, PivotFieldGroupOptions, gruppera pivotobjekt, anpassade grupper, PivotField.Group, C++, Excel-pivottabell
type: docs
weight: 90
url: /sv/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Automatisk gruppering samlar objekt efter datatyp, till exempel datum till månader och kvartal eller tal till intervall. Diskret gruppering används i stället för att samla specifika, orelaterade objekt i anpassade grupper med egna namn, till exempel produkter i grupperna frukt och grönsaker, butiker i regioner eller konton i zoner. Aspose.Cells erbjuder diskret gruppering med hjälp av klassen `DiscreteGroupItem` och egenskapen `PivotFieldGroupOptions.DiscreteGroupItems`.
- En `DiscreteGroupItem` består av ett gruppnamn och de objekt som tillhör det. Objekten kan identifieras på två sätt: antingen med sina namn (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) eller med sina nollbaserade positioner i källdatan (`DiscreteGroupItem("fruit", { 0, 3 })`). Båda formerna ger samma resultat.
- Diskret gruppering tillämpas på ett fält i rad- eller kolumnområdet i pivottabellen genom att skicka alternativen till `PivotField.Group(PivotFieldGroupOptions)`.

## **Gruppera objekt i pivotfält efter objektnamn**
Följande exempel bygger en liten försäljningslista (product, date och amount), skapar en pivottabell från listan med `product` i radområdet, `date` i kolumnområdet och `amount` i dataområdet och definierar sedan två anpassade grupper baserade på objektnamnen: fruit (grape, cherry) och vegetable (carrot, potato). Resultatet visar en radlayout med två nivåer: gruppnamnet ligger på den yttre nivån och de ursprungliga objekten är nästlade under, så att trender kan läsas för varje anpassad grupp och varje objekt.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Efter `CalculateData()` visar pivottabellens radområde fruit (grape 50, cherry 80) och vegetable (carrot 60, potato 70) med totalsumman 260, och kolumnetiketterna behåller de fyra datumen (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppera objekt i pivotfält efter objektindex**
När objektnamnen är långa eller lokaliserade kan objekten identifieras med den andra konstruktorn för `DiscreteGroupItem`, som använder index. Indexen anger de nollbaserade positionerna för objekten i den ordning de förekommer i källdatan, inte i alfabetisk ordning. I exempeldata ovan har grape objektindex 0, carrot objektindex 1, potato objektindex 2 och cherry objektindex 3, så att fruit är `{ 0, 3 }` och vegetable är `{ 1, 2 }`. Resultatet är identiskt med det namnbaserade exemplet.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Obs**

{{% alert color="primary" %}}
- Objekt som inte har tilldelats någon anpassad grupp försvinner inte. De stannar i pivottabellen på samma nivå som de anpassade grupperna, var och en som en separat post med ett enda objekt. Om endast gruppen fruit definieras i exemplet ovan lämnas carrot och potato kvar i radområdet som fristående poster bredvid gruppen fruit.
- Egenskapen `PivotFieldGroupOptions.NewPivotField` styr layouten för diskret gruppering. Standardvärdet är `true`, vilket lägger till det grupperade fältet som ett nytt yttre fält bredvid originalfältet och skapar den layout med två nivåer som visas ovan (`RowFields` ökar till 2). Ange värdet `false` för att i stället ersätta originalfältet. Radområdet visar då en enda nivå som endast innehåller gruppnamnen och deras aggregerade värden: fruit 130 (50 + 80) och vegetable 130 (60 + 70).
- De namnbaserade respektive indexbaserade konstruktorerna för `DiscreteGroupItem` kan kombineras inom samma `DiscreteGroupItems`-samling.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/cpp/group-pivot-fields-in-the-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabellen](/cells/sv/cpp/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/cpp/filter-by-label-or-value-of-pivot-table/)
- [Tillämpa format på pivottabellen](/cells/sv/cpp/apply-style-to-pivot-table/)
- [Uppdatera pivottabellen](/cells/sv/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}