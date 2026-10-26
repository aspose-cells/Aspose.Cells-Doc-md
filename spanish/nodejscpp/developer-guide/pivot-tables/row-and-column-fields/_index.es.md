---
title: Agregar campos de fila y columna a tablas dinámicas en Aspose.Cells for Node.js mediante C++
linktitle: Agregar campos de fila y columna a tablas dinámicas en Aspose.Cells for Node.js mediante C++
description: Aprenda a agregar campos base a las regiones de filas y columnas de una tabla dinámica y a controlar los subtotales de los campos de la tabla dinámica mediante PivotField.setSubtotals en Aspose.Cells for Node.js mediante C++
keywords: Aspose.Cells, Node.js, C++, tabla dinámica, campo de fila, campo de columna, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotales
type: docs
weight: 220
url: /es/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de filas o columnas**
El método `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` mueve un campo base desde los datos de origen hasta una de las cuatro regiones de la tabla dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.
- `Row` — campos colocados verticalmente a la izquierda
- `Column` — campos colocados horizontalmente en la parte superior
- `Data` — campos cuyos valores se agregan
- `Page` — campos utilizados como filtros del informe
El orden de anidamiento de los campos es importante. Al agregar primero `Category` a la región de filas y luego `Item`, se obtiene una tabla dinámica cuya agrupación exterior es `Category` y cuya agrupación interior es `Item`. Si se invierte el orden, se invierte la jerarquía.

## **Subtotales de campos de tablas dinámicas**
El método `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` controla qué filas de subtotales aparecen para un campo de la tabla dinámica. Cada llamada muestra u oculta un único tipo de subtotal de forma independiente. Al pasar `shown = true`, se muestra el subtotal, mientras que al pasar `shown = false`, se oculta. Como cada llamada solo afecta a un tipo, invocar el método varias veces con distintos valores de `subtotalType` crea un subconjunto personalizado de subtotales.
La enumeración `PivotFieldSubtotalType` define los tipos de subtotales disponibles.
- `Automatic` — Aspose.Cells elige la selección predeterminada (normalmente `Sum` para campos numéricos)
- `None` — suprime todas las filas de subtotales
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Los subtotales solo se muestran cuando hay dos o más campos de tabla dinámica en la región de filas o en la región de columnas. Un solo campo no ofrece una base significativa para calcular subtotales entre grupos, por lo que las llamadas a `setSubtotals` no tienen ningún efecto visible en ese caso. Por ello, este artículo coloca dos campos de fila (`Category` exterior e `Item` interior) en todos los ejemplos para que se vea el límite de cada grupo `Category` en los subtotales.
{{% /alert %}}

## **Escenario 1: subtotales automáticos (predeterminados)**
Cuando no se llama a `setSubtotals` en absoluto, Aspose.Cells aplica la selección `Automatic` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento al llamar a `setSubtotals(PivotFieldSubtotalType.Automatic, true)` en el campo de fila exterior `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Escenario 2: suprimir todos los subtotales (None)**
Al llamar a `setSubtotals(PivotFieldSubtotalType.None, true)`, se eliminan todas las filas de subtotales de la tabla dinámica y solo quedan las filas de campos y el total general en la parte inferior. Esto es útil para obtener los datos agrupados sin filas de resumen.

```javascript
const AsposeCells = require("aspose.cells.node");
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
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Escenario 3: subconjunto personalizado de subtotales (Sum + Average)**
No se limita a un solo tipo de subtotal. Cada llamada a `setSubtotals` afecta de forma independiente a un tipo de subtotal, por lo que llamar al método dos veces —una con `Sum` y otra con `Average`— produce un subconjunto personalizado de dos filas de subtotales para cada grupo `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
let pivotTable = pivotTables.add("A1:D9", 2, 5);
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

## **Resumen**
Los tres escenarios difieren únicamente en una cosa: las llamadas a `setSubtotals`. Todo lo demás —el conjunto de datos, los campos y las áreas a las que se asignan— es idéntico, lo que permite una comparación directa de las disposiciones.
- **Colocación de campos.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` mueve una columna de origen a una región. Dentro de una misma región, el orden de las llamadas determina el orden de visualización, por lo que la primera llamada se convierte en el grupo más externo. Los subtotales requieren dos o más campos en la misma región: con un único campo no hay nada entre los grupos sobre lo cual calcular el subtotal.
- **Escenario 1 — subtotales automáticos.** No invocar `setSubtotals` deja la elección a Excel, que aplica su subtotal predeterminado a los campos numéricos. Invocar `setSubtotals` con `AsposeCells.PivotFieldSubtotalType.Automatic` registra explícitamente dicha elección en lugar de dejarla implícita.
- **Escenario 2 — sin subtotales.** `setSubtotals` con `AsposeCells.PivotFieldSubtotalType.None` desactiva el subtotal predeterminado, de manera que la tabla dinámica conserva las filas de campo y el total general, pero omite las filas de subtotal que Excel insertaría entre ellas.
- **Escenario 3 — un subconjunto elegido.** Cada llamada activa o desactiva exactamente un tipo de subtotal, y las llamadas se acumulan en lugar de resetearse mutuamente. Por lo tanto, invocarlo una vez con `AsposeCells.PivotFieldSubtotalType.Sum` y otra vez con `AsposeCells.PivotFieldSubtotalType.Average` deja ambos habilitados, y la tabla dinámica muestra un subtotal de Suma, un subtotal de Promedio y el total general.

{{% alert color="primary" %}}
Nada acerca de los subtotales es específico de la región de fila. Las mismas llamadas a `setSubtotals` sobre un campo obtenido de `PivotTable.ColumnFields` producen las mismas tres disposiciones en el eje de columna, porque la configuración pertenece al campo de tabla dinámica y no al eje en el que se encuentra.
{{% /alert %}}

## **Artículos relacionados**
- [Campos de página en tablas dinámicas](/cells/es/nodejs-cpp/add-page-field-in-pivot-table/)
- [Actualizar tablas dinámicas en Aspose.Cells for Node.js mediante C++](/cells/es/nodejs-cpp/refresh-pivot-table/)
- [Aplicar estilos a tablas dinámicas](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}