---
title: Wertfelder in Aspose.Cells for C++
linktitle: Wertfelder
description: Erfahren Sie, wie Sie Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertfeld auf die Zeilen- oder Spaltenachse in Aspose.Cells for C++ setzen.
keywords: Aspose.Cells, C++, PivotTable, Wertfeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /de/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
Wertfelder sind das Herzstück jeder PivotTable, die numerischen Aggregate, die die Quelldaten zusammenfassen. In Aspose.Cells for C++ wird der Datenbereich einer PivotTable durch Hinzufügen von Basisfeldern über `PivotTable.AddFieldToArea` gefüllt, und jedes in diesem Bereich platzierte Feld kann seine eigene Zusammenfassungsfunktion besitzen. Wenn zwei oder mehr Datenfelder vorhanden sind, stellt Aspose.Cells ein spezielles Aggregatfeld, `PivotTable.ValuesField`, bereit, das als Basisfeld auf die Zeilen- oder Spaltenachse gesetzt werden kann, was Ihnen eine feinere Kontrolle darüber gibt, wie Wertfelder im Layout erscheinen.
## Hinzufügen eines Felds zum Datenbereich
Das Hinzufügen eines Basisfelds zum Daten- (Wert-) Bereich ist der erste Schritt bei der Gestaltung der Aggregation Ihrer Quelldaten durch eine PivotTable. Aspose.Cells stellt `PivotTable.AddFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.Data` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, wird es über die Sammlung `PivotTable.DataFields` in der Reihenfolge bereitgestellt, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.Sum` zusammengefasst, während eine nicht-numerische Spalte standardmäßig `Count` verwendet.
## Ändern der Zusammenfassungsfunktion
Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz gekapselt, und seine `Function`-Eigenschaft gibt einen Wert aus der Enumeration `ConsolidationFunction` zurück. Über denselben `Function`-Setter können Sie zwischen den verfügbaren Aggregaten wechseln, einschließlich `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` und `Varp`.
{{% alert color="primary" %}}
Das Ändern von `Function` wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
{{% /alert %}}
Sie können daher ein Datenfeld als `Sum` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte verweist, aber `Count` oder `Average` verwendet, alles in einer einzigen PivotTable.
## Wertfelder auf die Zeilen- oder Spaltenachse setzen
Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.ValuesField` bereit. Dieses virtuelle Feld stellt das Aggregat jedes Datenfelds dar, das sich im Datenbereich befindet. Sie können es als Basisfeld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Kennzahlen nebeneinander anzuordnen.
{{% alert color="primary" %}}
`PivotTable.ValuesField` funktioniert nicht, wenn kein oder nur ein Wertfeld vorhanden ist.
{{% /alert %}}
Die folgenden Szenarien durchlaufen drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben PivotTable-Struktur demonstrieren.
## Szenario 1 — Ziehen eines Basisfelds in den Wertebereich
Dieses Szenario zeigt, wie ein einzelnes Basisfeld (`Amount`) in den Datenbereich einer bestehenden PivotTable eingefügt wird. Die gemeinsame PivotTable-Struktur platziert `Category` und `Item` auf der Zeilenachse und `Year` auf der Spaltenachse. Nach der Operation erscheint `Amount` im Datenbereich und wird standardmäßig als `Sum` von `Amount` berechnet.
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

 // Überschriften in A1:D1
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));

 // Datenzeilen A2:D9 mit verschachtelten Schleifen, die nach j verzweigen
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

 // Pivot-Tabelle bei F3 mit dem Namen PivotTable1 hinzufügen
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

 // Pivot-Layout: Kategorie und Element in Zeile, Jahr in Spalte, Betrag als Datenfeld
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

 pivotTable.RefreshData();
 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");

 Aspose::Cells::Cleanup();
 return 0;
}
```
## Szenario 2 — Ändern der Zusammenfassungsfunktion
Dieses Szenario beginnt mit derselben PivotTable-Struktur wie Szenario 1, fügt jedoch das Feld `Amount` zweimal zum Datenbereich hinzu. Beide Datenfelder verweisen auf dieselbe Quellspalte, jedoch wird das zweite Feld mit dem Setter `PivotField.Function` überschrieben, sodass es `Count` anstelle des standardmäßigen `Sum` verwendet.
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
 // Daten ausfüllen ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 intrusive_ptr<PivotTable> pivotTable = ws->GetPivotTables()->Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType_Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 intrusive_ptr<PivotField> countField = pivotTable->GetDataFields()->Get(1);
 countField->SetFunction(ConsolidationFunction_Count);
 pivotTable->RefreshData();
 pivotTable->CalculateData();
 workbook->Save("output_function.xlsx");
}
```
## Szenario 3 — Wertfelder auf die Zeilen- oder Spaltenachse setzen
Mit zwei vorhandenen Datenfeldern wird `PivotTable.ValuesField` nutzbar. Dieses Szenario zieht dieses virtuelle Aggregatfeld in den Spaltenbereich, sodass jede Kennzahl im Datenbereich als eigener Spaltenblock neben `Year` erscheint.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 intrusive_ptr<Workbook> workbook = new Workbook();
 intrusive_ptr<Worksheet> ws = workbook->GetWorksheets()->Get(0);
 ws->SetName("Data");
 // ... Daten aufbauen ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 intrusive_ptr<PivotTable> pivotTable = ws->GetPivotTables()->Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType_Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType_Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType_Data, "Amount");
 pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
 pivotTable->AddFieldToArea(PivotFieldType_Column, pivotTable->GetValuesField()->GetName());
 pivotTable->RefreshData();
 pivotTable->CalculateData();
 workbook->Save("output_plot.xlsx");
}
```
Zusammen decken diese drei Szenarien jeden Aspekt der Wertfeldmanipulation in Aspose.Cells for C++ ab, von einem einzelnen Datenfeld mit dem Standardwert `Sum` bis zu einer PivotTable mit mehreren Kennzahlen, bei der das virtuelle `ValuesField` das Layout auf der Zeilen- oder Spaltenachse steuert.
## Verwandte Artikel
- [Zeilen- und Spaltenfelder in PivotTables in Aspose.Cells for C++](/cells/de/cpp/row-and-column-fields/)
- [Seitenfelder in PivotTables](/cells/de/cpp/add-page-field-in-pivot-table/)
- [Aktualisieren von PivotTables in Aspose.Cells for C++](/cells/de/cpp/refresh-pivot-table/)
- [Anwenden von Stilen auf PivotTables](/cells/de/cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="cpp" >}}