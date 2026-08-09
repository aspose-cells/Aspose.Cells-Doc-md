---
title: Värdefält i Aspose.Cells for Node.js via Java
linktitle: Värdefält i Aspose.Cells for Node.js via Java
description: Lär dig hur du lägger till basfält i dataregionen i en pivottabell, ändrar summeringsfunktionen med PivotField.Function och placerar värdefältet på rad- eller kolumnaxeln i Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, pivottabell, värdefält, PivotField, PivotField.Function, datafält, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /sv/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Värdefält är kärnan i varje pivottabell, de numeriska aggregaten som sammanfattar källdatan. I Aspose.Cells for Node.js via Java fylls dataregionen i en pivottabell genom att basfält läggs till den via `PivotTable.addFieldToArea`, och varje fält som placeras i den regionen kan ha en egen summeringsfunktion. När det finns två eller flera datafält exponerar Aspose.Cells ett särskilt aggregatfält, `PivotTable.getValuesField()`, som kan placeras på rad- eller kolumnaxeln som ett basfält, vilket ger dig finare kontroll över hur värdefält visas i layouten.

## Lägga till ett fält i dataregionen

Att lägga till ett basfält i data- (värde-) regionen är det första steget för att forma hur en pivottabell aggregerar din källdata. Aspose.Cells exponerar `PivotTable.addFieldToArea(PivotFieldType, string)`, en överlagring som accepterar konstanten `PivotFieldType.DATA` och källkolonnens namn. När ett fält har lagts till i dataregionen exponerar API:et det genom samlingen `PivotTable.getDataFields()`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.SUM`, medan en icke-numerisk kolumn som standard blir `COUNT`.

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

## Ändra summeringsfunktionen

Varje fält som placeras i dataregionen wrappas internt som en `PivotField`-instans, och dess `getFunction()`-egenskap returnerar ett värde från `ConsolidationFunction`-enumen. Samma `setFunction()`-setter låter dig växla mellan tillgängliga aggregat, inklusive `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` och `VARP`.

{{% alert color="primary" %}}Att ändra `Function` påverkar bara aggregatet, källkolumnen ändras inte.{{% /alert %}}

Du kan alltså låta ett datafält vara `SUM` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `COUNT` eller `AVERAGE`, allt i en enda pivot.

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

## Placera värdefält på rad- eller kolumnaxeln

När en pivottabell innehåller två eller flera datafält exponerar Aspose.Cells ytterligare ett virtuellt fält som kallas `PivotTable.getValuesField()`. Detta virtuella fält representerar aggregatet av varje datafält som finns i dataregionen. Du kan dra det till rad- eller kolumnregionen som ett baspivotfält, vilket är användbart för att lägga ut flera mått sida vid sida.

{{% alert color="primary" %}}`PivotTable.getValuesField()` fungerar inte om det inte finns något eller bara ett värdefält.{{% /alert %}}

Scenarierna nedan går igenom tre kompletta exempel som demonstrerar varje funktion som beskrivs ovan mot samma pivotstruktur.

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