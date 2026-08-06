---
title: Filtrar tablas dinámicas por etiqueta o valor
linktitle: Filtrar tablas dinámicas por etiqueta o valor
description: Aspose.Cells for C++ ofrece capacidades completas de filtrado de tablas dinámicas. Este artículo explica cómo filtrar datos de tablas dinámicas mediante filtros de etiqueta, filtros de fecha, filtros de valor, filtros de los 10 mejores, y ocultando o mostrando elementos dinámicos.
keywords: Aspose.Cells, biblioteca C++, hoja de cálculo, tabla dinámica, filtro, filtro de etiqueta, filtro de valor, filtro de fecha, filtro de los 10 mejores, elemento dinámico, ocultar elemento dinámico
type: docs
weight: 10
url: /es/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una tabla dinámica. Puede aplicar filtros de etiqueta a campos de fila o columna basados en texto, usar filtros de fecha cuando el campo solo contenga celdas de tipo fecha-hora o esté en blanco, aplicar filtros de valor frente a números agregados, usar filtros de los 10 mejores para clasificar por un campo de valor, u ocultar y mostrar manualmente elementos dinámicos individuales mediante la propiedad `IsHidden`. Cada estrategia se expone a través de API dedicadas en las clases `PivotField` y `PivotItem`.

{{% /alert %}}

## **Introducción**

Las tablas dinámicas son herramientas analíticas potentes, pero los resúmenes sin procesar a menudo contienen mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe específico. Aspose.Cells for C++ replica las capacidades de filtrado disponibles en Microsoft Excel, exponiéndolas de forma programática para que la generación de informes pueda automatizarse por completo.

Las siguientes estrategias de filtrado se tratan en este artículo:

1. **Filtro de etiqueta** — filtra los elementos de un campo de fila o columna según sus etiquetas de texto.
2. **Filtro de fecha** — filtra campos de fila o columna que solo contienen valores de fecha-hora (o están en blanco).
3. **Filtro de valor** — filtra los elementos según los valores agregados de un campo de datos.
4. **Filtro de los 10 mejores** — muestra solo los N elementos superiores o inferiores clasificados por un campo de valor.
5. **Ocultar/Mostrar elementos dinámicos** — controla manualmente la visibilidad de cada elemento individual en un campo.

Cada enfoque utiliza un método diferente de la clase `PivotField` o una propiedad de la clase `PivotItem`. Después de aplicar cualquier filtro, debe llamar a `RefreshData()` y `CalculateData()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro de etiqueta**

Un filtro de etiqueta le permite filtrar los elementos de un campo de fila o columna comparando sus etiquetas de texto con un patrón. Esto resulta útil cuando desea mostrar solo productos cuyos nombres comiencen con una letra específica, contengan una palabra concreta o coincidan con cualquier otro criterio basado en la etiqueta.

Aspose.Cells expone el filtrado por etiqueta a través del método `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.

El siguiente ejemplo carga un libro de trabajo que contiene una tabla dinámica existente, aplica un filtro de etiqueta para que solo permanezcan visibles los elementos cuyas etiquetas comiencen con un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // Cargar el libro existente que contiene una tabla dinámica
    Workbook wb(fileName);

    // Acceder a la hoja de cálculo por índice (primera hoja)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Acceder a la tabla dinámica por índice
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Obtener el primer PivotField de fila
    PivotField rowField = pt.GetRowFields().Get(0);

    // Aplicar el filtro de etiqueta — mostrar solo los elementos de fila cuyas etiquetas comiencen con el prefijo proporcionado
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // Actualizar y recalcular los datos de la tabla dinámica para que el filtro surta efecto
    pt.RefreshData();

    // Guardar el libro de nuevo en el disco
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro de fecha**

Los filtros de fecha le permiten reducir una tabla dinámica mediante criterios basados en fechas, como hoy, la semana pasada, este mes, el próximo trimestre o un rango de fechas específico. Son filtros especializados que solo funcionan con campos que almacenan información de fecha-hora.

{{% alert color="primary" %}}

El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de tipo fecha-hora o valores en blanco. Si el campo subyacente contiene otros tipos de datos como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo esté formateado como una fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.

{{% /alert %}}

Aspose.Cells expone el filtrado por fecha a través del método `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. La enumeración `PivotFilterType` contiene valores de fecha dedicados como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Dependiendo del tipo de filtro elegido, debe pasar uno o dos valores `DateTime` (para `Between`, debe pasar las fechas de inicio y fin).

El siguiente ejemplo carga un libro de trabajo con una tabla dinámica cuyo área de filas contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un rango de fechas particular, actualiza la tabla dinámica y guarda el libro de trabajo.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";

    if (!std::filesystem::exists(inputPath))
    {
        // Libro de trabajo fuente no encontrado.
        Aspose::Cells::Cleanup();
        return -1;
    }

    // Cargar el libro de trabajo existente que contiene la tabla dinámica
    Workbook workbook(U16String(inputPath.c_str()));

    // Acceder a la hoja de trabajo que contiene la tabla dinámica (por índice)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Acceder a la tabla dinámica por índice
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Obtener el PivotField de fecha del área de filas
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // Definir el criterio de fecha para el filtro Entre
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // Aplicar el filtro de fecha en el campo dinámico
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // Actualizar y recalcular la tabla dinámica para que el filtro surta efecto
    // Guardar el libro de trabajo
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro de valor**

Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de hacer coincidir etiquetas de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar solo productos cuya suma de ventas supere una cantidad objetivo o solo regiones cuyo número de transacciones se encuentre dentro de un rango.

Aspose.Cells expone el filtrado por valor a través del método `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. El parámetro `filterType` utiliza valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos se debe evaluar, y el/los último(s) argumento(s) proporciona(n) el/los valor(es) umbral.

El siguiente ejemplo carga un libro de trabajo con una tabla dinámica, aplica un filtro de valor que conserva solo los elementos cuyas ventas agregadas superan un umbral numérico, actualiza la tabla dinámica y guarda el libro de trabajo.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);

    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }

    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro de los 10 mejores**

El filtro de los 10 mejores es una forma especializada de filtro de valor que conserva solo los N elementos más altos o más bajos según un campo de valor elegido. Se usa comúnmente para informes de clasificación como "los 10 productos principales por ingresos" o "las 5 regiones inferiores por número de ventas".

{{% alert color="primary" %}}

El filtro de los 10 mejores solo es efectivo cuando la tabla dinámica tiene uno o más campos de valor en el área de datos. Sin al menos un campo de valor, no hay ninguna medida agregada con la que clasificar los elementos, y el filtro no se puede aplicar.

{{% /alert %}}

Aspose.Cells expone el filtrado de los 10 mejores a través del método `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. El parámetro `itemCount` define cuántos elementos se deben conservar, `isTop` indica si se conservan los elementos superiores (true) o los inferiores (false), `valueField` hace referencia al campo de datos utilizado para la clasificación, y `filterType` controla cómo se calcula el valor (normalmente `Sum`, pero también `Count` y `Percent`).

El siguiente ejemplo carga un libro de trabajo con una tabla dinámica que contiene un campo de valor, aplica un filtro de los 10 mejores para conservar solo los 10 elementos más altos según la suma de ventas, actualiza la tabla dinámica y guarda el libro de trabajo.

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }

    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);

    int valueFieldIndex = 0;

    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrar ocultando o mostrando elementos dinámicos**

Además de las API de filtrado estructurado, Aspose.Cells le permite controlar directamente la visibilidad de cada elemento dinámico individual. Iterando a través de la colección `PivotItems` de un `PivotField` y alternando la propiedad `IsHidden`, puede suprimir selectivamente elementos específicos sin aplicar un filtro basado en fórmulas. Establecer `IsHidden = true` oculta el elemento de la tabla dinámica; establecer `IsHidden = false` lo muestra y vuelve a hacerlo visible.

Este enfoque resulta útil cuando la regla de filtrado es irregular o específica del elemento, como ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe concreto. El siguiente ejemplo carga una tabla dinámica, oculta un elemento específico por nombre, muestra cómo volver a mostrarlo, actualiza la tabla dinámica y guarda el libro de trabajo.

```cpp
"Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Cargar un libro existente que contiene una tabla dinámica
    Workbook workbook(u"pivot_table_sample.xlsx");

    // Acceder a la primera hoja de cálculo que contiene la tabla dinámica
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Acceder a la tabla dinámica por índice (la primera tabla dinámica de la hoja)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // Obtener el PivotField objetivo (el primer campo de etiqueta de fila en el que ocultaremos/mostraremos elementos)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // Iterar a través de la colección PivotItems del PivotField seleccionado
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // Ocultar elementos de la tabla dinámica que coincidan con un nombre/criterio específico
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // Demostrar cómo mostrar: volver a mostrar un elemento de tabla dinámica previamente oculto
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // Refrescar y recalcular la tabla dinámica para que los cambios surtan efecto
    pivotTable.CalculateData();

    // Guardar el libro: los elementos ocultos permanecen en los datos subyacentes
    // pero se excluyen de la salida mostrada de la tabla dinámica
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Resumen**

Aspose.Cells for C++ proporciona un conjunto completo de capacidades de filtrado de tablas dinámicas que coinciden con las que se encuentran en Microsoft Excel. Los filtros de etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 mejores gestiona los informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible a nivel de elemento. Combinar estas estrategias —por ejemplo, aplicar un filtro de etiqueta y luego ocultar elementos específicos— le permite generar informes de tablas dinámicas dirigidos con precisión enteramente desde código.
{{< app/cells/assistant language="cpp" >}}