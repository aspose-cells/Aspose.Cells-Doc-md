---
title: Hinzufügen von Zeilen- und Spaltenfeldern zu PivotTables in Aspose.Cells for Node.js via Java
linktitle: Hinzufügen von Zeilen- und Spaltenfeldern zu PivotTables
description: Erfahren Sie, wie Sie Basisfelder zu den Zeilen- und Spaltenbereichen einer PivotTable hinzufügen und Zwischensummen für Pivot-Felder mit PivotField.setSubtotals in Aspose.Cells for Node.js via Java steuern
keywords: Aspose.Cells, Node.js, Java, PivotTable, Zeilenfeld, Spaltenfeld, PivotField, setSubtotals, PivotFieldSubtotalType, Zwischensummen
type: docs
weight: 220
url: /de/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**
Die Methode `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Bereiche der PivotTable. Das Argument `fieldType` akzeptiert einen der folgenden `PivotFieldType`-Werte.
- `ROW` — Felder, die vertikal auf der linken Seite angeordnet sind
- `COLUMN` — Felder, die horizontal am oberen Rand angeordnet sind
- `DATA` — Felder, deren Werte aggregiert werden
- `PAGE` — Felder, die als Berichtsfilter verwendet werden
Die Reihenfolge, in der Felder verschachtelt werden, ist wichtig. Wenn `Category` zuerst zum Zeilenbereich und anschließend `Item` hinzugefügt wird, entsteht eine PivotTable, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Durch die umgekehrte Reihenfolge wird die Hierarchie umgekehrt.

## **Zwischensummen für Pivot-Felder**
Die Methode `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` steuert, welche Zwischensummenzeilen für ein Pivot-Feld angezeigt werden. Jeder Aufruf steuert unabhängig die Anzeige eines einzelnen Zwischensummen-Typs. Wenn `shown = true` übergeben wird, wird die Zwischensumme angezeigt; bei `shown = false` wird sie ausgeblendet. Da jeder Aufruf nur einen Typ betrifft, können Sie durch mehrmaliges Aufrufen der Methode mit unterschiedlichen `subtotalType`-Werten eine benutzerdefinierte Teilmenge von Zwischensummen erstellen.
Die Enumeration `PivotFieldSubtotalType` definiert die verfügbaren Zwischensummenarten.
- `AUTOMATIC` — Aspose.Cells wählt die Standardauswahl (in der Regel `SUM` für numerische Felder)
- `NONE` — deaktiviert alle Zwischensummenzeilen
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Zwischensummen werden nur dann angezeigt, wenn im Zeilenbereich (oder im Spaltenbereich) zwei oder mehr Pivot-Felder vorhanden sind. Bei einem einzelnen Feld gibt es keine sinnvolle Grundlage für eine Zwischensumme; `setSubtotals`-Aufrufe haben in diesem Fall daher keine sichtbare Wirkung. Dieser Artikel verwendet in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Zwischensummengrenze zwischen den einzelnen `Category`-Gruppen sichtbar wird.
{{% /alert %}}

## **Szenario 1 — Automatische Zwischensummen (Standard)**
Wenn Sie `setSubtotals` nicht aufrufen, wendet Aspose.Cells die `AUTOMATIC`-Auswahl auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten ausdrücklich, indem es `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` für das äußere Zeilenfeld `Category` aufruft.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Szenario 2 — Alle Zwischensummen unterdrücken (None)**
Der Aufruf von `setSubtotals(PivotFieldSubtotalType.NONE, true)` entfernt jede Zwischensummenzeile aus der PivotTable, sodass nur die Feldzeilen und die Gesamtsumme am unteren Rand übrig bleiben. Dies ist nützlich, wenn Sie die gruppierten Rohdaten ohne jegliche Zusammenfassungszeilen anzeigen möchten.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Szenario 3 — Benutzerdefinierte Teilmenge von Zwischensummen (Sum + Average)**
Sie sind nicht auf einen einzelnen Zwischensummen-Typ beschränkt. Jeder `setSubtotals`-Aufruf wirkt unabhängig auf einen Typ. Wenn Sie die Methode zweimal aufrufen — einmal mit `SUM` und einmal mit `AVERAGE` —, erhalten Sie eine benutzerdefinierte Teilmenge von zwei Zwischensummenzeilen für jede `Category`-Gruppe.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Zusammenfassung**

Die drei Szenarien unterscheiden sich lediglich in den Aufrufen von `setSubtotals`. Alles Weitere — der Dataset, die Felder und die Bereiche, denen sie zugewiesen sind — ist identisch, was die Layouts unmittelbar miteinander vergleichbar macht.
- **Platzieren von Feldern.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` verschiebt eine Quellspalte in einen Bereich. Innerhalb eines Bereichs bestimmt die Reihenfolge der Aufrufe die Anzeigereihenfolge, sodass der erste Aufruf die äußerste Gruppe bildet. Zwischensummen benötigen zwei oder mehr Felder im selben Bereich: Bei nur einem Feld gibt es nichts zwischen den Gruppen, für das eine Zwischensumme gebildet werden könnte.
- **Szenario 1 — automatische Zwischensummen.** Das Auslassen von `setSubtotals` überlässt die Entscheidung Excel, welches seine eigene Standard-Zwischensumme für numerische Felder anwendet. Der Aufruf von `setSubtotals` mit `AsposeCells.PivotFieldSubtotalType.AUTOMATIC` dokumentiert diese Entscheidung explizit, statt sie implizit zu belassen.
- **Szenario 2 — keine Zwischensummen.** `setSubtotals` mit `AsposeCells.PivotFieldSubtotalType.NONE` schaltet die Standard-Zwischensumme aus, sodass das Pivot-Table die Feldzeilen und die Gesamtsumme beibehält, aber die zwischen ihnen von Excel normalerweise eingefügten Zwischensummenzeilen entfernt.
- **Szenario 3 — eine ausgewählte Teilmenge.** Jeder Aufruf aktiviert genau einen Zwischensummentyp, wobei sich die Aufrufe akkumulieren und sich nicht gegenseitig zurücksetzen. Ein Aufruf mit `AsposeCells.PivotFieldSubtotalType.SUM` und ein weiterer Aufruf mit `AsposeCells.PivotFieldSubtotalType.AVERAGE` lassen daher beide aktiviert, und das Pivot-Table zeigt sowohl eine Summen-Zwischensumme als auch eine Durchschnitts-Zwischensumme sowie die Gesamtsumme an.

{{% alert color="primary" %}}
Nichtsbezüglich der Zwischensummen ist auf den Zeilenbereich spezifisch beschränkt. Die gleichen Aufrufe von `setSubtotals` für ein Feld aus `PivotTable.ColumnFields` erzeugen die gleichen drei Layouts entlang der Spaltenachse, da die Einstellung zum Pivot-Feld selbst gehört und nicht zur Achse, auf der es platziert ist.
{{% /alert %}}
## **Verwandte Artikel**
- [Seitenfelder in PivotTables](/cells/de/nodejs-java/add-page-field-in-pivot-table/)
- [Aktualisieren von PivotTables in Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/refresh-pivot-table/)
- [Anwenden von Stilen auf PivotTables](/cells/de/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}