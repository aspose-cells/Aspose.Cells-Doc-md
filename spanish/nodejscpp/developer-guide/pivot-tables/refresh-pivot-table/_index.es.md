---
title: Actualizar Tablas Dinámicas y Caches de Tablas Dinámicas en Aspose.Cells para Node.js mediante C++
linktitle: Actualizar Tablas Dinámicas y Caches de Tablas Dinámicas en Aspose.Cells para Node.js mediante C++
description: Aprenda cómo actualizar tablas dinámicas en Aspose.Cells para Node.js mediante C++ utilizando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, Node.js mediante C++, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells proporciona una API de actualización por capas que permite recargar los datos de las tablas dinámicas en cuatro ámbitos diferentes: desde todo el libro de trabajo hasta una única tabla dinámica. A partir de **Aspose.Cells para Node.js mediante C++ v26.7**, el método heredado `PivotTable.RefreshData()` está marcado como obsoleto y debe reemplazarse por las APIs más eficientes y conscientes del cache descritas en este artículo.
{{% /alert %}}

## Introduction
Actualizar una tabla dinámica rara vez es una operación individual. En segundo plano, Aspose.Cells mantiene una cadena de datos en capas que conecta los datos de origen originales con los valores renderizados que se muestran en la hoja de cálculo. Comprender esta cadena es clave para elegir la API de actualización adecuada para cualquier situación.
La cadena de datos de cuatro capas es:
1. **Origen de datos** — los rangos originales de la hoja de cálculo, la consulta de base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Un `PivotTable` lee *únicamente* desde su `PivotCache`, nunca directamente desde el origen de datos.
4. **Cells** — los `Cells` de la hoja de cálculo donde el `PivotTable` renderiza sus valores calculados y estilos.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) indica el origen de los datos del cache. A partir de v26.7, `PivotCache.refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`** — es decir, datos que residen en rangos de hojas de cálculo. Los orígenes externos (bases de datos, conexiones externas, etc.) aún no son actualizables mediante la API del cache.
Debido a esta cadena, existen dos rutas fundamentales de actualización en Aspose.Cells:
- **`PivotTable.calculateData()`** — recalcula la visualización de un `PivotTable` a partir de datos ya en cache, sin volver al origen de datos.
Todos los escenarios de este artículo utilizan datos de origen en celdas de hojas de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan según lo descrito.
{{% /alert %}}

## Quick Start
Si solo necesita el código más breve posible que actualice todas las tablas dinámicas del libro, una única llamada es suficiente:

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

El resto de este artículo explica cuándo elegir una API más específica en lugar de esta.

## Required Imports
Todos los ejemplos de JavaScript de este artículo asumen que el módulo Aspose.Cells para Node.js mediante C++ se ha cargado y que los tipos de tablas dinámicas residen en el espacio de nombres `Aspose.Cells.Pivot`. Una configuración típica es:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (o acceder vía `AsposeCells.Pivot.PivotFieldType`)

## Refresh All Pivot Tables in the Workbook
Cuando necesita garantizar que cada cache de tabla dinámica y cada tabla dinámica del libro refleje los datos de origen más recientes, la API más simple y completa es `Workbook.refreshAll()`. Una sola llamada recorre todo el libro de trabajo: actualiza cada `PivotCache` desde su origen y luego recalcula cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento cuando el rendimiento no es una preocupación.
El siguiente ejemplo construye un libro de trabajo con un rango de origen Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `refreshAll()` para actualizar todo en una sola llamada.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
A veces solo necesita actualizar las tablas dinámicas que residen en una hoja específica, por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas no están relacionadas y no deben tocarse. Para este caso, Aspose.Cells proporciona `Worksheet.refreshPivotTables()`, que está limitado a una sola instancia de `Worksheet`.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Cuando desea un control detallado sobre una única tabla dinámica, la API basada en cache ofrece dos opciones. La elección entre ellas depende de lo que realmente haya cambiado: los datos de origen subyacentes o solo las configuraciones de vista/diseño de la tabla dinámica en sí.

### Source Data Changed — Use `PivotCache.refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada adecuado es `pivotTable.PivotCache.refresh()`. Esta llamada vuelve a leer los datos de origen en el cache y luego recalcula todos los `PivotTable` que dependen de ese cache.

### Only View/Layout Changed — Use `calculateData()`
Si los datos de origen *no* han cambiado, pero solo se han modificado las configuraciones de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a una región diferente o se ha alternado una configuración de actualización al abrir), no hay necesidad de volver al origen de datos. El cache ya contiene los datos correctos; solo el `PivotTable` renderizado necesita recalcularse. En este caso, `pivotTable.calculateData()` es la opción correcta.
El siguiente ejemplo modifica una propiedad no relacionada con el origen de la tabla dinámica y luego llama a `calculateData()` para volver a renderizarla desde el cache existente.

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);
// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Un libro de trabajo a menudo contiene muchas tablas dinámicas que todas se basan en un mismo cache compartido. Para enumerarlas — por ejemplo, antes de realizar una actualización por lotes, o para diagnosticar el impacto del cache compartido — utilice `PivotCache.getPivotTables()`. Este método devuelve la colección de todos los `PivotTable` que dependen del cache dado.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Antes de Aspose.Cells para Node.js mediante C++ v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica individualmente. A partir de v26.7, este método está marcado como **obsoleto** y debe reemplazarse por las APIs conscientes del cache descritas anteriormente.
Existen dos razones por las que el enfoque `RefreshData()` por tabla es problemático en libros de trabajo del mundo real:
- Vuelve a obtener los datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
Las sustituciones recomendadas son:
El siguiente ejemplo demuestra el nuevo patrón eficiente para libros de trabajo con múltiples tablas dinámicas que comparten un único cache.

## Which Refresh API Should I Use?
La tabla siguiente resume las APIs de actualización disponibles y cuándo elegir cada una.
| Objetivo | API Recomendada | Notas |
|----------|-----------------|-------|
| Actualizar todo en el libro de trabajo | `Workbook.refreshAll()` | Una llamada; cubre todos los caches y tablas. |
| Actualizar solo tablas dinámicas en una hoja | `Worksheet.refreshPivotTables()` | Limitado a una sola hoja de cálculo. |
| Datos de origen cambiados para un cache | `pivotTable.PivotCache.refresh()` | Actualiza TODAS las tablas dinámicas en ese cache compartido. |
| Solo cambiaron las configuraciones de vista/diseño | `pivotTable.calculateData()` | Evita el ciclo innecesario hacia el origen. |
| Enumerar todas las tablas dinámicas en un cache compartido | `pivotCache.getPivotTables()` | Úselo para enumerar antes de una actualización por lotes. |
En la práctica, prefiera las APIs basadas en cache frente al obsoleto `RefreshData()` por tabla. Son conscientes de los caches compartidos, evitan obtenciones redundantes del origen y le permiten elegir el ámbito más pequeño que satisfaga su requisito de actualización.

## Common Pitfalls
- **Olvidarse de actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores renderizados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica celdas de origen, llame a `PivotCache.refresh()` (o `Workbook.refreshAll()`) antes de `Workbook.save()`, de lo contrario el archivo guardado seguirá conteniendo los valores agregados antiguos.
- **Llamar a `RefreshData()` obsoleto por tabla.** En v26.7, `PivotTable.RefreshData()` está marcado como obsoleto y vuelve a obtener el origen en cada llamada. Con múltiples tablas dinámicas compartiendo un cache, esto significa N obtenciones redundantes del origen. Reemplácelo con una única llamada a `PivotCache.refresh()` seguida de `calculateData()` por tabla.
- **Actualizar cuando solo cambió el diseño.** Si solo modificó la vista de una tabla dinámica (orden de columnas, `ConsolidationFunction`, etc.) sin tocar los datos de origen, `PivotCache.refresh()` es innecesario y lento. Llame a `pivotTable.calculateData()` para volver a renderizar desde el cache existente.
- **Origen externo no admitido por `PivotCache.refresh()`.** Si el origen de la tabla dinámica proviene de una conexión externa (base de datos, cubo OLAP, etc.), `PivotCache.refresh()` no puede actualizarlo en v26.7 — actualmente solo admite los tipos de origen `Sheet` y `Consolidation`. Para orígenes externos, vuelva a abrir el libro de trabajo o reconstruya el cache desde el origen.

{{< app/cells/assistant language="nodejs-cpp" >}}