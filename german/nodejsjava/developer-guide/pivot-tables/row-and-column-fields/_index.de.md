---
title: Zeilen- und Spaltenfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
linktitle: Zeilen- und Spaltenfelder
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /de/nodejs-java/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**

Die Methode `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Pivot-Bereiche. Das Argument `fieldType` akzeptiert einen der folgenden `PivotFieldType`-Werte.

- `ROW` — Felder, die vertikal auf der linken Seite platziert sind
- `COLUMN` — Felder, die horizontal oben platziert sind
- `DATA` — Felder, deren Werte aggregiert werden
- `PAGE` — Felder, die als Berichtsfilter verwendet werden

Nachdem Felder hinzugefügt wurden, können Sie über die Eigenschaften `PivotTable.getRowFields()` und `PivotTable.getColumnFields()` darauf zugreifen. Jede Eigenschaft gibt eine `PivotFieldCollection` zurück. Das Feld am Index 0 von `RowFields` ist das äußerste Zeilenfeld, und nachfolgende Indizes stehen für darin verschachtelte Felder. Dieselbe Indexierungskonvention gilt für `ColumnFields`.

Die Verschachtelungsreihenfolge der Felder ist wichtig. Wenn zuerst `Category` zum Zeilenbereich und dann `Item` hinzugefügt wird, entsteht eine Pivot-Tabelle, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Durch Umkehren der Reihenfolge wird die Hierarchie umgekehrt.

## **Zwischensummen von Pivot-Feldern**

Die Methode `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` steuert, welche Zwischensummenzeilen für ein Pivot-Feld angezeigt werden. Jeder Aufruf schaltet einen einzelnen Zwischensummentyp unabhängig um. Wenn `shown = true` übergeben wird, wird die Zwischensumme angezeigt, während `shown = false` sie ausblendet. Da jeder Aufruf nur einen Typ betrifft, wird durch mehrmaliges Aufrufen der Methode mit unterschiedlichen `subtotalType`-Werten eine benutzerdefinierte Teilmenge von Zwischensummen erstellt.

Die Enum `PivotFieldSubtotalType` definiert die verfügbaren Zwischensummenarten.

- `AUTOMATIC` — Aspose.Cells wählt die Standardauswahl (typischerweise `SUM` für numerische Felder)
- `NONE` — unterdrückt jede Zwischensummenzeile
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
Zwischensummen werden nur gerendert, wenn sich zwei oder mehr Pivot-Felder im Zeilenbereich (oder im Spaltenbereich) befinden. Für ein einzelnes Feld gibt es nichts Sinnvolles, wofür eine Zwischensumme gebildet werden kann. Daher haben `setSubtotals`-Aufrufe in diesem Fall keine sichtbare Wirkung. Dieser Artikel platziert daher in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Zwischensummengrenze zwischen jeder `Category`-Gruppe sichtbar ist.
{{% /alert %}}

## **Szenario 1 — Automatische (Standard-) Zwischensummen**

Wenn Sie `setSubtotals` überhaupt nicht aufrufen, wendet Aspose.Cells die Auswahl `AUTOMATIC` auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten explizit, indem `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` auf dem äußeren Zeilenfeld `Category` aufgerufen wird.

```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Szenario 2 — Alle Zwischensummen unterdrücken (Keine)**

Der Aufruf von `setSubtotals(PivotFieldSubtotalType.NONE, true)` entfernt jede Zwischensummenzeile aus der Pivot-Tabelle und lässt nur die Feldzeilen und das Gesamtergebnis unten übrig. Dies ist nützlich, wenn Sie die rohen gruppierten Daten ohne zusammenfassende Zeilen wünschen.

```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Szenario 3 — Benutzerdefinierte Zwischensummen-Teilmenge (Summe + Durchschnitt)**

Sie sind nicht auf einen einzelnen Zwischensummentyp beschränkt. Jeder `setSubtotals`-Aufruf wirkt unabhängig auf einen Typ. Wenn die Methode daher zweimal aufgerufen wird — einmal mit `SUM` und einmal mit `AVERAGE` — wird eine benutzerdefinierte Teilmenge von zwei Zwischensummenzeilen für jede `Category`-Gruppe erzeugt.

```javascript
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

Die drei oben genannten Szenarien verwenden denselben Datensatz und dieselbe Pivot-Tabellenstruktur. Der einzige Unterschied zwischen ihnen ist der `setSubtotals`-Aufruf, der auf das äußere Zeilenfeld `Category` angewendet wird. Denken Sie an die Zwei-Felder-Regel: Ein einzelnes Feld in einem Bereich hat keine Möglichkeit zur Zwischensummenbildung dazwischen. Platzieren Sie daher immer mindestens zwei Felder im Zeilen- oder Spaltenbereich, wenn Sie möchten, dass `setSubtotals` eine sichtbare Wirkung hat.

## **Verwandte Artikel**

- [Seitenfelder in Pivot-Tabellen](/cells/de/nodejs-java/add-page-field-in-pivot-table/)
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/nodejs-java/apply-style-to-pivot-table/)
`javascript
```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```
```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```
```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```
```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```
```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```
```javascript
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```

## **Zusammenfassung**

Die drei oben genannten Szenarien verwenden denselben Datensatz und dieselbe Pivot-Tabellenstruktur. Der einzige Unterschied zwischen ihnen ist der `setSubtotals`-Aufruf, der auf das äußere Zeilenfeld `Category` angewendet wird. Denken Sie an die Zwei-Felder-Regel: Ein einzelnes Feld in einem Bereich hat keine sinnvolle Möglichkeit zur Zwischensummenbildung dazwischen. Platzieren Sie daher immer mindestens zwei Felder im Zeilen- oder Spaltenbereich, wenn Sie möchten, dass `setSubtotals` eine sichtbare Wirkung hat.

## **Verwandte Artikel**

- [Seitenfelder in Pivot-Tabellen](/cells/de/nodejs-java/add-page-field-in-pivot-table/)
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
