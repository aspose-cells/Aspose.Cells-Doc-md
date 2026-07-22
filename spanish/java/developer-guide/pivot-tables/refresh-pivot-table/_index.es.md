---
title: Actualizar tablas dinámicas en Aspose.Cells for Java
linktitle: Actualizar tablas dinámicas en Aspose.Cells for Java
description: Aprenda cómo actualizar tablas dinámicas en Aspose.Cells for Java usando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, Java, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una API de actualización en capas que le permite recargar datos de tablas dinámicas en cuatro ámbitos diferentes — desde el libro completo hasta una sola tabla dinámica. A partir de **Aspose.Cells for Java v26.7**, el método heredado `PivotTable.refreshData()` está marcado como obsoleto y debe reemplazarse con las API más eficientes y conscientes de la caché descritas en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una operación única. Tras bambalinas, Aspose.Cells mantiene una cadena de datos en capas que conecta sus datos de origen originales con los valores representados que ve en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización correcta para cualquier situación.

La cadena de datos de cuatro capas es:

1. **Origen de datos** — los rangos originales de la hoja de cálculo, consulta a base de datos o rango de consolidación donde se encuentran los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solo* desde su `PivotCache`, nunca directamente desde el origen de datos.
4. **Cells** — las `Cells` de la hoja de cálculo en las que la `PivotTable` representa sus valores calculados y estilos.

Un concepto particularmente importante es la **caché compartida**. Cuando varias tablas dinámicas en un libro hacen referencia al mismo rango de origen, comparten *una* instancia de `PivotCache`. Una sola `PivotCache` puede ser referenciada por muchas tablas dinámicas, y al actualizar esa caché se actualizan de inmediato todas las `PivotTable` dependientes.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de la v26.7, `PivotCache.refresh()` admite solo los tipos de origen **`Sheet`** y **`Consolidation`** — es decir, datos que se encuentran en rangos de hojas de cálculo. Los orígenes externos (bases de datos, conexiones externas, etc.) aún no se pueden actualizar a través de la API de caché.

{{% /alert %}}

Debido a esta cadena, hay dos rutas fundamentales de actualización en Aspose.Cells:

- **`PivotCache.refresh()`** — recarga origen → caché Y recalcula todas las `PivotTable` dependientes en una sola operación.
- **`PivotTable.calculateData()`** — recalcula la visualización de una `PivotTable` a partir de los datos ya en caché, sin volver al origen de datos.

Todos los escenarios de este artículo usan datos de origen de celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Sentencias de Importación Requeridas

Todos los ejemplos de Java en este artículo comienzan con las siguientes sentencias de importación porque los tipos de tablas dinámicas se encuentran en el paquete `com.aspose.cells.pivot`:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Actualizar Todas las Tablas Dinámicas del Libro

Cuando necesita asegurarse de que cada caché de tablas dinámicas y cada tabla dinámica del libro refleje los últimos datos de origen, la API más sencilla y completa es `Workbook.refreshAll()`. Una sola llamada recorre el libro completo — actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento donde el rendimiento no es una preocupación.

El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores de origen y luego usa `refreshAll()` para actualizar todo en una sola llamada.

```java
import com.aspose.cells.*;

// Crear un nuevo libro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Asignar campos dinámicos: Fruit a Filas, Year a Columnas, Amount a Datos
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Modificar varios valores de Amount en los datos de origen para simular cambios
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Actualizar cada tabla dinámica / caché dinámica en el libro
workbook.refreshAll();

// Guardar el libro
workbook.save("output.xlsx");
```

## Actualizar Todas las Tablas Dinámicas en una Sola Hoja de Cálculo

A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica — por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells proporciona `Worksheet.refreshPivotTables()`, que está limitado a una sola instancia de `Worksheet`.

Esto es más selectivo que `Workbook.refreshAll()`: solo se actualizan las tablas dinámicas de la hoja de cálculo objetivo, dejando intactas las tablas dinámicas de otras hojas.

El siguiente ejemplo completa los mismos datos de origen Fruta/Año/Cantidad, agrega una tabla dinámica en la primera hoja de cálculo, modifica algunos valores de origen y luego actualiza solo las tablas dinámicas de esa hoja.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

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

int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```

## Actualizar una Sola Tabla Dinámica

Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente haya cambiado: los datos de origen subyacentes, o solo la configuración de vista/diseño de la tabla dinámica misma.

### Cambiaron los Datos de Origen — Use `PivotCache.refresh()`

Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.getPivotCache().refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

{{% alert color="primary" %}}

Dado que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.refresh()` recalcula **todas** las tablas dinámicas construidas sobre esa misma caché — no solo la que usted referencia. Si dos tablas dinámicas comparten el mismo rango de origen, al actualizar una caché se actualizan ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas en el mismo rango de origen para demostrar este comportamiento de caché compartida, modifica algunos valores de origen y luego actualiza a través de una referencia de caché.

```java
import com.aspose.cells.*;

// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Write header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Write approximately 9 data rows (grape / blueberry / kiwi / cherry across 2020-2021)
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

// Add the first pivot table "Pivot1" anchored at cell E3, source range A1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Assign fields for Pivot1
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// Add a SECOND pivot table "Pivot2" anchored at E15 using the SAME source range A1:C9
// Both Pivot1 and Pivot2 share a single PivotCache because the source range is identical.
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Assign the same fields for Pivot2
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// Modify several Amount cell values in the source data to simulate a data change
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Refresh the shared PivotCache.
// Because Pivot1 and Pivot2 share the same PivotCache, this single call
// refreshes BOTH pivot tables (data + style) from the updated source.
pivotTable1.refreshData();

// Save the workbook
workbook.save("output.xlsx");
```

### Solo Cambió la Vista/Diseño — Use `calculateData()`

Si los datos de origen *no* han cambiado pero solo se han modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente, o se ha activado una opción de actualizar al abrir), no es necesario volver al origen de datos. La caché ya contiene los datos correctos; solo es necesario recalcular la `PivotTable` renderizada. En este caso, `pivotTable.calculateData()` es la opción correcta.

Esto evita la innecesaria recuperación del origen y es significativamente más rápido cuando muchas tablas dinámicas comparten la misma caché.

El siguiente ejemplo modifica una propiedad que no es de origen de la tabla dinámica y luego llama a `calculateData()` para volver a renderizarla desde la caché existente.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Asignar campos: Fruta a Fila, Año a Columna, Cantidad a Datos
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Modificar una propiedad de vista/disposición -- este es un cambio solo de presentación,
// por lo que NO requiere volver a leer los datos de origen mediante PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) desde los
// datos ya almacenados en el PivotCache. Debido a que los datos de origen no cambiaron,
// no se realiza un viaje de ida y vuelta al origen -- solo se recalculan los valores en caché
// en las celdas de la hoja de cálculo.
pivotTable.calculateData();

// Guardar el libro de trabajo en disco
workbook.save("output.xlsx");
```

## Obtener Todas las Tablas Dinámicas que Comparten el Mismo PivotCache

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas — por ejemplo, antes de realizar una actualización por lotes, o para diagnosticar el impacto de la caché compartida — use `PivotCache.getPivotTables()`. Este método devuelve la colección de todas las `PivotTable` que dependen de la caché dada.

Esta es también la forma más directa de confirmar que dos tablas dinámicas efectivamente comparten la misma instancia de `PivotCache`: puede comparar las referencias de caché (usando el operador `==`), o simplemente iterar la colección devuelta por `getPivotTables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas en el mismo rango de origen, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas de la caché.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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

int pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

boolean sameCache = pivotTable1.getPivotCache() == pivotTable2.getPivotCache();
System.out.println("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
System.out.println("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (PivotTable pt : sharedPivotTables)
{
    System.out.println("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Migrando desde el Obsoleto `PivotTable.refreshData()`

Antes de Aspose.Cells for Java v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.refreshData()` en cada tabla dinámica individualmente. A partir de la v26.7, ese método está marcado como **obsoleto** y debe reemplazarse con las API conscientes de la caché descritas anteriormente.

Hay dos razones por las que el enfoque por tabla `refreshData()` es problemático en libros del mundo real:

- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
- Cada llamada actualiza toda la caché compartida. Cuando muchas tablas dinámicas comparten una caché, llamar repetidamente a `refreshData()` por tabla dinámica hace que la misma caché se vuelva a obtener una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas del libro** → use `workbook.refreshAll();`
- **Actualizar ALGUNAS de ellas** → use `pivotTable.getPivotCache().refresh();` para una caché. Debido a que la caché es compartida, esta sola llamada actualiza cada tabla dinámica construida sobre esa caché. Otras tablas dinámicas que se asientan sobre una caché ya actualizada se pueden omitir de forma segura.
- **Solo cambió la vista/diseño de la tabla dinámica** → use `pivotTable.calculateData();` para volver a renderizar desde la caché existente sin ningún viaje de ida y vuelta al origen.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con múltiples tablas dinámicas que comparten una sola caché.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- Construir los datos fuente: Fruta / Año / Monto (encabezado + 9 filas) ---
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

// --- Agregar la primera tabla dinámica (Pivot1) en la celda de destino E3 ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Agregar la SEGUNDA tabla dinámica (Pivot2) en el MISMO rango de origen ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Modificar varios valores de Monto en los datos fuente ---
sheet.getCells().get("C2").putValue(5000);   // Uva 2020
sheet.getCells().get("C5").putValue(7500);   // Cereza 2020
sheet.getCells().get("C9").putValue(9500);   // Cereza 2021

// --- NUEVO patrón v26.7+: actualizar el caché UNA VEZ, luego volver a renderizar según sea necesario ---
pivotTable1.getPivotCache().refresh();

// Volver a renderizar la vista/disposición de la segunda tabla dinámica sin tocar el origen
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## ¿Qué API de Actualización Debo Usar?

La tabla a continuación resume las API de actualización disponibles y cuándo elegir cada una.

| Objetivo | API Recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro | `Workbook.refreshAll()` | Una sola llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una sola hoja | `Worksheet.refreshPivotTables()` | Limitado a una hoja de cálculo. |
| Cambiaron los datos de origen de una caché | `pivotTable.getPivotCache().refresh()` | Actualiza TODAS las tablas dinámicas en esa caché compartida. |
| Solo cambiaron la configuración de vista/diseño | `pivotTable.calculateData()` | Omite el innecesario viaje de ida y vuelta al origen. |
| Listar todas las tablas dinámicas en una caché compartida | `pivotCache.getPivotTables()` | Úselo para enumerar antes de la actualización en masa. |

En la práctica, prefiera las API basadas en caché sobre el obsoleto `refreshData()` por tabla. Son conscientes de las cachés compartidas, evitan recuperaciones redundantes del origen y le permiten elegir el ámbito más pequeño que satisface su requisito de actualización.

{{< app/cells/assistant language="java" >}}