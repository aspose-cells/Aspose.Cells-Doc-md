---
title: Wertfelder in Aspose.Cells for Node.js via C++
linktitle: Wertfelder
description: Lernen Sie, wie Sie Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertfeld auf die Zeilen- oder Spaltenachse in Aspose.Cells for Node.js via C++ setzen
keywords: Aspose.Cells, Node.js, C++, PivotTable, Wertfeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /de/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Wertfelder sind das Herzstück jeder PivotTable, die numerischen Aggregate, die die Quelldaten zusammenfassen. In Aspose.Cells for Node.js via C++ wird der Datenbereich einer PivotTable befüllt, indem Basisfelder über `PivotTable.addFieldToArea` hinzugefügt werden, und jedes in diesem Bereich platzierte Feld kann eine eigene Zusammenfassungsfunktion haben. Wenn zwei oder mehr Datenfelder vorhanden sind, stellt Aspose.Cells ein spezielles Aggregatfeld, `PivotTable.ValuesField`, bereit, das als Basisfeld auf die Zeilen- oder Spaltenachse gesetzt werden kann, sodass Sie eine feinere Kontrolle darüber haben, wie Wertfelder im Layout erscheinen.

## Hinzufügen eines Felds zum Datenbereich

Das Hinzufügen eines Basisfelds zum Datenbereich (Wertebereich) ist der erste Schritt, um zu gestalten, wie eine PivotTable Ihre Quelldaten aggregiert. Aspose.Cells stellt `PivotTable.addFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.Data` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, stellt die API es über die Sammlung `PivotTable.DataFields` in der Reihenfolge bereit, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.Sum` zusammengefasst, während eine nicht numerische Spalte standardmäßig `Count` verwendet.

## Ändern der Zusammenfassungsfunktion

Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz gekapselt, und seine `Function`-Eigenschaft gibt einen Wert aus der Enumeration `ConsolidationFunction` zurück. Mit demselben `Function`-Setter können Sie zwischen den verfügbaren Aggregaten wechseln, einschließlich `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` und `Varp`.

{{% alert color="primary" %}}
Das Ändern von `Function` wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
{{% /alert %}}

Sie können daher ein Datenfeld als `Sum` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte verweist, aber `Count` oder `Average` verwendet, alles in einer einzigen PivotTable.

## Wertfelder auf die Zeilen- oder Spaltenachse setzen

Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld namens `PivotTable.ValuesField` bereit. Dieses virtuelle Feld stellt das Aggregat jedes Datenfelds dar, das sich im Datenbereich befindet. Sie können es als Basisfeld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Measures nebeneinander anzuordnen.

{{% alert color="primary" %}}
`PivotTable.ValuesField` funktioniert nicht, wenn kein oder nur ein Wertfeld vorhanden ist.
{{% /alert %}}

Die folgenden Szenarien führen durch drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben Pivot-Struktur demonstrieren.

## Szenario 1 — Ziehen eines Basisfelds in den Wertebereich

Dieses Szenario zeigt, wie ein einzelnes Basisfeld (`Amount`) in den Datenbereich einer bestehenden PivotTable eingefügt wird. Die gemeinsame Pivot-Struktur platziert `Category` und `Item` auf der Zeilenachse und `Year` auf der Spaltenachse. Nach der Operation erscheint `Amount` im Datenbereich und wird standardmäßig als `Sum` von `Amount` berechnet.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Überschriften in A1:D1
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

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Szenario 2 — Ändern der Zusammenfassungsfunktion

Dieses Szenario beginnt mit derselben Pivot-Struktur wie Szenario 1, fügt jedoch das Feld `Amount` zweimal zum Datenbereich hinzu. Beide Datenfelder verweisen auf dieselbe Quellspalte, jedoch wird das zweite Feld mit dem `PivotField.Function`-Setter überschrieben, sodass es `Count` anstelle des Standardwerts `Sum` wird.

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

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```

## Szenario 3 — Wertfelder auf die Zeilen- oder Spaltenachse setzen

Mit zwei vorhandenen Datenfeldern wird `PivotTable.ValuesField` nutzbar. Dieses Szenario zieht dieses virtuelle Aggregatfeld in den Spaltenbereich, sodass jedes Measure im Datenbereich als eigener Spaltenblock neben `Year` erscheint.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

Zusammen decken diese drei Szenarien jeden Aspekt der Wertfeldmanipulation in Aspose.Cells for Node.js via C++ ab, von einem einzelnen Datenfeld mit dem Standardwert `Sum` bis zu einer PivotTable mit mehreren Measures, bei der das virtuelle `ValuesField` das Layout auf der Zeilen- oder Spaltenachse steuert.

## Verwandte Artikel

- [Zeilen- und Spaltenfelder in PivotTable in Aspose.Cells for Node.js via C++](/cells/de/nodejs-cpp/row-and-column-fields/)
- [Seitenfelder in PivotTables](/cells/de/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aktualisieren von PivotTables in Aspose.Cells for Node.js via C++](/cells/de/nodejs-cpp/refresh-pivot-table/)
- [Anwenden von Stilen auf PivotTables](/cells/de/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}