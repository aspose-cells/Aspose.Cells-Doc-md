---
title: Filtrado de Tablas Dinámicas por etiqueta o valor
description: Aspose.Cells for Java ofrece capacidades completas de filtrado de Tabla Dinámica. Este artículo explica cómo filtrar los datos de una Tabla Dinámica usando filtros de etiqueta, filtros de fecha, filtros de valor y filtros de los 10 principales, además de cómo ocultar o mostrar elementos de Tabla Dinámica.
linktitle: Filtrado de Tablas Dinámicas por etiqueta o valor
keywords: Aspose.Cells, biblioteca Java, hoja de cálculo, Tabla Dinámica, filtro, filtro por etiqueta, filtro por valor, filtro de fecha, filtro de los 10 principales, elemento de Tabla Dinámica, ocultar elemento de Tabla Dinámica
type: docs
weight: 10
url: /es/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una Tabla Dinámica. Puede aplicar filtros de etiqueta a campos de fila o columna basados en texto, utilizar filtros de fecha cuando el campo contenga únicamente celdas de fecha y hora o valores en blanco, aplicar filtros de valor a números agregados, utilizar filtros de los 10 principales para clasificar según un campo de valor u ocultar y mostrar manualmente elementos individuales de la Tabla Dinámica mediante la propiedad `IsHidden`. Cada estrategia se expone mediante API específicas en las clases `PivotField` y `PivotItem`.
{{% /alert %}}

## **Introducción**
Las Tablas Dinámicas son herramientas analíticas potentes, pero los resúmenes sin procesar suelen contener mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una Tabla Dinámica a las filas, columnas o valores que son importantes para un informe concreto. Aspose.Cells for Java reproduce las capacidades de filtrado disponibles en Microsoft Excel y las expone mediante programación para que la generación de informes pueda automatizarse por completo.
En este artículo se cubren las siguientes estrategias de filtrado:
1. **Filtro por etiqueta** — filtra los elementos de un campo de fila o columna según sus etiquetas de texto.
2. **Filtro de fecha** — filtra campos de fila o columna que contengan únicamente valores de fecha y hora, o valores en blanco.
3. **Filtro por valor** — filtra elementos según los valores agregados de un campo de datos.
4. **Filtro de los 10 principales** — muestra únicamente los N elementos con los valores más altos o más bajos según un campo de valor.
5. **Ocultar / Mostrar elementos de Tabla Dinámica** — controla manualmente la visibilidad de cada elemento individual de un campo.
Cada enfoque utiliza un método diferente de la clase `PivotField` o una propiedad de la clase `PivotItem`. Tras aplicar cualquier filtro, debe llamar a `getPivotCache().refresh()` en la Tabla Dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro por etiqueta**
Un filtro por etiqueta permite filtrar los elementos de un campo de fila o columna comparando sus rótulos de texto con un patrón. Esto resulta útil cuando desea mostrar únicamente productos cuyos nombres comiencen por una letra concreta, contengan una palabra determinada o coincidan con cualquier otro criterio basado en rótulos.
Aspose.Cells expone el filtrado por etiqueta mediante el método `PivotField.filterByLabel(PivotFilterType, String)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.
El siguiente ejemplo carga un libro de trabajo que contiene una Tabla Dinámica existente, aplica un filtro por etiqueta para que solo permanezcan visibles los elementos cuyos rótulos comiencen por un prefijo especificado, actualiza la Tabla Dinámica y guarda el resultado.

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
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Filtro de fecha**
Los filtros de fecha permiten reducir una Tabla Dinámica según criterios temporales como hoy, la semana pasada, este mes, el próximo trimestre o un intervalo de fechas concreto. Son filtros especializados que solo funcionan con campos que almacenan información de fecha y hora.

{{% alert color="primary" %}}
El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de fecha y hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo tenga formato de fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.
Aspose.Cells expone el filtrado por fecha mediante el método `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha específicos como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Según el tipo de filtro seleccionado, se pasan uno o dos valores `DateTime`; para `Between`, se pasan las fechas de inicio y fin.
El siguiente ejemplo carga un libro de trabajo con una Tabla Dinámica cuyo área de fila contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un intervalo de fechas concreto, actualiza la Tabla Dinámica y guarda el libro de trabajo.
{{% /alert %}}

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
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Filtro por valor**
Los filtros por valor operan sobre los valores agregados que calcula una Tabla Dinámica en su área de datos. En lugar de coincidir con etiquetas de texto, comparan totales numéricos con un umbral. Entre los casos de uso habituales se encuentran mostrar únicamente productos cuya suma de ventas supere un importe objetivo o solo regiones cuyo número de transacciones se sitúe dentro de un intervalo.
Aspose.Cells expone el filtrado por valor mediante el método `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos se debe evaluar y los argumentos finales proporcionan los valores de umbral.
El siguiente ejemplo carga un libro de trabajo con una Tabla Dinámica, aplica un filtro por valor que conserva únicamente los elementos cuyas ventas agregadas superen un umbral numérico, actualiza la Tabla Dinámica y guarda el libro de trabajo.

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
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Filtro de los 10 principales**
El filtro de los 10 principales es una forma especializada de filtro por valor que conserva únicamente los N elementos con los valores más altos o más bajos según un campo de valor seleccionado. Se utiliza habitualmente para generar informes de clasificación como "los 10 principales productos por ingresos" o "las 5 regiones inferiores por número de ventas".

{{% alert color="primary" %}}
El filtro de los 10 principales solo es eficaz cuando la Tabla Dinámica tiene uno o más campos de valor en el área de datos. Sin al menos un campo de valor, no existe ninguna medida agregada respecto a la cual clasificar los elementos y el filtro no puede aplicarse.
Aspose.Cells expone el filtrado de los 10 principales mediante el método `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)`. El parámetro `valueFieldIndex` es el índice del campo de datos cuyos valores agregados se utilizan para clasificar los elementos; `filterType` selecciona la unidad de `itemCount` (`PivotFilterType.COUNT` conserva un número fijo de elementos, mientras que `PivotFilterType.PERCENT` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje); `isTop` indica si se conservan los elementos superiores (`true`) o los inferiores (`false`); y `itemCount` define cuántos elementos, o qué porcentaje, se conservan.
El siguiente ejemplo carga un libro de trabajo con una Tabla Dinámica que contiene un campo de valor, aplica un filtro de los 10 principales para conservar únicamente los 10 elementos con la mayor suma de ventas, actualiza la Tabla Dinámica y guarda el libro de trabajo.
{{% /alert %}}

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
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filtrado mediante la ocultación o exibição de elementos de Tabla Dinámica**
Además de las API de filtrado estructurado, Aspose.Cells permite controlar directamente la visibilidad de cada elemento individual de una Tabla Dinámica. Al recorrer la colección `PivotItems` de un `PivotField` y cambiar el valor de la propiedad `IsHidden`, puede suprimir de forma selectiva elementos concretos sin aplicar un filtro basado en fórmulas. Establecer `IsHidden = true` oculta el elemento de la Tabla Dinámica; establecer `IsHidden = false` lo muestra de nuevo y vuelve a hacerlo visible.
Este enfoque resulta útil cuando la regla de filtrado es irregular o específica de cada elemento, por ejemplo, para ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe concreto. El siguiente ejemplo carga una Tabla Dinámica, oculta un elemento concreto por nombre, demuestra cómo volver a mostrarlo, actualiza la Tabla Dinámica y guarda el libro de trabajo.

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
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Resumen**
Aspose.Cells for Java proporciona un conjunto completo de capacidades de filtrado de Tabla Dinámica que coinciden con las disponibles en Microsoft Excel. Los filtros por etiqueta, de fecha y por valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 principales se ocupa de los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible al nivel de cada elemento. La combinación de estas estrategias —por ejemplo, aplicar un filtro por etiqueta y después ocultar elementos concretos— permite crear informes de Tabla Dinámica con una segmentación precisa, todo mediante código.

## Artículos relacionados
- [Insertar una Tabla Dinámica](/cells/es/java/create-pivot-table/)
- [Agregar campos de fila y columna de una Tabla Dinámica en Aspose.Cells for Java](/cells/es/java/pivot-table-add-row-and-column-fields/)
- [Agregar campos de filtro a una Tabla Dinámica en Aspose.Cells for Java](/cells/es/java/add-page-field-in-pivot-table/)
- [Administrar campos de valor de una Tabla Dinámica en Aspose.Cells for Java](/cells/es/java/manage-value-fields/)
- [Actualizar Tablas Dinámicas y sus cachés en Aspose.Cells for Java](/cells/es/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}