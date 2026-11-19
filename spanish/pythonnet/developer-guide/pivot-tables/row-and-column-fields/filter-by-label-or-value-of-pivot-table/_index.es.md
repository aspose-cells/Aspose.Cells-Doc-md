---
title: Filtrar tablas dinámicas por etiqueta o valor
description: Aspose.Cells for Python via .NET ofrece completas capacidades de filtrado para tablas dinámicas. Este artículo explica cómo filtrar datos de tablas dinámicas mediante filtros de etiquetas, filtros de fechas, filtros de valores, filtros de los 10 mejores, y ocultando o mostrando elementos de la tabla dinámica.
linktitle: Filtrar tablas dinámicas por etiqueta o valor
keywords: Aspose.Cells, biblioteca de Python via .NET, hoja de cálculo, tabla dinámica, filtro, filtro por etiqueta, filtro por valor, filtro por fecha, filtro de los 10 primeros, elemento de tabla dinámica, ocultar elemento de tabla dinámica
type: docs
weight: 10
url: /es/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una tabla dinámica. Puede aplicar filtros de etiquetas a campos de fila o columna basados en texto, usar filtros de fecha cuando el campo contenga únicamente celdas de tipo fecha-hora o vacías, aplicar filtros de valores contra números agregados, usar filtros de los 10 mejores para clasificar por un campo de valor, u ocultar y mostrar manualmente elementos individuales de la tabla dinámica mediante la propiedad `is_hidden`. Cada estrategia se expone a través de APIs dedicadas en las clases `PivotField` y `PivotItem`.
{{% /alert %}}

## **Introducción**
Las tablas dinámicas son potentes herramientas analíticas, pero los resúmenes sin procesar suelen contener mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe específico. Aspose.Cells for Python via .NET replica las capacidades de filtrado disponibles en Microsoft Excel, exponiéndolas mediante programación para que la generación de informes pueda automatizarse por completo.
Las siguientes estrategias de filtrado se tratan en este artículo:
1. **Filtro de etiqueta** — filtra los elementos de un campo de fila o columna basándose en sus etiquetas de texto.
2. **Filtro de fecha** — filtra campos de fila o columna que contienen únicamente valores de tipo fecha-hora (o espacios en blanco).
3. **Filtro de valor** — filtra elementos basándose en los valores agregados de un campo de datos.
4. **Filtro de los 10 mejores** — muestra únicamente los N elementos superiores o inferiores clasificados por un campo de valor.
5. **Ocultar / Mostrar elementos de la tabla dinámica** — controla manualmente la visibilidad de cada elemento individual en un campo.
Cada enfoque utiliza un método diferente en la clase `PivotField` o una propiedad en la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `refresh_data()` y `calculate_data()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**
Un filtro de etiqueta permite filtrar los elementos de un campo de fila o columna comparando sus textos de etiqueta con un patrón. Esto resulta útil cuando desea mostrar únicamente los productos cuyos nombres comiencen con una letra específica, contengan una palabra particular, o cumplan con cualquier otro criterio basado en la etiqueta.
Aspose.Cells expone el filtrado por etiquetas mediante el método `PivotField.filter_by_label(PivotFilterType, label_string)`. La enumeración `PivotFilterType` incluye valores tales como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.
El siguiente ejemplo carga un libro que contiene una tabla dinámica existente, aplica un filtro de etiqueta de modo que solo permanezcan visibles los elementos cuyas etiquetas comiencen con un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = ac.Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the first row PivotField
row_field = pivot_table.row_fields[0]
# Apply the label filter — show only row items whose labels begin with the supplied prefix
row_field.filter_by_label(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivot_table.pivot_cache.refresh()
# Save the workbook back to disk
workbook.save(fileName)
```

## **Filtro de fecha**
Los filtros de fecha permiten reducir una tabla dinámica según criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un rango de fechas específico. Son filtros especializados que funcionan únicamente contra campos que almacenan información de tipo fecha-hora.

{{% alert color="primary" %}}
El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de tipo fecha-hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo tenga formato de fecha y de que todos los valores sean instancias válidas de `datetime` o celdas vacías antes de aplicar este filtro.
Aspose.Cells expone el filtrado por fechas mediante el método `PivotField.filter_by_date(PivotFilterType, *date_times)`. La enumeración `PivotFilterType` contiene valores de fecha dedicados como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, y `Between`. Dependiendo del tipo de filtro elegido, se pasan uno o dos valores `datetime` (para `Between`, se pasan las fechas de inicio y fin).
El siguiente ejemplo carga un libro con una tabla dinámica cuya área de filas contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un rango de fechas particular, actualiza la tabla dinámica y guarda el libro.
{{% /alert %}}

```python
import os
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotFilterType
input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"
if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)
# Load the existing workbook that contains the pivot table
workbook = ac.Workbook(input_path)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
date_field = pivot_table.row_fields[0]
# Define the date criterion for the Between filter
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
# Apply the date filter on the pivot field
date_field.filter_by_date(PivotFilterType.DATE_BETWEEN, start_date, end_date)
# Refresh and recalculate the pivot table so the filter takes effect
pivot_table.pivot_cache.refresh()
# Persist the workbook
workbook.save(output_path)
```

## **Filtro de valor**
Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de coincidir con etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar únicamente los productos cuya suma de ventas supere un monto objetivo o solo las regiones cuyo recuento de transacciones se encuentre dentro de un rango.
Aspose.Cells expone el filtrado por valores mediante el método `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. El parámetro `PivotFilterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, y `ValueLessThanOrEqual`. El parámetro `value_field` especifica qué campo de datos debe evaluarse, y el último argumento (o argumentos) proporciona los valores umbral.
El siguiente ejemplo carga un libro con una tabla dinámica, aplica un filtro de valor que conserva únicamente los elementos cuyas ventas agregadas superen un umbral numérico, actualiza la tabla dinámica y guarda el libro.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]
row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
data_field_index = -1
for i in range(len(pivot_table.data_fields)):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break
if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, PivotFilterType.VALUE_GREATER_THAN, 5000.0, float('inf'))
pivot_table.pivot_cache.refresh()
workbook.save("output.xlsx")
```

## **Filtro de los 10 mejores**
El filtro de los 10 mejores es una forma especializada de filtro de valor que retiene únicamente los N elementos más altos o más bajos basándose en un campo de valor elegido. Se usa comúnmente para informes de clasificación como "los 10 productos principales por ingresos" o "las 5 regiones inferiores por recuento de ventas".

{{% alert color="primary" %}}
El filtro de los 10 mejores solo es efectivo cuando la tabla dinámica tiene uno o más campos de valor en el área de datos. Sin al menos un campo de valor, no existe ninguna medida agregada contra la cual clasificar los elementos y el filtro no puede aplicarse.
Aspose.Cells expone el filtrado Top 10 mediante el método `PivotField.filter_top10(value_field_index, filter_type, is_top, item_count)`. El parámetro `value_field_index` es el índice del campo de datos cuyos valores agregados clasifican los elementos, `filter_type` selecciona la unidad de `item_count` (`PivotFilterType.COUNT` conserva un número fijo de elementos, `PivotFilterType.PERCENT` conserva un porcentaje de los elementos, por lo que `item_count` es el propio porcentaje), `is_top` indica si se conservan los elementos superiores (True) o los inferiores (False), y `item_count` define cuántos elementos, o qué porcentaje, conservar.
El siguiente ejemplo carga un libro con una tabla dinámica que contiene un campo de valor, aplica un filtro de los 10 mejores para conservar solo los 10 elementos más altos por la suma de ventas, actualiza la tabla dinámica y guarda el libro.
{{% /alert %}}

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivotTable = worksheet.pivot_tables[0]
# Confirm there is at least one value PivotField in the data area
if len(pivotTable.data_fields) == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.row_fields[0]
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filter_top10(valueFieldIndex, acp.PivotFilterType.COUNT, True, 10)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.pivot_cache.refresh()
# Save the workbook
workbook.save(outputPath)
```

## **Filtrar ocultando o mostrando elementos de la tabla dinámica**
Además de las APIs estructuradas de filtrado, Aspose.Cells permite controlar directamente la visibilidad de cada elemento individual de la tabla dinámica. Mediante la iteración a través de la colección `PivotItems` de un `PivotField` y alternando la propiedad `is_hidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `is_hidden = True` oculta el elemento de la tabla dinámica; establecer `is_hidden = False` lo muestra nuevamente y lo hace visible.
Este enfoque resulta útil cuando la regla de filtrado es irregular o específica del elemento, como ocultar un pequeño número de categorías nombradas que no deben aparecer en un informe particular. El ejemplo siguiente carga una tabla dinámica, oculta un elemento específico por nombre, muestra cómo volver a mostrarlo, actualiza la tabla dinámica y guarda el libro.

```python
import aspose.cells as ac
# Load an existing workbook containing a pivot table
workbook = ac.Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.worksheets[0]
# Access the pivot table by index (the first pivot table on the sheet)
pivot_table = sheet.pivot_tables[0]
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivot_field = pivot_table.row_fields[0]
# Iterate through the PivotItems collection of the selected PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]
    # Hide pivot items that match a specific name/criterion
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.name == "Item3":
        item.is_hidden = False
# Refresh and recalculate the pivot table so changes take effect
pivot_table.pivot_cache.refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
```

## **Resumen**
Aspose.Cells for Python via .NET ofrece un conjunto completo de capacidades de filtrado para tablas dinámicas que se corresponden con las disponibles en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 mejores gestiona los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.is_hidden` ofrece un respaldo flexible a nivel de elemento. Combinar estas estrategias —por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos— le permite construir informes de tabla dinámica altamente precisos completamente desde código.

{{< app/cells/assistant language="python-net" >}}