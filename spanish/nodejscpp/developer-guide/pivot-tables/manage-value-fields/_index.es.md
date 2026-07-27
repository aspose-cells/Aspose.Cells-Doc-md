---
title: Administrar campos de valor de una tabla dinámica en Aspose.Cells para .NET
linktitle: Campos de valor
description: Aprenda a añadir campos base a la región de datos de una tabla dinámica, cambie la función de resumen con PivotField.Function y coloque el campo de valor en el eje de fila o columna en Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js via C++, tabla dinámica, campo de valor, PivotField, PivotField.Function, campo de datos, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /es/nodejs-cpp/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Añadir un campo a la región de datos

Añadir un campo base a la región de datos (valor) es el primer paso para dar forma a cómo una tabla dinámica agrega los datos de origen. Aspose.Cells expone `PivotTable.addFieldToArea(PivotFieldType, string)`, una sobrecarga que acepta la constante `PivotFieldType.Data` y el nombre de la columna de origen. Una vez que un campo se añade a la región de datos, la API lo expone a través de la colección `PivotTable.getDataFields()`, en el orden en que se añadieron los campos. Por defecto, una columna de origen numérica se resume con `ConsolidationFunction.Sum`, mientras que una columna no numérica usa `Count` por defecto.

## Cambiar la función de resumen

Cada campo colocado en la región de datos se envuelve internamente como una instancia de `PivotField`, y su propiedad `getFunction()` devuelve un valor de la enumeración `ConsolidationFunction`. El mismo setter `setFunction()` le permite cambiar entre las agregaciones disponibles, incluyendo `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` y `Varp`.

{{% alert color="primary" %}}
Cambiar la función de resumen solo afecta a la agregación, la columna de origen no cambia.
{{% /alert %}}

Por lo tanto, puede dejar un campo de datos como `Sum` mientras añade un segundo campo de datos que apunte a la misma columna de origen pero use `Count` o `Average`, todo en una sola tabla dinámica.

## Colocar campos de valor en el eje de fila o columna

Cuando una tabla dinámica contiene dos o más campos de datos, Aspose.Cells expone un campo virtual adicional llamado `PivotTable.getValuesField`. Este campo virtual representa la agregación de cada campo de datos que reside en la región de datos. Puede arrastrarlo a la región de fila o columna como un campo dinámico base, lo que resulta útil para disponer varias medidas en paralelo.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` no funciona si no hay ningún campo de valor o si solo hay uno.
{{% /alert %}}

Los escenarios a continuación recorren tres ejemplos de extremo a extremo que demuestran cada capacidad descrita anteriormente sobre la misma estructura de tabla dinámica.

## Escenario 1 — Arrastrar un campo base a la región de valor

Este escenario muestra cómo colocar un único campo base (`Amount`) en la región de datos de una tabla dinámica existente. La estructura compartida de la tabla dinámica coloca `Category` e `Item` en el eje de fila y `Year` en el eje de columna. Tras la operación, `Amount` aparece en la región de datos y se calcula como la `Sum` de `Amount` por defecto.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Encabezados en A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Filas de datos A2:D9 usando bucles anidados ramificándose en j
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

// Agregar tabla dinámica en F3 con el nombre PivotTable1
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Diseño de tabla dinámica: Categoría y Elemento en Fila, Año en Columna, Monto como campo de datos
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Escenario 2 — Cambiar la función de resumen

Este escenario parte de la misma estructura de tabla dinámica que el Escenario 1, pero añade el campo `Amount` a la región de datos dos veces. Ambos campos de datos hacen referencia a la misma columna de origen, sin embargo, el segundo campo se anula usando el setter `setFunction()` para que se convierta en `Count` en lugar del `Sum` por defecto.

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

## Escenario 3 — Colocar campos de valor en el eje de fila o columna

Con dos campos de datos en su lugar, `PivotTable.getValuesField()` se vuelve utilizable. Este escenario arrastra ese campo virtual agregado a la región de columna para que cada medida de la región de datos aparezca como su propio bloque de columna junto a `Year`.

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

En conjunto, estos tres escenarios cubren todos los aspectos de la manipulación de campos de valor en Aspose.Cells for Node.js via C++, desde un único campo de datos con el `Sum` por defecto hasta una tabla dinámica con múltiples medidas en la que el `ValuesField` virtual controla el diseño en el eje de fila o columna.

## Artículos relacionados

- [Campos de fila y columna de la tabla dinámica en Aspose.Cells for Node.js via C++](/cells/es/nodejs-cpp/row-and-column-fields/)
- [Campos de página en tablas dinámicas](/cells/es/nodejs-cpp/add-page-field-in-pivot-table/)
- [Actualización de tablas dinámicas en Aspose.Cells for Node.js via C++](/cells/es/nodejs-cpp/refresh-pivot-table/)
- [Aplicar estilos a tablas dinámicas](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}
