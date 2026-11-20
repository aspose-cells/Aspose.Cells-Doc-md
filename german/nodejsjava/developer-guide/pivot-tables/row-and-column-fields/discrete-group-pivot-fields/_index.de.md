---
title: Diskrete Gruppierung von Pivot-Feldelementen
linktitle: Diskrete Gruppierung
description: Erfahren Sie, wie Sie Pivot-Feldelemente in Aspose.Cells for Node.js via Java mithilfe von DiscreteGroupItem und PivotFieldGroupOptions.getDiscreteGroupItems() in benutzerdefinierte Gruppen wie etwa Obst und Gemüse gruppieren.
keywords: Aspose.Cells, PivotTable, diskrete Gruppierung, DiscreteGroupItem, PivotFieldGroupOptions, Pivot-Feldelemente gruppieren, benutzerdefinierte Gruppen, PivotField.group, Aspose.Cells for Node.js via Java, Excel-PivotTable
type: docs
weight: 90
url: /de/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
- Die automatische Gruppierung fasst Elemente nach Datentyp zusammen, etwa Datumsangaben nach Monaten und Quartalen oder Zahlen nach Bereichen. Die diskrete Gruppierung löst das umgekehrte Problem: Sie fasst bestimmte, nicht zusammengehörige Elemente in benutzerdefinierte Gruppen mit Namen zusammen, beispielsweise Produkte in Obst und Gemüse, Geschäfte in Regionen oder Konten in Zonen. Aspose.Cells bietet die diskrete Gruppierung über die Klasse `DiscreteGroupItem` und die Eigenschaft `PivotFieldGroupOptions.getDiscreteGroupItems()` an.
- Ein `DiscreteGroupItem` besteht aus einem Gruppennamen und den Elementen, die ihm zugeordnet sind. Die Elemente können auf zwei Arten identifiziert werden: durch ihre Namen (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) oder durch ihre auf null basierenden Positionen in den Quelldaten (`new DiscreteGroupItem("fruit", [0, 3])`). Beide Varianten führen zu demselben Ergebnis.
- Die diskrete Gruppierung wird für ein Feld im Zeilen- oder Spaltenbereich der PivotTable angewendet, indem die Optionen an `PivotField.group(PivotFieldGroupOptions)` übergeben werden.

## **Gruppieren von Pivot-Feldelementen nach Elementnamen**
Das folgende Beispiel erstellt eine kleine Verkaufsliste (Produkt, Datum und Betrag) und erzeugt daraus eine PivotTable mit `product` im Zeilenbereich, `date` im Spaltenbereich und `amount` im Datenbereich. Anschließend werden anhand der Elementnamen zwei benutzerdefinierte Gruppen definiert: `fruit` (`grape`, `cherry`) und `vegetables` (`carrot`, `potato`). Das Ergebnis zeigt einen zweistufigen Zeilenaufbau, bei dem der Gruppenname die äußere Ebene bildet und die ursprünglichen Elemente darunter verschachtelt sind. Dadurch lassen sich Trends je benutzerdefinierter Gruppe und je Element ablesen.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Nach `calculateData()` zeigt der Zeilenbereich der PivotTable `fruit` (`grape` 50, `cherry` 80) und `vegetable` (`carrot` 60, `potato` 70) mit einer Gesamtsumme von 260. In den Spaltenbeschriftungen bleiben die vier Datumsangaben (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) erhalten.

## **Gruppieren von Pivot-Feldelementen nach Elementindizes**
Wenn die Elementnamen lang oder lokalisiert sind, identifiziert der zweite Konstruktor von `DiscreteGroupItem` die Elemente anhand ihres Index. Die Indizes geben die auf null basierenden Positionen der Elemente in der Reihenfolge ihres Auftretens in den Quelldaten und nicht in alphabetischer Reihenfolge an. In den obigen Beispieldaten ist `grape` Element 0, `carrot` Element 1, `potato` Element 2 und `cherry` Element 3. Daher umfasst `fruit` `{ 0, 3 }` und `vegetable` `{ 1, 2 }`. Das Ergebnis ist mit dem namensbasierten Beispiel identisch.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Hinweis**

{{% alert color="primary" %}}
- Elemente, die keiner benutzerdefinierten Gruppe zugewiesen sind, gehen nicht verloren. Sie bleiben in der PivotTable auf derselben Ebene wie die benutzerdefinierten Gruppen erhalten und bilden jeweils einen eigenen Einzeleintrag. Im obigen Beispiel bleiben `carrot` und `potato` bei ausschließlicher Definition der Gruppe `fruit` als eigenständige Einträge im Zeilenbereich neben der Gruppe `fruit`.
- Die Eigenschaft `PivotFieldGroupOptions.getNewPivotField()` steuert den Layout der diskreten Gruppierung. Sie ist standardmäßig `true` und fügt damit das gruppierte Feld als neues äußeres Feld neben dem ursprünglichen Feld hinzu. So entsteht der oben gezeigte zweistufige Aufbau (`getRowFields()` wird auf 2 erweitert). Setzen Sie die Eigenschaft mit `PivotFieldGroupOptions.setNewPivotField(false)` auf `false`, um stattdessen das ursprüngliche Feld zu ersetzen. Der Zeilenbereich zeigt dann eine einzige Ebene mit den Gruppennamen und ihren aggregierten Werten: `fruit` 130 (50 + 80) und `vegetable` 130 (60 + 70).
- Die namensbasierten und indexbasierten Konstruktoren von `DiscreteGroupItem` können innerhalb desselben `getDiscreteGroupItems()`-Arrays kombiniert werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Zeilen- und Spaltenfelder in der PivotTable hinzufügen](/cells/de/nodejs-java/pivot-table-add-row-and-column-fields/)
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Stil auf die PivotTable anwenden](/cells/de/nodejs-java/apply-style-to-pivot-table/)
- [PivotTable aktualisieren](/cells/de/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}