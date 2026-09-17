---
title: Filtrar tablas dinámicas por etiqueta o valor
description: Aspose.Cells for Java ofrece completas capacidades de filtrado de tablas dinámicas. Este artículo explica cómo filtrar los datos de una tabla dinámica usando filtros de etiqueta, filtros de fecha, filtros de valor, filtros de los 10 mejores y ocultando o mostrando elementos de la tabla dinámica.
linktitle: Filtrar tablas dinámicas por etiqueta o valor
keywords: Aspose.Cells, biblioteca de Java, hoja de cálculo, tabla dinámica, filtro, filtro de etiqueta, filtro de valor, filtro de fecha, filtro de los 10 mejores, elemento de tabla dinámica, ocultar elemento de tabla dinámica
type: docs
weight: 10
url: /es/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos que se muestran en una tabla dinámica. Puede aplicar filtros de etiqueta a los campos de fila o columna basados en texto, usar filtros de fecha cuando el campo contenga solo celdas de fecha y hora o estén en blanco, aplicar filtros de valor frente a números agregados, usar filtros de los 10 mejores para clasificar por un campo de valor, u ocultar y mostrar manualmente elementos individuales de la tabla dinámica usando la propiedad `IsHidden`. Cada estrategia se expone a través de API dedicadas en las clases `PivotField` y `PivotItem`.
{{% /alert %}}

## **Introducción**
Las tablas dinámicas son potentes herramientas de análisis, pero los resúmenes sin procesar a menudo contienen mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe específico. Aspose.Cells for Java refleja las capacidades de filtrado disponibles en Microsoft Excel, exponiéndolas mediante programación para que la generación de informes pueda automatizarse por completo.
Las siguientes estrategias de filtrado se tratan en este artículo:
1. **Filtro de etiqueta** — filtra los elementos de los campos de fila o columna según sus etiquetas de texto.
2. **Filtro de fecha** — filtra campos de fila o columna que solo contienen valores de fecha y hora (o están en blanco).
3. **Filtro de valor** — filtra elementos según los valores agregados de un campo de datos.
4. **Filtro de los 10 mejores** — muestra solo los N elementos superiores o inferiores clasificados por un campo de valor.
5. **Ocultar / Mostrar elementos de la tabla dinámica** — controla manualmente la visibilidad de cada elemento individual en un campo.
Cada enfoque utiliza un método diferente en la clase `PivotField` o una propiedad en la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `refreshData()` y `calculateData()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**
Un filtro de etiqueta permite filtrar los elementos de un campo de fila o columna comparando sus rótulos de texto con un patrón. Esto resulta útil cuando desea mostrar solo los productos cuyos nombres comienzan con una letra específica, contienen una palabra concreta o cumplen algún otro criterio basado en el rótulo.
Aspose.Cells expone el filtrado por etiqueta mediante el método `PivotField.filterByLabel(PivotFilterType, String)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.
El siguiente ejemplo carga un libro que contiene una tabla dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyos rótulos comiencen con un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.refreshData();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Filtro de fecha**
Los filtros de fecha permiten reducir una tabla dinámica según criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un rango de fechas específico. Son filtros especializados que solo funcionan con campos que almacenan información de fecha y hora.

{{% alert color="primary" %}}
El filtro de fecha solo funciona cuando el área de fila o columna contiene exclusivamente celdas de fecha y hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo esté formateado como fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.
{{% /alert %}}

Aspose.Cells expone el filtrado por fecha mediante el método `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha dedicados como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Según el tipo de filtro elegido, se pasan uno o dos valores de `DateTime` (para `Between`, se pasan las fechas de inicio y fin).
El siguiente ejemplo carga un libro con una tabla dinámica cuya área de fila contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un rango de fechas concreto, actualiza la tabla dinámica y guarda el libro.

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.refreshData();
// Persist the workbook
workbook.save(outputPath);
```

## **Filtro de valor**
Los filtros de valor operan sobre los valores agregados que calcula una tabla dinámica en su área de datos. En lugar de comparar rótulos de texto, comparan totales numéricos con un umbral. Entre los casos de uso típicos se incluyen mostrar solo los productos cuya suma de ventas supere una cantidad objetivo o solo las regiones cuyo número de transacciones se encuentre dentro de un rango.
Aspose.Cells expone el filtrado por valor mediante el método `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos debe evaluarse, y los argumentos finales proporcionan los valores umbral.
El siguiente ejemplo carga un libro con una tabla dinámica, aplica un filtro de valor que conserva solo los elementos cuyas ventas agregadas superan un umbral numérico, actualiza la tabla dinámica y guarda el libro.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}
pivotTable.refreshData();
workbook.save("output.xlsx");
```

## **Filtro de los 10 mejores**
El filtro de los 10 mejores es una forma especializada de filtro de valor que conserva solo los N elementos superiores o inferiores según un campo de valor elegido. Se usa comúnmente en informes de clasificación, como "los 10 productos principales por ingresos" o "las 5 regiones inferiores por número de ventas".

{{% alert color="primary" %}}
El filtro de los 10 mejores solo es efectivo cuando la tabla dinámica tiene uno o varios campos de valor en el área de datos. Sin al menos un campo de valor, no existe ninguna medida agregada para clasificar los elementos y el filtro no puede aplicarse.
{{% /alert %}}

Aspose.Cells expone el filtrado de los 10 mejores mediante el método `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. El parámetro `itemCount` define cuántos elementos se deben conservar, `isTop` indica si se conservan los elementos superiores (true) o inferiores (false), `valueField` hace referencia al campo de datos utilizado para la clasificación y `filterType` controla cómo se calcula el valor (normalmente `Sum`, pero también `Count` y `Percent`).
El siguiente ejemplo carga un libro con una tabla dinámica que contiene un campo de valor, aplica un filtro de los 10 mejores para conservar solo los 10 elementos superiores según la suma de ventas, actualiza la tabla dinámica y guarda el libro.

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.refreshData();
// Save the workbook
workbook.save(outputPath);
```

## **Filtrar ocultando o mostrando elementos de la tabla dinámica**
Además de las API estructuradas de filtrado, Aspose.Cells permite controlar directamente la visibilidad de cada elemento individual de la tabla dinámica. Al iterar a través de la colección `PivotItems` de un `PivotField` y alternar la propiedad `IsHidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `IsHidden = true` oculta el elemento de la tabla dinámica; establecer `IsHidden = false` lo muestra y lo hace visible nuevamente.
Este enfoque resulta útil cuando la regla de filtrado es irregular o específica de un elemento, como ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe concreto. El siguiente ejemplo carga una tabla dinámica, oculta un elemento específico por nombre, muestra cómo volver a hacerlo visible, actualiza la tabla dinámica y guarda el libro.

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.refreshData();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Resumen**
Aspose.Cells for Java ofrece un conjunto completo de capacidades de filtrado de tablas dinámicas que coinciden con las disponibles en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 mejores gestiona los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible a nivel de elemento. Combinar estas estrategias —por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos— le permite generar informes de tablas dinámicas con gran precisión completamente desde código.

## Artículos relacionados
- [Insertar tabla dinámica](/cells/es/java/pivot-tables/)
- [Agregar campos de fila y columna a una tabla dinámica en Aspose.Cells for Java](/cells/es/java/pivot-table-add-row-and-column-fields/)
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for Java](/cells/es/java/add-page-field-in-pivot-table/)
- [Administrar campos de valor de una tabla dinámica en Aspose.Cells for Java](/cells/es/java/manage-value-fields/)
- [Actualizar tablas dinámicas y cachés de tablas dinámicas en Aspose.Cells for Java](/cells/es/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}