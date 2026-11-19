---
title: Filtrado de tablas dinámicas por etiqueta o valor
description: Aspose.Cells for C++ admite capacidades completas de filtrado de tablas dinámicas. Este artículo explica cómo filtrar los datos de una tabla dinámica mediante filtros de etiqueta, filtros de fecha, filtros de valor, filtros de los 10 principales y la ocultación o mostración de elementos de tablas dinámicas.
linktitle: Filtrado de tablas dinámicas por etiqueta o valor
keywords: Aspose.Cells, biblioteca C++, hoja de cálculo, tabla dinámica, filtro, filtro por etiqueta, filtro por valor, filtro por fecha, filtro de los 10 principales, elemento de tabla dinámica, ocultar elemento de tabla dinámica
type: docs
weight: 10
url: /es/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece cinco estrategias prácticas para filtrar los datos mostrados en una tabla dinámica. Puede aplicar filtros de etiqueta a campos de fila o columna basados en texto, usar filtros de fecha cuando el campo contenga únicamente celdas de fecha y hora o valores vacíos, aplicar filtros de valor frente a números agregados, usar filtros de los 10 principales para clasificar elementos según un campo de valor o controlar manualmente la visibilidad de elementos individuales de una tabla dinámica mediante la propiedad `IsHidden`. Cada estrategia está disponible mediante API específicas en las clases `PivotField` y `PivotItem`.
{{% /alert %}}

## **Introducción**
Las tablas dinámicas son herramientas analíticas potentes, pero los resúmenes sin procesar suelen contener mucha más información de la que necesita presentar. El filtrado es el mecanismo principal para reducir una tabla dinámica a las filas, columnas o valores que importan para un informe concreto. Aspose.Cells for C++ replica las capacidades de filtrado disponibles en Microsoft Excel y las expone mediante programación para que la generación de informes pueda automatizarse por completo.
Las siguientes estrategias de filtrado se abordan en este artículo:
1. **Filtro por etiqueta** — filtra elementos de campos de fila o columna según sus etiquetas de texto.
2. **Filtro por fecha** — filtra campos de fila o columna que contienen únicamente valores de fecha y hora (o vacíos).
3. **Filtro por valor** — filtra elementos según los valores agregados de un campo de datos.
4. **Filtro de los 10 principales** — muestra solo los N elementos superiores o inferiores, clasificados según un campo de valor.
5. **Ocultar / Mostrar elementos de tablas dinámicas** — controla manualmente la visibilidad de cada elemento individual de un campo.
Cada enfoque utiliza un método diferente de la clase `PivotField` o una propiedad de la clase `PivotItem`. Tras aplicar cualquier filtro, debe llamar a `GetPivotCache().Refresh()` en la tabla dinámica para que los datos en caché y los valores calculados reflejen el nuevo estado del filtro.

## **Filtro por etiqueta**
Un filtro por etiqueta permite filtrar los elementos de un campo de fila o columna comparando sus rótulos de texto con un patrón. Esto es útil cuando desea mostrar únicamente productos cuyos nombres comienzan por una letra concreta, contienen una palabra determinada o cumplen otro criterio basado en rótulos.
Aspose.Cells expone el filtrado por etiqueta mediante el método `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. La enumeración `PivotFilterType` incluye valores como `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`, entre otros. El segundo argumento proporciona la cadena de etiqueta utilizada para la comparación.
El siguiente ejemplo carga un libro de trabajo que contiene una tabla dinámica existente, aplica un filtro por etiqueta para que solo permanezcan visibles los elementos cuyos rótulos comienzan por un prefijo especificado, actualiza la tabla dinámica y guarda el resultado.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro por fecha**
Los filtros de fecha permiten reducir una tabla dinámica según criterios de fecha, como hoy, la semana pasada, este mes, el próximo trimestre o un intervalo de fechas concreto. Son filtros especializados que solo funcionan con campos que almacenan información de fecha y hora.

{{% alert color="primary" %}}
El filtro de fecha solo funciona cuando el área de fila o columna contiene únicamente celdas de fecha y hora o valores vacíos. Si el campo subyacente contiene otros tipos de datos, como números o texto, el filtro de fecha no producirá el resultado esperado. Asegúrese de que el campo esté formateado como fecha y de que todos los valores sean instancias válidas de `DateTime` o celdas vacías antes de aplicar este filtro.
Aspose.Cells expone el filtrado por fecha mediante el método `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. La enumeración `PivotFilterType` contiene valores específicos de fecha, como `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` y `Between`. Según el tipo de filtro elegido, se pasan uno o dos valores `DateTime` (para `Between`, se pasan las fechas de inicio y fin).
El siguiente ejemplo carga un libro de trabajo con una tabla dinámica cuyo área de fila contiene un campo de fecha, aplica un filtro de fecha que restringe los elementos visibles a un intervalo de fechas concreto, actualiza la tabla dinámica y guarda el libro de trabajo.
{{% /alert %}}

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
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro por valor**
Los filtros de valor operan sobre los valores agregados que una tabla dinámica calcula en su área de datos. En lugar de coincidir con rótulos de texto, comparan totales numéricos con un umbral. Los casos de uso típicos incluyen mostrar únicamente productos cuya suma de ventas supera un importe objetivo o únicamente regiones cuyo número de transacciones se sitúa dentro de un intervalo.
Aspose.Cells expone el filtrado por valor mediante el método `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. El parámetro `filterType` usa valores como `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` y `ValueLessThanOrEqual`. El parámetro `valueField` especifica qué campo de datos se debe evaluar, y el argumento o los argumentos finales proporcionan el valor o los valores de umbral.
El siguiente ejemplo carga un libro de trabajo con una tabla dinámica, aplica un filtro de valor que conserva únicamente los elementos cuyas ventas agregadas superan un umbral numérico, actualiza la tabla dinámica y guarda el libro de trabajo.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
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
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro de los 10 principales**
El filtro de los 10 principales es una forma especializada de filtro de valor que conserva únicamente los N elementos con los valores más altos o más bajos según un campo de valor elegido. Se usa habitualmente para generar informes de clasificación como "los 10 principales productos por ingresos" o "las 5 regiones inferiores por número de ventas".

{{% alert color="primary" %}}
El filtro de los 10 principales solo es eficaz cuando la tabla dinámica tiene uno o más campos de valor en el área de datos. Sin al menos un campo de valor, no existe una medida agregada con la que clasificar los elementos y el filtro no se puede aplicar.
Aspose.Cells expone el filtrado de los 10 principales mediante el método `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`. El parámetro `valueFieldIndex` es el índice del campo de datos cuyos valores agregados determinan la clasificación de los elementos; `type` selecciona la unidad de medición de `itemCount` (`PivotFilterType::Count` conserva un número fijo de elementos, `PivotFilterType::Percent` conserva un porcentaje de los elementos, de modo que `itemCount` es el porcentaje en sí); `isTop` indica si se deben conservar los elementos superiores (`true`) o los inferiores (`false`), y `itemCount` define cuántos elementos o qué porcentaje se deben conservar.
El siguiente ejemplo carga un libro de trabajo con una tabla dinámica que contiene un campo de valor, aplica un filtro de los 10 principales para conservar únicamente los 10 elementos con la mayor suma de ventas, actualiza la tabla dinámica y guarda el libro de trabajo.
{{% /alert %}}

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
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtrar ocultando o mostrando elementos de tablas dinámicas**
Además de las API de filtrado estructurado, Aspose.Cells permite controlar directamente la visibilidad de cada elemento individual de una tabla dinámica. Al iterar por la colección `PivotItems` de un `PivotField` y alternar la propiedad `IsHidden`, puede ocultar selectivamente elementos concretos sin aplicar un filtro basado en fórmulas. Al establecer `IsHidden = true`, el elemento se oculta de la tabla dinámica; al establecer `IsHidden = false`, se vuelve a mostrar y queda visible.
Este enfoque resulta útil cuando la regla de filtrado es irregular o específica de cada elemento, por ejemplo, para ocultar un pequeño número de categorías con nombre que no deben aparecer en un informe concreto. El siguiente ejemplo carga una tabla dinámica, oculta un elemento concreto por nombre, demuestra cómo volver a mostrarlo, actualiza la tabla dinámica y guarda el libro de trabajo.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Resumen**
Aspose.Cells for C++ proporciona un conjunto completo de capacidades de filtrado de tablas dinámicas que coincide con las disponibles en Microsoft Excel. Los filtros por etiqueta, fecha y valor cubren los escenarios analíticos más comunes, mientras que el filtro de los 10 principales permite gestionar informes de clasificación. Cuando la regla de filtrado es irregular, la propiedad `PivotItem.IsHidden` ofrece una alternativa flexible al nivel de cada elemento. La combinación de estas estrategias —por ejemplo, aplicar un filtro por etiqueta y después ocultar elementos concretos— permite crear informes de tablas dinámicas con el alcance exacto deseado, totalmente mediante código.

## Artículos relacionados
- [Insertar tabla dinámica](/cells/es/cpp/create-pivot-table/)
- [Añadir campos de fila y columna de tabla dinámica en Aspose.Cells for C++](/cells/es/cpp/pivot-table-add-row-and-column-fields/)
- [Añadir campos de filtro a una tabla dinámica en Aspose.Cells for C++](/cells/es/cpp/add-page-field-in-pivot-table/)
- [Administrar campos de valor de tabla dinámica en Aspose.Cells for C++](/cells/es/cpp/manage-value-fields/)
- [Actualizar tablas dinámicas y cachés de tablas dinámicas en Aspose.Cells for C++](/cells/es/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}