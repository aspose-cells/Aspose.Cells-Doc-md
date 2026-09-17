---
title: Actualizar tablas dinámicas y cachés de tablas dinámicas en Aspose.Cells for Java
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for Java usando la API de actualización de tablas dinámicas de v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
linktitle: Actualizar Tablas Dinámicas
keywords: Aspose.Cells, Java, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece una API de actualización por capas que permite recargar datos de tablas dinámicas en cuatro alcances diferentes, desde todo el libro de trabajo hasta una sola tabla dinámica. A partir de **Aspose.Cells for Java v26.7**, el método heredado `PivotTable.refreshData()` está marcado como obsoleto y debe reemplazarse por las APIs más eficientes y conscientes del caché descritas en este artículo.
{{% /alert %}}

## Introduction
Actualizar una tabla dinámica rara vez es una operación única. Entre bastidores, Aspose.Cells mantiene una cadena de datos por capas que conecta sus datos de origen originales con los valores representados que ve en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cualquier situación.
La cadena de datos de cuatro capas es:
1. **Origen de datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde viven los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se reúnen y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solo* de su `PivotCache`, nunca directamente del origen de datos.
4. **Cells** — las `Cells` de la hoja de cálculo en las que la `PivotTable` representa sus valores calculados y estilos.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica de dónde provienen los datos del caché. A partir de v26.7, `PivotCache.refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que viven en rangos de hojas de cálculo. Los orígenes externos (bases de datos, conexiones externas, etc.) aún no se pueden actualizar mediante la API de caché.
{{% /alert %}}

Debido a esta cadena, hay dos rutas fundamentales de actualización en Aspose.Cells:
- **`PivotTable.calculateData()`** — recalcula la visualización de una `PivotTable` a partir de datos ya almacenados en caché, sin volver al origen de datos.
Todos los escenarios de este artículo usan datos de origen de celdas de hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Quick Start
Si solo necesita el código más breve posible que actualice cada tabla dinámica en el libro de trabajo, una sola llamada es suficiente:

```java
import com.aspose.cells.*;
// Crear un nuevo libro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Asignar campos de la tabla dinámica: Fruit a Filas, Year a Columnas, Amount a Datos
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modificar varios valores de Amount en los datos de origen para simular cambios
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Actualizar cada tabla dinámica / caché de tabla dinámica en el libro
workbook.refreshAll();
// Guardar el libro
workbook.save("output.xlsx");
```

Todo lo demás en este artículo explica cuándo elegir una API más específica en su lugar.

## Required Import Statements
Todos los ejemplos de Java en este artículo comienzan con las siguientes sentencias de importación porque los tipos de tabla dinámica viven en el paquete `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica en el libro de trabajo refleje los datos de origen más recientes, la API más simple y completa es `Workbook.refreshAll()`. Una sola llamada recorre todo el libro de trabajo, actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales de documentos completos donde el rendimiento no es una preocupación.
El siguiente ejemplo construye un libro de trabajo con un rango de origen Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores de origen y luego usa `refreshAll()` para actualizar todo en una sola llamada.

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

## Refresh All Pivot Tables on a Single Worksheet
A veces solo necesita actualizar las tablas dinámicas que viven en una hoja de cálculo específica, por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas de cálculo no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells ofrece `Worksheet.refreshPivotTables()`, que está limitada a una sola instancia de `Worksheet`.

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
// Modificar una propiedad de vista/diseño -- esto es un cambio solo de presentación,
// por lo que NO requiere volver a leer los datos de origen a través de PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) desde los
// datos ya almacenados en el PivotCache. Debido a que los datos de origen no cambiaron,
// no se realiza un viaje de ida y vuelta al origen -- solo los valores en caché se recalculan
// en las celdas de la hoja de cálculo.
pivotTable.calculateData();
// Guardar el libro de trabajo en disco
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de qué cambió realmente: los datos de origen subyacentes, o solo la configuración de vista/diseño de la propia tabla dinámica.

### Source Data Changed — Use `PivotCache.refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.getPivotCache().refresh()`. Esta llamada vuelve a leer los datos de origen en el caché y luego recalcula cada `PivotTable` que depende de ese caché.

### Only View/Layout Changed — Use `calculateData()`
Si los datos de origen *no* han cambiado pero solo se han modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente, o se ha alternado una configuración de actualizar al abrir), no es necesario volver al origen de datos. El caché ya contiene los datos correctos; solo la `PivotTable` representada necesita recálculo. En este caso, `pivotTable.calculateData()` es la opción correcta.
El siguiente ejemplo modifica una propiedad que no es del origen de la tabla dinámica y luego llama a `calculateData()` para volver a representarla desde el caché existente.
Un libro de trabajo a menudo contiene muchas tablas dinámicas que se asientan sobre un caché compartido. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto del caché compartido, use `PivotCache.getPivotTables()`. Este método devuelve la colección de cada `PivotTable` que depende del caché dado.

## Migrating from the Obsolete `PivotTable.refreshData()`
Antes de Aspose.Cells for Java v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.refreshData()` en cada tabla dinámica individualmente. A partir de v26.7, ese método está marcado como **obsoleto** y debe reemplazarse por las APIs conscientes del caché descritas anteriormente.
Hay dos razones por las que el enfoque `refreshData()` por tabla es problemático en libros de trabajo del mundo real:
- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
Los reemplazos recomendados son:
El siguiente ejemplo demuestra el nuevo patrón eficiente para libros de trabajo con varias tablas dinámicas que comparten un único caché.

## Which Refresh API Should I Use?
La tabla a continuación resume las APIs de actualización disponibles y cuándo elegir cada una.
| Objetivo | API Recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro de trabajo | `Workbook.refreshAll()` | Una llamada; cubre todos los cachés y tablas. |
| Actualizar solo las tablas dinámicas en una sola hoja | `Worksheet.refreshPivotTables()` | Limitado a una hoja de cálculo. |
| Los datos de origen cambiaron para un caché | `pivotTable.getPivotCache().refresh()` | Actualiza TODAS las tablas dinámicas en ese caché compartido. |
| Solo cambió la configuración de vista/diseño | `pivotTable.calculateData()` | Evita el viaje innecesario al origen. |
| Listar todas las tablas dinámicas en un caché compartido | `pivotCache.getPivotTables()` | Use para enumerar antes de una actualización masiva. |
En la práctica, prefiera las APIs basadas en caché sobre la obsoleta `refreshData()` por tabla. Son conscientes de los cachés compartidos, evitan obtenciones redundantes del origen y le permiten elegir el alcance más pequeño que satisfaga su requisito de actualización.

## Common Pitfalls
- **Olvidar actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores representados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica las celdas de origen, llame a `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) antes de `Workbook.save()`, de lo contrario el archivo guardado aún contendrá los valores agregados antiguos.
- **Llamar al obsoleto `RefreshData()` por tabla.** En v26.7, `PivotTable.RefreshData()` está marcado como obsoleto y vuelve a obtener el origen en cada llamada. Con varias tablas dinámicas compartiendo un caché, esto significa N obtenciones de origen redundantes. Reemplace con un único `PivotCache.Refresh()` seguido de `CalculateData()` por tabla.
- **Actualizar cuando solo cambió el diseño.** Si solo cambió la vista de una tabla dinámica (orden de columnas, `ConsolidationFunction`, etc.) sin tocar los datos de origen, `PivotCache.Refresh()` es innecesario y lento. Llame a `pivotTable.CalculateData()` para volver a representar desde el caché existente.
- **Origen externo no admitido por `PivotCache.Refresh()`.** Si el origen de la tabla dinámica proviene de una conexión externa (base de datos, cubo OLAP, etc.), `PivotCache.Refresh()` no puede actualizarla en v26.7; actualmente solo admite los tipos de origen `Sheet` y `Consolidation`. Para orígenes externos, vuelva a abrir el libro de trabajo o reconstruya el caché desde el origen.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="java" >}}