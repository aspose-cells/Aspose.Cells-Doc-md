---
title: Hinzufügen von Zeilen- und Spaltenfeldern zu Pivot-Tabellen in Aspose.Cells for Node.js via C++
linktitle: Hinzufügen von Zeilen- und Spaltenfeldern zu Pivot-Tabellen
description: Erfahren Sie, wie Sie Basisfelder zu den Zeilen- und Spaltenbereichen einer Pivot-Tabelle hinzufügen und Pivot-Feld-Zwischensummen mit PivotField.setSubtotals in Aspose.Cells for Node.js via C++ steuern
keywords: Aspose.Cells, Node.js, C++, Pivot-Tabelle, Zeilenfeld, Spaltenfeld, PivotField, SetSubtotals, PivotFieldSubtotalType, Zwischensummen
type: docs
weight: 220
url: /de/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**
Die Methode `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Pivot-Bereiche. Das Argument `fieldType` akzeptiert einen der folgenden `PivotFieldType`-Werte.
- `Row` — Felder werden vertikal auf der linken Seite angeordnet
- `Column` — Felder werden horizontal am oberen Rand angeordnet
- `Data` — Felder, deren Werte aggregiert werden
- `Page` — Felder, die als Berichtsfilter verwendet werden
Die Verschachtelungsreihenfolge der Felder ist wichtig. Wenn Sie zuerst `Category` zum Zeilenbereich und dann `Item` hinzufügen, entsteht eine Pivot-Tabelle, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Eine umgekehrte Reihenfolge kehrt die Hierarchie um.

## **Zwischensummen von Pivot-Feldern**
Die Methode `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` steuert, welche Zwischensummenzeilen für ein Pivot-Feld angezeigt werden. Jeder Aufruf schaltet einen einzelnen Zwischensummentyp unabhängig um. Die Übergabe von `shown = true` zeigt die Zwischensumme an, während `shown = false` sie ausblendet. Da jeder Aufruf nur einen Typ betrifft, wird durch mehrere Aufrufe der Methode mit unterschiedlichen `subtotalType`-Werten eine benutzerdefinierte Untermenge von Zwischensummen erstellt.
Die Enumeration `PivotFieldSubtotalType` definiert die verfügbaren Zwischensummenarten.
- `Automatic` — Aspose.Cells wählt die Standardauswahl (in der Regel `Sum` für numerische Felder)
- `None` — alle Zwischensummenzeilen unterdrücken
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
Zwischensummen werden nur dann gerendert, wenn zwei oder mehr Pivot-Felder im Zeilenbereich (oder im Spaltenbereich) vorhanden sind. Ein einzelnes Feld bietet keine sinnvolle Grundlage für eine Zwischensumme, sodass Aufrufe von `setSubtotals` in diesem Fall keine sichtbare Wirkung haben. Dieser Artikel platziert daher zwei Zeilenfelder (`Category` außen, `Item` innen) in jedem Beispiel, damit die Zwischensummengrenze zwischen jeder `Category`-Gruppe sichtbar ist.
{{% /alert %}}

## **Szenario 1 — Automatische (Standard-) Zwischensummen**
Wenn Sie `setSubtotals` überhaupt nicht aufrufen, wendet Aspose.Cells die Auswahl `Automatic` auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten explizit, indem `setSubtotals(PivotFieldSubtotalType.Automatic, true)` auf dem äußeren `Category`-Zeilenfeld aufgerufen wird.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Szenario 2 — Unterdrücken aller Zwischensummen (None)**
Der Aufruf von `setSubtotals(PivotFieldSubtotalType.None, true)` entfernt jede Zwischensummenzeile aus der Pivot-Tabelle, sodass nur die Feldzeilen und die Gesamtsumme am unteren Rand übrig bleiben. Dies ist nützlich, wenn Sie die rohen gruppierten Daten ohne Zusammenfassungszeilen anzeigen möchten.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Szenario 3 — Benutzerdefinierte Zwischensummen-Untermenge (Sum + Average)**
Sie sind nicht auf einen einzelnen Zwischensummentyp beschränkt. Jeder `setSubtotals`-Aufruf wirkt unabhängig auf einen Typ. Daher erzeugt ein zweimaliger Aufruf der Methode — einmal mit `Sum` und einmal mit `Average` — eine benutzerdefinierte Untermenge von zwei Zwischensummenzeilen für jede `Category`-Gruppe.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
let pivotTables = worksheet.getPivotTables();
let pivotTable = pivotTables.add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Zusammenfassung**
Die drei Szenarien unterscheiden sich nur in einer Sache: den `setSubtotals`-Aufrufen. Alles Weitere – der Datensatz, die Felder und die Bereiche, in denen sie platziert werden – ist identisch, was die Layouts direkt vergleichbar macht.
- **Felder platzieren.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` verschiebt eine Quellspalte in einen Bereich. Innerhalb eines Bereichs entspricht die Reihenfolge der Aufrufe der Anzeigereihenfolge, sodass der erste Aufruf die äußere Gruppe bildet. Subtotals benötigen zwei oder mehr Felder im selben Bereich: Bei einem einzelnen Feld gibt es zwischen den Gruppen nichts, worauf eine Subtotalbildung angewendet werden könnte.
- **Szenario 1 – automatische Subtotals.** Wird `setSubtotals` nicht aufgerufen, trifft Excel selbst die Entscheidung und wendet seinen eigenen Standard-Subtotal-Typ auf numerische Felder an. Ein Aufruf von `setSubtotals` mit `AsposeCells.PivotFieldSubtotalType.Automatic` macht diese Entscheidung explizit, anstatt sie implizit zu belassen.
- **Szenario 2 – keine Subtotals.** `setSubtotals` mit `AsposeCells.PivotFieldSubtotalType.None` deaktiviert den Standard-Subtotal-Typ, sodass der Pivot-Tabellen die Feldzeilen und die Gesamtsumme beibehält, jedoch die Zwischensubtotal-Zeilen entfällt, die Excel andernfalls dazwischen einfügen würde.
- **Szenario 3 – eine ausgewählte Teilmenge.** Jeder Aufruf schaltet genau einen Subtotal-Typ um, und die Aufrufe summieren sich auf, anstatt sich gegenseitig zu überschreiben. Ein erstes Maliges Aufrufen mit `AsposeCells.PivotFieldSubtotalType.Sum` und ein zweites Maliges Aufrufen mit `AsposeCells.PivotFieldSubtotalType.Average` führt dazu, dass beide Subtotal-Typen aktiviert bleiben; der Pivot-Tabellen zeigt dann sowohl eine Summen- als auch eine Durchschnitts-Subtotal sowie die Gesamtsumme an.

{{% alert color="primary" %}}
Nichts an der Subtotal-Behandlung ist auf den Zeilenbereich beschränkt. Dieselben `setSubtotals`-Aufrufe für ein Feld, das aus `PivotTable.ColumnFields` stammt, erzeugen dieselben drei Layouts auf der Spaltenachse, da die Einstellung zum Pivot-Feld selbst gehört und nicht zur Achse, auf der es sitzt.
{{% /alert %}}

## **Verwandte Artikel**
- [Seitenfelder in Pivot-Tabellen](/cells/de/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells for Node.js via C++](/cells/de/nodejs-cpp/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}