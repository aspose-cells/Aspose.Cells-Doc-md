---
title: Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for C++ hinzufügen
linktitle: Filterfelder zu einer Pivot-Tabelle
description: Erfahren Sie, wie Sie Filterfelder in Pivot-Tabellen mit Aspose.Cells for C++ hinzufügen und konfigurieren, einschließlich des Hinzufügens von Filterfeldern, Einzel- und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, C++, Pivot-Tabelle, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in Pivot-Tabellen. Sie können ein Filterfeld über eine übergeordnete Komfort-API oder über die niedrigstufige `PageFields`-Sammlung hinzufügen. Sie können den Filter im Einzelauswahl-Modus steuern, ihn zurücksetzen, um alle Filterelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, damit Benutzer über die Kontrollkästchen-Benutzeroberfläche in Excel mehrere Filterelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**
Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten im Pivot-Körper angezeigt wird. Endbenutzer sehen es als Dropdown am oberen Rand einer in Excel gerenderten Pivot-Tabelle. Durch Auswahl eines der verfügbaren Filterelemente wird der Pivot-Körper neu aufgebaut, sodass nur die zu diesem Filterelement gehörenden Datensätze zusammengefasst werden. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.Page` registriert wird, anstatt als `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data`.

## **Filterfeld hinzufügen**

### Filterfeld mit AddFieldToArea hinzufügen
Das folgende Beispiel erstellt einen kleinen Datensatz mit den Spalten Fruit, Year und Amount, platziert eine Pivot-Tabelle in Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Eine neue Arbeitsmappe erstellen
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    Cells cells = worksheet.GetCells();
    // Die Kopfzeile einrichten
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    // 9 Zeilen mit Beispieldaten füllen: Obst, Jahr, Betrag
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };
    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Eine Pivot-Tabelle hinzufügen, die an Zelle E3 verankert ist
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Felder zu ihren Bereichen hinzufügen: Obst als Zeile, Betrag als Daten, Jahr als Seitenfeld
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    // Die Daten der Pivot-Tabelle aktualisieren und berechnen
    pivotTable.CalculateData();
    // Die Arbeitsmappe speichern
    workbook.Save(u"pageFieldSample.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### Filterfeld mit PageFields.Add hinzufügen
Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.PageFields.Add` übergeben. Die Pivot-Tabelle und das Filterfeld werden genau wie im vorherigen Szenario erstellt; nur die abschließende Filterbereichsregistrierung wird durch den niedrigstufigen API-Aufruf ersetzt.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // Überschriften
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
    // und es über PageFields.Add(PivotField) im Seitenbereich registrieren.
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }
    // Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe widergespiegelt wird
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Einzelauswahl-Filterung (Anzeige eines Filterelements)**
Im Standardverhalten der Einzelauswahl wird das Filterfeld als einzelnes Dropdown dargestellt, und der `PivotField.CurrentPageItem`-Integer wählt aus, welches Filterelement den Pivot-Körper steuert. Durch Zuweisen eines bestimmten Index wird dieses eine Element ausgewählt; durch Zuweisen des speziellen Sentinel-Werts `0x7FFD` (Dezimal 32765) wird der Filter zurückgesetzt, sodass alle Filterelemente gleichzeitig zusammengefasst werden. Die Einzelauswahl ist der Standard; Sie müssen sie nicht explizit aktivieren.

### Alle Elemente anzeigen
Das Setzen von `CurrentPageItem` auf den magischen Wert `0x7FFD` entspricht dem Zurücksetzen des Filters: Der Pivot-Körper fasst jedes Filterelement zusammen, als ob kein Filter angewendet worden wäre.

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
Das Setzen von `CurrentPageItem` auf einen echten Index wählt genau dieses eine Filterelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds. Beispielsweise wählt `1` das zweite Element nach der Sortierung aus.

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
Die Mehrfachauswahl-Filterung verwandelt das Filter-Dropdown in eine Kontrollkästchenliste und ermöglicht es dem Endbenutzer, mehrere Filterelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei zusammenarbeitende Eigenschaften bereit. `PivotField.IsMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.IsHidden`, welche Elemente in der Kontrollkästchenliste angezeigt werden, sodass Sie entweder jedes Element anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

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
    // Teil A — ALLE Elemente auswählen (jedes Element sichtbar machen)
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

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.IsHidden` **muss mindestens ein `PivotItem` sichtbar bleiben** (`IsHidden == false`). Wenn jedes Element ausgeblendet ist, stürzt Excel entweder beim Öffnen der Datei ab oder zeigt eine leere Pivot-Tabelle an. Stellen Sie stets sicher, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welchen Modus sollte ich verwenden?**
Die folgende Tabelle fasst zusammen, wann Sie welche API und welchen Modus verwenden sollten, damit Sie die richtige Kombination auswählen können, ohne jedes Szenario im Detail zu lesen.
| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Filterfeld nach Quellspaltenname hinzufügen (am häufigsten) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Übergeordnet, einzeilig. Verwenden Sie dies, sofern Sie keine `PivotField`-Referenz benötigen. |
| Filterfeld hinzufügen, wenn Sie bereits ein `PivotField`-Objekt haben | `PivotTable.PageFields.Add(PivotField)` | n/a | Verwenden Sie dies, wenn das Feldobjekt anderweitig erhalten wurde oder wiederverwendet werden muss. |
| Auf ein einzelnes Filterelement filtern (Standardmodus) | `PivotField.CurrentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste an. |
| Alle Elemente anzeigen / Filter zurücksetzen | `PivotField.CurrentPageItem` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (Dezimal 32765) ist der Sentinel-Wert für "alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.IsMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor `IsHidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahl-Liste ausblenden / anzeigen | `PivotItem.IsHidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`IsHidden == false`). |

{{% alert color="primary" %}}
Denken Sie stets an die Sichtbarkeitseinschränkung, wenn Sie die Mehrfachauswahl-Filterung konfigurieren. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder zeigt eine leere Pivot-Tabelle an. Erstellen Sie Ihre Whitelist anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Rechner zuverlässig geöffnet.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}