---
title: Wertfelder in Aspose.Cells for C++
description: Erfahren Sie, wie Sie Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertfeld auf die Zeilen- oder Spaltenachse in Aspose.Cells for C++ setzen.
linktitle: Wertfelder
keywords: Aspose.Cells, C++, PivotTable, Wertfeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /de/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Hinzufügen eines Felds zum Datenbereich
Das Hinzufügen eines Basisfelds zum Daten- (Wert-) Bereich ist der erste Schritt bei der Gestaltung der Aggregation Ihrer Quelldaten durch eine PivotTable. Aspose.Cells stellt `PivotTable.AddFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.Data` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, wird es über die Sammlung `PivotTable.DataFields` in der Reihenfolge bereitgestellt, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.Sum` zusammengefasst, während eine nicht-numerische Spalte standardmäßig `Count` verwendet.

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
 PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);
 // Pivot-Layout: Kategorie und Element in Zeile, Jahr in Spalte, Betrag als Datenfeld
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

## Ändern der Zusammenfassungsfunktion
Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz gekapselt, und seine `Function`-Eigenschaft gibt einen Wert aus der Enumeration `ConsolidationFunction` zurück. Über denselben `Function`-Setter können Sie zwischen den verfügbaren Aggregaten wechseln, einschließlich `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` und `Varp`.

{{% alert color="primary" %}}
Das Ändern von `Function` wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
Sie können daher ein Datenfeld als `Sum` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte verweist, aber `Count` oder `Average` verwendet, alles in einer einzigen PivotTable.
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

## Wertfelder auf die Zeilen- oder Spaltenachse setzen
Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.ValuesField` bereit. Dieses virtuelle Feld stellt das Aggregat jedes Datenfelds dar, das sich im Datenbereich befindet. Sie können es als Basisfeld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Kennzahlen nebeneinander anzuordnen.

{{% alert color="primary" %}}
`PivotTable.ValuesField` funktioniert nicht, wenn kein oder nur ein Wertfeld vorhanden ist.
Die folgenden Szenarien durchlaufen drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben PivotTable-Struktur demonstrieren.
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