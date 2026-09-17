---
title: Hinzufügen von Zeilen- und Spaltenfeldern zu einer PivotTable in Aspose.Cells for C++
linktitle: Hinzufügen von Zeilen- und Spaltenfeldern zu einer PivotTable
description: Erfahren Sie, wie Sie Basisfelder zu den Zeilen- und Spaltenbereichen einer PivotTable hinzufügen und Zwischensummen für PivotFields mithilfe von PivotField.SetSubtotals in Aspose.Cells for C++ steuern.
keywords: Aspose.Cells, C++, PivotTable, Zeilenfeld, Spaltenfeld, PivotField, SetSubtotals, PivotFieldSubtotalType, Zwischensummen
type: docs
weight: 220
url: /de/cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**
Die Methode `PivotTable.AddFieldToArea(PivotFieldType fieldType, U16String fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Bereiche einer PivotTable. Das Argument `fieldType` akzeptiert einen der folgenden `PivotFieldType`-Werte.
- `Row` — Felder, die vertikal auf der linken Seite angeordnet werden
- `Column` — Felder, die horizontal oben angeordnet werden
- `Data` — Felder, deren Werte aggregiert werden
- `Page` — Felder, die als Berichtsfilter verwendet werden
Die Reihenfolge der Feldverschachtelung ist wichtig. Wenn `Category` zuerst zum Zeilenbereich und anschließend `Item` hinzugefügt wird, weist die resultierende PivotTable die äußere Gruppierung `Category` und die innere Gruppierung `Item` auf. Wird die Reihenfolge umgekehrt, wird auch die Hierarchie umgekehrt.

## **PivotField-Zwischensummen**
Die Methode `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` steuert, welche Zwischensummenzeilen für ein PivotField angezeigt werden. Mit jedem Aufruf wird genau ein Zwischensummentyp unabhängig von den übrigen Typen aktiviert oder deaktiviert. Durch das Übergeben von `shown = true` wird die Zwischensumme angezeigt, während `shown = false` sie ausblendet. Da jeder Aufruf nur einen Typ betrifft, können Sie durch mehrere Methodenaufrufe mit unterschiedlichen `subtotalType`-Werten eine benutzerdefinierte Auswahl an Zwischensummen festlegen.
Die Enumeration `PivotFieldSubtotalType` definiert die verfügbaren Zwischensummenarten.
- `Automatic` — Aspose.Cells wählt die Standardoption (in der Regel `Sum` für numerische Felder)
- `None` — Alle Zwischensummenzeilen werden unterdrückt
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
Zwischensummen werden nur angezeigt, wenn der Zeilen- oder Spaltenbereich mindestens zwei PivotFields enthält. Bei einem einzelnen Feld gibt es keine Daten, für die eine aussagekräftige Zwischensumme gebildet werden könnte, sodass `SetSubtotals`-Aufrufe in diesem Fall keine sichtbare Wirkung haben. Dieser Artikel verwendet daher in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Zwischensumme am Übergang zwischen den einzelnen `Category`-Gruppen sichtbar ist.
{{% /alert %}}

## **Szenario 1 — Automatische Zwischensummen (Standard)**
Wenn `SetSubtotals` nicht aufgerufen wird, wendet Aspose.Cells auf numerische Felder die Option `Automatic` an. Das folgende Beispiel bestätigt dieses Verhalten ausdrücklich, indem `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` für das äußere Zeilenfeld `Category` aufgerufen wird.

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

## **Szenario 2 — Alle Zwischensummen unterdrücken (None)**
Der Aufruf von `SetSubtotals(PivotFieldSubtotalType.None, true)` entfernt alle Zwischensummenzeilen aus der PivotTable, sodass nur die Feldzeilen und die Gesamtsumme am unteren Ende verbleiben. Dies ist hilfreich, wenn die gruppierten Rohdaten ohne Zusammenfassungszeilen angezeigt werden sollen.

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

## **Szenario 3 — Benutzerdefinierte Teilmenge von Zwischensummen (Sum + Average)**
Sie sind nicht auf einen einzelnen Zwischensummentyp beschränkt. Jeder `SetSubtotals`-Aufruf wirkt unabhängig auf einen Typ. Wenn Sie die Methode daher zweimal aufrufen — einmal mit `Sum` und einmal mit `Average` — wird für jede `Category`-Gruppe eine benutzerdefinierte Auswahl aus zwei Zwischensummenzeilen erstellt.

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

## **Zusammenfassung**

## **Verwandte Artikel**
- [Seitenfelder in PivotTables](/cells/de/cpp/add-page-field-in-pivot-table/)
- [Aktualisieren von PivotTables in Aspose.Cells for C++](/cells/de/cpp/refresh-pivot-table/)
- [Anwenden von Stilen auf PivotTables](/cells/de/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}