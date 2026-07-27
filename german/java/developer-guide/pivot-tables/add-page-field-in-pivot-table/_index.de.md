---
title: Filterfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
linktitle: Filterfelder hinzufügen
description: Lernen Sie, wie Sie Filterfelder in Pivot-Tabellen mit Aspose.Cells for Java hinzufügen und konfigurieren, einschließlich des Hinzufügens von Filterfeldern, der Einfachauswahl-Filterung und der Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, Java, Pivot-Tabelle, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/java/add-filter-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in Pivot-Tabellen. Sie können ein Filterfeld über eine komfortable High-Level-API oder über die Low-Level-Sammlung `PageFields` hinzufügen, den Filter im Einfachauswahlmodus steuern, ihn löschen, um jedes Seitenelement anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, damit Benutzer über die Kontrollkästchen-Benutzeroberfläche in Excel mehrere Seitenelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**

Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten im Pivot-Körper angezeigt wird. Endbenutzer sehen es als Dropdown am oberen Rand einer gerenderten Pivot-Tabelle in Excel, und durch Auswahl eines der verfügbaren Seitenelemente wird der Pivot-Körper neu aufgebaut, sodass nur die zu diesem Seitenelement gehörenden Datensätze zusammengefasst werden. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.Page` registriert wird, anstatt als `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data`.

Ein Filterfeld kann in zwei Verhaltensweisen arbeiten. Im standardmäßigen **Einfachauswahl**-Verhalten ist jeweils nur ein Seitenelement sichtbar, sodass der Pivot-Körper genau eine Teilmenge zusammenfasst. Im **Mehrfachauswahl**-Verhalten stellt das Feld eine Kontrollkästchenliste bereit, und der Pivot-Körper fasst die Vereinigung aller markierten Seitenelemente zusammen. Dasselbe Quellfeld kann durch Umschalten einer einzelnen Eigenschaft zwischen diesen Verhaltensweisen hin- und herwechseln.

Aspose.Cells for Java stellt zwei gleichwertige Möglichkeiten bereit, ein Filterfeld zu registrieren. Die High-Level-API ist `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")`, die den Namen der Quellspalte annimmt und das Feld in einem einzigen Aufruf hinzufügt. Die Low-Level-API ist `PivotTable.PageFields.add(PivotField)`, die verwendet wird, wenn Sie bereits eine `PivotField`-Referenz besitzen und dieselbe Feldinstanz dem Filterbereich hinzufügen möchten. Beide APIs füllen letztendlich dieselbe `PageFields`-Sammlung, und der Rest dieses Artikels zeigt, wie Sie zwischen ihnen wählen und wie Sie jeden Filtermodus steuern.

## **Hinzufügen eines Filterfelds**

Es gibt zwei Möglichkeiten, ein Pivot-Feld im Filterbereich zu registrieren. Der High-Level-Aufruf nimmt den Namen der Quellspalte als Zeichenkette und ist der häufigste Weg. Der Low-Level-Aufruf akzeptiert eine vorhandene `PivotField`-Instanz und ist praktisch, wenn dasselbe Feldobjekt in mehreren Pivot-Bereichen wiederverwendet werden muss. Beide Aufrufe platzieren das Feld in `PivotTable.PageFields`, woraufhin es als Seiten-Dropdown am oberen Rand der gerenderten Pivot-Tabelle erscheint.

### Hinzufügen eines Filterfelds mit addFieldToArea

Das folgende Beispiel erstellt einen kleinen Datensatz mit Fruit / Year / Amount, platziert eine Pivot-Tabelle an Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

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

// Füllen Sie 9 Zeilen mit Beispieldaten: Frucht, Jahr, Menge
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

// Fügen Sie Felder zu ihren Bereichen hinzu: Frucht als Zeile, Menge als Daten, Jahr als Seitenfeld
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// Aktualisieren und berechnen Sie die Pivot-Tabellen-Daten
pivotTable.calculateData();

// Speichern Sie die Arbeitsmappe
workbook.save("pageFieldSample.xlsx");
```

### Hinzufügen eines Filterfelds mit PageFields.add

Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.PageFields.add` übergeben. Die Pivot-Tabelle und das Filterfeld werden genau wie im vorherigen Szenario erstellt; nur die endgültige Registrierung des Filterbereichs wird durch den Low-Level-API-Aufruf ersetzt.

```java
import com.aspose.cells.*;

// - Die Pivot-Tabelle und das Seitenfeld werden genau wie in
//   Szenario 1a konstruiert (Fruit/Year/Amount-Daten, Pivot bei E3, Fruit->Zeile,
//   Amount->Daten). Unten holen wir das Year-PivotField aus der
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

// Fruit -> Zeile, Amount -> Daten (Year wird unten zu Seite)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Low-Level-Ansatz: das vorhandene Year-PivotField aus BaseFields holen
// und im Seitenbereich über PageFields.Add(PivotField) registrieren.
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe widergespiegelt wird
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Einfachauswahl-Filterung (Anzeigen eines einzelnen Seitenelements)**

Im standardmäßigen Einfachauswahlverhalten wird das Filterfeld als einzelnes Dropdown gerendert, und die Ganzzahl `PivotField.CurrentPageItem` wählt aus, welches Seitenelement den Pivot-Körper steuert. Durch Zuweisen eines bestimmten Index wird dieses eine Element ausgewählt; durch Zuweisen des speziellen Sentinels `0x7FFD` (Dezimal 32765) wird der Filter gelöscht, sodass jedes Seitenelement sofort zusammengefasst wird. Einfachauswahl ist der Standard; Sie müssen sie nicht explizit aktivieren.

### Anzeigen aller Elemente

Das Setzen von `CurrentPageItem` auf den magischen Wert `0x7FFD` entspricht dem Löschen des Filters: Der Pivot-Körper fasst jedes Seitenelement zusammen, als wäre kein Filter angewendet worden.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// Fruit/Jahr/Betrag Daten befüllen
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

// Pivot-Felder konfigurieren: Fruit in Zeile, Amount in Daten, Year in Seite
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");

pivot.calculateData();

// Den Seitenfilter zurücksetzen, damit jedes Element im Seitenfeld sichtbar ist.
// 0x7FFD (Dezimal 32765) ist der spezielle Sentinel-Wert, der "alle Elemente" bedeutet,
// entspricht der Auswahl von "(Alle)" im Excel-Seitenfeld-Dropdown.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);

workbook.save("output.xlsx");
```

### Anzeigen eines bestimmten Elements

Durch Setzen von `CurrentPageItem` auf einen realen Index wird genau dieses eine Seitenelement ausgewählt. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```java
import com.aspose.cells.*;

// Arbeitsmappe erstellen
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Beispieldaten hinzufügen (Frucht/Jahr/Betrag)
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

// Felder hinzufügen: Frucht→Zeile, Betrag→Daten, Jahr→Seite
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

Die Mehrfachauswahl-Filterung verwandelt das Seiten-Dropdown in eine Kontrollkästchenliste und ermöglicht es dem Endbenutzer, mehrere Seitenelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.IsMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.IsHidden`, welche Elemente in der Kontrollkästchenliste erscheinen, sodass Sie entweder jedes Element anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

Der folgende Code aktiviert die Mehrfachauswahl für dasselbe Year-Filterfeld, das in Szenario 1a erstellt wurde, und zeigt dann zwei Muster: Teil A zeigt jedes Seitenelement, indem `IsHidden` für jeden Eintrag auf `false` belassen wird, während Teil B nur die von Ihnen ausgewählten Quellwerte auf die Whitelist setzt und alles andere über einen `switch (pivotItems[i].getStringValue())`-Block ausblendet.

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

// Teil A -- alle Elemente auswählen (alle Elemente sichtbar machen)
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

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.IsHidden` **muss mindestens ein `PivotItem` sichtbar bleiben** (`IsHidden == false`). Wenn jedes Element ausgeblendet ist, stürzt Excel entweder beim Öffnen der Datei ab oder rendert eine leere Pivot-Tabelle. Stellen Sie immer sicher, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollten verwendet werden?**

Die folgende Tabelle fasst zusammen, wann jede API und jeder Modus verwendet werden sollte, damit Sie die richtige Kombination wählen können, ohne jedes Szenario im Detail lesen zu müssen.

| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Hinzufügen eines Filterfelds nach Quellspaltenname (am häufigsten) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/v | High-Level, einzeilig. Verwenden Sie dies, sofern Sie keine `PivotField`-Referenz benötigen. |
| Hinzufügen eines Filterfelds, wenn Sie bereits ein `PivotField`-Objekt besitzen | `PivotTable.PageFields.add(PivotField)` | n/v | Verwenden Sie dies, wenn das Feldobjekt an anderer Stelle erhalten wurde oder wiederverwendet werden muss. |
| Filtern auf ein einzelnes Seitenelement (Standardmodus) | `PivotField.CurrentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste. |
| Alle Elemente anzeigen / Filter löschen | `PivotField.CurrentPageItem` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (Dezimal 32765) ist das Sentinel für "alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.IsMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor `IsHidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste ausblenden / einblenden | `PivotItem.IsHidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`IsHidden == false`). |

{{% alert color="primary" %}}
Denken Sie immer an die Sichtbarkeitsbeschränkung, wenn Sie die Mehrfachauswahl-Filterung konfigurieren. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder rendert eine leere Pivot-Tabelle. Erstellen Sie Ihre Whitelist anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Computer zuverlässig geöffnet.
{{% /alert %}}



{{< app/cells/assistant language="java" >}}
