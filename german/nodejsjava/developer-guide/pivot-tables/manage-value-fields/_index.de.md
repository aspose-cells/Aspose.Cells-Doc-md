---
title: Wertfelder einer PivotTable in Aspose.Cells für .NET verwalten
linktitle: Wertfelder
description: Erfahren Sie, wie Sie Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertefeld auf die Zeilen- oder Spaltenachse in Aspose.Cells for Node.js via Java plotten.
keywords: Aspose.Cells, Node.js via Java, PivotTable, Wertefeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Summe, Mittelwert
type: docs
weight: 230
url: /de/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## Hinzufügen eines Felds zum Datenbereich

Das Hinzufügen eines Basisfelds zum Daten- (Werte-) Bereich ist der erste Schritt bei der Gestaltung der Aggregation Ihrer Quelldaten in einer PivotTable. Aspose.Cells stellt `PivotTable.addFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.DATA` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, wird es über die Sammlung `PivotTable.getDataFields()` in der Reihenfolge verfügbar gemacht, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.SUM` zusammengefasst, während eine nicht numerische Spalte standardmäßig `COUNT` verwendet.

## Ändern der Zusammenfassungsfunktion

Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz gekapselt, und seine Eigenschaft `getFunction()` gibt einen Wert aus der Enumeration `ConsolidationFunction` zurück. Über denselben Setter `setFunction()` können Sie zwischen den verfügbaren Aggregaten wechseln, einschließlich `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` und `VARP`.

{{% alert color="primary" %}}
Das Ändern von `Function` wirkt sich nur auf das Aggregat aus, die Quellspalte wird nicht geändert.
{{% /alert %}}

Sie können daher ein Datenfeld als `SUM` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte abzielt, aber `COUNT` oder `AVERAGE` verwendet — alles in einer einzigen PivotTable.

## Wertefelder auf die Zeilen- oder Spaltenachse plotten

Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.getValuesField()` bereit. Dieses virtuelle Feld repräsentiert das Aggregat aller Datenfelder im Datenbereich. Sie können es als Basisfeld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Measures nebeneinander anzuordnen.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` funktioniert nicht, wenn kein oder nur ein Wertefeld vorhanden ist.
{{% /alert %}}

Die folgenden Szenarien führen durch drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben PivotTable-Struktur demonstrieren.

## Szenario 1 — Ziehen eines Basisfelds in den Wertebereich

Dieses Szenario zeigt, wie ein einzelnes Basisfeld (`Amount`) in den Datenbereich einer vorhandenen PivotTable eingefügt wird. Die gemeinsame PivotTable-Struktur platziert `Category` und `Item` auf der Zeilenachse und `Year` auf der Spaltenachse. Nach der Operation erscheint `Amount` im Datenbereich und wird standardmäßig als `Sum` von `Amount` berechnet.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// Pivot-Tabelle bei F3 mit dem Namen PivotTable1 hinzufügen
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot-Layout: Kategorie und Element in Zeile, Jahr in Spalte, Betrag als Datenfeld
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Szenario 2 — Ändern der Zusammenfassungsfunktion

Dieses Szenario beginnt mit derselben PivotTable-Struktur wie Szenario 1, fügt jedoch das Feld `Amount` zweimal zum Datenbereich hinzu. Beide Datenfelder verweisen auf dieselbe Quellspalte, jedoch wird das zweite Feld mithilfe des Setters `PivotField.setFunction()` überschrieben, sodass es anstelle der standardmäßigen `SUM` zu `COUNT` wird.

## Szenario 3 — Wertefelder auf die Zeilen- oder Spaltenachse plotten

Wenn zwei Datenfelder vorhanden sind, wird `PivotTable.getValuesField()` verwendbar. Dieses Szenario zieht das virtuelle Aggregatfeld in den Spaltenbereich, sodass jedes Measure im Datenbereich als eigener Spaltenblock neben `Year` erscheint.

Zusammen decken diese drei Szenarien jeden Aspekt der Wertefeldmanipulation in Aspose.Cells for Node.js via Java ab — von einem einzelnen Datenfeld mit der standardmäßigen `SUM` bis hin zu einer Multi-Measure-PivotTable, in der das virtuelle `ValuesField` das Layout auf der Zeilen- oder Spaltenachse steuert.

{{< app/cells/assistant language="nodejs-java" >}}
