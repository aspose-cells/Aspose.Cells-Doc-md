---
title: Wertfelder einer PivotTable in Aspose.Cells für .NET verwalten
linktitle: Wertfelder
description: Erfahren Sie, wie Sie Basisfelder zum Datenbereich einer PivotTable hinzufügen, die Zusammenfassungsfunktion mit PivotField.Function ändern und das Wertfeld auf die Zeilen- oder Spaltenachse in Aspose.Cells for .NET ablegen.
keywords: Aspose.Cells, .NET, PivotTable, Wertfeld, PivotField, PivotField.Function, Datenfeld, PivotTable.ValuesField, Summe, Mittelwert
type: docs
weight: 230
url: /de/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Hinzufügen eines Felds zum Datenbereich
Das Hinzufügen eines Basisfelds zum Daten- (Wert-)Bereich ist der erste Schritt bei der Gestaltung der Aggregation Ihrer Quelldaten durch eine PivotTable. Aspose.Cells stellt `PivotTable.AddFieldToArea(PivotFieldType, string)` bereit, eine Überladung, die die Konstante `PivotFieldType.Data` und den Namen der Quellspalte akzeptiert. Sobald ein Feld zum Datenbereich hinzugefügt wurde, stellt die API es über die Auflistung `PivotTable.DataFields` in der Reihenfolge bereit, in der die Felder hinzugefügt wurden. Standardmäßig wird eine numerische Quellspalte mit `ConsolidationFunction.Sum` zusammengefasst, während eine nicht-numerische Spalte standardmäßig `Count` verwendet.
## Ändern der Zusammenfassungsfunktion
Jedes im Datenbereich platzierte Feld wird intern als `PivotField`-Instanz gekapselt, und seine `Function`-Eigenschaft gibt einen Wert aus der Enumeration `ConsolidationFunction` zurück. Mit demselben `Function`-Setter können Sie zwischen den verfügbaren Aggregaten wechseln, einschließlich `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` und `Varp`.
{{% alert color="primary" %}}
Das Ändern von `Function` wirkt sich nur auf das Aggregat aus, die Quellspalte ändert sich nicht.
{{% /alert %}}
Sie können daher ein Datenfeld als `Sum` belassen, während Sie ein zweites Datenfeld hinzufügen, das auf dieselbe Quellspalte abzielt, aber `Count` oder `Average` verwendet, alles in einer einzigen PivotTable.
## Wertfelder auf die Zeilen- oder Spaltenachse ablegen
Wenn eine PivotTable zwei oder mehr Datenfelder enthält, stellt Aspose.Cells ein zusätzliches virtuelles Feld mit der Bezeichnung `PivotTable.ValuesField` bereit. Dieses virtuelle Feld repräsentiert das Aggregat jedes Datenfelds, das sich im Datenbereich befindet. Sie können es als Basis-Pivot-Feld in den Zeilen- oder Spaltenbereich ziehen, was nützlich ist, um mehrere Measures nebeneinander anzuordnen.
{{% alert color="primary" %}}
`PivotTable.ValuesField` funktioniert nicht, wenn kein oder nur ein Wertfeld vorhanden ist.
{{% /alert %}}
Die folgenden Szenarien führen durch drei durchgängige Beispiele, die jede der oben beschriebenen Funktionen anhand derselben Pivot-Struktur demonstrieren.
## Szenario 1 — Ziehen eines Basisfelds in den Wertebereich
Dieses Szenario zeigt, wie ein einzelnes Basisfeld (`Amount`) in den Datenbereich einer vorhandenen PivotTable eingefügt wird. Die gemeinsame Pivot-Struktur platziert `Category` und `Item` auf der Zeilenachse und `Year` auf der Spaltenachse. Nach der Operation erscheint `Amount` im Datenbereich und wird standardmäßig als `Sum` von `Amount` berechnet.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Kopfzeilen in A1:D1
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

// Datenzeilen A2:D9 mit verschachtelten Schleifen, die nach j verzweigen
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.Cells[i, j].PutValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.Cells[i, j].PutValue("Apple");
 else if (i == 3 || i == 4) worksheet.Cells[i, j].PutValue("Banana");
 else if (i == 5 || i == 6) worksheet.Cells[i, j].PutValue("Carrot");
 else worksheet.Cells[i, j].PutValue("Daikon");
 break;
 case 2:
 worksheet.Cells[i, j].PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.Cells[i, j].PutValue(100);
 else if (i == 2) worksheet.Cells[i, j].PutValue(150);
 else if (i == 3) worksheet.Cells[i, j].PutValue(80);
 else if (i == 4) worksheet.Cells[i, j].PutValue(90);
 else if (i == 5) worksheet.Cells[i, j].PutValue(50);
 else if (i == 6) worksheet.Cells[i, j].PutValue(60);
 else if (i == 7) worksheet.Cells[i, j].PutValue(40);
 else worksheet.Cells[i, j].PutValue(45);
 break;
 }
 }
}

// Pivot-Tabelle bei F3 mit dem Namen PivotTable1 hinzufügen
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Pivot-Layout: Kategorie und Element in Zeile, Jahr in Spalte, Betrag als Datenfeld
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```
## Szenario 2 — Ändern der Zusammenfassungsfunktion
Dieses Szenario beginnt mit derselben Pivot-Struktur wie Szenario 1, fügt jedoch das Feld `Amount` zweimal zum Datenbereich hinzu. Beide Datenfelder verweisen auf dieselbe Quellspalte, jedoch wird das zweite Feld mithilfe des `PivotField.Function`-Setters überschrieben, sodass es `Count` anstelle der Standardeinstellung `Sum` wird.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.Cells[i, j].PutValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
 worksheet.Cells[i, j].PutValue(items[i - 1]);
 }
 else if (j == 2)
 {
 int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
 worksheet.Cells[i, j].PutValue(years[i - 1]);
 }
 else
 {
 int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };
 worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");

pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;

pivotTable.CalculateData();

workbook.Save("output_function.xlsx");
```
## Szenario 3 — Wertfelder auf die Zeilen- oder Spaltenachse ablegen
Wenn zwei Datenfelder vorhanden sind, wird `PivotTable.ValuesField` nutzbar. Dieses Szenario zieht dieses aggregierte virtuelle Feld in den Spaltenbereich, sodass jedes Measure im Datenbereich als eigener Spaltenblock neben `Year` angezeigt wird.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

string[] categories = { "Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable" };
string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.Cells[i, j].PutValue(categories[i - 1]);
 else if (j == 1) worksheet.Cells[i, j].PutValue(items[i - 1]);
 else if (j == 2) worksheet.Cells[i, j].PutValue(years[i - 1]);
 else worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.DataFields[1].Function = ConsolidationFunction.Count;

pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);

pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```
Zusammengenommen decken diese drei Szenarien jeden Aspekt der Wertfeldmanipulation in Aspose.Cells for .NET ab, von einem einzelnen Datenfeld mit der Standardeinstellung `Sum` bis zu einer PivotTable mit mehreren Measures, in der das virtuelle Feld `ValuesField` das Layout auf der Zeilen- oder Spaltenachse steuert.

{{< app/cells/assistant language="csharp" >}}
