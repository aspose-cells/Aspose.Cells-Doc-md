---
title: Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for Java hinzufügen
description: Erfahren Sie, wie Sie Filterfelder in Pivot-Tabellen mit Aspose.Cells for Java hinzufügen und konfigurieren, einschließlich des Hinzufügens von Filterfeldern, Einfachauswahl-Filterung und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, Java, Pivot-Tabelle, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Filterfelder hinzufügen
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in Pivot-Tabellen. Sie können ein Filterfeld über eine komfortable High-Level-API oder über die Low-Level-Sammlung `PageFields` hinzufügen, und Sie können den Filter im Einfachauswahlmodus steuern, ihn zurücksetzen, um alle Filterelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, sodass Benutzer über die Checkbox-Benutzeroberfläche in Excel mehrere Filterelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**
Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Bereich anzeigt. Endbenutzer sehen es als Dropdown am oberen Rand einer gerenderten Pivot-Tabelle in Excel, und die Auswahl eines der verfügbaren Filterelemente baut den Pivot-Bereich neu auf, sodass nur die Datensätze zusammengefasst werden, die zu diesem Filterelement gehören. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.Page` registriert wird, anstelle von `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data`.

## **Hinzufügen eines Filterfelds**

### Hinzufügen eines Filterfelds mit addFieldToArea
Das folgende Beispiel erstellt einen kleinen Datensatz mit Frucht / Jahr / Betrag, platziert eine Pivot-Tabelle in Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```java
import com.aspose.cells.*;
// Erstellen Sie eine neue Arbeitsmappe
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Richten Sie die Kopfzeile ein
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Füllen Sie 9 Zeilen mit Beispieldaten: Frucht, Jahr, Betrag
Object[][] data = new Object[][]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}
// Fügen Sie eine Pivot-Tabelle hinzu, die an Zelle E3 verankert ist
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Fügen Sie Felder zu ihren Bereichen hinzu: Frucht als Zeile, Betrag als Daten, Jahr als Seitenfeld
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Aktualisieren und berechnen Sie die Pivot-Tabellen-Daten
pivotTable.calculateData();
// Speichern Sie die Arbeitsmappe
workbook.save("pageFieldSample.xlsx");
```

### Hinzufügen eines Filterfelds mit PageFields.add
Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.PageFields.add` übergeben. Die Pivot-Tabelle und das Filterfeld werden genau wie im vorherigen Szenario erstellt; nur die endgültige Registrierung im Filterbereich wird durch den Low-Level-API-Aufruf ersetzt.

```java
import com.aspose.cells.*;
// - Die Pivot-Tabelle und das Seitenfeld werden genau wie in
//   Szenario 1a (Fruit/Year/Amount-Daten, Pivot bei E3, Fruit->Zeile,
//   Amount->Daten) erstellt. Unten holen wir das Year PivotField aus der
//   BaseFields-Sammlung und übergeben es an PageFields.Add - die
//   Low-Level-Alternative zu AddFieldToArea. Das Ergebnis ist
//   funktional identisch mit Szenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Kopfzeilen
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Beispieldaten (9 Zeilen)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Pivot-Tabelle bei E3 hinzufügen, die A1:C10 abdeckt
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Fruit -> Zeile, Amount -> Daten (Year wird unten zur Seite hinzugefügt)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Low-Level-Ansatz: das vorhandene Year PivotField aus BaseFields holen
// und über PageFields.Add(PivotField) im Seitenbereich registrieren.
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe widergespiegelt wird
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Einfachauswahl-Filterung (Anzeigen eines Filterelements)**
Im standardmäßigen Einfachauswahlverhalten wird das Filterfeld als einzelnes Dropdown angezeigt, und die Ganzzahl `PivotField.CurrentPageItem` wählt aus, welches Filterelement den Pivot-Bereich steuert. Durch Zuweisen eines bestimmten Index wird dieses eine Element ausgewählt; durch Zuweisen des speziellen Sentinel-Werts `0x7FFD` (dezimal 32765) wird der Filter zurückgesetzt, sodass alle Filterelemente gleichzeitig zusammengefasst werden. Die Einfachauswahl ist die Standardeinstellung; Sie müssen sie nicht explizit aktivieren.

### Anzeigen aller Elemente
Das Setzen von `CurrentPageItem` auf den magischen Wert `0x7FFD` entspricht dem Zurücksetzen des Filters: Der Pivot-Bereich fasst alle Filterelemente zusammen, als ob kein Filter angewendet wäre.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Frucht/Jahr/Betrag-Daten einfügen
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
// Pivot-Tabelle bei E3 erstellen
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);
// Pivot-Felder konfigurieren: Frucht in Zeile, Betrag in Daten, Jahr in Seite
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Den Seitenfilter löschen, damit jedes Element im Seitenfeld sichtbar ist.
// 0x7FFD (dezimal 32765) ist der spezielle Sentinel-Wert, der "alle Elemente" bedeutet,
// entspricht der Auswahl von "(Alle)" im Dropdown-Menü des Seitenfelds in Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Anzeigen eines bestimmten Elements
Das Setzen von `CurrentPageItem` auf einen realen Index wählt nur dieses eine Filterelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds, sodass zum Beispiel `1` das zweite Element nach dem Sortieren auswählt.

```java
import com.aspose.cells.*;
// Arbeitsmappe erstellen
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Beispieldaten hinzufügen (Obst/Jahr/Betrag)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");
cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");
cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");
cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");
// Pivot-Tabelle bei E3 hinzufügen
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// Felder hinzufügen: Obst→Zeile, Betrag→Daten, Jahr→Seite
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Seitenfeld-spezifische Operationen
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = zweites Element in sortierter Reihenfolge (z. B. "2021")
// Pivot-Tabelle aktualisieren und berechnen
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Mehrfachauswahl-Filterung**
Die Mehrfachauswahl-Filterung verwandelt das Filter-Dropdown in eine Checkbox-Liste und ermöglicht es dem Endbenutzer, mehrere Filterelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.IsMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.IsHidden`, welche Elemente in der Checkbox-Liste angezeigt werden, sodass Sie entweder alle Elemente anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Beispieldaten: Frucht | Jahr | Menge
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");
String[][] data = new String[][]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}
Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Mehrfachauswahl auf dem Seitenfeld aktivieren
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Teil A -- ALLE Elemente auswählen (alle Elemente sichtbar machen)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Teil B -- nur bestimmte Elemente nach Quellwert auswählen
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.IsHidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`IsHidden == false`). Wenn jedes Element ausgeblendet ist, stürzt Excel entweder beim Öffnen der Datei ab oder rendert eine leere Pivot-Tabelle. Stellen Sie immer sicher, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollten verwendet werden?**
Die folgende Tabelle fasst zusammen, wann welche API und welcher Modus verwendet werden sollte, damit Sie die richtige Kombination auswählen können, ohne jedes Szenario im Detail lesen zu müssen.
| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Filterfeld nach Quellspaltenname hinzufügen (am häufigsten) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | High-Level, einzeilig. Verwenden Sie dies, sofern Sie keine `PivotField`-Referenz benötigen. |
| Filterfeld hinzufügen, wenn Sie bereits ein `PivotField`-Objekt haben | `PivotTable.PageFields.add(PivotField)` | n/a | Verwenden Sie dies, wenn das Feldobjekt anderswo bezogen wurde oder wiederverwendet werden soll. |
| Auf ein einzelnes Filterelement filtern (Standardmodus) | `PivotField.CurrentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste an. |
| Alle Elemente anzeigen / Filter zurücksetzen | `PivotField.CurrentPageItem` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (dezimal 32765) ist der Sentinel für „alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.IsMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor `IsHidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste ausblenden/anzeigen | `PivotItem.IsHidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`IsHidden == false`). |

{{% alert color="primary" %}}
Denken Sie immer an die Sichtbarkeitseinschränkung, wenn Sie die Mehrfachauswahl-Filterung konfigurieren. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder rendert eine leere Pivot-Tabelle. Erstellen Sie Ihre Whitelist anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Computer zuverlässig geöffnet.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}