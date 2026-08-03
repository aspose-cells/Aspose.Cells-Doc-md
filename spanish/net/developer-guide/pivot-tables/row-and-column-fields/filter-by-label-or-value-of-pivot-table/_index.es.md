---
title: Filtrado de tablas dinámicas por etiqueta o valor
linktitle: Filtrado de tablas dinámicas por etiqueta o valor
description: Aspose.Cells for .NET ofrece capacidades completas de filtrado de tablas dinámicas. Este artículo explica cómo filtrar datos de tablas dinámicas mediante filtros de etiqueta, filtros de fecha, filtros de valor, filtros de los 10 mejores, y ocultando o mostrando elementos dinámicos.
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, tabla dinámica, filtro, filtro de etiqueta, filtro de valor, filtro de fecha, filtro de los 10 mejores, elemento dinámico, ocultar elemento dinámico
type: docs
weight: 10
url: /es/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una tabla dinámica. Puede aplicar filtros de etiqueta a campos de fila o columna basados en texto, usar filtros de fecha cuando el campo contenga solo celdas de fecha-hora o en blanco, aplicar filtros de valor contra números agregados, usar filtros de los 10 mejores para clasificar por un campo de valor, u ocultar y mostrar manualmente elementos dinámicos individuales mediante la propiedad `IsHidden`. Cada estrategia se expone a través de API dedicadas en las clases `PivotField` y `PivotItem`.

{{% /alert %}}

## **Introducción**

Las tablas dinámicas son potentes herramientas analíticas, pero los resúmenes sin procesar suelen contener mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe específico. Aspose.Cells for .NET refleja las capacidades de filtrado disponibles en Microsoft Excel, exponiéndolas mediante programación para que la generación de informes pueda automatizarse completamente.

Las siguientes estrategias de filtrado se tratan en este artículo:

1. **Filtro de etiqueta** — filtra los elementos de campos de fila o columna según sus etiquetas de texto.
2. **Filtro de fecha** — filtra campos de fila o columna que contienen solo valores de fecha-hora (o en blanco).
3. **Filtro de valor** — filtra elementos según los valores agregados de un campo de datos.
4. **Filtro de los 10 mejores** — muestra solo los N elementos superiores o inferiores clasificados por un campo de valor.
5. **Ocultar / Mostrar elementos dinámicos** — controla manualmente la visibilidad de cada elemento individual en un campo.

Cada enfoque utiliza un método diferente en la clase `PivotField` o una propiedad en la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `RefreshData()` y `CalculateData()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**

Un filtro de etiqueta le permite filtrar los elementos de un campo de fila o columna comparando sus títulos de texto con un patrón. Esto resulta útil cuando desea mostrar solo productos cuyos nombres comiencen con una letra específica, contengan una palabra concreta o coincidan con algún otro criterio basado en títulos.

Aspose.Cells expone el filtrado por etiqueta mediante el método `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.

El siguiente ejemplo carga un libro que contiene una tabla dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyos títulos comiencen con un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string fileName = "sample.xlsx";
string prefix = "B";

// Cargar el libro de trabajo existente que contiene una tabla dinámica
Workbook workbook = new Workbook(fileName);

// Acceder a la hoja de trabajo por índice (primera hoja de trabajo)
Worksheet worksheet = workbook.Worksheets[0];

// Acceder a la tabla dinámica por índice
PivotTable pivotTable = worksheet.PivotTables[0];

// Obtener el primer PivotField de fila
PivotField rowField = pivotTable.RowFields[0];

// Aplicar el filtro de etiqueta — mostrar solo los elementos de fila cuyas etiquetas comiencen con el prefijo proporcionado
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);

// Refrescar y recalcular los datos de la tabla dinámica para que el filtro surta efecto
pivotTable.PivotCache.Refresh();

// Guardar el libro de trabajo de nuevo en disco
workbook.Save(fileName);
```

## **Filtro de fecha**

Los filtros de fecha le permiten reducir una tabla dinámica según criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un rango de fechas específico. Son filtros especializados que funcionan solo contra campos que almacenan información de fecha-hora.

{{% alert color="primary" %}}

El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de fecha-hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo esté formateado como fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.

{{% /alert %}}

Aspose.Cells expone el filtrado por fecha mediante el método `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha dedicados como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Según el tipo de filtro elegido, pasa uno o dos valores `DateTime` (para `Between`, pasa las fechas de inicio y fin).

El siguiente ejemplo carga un libro con una tabla dinámica cuya área de fila contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un rango de fechas particular, actualiza la tabla dinámica y guarda el libro.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";

if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}

// Cargar el libro existente que contiene la tabla dinámica
var workbook = new Workbook(inputPath);

// Acceder a la hoja de cálculo que contiene la tabla dinámica (por índice)
var worksheet = workbook.Worksheets[0];

// Acceder a la tabla dinámica por índice
var pivotTable = worksheet.PivotTables[0];

// Obtener el PivotField de fecha del área de filas
// (El filtro de fecha solo funciona cuando el área de filas/columnas contiene solo celdas de fecha-hora o espacios en blanco)
PivotField dateField = pivotTable.RowFields[0];

// Definir el criterio de fecha para el filtro Between
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Aplicar el filtro de fecha en el campo dinámico
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);

// Actualizar y recalcular la tabla dinámica para que el filtro surta efecto
pivotTable.PivotCache.Refresh();

// Guardar el libro
workbook.Save(outputPath);
```

## **Filtro de valor**

Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de hacer coincidir etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar solo productos cuya suma de ventas supere una cantidad objetivo o solo regiones cuyo número de transacciones se encuentre dentro de un rango.

Aspose.Cells expone el filtrado por valor mediante el método `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos debe evaluarse, y los argumentos finales proporcionan el valor o valores umbral.

El siguiente ejemplo carga un libro con una tabla dinámica, aplica un filtro de valor que conserva solo los elementos cuyas ventas agregadas superen un umbral numérico, actualiza la tabla dinámica y guarda el libro.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];

var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];

// Encontrar el índice del campo de datos manualmente ya que PivotFieldCollection no tiene IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}

pivotTable.PivotCache.Refresh();

workbook.Save("output.xlsx");
```

## **Filtro de los 10 mejores**

El filtro de los 10 mejores es una forma especializada de filtro de valor que conserva solo los N elementos superiores o inferiores según un campo de valor elegido. Se usa habitualmente para informes de clasificación como «los 10 productos principales por ingresos» o «las 5 regiones inferiores por número de ventas».

{{% alert color="primary" %}}

El filtro de los 10 mejores solo es efectivo cuando la tabla dinámica tiene uno o más campos dinámicos de valor en el área de datos. Sin al menos un campo de valor, no hay ninguna medida agregada con la que clasificar los elementos y el filtro no puede aplicarse.

{{% /alert %}}

Aspose.Cells expone el filtrado de los 10 mejores mediante el método `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)`. El parámetro `itemCount` define cuántos elementos se deben conservar, `isTop` indica si se conservan los elementos superiores (true) o los inferiores (false), `valueField` hace referencia al campo de datos utilizado para la clasificación, y `filterType` controla cómo se calcula el valor (normalmente `Sum`, pero también `Count` y `Percent`).

El siguiente ejemplo carga un libro con una tabla dinámica que contiene un campo de valor, aplica un filtro de los 10 mejores para conservar solo los 10 elementos superiores según la suma de ventas, actualiza la tabla dinámica y guarda el libro.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Cargar el libro de trabajo existente que contiene la tabla dinámica
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Acceder a la hoja de trabajo que contiene la tabla dinámica (índice 0)
Worksheet worksheet = workbook.Worksheets[0];

// Acceder a la tabla dinámica por índice
PivotTable pivotTable = worksheet.PivotTables[0];

// Confirmar que hay al menos un PivotField de valor en el área de datos
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];

// Recuperar el PivotField de fila objetivo (el campo al que queremos aplicar Top 10)
PivotField rowField = pivotTable.RowFields[0];

// El primer (y único) campo de datos está en el índice 0; Top 10 clasifica por él.
int valueFieldIndex = 0;

// Aplicar el filtro Top 10 en el campo de fila:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false significaría bottom N)
//   - valueFieldIndex = el índice del campo de datos utilizado para clasificar los elementos
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);

// Actualizar los datos de la tabla dinámica y recalcular para que el filtro surta efecto
pivotTable.PivotCache.Refresh();

// Guardar el libro de trabajo
workbook.Save(outputPath);
```

## **Filtrar ocultando o mostrando elementos dinámicos**

Además de las API de filtros estructurados, Aspose.Cells le permite controlar directamente la visibilidad de cada elemento dinámico individual. Al recorrer en iteración la colección `PivotItems` de un `PivotField` y alternar la propiedad `IsHidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `IsHidden = true` oculta el elemento de la tabla dinámica; establecer `IsHidden = false` lo muestra de nuevo y lo hace visible nuevamente.

Este enfoque es útil cuando la regla de filtrado es irregular o específica de un elemento, como ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe concreto. El siguiente ejemplo carga una tabla dinámica, oculta un elemento específico por nombre, demuestra cómo mostrarlo de nuevo, actualiza la tabla dinámica y guarda el libro.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.Worksheets[0];

// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.PivotTables[0];

// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.RowFields[0];

// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];

    // Hide pivot items that match a specific name/criterion
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }

    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}

// Refresh and recalculate the pivot table so changes take effect
pivotTable.PivotCache.Refresh();

// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.Save("output_pivot_filtered.xlsx");
```

## **Resumen**

Aspose.Cells for .NET ofrece un conjunto completo de capacidades de filtrado de tablas dinámicas que coinciden con las que se encuentran en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 mejores gestiona los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible a nivel de elemento. Combinar estas estrategias — por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos — le permite crear informes de tablas dinámicas dirigidos con precisión completamente desde código.
{{< app/cells/assistant language="csharp" >}}