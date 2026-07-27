---
title: Lägga till rad- och kolumnfält i en pivottabell i Aspose.Cells för .NET
linktitle: Rad- och kolumnfält
description: Lär dig hur du lägger till basfält i rad- och kolumnområdena i en pivottabell och styr pivotfältets delsummor med PivotField.SetSubtotals i Aspose.Cells for C++.
keywords: Aspose.Cells, C++, pivottabell, radfält, kolumnfält, PivotField, SetSubtotals, PivotFieldSubtotalType, delsummor
type: docs
weight: 220
url: /sv/cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Lägga till ett fält i rad- eller kolumnområdet**

Metoden `PivotTable.AddFieldToArea(PivotFieldType fieldType, intrusive_ptr<Aspose::Cells::Systems::String> fieldName)` flyttar ett basfält från källdatan till ett av de fyra pivotområdena. Argumentet `fieldType` accepterar ett av följande `PivotFieldType`-värden.

- `Row` — fält som placeras vertikalt till vänster
- `Column` — fält som placeras horisontellt överst
- `Data` — fält vars värden aggregeras
- `Page` — fält som används som rapportfilter

När fälten har lagts till kan du komma åt dem via egenskaperna `PivotTable.RowFields` och `PivotTable.ColumnFields`. Varje egenskap returnerar en `PivotFieldCollection`. Fältet vid index 0 i `RowFields` är det yttersta radfältet, och efterföljande index representerar fält som är nästlade inuti det. Samma indexeringskonvention gäller för `ColumnFields`.

Ordningen på fältnästningen spelar roll. Om du lägger till `Category` i radområdet först och sedan `Item` skapas en pivot vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Om du vänder på ordningen får du omvänd hierarki.

## **Pivotfältets delsummor**

Metoden `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` styr vilka delsummerader som visas för ett pivotfält. Varje anrop växlar en enskild delsummatyp oberoende. Om du skickar `shown = true` visas delsummoraden, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ, kan du bygga en anpassad uppsättning delsummor genom att anropa metoden flera gånger med olika `subtotalType`-värden.

Enumen `PivotFieldSubtotalType` definierar de tillgängliga delsummekategorierna.

- `Automatic` — Aspose.Cells väljer standardvalet (vanligtvis `Sum` för numeriska fält)
- `None` — undertryck alla delsummerader
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Delsummor renderas endast när det finns två eller fler pivotfält i radområdet (eller i kolumnområdet). Ett enskilt fält har inget meningsfullt att göra delsummor mellan, så `SetSubtotals`-anrop har ingen synlig effekt i det fallet. Denna artikel placerar därför två radfält (`Category` ytterst, `Item` innerst) i varje exempel så att delsummegränsen mellan varje `Category`-grupp syns.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) delsummor**

När du inte anropar `SetSubtotals` alls tillämpar Aspose.Cells valet `Automatic` på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` på det yttre `Category`-radfältet.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Automatic, true);

    pivotTable.CalculateData();

    workbook.Save(u"output_automatic.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Scenario 2 — Undertrycka alla delsummor (None)**

Att anropa `SetSubtotals(PivotFieldSubtotalType.None, true)` tar bort alla delsummerader från pivottabellen och lämnar endast fältraderna och totalsumman längst ned. Detta är användbart när du vill ha den råa grupperade datan utan några sammanfattningsrader.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.SetName(u"Data");

    U16String headers[] = { u"Category", u"Item", u"Year", u"Amount" };
    for (int j = 0; j < 4; j++) {
        sheet.GetCells().Get(0, j).PutValue(headers[j]);
    }

    U16String categories[] = { u"Fruit", u"Fruit", u"Fruit", u"Fruit",
                               u"Vegetable", u"Vegetable", u"Vegetable", u"Vegetable" };
    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana",
                          u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[]   = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = {  100,  150,   80,   90,   50,   60,   40,   45 };

    for (int i = 0; i < 8; i++) {
        sheet.GetCells().Get(i + 1, 0).PutValue(categories[i]);
        sheet.GetCells().Get(i + 1, 1).PutValue(items[i]);
        sheet.GetCells().Get(i + 1, 2).PutValue(years[i]);
        sheet.GetCells().Get(i + 1, 3).PutValue(amounts[i]);
    }

    int pivotIndex = sheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::None, true);
    pivotTable.CalculateData();

    wb.Save(u"output_none.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Scenario 3 — Anpassad delsummauppsättning (Sum + Average)**

Du är inte begränsad till en enda delsummatyp. Varje `SetSubtotals`-anrop fungerar oberoende på en typ, så genom att anropa metoden två gånger — en gång med `Sum` och en gång med `Average` — skapas en anpassad uppsättning av två delsummerader för varje `Category`-grupp.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(u"A1").PutValue(u"Category");
    worksheet.GetCells().Get(u"B1").PutValue(u"Item");
    worksheet.GetCells().Get(u"C1").PutValue(u"Year");
    worksheet.GetCells().Get(u"D1").PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Average, true);

    pivotTable.CalculateData();

    workbook.Save(u"output_custom.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sammanfattning**

De tre scenarierna ovan delar samma dataset och pivottabellstruktur. Den enda skillnaden mellan dem är `SetSubtotals`-anropet som tillämpas på det yttre `Category`-radfältet. Kom ihåg regeln om två fält: ett enskilt fält i ett område har inget att göra delsummor mellan, så placera alltid minst två fält i rad- eller kolumnområdet när du vill att `SetSubtotals` ska ha en synlig effekt.

## **Relaterade artiklar**

- [Sidfält i pivottabeller](/cells/sv/cpp/add-page-field-in-pivot-table/)
- [Uppdatera pivottabeller i Aspose.Cells for C++](/cells/sv/cpp/refresh-pivot-table/)
- [Tillämpa stilar på pivottabeller](/cells/sv/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
