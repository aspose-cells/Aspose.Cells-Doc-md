---
title: "Campos de valor en Aspose.Cells for Node.js via C++"
description: "Aprenda cómo agregar campos base a la región de datos de una tabla dinámica, cambie la función de resumen con PivotField.Function y grafique el campo de valor en el eje de filas o columnas en Aspose.Cells for Node.js via C++."
keywords: "Aspose.Cells, Node.js, C++, tabla dinámica, campo de valor, PivotField, PivotField.Function, campo de datos, PivotTable.ValuesField, Suma, Promedio"
type: docs
weight: 230
url: /es/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Los campos de valor son el corazón de cada tabla dinámica, los agregados numéricos que resumen los datos de origen. En Aspose.Cells for Node.js via C++, la región de datos de una tabla dinámica se rellena agregando campos base mediante `PivotTable.addFieldToArea`, y cada campo colocado en esa región puede tener su propia función de resumen. Cuando existen dos o más campos de datos, Aspose.Cells expone un campo agregado especial, `PivotTable.ValuesField`, que puede graficarse en el eje de filas o columnas como un campo base, brindándole un control más preciso sobre cómo aparecen los campos de valor en el diseño.

## Agregar un campo a la región de datos

Agregar un campo base a la región de datos (valor) es el primer paso para dar forma a cómo una tabla dinámica agrega los datos de origen. Aspose.Cells expone `PivotTable.addFieldToArea(PivotFieldType, string)`, una sobrecarga que acepta la constante `PivotFieldType.Data` y el nombre de la columna de origen. Una vez que se agrega un campo a la región de datos, la API lo expone a través de la colección `PivotTable.DataFields`, en el orden en que se agregaron los campos. De forma predeterminada, una columna de origen numérica se resume con `ConsolidationFunction.Sum`, mientras que una columna no numérica tiene `Count` como valor predeterminado.

## Cambiar la función de resumen

Cada campo colocado en la región de datos se envuelve internamente como una instancia de `PivotField`, y su propiedad `Function` devuelve un valor de la enumeración `ConsolidationFunction`. El mismo establecedor `Function` le permite alternar entre los agregados disponibles, incluidos `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` y `Varp`.

{{% alert color="primary" %}}
Cambiar `Function` solo afecta al agregado, la columna de origen no cambia.
{{% /alert %}}

Por lo tanto, puede dejar un campo de datos como `Sum` mientras agrega un segundo campo de datos que tenga como destino la misma columna de origen pero use `Count` o `Average`, todo en una sola tabla dinámica.

## Graficar campos de valor en el eje de filas o columnas

Cuando una tabla dinámica contiene dos o más campos de datos, Aspose.Cells expone un campo virtual adicional llamado `PivotTable.ValuesField`. Este campo virtual representa el agregado de cada campo de datos que reside en la región de datos. Puede arrastrarlo a la región de filas o columnas como un campo base de la tabla dinámica, lo cual es útil para disponer varias medidas una al lado de la otra.

{{% alert color="primary" %}}
`PivotTable.ValuesField` no funciona si no hay o solo hay un campo de valor.
{{% /alert %}}

Los escenarios a continuación recorren tres ejemplos de extremo a extremo que demuestran cada capacidad descrita anteriormente con la misma estructura de tabla dinámica.

## Escenario 1 — Arrastrar un campo base a la región de valor

Este escenario muestra cómo colocar un único campo base (`Amount`) en la región de datos de una tabla dinámica existente. La estructura compartida de la tabla dinámica coloca `Category` e `Item` en el eje de filas y `Year` en el eje de columnas. Tras la operación, `Amount` aparece en la región de datos y se calcula como la `Sum` de `Amount` de forma predeterminada.

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

// Filas de datos A2:D9 usando bucles anidados con bifurcación en j
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

// Diseño de la tabla dinámica: Category e Item en Fila, Year en Columna, Amount como campo de datos
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Escenario 2 — Cambiar la función de resumen

Este escenario parte de la misma estructura de tabla dinámica que el Escenario 1, pero agrega el campo `Amount` a la región de datos dos veces. Ambos campos de datos hacen referencia a la misma columna de origen; sin embargo, el segundo campo se anula mediante el establecedor `PivotField.Function` para que se convierta en `Count` en lugar del valor predeterminado `Sum`.

<!-- CODE_BLOCK:1:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice so that pivotTable.getDataFields().getCount() equals 2. Retrieve the second data field via pivotTable.getDataFields().get(1) and assign countField.setFunction(ConsolidationFunction.Count) to change its summary function from the default Sum to Count; the first data field remains Sum of Amount. Demonstrate that the Function setter can also be assigned ConsolidationFunction.Average, Max, Min, etc. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_function.xlsx"). -->

## Escenario 3 — Graficar campos de valor en el eje de filas o columnas

Con dos campos de datos en su lugar, `PivotTable.ValuesField` se vuelve utilizable. Este escenario arrastra ese campo virtual agregado a la región de columnas, de modo que cada medida en la región de datos aparece como su propio bloque de columna junto a `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

En conjunto, estos tres escenarios cubren todos los aspectos de la manipulación de campos de valor en Aspose.Cells for Node.js via C++, desde un único campo de datos con el `Sum` predeterminado hasta una tabla dinámica con múltiples medidas en la que el `ValuesField` virtual controla el diseño en el eje de filas o columnas.

## Artículos relacionados

- [Campos de fila y columna de tabla dinámica en Aspose.Cells for Node.js via C++](/cells/es/nodejs-cpp/row-and-column-fields/)
- [Campos de página en tablas dinámicas](/cells/es/nodejs-cpp/add-page-field-in-pivot-table/)
- [Actualización de tablas dinámicas en Aspose.Cells for Node.js via C++](/cells/es/nodejs-cpp/refresh-pivot-table/)
- [Aplicar estilos a tablas dinámicas](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}