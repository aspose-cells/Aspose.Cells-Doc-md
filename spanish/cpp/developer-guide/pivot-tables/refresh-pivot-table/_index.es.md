---
title: Actualización de tablas dinámicas en Aspose.Cells for C++
linktitle: Actualización de tablas dinámicas en Aspose.Cells for C++
description: Aprenda cómo actualizar tablas dinámicas en Aspose.Cells for C++ utilizando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, C++, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells ofrece una API de actualización por capas que le permite recargar datos de tablas dinámicas en cuatro niveles diferentes, desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for C++ v26.7**, el método heredado `PivotTable.RefreshData()` queda marcado como obsoleto y debe reemplazarse por las APIs más eficientes y conscientes de la caché que se describen en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una operación única. Entre bastidores, Aspose.Cells mantiene una cadena de datos por capas que conecta los datos de origen originales con los valores renderizados que ve en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cualquier situación.

La cadena de datos de cuatro capas es:

1. **Fuente de datos** — los rangos originales de la hoja de cálculo, consulta a base de datos o rango de consolidación donde viven los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y se agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Un `PivotTable` lee *solo* desde su `PivotCache`, nunca directamente desde la fuente de datos.
4. **Celdas** — las `Cells` de la hoja de cálculo en las que el `PivotTable` renderiza sus valores calculados y estilos.

Un concepto particularmente importante es la **caché compartida**. Cuando varias tablas dinámicas en un libro hacen referencia al mismo rango de origen, comparten *una* instancia de `PivotCache`. Una sola `PivotCache` puede ser referenciada por muchas tablas dinámicas, y al actualizar esa caché se actualizan todas las `PivotTable` dependientes a la vez.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de v26.7, `PivotCache.Refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que viven en rangos de hojas de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no se pueden actualizar mediante la API de caché.

{{% /alert %}}

Debido a esta cadena, hay dos rutas fundamentales de actualización en Aspose.Cells:

- **`PivotCache.Refresh()`** — recarga origen → caché Y recalcula todas las `PivotTable` dependientes en una sola operación.
- **`PivotTable.CalculateData()`** — recalcula la visualización de una sola `PivotTable` desde los datos ya almacenados en caché, sin volver a la fuente de datos.

Todos los escenarios de este artículo utilizan datos de origen en celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Directivas de inclusión requeridas

Todos los ejemplos en C++ de este artículo comienzan con las siguientes directivas de inclusión de cabecera y espacio de nombres porque los tipos de tablas dinámicas se encuentran en el espacio de nombres `Aspose::Cells::Pivot`:

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Actualizar todas las tablas dinámicas del libro

Cuando necesite asegurarse de que cada caché de tabla dinámica y cada tabla dinámica del libro reflejen los datos de origen más recientes, la API más sencilla y completa es `Workbook.RefreshAll()`. Una sola llamada recorre todo el libro, actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento cuando el rendimiento no es un problema.

El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `RefreshAll()` para actualizarlo todo en una sola llamada.

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

    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Actualizar todas las tablas dinámicas en una sola hoja de cálculo

A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica; por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells proporciona `Worksheet.RefreshPivotTables()`, que está limitado a una sola instancia de `Worksheet`.

Esto es más selectivo que `Workbook.RefreshAll()`: solo se actualizan las tablas dinámicas de la hoja de cálculo objetivo, dejando intactas las tablas dinámicas en otras hojas.

El siguiente ejemplo rellena los mismos datos de origen Fruta/Año/Cantidad, agrega una tabla dinámica en la primera hoja de cálculo, modifica algunos valores de origen y luego actualiza solo las tablas dinámicas de esa hoja.

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

## Actualizar una sola tabla dinámica

Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente cambió: los datos de origen subyacentes, o solo la configuración de vista/diseño de la propia tabla dinámica.

### Cambiaron los datos de origen: use `PivotCache.Refresh()`

Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.GetPivotCache().Refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

{{% alert color="primary" %}}

Dado que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.Refresh()` recalcula **todas** las tablas dinámicas construidas sobre esa misma caché, no solo aquella a la que hace referencia. Si dos tablas dinámicas comparten el mismo rango de origen, actualizar una caché actualiza ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen para demostrar este comportamiento de caché compartida, modifica algunos valores de origen y luego actualiza mediante una referencia a la caché.

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

    // Actualizar el PivotCache compartido actualizando los datos de la tabla dinámica
    pivotTable1.RefreshData();

    // Guardar el libro
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Solo cambió la vista/diseño: use `CalculateData()`

Si los datos de origen *no* han cambiado pero solo se han modificado los ajustes de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente o se ha alternado un ajuste de actualización al abrir), no es necesario volver a la fuente de datos. La caché ya contiene los datos correctos; solo es necesario recalcular el `PivotTable` renderizado. En este caso, `pivotTable.CalculateData()` es la elección correcta.

Esto evita la obtención innecesaria de datos del origen y es significativamente más rápido cuando muchas tablas dinámicas comparten la misma caché.

El siguiente ejemplo modifica una propiedad que no es de origen de la tabla dinámica y luego llama a `CalculateData()` para volver a renderizarla desde la caché existente.

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

    // Asignar campos: Fruit a Fila, Year a Columna, Amount a Datos
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Modificar una propiedad de vista/diseño — este es un cambio solo de presentación,
    // por lo que NO requiere volver a leer los datos de origen mediante PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() vuelve a renderizar la visualización (datos + estilo) de ESTA tabla dinámica
    // a partir de los datos ya contenidos en PivotCache. Dado que los datos de origen no cambiaron,
    // no se realiza un ida y vuelta al origen — solo se recalculan los valores en caché
    // hacia las celdas de la hoja de cálculo.
    pivotTable.CalculateData();

    // Guardar el libro en disco
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Obtener todas las tablas dinámicas que comparten la misma PivotCache

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes, o para diagnosticar el impacto de la caché compartida, utilice `PivotCache.GetPivotTables()`. Este método devuelve la colección de cada `PivotTable` que depende de la caché dada.

Esta es también la forma más directa de confirmar que dos tablas dinámicas efectivamente comparten la misma instancia de `PivotCache`: puede comparar referencias de caché, o simplemente iterar la colección devuelta por `GetPivotTables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas de la caché.


## Migración desde el obsoleto `PivotTable.RefreshData()`

Antes de Aspose.Cells for C++ v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica individualmente. A partir de v26.7, ese método queda marcado como **obsoleto** y debe reemplazarse por las APIs conscientes de la caché descritas anteriormente.

Hay dos razones por las que el enfoque `RefreshData()` por tabla es problemático en libros reales:

- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
- Cada llamada actualiza toda la caché compartida. Cuando muchas tablas dinámicas comparten una caché, llamar repetidamente a `RefreshData()` por tabla dinámica hace que la misma caché se vuelva a obtener una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas del libro** → use `workbook.RefreshAll();`
- **Actualizar ALGUNAS de ellas** → use `pivotTable.GetPivotCache().Refresh();` para una caché. Debido a que la caché está compartida, esta única llamada actualiza todas las tablas dinámicas construidas sobre esa caché. Otras tablas dinámicas que se asientan sobre una caché ya actualizada se pueden omitir de forma segura.
- **Solo cambió la vista/diseño de la tabla dinámica** → use `pivotTable.CalculateData();` para volver a renderizar desde la caché existente sin ningún viaje de ida y vuelta al origen.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con varias tablas dinámicas que comparten una sola caché.

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


    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## ¿Qué API de actualización debo usar?

La tabla a continuación resume las APIs de actualización disponibles y cuándo elegir cada una.

| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro | `Workbook.RefreshAll()` | Una sola llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas en una sola hoja | `Worksheet.RefreshPivotTables()` | Limitado a una hoja de cálculo. |
| Cambiaron los datos de origen para una caché | `pivotTable.GetPivotCache().Refresh()` | Actualiza TODAS las tablas dinámicas en esa caché compartida. |
| Solo cambiaron los ajustes de vista/diseño | `pivotTable.CalculateData()` | Evita viajes innecesarios al origen. |
| Listar todas las tablas dinámicas en una caché compartida | `pivotCache.GetPivotTables()` | Úselo para enumerar antes de una actualización masiva. |

En la práctica, prefiera las APIs basadas en caché sobre el obsoleto `RefreshData()` por tabla. Son conscientes de las cachés compartidas, evitan obtenciones redundantes del origen y le permiten elegir el alcance más pequeño que satisface su requisito de actualización.

{{< app/cells/assistant language="cpp" >}}
