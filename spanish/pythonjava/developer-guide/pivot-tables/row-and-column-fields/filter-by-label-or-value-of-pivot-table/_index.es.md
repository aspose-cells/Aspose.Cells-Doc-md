---
title: Filtrar tablas dinámicas por etiqueta o valor
linktitle: Filtrar tablas dinámicas por etiqueta o valor
description: Aspose.Cells for Python via Java admite capacidades completas de filtrado de tablas dinámicas. Este artículo explica cómo filtrar datos de tablas dinámicas mediante filtros de etiqueta, filtros de fecha, filtros de valor, filtros de los 10 mejores y ocultando o mostrando elementos dinámicos.
keywords: Aspose.Cells, biblioteca de Python via Java, hoja de cálculo, tabla dinámica, filtro, filtro de etiqueta, filtro de valor, filtro de fecha, filtro de los 10 mejores, elemento dinámico, ocultar elemento dinámico
type: docs
weight: 10
url: /es/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos que se muestran en una tabla dinámica. Puede aplicar filtros de etiqueta a los campos de fila o columna basados en texto, usar filtros de fecha cuando el campo contenga únicamente celdas de tipo fecha-hora o estén en blanco, aplicar filtros de valor frente a los números agregados, usar filtros de los 10 mejores para clasificar por un campo de valor, u ocultar y mostrar manualmente elementos dinámicos individuales utilizando la propiedad `is_hidden`. Cada estrategia se expone a través de API dedicadas en las clases `PivotField` y `PivotItem`.

{{% /alert %}}

## **Introducción**

Las tablas dinámicas son potentes herramientas de análisis, pero los resúmenes sin procesar a menudo contienen mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe específico. Aspose.Cells for Python via Java replica las capacidades de filtrado disponibles en Microsoft Excel, exponiéndolas mediante programación para que la generación de informes pueda automatizarse por completo.

En este artículo se cubren las siguientes estrategias de filtrado:

1. **Filtro de etiqueta**: filtra los elementos de un campo de fila o columna según sus etiquetas de texto.
2. **Filtro de fecha**: filtra los campos de fila o columna que contienen únicamente valores de tipo fecha-hora (o están en blanco).
3. **Filtro de valor**: filtra los elementos según los valores agregados de un campo de datos.
4. **Filtro de los 10 mejores**: muestra solo los N elementos superiores o inferiores clasificados por un campo de valor.
5. **Ocultar/Mostrar elementos dinámicos**: controla manualmente la visibilidad de cada elemento individual en un campo.

Cada enfoque utiliza un método diferente en la clase `PivotField` o una propiedad en la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `refresh_data()` y `calculate_data()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**

Un filtro de etiqueta le permite filtrar los elementos de un campo de fila o columna comparando sus títulos de texto con un patrón. Esto resulta útil cuando desea mostrar solo los productos cuyos nombres comiencen con una letra específica, contengan una palabra determinada o coincidan con cualquier otro criterio basado en el título.

Aspose.Cells expone el filtrado por etiqueta mediante el método `PivotField.filter_by_label(PivotFilterType, str)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.

El siguiente ejemplo carga un libro que contiene una tabla dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyos títulos comiencen con un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# Cargar el libro de trabajo existente que contiene una tabla dinámica
workbook = Workbook(fileName)

# Acceder a la hoja de trabajo por índice (primera hoja de trabajo)
worksheet = workbook.getWorksheets().get(0)

# Acceder a la tabla dinámica por índice
pivotTable = worksheet.getPivotTables().get(0)

# Obtener el primer campo de fila PivotField
rowField = pivotTable.getRowFields().get(0)

# Aplicar el filtro de etiqueta — mostrar solo los elementos de fila cuyas etiquetas comiencen con el prefijo proporcionado
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# Refrescar y recalcular los datos de la tabla dinámica para que el filtro surta efecto
pivotTable.getPivotCache().refresh()

# Guardar el libro de trabajo de vuelta en disco
workbook.save(fileName)

jpype.shutdownJVM()
```

## **Filtro de fecha**

Los filtros de fecha le permiten reducir una tabla dinámica según criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un rango de fechas específico. Son filtros especializados que solo funcionan con campos que almacenan información de tipo fecha-hora.

{{% alert color="primary" %}}

El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de tipo fecha-hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo esté formateado como fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.

{{% /alert %}}

Aspose.Cells expone el filtrado por fecha mediante el método `PivotField.filter_by_date(PivotFilterType, values)`. La enumeración `PivotFilterType` contiene valores específicos de fecha, como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Según el tipo de filtro elegido, debe pasar uno o dos valores `DateTime` (para `Between`, debe pasar las fechas de inicio y fin).

El siguiente ejemplo carga un libro con una tabla dinámica cuyo área de filas contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un rango de fechas particular, actualiza la tabla dinámica y guarda el libro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"

if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")

# Cargar el libro de trabajo existente que contiene la tabla dinámica
workbook = Workbook(inputPath)

# Acceder a la hoja de cálculo que contiene la tabla dinámica (por índice)
worksheet = workbook.getWorksheets().get(0)

# Acceder a la tabla dinámica por índice
pivotTable = worksheet.getPivotTables().get(0)

# Obtener el PivotField de fecha del área de filas
# (El filtro de fecha solo funciona cuando el área de fila/columna contiene solo celdas de fecha-hora o espacios en blanco)
dateField = pivotTable.getRowFields().get(0)

# Definir el criterio de fecha para el filtro Entre
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# Aplicar el filtro de fecha en el campo dinámico
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# Actualizar y recalcular la tabla dinámica para que el filtro surta efecto
pivotTable.getPivotCache().refresh()

# Guardar el libro de trabajo
workbook.save(outputPath)

jpype.shutdownJVM()
```

## **Filtro de valor**

Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de comparar etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar solo los productos cuya suma de ventas supere un importe objetivo, o solo las regiones cuyo número de transacciones se encuentre dentro de un rango.

Aspose.Cells expone el filtrado por valor mediante el método `PivotField.filter_by_value(value_field, filter_type, values)`. El parámetro `filter_type` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. El parámetro `value_field` especifica qué campo de datos se debe evaluar, y los argumentos finales proporcionan los valores de umbral.

El siguiente ejemplo carga un libro con una tabla dinámica, aplica un filtro de valor que mantiene solo los elementos cuyas ventas agregadas superen un umbral numérico, actualiza la tabla dinámica y guarda el libro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)

rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)

# Buscar el índice del campo de datos manualmente ya que PivotFieldCollection no tiene IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break

if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivotTable.getPivotCache().refresh()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Filtro de los 10 mejores**

El filtro de los 10 mejores es una forma especializada de filtro de valor que conserva solo los N elementos superiores o inferiores según un campo de valor elegido. Se usa habitualmente para informes de clasificación, como "los 10 productos principales por ingresos" o "las 5 regiones inferiores por número de ventas".

{{% alert color="primary" %}}

El filtro de los 10 mejores solo es eficaz cuando la tabla dinámica tiene uno o más campos de valor en el área de datos. Sin al menos un campo de valor, no existe ninguna medida agregada con la que clasificar los elementos, y el filtro no se puede aplicar.

{{% /alert %}}

Aspose.Cells expone el filtrado de los 10 mejores mediante el método `PivotField.filter_top10(item_count, is_top, value_field, filter_type)`. El parámetro `item_count` define cuántos elementos se deben conservar, `is_top` indica si se deben mantener los elementos superiores (true) o los inferiores (false), `value_field` hace referencia al campo de datos utilizado para la clasificación, y `filter_type` controla cómo se calcula el valor (normalmente `Sum`, pero también `Count` y `Percent`).

El siguiente ejemplo carga un libro con una tabla dinámica que contiene un campo de valor, aplica un filtro de los 10 mejores para mantener solo los 10 elementos superiores por la suma de ventas, actualiza la tabla dinámica y guarda el libro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# Cargar el libro de trabajo existente que contiene la tabla dinámica
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# Acceder a la hoja de cálculo que contiene la tabla dinámica (índice 0)
worksheet = workbook.getWorksheets().get(0)

# Acceder a la tabla dinámica por índice
pivotTable = worksheet.getPivotTables().get(0)

# Confirmar que hay al menos un PivotField de valor en el área de datos
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)

# Obtener el PivotField de fila objetivo (el campo al que queremos aplicar Top 10)
rowField = pivotTable.getRowFields().get(0)

# El primer (y único) campo de datos está en el índice 0; Top 10 clasifica por él.
valueFieldIndex = 0

# Aplicar el filtro Top 10 en el campo de fila:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (N superiores; false significaría N inferiores)
#   - valueFieldIndex = el índice del campo de datos utilizado para clasificar los elementos
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# Actualizar los datos de la tabla dinámica y recalcularla para que el filtro surta efecto
pivotTable.getPivotCache().refresh()

# Guardar el libro de trabajo
workbook.save(outputPath)

jpype.shutdownJVM()
```

## **Filtrar ocultando o mostrando elementos dinámicos**

Además de las API de filtrado estructurado, Aspose.Cells le permite controlar la visibilidad de cada elemento dinámico individual directamente. Al recorrer la colección `PivotItems` de un `PivotField` y alternar la propiedad `is_hidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `is_hidden = True` oculta el elemento de la tabla dinámica; establecer `is_hidden = False` lo muestra nuevamente y lo hace visible de nuevo.

Este enfoque resulta útil cuando la regla de filtrado es irregular o específica de un elemento, como ocultar un número reducido de categorías con nombre que no deben aparecer en un informe en particular. El siguiente ejemplo carga una tabla dinámica, oculta un elemento específico por su nombre, muestra cómo volver a mostrarlo, actualiza la tabla dinámica y guarda el libro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# Cargar un libro de trabajo existente que contiene una tabla dinámica
workbook = Workbook("pivot_table_sample.xlsx")

# Acceder a la primera hoja de cálculo que contiene la tabla dinámica
sheet = workbook.getWorksheets().get(0)

# Acceder a la tabla dinámica por índice (la primera tabla dinámica en la hoja)
pivotTable = sheet.getPivotTables().get(0)

# Recuperar el PivotField de destino (el primer campo de etiqueta de fila en el que ocultaremos/mostraremos elementos)
pivotField = pivotTable.getRowFields().get(0)

# Iterar a través de la colección PivotItems del PivotField seleccionado
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # Ocultar elementos de la tabla dinámica que coincidan con un nombre/criterio específico
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # Demostrar cómo mostrar: volver a mostrar un elemento previamente oculto de la tabla dinámica
    if item.getName() == "Item3":
        item.setIsHidden(False)

# Actualizar y recalcular la tabla dinámica para que los cambios surtan efecto
pivotTable.getPivotCache().refresh()

# Guardar el libro de trabajo — los elementos ocultos permanecen en los datos subyacentes
# pero se excluyen de la salida mostrada de la tabla dinámica
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```

## **Resumen**

Aspose.Cells for Python via Java proporciona un conjunto completo de capacidades de filtrado de tablas dinámicas que se corresponden con las que se encuentran en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 mejores gestiona los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.is_hidden` ofrece una alternativa flexible a nivel de elemento. La combinación de estas estrategias (por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos) le permite crear informes de tabla dinámica muy precisos íntegramente desde el código.
{{< app/cells/assistant language="python" >}}