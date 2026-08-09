---
title: Wertfelder in Aspose.Cells for Node.js via Java
linktitle: Wertfelder
description: Erfahren Sie, wie Sie Basisfelder zum Datenbereich einer Pivot-Tabelle hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertfeld in Aspose.Cells for Node.js via Java auf die Zeilen- oder Spaltenachse abbilden.
keywords: Aspose.Cells, Node.js via Java, Pivot-Tabelle, Wertfeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Summe, Mittelwert
type: docs
weight: 230
url: /de/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Wertfelder sind das Herzstück jeder Pivot-Tabelle, die numerischen Aggregate, die die Quelldaten zusammenfassen. In Aspose.Cells for Node.js via Java wird der Datenbereich einer Pivot-Tabelle gefüllt, indem Basisfelder über `PivotTable.addFieldToArea` hinzugefügt werden, und jedes in diesem Bereich platzierte Feld kann eine eigene Zusammenfassungsfunktion haben. Wenn zwei oder mehr Datenfelder vorhanden sind, stellt Aspose.Cells ein spezielles Aggregatfeld, `PivotTable.getValuesField()`, bereit, das als Basisfeld auf die Zeilen- oder Spaltenachse abgebildet werden kann, wodurch Sie eine feinere Kontrolle darüber erhalten, wie Wertfelder im Layout angezeigt werden.
## Hinzufügen eines Felds zum Datenbereich
Das Hinzufügen eines Basisfelds zum Datenbereich (Wertebereich) ist der erste Schritt, um zu gestalten, wie eine Pivot-Tabelle Ihre Quelldaten aggregiert. Aspose.Cells stellt `PivotTable.addFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.DATA` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, ist es über die Sammlung `PivotTable.getDataFields()` in der Reihenfolge zugänglich, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.SUM` zusammengefasst, während eine nicht-numerische Spalte standardmäßig auf `COUNT` gesetzt ist.

```javascript
const AsposeCells = require("aspose.cells");

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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Ändern der Zusammenfassungsfunktion
Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz umschlossen, und die `getFunction()`-Eigenschaft gibt einen Wert aus der `ConsolidationFunction`-Enumeration zurück. Derselbe `setFunction()`-Setter ermöglicht es Ihnen, zwischen den verfügbaren Aggregaten zu wechseln, einschließlich `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` und `VARP`.
{{% alert color="primary" %}}
Das Ändern von `Function` wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
{{% /alert %}}
Sie können daher ein Datenfeld als `SUM` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte abzielt, aber `COUNT` oder `AVERAGE` verwendet, alles in einer einzigen Pivot-Tabelle.

```javascript
const AsposeCells = require("aspose.cells");

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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## Wertfelder auf die Zeilen- oder Spaltenachse abbilden
Wenn eine Pivot-Tabelle zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.getValuesField()` bereit. Dieses virtuelle Feld repräsentiert das Aggregat jedes Datenfelds im Datenbereich. Sie können es als Basisfeld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Measures nebeneinander anzuordnen.
{{% alert color="primary" %}}
`PivotTable.getValuesField()` funktioniert nicht, wenn kein oder nur ein Wertfeld vorhanden ist.
{{% /alert %}}
Die folgenden Szenarien durchlaufen drei durchgängige Beispiele, die jede oben beschriebene Funktion anhand derselben Pivot-Struktur demonstrieren.

```javascript
const AsposeCells = require("aspose.cells");

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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
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

{{< app/cells/assistant language="javascript" >}}