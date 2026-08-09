---
title: Wertfelder einer PivotTable in Aspose.Cells für .NET verwalten
linktitle: Wertfelder
description: Erfahren Sie, wie Sie Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertfeld auf die Zeilen- oder Spaltenachse in Aspose.Cells for Node.js via C++ setzen.
keywords: Aspose.Cells, Node.js via C++, PivotTable, Wertfeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Summe, Mittelwert
type: docs
weight: 230
url: /de/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Hinzufügen eines Felds zum Datenbereich
Das Hinzufügen eines Basisfelds zum Daten-(Wert-)Bereich ist der erste Schritt, um zu gestalten, wie eine PivotTable Ihre Quelldaten aggregiert. Aspose.Cells stellt `PivotTable.addFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.Data` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, macht die API es über die Sammlung `PivotTable.getDataFields()` in der Reihenfolge verfügbar, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.Sum` zusammengefasst, während eine nicht numerische Spalte standardmäßig `Count` verwendet.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Kopfzeilen in A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Datenzeilen A2:D9 mit verschachtelten Schleifen, die nach j verzweigen
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i === 1 || i === 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i === 3 || i === 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i === 5 || i === 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i === 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i === 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i === 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i === 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i === 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i === 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i === 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// Pivot-Tabelle bei F3 mit dem Namen PivotTable1 hinzufügen
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot-Layout: Kategorie und Element in Zeile, Jahr in Spalte, Betrag als Datenfeld
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Ändern der Zusammenfassungsfunktion
Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz umschlossen, und seine Eigenschaft `getFunction()` gibt einen Wert aus der Enumeration `ConsolidationFunction` zurück. Mit demselben Setter `setFunction()` können Sie zwischen den verfügbaren Aggregaten wechseln, einschließlich `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` und `Varp`.
{{% alert color="primary" %}}
Das Ändern der Zusammenfassungsfunktion wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
{{% /alert %}}
Sie können daher ein Datenfeld als `Sum` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte abzielt, aber `Count` oder `Average` verwendet, alles in einer einzigen PivotTable.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
 worksheet.getCells().get(i, j).putValue(items[i - 1]);
 }
 else if (j == 2)
 {
 let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
 worksheet.getCells().get(i, j).putValue(years[i - 1]);
 }
 else
 {
 let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
 worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();

workbook.save("output_function.xlsx");
```

## Wertfelder auf die Zeilen- oder Spaltenachse setzen
Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.getValuesField` bereit. Dieses virtuelle Feld stellt das Aggregat jedes Datenfelds dar, das sich im Datenbereich befindet. Sie können es als Basis-Pivot-Feld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Kennzahlen nebeneinander anzuordnen.
{{% alert color="primary" %}}
`PivotTable.getValuesField()` funktioniert nicht, wenn kein oder nur ein Wertfeld vorhanden ist.
{{% /alert %}}
Die folgenden Szenarien führen durch drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben Pivot-Struktur demonstrieren.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

let categories = ["Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable"];
let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
let amounts = [100, 150, 80, 90, 50, 60, 40, 45];

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.getCells().get(i, j).putValue(categories[i - 1]);
 else if (j == 1) worksheet.getCells().get(i, j).putValue(items[i - 1]);
 else if (j == 2) worksheet.getCells().get(i, j).putValue(years[i - 1]);
 else worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField().getName());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}