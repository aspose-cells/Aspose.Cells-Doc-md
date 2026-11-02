---
title: Mostrar o filtrar los 10 principales en una tabla dinámica
linktitle: Mostrar o filtrar los 10 principales en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos que ocupan las posiciones más alta o más baja de un campo de tabla dinámica en Aspose.Cells for C++. Este artículo explica el método Top10AutoShow de Excel 97-2003, cómo leer las opciones con GetTop10AutoShowSettings y el filtro de los 10 principales de Excel 2007-365 mediante FilterTop10.
keywords: Aspose.Cells, C++, tabla dinámica, 10 principales, mostrar automáticamente, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /es/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede resultar difícil de leer cuando el campo contiene decenas de elementos. Un informe de los 10 principales conserva únicamente los elementos con la clasificación más alta o más baja, que es exactamente lo que necesitan los informes basados en la clasificación: «los 5 principales productos por ingresos» o «las 3 regiones con menor número de ventas». Aspose.Cells admite dos mecanismos para ello, que se corresponden con dos generaciones de Microsoft Excel.
- **Excel 97-2003 AutoShow** — el método `PivotField.Top10AutoShow()`. Esta es la configuración clásica «Mostrar los N elementos superiores/inferiores» almacenada directamente en el campo de tabla dinámica. Funciona en todas las versiones de Excel, tanto antiguas como recientes, porque forma parte del formato original de tabla dinámica.
- **Filtro de los 10 principales de Excel 2007-365** — el método `PivotField.FilterTop10()`. Este es el filtro moderno de los 10 principales disponible en «Filtros de valores», en el menú del campo. Se almacena como un objeto `PivotFilter` adjunto al campo y ofrece una clasificación basada en el número de elementos o en el porcentaje.

## **Mostrar los 10 principales en Excel 97-2003 (Top10AutoShow)**
La función clásica AutoShow se configura con una sola llamada a `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)`:
- `isAutoShow` — habilita o deshabilita la configuración de AutoShow en el campo.
- `isTop` — `true` conserva los elementos con la clasificación más alta (Superior), mientras que `false` conserva los de menor clasificación (Inferior).
- `count` — el número de elementos que se conservarán; por ejemplo, 10 para un informe clásico de los 10 principales.
- `rankBy` — el índice basado en cero del **campo de datos** cuyos valores determinan la clasificación de los elementos. Pase -1 para clasificar los elementos por el propio campo.
La clasificación puede basarse en un campo de valores o en el propio campo. A continuación se muestran dos variantes habituales.

### **Clasificar por un campo de valores**
Clasifique los elementos del campo de fila según un campo de valores común como «Suma de ventas». El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`) y, a continuación, muestra los 2 deportes con más ventas. `rankBy` es 0 porque «Suma de ventas» es el campo de datos con índice 0.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Mostrar los 2 elementos principales clasificados por "Suma de ventas" (índice 0 del campo de datos)
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Clasificar por el propio campo**
Un campo también puede clasificarse por sí mismo: pase -1 como `rankBy`. Esta variante no necesita ningún campo de datos adicional; basta con que el campo se encuentre en el área de filas (o columnas). El siguiente ejemplo muestra los 3 deportes con la posición más baja en la clasificación por el propio campo. Al guardar esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `GetTop10AutoShowSettings().GetRankBy()` devuelve -1.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Mostrar los 3 elementos inferiores clasificados por el propio campo (rankBy = -1)
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Leer las opciones actuales (GetTop10AutoShowSettings)**
El método `PivotField.GetTop10AutoShowSettings()` devuelve un objeto `PivotFieldTop10AutoShowSettings` que expone las opciones de AutoShow almacenadas actualmente en el campo. Utilícelo para consultar cómo se muestran sus elementos en un libro de trabajo existente o en una tabla dinámica que acaba de configurar, incluidos los libros de trabajo cargados desde un archivo.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Los cuatro miembros se corresponden con los atributos clásicos de AutoShow escritos en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que los valores leídos se respetarán en todas las versiones de Excel.

## **Nota**

{{% alert color="primary" %}}
- Las propiedades directas `IsAutoShow`, `IsAscendShow`, `GetAutoShowCount` y `GetAutoShowField` de `PivotField` están obsoletas. Utilice en su lugar el objeto `PivotFieldTop10AutoShowSettings`: `IsAutoShow` se sustituye por `GetTop10AutoShowSettings().IsAutoShow()`, `IsAscendShow` se sustituye por `GetTop10AutoShowSettings().IsTop()`, `GetAutoShowCount` se sustituye por `GetTop10AutoShowSettings().GetAutoShowCount()` y `GetAutoShowField` se sustituye por `GetTop10AutoShowSettings().GetRankBy()`. El método `Top10AutoShow()` es la forma admitida de modificar la configuración.
- `Top10AutoShow` funciona con campos de fila y de columna. Un campo que solo se encuentra en el área de página (filtro) no puede clasificarse de esta forma porque sus elementos no están dispuestos en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de los 10 principales (FilterTop10)**
Las versiones modernas de Excel ofrecen los 10 principales como filtro de valores en el menú del campo (Filtros de valores, 10 principales...). Aspose.Cells representa esta funcionalidad mediante el método `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`, que devuelve el `PivotFilter` creado:
- `valueFieldIndex` — el índice basado en cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type` — indica qué significa `itemCount`. `PivotFilterType::Count` conserva un número fijo de elementos (la opción Elementos del diálogo). `PivotFilterType::Percent` conserva un porcentaje de los elementos, de modo que `itemCount` es el propio porcentaje: 30 conserva el 30 % de los elementos mejor clasificados. `PivotFilterType::Sum` clasifica según la cobertura acumulada de los valores.
- `isTop` — `true` para mostrar los elementos superiores, `false` para mostrar los inferiores.
- `itemCount` — el valor N en «N principales»; su unidad depende de `type`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Filtro Top 10: conservar los 2 elementos principales por "Suma de ventas" (índice 0 del campo de datos)
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // En su lugar, para un filtro basado en porcentaje, conservar el 30 % principal de los elementos:
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` y `FilterTop10` son dos funciones distintas. `AutoShow` establece en el campo de tabla dinámica el conjunto clásico de atributos `autoShow`, y este conjunto es respetado por todas las versiones de Excel desde Excel 97. `FilterTop10` escribe una entrada `PivotFilter` moderna, que requiere Excel 2007 o posterior. Al abrir un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utiliza el filtro moderno muestra todos los elementos. Para los documentos que deban procesarse de ida y vuelta con herramientas heredadas, se recomienda `Top10AutoShow`; para los libros de trabajo modernos, se recomienda `FilterTop10`, porque se combina con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/cpp/filter-by-label-or-value-of-pivot-table/)
- [Agregar campos de fila y columna a una tabla dinámica](/cells/es/cpp/pivot-table-add-row-and-column-fields/)
- [Agrupar campos en una tabla dinámica](/cells/es/cpp/group-pivot-fields-in-the-pivot-table/)
- [Actualizar una tabla dinámica](/cells/es/cpp/refresh-pivot-table/)
- [Agregar un campo de página en una tabla dinámica](/cells/es/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}