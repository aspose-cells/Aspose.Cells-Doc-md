---
title: Agrupación discreta de elementos de campo de tabla dinámica
linktitle: Agrupación discreta
description: Aprenda cómo agrupar elementos de campo de tabla dinámica en grupos con nombres personalizados, como frutas y verduras, usando DiscreteGroupItem y PivotFieldGroupOptions.DiscreteGroupItems en Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, tabla dinámica, agrupación discreta, DiscreteGroupItem, PivotFieldGroupOptions, agrupar elementos de tabla dinámica, grupos personalizados, PivotField.Group, Node.js, tabla dinámica de Excel
type: docs
weight: 90
url: /es/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
- El agrupamiento automático reúne los elementos por tipo de datos, como fechas en meses y trimestres o números en rangos. El agrupamiento discreto resuelve el problema opuesto, reuniendo elementos específicos y no relacionados en grupos con nombres personalizados, por ejemplo productos en frutas y verduras, tiendas en regiones o cuentas en zonas. Aspose.Cells for Node.js via C++ proporciona agrupamiento discreto a través de la clase `DiscreteGroupItem` y la propiedad `PivotFieldGroupOptions.discreteGroupItems`.
- Un `DiscreteGroupItem` es un nombre de grupo más los elementos que le pertenecen. Los elementos pueden identificarse de dos maneras, por sus nombres (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) o por sus posiciones basadas en cero en los datos de origen (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Ambas formas producen el mismo resultado.
- El agrupamiento discreto se aplica a un campo en el área de filas o columnas de la tabla dinámica pasando las opciones a `pivotField.group(pivotFieldGroupOptions)`.

## **Agrupar elementos de campo de tabla dinámica por los nombres de los elementos**
El siguiente ejemplo crea una pequeña lista de ventas (producto, fecha y cantidad), genera una tabla dinámica a partir de ella con `product` en el área de filas, `date` en el área de columnas y `amount` en el área de datos, y luego define dos grupos personalizados por los nombres de los elementos, frutas (grape, cherry) y verduras (carrot, potato). El resultado muestra un diseño de filas de dos niveles, el nombre del grupo como nivel externo y los elementos originales anidados debajo, de modo que las tendencias se pueden leer por grupo personalizado y por elemento.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Después de `calculateData()` el área de filas de la tabla dinámica muestra fruit (grape 50, cherry 80) y vegetable (carrot 60, potato 70) con el total general 260, y las etiquetas de columna mantienen las cuatro fechas (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Agrupar elementos de campo de tabla dinámica por los índices de los elementos**
Cuando los nombres de los elementos son extensos o están localizados, el segundo constructor de `DiscreteGroupItem` identifica los elementos por índice. Los índices son posiciones basadas en cero de los elementos en el orden en que aparecen en los datos de origen, no en orden alfabético. En los datos de muestra anteriores, grape es el elemento 0, carrot el 1, potato el 2 y cherry el 3, por lo que fruit es `{ 0, 3 }` y vegetable es `{ 1, 2 }`. El resultado es idéntico al ejemplo basado en nombres.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Los elementos que no se asignan a ningún grupo personalizado no se pierden. Permanecen en la tabla dinámica al mismo nivel que los grupos personalizados, cada uno como una entrada de un solo elemento. En el ejemplo anterior, definir solo el grupo fruit deja carrot y potato en el área de filas como entradas independientes junto al grupo fruit.
- La propiedad `PivotFieldGroupOptions.newPivotField` controla el diseño del agrupamiento discreto. Por defecto es true, lo que agrega el campo agrupado como un nuevo campo externo junto al original, produciendo el diseño de dos niveles mostrado arriba (`rowFields` crece a 2). Establézcalo en false para reemplazar el campo original; el área de filas mostrará entonces un solo nivel que contiene solo los nombres de los grupos con sus valores agregados, fruit 130 (50 + 80) y vegetable 130 (60 + 70).
- Los constructores basados en nombre y en índice de `DiscreteGroupItem` pueden mezclarse dentro del mismo arreglo `PivotFieldGroupOptions.discreteGroupItems`.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos dinámicos en la tabla dinámica](/cells/es/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Agregar campos de fila y columna en la tabla dinámica](/cells/es/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Aplicar estilo a la tabla dinámica](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)
- [Actualizar tabla dinámica](/cells/es/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}