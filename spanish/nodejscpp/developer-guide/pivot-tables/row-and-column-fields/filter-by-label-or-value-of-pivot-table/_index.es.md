---
title: Filtrar tablas dinámicas por etiqueta o valor
description: Aspose.Cells for Node.js via C++ admite capacidades completas de filtrado de tablas dinámicas. Este artículo explica cómo filtrar los datos de una tabla dinámica usando filtros de etiqueta, filtros de fecha, filtros de valor, filtros top 10, y mediante ocultar o mostrar elementos dinámicos.
linktitle: Filtrar tablas dinámicas por etiqueta o valor
keywords: Aspose.Cells, Node.js via C++ library, hoja de cálculo, tabla dinámica, filtro, filtro de etiqueta, filtro de valor, filtro de fecha, filtro top 10, elemento dinámico, ocultar elemento dinámico
type: docs
weight: 10
url: /es/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una tabla dinámica. Puede aplicar filtros de etiqueta a campos de fila o columna basados en texto, usar filtros de fecha cuando el campo solo contenga celdas de fecha-hora o espacios en blanco, aplicar filtros de valor contra números agregados, usar filtros top 10 para clasificar por un campo de valor, u ocultar y mostrar manualmente elementos dinámicos individuales usando la propiedad `IsHidden`. Cada estrategia se expone a través de API dedicadas en las clases `PivotField` y `PivotItem`.
{{% /alert %}}

## **Introducción**
Las tablas dinámicas son herramientas analíticas poderosas, pero los resúmenes sin procesar a menudo contienen mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe específico. Aspose.Cells for Node.js via C++ replica las capacidades de filtrado disponibles en Microsoft Excel, exponiéndolas mediante programación para que la generación de informes pueda automatizarse por completo.
Las siguientes estrategias de filtrado se cubren en este artículo:
1. **Filtro de etiqueta** — filtra los elementos de un campo de fila o columna según sus etiquetas de texto.
2. **Filtro de fecha** — filtra campos de fila o columna que contienen solo valores de fecha-hora (o espacios en blanco).
3. **Filtro de valor** — filtra elementos según los valores agregados de un campo de datos.
4. **Filtro Top 10** — muestra solo los N elementos superiores o inferiores clasificados por un campo de valor.
5. **Ocultar / Mostrar elementos dinámicos** — controla manualmente la visibilidad de cada elemento individual en un campo.
Cada enfoque utiliza un método diferente en la clase `PivotField` o una propiedad en la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `getPivotCache().refresh()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**
Un filtro de etiqueta le permite filtrar los elementos de un campo de fila o columna comparando sus leyendas de texto con un patrón. Esto resulta útil cuando desea mostrar solo productos cuyos nombres comiencen con una letra específica, contengan una palabra particular o coincidan con algún otro criterio basado en leyendas.
Aspose.Cells expone el filtrado por etiqueta a través del método `PivotField.filterByLabel(PivotFilterType, string)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.
El siguiente ejemplo carga un libro que contiene una tabla dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyas leyendas comiencen con un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```javascript
const AsposeCells = require("aspose.cells.node");
let fileName = "sample.xlsx";
let prefix = "B";
// Load the existing workbook containing a pivot table
let workbook = new AsposeCells.Workbook(fileName);
// Access the worksheet by index (first worksheet)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
let rowField = pivotTable.getRowFields().get(0);
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Filtro de fecha**
Los filtros de fecha le permiten reducir una tabla dinámica según criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un rango de fechas específico. Son filtros especializados que funcionan solo contra campos que almacenan información de fecha-hora.

{{% alert color="primary" %}}
El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de fecha-hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo tenga formato de fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.
Aspose.Cells expone el filtrado por fecha a través del método `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha dedicados como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Según el tipo de filtro elegido, pasa uno o dos valores `DateTime` (para `Between`, pasa las fechas de inicio y fin).
El siguiente ejemplo carga un libro con una tabla dinámica cuyo área de fila contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un rango de fechas particular, actualiza la tabla dinámica y guarda el libro.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");
const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
const workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
const worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
const pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
const dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Filtro de valor**
Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de coincidir con etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar solo productos cuya suma de ventas supere una cantidad objetivo, o solo regiones cuyo número de transacciones se encuentre dentro de un rango.
Aspose.Cells expone el filtrado por valor a través del método `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos se debe evaluar, y el argumento o argumentos finales proporcionan el valor o valores umbral.
El siguiente ejemplo carga un libro con una tabla dinámica, aplica un filtro de valor que conserva solo los elementos cuyas ventas agregadas superan un umbral numérico, actualiza la tabla dinámica y guarda el libro.

```javascript
const AsposeCells = require("aspose.cells.node");
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Filtro Top 10**
El filtro top 10 es una forma especializada de filtro de valor que retiene solo los N elementos más altos o más bajos según un campo de valor elegido. Se usa comúnmente para informes de clasificación como "los 10 productos principales por ingresos" o "las 5 regiones inferiores por número de ventas".

{{% alert color="primary" %}}
El filtro top 10 solo es efectivo cuando la tabla dinámica tiene uno o más campos de valor en el área de datos. Sin al menos un campo de valor, no hay ninguna medida agregada contra la cual clasificar los elementos, y el filtro no se puede aplicar.
Aspose.Cells expone el filtrado Top 10 mediante el método `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. El parámetro `valueFieldIndex` es el índice del campo de datos cuyos valores agregados clasifican los elementos, `filterType` selecciona la unidad de `itemCount` (`PivotFilterType.Count` conserva un número fijo de elementos, `PivotFilterType.Percent` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje), `isTop` indica si se conservan los elementos superiores (true) o los inferiores (false), y `itemCount` define cuántos elementos, o qué porcentaje, conservar.
El siguiente ejemplo carga un libro con una tabla dinámica que contiene un campo de valor, aplica un filtro top 10 para conservar solo los 10 elementos más altos por la suma de ventas, actualiza la tabla dinámica y guarda el libro.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
// Load the existing workbook that contains the pivot table
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
const worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
const pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
const rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
const valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtrar ocultando o mostrando elementos dinámicos**
Además de las API estructuradas de filtrado, Aspose.Cells le permite controlar la visibilidad de cada elemento dinámico individual directamente. Al iterar por la colección `PivotItems` de un `PivotField` y alternar la propiedad `IsHidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `IsHidden = true` oculta el elemento de la tabla dinámica; establecer `IsHidden = false` lo muestra nuevamente y lo hace visible de nuevo.
Este enfoque resulta útil cuando la regla de filtrado es irregular o específica de un elemento, como ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe particular. El siguiente ejemplo carga una tabla dinámica, oculta un elemento específico por nombre, muestra cómo volver a mostrarlo, actualiza la tabla dinámica y guarda el libro.

```javascript
const AsposeCells = require("aspose.cells.node");
// Load an existing workbook containing a pivot table
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
const sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
const pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
const pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Resumen**
Aspose.Cells for Node.js via C++ proporciona un conjunto completo de capacidades de filtrado de tablas dinámicas que coinciden con las que se encuentran en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro top 10 gestiona los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible a nivel de elemento. La combinación de estas estrategias (por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos) le permite construir informes de tablas dinámicas dirigidos con precisión totalmente desde código.

{{< app/cells/assistant language="nodejs-cpp" >}}