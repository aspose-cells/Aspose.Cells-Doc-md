---
title: Filterfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
linktitle: Filterfelder hinzufügen
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ Filterfelder in Pivot-Tabellen hinzufügen und konfigurieren, einschließlich Hinzufügen von Filterfeldern, Einfachauswahl-Filterung und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, C++, Pivot-Tabelle, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in Pivot-Tabellen. Sie können ein Filterfeld über eine komfortable High-Level-API oder über die Low-Level-Sammlung `PageFields` hinzufügen, und Sie können den Filter im Einfachauswahlmodus steuern, ihn zurücksetzen, um alle Seitenelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, damit Benutzer über die Checkbox-Benutzeroberfläche in Excel mehrere Seitenelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**

Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Bereich anzeigt. Endbenutzer sehen es als Dropdown-Liste am oberen Rand einer in Excel gerenderten Pivot-Tabelle, und die Auswahl eines der verfügbaren Seitenelemente baut den Pivot-Bereich neu auf, sodass nur die Datensätze zusammengefasst werden, die zu diesem Seitenelement gehören. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.Page` registriert wird, anstatt als `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data`.

Ein Filterfeld kann in zwei Verhaltensweisen arbeiten. Im standardmäßigen **Einfachauswahl**-Verhalten ist jeweils nur ein Seitenelement sichtbar, sodass der Pivot-Bereich genau eine Teilmenge zusammenfasst. Im **Mehrfachauswahl**-Verhalten zeigt das Feld eine Checkbox-Liste, und der Pivot-Bereich fasst die Vereinigung aller markierten Seitenelemente zusammen. Dasselbe Quellfeld kann zwischen diesen Verhaltensweisen hin- und hergeschaltet werden, indem eine einzelne Eigenschaft umgeschaltet wird.

Aspose.Cells for C++ bietet zwei gleichwertige Möglichkeiten, ein Filterfeld zu registrieren. Die High-Level-API ist `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, die den Namen der Quellspalte akzeptiert und das Feld in einem einzigen Aufruf hinzufügt. Die Low-Level-API ist `PivotTable.PageFields.Add(PivotField)`, die verwendet wird, wenn Sie bereits eine `PivotField`-Referenz haben und dieselbe Feldinstanz dem Filterbereich hinzufügen möchten. Beide APIs füllen letztendlich dieselbe `PageFields`-Sammlung, und der Rest dieses Artikels zeigt, wie Sie zwischen ihnen wählen und wie Sie jeden Filtermodus steuern.

## **Hinzufügen eines Filterfelds**

Es gibt zwei Möglichkeiten, ein Pivot-Feld im Filterbereich zu registrieren. Der High-Level-Aufruf akzeptiert den Namen der Quellspalte als Zeichenkette und ist der häufigste Weg. Der Low-Level-Aufruf akzeptiert eine vorhandene `PivotField`-Instanz und ist praktisch, wenn dasselbe Feldobjekt in mehreren Pivot-Bereichen wiederverwendet werden muss. Beide Aufrufe platzieren das Feld in `PivotTable.PageFields`, woraufhin es als Seiten-Dropdown am oberen Rand der gerenderten Pivot-Tabelle erscheint.

### Hinzufügen eines Filterfelds mit AddFieldToArea

Das folgende Beispiel erstellt einen kleinen Fruit / Year / Amount-Datensatz, platziert eine Pivot-Tabelle in Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    // Neue Arbeitsmappe erstellen
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Daten");

    Cells cells = worksheet.GetCells();

    // Kopfzeile einrichten
    cells.Get(u"A1").PutValue(u"Frucht");
    cells.Get(u"B1").PutValue(u"Jahr");
    cells.Get(u"C1").PutValue(u"Betrag");

    // 9 Zeilen Beispieldaten befüllen: Frucht, Jahr, Betrag
    const char* fruits[] = { "Apfel", "Banane", "Apfel", "Traube", "Orange", "Banane", "Traube", "Apfel", "Orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };

    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }

    // Pivot-Tabelle an Zelle E3 verankert hinzufügen
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTabelle1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Felder zu ihren Bereichen hinzufügen: Frucht als Zeile, Betrag als Daten, Jahr als Seitenfeld
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Frucht");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Betrag");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Jahr");

    // Pivot-Tabellendaten aktualisieren und berechnen
    pivotTable.CalculateData();

    // Arbeitsmappe speichern
    workbook.Save(u"seitenfeldBeispiel.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Hinzufügen eines Filterfelds mit PageFields.Add

Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.PageFields.Add` übergeben. Die Pivot-Tabelle und das Filterfeld werden genau wie im vorherigen Szenario erstellt; nur die abschließende Registrierung im Filterbereich wird durch den Low-Level-API-Aufruf ersetzt.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Kopfzeilen
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Beispieldaten (9 Zeilen)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);

    // Pivot-Tabelle bei E3 hinzufügen, die A1:C10 abdeckt
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Frucht -> Zeile, Betrag -> Daten
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // Low-Level-Ansatz: das vorhandene Year-PivotField in BaseFields suchen
    // und es im Seitenbereich über PageFields.Add(PivotField) registrieren.
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe übernommen wird
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Einfachauswahl-Filterung (Anzeigen eines Seitenelements)**

Im standardmäßigen Einfachauswahl-Verhalten wird das Filterfeld als einzelnes Dropdown gerendert, und die Ganzzahl `PivotField.CurrentPageItem` wählt aus, welches Seitenelement den Pivot-Bereich steuert. Das Zuweisen eines bestimmten Indexes wählt dieses eine Element aus; das Zuweisen des speziellen Sentinelwerts `0x7FFD` (dezimal 32765) hebt den Filter auf, sodass alle Seitenelemente gleichzeitig zusammengefasst werden. Die Einfachauswahl ist die Standardeinstellung; Sie müssen sie nicht explizit aktivieren.

### Alle Elemente anzeigen

Das Setzen von `CurrentPageItem` auf den magischen Wert `0x7FFD` entspricht dem Aufheben des Filters: Der Pivot-Bereich fasst alle Seitenelemente zusammen, als ob kein Filter angewendet wäre.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};

    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    pivotTable.CalculateData();

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Ein bestimmtes Element anzeigen

Das Setzen von `CurrentPageItem` auf einen realen Index wählt genau dieses eine Seitenelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));

    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));

    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));

    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);

    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Mehrfachauswahl-Filterung**

Die Mehrfachauswahl-Filterung wandelt das Seiten-Dropdown in eine Checkbox-Liste um und ermöglicht es dem Endbenutzer, mehrere Seitenelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei zusammenarbeitende Eigenschaften bereit. `PivotField.IsMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.IsHidden`, welche Elemente in der Checkbox-Liste angezeigt werden, sodass Sie entweder alle Elemente anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

Der folgende Code aktiviert die Mehrfachauswahl für dasselbe Year-Filterfeld, das in Szenario 1a erstellt wurde, und zeigt dann zwei Muster: Teil A zeigt jedes Seitenelement an, indem `IsHidden` für jeden Eintrag auf `false` belassen wird, während Teil B nur die von Ihnen gewählten Quellwerte auf eine Whitelist setzt und alles andere über einen `switch (pivotItems[i].GetStringValue())`-Block ausblendet.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Beispieldaten: Frucht | Jahr | Betrag
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");

    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };

    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }

    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // — Mehrfachauswahl im Seitenfeld aktivieren
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);

    // Teil A — ALLE Elemente auswählen (alle Elemente sichtbar machen)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }

    // Teil B — nur bestimmte Elemente nach Quellwert auswählen
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }

    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.IsHidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`IsHidden == false`). Wenn jedes Element ausgeblendet ist, stürzt Excel entweder beim Öffnen der Datei ab oder rendert eine leere Pivot-Tabelle. Stellen Sie immer sicher, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollten verwendet werden?**

Die folgende Tabelle fasst zusammen, wann welche API und welcher Modus verwendet werden sollten, damit Sie die richtige Kombination auswählen können, ohne jedes Szenario im Detail lesen zu müssen.

| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Hinzufügen eines Filterfelds nach Quellspaltenname (am häufigsten) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | High-Level, einzeilig. Verwenden Sie dies, sofern Sie keine `PivotField`-Referenz benötigen. |
| Hinzufügen eines Filterfelds, wenn Sie bereits ein `PivotField`-Objekt haben | `PivotTable.PageFields.Add(PivotField)` | n/a | Verwenden Sie dies, wenn das Feldobjekt anderswo bezogen wurde oder wiederverwendet werden muss. |
| Auf ein einzelnes Seitenelement filtern (Standardmodus) | `PivotField.CurrentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste an. |
| Alle Elemente anzeigen / Filter aufheben | `PivotField.CurrentPageItem` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (dezimal 32765) ist der Sentinelwert für „alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.IsMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor `IsHidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste aus-/einblenden | `PivotItem.IsHidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`IsHidden == false`). |

{{% alert color="primary" %}}
Beachten Sie immer die Sichtbarkeitsbedingung bei der Konfiguration der Mehrfachauswahl-Filterung. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder rendert eine leere Pivot-Tabelle. Erstellen Sie Ihre Whitelist auf Grundlage Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Computer zuverlässig geöffnet.
{{% /alert %}}



{{< app/cells/assistant language="cpp" >}}
