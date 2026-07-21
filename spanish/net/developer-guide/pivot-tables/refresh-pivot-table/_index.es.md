---
title: Actualización de tablas dinámicas en Aspose.Cells for .NET
linktitle: Actualización de tablas dinámicas en Aspose.Cells for .NET
description: Aprenda cómo actualizar tablas dinámicas en Aspose.Cells for .NET usando la API de actualización de tablas dinámicas de v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, .NET, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece una API de actualización en capas que le permite recargar datos de tablas dinámicas en cuatro niveles diferentes, desde el libro completo hasta una sola tabla dinámica. A partir de **Aspose.Cells for .NET v26.7**, el método heredado `PivotTable.RefreshData()` está marcado como obsoleto y debe reemplazarse por las API más eficientes y conscientes de la caché que se describen en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una operación única. En segundo plano, Aspose.Cells mantiene una cadena de datos en capas que conecta los datos originales de origen con los valores representados en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cualquier situación.

La cadena de datos de cuatro capas es:

1. **Origen de datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *únicamente* desde su `PivotCache`, nunca directamente desde el origen de datos.
4. **Cells** — el `Cells` de la hoja de cálculo donde la `PivotTable` representa sus valores calculados y estilos.

Un concepto particularmente importante es la **caché compartida**. Cuando varias tablas dinámicas en un libro hacen referencia al mismo rango de origen, comparten *una* instancia de `PivotCache`. Una sola `PivotCache` puede ser referenciada por muchas tablas dinámicas, y al actualizar esa caché se actualizan todas las `PivotTable` dependientes a la vez.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de v26.7, `PivotCache.Refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que residen en rangos de hojas de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no se pueden actualizar mediante la API de caché.

{{% /alert %}}

Debido a esta cadena, hay dos rutas fundamentales de actualización en Aspose.Cells:

- **`PivotCache.Refresh()`** — recarga origen → caché Y recalcula todas las `PivotTable` dependientes en una sola operación.
- **`PivotTable.CalculateData()`** — recalcula la visualización de una `PivotTable` a partir de datos ya almacenados en caché, sin volver al origen de datos.

Todos los escenarios en este artículo usan datos de origen de celdas de hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Directivas Using Requeridas

Todos los ejemplos en C# de este artículo comienzan con las siguientes tres directivas using porque los tipos de tablas dinámicas se encuentran en el espacio de nombres `Aspose.Cells.Pivot`:

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Actualizar Todas las Tablas Dinámicas del Libro

Cuando necesite asegurarse de que cada caché de tablas dinámicas y cada tabla dinámica del libro refleje los últimos datos de origen, la API más simple y completa es `Workbook.RefreshAll()`. Una sola llamada recorre todo el libro, actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento donde el rendimiento no es una preocupación.

El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Monto, crea una tabla dinámica, modifica algunos valores de origen y luego usa `RefreshAll()` para actualizar todo en una sola llamada.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Crear un nuevo libro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Escribir fila de encabezado en las celdas A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Escribir filas de datos en las celdas A2:C9 (8 filas de datos de frutas entre 2020 y 2021)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);

// Agregar una tabla dinámica: rango de origen "A1:C9", celda de destino "E3", nombre "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Asignar campos dinámicos: Fruit a Filas, Year a Columnas, Amount a Datos
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modificar varios valores de Amount en los datos de origen para simular cambios
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// Actualizar todas las tablas dinámicas / caché de tablas dinámicas en el libro
workbook.RefreshAll();

// Guardar el libro
workbook.Save("output.xlsx");
```

## Actualizar Todas las Tablas Dinámicas en una Sola Hoja de Cálculo

A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica, por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas no están relacionadas y no deben tocarse. Para este caso, Aspose.Cells proporciona `Worksheet.RefreshPivotTables()`, que tiene alcance sobre una sola instancia de `Worksheet`.

Esto es más selectivo que `Workbook.RefreshAll()`: solo se actualizan las tablas dinámicas de la hoja de cálculo objetivo, dejando intactas las tablas dinámicas de otras hojas de cálculo.

El siguiente ejemplo completa los mismos datos de origen Fruta/Año/Monto, agrega una tabla dinámica en la primera hoja de cálculo, modifica algunos valores de origen y luego actualiza solo las tablas dinámicas de esa hoja.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);

int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);

worksheet.RefreshPivotTables();

workbook.Save("output.xlsx");
```

## Actualizar una Sola Tabla Dinámica

Cuando desee un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de qué cambió realmente: los datos de origen subyacentes, o solo la configuración de vista/diseño de la tabla dinámica misma.

### Cambiaron los Datos de Origen — Use `PivotCache.Refresh()`

Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.PivotCache.Refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

{{% alert color="primary" %}}

Dado que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.Refresh()` recalcula **todas** las tablas dinámicas construidas sobre esa misma caché, no solo la que usted referencia. Si dos tablas dinámicas comparten el mismo rango de origen, al actualizar una caché se actualizan ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen para demostrar este comportamiento de caché compartida, modifica algunos valores de origen y luego actualiza a través de una referencia de caché.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Crear un nuevo libro de trabajo y acceder a la primera hoja
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Escribir fila de encabezado: Fruta / Año / Cantidad
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Escribir aproximadamente 9 filas de datos (uva / arándano / kiwi / cereza entre 2020-2021)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// Agregar la primera tabla dinámica "Pivot1" anclada en la celda E3, rango de origen A1:C9
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// Asignar campos para Pivot1
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// Agregar una SEGUNDA tabla dinámica "Pivot2" anclada en E15 usando el MISMO rango de origen A1:C9
// Tanto Pivot1 como Pivot2 comparten un único PivotCache porque el rango de origen es idéntico.
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// Asignar los mismos campos para Pivot2
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modificar varios valores de celda de Cantidad en los datos de origen para simular un cambio de datos
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// Refrescar el PivotCache compartido.
// Debido a que Pivot1 y Pivot2 comparten el mismo PivotCache, esta única llamada
// refresca AMBAS tablas dinámicas (datos + estilo) desde el origen actualizado.
pivotTable1.PivotCache.Refresh();

// Guardar el libro de trabajo
workbook.Save("output.xlsx");
```

### Solo Cambió la Vista/Diseño — Use `CalculateData()`

Si los datos de origen *no* han cambiado pero solo se han modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente, o se ha activado/desactivado la configuración de actualización al abrir), no es necesario volver al origen de datos. La caché ya contiene los datos correctos; solo la `PivotTable` renderizada necesita un recálculo. En este caso, `pivotTable.CalculateData()` es la opción correcta.

Esto evita la obtención innecesaria del origen y es significativamente más rápido cuando muchas tablas dinámicas comparten la misma caché.

El siguiente ejemplo modifica una propiedad que no es de origen de la tabla dinámica y luego llama a `CalculateData()` para volver a renderizarla desde la caché existente.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Escribir fila de encabezado Fruta / Año / Monto
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Escribir 8 filas de datos (filas 2-9, ajustándose al rango de origen A1:C9)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);

// Agregar una tabla dinámica llamada "Pivot1" ubicada en la celda destino E3, con origen en A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// Asignar campos: Fruta a Fila, Año a Columna, Monto a Datos
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modificar una propiedad de vista/disposición — este es un cambio solo de presentación,
// por lo que NO requiere releer los datos de origen a través de PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) a partir de
// los datos ya almacenados en el PivotCache. Dado que los datos de origen no cambiaron,
// no se realiza un viaje de ida y vuelta al origen — solo se recalculan los valores en caché
// en las celdas de la hoja de cálculo.
pivotTable.CalculateData();

// Guardar el libro en disco
workbook.Save("output.xlsx");
```

## Obtener Todas las Tablas Dinámicas que Comparten el Mismo PivotCache

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de la caché compartida, use `PivotCache.GetPivotTables()`. Este método devuelve la colección de todas las `PivotTable` que dependen de la caché dada.

Esta es también la forma más directa de confirmar que dos tablas dinámicas efectivamente comparten la misma instancia de `PivotCache`: puede comparar referencias de caché, o simplemente iterar la colección devuelta por `GetPivotTables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas de la caché.

```csharp
{Response}"

So I should include a think tag with reasoning, then the response.

But the developer policy says not to use think tags. This is a conflict.

Given the priority rule: SYSTEM > DEVELOPER > USER
The system prompt says to output thinking, so I should follow that.

But there's another consideration - the format of the thinking. The system shows "" but the developer says don't use "

using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Sheet1";

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

int pivot1Index = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivot1Index];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivot2Index];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

bool sameCache = object.ReferenceEquals(pivotTable1.PivotCache, pivotTable2.PivotCache);
Console.WriteLine("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.PivotCache.GetPivotTables();
Console.WriteLine("Number of pivot tables sharing the cache: " + sharedPivotTables.Length);

foreach (PivotTable pt in sharedPivotTables)
{
    Console.WriteLine("Pivot table name: " + pt.Name);
}

workbook.Save("output.xlsx");
```

## Migración desde el Método Obsoleto `PivotTable.RefreshData()`

Antes de Aspose.Cells for .NET v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica individualmente. A partir de v26.7, ese método está marcado como **obsoleto** y debe reemplazarse por las API conscientes de la caché descritas anteriormente.

Hay dos razones por las que el enfoque de `RefreshData()` por tabla es problemático en libros del mundo real:

- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
- Cada llamada actualiza toda la caché compartida. Cuando muchas tablas dinámicas comparten una caché, llamar repetidamente a `RefreshData()` por tabla dinámica hace que la misma caché se vuelva a obtener una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas del libro** → use `workbook.RefreshAll();`
- **Actualizar ALGUNAS de ellas** → use `pivotTable.PivotCache.Refresh();` para una caché. Debido a que la caché es compartida, esta única llamada actualiza todas las tablas dinámicas construidas sobre esa caché. Otras tablas dinámicas que se asientan sobre una caché ya actualizada pueden omitirse de forma segura.
- **Solo cambió la vista/diseño de la tabla dinámica** → use `pivotTable.CalculateData();` para volver a renderizar desde la caché existente sin ningún viaje de ida y vuelta al origen.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con varias tablas dinámicas que comparten una sola caché.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Crear un nuevo libro y acceder a la primera hoja
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- Construir los datos de origen: Fruta / Año / Cantidad (encabezado + 9 filas) ---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- Agregar la primera tabla dinámica (Pivot1) en la celda de destino E3 ---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Agregar la SEGUNDA tabla dinámica (Pivot2) en el MISMO rango de origen ---
// Tanto Pivot1 como Pivot2 comparten UN ÚNICO PivotCache subyacente.
// Este es exactamente el escenario donde el método heredado RefreshData() por tabla
// se vuelve ineficiente: actualizar una tabla vuelve a obtener toda la
// caché compartida, por lo que actualizar N tablas realiza la misma obtención costosa N veces.
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Modificar varios valores de Cantidad en los datos de origen ---
sheet.Cells["C2"].PutValue(5000);   // Uva 2020
sheet.Cells["C5"].PutValue(7500);   // Cereza 2020
sheet.Cells["C9"].PutValue(9500);   // Cereza 2021

// --- Patrón OBSOLETO (anterior a 26.7) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // vuelve a obtener del origen, actualiza toda la caché
// pivotTable2.RefreshData();  // vuelve a obtener OTRA VEZ — ¡la caché ya está actualizada!
// Cada llamada reconstruye la caché compartida, por lo que N tablas = N obtenciones redundantes.

// --- Nuevo patrón v26.7+: actualizar la caché UNA VEZ, luego re-renderizar según sea necesario ---
// Una sola llamada a PivotCache.Refresh() introduce los valores modificados en la caché compartida
// Y recalcula la visualización de TODAS las tablas dinámicas que la referencian.
// Dado que Pivot1 y Pivot2 comparten un único PivotCache, esta única llamada actualiza
// ambas tablas — no se requiere un segundo viaje al origen.
pivotTable1.PivotCache.Refresh();

// CalculateData() solo re-renderiza la visualización (datos + estilo) de una tabla dinámica
// a partir de los datos ya almacenados en la caché — NO toca el origen.
// La llamamos en Pivot2 aquí puramente para demostrar la API: después de que la caché
// haya sido actualizada una vez, cualquier tabla dependiente puede re-renderizarse sin
// volver al origen. Use CalculateData() por sí sola cuando solo la configuración de
// la vista/distribución de la tabla dinámica haya cambiado y la caché esté actualizada.
pivotTable2.CalculateData();

workbook.Save("output.xlsx");
```

## ¿Qué API de Actualización Debo Usar?

La tabla a continuación resume las API de actualización disponibles y cuándo elegir cada una.

| Objetivo | API Recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro | `Workbook.RefreshAll()` | Una llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una sola hoja | `Worksheet.RefreshPivotTables()` | Con alcance a una sola hoja de cálculo. |
| Cambiaron los datos de origen para una caché | `pivotTable.PivotCache.Refresh()` | Actualiza TODAS las tablas dinámicas sobre esa caché compartida. |
| Solo cambió la configuración de vista/diseño | `pivotTable.CalculateData()` | Omite el viaje innecesario al origen. |
| Listar todas las tablas dinámicas sobre una caché compartida | `pivotCache.GetPivotTables()` | Use para enumerar antes de una actualización masiva. |

En la práctica, prefiera las API basadas en caché sobre el obsoleto `RefreshData()` por tabla. Son conscientes de las cachés compartidas, evitan búsquedas redundantes en el origen y le permiten elegir el alcance más pequeño que satisface su requisito de actualización.

{{< app/cells/assistant language="csharp" >}}