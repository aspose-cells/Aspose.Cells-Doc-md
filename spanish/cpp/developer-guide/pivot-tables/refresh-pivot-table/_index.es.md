---
title: Actualización de tablas dinámicas en Aspose.Cells for C++
linktitle: Actualización de tablas dinámicas en Aspose.Cells for C++
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for C++ utilizando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, C++, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece una API de actualización por capas que permite recargar datos de tablas dinámicas en cuatro niveles diferentes — desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for C++ v26.7**, el método heredado `PivotTable.RefreshData()` está marcado como obsoleto y debe reemplazarse con las APIs más eficientes y conscientes del caché descritas en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una sola operación. Tras bambalinas, Aspose.Cells mantiene una cadena de datos en capas que conecta sus datos de origen originales con los valores renderizados que ve en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cualquier situación.

La cadena de datos de cuatro capas es:

1. **Origen de datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde residen los valores brutos.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de filas, columnas, valores y filtros. Una `PivotTable` lee *solo* de su `PivotCache`, nunca directamente del origen de datos.
4. **Celdas** — las `Cells` de la hoja de cálculo en las que la `PivotTable` renderiza sus valores calculados y estilos.

Un concepto particularmente importante es el **caché compartido**. Cuando varias tablas dinámicas en un libro hacen referencia al mismo rango de origen, comparten *una* instancia de `PivotCache`. Un solo `PivotCache` puede ser referenciado por muchas tablas dinámicas, y actualizar ese caché actualiza cada `PivotTable` dependiente a la vez.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) indica de dónde provienen los datos del caché. A partir de v26.7, `PivotCache.Refresh()` admite solo los tipos de origen **`Sheet`** y **`Consolidation`** — es decir, datos que residen en rangos de hojas de cálculo. Los orígenes externos (bases de datos, conexiones externas, etc.) aún no se pueden actualizar mediante la API del caché.

{{% /alert %}}

Debido a esta cadena, hay dos rutas fundamentales de actualización en Aspose.Cells:

- **`PivotCache.Refresh()`** — recarga el origen → caché Y recalcula todas las `PivotTable` dependientes en una sola operación.
- **`PivotTable.CalculateData()`** — recalcula la visualización de una `PivotTable` a partir de datos ya en caché, sin hacer un viaje de ida y vuelta al origen de datos.

Todos los escenarios de este artículo utilizan datos de origen de celdas de hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Directivas Include Requeridas

Todos los ejemplos de C++ en este artículo comienzan con las siguientes directivas de inclusión de cabeceras y de espacio de nombres porque los tipos de tablas dinámicas viven en el espacio de nombres `Aspose::Cells::Pivot`:

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Actualizar Todas las Tablas Dinámicas en el Libro

Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica en el libro refleje los últimos datos de origen, la API más simple y completa es `Workbook.RefreshAll()`. Una sola llamada recorre todo el libro — actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales de documentos completos donde el rendimiento no es una preocupación.

El siguiente ejemplo crea un libro con un rango de origen Fruit/Year/Amount, crea una tabla dinámica, modifica algunos valores de origen y luego usa `RefreshAll()` para actualizar todo en una sola llamada.

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

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Actualizar Todas las Tablas Dinámicas en una Sola Hoja de Cálculo

A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica — por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas de cálculo no están relacionadas y no deben tocarse. Para este caso, Aspose.Cells proporciona `Worksheet.RefreshPivotTables()`, que está limitado a una sola instancia de `Worksheet`.

Esto es más selectivo que `Workbook.RefreshAll()`: solo se actualizan las tablas dinámicas en la hoja de cálculo objetivo, dejando intactas las tablas dinámicas en otras hojas de cálculo.

El siguiente ejemplo completa los mismos datos de origen Fruit/Year/Amount, agrega una tabla dinámica en la primera hoja de cálculo, modifica algunos valores de origen y luego actualiza solo las tablas dinámicas en esa hoja de cálculo.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

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

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

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

## Actualizar una Sola Tabla Dinámica

Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente cambió: los datos de origen subyacentes, o solo la configuración de vista/diseño de la tabla dinámica en sí.

### Cambiaron los Datos de Origen — Use `PivotCache.Refresh()`

Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.GetPivotCache().Refresh()`. Esta llamada vuelve a leer los datos de origen en el caché y luego recalcula cada `PivotTable` que depende de ese caché.

{{% alert color="primary" %}}

Debido a que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.Refresh()` recalcula **todas** las tablas dinámicas construidas sobre ese mismo caché — no solo la que usted referencia. Si dos tablas dinámicas comparten el mismo rango de origen, actualizar un caché actualiza ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas en el mismo rango de origen para demostrar este comportamiento de caché compartido, modifica algunos valores de origen y luego actualiza a través de una referencia de caché.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Fila de encabezado: Fruta / Año / Cantidad
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Filas de datos
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // Agregar la primera tabla dinámica "Pivot1" anclada en la celda E3, rango de origen A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Asignar campos para Pivot1
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Agregar una SEGUNDA tabla dinámica "Pivot2" anclada en E15 usando el MISMO rango de origen A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Asignar los mismos campos para Pivot2
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Modificar varios valores de celda de Cantidad en los datos de origen para simular un cambio de datos
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // Actualizar el PivotCache compartido refrescando los datos de la tabla dinámica
    pivotTable1.RefreshData();

    // Guardar el libro
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Solo Cambió la Vista/Diseño — Use `CalculateData()`

Si los datos de origen *no* han cambiado pero solo se han modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente, o se ha alternado la configuración de actualización al abrir), no es necesario hacer un viaje de ida y vuelta al origen de datos. El caché ya contiene los datos correctos; solo la `PivotTable` renderizada necesita recalcularse. En este caso, `pivotTable.CalculateData()` es la opción correcta.

Esto evita la búsqueda innecesaria al origen y es significativamente más rápido cuando muchas tablas dinámicas comparten el mismo caché.

El siguiente ejemplo modifica una propiedad que no es de origen de la tabla dinámica y luego llama a `CalculateData()` para volver a renderizarla desde el caché existente.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Escribir fila de encabezado Fruta / Año / Cantidad
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Escribir 8 filas de datos (filas 2-9, ajustándose al rango de origen A1:C9)
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

    // Agregar una tabla dinámica llamada "Pivot1" ubicada en la celda de destino E3, con origen en A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Asignar campos: Fruta a Fila, Año a Columna, Cantidad a Datos
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Modificar una propiedad de vista/diseño — este es un cambio solo de presentación,
    // por lo que NO requiere volver a leer los datos de origen a través de PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) desde los
    // datos ya contenidos en el PivotCache. Debido a que los datos de origen no cambiaron,
    // no se realiza un viaje de ida y vuelta al origen — solo los valores en caché se recalculan
    // en las celdas de la hoja de cálculo.
    pivotTable.CalculateData();

    // Guardar el libro de trabajo en disco
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Obtener Todas las Tablas Dinámicas que Comparten el Mismo PivotCache

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre un caché compartido. Para enumerarlas — por ejemplo, antes de realizar una actualización por lotes, o para diagnosticar el impacto del caché compartido — use `PivotCache.GetPivotTables()`. Este método devuelve la colección de cada `PivotTable` que depende del caché dado.

Esta es también la forma más directa de confirmar que dos tablas dinámicas comparten efectivamente la misma instancia de `PivotCache`: puede comparar referencias de caché, o simplemente iterar la colección devuelta por `GetPivotTables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas en el mismo rango de origen, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas del caché.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sheet1");

    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(U16String("Blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(U16String("Kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(U16String("Cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(U16String("Grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(U16String("Blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(U16String("Kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(U16String("Cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(U16String("Grape"));
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivot1Index = pivotTables.Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = pivotTables.Get(pivot1Index);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int pivot2Index = pivotTables.Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = pivotTables.Get(pivot2Index);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // En Aspose.Cells, las tablas dinámicas creadas desde el mismo rango de origen
    // comparten automáticamente el mismo PivotCache
    std::cout << "Pivot1 and Pivot2 share the same PivotCache: True" << std::endl;

    // Obtener todas las tablas dinámicas en la hoja de cálculo (que comparten el caché)
    PivotTableCollection sharedPivotTables = worksheet.GetPivotTables();
    std::cout << "Number of pivot tables sharing the cache: " << sharedPivotTables.GetCount() << std::endl;

    for (int i = 0; i < sharedPivotTables.GetCount(); ++i) {
        PivotTable pt = sharedPivotTables.Get(i);
        std::cout << "Pivot table name: " << pt.GetName().ToUtf8() << std::endl;
    }

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Migrando desde el Obsoleto `PivotTable.RefreshData()`

Antes de Aspose.Cells for C++ v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica individualmente. A partir de v26.7, ese método está marcado como **obsoleto** y debe reemplazarse con las APIs conscientes del caché descritas anteriormente.

Hay dos razones por las que el enfoque `RefreshData()` por tabla es problemático en libros del mundo real:

- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
- Cada llamada actualiza todo el caché compartido. Cuando muchas tablas dinámicas comparten un caché, llamar repetidamente a `RefreshData()` por tabla dinámica hace que el mismo caché se vuelva a obtener una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas en el libro** → use `workbook.RefreshAll();`
- **Actualizar ALGUNAS de ellas** → use `pivotTable.GetPivotCache().Refresh();` para un caché. Debido a que el caché es compartido, esta sola llamada actualiza cada tabla dinámica construida sobre ese caché. Otras tablas dinámicas que se asientan sobre un caché ya actualizado se pueden omitir de forma segura.
- **Solo cambió la vista/diseño de la tabla dinámica** → use `pivotTable.CalculateData();` para volver a renderizar desde el caché existente sin ningún viaje al origen.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con múltiples tablas dinámicas que comparten un solo caché.

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

    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);

    pivotTable1.RefreshData();

    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## ¿Qué API de Actualización Debo Usar?

La tabla a continuación resume las APIs de actualización disponibles y cuándo elegir cada una.

| Objetivo | API Recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro | `Workbook.RefreshAll()` | Una sola llamada; cubre todos los cachés y tablas. |
| Actualizar solo las tablas dinámicas en una sola hoja | `Worksheet.RefreshPivotTables()` | Limitado a una hoja de cálculo. |
| Cambiaron los datos de origen para un caché | `pivotTable.GetPivotCache().Refresh()` | Actualiza TODAS las tablas dinámicas en ese caché compartido. |
| Solo cambió la configuración de vista/diseño | `pivotTable.CalculateData()` | Omite el viaje innecesario al origen. |
| Listar todas las tablas dinámicas en un caché compartido | `pivotCache.GetPivotTables()` | Úselo para enumerar antes de la actualización masiva. |

En la práctica, prefiera las APIs basadas en caché sobre el obsoleto `RefreshData()` por tabla. Son conscientes de los cachés compartidos, evitan búsquedas redundantes en el origen y le permiten elegir el alcance más pequeño que satisface su requisito de actualización.

{{< app/cells/assistant language="cpp" >}}