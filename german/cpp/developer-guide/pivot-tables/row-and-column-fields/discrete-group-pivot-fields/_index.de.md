---
title: Diskrete Gruppierung von Pivot-Feldelementen
linktitle: Diskrete Gruppierung
description: Erfahren Sie, wie Sie mithilfe von DiscreteGroupItem und PivotFieldGroupOptions.DiscreteGroupItems Pivot-Feldelemente in Aspose.Cells for C++ zu benutzerdefinierten Gruppen mit Namen wie Obst und Gemüse gruppieren.
keywords: Aspose.Cells for C++, PivotTable, diskrete Gruppierung, DiscreteGroupItem, PivotFieldGroupOptions, Pivot-Elemente gruppieren, benutzerdefinierte Gruppen, PivotField.Group, C++, Excel-PivotTable
type: docs
weight: 90
url: /de/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
- Bei der automatischen Gruppierung werden Elemente nach Datentyp zusammengefasst, etwa Datumsangaben nach Monaten und Quartalen oder Zahlen nach Bereichen. Die diskrete Gruppierung löst das entgegengesetzte Problem: Sie fasst bestimmte, thematisch unverbundene Elemente in benutzerdefinierten Gruppen mit Namen zusammen, beispielsweise Produkte in Obst und Gemüse, Filialen in Regionen oder Konten in Zonen. Aspose.Cells bietet die diskrete Gruppierung über die Klasse `DiscreteGroupItem` und die Eigenschaft `PivotFieldGroupOptions.DiscreteGroupItems`.
- Ein `DiscreteGroupItem` besteht aus einem Gruppennamen und den Elementen, die ihm angehören. Die Elemente können auf zwei Arten identifiziert werden: über ihre Namen (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) oder über ihre nullbasierten Positionen in den Quelldaten (`DiscreteGroupItem("fruit", { 0, 3 })`). Beide Varianten führen zum selben Ergebnis.
- Die diskrete Gruppierung wird auf ein Feld im Zeilen- oder Spaltenbereich einer PivotTable angewendet, indem die Optionen an `PivotField.Group(PivotFieldGroupOptions)` übergeben werden.

## **Pivot-Feldelemente nach Elementnamen gruppieren**
Das folgende Beispiel erstellt eine kleine Verkaufsliste (Produkt, Datum und Betrag) und erzeugt daraus eine PivotTable. Dabei werden `product` im Zeilenbereich, `date` im Spaltenbereich und `amount` im Datenbereich platziert. Anschließend werden zwei benutzerdefinierte Gruppen nach Elementnamen definiert: Obst (`grape`, `cherry`) und Gemüse (`carrot`, `potato`). Das Ergebnis zeigt einen zweistufigen Zeilenaufbau: Der Gruppenname bildet die äußere Ebene, und die ursprünglichen Elemente sind darunter verschachtelt. So lassen sich Trends je benutzerdefinierter Gruppe und Element ablesen.

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

Nach `CalculateData()` zeigt der Zeilenbereich der PivotTable die Gruppen `fruit` (`grape` 50, `cherry` 80) und `vegetable` (`carrot` 60, `potato` 70) mit der Gesamtsumme 260. Die Spaltenbeschriftungen zeigen weiterhin die vier Datumsangaben (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Pivot-Feldelemente nach Elementindizes gruppieren**
Wenn Elementnamen lang oder lokalisiert sind, identifiziert der zweite Konstruktor von `DiscreteGroupItem` die Elemente anhand ihres Index. Die Indizes entsprechen den nullbasierten Positionen der Elemente in der Reihenfolge, in der sie in den Quelldaten erscheinen, und nicht ihrer alphabetischen Reihenfolge. In den obigen Beispieldaten ist `grape` Element 0, `carrot` Element 1, `potato` Element 2 und `cherry` Element 3. Daher umfasst `fruit` die Indizes `{ 0, 3 }` und `vegetable` die Indizes `{ 1, 2 }`. Das Ergebnis ist mit dem namensbasierten Beispiel identisch.

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

## **Hinweis**

{{% alert color="primary" %}}
- Elemente, die keiner benutzerdefinierten Gruppe zugewiesen sind, gehen nicht verloren. Sie bleiben in der PivotTable auf derselben Ebene wie die benutzerdefinierten Gruppen und bilden jeweils einen eigenen Eintrag mit nur einem Element. Wenn im obigen Beispiel nur die Gruppe `fruit` definiert wird, verbleiben `carrot` und `potato` im Zeilenbereich als eigenständige Einträge neben der Gruppe `fruit`.
- Die Eigenschaft `PivotFieldGroupOptions.NewPivotField` steuert das Layout der diskreten Gruppierung. Der Standardwert ist `true`. Dadurch wird das gruppierte Feld als neues äußeres Feld neben dem Originalfeld hinzugefügt, wodurch das oben gezeigte zweistufige Layout entsteht (`RowFields` wächst auf 2). Setzen Sie den Wert auf `false`, wird das Originalfeld durch das gruppierte Feld ersetzt. Der Zeilenbereich zeigt dann eine einzige Ebene mit den Gruppennamen und ihren aggregierten Werten: `fruit` 130 (50 + 80) und `vegetable` 130 (60 + 70).
- Die namens- und indexbasierten Konstruktoren von `DiscreteGroupItem` können innerhalb derselben `DiscreteGroupItems`-Sammlung kombiniert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in einer PivotTable gruppieren](/cells/de/cpp/group-pivot-fields-in-the-pivot-table/)
- [Zeilen- und Spaltenfelder zu einer PivotTable hinzufügen](/cells/de/cpp/pivot-table-add-row-and-column-fields/)
- [PivotTables nach Bezeichnung oder Wert filtern](/cells/de/cpp/filter-by-label-or-value-of-pivot-table/)
- [Stil auf eine PivotTable anwenden](/cells/de/cpp/apply-style-to-pivot-table/)
- [PivotTable aktualisieren](/cells/de/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}