---
title: Filterfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
linktitle: Filterfelder hinzufügen
description: Lernen Sie, wie Sie Filterfelder in Pivot-Tabellen mit Aspose.Cells for Node.js via C++ hinzufügen und konfigurieren, einschließlich Hinzufügen von Filterfeldern, Einzelauswahl-Filterung und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, Node.js via C++, Pivot-Tabelle, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/nodejs-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in Pivot-Tabellen. Sie können ein Filterfeld über eine High-Level-Komfort-API oder über die Low-Level-Sammlung `PageFields` hinzufügen, und sie können den Filter im Einzelauswahlmodus steuern, ihn löschen, um alle Seitenelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, damit Benutzer mehrere Seitenelemente gleichzeitig über die Kontrollkästchen-Benutzeroberfläche in Excel auswählen können.
{{% /alert %}}

## **Einführung**

Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Körper anzeigt. Endbenutzer sehen es als Dropdown oben in einer gerenderten Pivot-Tabelle in Excel, und die Auswahl eines der verfügbaren Seitenelemente baut den Pivot-Körper neu auf, sodass nur die Datensätze zusammengefasst werden, die zu diesem Seitenelement gehören. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.Page` registriert wird, anstatt als `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data`.

Ein Filterfeld kann in zwei Verhaltensweisen arbeiten. Im Standardverhalten der **Einzelauswahl** ist immer nur ein Seitenelement sichtbar, sodass der Pivot-Körper genau eine Teilmenge zusammenfasst. Im Verhalten der **Mehrfachauswahl** zeigt das Feld eine Kontrollkästchenliste, und der Pivot-Körper fasst die Vereinigung aller markierten Seitenelemente zusammen. Dasselbe Quellfeld kann durch Umschalten einer einzigen Eigenschaft zwischen diesen Verhaltensweisen hin und her bewegt werden.

Aspose.Cells for Node.js via C++ bietet zwei gleichwertige Möglichkeiten, ein Filterfeld zu registrieren. Die High-Level-API ist `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, die den Namen der Quellspalte übernimmt und das Feld in einem einzigen Aufruf hinzufügt. Die Low-Level-API ist `PivotTable.pageFields.add(PivotField)`, die verwendet wird, wenn Sie bereits eine `PivotField`-Referenz besitzen und dieselbe Feldinstanz zum Filterbereich hinzufügen möchten. Beide APIs füllen am Ende dieselbe `PageFields`-Sammlung, und der Rest dieses Artikels zeigt, wie Sie zwischen ihnen wählen und wie Sie jeden Filtermodus steuern.

## **Hinzufügen eines Filterfelds**

Es gibt zwei Möglichkeiten, ein Pivot-Feld im Filterbereich zu registrieren. Der High-Level-Aufruf übernimmt den Namen der Quellspalte als Zeichenfolge und ist der häufigste Weg. Der Low-Level-Aufruf akzeptiert eine vorhandene `PivotField`-Instanz und ist praktisch, wenn dasselbe Feldobjekt in mehreren Pivot-Bereichen wiederverwendet werden muss. Beide Aufrufe platzieren das Feld in `PivotTable.pageFields`, wonach es als Seiten-Dropdown oben in der gerenderten Pivot-Tabelle erscheint.

### Hinzufügen eines Filterfelds mit addFieldToArea

Das folgende Beispiel erstellt einen kleinen Fruit / Year / Amount-Datensatz, platziert eine Pivot-Tabelle in Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Kopfzeile einrichten
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 Zeilen Beispieldaten befüllen: Frucht, Jahr, Betrag
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

// Pivot-Tabelle verankert an Zelle E3 hinzufügen
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Felder ihren Bereichen hinzufügen: Frucht als Zeile, Betrag als Daten, Jahr als Seitenfeld
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Pivot-Tabellen-Daten aktualisieren und berechnen
pivotTable.calculateData();

// Arbeitsmappe speichern
workbook.save("pageFieldSample.xlsx");
```

### Hinzufügen eines Filterfelds mit pageFields.add

Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.pageFields.add` übergeben. Die Pivot-Tabelle und das Filterfeld werden genau wie im vorherigen Szenario konstruiert; nur die endgültige Registrierung im Filterbereich wird durch den Low-Level-API-Aufruf ersetzt.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Überschriften
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Beispieldaten (9 Zeilen)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Pivot-Tabelle bei E3 hinzufügen, die A1:C10 abdeckt
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Frucht -> Zeile, Betrag -> Daten (Jahr wird unten zur Seite hinzugefügt)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Low-Level-Ansatz: Das vorhandene Jahr-PivotField aus BaseFields holen
// und es über PageFields.Add(PivotField) im Seitenbereich registrieren.
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe widergespiegelt wird
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Einzelauswahl-Filterung (Anzeigen eines Seitenelements)**

Im Standardverhalten der Einzelauswahl rendert das Filterfeld als einzelnes Dropdown, und die `PivotField.currentPageItem`-Ganzzahl wählt aus, welches Seitenelement den Pivot-Körper steuert. Durch Zuweisen eines bestimmten Index wird genau dieses Element ausgewählt; durch Zuweisen des speziellen Sentinelwerts `0x7FFD` (dezimal 32765) wird der Filter gelöscht, sodass alle Seitenelemente gleichzeitig zusammengefasst werden. Einzelauswahl ist die Standardeinstellung; Sie müssen sie nicht explizit aktivieren.

### Anzeigen aller Elemente

Das Setzen von `currentPageItem` auf den magischen Wert `0x7FFD` entspricht dem Löschen des Filters: der Pivot-Körper fasst jedes Seitenelement zusammen, als ob kein Filter angewendet wäre.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Fruit/Jahr/Betrag Daten einfügen
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Pivot-Tabelle bei E3 erstellen
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// Pivot-Felder konfigurieren: Fruit→Zeile, Amount→Daten, Year→Seite
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// Den Seitenfilter zurücksetzen, damit jedes Element im Seitenfeld sichtbar ist.
// 0x7FFD (Dezimal 32765) ist der spezielle Sentinel-Wert, der "alle Elemente" bedeutet —
// entspricht der Auswahl von "(Alle)" im Dropdown-Menü des Seitenfelds in Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Anzeigen eines bestimmten Elements

Das Setzen von `currentPageItem` auf einen tatsächlichen Index wählt genau dieses eine Seitenelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

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
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Felder hinzufügen: Frucht→Zeile, Betrag→Daten, Jahr→Seite
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Seitenfeld-spezifische Operationen
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = zweites Element in sortierter Reihenfolge (z. B. "2021")

// Pivot-Tabelle aktualisieren und berechnen
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Mehrfachauswahl-Filterung**

Die Mehrfachauswahl-Filterung verwandelt das Seiten-Dropdown in eine Kontrollkästchenliste und ermöglicht es dem Endbenutzer, mehrere Seitenelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.isMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.isHidden`, welche Elemente in der Kontrollkästchenliste erscheinen, sodass Sie entweder jedes Element anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

Der folgende Code aktiviert die Mehrfachauswahl für dasselbe Year-Filterfeld, das in Szenario 1a erstellt wurde, und zeigt dann zwei Muster: Teil A deckt jedes Seitenelement auf, indem `isHidden` für jeden Eintrag auf `false` belassen wird, während Teil B nur die von Ihnen gewählten Quellwerte auf die Whitelist setzt und alles andere über einen `switch (pivotItems[i].getStringValue())`-Block ausblendet.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// Beispieldaten: Frucht | Jahr | Betrag
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// — Mehrfachauswahl für das Seitenfeld aktivieren
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// Teil A — ALLE Elemente auswählen (alle Elemente sichtbar machen)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// Teil B — nur bestimmte Elemente nach Quellwert auswählen
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.isHidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`isHidden == false`). Wenn jedes Element ausgeblendet ist, stürzt Excel entweder beim Öffnen der Datei ab oder rendert eine leere Pivot-Tabelle. Überprüfen Sie immer, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welchen Modus sollte ich verwenden?**

Die folgende Tabelle fasst zusammen, wann Sie jede API und jeden Modus verwenden sollten, damit Sie die richtige Kombination auswählen können, ohne jedes Szenario im Detail lesen zu müssen.

| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Hinzufügen eines Filterfelds nach Quellspaltenname (am häufigsten) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/v | High-Level, einzeilig. Verwenden Sie dies, sofern Sie keine `PivotField`-Referenz benötigen. |
| Hinzufügen eines Filterfelds, wenn Sie bereits ein `PivotField`-Objekt haben | `PivotTable.pageFields.add(PivotField)` | n/v | Verwenden Sie dies, wenn das Feldobjekt anderweitig bezogen wurde oder wiederverwendet werden muss. |
| Filter auf ein einzelnes Seitenelement (Standardmodus) | `PivotField.currentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste an. |
| Alle Elemente anzeigen / Filter löschen | `PivotField.currentPageItem` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (dezimal 32765) ist der Sentinelwert für „alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.isMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor `isHidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste ausblenden / anzeigen | `PivotItem.isHidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`isHidden == false`). |

{{% alert color="primary" %}}
Denken Sie immer an die Sichtbarkeitseinschränkung, wenn Sie die Mehrfachauswahl-Filterung konfigurieren. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder rendert eine leere Pivot-Tabelle. Erstellen Sie Ihre Whitelist anhand Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Computer zuverlässig geöffnet.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
