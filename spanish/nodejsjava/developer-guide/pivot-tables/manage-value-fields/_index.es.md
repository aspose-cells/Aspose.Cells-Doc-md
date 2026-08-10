---
title: Campos de Valor en Aspose.Cells for Node.js via Java
linktitle: Campos de Valor en Aspose.Cells for Node.js via Java
description: Aprenda a añadir campos base a la región de datos de una tabla dinámica, cambie la función de resumen con PivotField.Function y coloque el campo de valor en el eje de fila o columna en Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, tabla dinámica, campo de valor, PivotField, PivotField.Function, campo de datos, PivotTable.ValuesField, Suma, Promedio
type: docs
weight: 230
url: /es/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los campos de valor son el corazón de toda tabla dinámica, los agregados numéricos que resumen los datos de origen. En Aspose.Cells for Node.js via Java, la región de datos de una tabla dinámica se completa añadiendo campos base a ella mediante `PivotTable.addFieldToArea`, y cada campo colocado en esa región puede tener su propia función de resumen. Cuando existen dos o más campos de datos, Aspose.Cells expone un campo agregado especial, `PivotTable.getValuesField()`, que puede colocarse en el eje de fila o columna como un campo base, brindándole un control más preciso sobre cómo aparecen los campos de valor en el diseño.

## Agregar un Campo a la Región de Datos

Añadir un campo base a la región de datos (valor) es el primer paso para dar forma a cómo una tabla dinámica agrega los datos de origen. Aspose.Cells expone `PivotTable.addFieldToArea(PivotFieldType, string)`, una sobrecarga que acepta la constante `PivotFieldType.DATA` y el nombre de la columna de origen. Una vez que se añade un campo a la región de datos, la API lo expone a través de la colección `PivotTable.getDataFields()`, en el orden en que se añadieron los campos. Por defecto, una columna de origen numérica se resume con `ConsolidationFunction.SUM`, mientras que una columna no numérica toma como valor predeterminado `COUNT`.

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

## Cambiar la Función de Resumen

Cada campo colocado en la región de datos se envuelve internamente como una instancia de `PivotField`, y su propiedad `getFunction()` devuelve un valor de la enumeración `ConsolidationFunction`. El mismo setter `setFunction()` le permite cambiar entre los agregados disponibles, incluyendo `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` y `VARP`.

{{% alert color="primary" %}}
Cambiar `Function` solo afecta al agregado; la columna de origen no cambia.
{{% /alert %}}

Por lo tanto, puede dejar un campo de datos como `SUM` mientras añade un segundo campo de datos que tenga como destino la misma columna de origen pero que use `COUNT` o `AVERAGE`, todo en una sola tabla dinámica.

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

## Trazar Campos de Valor en el Eje de Filas o Columnas

Cuando una tabla dinámica contiene dos o más campos de datos, Aspose.Cells expone un campo virtual adicional llamado `PivotTable.getValuesField()`. Este campo virtual representa el agregado de cada campo de datos que reside en la región de datos. Puede arrastrarlo a la región de Filas o Columnas como un campo dinámico base, lo cual resulta útil para disponer varias medidas una al lado de la otra.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` no funciona si no hay ningún campo de valor o si solo hay uno.
{{% /alert %}}

Los escenarios siguientes recorren tres ejemplos de extremo a extremo que demuestran cada capacidad descrita anteriormente contra la misma estructura dinámica.

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