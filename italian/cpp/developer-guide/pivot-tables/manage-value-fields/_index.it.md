---
title: Campi valore in Aspose.Cells for C++
linktitle: Campi valore
description: Scopri come aggiungere campi base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.Function e tracciare il campo valore sull'asse Riga o Colonna in Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tabella pivot, campo valore, PivotField, PivotField.Function, campo dati, PivotTable.ValuesField, Somma, Media
type: docs
weight: 230
url: /it/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Aggiunta di un campo all'area dati

Aggiungere un campo base all'area dati (valore) è il primo passo per definire il modo in cui una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.AddFieldToArea(PivotFieldType, string)`, un overload che accetta la costante `PivotFieldType.Data` e il nome della colonna di origine. Una volta che un campo viene aggiunto all'area dati, l'API lo espone attraverso la raccolta `PivotTable.DataFields`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna di origine numerica viene riassunta con `ConsolidationFunction.Sum`, mentre una colonna non numerica utilizza `Count` come valore predefinito.

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

 // Intestazioni in A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));

 // Righe di dati A2:D9 utilizzando cicli annidati che si diramano su j
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

 // Aggiungi tabella pivot in F3 con nome PivotTable1
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

 // Layout pivot: Categoria e Articolo su Riga, Anno su Colonna, Importo come campo dati
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

## Modifica della funzione di riepilogo

Ogni campo posizionato nell'area dati è incapsulato internamente come un'istanza di `PivotField`, e la sua proprietà `Function` restituisce un valore dall'enum `ConsolidationFunction`. Lo stesso setter `Function` ti permette di passare tra le aggregazioni disponibili, tra cui `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` e `Varp`.

{{% alert color="primary" %}}
La modifica di `Function` influisce solo sull'aggregazione, la colonna di origine non cambia.
{{% /alert %}}

Puoi quindi lasciare un campo dati come `Sum` mentre aggiungi un secondo campo dati che fa riferimento alla stessa colonna di origine ma utilizza `Count` o `Average`, tutto in un'unica tabella pivot.

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
 // Riempi dati ...
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

## Tracciare i campi valore sull'asse Riga o Colonna

Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un ulteriore campo virtuale chiamato `PivotTable.ValuesField`. Questo campo virtuale rappresenta l'aggregazione di ogni campo dati presente nell'area dati. Puoi trascinarlo nell'area Riga o Colonna come campo pivot base, il che è utile per disporre più misure affiancate.

{{% alert color="primary" %}}
`PivotTable.ValuesField` non funziona se non ci sono campi valore o se ce n'è solo uno.
{{% /alert %}}

Gli scenari seguenti illustrano tre esempi end-to-end che dimostrano ciascuna funzionalità descritta sopra sulla stessa struttura di pivot.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 // ... costruisci dati ...
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