---
title: Filtrar tablas dinámicas por etiqueta o valor
linktitle: Filtrar tablas dinámicas por etiqueta o valor
description: Aspose.Cells for Node.js via C++ admite capacidades completas de filtrado de tablas dinámicas. Este artículo explica cómo filtrar los datos de una tabla dinámica usando filtros de etiqueta, filtros de fecha, filtros de valor, filtros top 10, y mediante ocultar o mostrar elementos dinámicos.
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

Cada enfoque utiliza un método diferente en la clase `PivotField` o una propiedad en la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `refreshData()` y `calculateData()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**

Un filtro de etiqueta le permite filtrar los elementos de un campo de fila o columna comparando sus leyendas de texto con un patrón. Esto resulta útil cuando desea mostrar solo productos cuyos nombres comiencen con una letra específica, contengan una palabra particular o coincidan con algún otro criterio basado en leyendas.

Aspose.Cells expone el filtrado por etiqueta a través del método `PivotField.filterByLabel(PivotFilterType, string)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.

El siguiente ejemplo carga un libro que contiene una tabla dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyas leyendas comiencen con un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Cargar el libro de trabajo existente que contiene una tabla dinámica
let workbook = new AsposeCells.Workbook(fileName);

// Acceder a la hoja de cálculo por índice (primera hoja)
let worksheet = workbook.getWorksheets().get(0);

// Acceder a la tabla dinámica por índice
let pivotTable = worksheet.getPivotTables().get(0);

// Obtener el primer PivotField de fila
let rowField = pivotTable.getRowFields().get(0);

// Aplicar el filtro de etiqueta: mostrar solo los elementos de fila cuyas etiquetas comiencen con el prefijo proporcionado
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Refrescar y recalcular los datos de la tabla dinámica para que el filtro surta efecto
pivotTable.getPivotCache().refresh();

// Guardar el libro de trabajo de vuelta en disco
workbook.save(fileName);
```

## **Filtro de fecha**

Los filtros de fecha le permiten reducir una tabla dinámica según criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un rango de fechas específico. Son filtros especializados que funcionan solo contra campos que almacenan información de fecha-hora.

{{% alert color="primary" %}}

El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de fecha-hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo tenga formato de fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.

{{% /alert %}}

Aspose.Cells expone el filtrado por fecha a través del método `PivotField.filterByDate(PivotFilterType, params DateTime[] values)`. La enumeración `PivotFilterType` contiene valores de fecha dedicados como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Según el tipo de filtro elegido, pasa uno o dos valores `DateTime` (para `Between`, pasa las fechas de inicio y fin).

El siguiente ejemplo carga un libro con una tabla dinámica cuyo área de fila contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un rango de fechas particular, actualiza la tabla dinámica y guarda el libro.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}

// Cargar el libro de trabajo existente que contiene la tabla dinámica
const workbook = new AsposeCells.Workbook(inputPath);

// Acceder a la hoja de trabajo que contiene la tabla dinámica (por índice)
const worksheet = workbook.getWorksheets().get(0);

// Acceder a la tabla dinámica por índice
const pivotTable = worksheet.getPivotTables().get(0);

// Obtener el PivotField de fecha del área de filas
// (El filtro de fecha solo funciona cuando el área de filas/columnas contiene solo celdas de fecha-hora o espacios en blanco)
const dateField = pivotTable.getRowFields().get(0);

// Definir el criterio de fecha para el filtro Entre
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// Aplicar el filtro de fecha en el campo dinámico
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Actualizar y recalcular la tabla dinámica para que el filtro surta efecto
pivotTable.getPivotCache().refresh();

// Guardar el libro de trabajo
workbook.save(outputPath);
```

## **Filtro de valor**

Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de coincidir con etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar solo productos cuya suma de ventas supere una cantidad objetivo, o solo regiones cuyo número de transacciones se encuentre dentro de un rango.

Aspose.Cells expone el filtrado por valor a través del método `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`. El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos se debe evaluar, y el argumento o argumentos finales proporcionan el valor o valores umbral.

El siguiente ejemplo carga un libro con una tabla dinámica, aplica un filtro de valor que conserva solo los elementos cuyas ventas agregadas superan un umbral numérico, actualiza la tabla dinámica y guarda el libro.

```javascript
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

{{% /alert %}}

Aspose.Cells expone el filtrado top 10 a través del método `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. El parámetro `itemCount` define cuántos elementos se deben retener, `isTop` indica si se deben conservar los elementos superiores (true) o los elementos inferiores (false), `valueField` hace referencia al campo de datos utilizado para la clasificación, y `filterType` controla cómo se calcula el valor (normalmente `Sum`, pero también `Count` y `Percent`).

El siguiente ejemplo carga un libro con una tabla dinámica que contiene un campo de valor, aplica un filtro top 10 para conservar solo los 10 elementos más altos por la suma de ventas, actualiza la tabla dinámica y guarda el libro.

```javascript
const AsposeCells = require("aspose.cells");

// Cargar el libro de trabajo existente que contiene la tabla dinámica
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// Acceder a la hoja de trabajo que contiene la tabla dinámica (índice 0)
const worksheet = workbook.getWorksheets().get(0);

// Acceder a la tabla dinámica por índice
const pivotTable = worksheet.getPivotTables().get(0);

// Confirmar que hay al menos un PivotField de valor en el área de datos
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);

// Obtener el PivotField de fila objetivo (el campo al que queremos aplicar Top 10)
const rowField = pivotTable.getRowFields().get(0);

// El primer (y único) campo de datos está en el índice 0; Top 10 clasifica por él.
const valueFieldIndex = 0;

// Aplicar el filtro Top 10 en el campo de fila:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (N superiores; false significaría N inferiores)
//   - valueFieldIndex = el índice del campo de datos utilizado para clasificar elementos
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Actualizar los datos de la tabla dinámica y recalcularla para que el filtro surta efecto
pivotTable.getPivotTableCache().refresh();

// Guardar el libro de trabajo
workbook.save(outputPath);
```

## **Filtrar ocultando o mostrando elementos dinámicos**

Además de las API estructuradas de filtrado, Aspose.Cells le permite controlar la visibilidad de cada elemento dinámico individual directamente. Al iterar por la colección `PivotItems` de un `PivotField` y alternar la propiedad `IsHidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `IsHidden = true` oculta el elemento de la tabla dinámica; establecer `IsHidden = false` lo muestra nuevamente y lo hace visible de nuevo.

Este enfoque resulta útil cuando la regla de filtrado es irregular o específica de un elemento, como ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe particular. El siguiente ejemplo carga una tabla dinámica, oculta un elemento específico por nombre, muestra cómo volver a mostrarlo, actualiza la tabla dinámica y guarda el libro.

```javascript
const AsposeCells = require("aspose.cells");

// Cargar un libro de trabajo existente que contiene una tabla dinámica
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Acceder a la primera hoja de cálculo que contiene la tabla dinámica
const sheet = workbook.getWorksheets().get(0);

// Acceder a la tabla dinámica por índice (la primera tabla dinámica de la hoja)
const pivotTable = sheet.getPivotTables().get(0);

// Obtener el PivotField objetivo (el primer campo de etiqueta de fila en el que ocultaremos/mostraremos elementos)
const pivotField = pivotTable.getRowFields().get(0);

// Iterar a través de la colección PivotItems del PivotField seleccionado
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // Ocultar los elementos de la tabla dinámica que coincidan con un nombre/criterio específico
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // Demostrar cómo mostrar nuevamente un elemento previamente oculto
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// Actualizar y recalcular la tabla dinámica para que los cambios surtan efecto
pivotTable.getPivotCache().refreshData();

// Guardar el libro de trabajo: los elementos ocultos permanecen en los datos subyacentes
// pero se excluyen de la salida mostrada de la tabla dinámica
workbook.save("output_pivot_filtered.xlsx");
```

## **Resumen**

Aspose.Cells for Node.js via C++ proporciona un conjunto completo de capacidades de filtrado de tablas dinámicas que coinciden con las que se encuentran en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro top 10 gestiona los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible a nivel de elemento. La combinación de estas estrategias (por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos) le permite construir informes de tablas dinámicas dirigidos con precisión totalmente desde código.
{{< app/cells/assistant language="nodejs-cpp" >}}