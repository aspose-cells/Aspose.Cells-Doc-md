---
title: Actualizar Tablas Dinámicas y Cachés de Tablas Dinámicas en Aspose.Cells for Node.js via Java
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for Node.js via Java usando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
linktitle: Actualizar Tablas Dinámicas
keywords: Aspose.Cells, Node.js, Java, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece una API de actualización en capas que permite recargar datos de tablas dinámicas en cuatro niveles diferentes, desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for Node.js via Java v26.7**, el método heredado `PivotTable.RefreshData()` está marcado como obsoleto y debe reemplazarse por las API más eficientes y conscientes de la caché descritas en este artículo.
{{% /alert %}}

## Introducción
Actualizar una tabla dinámica rara vez es una operación única. En segundo plano, Aspose.Cells mantiene una cadena de datos en capas que conecta sus datos de origen originales con los valores renderizados que ve en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cualquier situación.
La cadena de datos de cuatro capas es:
1. **Origen de Datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde residen los valores brutos.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solo* de su `PivotCache`, nunca directamente del origen de datos.
4. **Celdas** — el `Cells` de la hoja de cálculo en el que la `PivotTable` renderiza sus valores calculados y estilos.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enumeración `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de la v26.7, `PivotCache.Refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que residen en rangos de hojas de cálculo. Los orígenes externos (bases de datos, conexiones externas, etc.) aún no se pueden actualizar a través de la API de caché.
{{% /alert %}}

Debido a esta cadena, existen dos rutas fundamentales de actualización en Aspose.Cells:
- **`PivotTable.CalculateData()`** — recalcula la visualización de una `PivotTable` a partir de los datos ya almacenados en caché, sin volver al origen de datos.
Todos los escenarios de este artículo usan datos de origen de celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Inicio Rápido
Si solo necesita el código más corto posible que actualice cada tabla dinámica del libro, basta con una sola llamada:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Todo lo demás de este artículo explica cuándo elegir una API más específica en su lugar.

## Importaciones Requeridas
- `const aspose = require('aspose.cells');`
- O para importaciones específicas: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Actualizar Todas las Tablas Dinámicas del Libro
Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica del libro refleje los datos de origen más recientes, la API más sencilla y completa es `Workbook.RefreshAll()`. Una sola llamada recorre todo el libro: actualiza cada `PivotCache` desde su origen y luego recalcula cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales de documentos completos donde el rendimiento no es una preocupación.
El siguiente ejemplo crea un libro con un rango de origen Fruto/Año/Importe, crea una tabla dinámica, modifica algunos valores de origen y luego usa `RefreshAll()` para poner todo al día con una sola llamada.

```javascript
const AsposeCells = require("aspose.cells");
// Crear un nuevo libro de trabajo
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Escribir la fila de encabezado en las celdas A1:C1
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
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Asignar campos dinámicos: Fruta a Filas, Año a Columnas, Cantidad a Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modificar varios valores de Cantidad en los datos de origen para simular cambios
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Actualizar todas las tablas dinámicas / caché dinámica en el libro de trabajo
workbook.refreshAll();
// Guardar el libro de trabajo
workbook.save("output.xlsx");
```

## Actualizar Todas las Tablas Dinámicas en una Sola Hoja de Cálculo
A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica; por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells ofrece `Worksheet.RefreshPivotTables()`, que está limitada a una sola instancia de `Worksheet`.

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

## Actualizar una Sola Tabla Dinámica
Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente haya cambiado: los datos de origen subyacentes, o solo la configuración de vista/diseño de la propia tabla dinámica.

### Cambiaron los Datos de Origen — Use `PivotCache.Refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.PivotCache.Refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

### Solo Cambió la Vista/Diseño — Use `CalculateData()`
Si los datos de origen *no* han cambiado pero solo se ha modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente o se ha activado/desactivado una opción de actualización al abrir), no es necesario volver al origen de datos. La caché ya contiene los datos correctos; solo la `PivotTable` renderizada necesita recálculo. En este caso, `pivotTable.CalculateData()` es la opción correcta.
El siguiente ejemplo modifica una propiedad que no es de origen de la tabla dinámica y luego llama a `CalculateData()` para volver a renderizarla desde la caché existente.

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
// Agregar una tabla dinámica llamada "Pivot1" ubicada en la celda de destino E3, con origen en A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Asignar campos: Fruta a Fila, Año a Columna, Cantidad a Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modificar una propiedad de vista/diseño — este es un cambio únicamente de presentación,
// por lo que NO requiere releer los datos de origen mediante PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) a partir de los
// datos ya almacenados en el PivotCache. Dado que los datos de origen no cambiaron,
// no se realiza un recorrido de ida y vuelta al origen — solo los valores en caché se recalculan
// en las celdas de la hoja de cálculo.
pivotTable.calculateData();
// Guardar el libro en disco
workbook.save("output.xlsx");
```

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas — por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de la caché compartida — use `PivotCache.GetPivotTables()`. Este método devuelve la colección de cada `PivotTable` que depende de la caché indicada.

## Migración desde el Obsoleto `PivotTable.RefreshData()`
Antes de Aspose.Cells for Node.js via Java v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica individualmente. A partir de la v26.7, ese método está marcado como **obsoleto** y debe reemplazarse por las API conscientes de la caché descritas anteriormente.
Hay dos razones por las que el enfoque de `RefreshData()` por tabla resulta problemático en libros reales:
- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
Los reemplazos recomendados son:
El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con múltiples tablas dinámicas que comparten una sola caché.

## ¿Qué API de Actualización Debo Usar?
La tabla siguiente resume las API de actualización disponibles y cuándo elegir cada una.
| Objetivo | API Recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo el libro | `Workbook.RefreshAll()` | Una sola llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una hoja | `Worksheet.RefreshPivotTables()` | Limitada a una hoja de cálculo. |
| Cambiaron los datos de origen de una caché | `pivotTable.PivotCache.Refresh()` | Actualiza TODAS las tablas dinámicas de esa caché compartida. |
| Solo cambió la configuración de vista/diseño | `pivotTable.CalculateData()` | Evita una lectura innecesaria del origen. |
| Listar todas las tablas dinámicas de una caché compartida | `pivotCache.GetPivotTables()` | Úsela para enumerar antes de una actualización masiva. |
En la práctica, prefiera las API basadas en caché sobre la obsoleta `RefreshData()` por tabla. Son conscientes de las cachés compartidas, evitan lecturas redundantes del origen y le permiten elegir el alcance más pequeño que satisfaga su requisito de actualización.

## Errores Comunes
- **Olvidar actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores renderizados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica celdas de origen, llame a `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) antes de `Workbook.save()`; de lo contrario, el archivo guardado aún contendrá los valores agregados antiguos.
- **Llamar al obsoleto `RefreshData()` por tabla.** En la v26.7, `PivotTable.RefreshData()` está marcado como obsoleto y vuelve a obtener el origen en cada llamada. Con varias tablas dinámicas que comparten una caché, esto significa N lecturas redundantes del origen. Reemplácelo por una sola llamada a `PivotCache.Refresh()` seguida de `CalculateData()` por tabla.
- **Actualizar cuando solo ha cambiado el diseño.** Si solo cambió la vista de la tabla dinámica (orden de columnas, `ConsolidationFunction`, etc.) sin modificar los datos de origen, `PivotCache.Refresh()` es innecesario y lento. Llame a `pivotTable.CalculateData()` para volver a renderizar desde la caché existente.
- **Origen externo no admitido por `PivotCache.Refresh()`.** Si el origen de la tabla dinámica proviene de una conexión externa (base de datos, cubo OLAP, etc.), `PivotCache.Refresh()` no puede actualizarla en la v26.7; actualmente solo admite los tipos de origen `Sheet` y `Consolidation`. Para orígenes externos, vuelva a abrir el libro o reconstruya la caché desde el origen.

{{< app/cells/assistant language="nodejs-java" >}}