---
title: Actualizar Tablas Dinámicas y Pivots Caches en Aspose.Cells for Node.js via C++
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for Node.js via C++ usando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos de código prácticos.
linktitle: Actualizar Tablas Dinámicas
keywords: Aspose.Cells, Node.js vía C++, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells proporciona una API de actualización por capas que le permite recargar los datos de las tablas dinámicas en cuatro niveles distintos, desde el libro completo hasta una sola tabla dinámica. A partir de **Aspose.Cells for Node.js via C++ v26.7**, el método heredado `PivotTable.RefreshData()` está marcado como obsoleto y debe sustituirse por las API más eficientes y conscientes de la caché que se describen en este artículo.
{{% /alert %}}

## Introducción
Actualizar una tabla dinámica rara vez es una sola operación. En segundo plano, Aspose.Cells mantiene una cadena de datos por capas que conecta sus datos de origen originales con los valores representados que ve en la hoja de cálculo. Comprender esta cadena es clave para elegir la API de actualización adecuada para cada situación.
La cadena de datos en cuatro capas es:
1. **Fuente de datos** — los rangos de la hoja de cálculo original, la consulta a la base de datos o el rango de consolidación donde se encuentran los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *únicamente* de su `PivotCache`, nunca directamente desde la fuente de datos.
4. **Cells** — la colección `Cells` de la hoja de cálculo en la que la `PivotTable` representa sus valores calculados y estilos.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enumeración `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de la versión v26.7, `PivotCache.Refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que residen en rangos de hojas de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no pueden actualizarse mediante la API de caché.
{{% /alert %}}

Gracias a esta cadena, existen dos rutas fundamentales de actualización en Aspose.Cells:
- **`PivotTable.CalculateData()`** — recalcula la visualización de una sola `PivotTable` a partir de los datos ya almacenados en caché, sin volver a la fuente de datos.
Todos los escenarios de este artículo utilizan datos de origen en celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Inicio rápido
Si solo necesita el código más breve posible que actualice cada tabla dinámica del libro, basta con una sola llamada:

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Escribir fila de encabezado en las celdas A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Escribir filas de datos en las celdas A2:C9 (8 filas de datos de frutas entre 2020 y 2021)
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
// Agregar una tabla dinámica: rango de origen "A1:C9", celda de destino "E3", nombre "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Asignar campos de la tabla dinámica: Fruit a Filas, Year a Columnas, Amount a Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modificar varios valores de Amount en los datos de origen para simular cambios
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Actualizar todas las tablas dinámicas / caché de tablas dinámicas en el libro
workbook.refreshAll();
// Guardar el libro
workbook.save("output.xlsx");
```

Todo lo demás en este artículo explica cuándo elegir una API más específica en su lugar.

## Importaciones necesarias
Todos los ejemplos de JavaScript en este artículo asumen que se ha cargado el módulo Aspose.Cells for Node.js via C++ y que los tipos de tablas dinámicas se encuentran en el espacio de nombres `Aspose.Cells.Pivot`. Una configuración típica es:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (o acceder mediante `AsposeCells.Pivot.PivotFieldType`)

## Actualizar todas las tablas dinámicas del libro
Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica del libro reflejen los datos de origen más recientes, la API más simple y completa es `Workbook.RefreshAll()`. Una sola llamada recorre todo el libro, actualiza cada `PivotCache` desde su origen y luego recalcula cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento cuando el rendimiento no es una preocupación.
El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Importe, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `RefreshAll()` para actualizar todo en una sola llamada.

```javascript
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

## Actualizar todas las tablas dinámicas en una sola hoja de cálculo
A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica, por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas no están relacionadas y no deben verse afectadas. Para este caso, Aspose.Cells proporciona `Worksheet.RefreshPivotTables()`, que se limita a una sola instancia de `Worksheet`.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Escribir la fila de encabezado Fruta / Año / Cantidad
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Escribir 8 filas de datos (filas 2-9, ajustándose al rango de origen A1:C9)
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
// Agregar una tabla dinámica llamada "Pivot1" colocada en la celda de destino E3, con origen en A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Asignar campos: Fruta a Fila, Año a Columna, Cantidad a Datos
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");
// Modificar una propiedad de vista/diseño — este es un cambio solo de presentación,
// por lo que NO requiere volver a leer los datos de origen a través de PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() vuelve a renderizar la visualización (datos + estilo) de ESTA tabla dinámica
// a partir de los datos ya almacenados en el PivotCache. Debido a que los datos de origen no cambiaron,
// no se realiza ningún viaje de ida y vuelta al origen — solo los valores en caché se recalculan
// en las celdas de la hoja de cálculo.
pivotTable.calculateData();
// Guardar el libro de trabajo en disco
workbook.save("output.xlsx");
```

## Actualizar una sola tabla dinámica
Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente haya cambiado: los datos de origen subyacentes, o solo la configuración de vista o diseño de la propia tabla dinámica.

### Cambiaron los datos de origen — Use `PivotCache.Refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.PivotCache.Refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

### Solo cambió la vista o el diseño — Use `CalculateData()`
Si los datos de origen *no* han cambiado pero solo se han modificado los ajustes de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente o se ha activado una opción de actualizar al abrir), no es necesario volver a la fuente de datos. La caché ya contiene los datos correctos; solo es necesario recalcular la `PivotTable` renderizada. En este caso, `pivotTable.CalculateData()` es la opción adecuada.
El siguiente ejemplo modifica una propiedad no relacionada con el origen de la tabla dinámica y luego llama a `CalculateData()` para volver a renderizarla desde la caché existente.
Un libro a menudo contiene muchas tablas dinámicas que se apoyan en una caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de una caché compartida, utilice `PivotCache.GetPivotTables()`. Este método devuelve la colección de todas las `PivotTable` que dependen de la caché indicada.

## Migración desde el obsoleto `PivotTable.RefreshData()`
Antes de Aspose.Cells for Node.js via C++ v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica de forma individual. A partir de v26.7, ese método está marcado como **obsoleto** y debe sustituirse por las API conscientes de la caché descritas anteriormente.
Existen dos razones por las que el enfoque `RefreshData()` por tabla resulta problemático en libros del mundo real:
- Vuelve a obtener los datos del origen *cada vez* que se llama, incluso cuando el origen no ha cambiado.
Las sustituciones recomendadas son:
El siguiente ejemplo muestra el nuevo patrón eficiente para libros con varias tablas dinámicas que comparten una sola caché.

## ¿Qué API de actualización debo usar?
La tabla siguiente resume las API de actualización disponibles y cuándo elegir cada una.
| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo el libro | `Workbook.RefreshAll()` | Una sola llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una hoja | `Worksheet.RefreshPivotTables()` | Limitado a una hoja de cálculo. |
| Cambiaron los datos de origen de una caché | `pivotTable.PivotCache.Refresh()` | Actualiza TODAS las tablas dinámicas de esa caché compartida. |
| Solo cambiaron los ajustes de vista/diseño | `pivotTable.CalculateData()` | Evita un viaje innecesario a la fuente. |
| Listar todas las tablas dinámicas de una caché compartida | `pivotCache.GetPivotTables()` | Úselo para enumerar antes de una actualización masiva. |
En la práctica, prefiera las API basadas en caché en lugar del obsoleto `RefreshData()` por tabla. Dichas API conocen las cachés compartidas, evitan lecturas redundantes del origen y le permiten elegir el alcance más pequeño que satisfaga su requisito de actualización.

## Errores comunes
- **Olvidar actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores representados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica las celdas de origen, llame a `PivotCache.Refresh()` (o a `Workbook.RefreshAll()`) antes de `Workbook.save()`, de lo contrario el archivo guardado aún contendrá los valores agregados antiguos.
- **Llamar al obsoleto `RefreshData()` por tabla.** En la versión v26.7, `PivotTable.RefreshData()` está marcado como obsoleto y vuelve a obtener el origen en cada llamada. Con varias tablas dinámicas compartiendo una caché, esto significa N lecturas redundantes del origen. Sustitúyalo por una sola llamada a `PivotCache.Refresh()` seguida de `CalculateData()` por tabla.
- **Actualizar cuando solo cambió el diseño.** Si solo cambió la vista de una tabla dinámica (orden de columnas, `ConsolidationFunction`, etc.) sin tocar los datos de origen, `PivotCache.Refresh()` es innecesario y lento. Llame a `pivotTable.CalculateData()` para volver a renderizar desde la caché existente.
- **Fuente externa no admitida por `PivotCache.Refresh()`.** Si el origen de la tabla dinámica proviene de una conexión externa (base de datos, cubo OLAP, etc.), `PivotCache.Refresh()` no puede actualizarla en la versión v26.7; actualmente solo admite los tipos de origen `Sheet` y `Consolidation`. Para fuentes externas, vuelva a abrir el libro o reconstruya la caché desde el origen.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}