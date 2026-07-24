---
title: Zeilen- und Spaltenfelder in Aspose.Cells for C++
linktitle: Zeilen- und Spaltenfelder
description: Erfahren Sie, wie Sie Basisfelder zu den Zeilen- und Spaltenbereichen einer PivotTable hinzufügen und PivotField-Zwischensummen mit PivotField.SetSubtotals in Aspose.Cells for C++ steuern.
keywords: Aspose.Cells, C++, PivotTable, Zeilenfeld, Spaltenfeld, PivotField, SetSubtotals, PivotFieldSubtotalType, Zwischensummen
type: docs
weight: 220
url: /de/cpp/row-and-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Zeilen- und Spaltenfelder sind die Bausteine einer PivotTable. Ein Feld, das im Zeilenbereich platziert wird, erscheint vertikal auf der linken Seite der PivotTable, während ein Feld im Spaltenbereich horizontal oben angezeigt wird. Dieser Artikel zeigt, wie Sie Basisfelder programmatisch zu diesen Bereichen hinzufügen und wie Sie die zwischen Feldgruppen gerenderten Zwischensummen mithilfe der Methode `PivotField.SetSubtotals` steuern.

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**

Die Methode `PivotTable.AddFieldToArea(PivotFieldType fieldType, intrusive_ptr<Aspose::Cells::Systems::String> fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Pivot-Bereiche. Das `fieldType`-Argument akzeptiert einen der folgenden `PivotFieldType`-Werte.

- `Row` — Felder, die vertikal auf der linken Seite platziert werden
- `Column` — Felder, die horizontal oben platziert werden
- `Data` — Felder, deren Werte aggregiert werden
- `Page` — Felder, die als Berichtsfilter verwendet werden

Nachdem Felder hinzugefügt wurden, können Sie über die Eigenschaften `PivotTable.RowFields` und `PivotTable.ColumnFields` darauf zugreifen. Jede Eigenschaft gibt eine `PivotFieldCollection` zurück. Das Feld bei Index 0 von `RowFields` ist das äußerste Zeilenfeld, und nachfolgende Indizes repräsentieren Felder, die darin verschachtelt sind. Die gleiche Indexierungskonvention gilt für `ColumnFields`.

Die Verschachtelungsreihenfolge der Felder ist wichtig. Wenn `Category` zuerst zum Zeilenbereich und dann `Item` hinzugefügt wird, entsteht eine PivotTable, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Das Umkehren der Reihenfolge kehrt auch die Hierarchie um.

## **Zwischensummen von Pivot-Feldern**

Die Methode `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` steuert, welche Zwischensummenzeilen für ein Pivot-Feld angezeigt werden. Jeder Aufruf schaltet einen einzelnen Zwischensummentyp unabhängig um. Die Übergabe von `shown = true` zeigt die Zwischensumme an, während `shown = false` sie ausblendet. Da jeder Aufruf nur einen Typ betrifft, wird durch mehrmaliges Aufrufen der Methode mit unterschiedlichen `subtotalType`-Werten eine benutzerdefinierte Teilmenge von Zwischensummen erstellt.

Die Enumeration `PivotFieldSubtotalType` definiert die verfügbaren Zwischensummenarten.

- `Automatic` — Aspose.Cells wählt die Standardauswahl (in der Regel `Sum` für numerische Felder)
- `None` — unterdrückt jede Zwischensummenzeile
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
Zwischensummen werden nur gerendert, wenn zwei oder mehr Pivot-Felder im Zeilenbereich (oder im Spaltenbereich) vorhanden sind. Ein einzelnes Feld hat keine sinnvolle Grundlage für eine Zwischensumme, daher haben `SetSubtotals`-Aufrufe in diesem Fall keine sichtbare Wirkung. Dieser Artikel platziert daher in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Zwischensummengrenze zwischen jeder `Category`-Gruppe sichtbar ist.
{{% /alert %}}

## **Szenario 1 — Automatische (Standard-)Zwischensummen**

Wenn Sie `SetSubtotals` überhaupt nicht aufrufen, wendet Aspose.Cells die Auswahl `Automatic` auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten explizit, indem es `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` auf dem äußeren `Category`-Zeilenfeld aufruft.

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output_automatic.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Szenario 2 — Alle Zwischensummen unterdrücken (None)**

Der Aufruf von `SetSubtotals(PivotFieldSubtotalType.None, true)` entfernt jede Zwischensummenzeile aus der PivotTable und lässt nur die Feldzeilen und das Gesamtergebnis unten übrig. Dies ist nützlich, wenn Sie die rohen gruppierten Daten ohne zusammenfassende Zeilen wünschen.

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
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output_none.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Szenario 3 — Benutzerdefinierte Zwischensummen-Teilmenge (Sum + Average)**

Sie sind nicht auf einen einzelnen Zwischensummentyp beschränkt. Jeder `SetSubtotals`-Aufruf wirkt unabhängig auf einen Typ. Wenn Sie die Methode zweimal aufrufen — einmal mit `Sum` und einmal mit `Average` — entsteht eine benutzerdefinierte Teilmenge von zwei Zwischensummenzeilen für jede `Category`-Gruppe.

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output_custom.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Zusammenfassung**

Die drei oben beschriebenen Szenarien verwenden denselben Datensatz und dieselbe PivotTable-Struktur. Der einzige Unterschied zwischen ihnen ist der `SetSubtotals`-Aufruf, der auf das äußere `Category`-Zeilenfeld angewendet wird. Denken Sie an die Zwei-Felder-Regel: Ein einzelnes Feld in einem Bereich hat keine Grundlage für eine Zwischensumme. Platzieren Sie daher immer mindestens zwei Felder im Zeilen- oder Spaltenbereich, wenn `SetSubtotals` eine sichtbare Wirkung haben soll.

## **Verwandte Artikel**

- [Seitenfelder in Pivot-Tabellen](/cells/de/cpp/add-page-field-in-pivot-table/)
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells for C++](/cells/de/cpp/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
