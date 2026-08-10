---
title: Campi Valore in Aspose.Cells for Node.js via Java
linktitle: Campi Valore
description: Scopri come aggiungere campi base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.Function e posizionare il campo valore sull'asse Riga o Colonna in Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, tabella pivot, campo valore, PivotField, PivotField.Function, campo dati, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /it/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

I campi valore sono il cuore di ogni tabella pivot, le aggregazioni numeriche che riepilogano i dati di origine. In Aspose.Cells for Node.js via Java, l'area dati di una tabella pivot viene popolata aggiungendovi campi base tramite `PivotTable.addFieldToArea`, e ogni campo posizionato in tale area può avere la propria funzione di riepilogo. Quando esistono due o più campi dati, Aspose.Cells espone uno speciale campo aggregato, `PivotTable.getValuesField()`, che può essere posizionato sull'asse Riga o Colonna come campo base, offrendoti un controllo più preciso su come i campi valore appaiono nel layout.

## Aggiunta di un Campo all'Area Dati

L'aggiunta di un campo base all'area dati (valore) è il primo passo per definire come una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.addFieldToArea(PivotFieldType, string)`, un overload che accetta la costante `PivotFieldType.DATA` e il nome della colonna di origine. Una volta aggiunto un campo all'area dati, l'API lo espone tramite la raccolta `PivotTable.getDataFields()`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna di origine numerica viene riepilogata con `ConsolidationFunction.SUM`, mentre una colonna non numerica utilizza `COUNT` come impostazione predefinita.

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

## Modifica della Funzione di Riepilogo

Ogni campo posizionato nell'area dati viene incapsulato internamente come istanza di `PivotField` e la sua proprietà `getFunction()` restituisce un valore dall'enumerazione `ConsolidationFunction`. Lo stesso setter `setFunction()` consente di passare tra gli aggregati disponibili, inclusi `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` e `VARP`.

{{% alert color="primary" %}}
La modifica di `Function` influisce solo sull'aggregato, la colonna di origine non cambia.
{{% /alert %}}

È quindi possibile lasciare un campo dati come `SUM` mentre si aggiunge un secondo campo dati che fa riferimento alla stessa colonna di origine ma utilizza `COUNT` o `AVERAGE`, il tutto in un'unica tabella pivot.

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

## Posizionamento dei Campi Valore sull'Asse Riga o Colonna

Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un ulteriore campo virtuale chiamato `PivotTable.getValuesField()`. Questo campo virtuale rappresenta l'aggregato di ogni campo dati presente nell'area dati. È possibile trascinarlo nell'area Riga o Colonna come campo pivot base, utile per disporre più misure affiancate.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` non funziona se non è presente alcun campo valore o se ne è presente solo uno.
{{% /alert %}}

Gli scenari seguenti illustrano tre esempi end-to-end che dimostrano ciascuna capacità descritta sopra sulla stessa struttura di tabella pivot.

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

{{< app/cells/assistant language="javascript" >}}