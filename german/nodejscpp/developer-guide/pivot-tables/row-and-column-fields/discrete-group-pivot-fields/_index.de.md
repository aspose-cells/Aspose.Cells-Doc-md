---
title: Diskrete Gruppierung von Pivot-Feld-Elementen
linktitle: Diskrete Gruppierung
description: Erfahren Sie, wie Sie Pivot-Feld-Elemente in benutzerdefinierte benannte Gruppen wie Obst und Gemüse mithilfe von DiscreteGroupItem und PivotFieldGroupOptions.DiscreteGroupItems in Aspose.Cells for Node.js via C++ gruppieren.
keywords: Aspose.Cells, PivotTable, diskrete Gruppierung, DiscreteGroupItem, PivotFieldGroupOptions, Pivot-Elemente gruppieren, benutzerdefinierte Gruppen, PivotField.Group, Node.js, Excel-PivotTable
type: docs
weight: 90
url: /de/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
- Die automatische Gruppierung sammelt Elemente nach Datentyp, zum Beispiel Daten in Monate und Quartale oder Zahlen in Bereiche. Die diskrete Gruppierung löst das gegenteilige Problem, indem sie spezifische, nicht zusammengehörige Elemente in benutzerdefinierte benannte Gruppen sammelt, beispielsweise Produkte in Obst und Gemüse, Filialen in Regionen oder Konten in Zonen. Aspose.Cells for Node.js via C++ bietet die diskrete Gruppierung über die Klasse `DiscreteGroupItem` und die Eigenschaft `PivotFieldGroupOptions.discreteGroupItems`.
- `DiscreteGroupItem` ist ein Gruppenname plus die zugehörigen Elemente. Die Elemente können auf zwei Arten identifiziert werden, entweder über ihre Namen (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) oder über ihre nullbasierten Positionen in den Quelldaten (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Beide Formen erzeugen das gleiche Ergebnis.
- Die diskrete Gruppierung wird auf ein Feld im Zeilen‑ oder Spaltenbereich der PivotTable angewendet, indem die Optionen an `pivotField.group(pivotFieldGroupOptions)` übergeben werden.

## **Pivot-Feld-Elemente nach Elementnamen gruppieren**
Das folgende Beispiel erstellt eine kleine Verkaufsliste (Produkt, Datum und Betrag), erzeugt daraus eine PivotTable mit `product` im Zeilenbereich, `date` im Spaltenbereich und `amount` im Datenbereich und definiert anschließend zwei benutzerdefinierte Gruppen anhand von Elementnamen, Obst (grape, cherry) und Gemüse (carrot, potato). Das Ergebnis zeigt ein zweistufiges Zeilenlayout, wobei der Gruppenname die äußere Ebene bildet und die ursprünglichen Elemente darunter verschachtelt sind, sodass Trends pro benutzerdefinierter Gruppe und pro Element gelesen werden können.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Nach `calculateData()` zeigt der Zeilenbereich der PivotTable Obst (grape 50, cherry 80) und Gemüse (carrot 60, potato 70) mit einer Gesamtsumme von 260, und die Spaltenbeschriftungen behalten die vier Daten bei (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Pivot-Feld-Elemente nach Elementindizes gruppieren**
Wenn die Elementnamen lang oder lokalisiert sind, identifiziert der zweite Konstruktor von `DiscreteGroupItem` die Elemente über den Index. Die Indizes sind nullbasierte Positionen der Elemente in der Reihenfolge, in der sie in den Quelldaten erscheinen, nicht alphabetisch. In den obigen Beispieldaten ist grape Element 0, carrot Element 1, potato Element 2 und cherry Element 3, sodass Obst `{ 0, 3 }` und Gemüse `{ 1, 2 }` ist. Das Ergebnis ist identisch mit dem namenbasierten Beispiel.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Hinweis**

{{% alert color="primary" %}}
- Elemente, die keinen benutzerdefinierten Gruppen zugewiesen sind, gehen nicht verloren. Sie verbleiben in der PivotTable auf derselben Ebene wie die benutzerdefinierten Gruppen, jeweils als eigenständiger Eintrag. Im obigen Beispiel lässt die Definition nur der Obst‑Gruppe Karotte und Kartoffel im Zeilenbereich als einzelne Einträge neben der Obst‑Gruppe.
- Die Eigenschaft `PivotFieldGroupOptions.newPivotField` steuert das Layout der diskreten Gruppierung. Sie ist standardmäßig auf true gesetzt, wodurch das gruppierte Feld als neues äußeres Feld neben dem ursprünglichen hinzugefügt wird und das oben gezeigte zweistufige Layout erzeugt (`rowFields` wächst auf 2). Setzt man sie auf false, wird das ursprüngliche Feld stattdessen ersetzt; der Zeilenbereich zeigt dann eine einzelne Ebene, die nur die Gruppennamen mit ihren aggregierten Werten enthält, Obst 130 (50 + 80) und Gemüse 130 (60 + 70).
- Die namenbasierten und indexbasierten Konstruktoren von `DiscreteGroupItem` können innerhalb desselben `PivotFieldGroupOptions.discreteGroupItems`‑Arrays gemischt werden.
{{% /alert %}}

## **Verwandte Artikel**
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Zeilen‑ und Spaltenfelder zur PivotTable hinzufügen](/cells/de/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [PivotTable nach Etikett oder Wert filtern](/cells/de/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Stil auf PivotTable anwenden](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)
- [PivotTable aktualisieren](/cells/de/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}