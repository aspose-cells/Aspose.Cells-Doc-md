---
title: Värdefält i Aspose.Cells for C++
description: Lär dig hur du lägger till basfält i dataregionen i en pivottabell, ändrar summeringsfunktionen med PivotField.Function, och placerar värdefältet på rad- eller kolumnaxeln i Aspose.Cells for C++.
linktitle: Värdefält i Aspose.Cells for C++
keywords: Aspose.Cells, C++, pivottabell, värdefält, PivotField, PivotField.Function, datafält, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /sv/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Lägga till ett fält i dataregionen
Att lägga till ett basfält i data- (värde-) regionen är det första steget för att forma hur en pivottabell aggregerar din källdata. Aspose.Cells exponerar `PivotTable.AddFieldToArea(PivotFieldType, string)`, en överlagring som accepterar konstanten `PivotFieldType.Data` och källkolumnens namn. När ett fält väl har lagts till i dataregionen, exponerar API:t det via samlingen `PivotTable.DataFields`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.Sum`, medan en icke-numerisk kolumn som standard använder `Count`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
 Aspose::Cells::Startup();
 Workbook workbook;
 Worksheet worksheet = workbook.GetWorksheets().Get(0);
 worksheet.SetName(u"Data");
 Cells cells = worksheet.GetCells();
 // Rubriker i A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));
 // Datarader A2:D9 med kapslade slingor som förgrenar sig på j
 for (int i = 1; i <= 8; i++)
 {
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 cells.Get(i, j).PutValue(U16String(i <= 4 ? "Fruit" : "Vegetable"));
 break;
 case 1:
 if (i == 1 || i == 2) cells.Get(i, j).PutValue(U16String("Apple"));
 else if (i == 3 || i == 4) cells.Get(i, j).PutValue(U16String("Banana"));
 else if (i == 5 || i == 6) cells.Get(i, j).PutValue(U16String("Carrot"));
 else cells.Get(i, j).PutValue(U16String("Daikon"));
 break;
 case 2:
 cells.Get(i, j).PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) cells.Get(i, j).PutValue(100);
 else if (i == 2) cells.Get(i, j).PutValue(150);
 else if (i == 3) cells.Get(i, j).PutValue(80);
 else if (i == 4) cells.Get(i, j).PutValue(90);
 else if (i == 5) cells.Get(i, j).PutValue(50);
 else if (i == 6) cells.Get(i, j).PutValue(60);
 else if (i == 7) cells.Get(i, j).PutValue(40);
 else cells.Get(i, j).PutValue(45);
 break;
 }
 }
 }
 // Lägg till pivottabell vid F3 med namnet PivotTable1
 PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);
 // Pivotlayout: Category och Item på Rad, Year på Kolumn, Amount som datafält
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");
 Aspose::Cells::Cleanup();
 return 0;
}
```

## Ändra summeringsfunktionen
Varje fält som placeras i dataregionen omsluts internt som en `PivotField`-instans, och dess `Function`-egenskap returnerar ett värde från enumerationen `ConsolidationFunction`. Samma `Function`-sättare låter dig växla mellan de tillgängliga aggregaten, inklusive `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` och `Varp`.

{{% alert color="primary" %}}
Att ändra `Function` påverkar bara aggregatet, källkolumnen ändras inte.
Du kan därför lämna ett datafält som `Sum` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `Count` eller `Average`, allt i en enda pivot.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana", u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) {
                worksheet.GetCells().Get(i, j).PutValue(i <= 4 ? u"Fruit" : u"Vegetable");
            } else if (j == 1) {
                worksheet.GetCells().Get(i, j).PutValue(items[i - 1]);
            } else if (j == 2) {
                worksheet.GetCells().Get(i, j).PutValue(years[i - 1]);
            } else {
                worksheet.GetCells().Get(i, j).PutValue(amounts[i - 1]);
            }
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField countField = pivotTable.GetDataFields().Get(1);
    countField.SetFunction(ConsolidationFunction::Count);

    pivotTable.CalculateData();

    wb.Save(u"output_function.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Placera värdefält på rad- eller kolumnaxeln
När en pivottabell innehåller två eller flera datafält, exponerar Aspose.Cells ett ytterligare virtuellt fält kallat `PivotTable.ValuesField`. Detta virtuella fält representerar aggregatet av varje datafält som finns i dataregionen. Du kan dra det till rad- eller kolumnregionen som ett baspivotfält, vilket är användbart för att placera flera mått sida vid sida.

{{% alert color="primary" %}}
`PivotTable.ValuesField` fungerar inte om det inte finns något eller bara ett värdefält.
Scenarierna nedan går igenom tre kompletta exempel som visar varje funktion som beskrivs ovan mot samma pivotstruktur.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Category"));
    cells.Get(0, 1).PutValue(U16String("Item"));
    cells.Get(0, 2).PutValue(U16String("Year"));
    cells.Get(0, 3).PutValue(U16String("Amount"));

    std::vector<U16String> categories = {
        U16String("Fruit"), U16String("Fruit"), U16String("Fruit"), U16String("Fruit"),
        U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable")
    };
    std::vector<U16String> items = {
        U16String("Apple"), U16String("Apple"), U16String("Banana"), U16String("Banana"),
        U16String("Carrot"), U16String("Carrot"), U16String("Daikon"), U16String("Daikon")
    };
    int years[8] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[8] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) cells.Get(i, j).PutValue(categories[i - 1]);
            else if (j == 1) cells.Get(i, j).PutValue(items[i - 1]);
            else if (j == 2) cells.Get(i, j).PutValue(years[i - 1]);
            else cells.Get(i, j).PutValue(amounts[i - 1]);
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::Count);

    pivotTable.AddFieldToArea(PivotFieldType::Column, pivotTable.GetValuesField().GetName());

    pivotTable.CalculateData();
    workbook.Save(u"output_plot.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}