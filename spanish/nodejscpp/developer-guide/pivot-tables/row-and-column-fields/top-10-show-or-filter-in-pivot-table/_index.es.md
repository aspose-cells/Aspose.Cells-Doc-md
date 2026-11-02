---
title: Mostrar o filtrar los 10 primeros en una tabla dinámica
linktitle: Mostrar o filtrar los 10 primeros en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos con la clasificación más alta o más baja de un campo de tabla dinámica en Aspose.Cells for Node.js mediante C++. Este artículo explica el método Top10AutoShow de Excel 97-2003, cómo leer las opciones con Top10AutoShowSettings y el filtro de los 10 primeros de Excel 2007-365 mediante FilterTop10.
keywords: Aspose.Cells, Node.js mediante C++, tabla dinámica, 10 primeros, visualización automática, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /es/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede resultar difícil de leer cuando el campo contiene decenas de miembros. Un informe de los 10 primeros conserva únicamente los elementos con la clasificación más alta o más baja, que es exactamente lo que necesitan los informes de clasificación: "los 5 productos con mayores ingresos" o "las 3 regiones con menor número de ventas". Aspose.Cells admite dos mecanismos para ello, que corresponden a dos generaciones de Microsoft Excel.
- **Excel 97-2003: visualización automática** — el método `pivotField.top10AutoShow()`. Se trata de la configuración clásica "Mostrar los N elementos superiores/inferiores", almacenada directamente en el campo de tabla dinámica. Funciona en todas las versiones de Excel, antiguas y nuevas, porque forma parte del formato original de las tablas dinámicas.
- **Excel 2007-365: filtro de los 10 primeros** — el método `pivotField.filterTop10()`. Es el filtro moderno de valores de los 10 primeros disponible en "Filtros de valores" del menú del campo. Se almacena como un objeto `PivotFilter` adjunto al campo y ofrece una clasificación basada en el número de elementos o en porcentajes.

## **Mostrar los 10 primeros en Excel 97-2003 (top10AutoShow)**
La visualización automática clásica se configura con una sola llamada a `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)`:
- `isAutoShow` — habilita o deshabilita la configuración de visualización automática en el campo.
- `isTop` — `true` conserva los elementos con la clasificación más alta (Superiores), mientras que `false` conserva los elementos con la clasificación más baja (Inferiores).
- `count` — número de elementos que se conservarán; por ejemplo, 10 para un informe clásico de los 10 primeros.
- `rankBy` — índice de base cero del **campo de datos** cuyos valores determinan la clasificación de los elementos. Pase -1 para clasificar los elementos por el propio campo.
La clasificación puede basarse en un campo de valores o en el propio campo. A continuación se presentan dos variantes habituales.

### **Clasificar por un campo de valores**
Clasifique los elementos de un campo de fila mediante un campo de valores convencional como "Suma de ventas". El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`) y, a continuación, muestra los 2 deportes con mayor volumen de ventas. `rankBy` es 0 porque "Suma de ventas" es el campo de datos en el índice 0.

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Clasificar por el propio campo**
Un campo también puede clasificarse por sí mismo: pase -1 como `rankBy`. Esta variante no requiere ningún campo de datos adicional; basta con que el campo se encuentre en el área de filas (o columnas). El siguiente ejemplo muestra los 3 deportes con la clasificación más baja según el propio campo. Al guardar esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `top10AutoShowSettings.getRankBy()` recupera el valor -1.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Lectura de las opciones actuales (Top10AutoShowSettings)**
El getter `pivotField.getTop10AutoShowSettings()` devuelve un objeto `PivotFieldTop10AutoShowSettings` que expone las opciones de visualización automática almacenadas actualmente en el campo. Utilícelo para comprobar cómo se presentan los elementos de una tabla dinámica en un libro de trabajo existente o recién configurado, incluidos los libros de trabajo cargados desde un archivo.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Las cuatro propiedades se corresponden con los atributos clásicos de visualización automática escritos en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que todas las versiones de Excel respetarán los valores leídos.

## **Nota**

{{% alert color="primary" %}}
- Los getters directos de `PivotField` (`isAutoShow`, `getIsAscendShow()`, `getAutoShowCount()` y `getAutoShowField()`) están marcados como obsoletos. En su lugar, utilice el objeto `Top10AutoShowSettings`: `pivotField.isAutoShow` se sustituye por `top10AutoShowSettings.isAutoShow`, `pivotField.getIsAscendShow()` se sustituye por `top10AutoShowSettings.isTop`, `pivotField.getAutoShowCount()` se sustituye por `top10AutoShowSettings.getAutoShowCount()` y `pivotField.getAutoShowField()` se sustituye por `top10AutoShowSettings.getRankBy()`. El propio método `pivotField.top10AutoShow()` es la forma admitida de cambiar la configuración.
- `top10AutoShow()` funciona con campos de fila y de columna. Un campo que se encuentre únicamente en el área de página (filtro) no se puede clasificar de esta manera porque sus elementos no se colocan en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de los 10 primeros (filterTop10)**
Las versiones modernas de Excel ofrecen un filtro de valores de los 10 primeros en el menú del campo ("Filtros de valores", "Los 10 primeros..."). Aspose.Cells lo modela con el método `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)`, que devuelve el objeto `PivotFilter` creado:
- `valueFieldIndex` — índice de base cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type` — determina el significado de `itemCount`. `PivotFilterType.Count` conserva un número fijo de elementos (la opción "Elementos" del diálogo). `PivotFilterType.Percent` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje: 30 conserva el 30 % de los elementos mejor clasificados. `PivotFilterType.SUM` clasifica según la cobertura acumulada del valor.
- `isTop` — `true` para Superiores, `false` para Inferiores.
- `itemCount` — cantidad N que representa el filtro; su unidad depende de `type`.

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` y `filterTop10` son dos funcionalidades distintas. La visualización automática escribe en el campo de tabla dinámica el conjunto clásico de atributos que incluye `autoShow` y es respetada en todas las versiones de Excel desde Excel 97. `filterTop10` escribe una entrada moderna de tipo `PivotFilter`, que requiere Excel 2007 o posterior. Al abrir un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utilice el filtro moderno vuelve a mostrar todos los elementos. Para los documentos que deban procesarse de ida y vuelta con herramientas heredadas, prefiera `top10AutoShow`; para los libros de trabajo modernos, prefiera `filterTop10` porque se combina con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Agregar campos de fila y columna a una tabla dinámica](/cells/es/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Agrupar campos de la tabla dinámica](/cells/es/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/nodejs-cpp/refresh-pivot-table/)
- [Agregar un campo de página a una tabla dinámica](/cells/es/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}