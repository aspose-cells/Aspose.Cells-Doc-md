---
title: Mostrar o filtrar los 10 principales en una tabla dinámica
linktitle: Mostrar o filtrar los 10 principales en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos mejor o peor clasificados de un campo de una tabla dinámica en Aspose.Cells for Node.js mediante Java. Este artículo explica el método Top10AutoShow de Excel 97-2003, cómo leer las opciones con Top10AutoShowSettings y el filtro de los 10 principales de Excel 2007-365 mediante FilterTop10.
keywords: Aspose.Cells, Node.js mediante Java, tabla dinámica, 10 principales, mostrar automáticamente, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /es/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles casos de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede ser difícil de leer cuando el campo contiene decenas de elementos. Un informe de los 10 principales conserva solo los elementos mejor o peor clasificados, justo lo que necesitan los informes de clasificación: «los 5 productos con mayores ingresos» o «las 3 regiones con menor número de ventas». Aspose.Cells admite dos mecanismos para ello, que corresponden a dos generaciones de Microsoft Excel.
- **AutoShow de Excel 97-2003** — el método `PivotField.top10AutoShow()`. Es la configuración clásica «Mostrar los N elementos superiores/inferiores», almacenada directamente en el campo de tabla dinámica. Funciona en todas las versiones de Excel, tanto antiguas como modernas, porque forma parte del formato original de tabla dinámica.
- **Filtro de los 10 principales de Excel 2007-365** — el método `PivotField.filterTop10()`. Es el filtro moderno de valores de los 10 principales disponible en «Filtros de valores» del menú del campo. Se almacena como un objeto `PivotFilter` asociado al campo y permite clasificar por número de elementos o por porcentaje.

## **Mostrar los 10 principales en Excel 97-2003 (Top10AutoShow)**
El AutoShow clásico se configura con una sola llamada a `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — habilita o deshabilita la configuración de AutoShow en el campo.
- `isTop` — `true` conserva los elementos con la clasificación más alta (Superiores), mientras que `false` conserva los de menor clasificación (Inferiores).
- `count` — el número de elementos que se conservan; por ejemplo, 10 para un informe clásico de los 10 principales.
- `rankBy` — el índice basado en cero del **campo de datos** cuyos valores determinan la clasificación de los elementos. Pase -1 para clasificar los elementos por el propio campo.
La clasificación puede determinarse mediante un campo de valores o mediante el propio campo. A continuación se muestran dos variantes habituales.

### **Clasificar según un campo de valores**
Clasifique los elementos del campo de fila por un campo de valores común, como «Suma de ventas». El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`), y luego muestra los dos deportes con más ventas. `rankBy` es 0 porque «Suma de ventas» es el campo de datos situado en el índice 0.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Clasificar según el propio campo**
Un campo también puede clasificarse por sí mismo: pase -1 como `rankBy`. Esta variante no requiere ningún campo de datos adicional; basta con que el campo se encuentre en el área de filas (o columnas). El siguiente ejemplo muestra los tres deportes con la clasificación más baja según el propio campo. Cuando se guarda esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `getTop10AutoShowSettings().getRankBy()` devuelve -1.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Leer las opciones actuales (Top10AutoShowSettings)**
El método `PivotField.getTop10AutoShowSettings()` devuelve un objeto `PivotFieldTop10AutoShowSettings` que expone las opciones de AutoShow almacenadas actualmente en el campo. Utilícelo para comprobar cómo se presentan los elementos de un libro de trabajo existente o de una tabla dinámica recién configurada, incluidos los libros de trabajo cargados desde un archivo.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Los métodos de acceso `isAutoShow()`, `isTop()`, `getAutoShowCount()` y `getRankBy()` se corresponden con los atributos clásicos de AutoShow escritos en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que los valores recuperados se respetarán en todas las versiones de Excel.

## **Nota**

{{% alert color="primary" %}}
- Los métodos de acceso directos de `PivotField` (`isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` y `getAutoShowField()`) están marcados como obsoletos. Utilice en su lugar el objeto `getTop10AutoShowSettings()`: `isAutoShow()` se convierte en `getTop10AutoShowSettings().isAutoShow()`, `isAscendShow()` se convierte en `getTop10AutoShowSettings().isTop()`, `getAutoShowCount()` se convierte en `getTop10AutoShowSettings().getAutoShowCount()` y `getAutoShowField()` se convierte en `getTop10AutoShowSettings().getRankBy()`. El método `top10AutoShow()` es la forma admitida de cambiar la configuración.
- `top10AutoShow()` funciona con campos de fila y de columna. Un campo que solo se encuentre en el área de página (filtro) no se puede clasificar de esta forma porque sus elementos no están distribuidos en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de los 10 principales (FilterTop10)**
Las versiones modernas de Excel permiten aplicar un filtro de valores de los 10 principales desde el menú del campo (Filtros de valores, 10 principales...). Aspose.Cells lo representa mediante el método `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, que devuelve el `PivotFilter` creado:
- `valueFieldIndex` — el índice basado en cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type` — el significado de `itemCount`. `PivotFilterType.COUNT` conserva un número fijo de elementos (la opción Elementos del diálogo). `PivotFilterType.PERCENT` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje: 30 conserva el 30 % de los elementos mejor clasificados. `PivotFilterType.SUM` clasifica los elementos según la cobertura acumulativa de los valores.
- `isTop` — `true` para Superiores, `false` para Inferiores.
- `itemCount` — el valor N en «N principales»; su unidad depende de `type`.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` y `filterTop10()` son dos funcionalidades distintas. AutoShow escribe el atributo clásico `autoShow` en el campo de tabla dinámica y se respeta en todas las versiones de Excel desde Excel 97. `filterTop10()` escribe una entrada `PivotFilter` moderna y requiere Excel 2007 o posterior. Al abrir un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utiliza el filtro moderno recurre a la visualización de todos los elementos. Para los documentos que deben conservarse durante un ciclo de exportación e importación con herramientas heredadas, prefiera `top10AutoShow()`; para los libros de trabajo modernos, prefiera `filterTop10()`, porque se combina con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Agregar campos de fila y de columna a una tabla dinámica](/cells/es/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Agrupar campos de una tabla dinámica](/cells/es/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/nodejs-java/refresh-pivot-table/)
- [Agregar un campo de página a una tabla dinámica](/cells/es/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}