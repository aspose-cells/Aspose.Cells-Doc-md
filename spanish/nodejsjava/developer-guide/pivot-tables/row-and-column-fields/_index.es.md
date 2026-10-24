---
title: Agregar campos de fila y columna a una tabla dinámica en Aspose.Cells para .NET
description: Aprenda a agregar campos base a las regiones de fila y columna de una tabla dinámica y a controlar los subtotales de los campos dinámicos mediante PivotField.setSubtotals en Aspose.Cells for Node.js via Java
linktitle: Campos de fila y columna
keywords: Aspose.Cells, Node.js, Java, tabla dinámica, campo de fila, campo de columna, PivotField, setSubtotals, PivotFieldSubtotalType, subtotales
type: docs
weight: 220
url: /es/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de filas o columnas**
El método `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` mueve un campo base desde los datos de origen hacia una de las cuatro regiones de la tabla dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.
- `ROW` — campos colocados verticalmente a la izquierda
- `COLUMN` — campos colocados horizontalmente en la parte superior
- `DATA` — campos cuyos valores se agregan
- `PAGE` — campos utilizados como filtros de informe
Una vez agregados los campos, puede acceder a ellos mediante las propiedades `PivotTable.getRowFields()` y `PivotTable.getColumnFields()`. Cada propiedad devuelve un `PivotFieldCollection`. El campo en el índice 0 de `RowFields` es el campo de fila más externo, y los índices posteriores representan campos anidados dentro de él. La misma convención de indexación se aplica a `ColumnFields`.
El orden de anidamiento de los campos es importante. Agregar `Category` a la región de filas primero y luego `Item` produce una tabla dinámica cuya agrupación externa es `Category` y cuya agrupación interna es `Item`. Invertir el orden invierte la jerarquía.

## **Subtotales de campos dinámicos**
El método `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` controla qué filas de subtotal aparecen para un campo dinámico. Cada llamada activa o desactiva un único tipo de subtotal de forma independiente. Pasar `shown = true` muestra el subtotal, mientras que `shown = false` lo oculta. Dado que cada llamada solo afecta a un tipo, llamar al método varias veces con diferentes valores de `subtotalType` crea un subconjunto personalizado de subtotales.
La enumeración `PivotFieldSubtotalType` define los tipos de subtotal disponibles.
- `AUTOMATIC` — Aspose.Cells elige la selección predeterminada (normalmente `SUM` para campos numéricos)
- `NONE` — suprime toda fila de subtotal
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Los subtotales solo se representan cuando hay dos o más campos dinámicos en la región de filas (o en la región de columnas). Un único campo no tiene nada significativo para calcular subtotales entre grupos, por lo que las llamadas a `setSubtotals` no tienen ningún efecto visible en ese caso. Por lo tanto, este artículo coloca dos campos de fila (`Category` externo, `Item` interno) en cada ejemplo para que el límite de subtotal entre cada grupo `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**
Cuando no llama a `setSubtotals` en absoluto, Aspose.Cells aplica la selección `AUTOMATIC` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento llamando a `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` en el campo de fila externo `Category`.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Escenario 2 — Suprimir todos los subtotales (None)**
Llamar a `setSubtotals(PivotFieldSubtotalType.NONE, true)` elimina todas las filas de subtotal de la tabla dinámica, dejando solo las filas de campo y el total general en la parte inferior. Esto es útil cuando desea los datos agrupados sin procesar sin ninguna fila de resumen.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Escenario 3 — Subconjunto personalizado de subtotales (Sum + Average)**
No está limitado a un único tipo de subtotal. Cada llamada a `setSubtotals` opera de forma independiente en un solo tipo, por lo que llamar al método dos veces — una con `SUM` y otra con `AVERAGE` — produce un subconjunto personalizado de dos filas de subtotal para cada grupo `Category`.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Resumen**

Los tres escenarios difieren únicamente en las llamadas a `setSubtotals`. Todo lo demás —el conjunto de datos, los campos y las áreas a las que se asignan— es idéntico, lo cual permite comparar directamente los diseños.
- **Colocación de campos.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` mueve una columna de origen a una región. Dentro de una misma región, el orden de las llamadas determina el orden de visualización, por lo que la primera llamada corresponde al grupo más externo. Para calcular subtotales se requieren dos o más campos en la misma región: con un único campo no hay nada entre los grupos sobre lo cual calcular el subtotal.
- **Escenario 1 — subtotales automáticos.** Si no se llama a `setSubtotals`, se deja a Excel la decisión, que aplica su subtotal predeterminado automáticamente a los campos numéricos. Llamar a `setSubtotals` con `AsposeCells.PivotFieldSubtotalType.AUTOMATIC` registra explícitamente esa elección en lugar de dejarla implícita.
- **Escenario 2 — sin subtotales.** `setSubtotals` con `AsposeCells.PivotFieldSubtotalType.NONE` desactiva el subtotal predeterminado, de modo que la tabla dinámica conserva las filas de campo y el total general, pero omite las filas de subtotal que Excel insertaría entre ellas.
- **Escenario 3 — un subconjunto elegido.** Cada llamada alterna exactamente un tipo de subtotal, y las llamadas se acumulan en lugar de restablecerse mutuamente. Por tanto, si se llama una vez con `AsposeCells.PivotFieldSubtotalType.SUM` y otra vez con `AsposeCells.PivotFieldSubtotalType.AVERAGE`, ambos se mantienen habilitados, y la tabla dinámica muestra un subtotal de suma, un subtotal de promedio y un total general.

{{% alert color="primary" %}}
Nada acerca de los subtotales es específico de la región de filas. Las mismas llamadas a `setSubtotals` aplicadas a un campo obtenido de `PivotTable.ColumnFields` producen los mismos tres diseños en el eje de columnas, porque la configuración pertenece al campo dinámico y no al eje en el que se encuentra.
{{% /alert %}}
## **Artículos relacionados**

- [Campos de página en tablas dinámicas](/cells/es/nodejs-java/add-page-field-in-pivot-table/)
- [Actualización de tablas dinámicas en Aspose.Cells para Node.js mediante Java](/cells/es/nodejs-java/refresh-pivot-table/)
- [Aplicación de estilos a tablas dinámicas](/cells/es/nodejs-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="nodejs-java" >}}