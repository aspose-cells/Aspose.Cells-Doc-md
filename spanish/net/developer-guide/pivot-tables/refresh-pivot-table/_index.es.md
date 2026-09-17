---
title: Actualizar Tablas Dinámicas y Cachés de Tablas Dinámicas en Aspose.Cells for .NET
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for .NET utilizando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
linktitle: Actualizar Tablas Dinámicas
keywords: Aspose.Cells, .NET, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece una API de actualización en capas que le permite recargar datos de tablas dinámicas en cuatro niveles diferentes — desde todo el libro de trabajo hasta una sola tabla dinámica. A partir de **Aspose.Cells for .NET v26.7**, el método heredado `PivotTable.RefreshData()` está marcado como obsoleto y debe reemplazarse con las APIs más eficientes y conscientes de la caché descritas en este artículo.
{{% /alert %}}

## Introducción
Actualizar una tabla dinámica rara vez es una operación única. En segundo plano, Aspose.Cells mantiene una cadena de datos en capas que conecta sus datos de origen originales con los valores representados que ve en la hoja de cálculo. Comprender esta cadena es clave para elegir la API de actualización adecuada para cualquier situación.
La cadena de datos de cuatro capas es:
1. **Origen de Datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **Tabla Dinámica** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solo* desde su `PivotCache`, nunca directamente desde el origen de datos.
4. **Celdas** — las `Cells` de la hoja de cálculo en las que la `PivotTable` representa sus valores calculados y estilos.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enumeración `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de la versión 26.7, `PivotCache.Refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que residen en rangos de hojas de cálculo. Los orígenes externos (bases de datos, conexiones externas, etc.) aún no se pueden actualizar mediante la API de caché.
{{% /alert %}}

Debido a esta cadena, existen dos rutas fundamentales de actualización en Aspose.Cells:
- **`PivotTable.CalculateData()`** — recalcula la visualización de una `PivotTable` a partir de los datos ya almacenados en caché, sin realizar un viaje de ida y vuelta al origen de datos.
Todos los escenarios de este artículo usan datos de origen de celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Inicio Rápido
Si solo necesita el código más breve posible que actualice cada tabla dinámica del libro, basta con una sola llamada:

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Todo lo demás en este artículo explica cuándo elegir una API más restringida en su lugar.

## Directivas Using Requeridas
Todos los ejemplos de C# de este artículo comienzan con las siguientes tres directivas using porque los tipos de tablas dinámicas se encuentran en el espacio de nombres `Aspose.Cells.Pivot`:
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Actualizar Todas las Tablas Dinámicas del Libro de Trabajo
Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica del libro reflejen los datos de origen más recientes, la API más sencilla y completa es `Workbook.RefreshAll()`. Una sola llamada recorre todo el libro de trabajo: actualiza cada `PivotCache` desde su origen y luego recalcula cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales de documentos completos donde el rendimiento no es una preocupación.
El siguiente ejemplo crea un libro de trabajo con un rango de origen de Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores de origen y luego usa `RefreshAll()` para actualizar todo en una sola llamada.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Crear un nuevo libro de trabajo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Escribir la fila de encabezado en las celdas A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Escribir las filas de datos en las celdas A2:C9 (8 filas de datos de frutas entre 2020 y 2021)
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
// Actualizar todas las tablas dinámicas / caché dinámica del libro de trabajo
workbook.RefreshAll();
// Guardar el libro de trabajo
workbook.Save("output.xlsx");
```

## Actualizar Todas las Tablas Dinámicas en una Sola Hoja de Cálculo
A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica; por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas de cálculo no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells ofrece `Worksheet.RefreshPivotTables()`, que está limitada a una sola instancia de `Worksheet`.

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
Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de qué cambió realmente: los datos de origen subyacentes, o solo la configuración de visualización/disposición de la propia tabla dinámica.

### Cambiaron los Datos de Origen — Use `PivotCache.Refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.PivotCache.Refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

### Solo Cambió la Vista/Disposición — Use `CalculateData()`
Si los datos de origen *no* han cambiado, pero solo se ha modificado la configuración de visualización o disposición de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente, o se ha activado una configuración de actualización al abrir), no es necesario volver al origen de datos. La caché ya contiene los datos correctos; solo es necesario recalcular la `PivotTable` ya representada. En este caso, `pivotTable.CalculateData()` es la opción correcta.
El siguiente ejemplo modifica una propiedad no relacionada con el origen de la tabla dinámica y luego llama a `CalculateData()` para volver a representarla desde la caché existente.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Escribir fila de encabezado Fruit / Year / Amount
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
// Agregar una tabla dinámica llamada "Pivot1" ubicada en la celda de destino E3, con origen en A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// Asignar campos: Fruit a Fila, Year a Columna, Amount a Datos
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Modificar una propiedad de vista/diseño — este es un cambio solo de presentación,
// por lo que NO requiere releer los datos de origen a través de PivotCache.Refresh().
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) desde los
// datos ya almacenados en el PivotCache. Como los datos de origen no cambiaron,
// no se realiza un viaje de ida y vuelta al origen — solo se recalculan los valores en caché
// en las celdas de la hoja de cálculo.
pivotTable.CalculateData();
// Guardar el libro en disco
workbook.Save("output.xlsx");
```

Un libro de trabajo a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas — por ejemplo, antes de realizar una actualización por lotes, o para diagnosticar el impacto de la caché compartida — use `PivotCache.GetPivotTables()`. Este método devuelve la colección de cada `PivotTable` que depende de la caché indicada.

## Migración desde la Obsoleta `PivotTable.RefreshData()`
Antes de Aspose.Cells for .NET v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica individualmente. A partir de la versión 26.7, ese método está marcado como **obsoleto** y debe reemplazarse con las APIs conscientes de la caché descritas anteriormente.
Hay dos razones por las que el enfoque `RefreshData()` por tabla es problemático en libros de trabajo reales:
- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
Los reemplazos recomendados son:
El siguiente ejemplo demuestra el nuevo patrón eficiente para libros de trabajo con varias tablas dinámicas que comparten una sola caché.

## ¿Qué API de Actualización Debo Usar?
La tabla siguiente resume las APIs de actualización disponibles y cuándo elegir cada una.
| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro de trabajo | `Workbook.RefreshAll()` | Una sola llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una hoja | `Worksheet.RefreshPivotTables()` | Limitada a una hoja de cálculo. |
| Los datos de origen cambiaron para una caché | `pivotTable.PivotCache.Refresh()` | Actualiza TODAS las tablas dinámicas en esa caché compartida. |
| Solo cambió la configuración de vista/disposición | `pivotTable.CalculateData()` | Evita el viaje innecesario al origen. |
| Listar todas las tablas dinámicas en una caché compartida | `pivotCache.GetPivotTables()` | Úselo para enumerar antes de una actualización masiva. |
En la práctica, prefiera las APIs basadas en caché sobre la obsoleta `RefreshData()` por tabla. Son conscientes de las cachés compartidas, evitan lecturas redundantes del origen y le permiten elegir el alcance más pequeño que satisfaga su requisito de actualización.

## Errores Comunes
- **Olvidar actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores representados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica las celdas de origen, llame a `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) antes de `Workbook.Save()`, de lo contrario el archivo guardado aún contendrá los valores agregados antiguos.
- **Llamar a la obsoleta `RefreshData()` por tabla.** En la versión 26.7, `PivotTable.RefreshData()` está marcada como obsoleta y vuelve a obtener el origen en cada llamada. Con varias tablas dinámicas que comparten una caché, esto significa N lecturas redundantes del origen. Reemplácelo con una sola llamada a `PivotCache.Refresh()` seguida de `CalculateData()` por tabla.
- **Actualizar cuando solo cambió la disposición.** Si solo cambió la vista de una tabla dinámica (orden de columnas, `ConsolidationFunction`, etc.) sin tocar los datos de origen, `PivotCache.Refresh()` es innecesaria y lenta. Llame a `pivotTable.CalculateData()` para volver a representar desde la caché existente.
- **Origen externo no admitido por `PivotCache.Refresh()`.** Si el origen de la tabla dinámica proviene de una conexión externa (base de datos, cubo OLAP, etc.), `PivotCache.Refresh()` no puede actualizarla en la versión 26.7 — actualmente solo admite los tipos de origen `Sheet` y `Consolidation`. Para orígenes externos, vuelva a abrir el libro de trabajo o reconstruya la caché desde el origen.

{{< app/cells/assistant language="csharp" >}}