---
title: Administrar campos de valor de una tabla dinámica en Aspose.Cells para .NET
linktitle: Campos de valor
description: Aprenda a añadir campos base a la región de datos de una tabla dinámica, cambiar la función de resumen con PivotField.Function, y trazar el campo de valor en el eje de Filas o Columnas en Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, tabla dinámica, campo de valor, PivotField, PivotField.Function, campo de datos, PivotTable.ValuesField, Suma, Promedio
type: docs
weight: 230
url: /es/nodejs-java/pivot-table-manage-value-fields/
/es/nodejs-java/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los campos de valor son el núcleo de cada tabla dinámica, los agregados numéricos que resumen los datos de origen. En Aspose.Cells for Node.js via Java, la región de datos de una tabla dinámica se rellena añadiendo campos base a ella mediante `PivotTable.addFieldToArea`, y cada campo colocado en esa región puede tener su propia función de resumen. Cuando existen dos o más campos de datos, Aspose.Cells expone un campo agregado especial, `PivotTable.getValuesField()`, que se puede trazar en el eje de Filas o Columnas como un campo base, ofreciendo un control más preciso sobre cómo aparecen los campos de valor en el diseño.

## Añadir un Campo a la Región de Datos

Añadir un campo base a la región de datos (valor) es el primer paso para definir cómo una tabla dinámica agrega los datos de origen. Aspose.Cells expone `PivotTable.addFieldToArea(PivotFieldType, string)`, una sobrecarga que acepta la constante `PivotFieldType.DATA` y el nombre de la columna de origen. Una vez que se añade un campo a la región de datos, la API lo expone a través de la colección `PivotTable.getDataFields()`, en el orden en que se añadieron los campos. Por defecto, una columna de origen numérica se resume con `ConsolidationFunction.SUM`, mientras que una columna no numérica toma como valor predeterminado `COUNT`.

## Cambiar la Función de Resumen

Cada campo colocado en la región de datos se envuelve internamente como una instancia de `PivotField`, y su propiedad `getFunction()` devuelve un valor de la enumeración `ConsolidationFunction`. El mismo establecedor `setFunction()` permite cambiar entre los agregados disponibles, incluyendo `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` y `VARP`.

{{% alert color="primary" %}}
Cambiar `Function` solo afecta al agregado, la columna de origen no cambia.
{{% /alert %}}

Por lo tanto, puede dejar un campo de datos como `SUM` mientras añade un segundo campo de datos que tenga como destino la misma columna de origen pero que use `COUNT` o `AVERAGE`, todo en una sola tabla dinámica.

## Trazar Campos de Valor en el Eje de Filas o Columnas

Cuando una tabla dinámica contiene dos o más campos de datos, Aspose.Cells expone un campo virtual adicional llamado `PivotTable.getValuesField()`. Este campo virtual representa el agregado de cada campo de datos que reside en la región de datos. Puede arrastrarlo a la región de Filas o Columnas como un campo dinámico base, lo que resulta útil para disponer varias medidas una al lado de la otra.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` no funciona si no hay ningún campo de valor o solo hay uno.
{{% /alert %}}

Los escenarios a continuación presentan tres ejemplos completos que demuestran cada capacidad descrita anteriormente con la misma estructura de tabla dinámica.

## Escenario 1 — Arrastrar un Campo Base a la Región de Valor

Este escenario muestra cómo poner un único campo base (`Amount`) en la región de datos de una tabla dinámica existente. La estructura compartida de la tabla dinámica coloca `Category` e `Item` en el eje de Filas y `Year` en el eje de Columnas. Tras la operación, `Amount` aparece en la región de datos y se calcula como `Sum` de `Amount` por defecto.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Encabezados en A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Filas de datos A2:D9 usando bucles anidados ramificando en j
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

// Agregar tabla dinámica en F3 con el nombre PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Diseño de tabla dinámica: Category e Item en Fila, Year en Columna, Amount como campo de datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Escenario 2 — Cambiar la Función de Resumen

Este escenario parte de la misma estructura de tabla dinámica que el Escenario 1, pero añade el campo `Amount` a la región de datos dos veces. Ambos campos de datos hacen referencia a la misma columna de origen; sin embargo, el segundo campo se reemplaza mediante el establecedor `PivotField.setFunction()` para que pase a ser `COUNT` en lugar del `SUM` predeterminado.

<!-- CODE_BLOCK:1:Build a complete end-to-end sample that imports the Aspose.Cells namespace, then creates a new Workbook instance, gets worksheets.get(0), assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual cells.get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount") twice so that pivotTable.getDataFields() contains two fields. Retrieve the second data field via pivotTable.getDataFields().get(1) and assign countField.setFunction(ConsolidationFunction.COUNT) to change its summary function from the default SUM to COUNT; the first data field remains Sum of Amount. Demonstrate that the setFunction setter can also be assigned ConsolidationFunction.AVERAGE, MAX, MIN, etc. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_function.xlsx"). -->

## Escenario 3 — Trazar Campos de Valor en el Eje de Filas o Columnas

Con dos campos de datos en su lugar, `PivotTable.getValuesField()` se vuelve utilizable. Este escenario arrastra ese campo virtual agregado a la región de Columnas para que cada medida en la región de datos aparezca como su propio bloque de columna junto a `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that imports the Aspose.Cells namespace, then creates a new Workbook instance, gets worksheets.get(0), assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual cells.get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT) so the second data field becomes COUNT while the first remains SUM. Finally call pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

En conjunto, estos tres escenarios cubren todos los aspectos de la manipulación de campos de valor en Aspose.Cells for Node.js via Java, desde un único campo de datos con el `SUM` predeterminado hasta una tabla dinámica con múltiples medidas en la que el `ValuesField` virtual controla la disposición en el eje de Filas o Columnas.

## Artículos Relacionados

- [Campos de Fila y Columna de Tabla Dinámica en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/row-and-column-fields/)
- [Campos de Página en Tablas Dinámicas](/cells/es/nodejs-java/add-page-field-in-pivot-table/)
- [Actualizar Tablas Dinámicas en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/refresh-pivot-table/)
- [Aplicar Estilos a Tablas Dinámicas](/cells/es/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}