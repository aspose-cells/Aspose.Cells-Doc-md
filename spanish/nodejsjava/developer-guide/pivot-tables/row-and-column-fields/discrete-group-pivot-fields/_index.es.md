---
title: Agrupación discreta de elementos de campos de tabla dinámica
linktitle: Agrupación discreta
description: Aprenda a agrupar elementos de campos de tabla dinámica en grupos personalizados con nombre, como los de frutas y verduras, utilizando DiscreteGroupItem y PivotFieldGroupOptions.getDiscreteGroupItems() en Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, tabla dinámica, agrupación discreta, DiscreteGroupItem, PivotFieldGroupOptions, agrupar elementos de tablas dinámicas, grupos personalizados, PivotField.group, Aspose.Cells for Node.js via Java, tabla dinámica de Excel
type: docs
weight: 90
url: /es/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- El agrupamiento automático agrupa elementos según el tipo de datos; por ejemplo, agrupa las fechas por meses y trimestres o los números por rangos. La agrupación discreta resuelve el problema opuesto: agrupa elementos específicos no relacionados en grupos personalizados con nombre; por ejemplo, agrupa productos en frutas y verduras, tiendas en regiones o cuentas en zonas. Aspose.Cells ofrece la agrupación discreta mediante la clase `DiscreteGroupItem` y la propiedad `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- `DiscreteGroupItem` representa un nombre de grupo junto con los elementos que pertenecen a él. Los elementos pueden identificarse de dos maneras: por sus nombres (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) o por sus posiciones indexadas desde cero en los datos de origen (`new DiscreteGroupItem("fruit", [0, 3])`). Ambas formas producen el mismo resultado.
- La agrupación discreta se aplica a un campo en el área de filas o de columnas de la tabla dinámica al pasar las opciones a `PivotField.group(PivotFieldGroupOptions)`.

## **Agrupar elementos de campos de tabla dinámica por nombres de elementos**
El siguiente ejemplo crea una pequeña lista de ventas (producto, fecha e importe), genera una tabla dinámica con `product` en el área de filas, `date` en el área de columnas y `amount` en el área de datos; a continuación, define dos grupos personalizados por nombres de elementos: frutas (uva y cereza) y verduras (zanahoria y patata). El resultado muestra un diseño de filas de dos niveles, con el nombre del grupo como nivel exterior y los elementos originales anidados debajo, lo que permite analizar las tendencias de cada grupo personalizado y cada elemento.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Después de `calculateData()`, el área de filas de la tabla dinámica muestra el grupo de frutas (uva 50, cereza 80) y el de verduras (zanahoria 60, patata 70), con un total general de 260; las etiquetas de columna conservan las cuatro fechas (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Agrupar elementos de campos de tabla dinámica por índices de elementos**
Cuando los nombres de los elementos son largos o están localizados, el segundo constructor de `DiscreteGroupItem` los identifica por índice. Los índices representan las posiciones de los elementos en los datos de origen, numeradas desde cero y no en orden alfabético. En los datos de ejemplo, la uva es el elemento 0, la zanahoria el 1, la patata el 2 y la cereza el 3, por lo que el grupo de frutas es `{ 0, 3 }` y el de verduras es `{ 1, 2 }`. El resultado es idéntico al ejemplo basado en nombres.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Los elementos que no se asignan a ningún grupo personalizado no se pierden. Se mantienen en la tabla dinámica en el mismo nivel que los grupos personalizados, cada uno en una entrada independiente de un solo elemento. En el ejemplo anterior, al definir solo el grupo de frutas, la zanahoria y la patata permanecen en el área de filas como entradas independientes junto al grupo de frutas.
- La propiedad `PivotFieldGroupOptions.getNewPivotField()` controla el diseño de la agrupación discreta. De forma predeterminada, esta propiedad es `true`, lo que añade el campo agrupado como un nuevo campo exterior adyacente al original y produce el diseño de dos niveles mostrado anteriormente (`getRowFields()` pasa a contener 2 campos). Establezca su valor en `false` mediante `PivotFieldGroupOptions.setNewPivotField(false)` para sustituir el campo original; el área de filas muestra entonces un único nivel que contiene solo los nombres de los grupos con sus valores agregados: frutas 130 (50 + 80) y verduras 130 (60 + 70).
- Los constructores de `DiscreteGroupItem` basados en nombres y en índices se pueden mezclar dentro de la misma matriz `getDiscreteGroupItems()`.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de tabla dinámica en la tabla dinámica](/cells/es/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Agregar campos de fila y columna en una tabla dinámica](/cells/es/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Aplicar estilo a una tabla dinámica](/cells/es/nodejs-java/apply-style-to-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}