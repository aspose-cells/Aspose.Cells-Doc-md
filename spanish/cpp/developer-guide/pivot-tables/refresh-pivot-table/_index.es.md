---
title: Actualizar Tablas Dinámicas y Cachés de Tablas Dinámicas en Aspose.Cells for C++
linktitle: Actualizar Tablas Dinámicas y Cachés de Tablas Dinámicas en Aspose.Cells for C++
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for C++ utilizando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, C++, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece una API de actualización por capas que permite recargar los datos de las tablas dinámicas en cuatro niveles diferentes, desde todo el libro de trabajo hasta una sola tabla dinámica. A partir de **Aspose.Cells for C++ v26.7**, el método heredado `PivotTable.RefreshData()` está marcado como obsoleto y debe reemplazarse por las API más eficientes y conscientes del caché descritas en este artículo.
{{% /alert %}}

## Introduction
Actualizar una tabla dinámica rara vez es una operación única. En segundo plano, Aspose.Cells mantiene una cadena de datos por capas que conecta sus datos de origen originales con los valores representados que se ven en la hoja de cálculo. Comprender esta cadena es clave para elegir la API de actualización adecuada en cualquier situación.
La cadena de datos de cuatro capas es:
1. **Fuente de datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de filas, columnas, valores y filtros. Un `PivotTable` lee *únicamente* desde su `PivotCache`, nunca directamente desde la fuente de datos.
4. **Cells** — el `Cells` de la hoja de cálculo en el que `PivotTable` representa sus valores calculados y estilos.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica de dónde provienen los datos del caché. A partir de v26.7, `PivotCache.Refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que residen en rangos de hojas de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no pueden actualizarse a través de la API de caché.
Debido a esta cadena, existen dos rutas fundamentales de actualización en Aspose.Cells:
- **`PivotTable.CalculateData()`** — recalcula la visualización de un `PivotTable` a partir de datos ya almacenados en caché, sin volver a la fuente de datos.
Todos los escenarios de este artículo utilizan datos de origen en celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.
{{% /alert %}}

## Quick Start
Si solo necesita el código más breve posible que actualice cada tabla dinámica del libro de trabajo, basta con una sola llamada:

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Todo lo demás en este artículo explica cuándo elegir una API más restringida en su lugar.

## Required Include Directives
Todos los ejemplos de C++ en este artículo comienzan con las siguientes directivas de inclusión de encabezados y espacios de nombres, ya que los tipos de tablas dinámicas se encuentran en el espacio de nombres `Aspose::Cells::Pivot`:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Refresh All Pivot Tables in the Workbook
Cuando necesita asegurarse de que cada caché de tablas dinámicas y cada tabla dinámica del libro de trabajo refleje los datos de origen más recientes, la API más sencilla y completa es `Workbook.RefreshAll()`. Una sola llamada recorre todo el libro de trabajo: actualiza cada `PivotCache` desde su origen y luego recalcula cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento cuando el rendimiento no es una preocupación.
El siguiente ejemplo crea un libro de trabajo con un rango de origen de Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `RefreshAll()` para actualizar todo en una sola llamada.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);
    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);
    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);
    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);
    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);
    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);
    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);
    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);
    pivotTable.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh All Pivot Tables on a Single Worksheet
A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica; por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas de cálculo no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells proporciona `Worksheet.RefreshPivotTables()`, que está limitada a una sola instancia de `Worksheet`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);
    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);
    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);
    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);
    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);
    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);
    worksheet.RefreshPivotTables();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh a Single Pivot Table
Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente haya cambiado: los datos de origen subyacentes o solo la configuración de la vista o el diseño de la propia tabla dinámica.

### Source Data Changed — Use `PivotCache.Refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.GetPivotCache().Refresh()`. Esta llamada vuelve a leer los datos de origen en el caché y luego recalcula cada `PivotTable` que depende de ese caché.

### Only View/Layout Changed — Use `CalculateData()`
Si los datos de origen *no* han cambiado pero solo se han modificado la vista o la configuración de diseño de la tabla dinámica (por ejemplo, un campo se ha movido a otra área o se ha cambiado una opción de actualización al abrir), no es necesario volver a la fuente de datos. El caché ya contiene los datos correctos; solo necesita recalcularse el `PivotTable` representado. En este caso, `pivotTable.CalculateData()` es la elección correcta.
El siguiente ejemplo modifica una propiedad no relacionada con el origen de la tabla dinámica y luego llama a `CalculateData()` para volver a representarla desde el caché existente.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Write Fruit / Year / Amount header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);
 // Add a pivot table placed at destination cell E3, sourcing from A1:C9
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    // Assign fields: Fruit to Row, Year to Column, Amount to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modify a view/layout property — this is a presentation-only change,
    // so it does NOT require re-reading the source data through PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() re-renders THIS pivot table's display (data + style) from the
    // data already held in the PivotCache. Because the source data did not change,
    // no round-trip to the source is performed — only the cached values are recalculated
    // into worksheet cells.
    pivotTable.CalculateData();
    // Save the workbook to disk
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Un libro de trabajo a menudo contiene muchas tablas dinámicas que se asientan sobre un caché compartido. Para enumerarlas (por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de un caché compartido), use `PivotCache.GetPivotTables()`. Este método devuelve la colección de todos los `PivotTable` que dependen del caché dado.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Antes de Aspose.Cells for C++ v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica individualmente. A partir de v26.7, ese método está marcado como **obsoleto** y debe reemplazarse por las API conscientes del caché descritas anteriormente.
Hay dos razones por las que el enfoque por tabla `RefreshData()` resulta problemático en libros de trabajo del mundo real:
- Vuelve a obtener datos del origen *cada vez que se llama*, incluso cuando el origen no ha cambiado.
Los reemplazos recomendados son:
El siguiente ejemplo demuestra el nuevo patrón eficiente para libros de trabajo con varias tablas dinámicas que comparten un único caché.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");
    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);
    PivotTable pivotTable1 = sheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotTable pivotTable2 = sheet.GetPivotTables().Add(u"A1:C9", 14, 4);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");
    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);
    pivotTable2.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Which Refresh API Should I Use?
La tabla siguiente resume las API de actualización disponibles y cuándo elegir cada una.
| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo el libro de trabajo | `Workbook.RefreshAll()` | Una sola llamada; cubre todos los cachés y tablas. |
| Actualizar solo las tablas dinámicas de una hoja | `Worksheet.RefreshPivotTables()` | Limitado a una hoja de cálculo. |
| Cambiaron los datos de origen para un caché | `pivotTable.GetPivotCache().Refresh()` | Actualiza TODAS las tablas dinámicas de ese caché compartido. |
| Solo cambió la configuración de vista o diseño | `pivotTable.CalculateData()` | Evita viajes innecesarios al origen. |
| Listar todas las tablas dinámicas de un caché compartido | `pivotCache.GetPivotTables()` | Úselo para enumerar antes de una actualización masiva. |
En la práctica, prefiera las API basadas en caché sobre el `RefreshData()` obsoleto por tabla. Son conscientes de los cachés compartidos, evitan búsquedas redundantes en el origen y le permiten elegir el alcance más pequeño que satisface su requisito de actualización.

## Common Pitfalls
- **Olvidar actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores representados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica celdas de origen, llame a `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) antes de `Workbook.Save()`. De lo contrario, el archivo guardado seguirá conteniendo los valores agregados antiguos.
- **Llamar al `RefreshData()` obsoleto por tabla.** En v26.7, `PivotTable.RefreshData()` está marcado como obsoleto y vuelve a obtener el origen en cada llamada. Con varias tablas dinámicas que comparten un caché, esto significa N búsquedas redundantes en el origen. Reemplácelo con una sola llamada a `PivotCache.Refresh()` seguida de `CalculateData()` por tabla.
- **Actualizar cuando solo cambió el diseño.** Si solo cambió la vista de una tabla dinámica (orden de columnas, `ConsolidationFunction`, etc.) sin tocar los datos de origen, `PivotCache.Refresh()` es innecesario y lento. Llame a `pivotTable.CalculateData()` para volver a renderizar desde el caché existente.
- **Fuente externa no admitida por `PivotCache.Refresh()`.** Si la fuente de la tabla dinámica proviene de una conexión externa (base de datos, cubo OLAP, etc.), `PivotCache.Refresh()` no puede actualizarla en v26.7; actualmente solo admite los tipos de origen `Sheet` y `Consolidation`. Para fuentes externas, vuelva a abrir el libro de trabajo o reconstruya el caché desde el origen.

{{< app/cells/assistant language="cpp" >}}