---
title: Filtrar tablas dinámicas por etiqueta o valor
description: Aspose.Cells for Node.js via Java admite capacidades completas de filtrado de tablas dinámicas. Este artículo explica cómo filtrar datos de tablas dinámicas mediante filtros de etiqueta, filtros de fecha, filtros de valor, filtros de los 10 mejores y ocultando o mostrando elementos dinámicos.
linktitle: Filtrar por etiqueta o valor
url: /es/nodejs-java/filter-by-label-or-value-of-pivot-table/
keywords: Aspose.Cells, biblioteca Node.js via Java, hoja de cálculo, tabla dinámica, filtro, filtro de etiqueta, filtro de valor, filtro de fecha, filtro de los 10 mejores, elemento dinámico, ocultar elemento dinámico
type: docs
weight: 10
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una tabla dinámica. Puede aplicar filtros de etiqueta a campos de fila o columna basados en texto, usar filtros de fecha cuando el campo solo contenga celdas de fecha-hora o espacios en blanco, aplicar filtros de valor contra números agregados, usar filtros de los 10 mejores para clasificar por un campo de valor, u ocultar y mostrar manualmente elementos dinámicos individuales utilizando la propiedad `IsHidden`. Cada estrategia se expone mediante API dedicadas en las clases `PivotField` y `PivotItem`.
{{% /alert %}}

## **Introducción**
Las tablas dinámicas son potentes herramientas de análisis, pero los resúmenes sin procesar a menudo contienen mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe específico. Aspose.Cells for Node.js via Java replica las capacidades de filtrado disponibles en Microsoft Excel, exponiéndolas mediante programación para que la generación de informes pueda automatizarse por completo.
Las siguientes estrategias de filtrado se tratan en este artículo:
1. **Filtro de etiqueta** — filtra los elementos de un campo de fila o columna según sus etiquetas de texto.
2. **Filtro de fecha** — filtra campos de fila o columna que solo contienen valores de fecha-hora (o espacios en blanco).
3. **Filtro de valor** — filtra elementos según los valores agregados de un campo de datos.
4. **Filtro de los 10 mejores** — muestra solo los N elementos superiores o inferiores clasificados por un campo de valor.
5. **Ocultar/Mostrar elementos dinámicos** — controla manualmente la visibilidad de cada elemento individual en un campo.
Cada enfoque utiliza un método diferente en la clase `PivotField` o una propiedad en la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `getPivotCache().refresh()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**
Un filtro de etiqueta le permite filtrar los elementos de un campo de fila o columna comparando sus títulos de texto con un patrón. Esto resulta útil cuando desea mostrar solo los productos cuyos nombres comiencen con una letra específica, contengan una palabra particular o coincidan con algún otro criterio basado en el título.
Aspose.Cells expone el filtrado por etiqueta mediante el método `PivotField.filterByLabel(PivotFilterType, string)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.
El siguiente ejemplo carga un libro que contiene una tabla dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyas etiquetas comiencen con un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```javascript
const AsposeCells = require("aspose.cells");
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
rowField.filterByLabel(AsposeCells.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Filtro de fecha**
Los filtros de fecha le permiten reducir una tabla dinámica según criterios basados en fechas como hoy, la semana pasada, este mes, el próximo trimestre o un rango de fechas específico. Son filtros especializados que solo funcionan contra campos que almacenan información de fecha-hora.

{{% alert color="primary" %}}
El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de fecha-hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo esté formateado como fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.
Aspose.Cells expone el filtrado por fecha mediante el método `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha dedicados como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, y `Between`. Según el tipo de filtro elegido, pasa uno o dos valores `DateTime` (para `Between`, pasa las fechas de inicio y fin).
El siguiente ejemplo carga un libro con una tabla dinámica cuya área de fila contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un rango de fechas particular, actualiza la tabla dinámica y guarda el libro.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
var pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
let dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Filtro de valor**
Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de coincidir con etiquetas de texto, comparan totales numéricos contra un umbral. Los casos de uso típicos incluyen mostrar solo productos cuya suma de ventas supere una cantidad objetivo o solo regiones cuyo recuento de transacciones esté dentro de un rango.
Aspose.Cells expone el filtrado por valor mediante el método `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos debe evaluarse, y los argumentos finales proporcionan los valores umbral.
El siguiente ejemplo carga un libro con una tabla dinámica, aplica un filtro de valor que mantiene solo los elementos cuyas ventas agregadas superen un umbral numérico, actualiza la tabla dinámica y guarda el libro.

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);
var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.VALUE_GREATER_THAN, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Filtro de los 10 mejores**
El filtro de los 10 mejores es una forma especializada de filtro de valor que retiene solo los N elementos superiores o inferiores según un campo de valor elegido. Se usa comúnmente para informes de clasificación como "los 10 mejores productos por ingresos" o "las 5 regiones inferiores por recuento de ventas".

{{% alert color="primary" %}}
El filtro de los 10 mejores solo es efectivo cuando la tabla dinámica tiene uno o más campos dinámicos de valor en el área de datos. Sin al menos un campo de valor, no hay ninguna medida agregada contra la cual clasificar los elementos, y no se puede aplicar el filtro.
Aspose.Cells expone el filtrado Top 10 mediante el método `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)`. El parámetro `valueFieldIndex` es el índice del campo de datos cuyos valores agregados clasifican los elementos, `filterType` selecciona la unidad de `itemCount` (`PivotFilterType.COUNT` conserva un número fijo de elementos, `PivotFilterType.PERCENT` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje), `isTop` indica si se conservan los elementos superiores (true) o los inferiores (false), y `itemCount` define cuántos elementos, o qué porcentaje, conservar.
El siguiente ejemplo carga un libro con una tabla dinámica que contiene un campo de valor, aplica un filtro de los 10 mejores para mantener solo los 10 elementos superiores por la suma de ventas, actualiza la tabla dinámica y guarda el libro.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
let rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
let valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtrar ocultando o mostrando elementos dinámicos**
Además de las API de filtros estructurados, Aspose.Cells le permite controlar directamente la visibilidad de cada elemento dinámico individual. Al iterar a través de la colección `PivotItems` de un `PivotField` y alternar la propiedad `IsHidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `IsHidden = true` oculta el elemento de la tabla dinámica; establecer `IsHidden = false` lo muestra nuevamente y lo hace visible de nuevo.
Este enfoque es útil cuando la regla de filtrado es irregular o específica de un elemento, como ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe particular. El siguiente ejemplo carga una tabla dinámica, oculta un elemento específico por nombre, demuestra cómo mostrarlo nuevamente, actualiza la tabla dinámica y guarda el libro.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
let sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
let pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
let pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3") {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Resumen**
Aspose.Cells for Node.js via Java proporciona un conjunto completo de capacidades de filtrado de tablas dinámicas que coinciden con las que se encuentran en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 mejores maneja los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible a nivel de elemento. Combinar estas estrategias —por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos— le permite construir informes de tablas dinámicas específicamente dirigidos completamente desde código.

{{< app/cells/assistant language="nodejs-java" >}}