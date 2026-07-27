---
title: Filterfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
linktitle: Filterfelder hinzufügen
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via Java Filterfelder in Pivot-Tabellen hinzufügen und konfigurieren, einschließlich des Hinzufügens von Filterfeldern, Einzel- und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, Node.js via Java, Pivot-Tabelle, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/nodejs-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in Pivot-Tabellen. Sie können ein Filterfeld über eine High-Level-Komfort-API oder über die Low-Level-Sammlung `PageFields` hinzufügen. Sie können den Filter im Einzel-Auswahl-Modus steuern, ihn löschen, um alle Seitenelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, sodass Benutzer über die Kontrollkästchen-Benutzeroberfläche in Excel mehrere Seitenelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**

Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Bereich anzeigt. Endbenutzer sehen es als Dropdown am oberen Rand einer gerenderten Pivot-Tabelle in Excel. Durch die Auswahl eines der verfügbaren Seitenelemente wird der Pivot-Bereich neu aufgebaut, sodass nur die Datensätze zusammengefasst werden, die zu diesem Seitenelement gehören. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.Page` registriert wird, anstatt als `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data`.

Ein Filterfeld kann in zwei Verhaltensweisen arbeiten. Im Standardverhalten **Einzel-Auswahl** ist jeweils nur ein Seitenelement sichtbar, sodass der Pivot-Bereich genau eine Teilmenge zusammenfasst. Im Verhalten **Mehrfachauswahl** zeigt das Feld eine Kontrollkästchenliste, und der Pivot-Bereich fasst die Vereinigung aller markierten Seitenelemente zusammen. Dasselbe Quellfeld kann zwischen diesen Verhaltensweisen hin- und hergeschaltet werden, indem eine einzelne Eigenschaft umgeschaltet wird.

Aspose.Cells for Node.js via Java bietet zwei gleichwertige Möglichkeiten, ein Filterfeld zu registrieren. Die High-Level-API ist `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, die den Namen der Quellspalte annimmt und das Feld in einem einzigen Aufruf hinzufügt. Die Low-Level-API ist `pivotTable.getPageFields().add(PivotField)`, die verwendet wird, wenn Sie bereits eine `PivotField`-Referenz haben und dieselbe Feldinstanz dem Filterbereich hinzufügen möchten. Beide APIs füllen am Ende dieselbe `PageFields`-Sammlung, und der Rest dieses Artikels zeigt, wie Sie zwischen diesen wählen und wie Sie jeden Filtermodus steuern.

## **Hinzufügen eines Filterfelds**

Es gibt zwei Möglichkeiten, ein Pivot-Feld im Filterbereich zu registrieren. Der High-Level-Aufruf nimmt den Namen der Quellspalte als Zeichenfolge und ist der häufigste Weg. Der Low-Level-Aufruf akzeptiert eine vorhandene `PivotField`-Instanz und ist praktisch, wenn dasselbe Feldobjekt in mehreren Pivot-Bereichen wiederverwendet werden muss. Beide Aufrufe platzieren das Feld in `pivotTable.getPageFields()`, woraufhin es als Seiten-Dropdown am oberen Rand der gerenderten Pivot-Tabelle angezeigt wird.

### Hinzufügen eines Filterfelds mit addFieldToArea

Das folgende Beispiel erstellt einen kleinen Datensatz mit Fruit, Year und Amount, platziert eine Pivot-Tabelle an Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Kopfzeile einrichten
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 Zeilen mit Beispieldaten befüllen: Frucht, Jahr, Menge
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// Pivot-Tabelle hinzufügen, verankert an Zelle E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Felder ihren Bereichen hinzufügen: Frucht als Zeile, Menge als Daten, Jahr als Seitenfeld
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Pivot-Tabellen-Daten aktualisieren und berechnen
pivotTable.calculateData();

// Arbeitsmappe speichern
workbook.save("pageFieldSample.xlsx");
```

### Hinzufügen eines Filterfelds mit getPageFields().add

Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `pivotTable.getPageFields().add` übergeben. Die Pivot-Tabelle und das Filterfeld werden genau wie im vorherigen Szenario erstellt; nur die endgültige Registrierung im Filterbereich wird durch den Low-Level-API-Aufruf ersetzt.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

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
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Zeile, Amount -> Daten (Year wird unten zur Seite hinzugefügt)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Low-Level-Ansatz: das vorhandene Year-PivotField aus BaseFields holen
// und über PageFields.Add(PivotField) im Seitenbereich registrieren
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe widergespiegelt wird
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Einzel-Auswahl-Filterung (Anzeigen eines Seitenelements)**

Im Standardverhalten der Einzel-Auswahl wird das Filterfeld als einzelnes Dropdown gerendert, und der Integer `PivotField.CurrentPageItem` wählt aus, welches Seitenelement den Pivot-Bereich steuert. Durch Zuweisen eines bestimmten Index wird dieses eine Element ausgewählt; durch Zuweisen des speziellen Sentinel-Werts `0x7FFD` (dezimal 32765) wird der Filter gelöscht, sodass alle Seitenelemente gleichzeitig zusammengefasst werden. Einzel-Auswahl ist die Standardeinstellung; Sie müssen sie nicht explizit aktivieren.

### Anzeigen aller Elemente

Das Setzen von `CurrentPageItem` auf den magischen Wert `0x7FFD` entspricht dem Löschen des Filters; der Pivot-Bereich fasst alle Seitenelemente zusammen, als ob kein Filter angewendet wäre.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// Fülle Obst/Jahr/Betrag Daten
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Erstelle Pivot-Tabelle bei E3
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// Konfiguriere Pivot-Felder: Obst→Zeile, Betrag→Daten, Jahr→Seite
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// Lösche den Seitenfilter, damit jedes Element im Seitenfeld sichtbar ist.
// 0x7FFD (Dezimal 32765) ist der spezielle Sentinel-Wert, der "alle Elemente" bedeutet —
// entspricht der Auswahl von "(Alle)" im Excel-Seitenfeld-Dropdown.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Anzeigen eines bestimmten Elements

Das Setzen von `CurrentPageItem` auf einen realen Index wählt genau dieses eine Seitenelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Beispieldaten hinzufügen (Obst/Jahr/Betrag)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// Pivot-Tabelle bei E3 hinzufügen
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Felder hinzufügen: Obst→Zeile, Betrag→Daten, Jahr→Seite
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Seitenfeldspezifische Operationen
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = zweites Element in sortierter Reihenfolge (z. B. "2021")

// Pivot-Tabelle aktualisieren und berechnen
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Mehrfachauswahl-Filterung**

Die Mehrfachauswahl-Filterung wandelt das Seiten-Dropdown in eine Kontrollkästchenliste um und ermöglicht es dem Endbenutzer, mehrere Seitenelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.IsMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.IsHidden`, welche Elemente in der Kontrollkästchenliste angezeigt werden, sodass Sie entweder jedes Element anzeigen oder nur bestimmte Elemente auf die Whitelist setzen können.

Der folgende Code aktiviert die Mehrfachauswahl für dasselbe Year-Filterfeld, das in Szenario 1a erstellt wurde, und zeigt dann zwei Muster. Teil A deckt jedes Seitenelement auf, indem `IsHidden` für jeden Eintrag auf `false` belassen wird, während Teil B nur die von Ihnen ausgewählten Quellwerte auf die Whitelist setzt und alles andere über einen `switch (pivotItems[i].getStringValue())`-Block ausblendet.

```javascript
const AsposeCells = require("aspose.cells");

// — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
//   Szenario 1a erstellt (Fruit/Year/Amount-Daten, Pivot bei E3, Fruit→Zeile,
//   Amount→Daten, Year→Seite über AddFieldToArea).
//   Unten wenden wir Mehrfachauswahl-Filterung auf das Seitenfeld an.

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// Beispieldaten: Frucht | Jahr | Betrag
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — Mehrfachauswahl auf dem Seitenfeld aktivieren
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// Teil A — ALLE Elemente auswählen (jedes Element sichtbar machen)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// Teil B — nur bestimmte Elemente anhand des Quellwerts auswählen
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
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

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.IsHidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`IsHidden == false`). Wenn jedes Element ausgeblendet ist, stürzt Excel beim Öffnen der Datei entweder ab oder rendert eine leere Pivot-Tabelle. Stellen Sie immer sicher, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollten verwendet werden?**

Die folgende Tabelle fasst zusammen, wann Sie welche API und welchen Modus verwenden sollten, damit Sie die richtige Kombination auswählen können, ohne jedes Szenario im Detail lesen zu müssen.

| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Filterfeld anhand des Quellspaltennamens hinzufügen (am häufigsten) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | High-Level, einzeilig. Verwenden Sie dies, sofern Sie keine `PivotField`-Referenz benötigen. |
| Filterfeld hinzufügen, wenn Sie bereits ein `PivotField`-Objekt haben | `pivotTable.getPageFields().add(PivotField)` | n/a | Verwenden Sie dies, wenn das Feldobjekt anderswo erhalten wurde oder wiederverwendet werden muss. |
| Auf ein einzelnes Seitenelement filtern (Standardmodus) | `PivotField.CurrentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste. |
| Alle Elemente anzeigen / Filter löschen | `PivotField.CurrentPageItem` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (dezimal 32765) ist der Sentinel für "alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.IsMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor `IsHidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste aus- / einblenden | `PivotItem.IsHidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`IsHidden == false`). |

{{% alert color="primary" %}}
Denken Sie immer an die Sichtbarkeitsbeschränkung, wenn Sie die Mehrfachauswahl-Filterung konfigurieren. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder rendert eine leere Pivot-Tabelle. Erstellen Sie Ihre Whitelist anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Computer zuverlässig geöffnet.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}
