---
title: Gestire i campi valore di una tabella pivot in Aspose.Cells per .NET
description: Scopri come aggiungere campi di base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.Function e posizionare il campo valore sull'asse Riga o Colonna in Aspose.Cells for Node.js via C++.
linktitle: Campi valore
keywords: Aspose.Cells, Node.js via C++, tabella pivot, campo valore, PivotField, PivotField.Function, campo dati, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /it/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Aggiungere un campo all'area dati
Aggiungere un campo di base all'area dati (valore) è il primo passo per definire come una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.addFieldToArea(PivotFieldType, string)`, un overload che accetta la costante `PivotFieldType.Data` e il nome della colonna di origine. Una volta che un campo viene aggiunto all'area dati, l'API lo espone tramite la raccolta `PivotTable.getDataFields()`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna di origine numerica viene sintetizzata con `ConsolidationFunction.Sum`, mentre una colonna non numerica utilizza `Count` come valore predefinito.

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
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField());
pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

## Modificare la funzione di riepilogo
Ogni campo inserito nell'area dati viene incapsulato internamente come un'istanza di `PivotField`, e la sua proprietà `getFunction()` restituisce un valore dall'enum `ConsolidationFunction`. Lo stesso setter `setFunction()` ti consente di passare tra le aggregazioni disponibili, tra cui `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` e `Varp`.

{{% alert color="primary" %}}
La modifica della funzione di riepilogo influisce solo sull'aggregazione, la colonna di origine non cambia.
{{% /alert %}}

Puoi quindi mantenere un campo dati come `Sum` mentre aggiungi un secondo campo dati che fa riferimento alla stessa colonna di origine ma utilizza `Count` o `Average`, tutto in un'unica pivot.

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
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
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

## Posizionare i campi valore sull'asse Riga o Colonna
Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un ulteriore campo virtuale chiamato `PivotTable.getValuesField`. Questo campo virtuale rappresenta l'aggregazione di ogni campo dati che risiede nell'area dati. Puoi trascinarlo nell'area Riga o Colonna come campo pivot di base, utile per affiancare più misure.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` non funziona se non c'è alcun campo valore o se ne esiste solo uno.
{{% /alert %}}

Gli scenari seguenti illustrano tre esempi end-to-end che dimostrano ciascuna funzionalità descritta sopra applicata alla stessa struttura pivot.

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
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}