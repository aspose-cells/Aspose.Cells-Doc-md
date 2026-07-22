---
title: Actualización de tablas dinámicas en Aspose.Cells for Node.js via Java
linktitle: Actualización de tablas dinámicas en Aspose.Cells for Node.js via Java
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for Node.js via Java utilizando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, Node.js, Java, tabla dinámica, actualización, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece una API de actualización por niveles que permite recargar los datos de las tablas dinámicas en cuatro alcances diferentes, desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for Node.js via Java v26.7**, el método heredado `PivotTable.RefreshData()` está marcado como obsoleto y debe sustituirse por las API más eficientes y conscientes del caché que se describen en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una operación única. Tras bambalinas, Aspose.Cells mantiene una cadena de datos por niveles que conecta sus datos de origen originales con los valores representados que se ven en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada en cada situación.

La cadena de datos de cuatro niveles es:

1. **Origen de datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde residen los valores brutos.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se reúnen y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *únicamente* desde su `PivotCache`, nunca directamente desde el origen de datos.
4. **Celdas** — el `Cells` de la hoja de cálculo en el que la `PivotTable` representa sus valores calculados y estilos.

Un concepto particularmente importante es el **caché compartido**. Cuando varias tablas dinámicas de un libro hacen referencia al mismo rango de origen, comparten *una* instancia de `PivotCache`. Un solo `PivotCache` puede ser referenciado por muchas tablas dinámicas, y actualizar ese caché actualiza cada `PivotTable` dependiente de una vez.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enumeración `PivotTableSourceType`) indica de dónde provienen los datos del caché. A partir de v26.7, `PivotCache.Refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que residen en rangos de hojas de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no se pueden actualizar a través de la API de caché.

{{% /alert %}}

Debido a esta cadena, existen dos rutas fundamentales de actualización en Aspose.Cells:

- **`PivotCache.Refresh()`** — recarga origen → caché Y recalcula todas las `PivotTable`s dependientes en una sola operación.
- **`PivotTable.CalculateData()`** — recalcula la vista de una `PivotTable` a partir de los datos ya almacenados en caché, sin volver al origen de datos.

Todos los escenarios de este artículo utilizan datos de origen en celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Importaciones Requeridas

Todos los ejemplos de JavaScript de este artículo requieren el módulo Aspose.Cells for Node.js via Java. Los tipos de tablas dinámicas se encuentran en el espacio de nombres `Aspose.Cells.Pivot`, que forma parte del mismo módulo:

- `const aspose = require('aspose.cells');`
- O para importaciones específicas: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Actualizar Todas las Tablas Dinámicas del Libro

Cuando necesita asegurarse de que cada caché de tablas dinámicas y cada tabla dinámica del libro reflejen los datos de origen más recientes, la API más sencilla y completa es `Workbook.RefreshAll()`. Una sola llamada recorre todo el libro, actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento, donde el rendimiento no es un problema.

El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Monto, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `RefreshAll()` para actualizar todo en una sola llamada.

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

// Asignar campos dinámicos: Fruit a Filas, Year a Columnas, Amount a Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modificar varios valores de Amount en los datos de origen para simular cambios
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Actualizar todas las tablas dinámicas / caché de tablas dinámicas en el libro de trabajo
workbook.refreshAll();

// Guardar el libro de trabajo
workbook.save("output.xlsx");
```

## Actualizar Todas las Tablas Dinámicas en una Sola Hoja de Cálculo

A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica, por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas no están relacionadas y no deben tocarse. Para este caso, Aspose.Cells proporciona `Worksheet.RefreshPivotTables()`, que está limitado a una sola instancia de `Worksheet`.

Esto es más selectivo que `Workbook.RefreshAll()`: solo se actualizan las tablas dinámicas de la hoja de cálculo objetivo, dejando intactas las tablas dinámicas de otras hojas.

El siguiente ejemplo completa los mismos datos de origen Fruta/Año/Monto, añade una tabla dinámica en la primera hoja de cálculo, modifica algunos valores de origen y luego actualiza únicamente las tablas dinámicas de esa hoja.

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

Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente haya cambiado: los datos de origen subyacentes o solo la configuración de vista/diseño de la propia tabla dinámica.

### Cambiaron los Datos de Origen — Utilice `PivotCache.Refresh()`

Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.PivotCache.Refresh()`. Esta llamada vuelve a leer los datos de origen en el caché y luego recalcula cada `PivotTable` que depende de ese caché.

{{% alert color="primary" %}}

Dado que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.Refresh()` recalcula **todas** las tablas dinámicas construidas sobre ese mismo caché, no solo la que usted referencia. Si dos tablas dinámicas comparten el mismo rango de origen, actualizar un caché actualiza ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen para demostrar este comportamiento de caché compartido, modifica algunos valores de origen y luego actualiza a través de una referencia de caché.

```javascript
const AsposeCells = require("aspose.cells");

// Crear un nuevo libro de trabajo y acceder a la primera hoja de cálculo
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Escribir fila de encabezado: Fruta / Año / Cantidad
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Escribir aproximadamente 9 filas de datos (uva / arándano / kiwi / cereza a lo largo de 2020-2021)
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Agregar la primera tabla dinámica "Pivot1" anclada en la celda E3, rango de origen A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Asignar campos para Pivot1
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Agregar una SEGUNDA tabla dinámica "Pivot2" anclada en E15 usando el MISMO rango de origen A1:C9
// Tanto Pivot1 como Pivot2 comparten un único PivotCache porque el rango de origen es idéntico.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Asignar los mismos campos para Pivot2
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modificar varios valores de celda de Cantidad en los datos de origen para simular un cambio de datos
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Refrescar el PivotCache compartido.
// Debido a que Pivot1 y Pivot2 comparten el mismo PivotCache, esta única llamada
// refresca AMBAS tablas dinámicas (datos + estilo) desde la fuente actualizada.
pivotTable1.getPivotCache().refresh();

// Guardar el libro de trabajo
workbook.save("output.xlsx");
```

### Solo Cambió la Vista/Diseño — Utilice `CalculateData()`

Si los datos de origen *no* han cambiado pero solo se han modificado los ajustes de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente o se ha alternado un ajuste de actualización al abrir), no es necesario volver al origen de datos. El caché ya contiene los datos correctos; solo la `PivotTable` representada necesita ser recalculada. En este caso, `pivotTable.CalculateData()` es la opción correcta.

Esto evita la obtención innecesaria desde el origen y es significativamente más rápido cuando muchas tablas dinámicas comparten el mismo caché.

El siguiente ejemplo modifica una propiedad que no es del origen de la tabla dinámica y luego llama a `CalculateData()` para volver a representarla desde el caché existente.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Escribir fila de encabezado Fruta / Año / Cantidad
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

// Modificar una propiedad de vista/diseño — este es un cambio solo de presentación,
// por lo que NO requiere volver a leer los datos de origen a través de PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) desde los
// datos que ya se encuentran en el PivotCache. Debido a que los datos de origen no cambiaron,
// no se realiza un viaje de ida y vuelta al origen — solo los valores almacenados en caché se recalculan
// en las celdas de la hoja de cálculo.
pivotTable.calculateData();

// Guardar el libro de trabajo en disco
workbook.save("output.xlsx");
```

## Obtener Todas las Tablas Dinámicas que Comparten el Mismo PivotCache

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre un único caché compartido. Para enumerarlas (por ejemplo, antes de realizar una actualización por lotes, o para diagnosticar el impacto del caché compartido), utilice `PivotCache.GetPivotTables()`. Este método devuelve la colección de cada `PivotTable` que depende del caché dado.

Esta es también la forma más directa de confirmar que dos tablas dinámicas realmente comparten la misma instancia de `PivotCache`: puede comparar las referencias del caché, o simplemente iterar la colección devuelta por `GetPivotTables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas del caché.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Migración desde el Obsoleto `PivotTable.RefreshData()`

Antes de Aspose.Cells for Node.js via Java v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.RefreshData()` en cada tabla dinámica individualmente. A partir de v26.7, ese método está marcado como **obsoleto** y debe sustituirse por las API conscientes del caché descritas anteriormente.

Hay dos razones por las que el enfoque `RefreshData()` por tabla es problemático en libros del mundo real:

- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
- Cada llamada actualiza todo el caché compartido. Cuando muchas tablas dinámicas comparten un caché, llamar repetidamente a `RefreshData()` por tabla dinámica hace que el mismo caché se vuelva a obtener una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas del libro** → use `workbook.refreshAll();`
- **Actualizar ALGUNAS de ellas** → use `pivotTable.getPivotCache().refresh();` para un caché. Debido a que el caché es compartido, esta única llamada actualiza cada tabla dinámica construida sobre ese caché. Otras tablas dinámicas que se asientan sobre un caché ya actualizado pueden omitirse de forma segura.
- **Solo cambió la vista/diseño de la tabla dinámica** → use `pivotTable.calculateData();` para volver a representar desde el caché existente sin necesidad de ir al origen.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con múltiples tablas dinámicas que comparten un solo caché.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Construir los datos de origen: Fruta / Año / Cantidad (encabezado + 9 filas) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Agregar la primera tabla dinámica (Pivot1) en la celda destino E3 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Agregar la SEGUNDA tabla dinámica (Pivot2) sobre el MISMO rango de origen ---
// Tanto Pivot1 como Pivot2 comparten UN ÚNICO PivotCache subyacente.
// Este es exactamente el escenario donde el enfoque legacy por tabla RefreshData()
// se vuelve ineficiente: refrescar una tabla vuelve a obtener todo el caché
// compartido, por lo que refrescar N tablas realiza la misma obtención costosa N veces.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Modificar varios valores de Cantidad en los datos de origen ---
sheet.getCells().get("C2").putValue(5000);   // Uva     2020
sheet.getCells().get("C5").putValue(7500);   // Cereza  2020
sheet.getCells().get("C9").putValue(9500);   // Cereza  2021

// --- Patrón OBSOLETO (anterior a 26.7) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // vuelve a obtener desde el origen, refresca todo el caché
// pivotTable2.refreshData();  // vuelve a obtener DE NUEVO — ¡el caché ya está actualizado!
// Cada llamada reconstruye el caché compartido, por lo que N tablas = N obtenciones redundantes.

// --- NUEVO patrón v26.7+: refrescar el caché UNA VEZ, luego re-renderizar según sea necesario ---
// Una sola llamada a PivotCache.Refresh() extrae los valores modificados al caché
// compartido Y recalcula la visualización de CADA tabla dinámica que lo referencia.
// Debido a que Pivot1 y Pivot2 comparten un PivotCache, esta única llamada actualiza
// ambas tablas — no se requiere un segundo viaje de ida y vuelta al origen.
pivotTable1.getPivotCache().refresh();

// CalculateData() solo re-renderiza la visualización de una tabla dinámica (datos + estilo)
// a partir de los datos ya almacenados en el caché — NO toca el origen.
// Lo llamamos en Pivot2 aquí puramente para demostrar la API: después de que el caché
// ha sido refrescado una vez, cualquier tabla dependiente puede re-renderizarse sin
// volver al origen. Use CalculateData() por sí solo cuando solo haya cambiado la
// configuración de vista/diseño de la tabla dinámica y el caché esté actualizado.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## ¿Qué API de Actualización Debo Utilizar?

La tabla siguiente resume las API de actualización disponibles y cuándo elegir cada una.

| Objetivo | API Recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro | `Workbook.RefreshAll()` | Una sola llamada; cubre todos los cachés y tablas. |
| Actualizar solo las tablas dinámicas de una sola hoja | `Worksheet.RefreshPivotTables()` | Limitado a una hoja de cálculo. |
| Cambiaron los datos de origen para un caché | `pivotTable.PivotCache.Refresh()` | Actualiza TODAS las tablas dinámicas sobre ese caché compartido. |
| Solo cambiaron los ajustes de vista/diseño | `pivotTable.CalculateData()` | Evita un viaje innecesario al origen. |
| Listar todas las tablas dinámicas sobre un caché compartido | `pivotCache.GetPivotTables()` | Utilícelo para enumerar antes de una actualización masiva. |

En la práctica, prefiera las API basadas en caché sobre el obsoleto `RefreshData()` por tabla. Son conscientes de los cachés compartidos, evitan obtener el origen de forma redundante y le permiten elegir el menor alcance que satisfaga su requisito de actualización.

{{< app/cells/assistant language="javascript" >}}