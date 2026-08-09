---
title: Värdefält i Aspose.Cells for C++
linktitle: Värdefält i Aspose.Cells for C++
description: Lär dig hur du lägger till basfält i dataregionen i en pivottabell, ändrar summeringsfunktionen med PivotField.Function, och placerar värdefältet på rad- eller kolumnaxeln i Aspose.Cells for C++.
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
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

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
{{% /alert %}}
Du kan därför lämna ett datafält som `Sum` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `Count` eller `Average`, allt i en enda pivot.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 Vector<String> headers{ "Category", "Item", "Year", "Amount" };
 for (int j = 0; j < 4; j++) ws->GetCells()->Get(0, j)->PutValue(headers[j]);

 Vector<Vector<Object*>> data;
 // Fyll i data ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 PivotField countField = pivotTable.GetDataFields().Get(1);
 countField->SetFunction(ConsolidationFunction_Count);
 pivotTable->CalculateData();
 workbook->Save("output_function.xlsx");
}
```

## Placera värdefält på rad- eller kolumnaxeln
När en pivottabell innehåller två eller flera datafält, exponerar Aspose.Cells ett ytterligare virtuellt fält kallat `PivotTable.ValuesField`. Detta virtuella fält representerar aggregatet av varje datafält som finns i dataregionen. Du kan dra det till rad- eller kolumnregionen som ett baspivotfält, vilket är användbart för att placera flera mått sida vid sida.
{{% alert color="primary" %}}
`PivotTable.ValuesField` fungerar inte om det inte finns något eller bara ett värdefält.
{{% /alert %}}
Scenarierna nedan går igenom tre kompletta exempel som visar varje funktion som beskrivs ovan mot samma pivotstruktur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 // ... bygg data ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
 pivotTable->AddFieldToArea(PivotFieldType::Column, pivotTable->GetValuesField()->GetName());
 pivotTable->CalculateData();
 workbook->Save("output_plot.xlsx");
}
```

{{< app/cells/assistant language="cpp" >}}