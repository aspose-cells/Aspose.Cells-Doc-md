---
title: Manage Pivot Table Value Fields in Aspose.Cells for .NET
linktitle: Value Fields
description: Learn how to add base fields to the data region of a pivot table, change the summary function with PivotField.Function, and plot the value field onto the Row or Column axis in Aspose.Cells for C++.
keywords: Aspose.Cells, C++, pivot table, value field, PivotField, PivotField.Function, data field, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /cpp/pivot-table-manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## Adding a Field to the Data Region

Adding a base field to the data (value) region is the first step in shaping how a pivot table aggregates your source data. Aspose.Cells exposes `PivotTable.AddFieldToArea(PivotFieldType, string)`, an overload that accepts the constant `PivotFieldType.Data` and the source-column name. Once a field is added to the data region, the API exposes it through the `PivotTable.DataFields` collection, in the order in which the fields were added. By default, a numeric source column is summarised with `ConsolidationFunction.Sum`, while a non-numeric column defaults to `Count`.

## Changing the Summary Function

{{% alert color="primary" %}}
Changing `Function` only affects the aggregate, the source column does not change.
{{% /alert %}}

## Plotting Value Fields to Row or Column Axis

When a pivot table contains two or more data fields, Aspose.Cells exposes an additional virtual field called `PivotTable.ValuesField`. This virtual field represents the aggregate of every data field that lives in the data region. You can drag it into the Row or Column region as a base pivot field, which is useful for laying out multiple measures side by side.

{{% alert color="primary" %}}
`PivotTable.ValuesField` does not work if there is no or only one value field.
{{% /alert %}}

## **Dragging a Base Field into the Value Region**

This scenario shows how to put a single base field (`Amount`) into the data region of an existing pivot table. The shared pivot structure places `Category` and `Item` on the Row axis and `Year` on the Column axis. After the operation, `Amount` appears in the data region and is computed as the `Sum` of `Amount` by default.

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

 // Headers in A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));

 // Data rows A2:D9 using nested loops branching on j
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

 // Add pivot table at F3 with name PivotTable1
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

 // Pivot layout: Category and Item on Row, Year on Column, Amount as data field
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

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 intrusive_ptr<Workbook> workbook = new Workbook();
 intrusive_ptr<Worksheet> ws = workbook->GetWorksheets()->Get(0);
 ws->SetName("Data");
 Vector<String> headers{ "Category", "Item", "Year", "Amount" };
 for (int j = 0; j < 4; j++) ws->GetCells()->Get(0, j)->PutValue(headers[j]);

 Vector<Vector<Object*>> data;
 // Fill data ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 intrusive_ptr<PivotTable> pivotTable = ws->GetPivotTables()->Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType_Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 intrusive_ptr<PivotField> countField = pivotTable->GetDataFields()->Get(1);
 countField->SetFunction(ConsolidationFunction_Count);
 pivotTable->CalculateData();
 workbook->Save("output_function.xlsx");
}
```

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 intrusive_ptr<Workbook> workbook = new Workbook();
 intrusive_ptr<Worksheet> ws = workbook->GetWorksheets()->Get(0);
 ws->SetName("Data");
 // ... build data ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 intrusive_ptr<PivotTable> pivotTable = ws->GetPivotTables()->Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType_Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
 pivotTable->AddFieldToArea(PivotFieldType_Column, pivotTable->GetValuesField()->GetName());
 pivotTable->CalculateData();
 workbook->Save("output_plot.xlsx");
}
```

{{< app/cells/assistant language="cpp" >}}
