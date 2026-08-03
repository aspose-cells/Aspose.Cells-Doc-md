---
title: Filtrar Tablas Dinámicas por Etiqueta o Valor
linktitle: Filtrar Tablas Dinámicas por Etiqueta o Valor
description: Aspose.Cells for Java ofrece capacidades completas de filtrado de tablas dinámicas. Este artículo explica cómo filtrar datos de tablas dinámicas usando filtros de etiqueta, filtros de fecha, filtros de valor, filtros top 10, y ocultando o mostrando elementos de la tabla dinámica.
keywords: Aspose.Cells, biblioteca Java, hoja de cálculo, tabla dinámica, filtro, filtro de etiqueta, filtro de valor, filtro de fecha, filtro top 10, elemento de tabla dinámica, ocultar elemento de tabla dinámica
type: docs
weight: 10
url: /es/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una tabla dinámica. Puede aplicar filtros de etiqueta a campos de fila o columna basados en texto, usar filtros de fecha cuando el campo contiene únicamente celdas de fecha-hora o en blanco, aplicar filtros de valor contra números agregados, usar filtros top 10 para clasificar por un campo de valor, o ocultar y mostrar manualmente elementos individuales de la tabla dinámica usando la propiedad `IsHidden`. Cada estrategia se expone a través de API dedicadas en las clases `PivotField` y `PivotItem`.

{{% /alert %}}

## **Introducción**

Las tablas dinámicas son potentes herramientas analíticas, pero los resúmenes sin procesar a menudo contienen mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe específico. Aspose.Cells for Java refleja las capacidades de filtrado disponibles en Microsoft Excel, exponiéndolas mediante programación para que la generación de informes pueda ser completamente automatizada.

Las siguientes estrategias de filtrado se cubren en este artículo:

1. **Filtro de Etiqueta** — filtra los elementos de un campo de fila o columna basándose en sus etiquetas de texto.
2. **Filtro de Fecha** — filtra campos de fila o columna que contienen únicamente valores de fecha-hora (o en blanco).
3. **Filtro de Valor** — filtra elementos basándose en los valores agregados de un campo de datos.
4. **Filtro Top 10** — muestra solo los N elementos superiores o inferiores clasificados por un campo de valor.
5. **Ocultar / Mostrar Elementos de la Tabla Dinámica** — controla manualmente la visibilidad de cada elemento individual en un campo.

Cada enfoque utiliza un método diferente en la clase `PivotField` o una propiedad en la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `refreshData()` y `calculateData()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de Etiqueta**

Un filtro de etiqueta le permite filtrar los elementos de un campo de fila o columna comparando sus textos de etiqueta con un patrón. Esto es útil cuando desea mostrar solo los productos cuyos nombres comienzan con una letra específica, contienen una palabra particular, o cumplen con algún otro criterio basado en la etiqueta.

Aspose.Cells expone el filtrado de etiquetas a través del método `PivotField.filterByLabel(PivotFilterType, String)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, etc. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.

El siguiente ejemplo carga un libro de trabajo que contiene una tabla dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyas etiquetas comiencen con un prefijo específico, actualiza la tabla dinámica y guarda el resultado.

```java
import com.aspose.cells.*;

String fileName = "sample.xlsx";
String prefix = "B";

// Cargar el libro de trabajo existente que contiene una tabla dinámica
Workbook workbook = new Workbook(fileName);

// Acceder a la hoja de trabajo por índice (primera hoja de trabajo)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Acceder a la tabla dinámica por índice
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Obtener el primer campo de fila PivotField
PivotField rowField = pivotTable.getRowFields().get(0);

// Aplicar el filtro de etiqueta - mostrar solo los elementos de fila cuyas etiquetas comiencen con el prefijo proporcionado
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");

// Actualizar y recalcular los datos de la tabla dinámica para que el filtro surta efecto
pivotTable.refreshData();

// Guardar el libro de trabajo de vuelta en el disco
workbook.save(fileName);
```

## **Filtro de Fecha**

Los filtros de fecha le permiten reducir una tabla dinámica mediante criterios basados en fechas como hoy, la semana pasada, este mes, el próximo trimestre, o un rango de fechas específico. Son filtros especializados que funcionan solo contra campos que almacenan información de fecha-hora.

{{% alert color="primary" %}}

El filtro de fecha solo funciona cuando el área de filas o columnas contiene únicamente celdas de fecha-hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo esté formateado como fecha y que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.

{{% /alert %}}

Aspose.Cells expone el filtrado de fechas a través del método `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha dedicados como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, y `Between`. Según el tipo de filtro elegido, pasa uno o dos valores `DateTime` (para `Between`, pasa las fechas de inicio y fin).

El siguiente ejemplo carga un libro de trabajo con una tabla dinámica cuyo área de filas contiene un campo de fecha, aplica un filtro de fecha que limita los elementos visibles a un rango de fechas particular, actualiza la tabla dinámica y guarda el libro de trabajo.

```java
import java.io.File;
import java.io.FileNotFoundException;

String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";

if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}

// Cargar el libro existente que contiene la tabla dinámica
Workbook workbook = new Workbook(inputPath);

// Acceder a la hoja de cálculo que contiene la tabla dinámica (por índice)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Acceder a la tabla dinámica por índice
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Recuperar el PivotField de fecha del área de filas
// (El filtro de fecha solo funciona cuando el área de filas/columnas contiene solo celdas de fecha-hora o están vacías)
PivotField dateField = pivotTable.getRowFields().get(0);

// Definir el criterio de fecha para el filtro Entre
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Aplicar el filtro de fecha en el campo dinámico
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);

// Actualizar y recalcular la tabla dinámica para que el filtro surta efecto
pivotTable.refreshData();

// Guardar el libro
workbook.save(outputPath);
```

## **Filtro de Valor**

Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de coincidir con etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar solo los productos cuya suma de ventas excede una cantidad objetivo o solo las regiones cuyo conteo de transacciones está dentro de un rango.

Aspose.Cells expone el filtrado de valores a través del método `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)`. El parámetro `filterType` usa valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos debe evaluarse, y los argumentos finales proporcionan el valor o valores umbral.

El siguiente ejemplo carga un libro de trabajo con una tabla dinámica, aplica un filtro de valor que mantiene solo los elementos cuyas ventas agregadas exceden un umbral numérico, actualiza la tabla dinámica y guarda el libro de trabajo.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);

PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);

// Encontrar el índice del campo de datos manualmente ya que PivotFieldCollection no tiene IndexOf
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

## **Filtro Top 10**

El filtro top 10 es una forma especializada de filtro de valor que retiene solo los N elementos superiores o inferiores basados en un campo de valor elegido. Se usa comúnmente para informes de clasificación como "los 10 mejores productos por ingresos" o "las 5 regiones inferiores por conteo de ventas".

{{% alert color="primary" %}}

El filtro top 10 solo es efectivo cuando la tabla dinámica tiene uno o más campos de valor en el área de datos. Sin al menos un campo de valor, no hay ninguna medida agregada contra la cual clasificar los elementos, y el filtro no se puede aplicar.

{{% /alert %}}

Aspose.Cells expone el filtrado top 10 a través del método `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)`. El parámetro `itemCount` define cuántos elementos retener, `isTop` indica si se deben mantener los elementos superiores (true) o los elementos inferiores (false), `valueField` hace referencia al campo de datos usado para la clasificación, y `filterType` controla cómo se calcula el valor (típicamente `Sum`, pero también `Count` y `Percent`).

El siguiente ejemplo carga un libro de trabajo con una tabla dinámica que contiene un campo de valor, aplica un filtro top 10 para mantener solo los 10 elementos superiores por la suma de ventas, actualiza la tabla dinámica y guarda el libro de trabajo.

```java
import com.aspose.cells.*;

// Cargar el libro existente que contiene la tabla dinámica
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Acceder a la hoja de cálculo que contiene la tabla dinámica (índice 0)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Acceder a la tabla dinámica por índice
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Confirmar que hay al menos un PivotField de valor en el área de datos
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);

// Obtener el PivotField de fila objetivo (el campo al que queremos aplicar Top 10)
PivotField rowField = pivotTable.getRowFields().get(0);

// El primer (y único) campo de datos está en el índice 0; Top 10 clasifica por él.
int valueFieldIndex = 0;

// Aplicar el filtro Top 10 en el campo de fila:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false significaría bottom N)
//   - valueFieldIndex = el índice del campo de datos utilizado para clasificar elementos
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);

// Actualizar los datos de la tabla dinámica y recalcularla para que el filtro surta efecto
pivotTable.refreshData();

// Guardar el libro
workbook.save(outputPath);
```

## **Filtrar Ocultando o Mostrando Elementos de la Tabla Dinámica**

Además de las API de filtrado estructurado, Aspose.Cells le permite controlar la visibilidad de cada elemento individual de la tabla dinámica directamente. Al iterar a través de la colección `PivotItems` de un `PivotField` y alternar la propiedad `IsHidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `IsHidden = true` oculta el elemento de la tabla dinámica; establecer `IsHidden = false` lo muestra y lo hace visible nuevamente.

Este enfoque es útil cuando la regla de filtrado es irregular o específica del elemento, como ocultar un pequeño número de categorías nombradas que no deben aparecer en un informe particular. El ejemplo a continuación carga una tabla dinámica, oculta un elemento específico por nombre, demuestra cómo mostrarlo, actualiza la tabla dinámica y guarda el libro de trabajo.

```java
import com.aspose.cells.*;

// Cargar un libro existente que contiene una tabla dinámica
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Acceder a la primera hoja de cálculo que contiene la tabla dinámica
Worksheet sheet = workbook.getWorksheets().get(0);

// Acceder a la tabla dinámica por índice (la primera tabla dinámica en la hoja)
PivotTable pivotTable = sheet.getPivotTables().get(0);

// Recuperar el PivotField objetivo (el primer campo de etiqueta de fila en el que ocultaremos/mostraremos elementos)
PivotField pivotField = pivotTable.getRowFields().get(0);

// Iterar a través de la colección PivotItems del PivotField seleccionado
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);

    // Ocultar elementos dinámicos que coincidan con un nombre/criterio específico
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }

    // Demostrar cómo mostrar: volver a mostrar un elemento dinámico previamente ocultado
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}

// Refrescar y recalcular la tabla dinámica para que los cambios surtan efecto
pivotTable.refreshData();

// Guardar el libro: los elementos ocultos permanecen en los datos subyacentes
// pero se excluyen de la salida mostrada de la tabla dinámica
workbook.save("output_pivot_filtered.xlsx");
```

## **Resumen**

Aspose.Cells for Java ofrece un conjunto completo de capacidades de filtrado de tablas dinámicas que coinciden con las que se encuentran en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro top 10 maneja los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible a nivel de elemento. Combinar estas estrategias — por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos — le permite construir informes de tablas dinámicas precisamente dirigidos completamente desde código.
{{< app/cells/assistant language="java" >}}
