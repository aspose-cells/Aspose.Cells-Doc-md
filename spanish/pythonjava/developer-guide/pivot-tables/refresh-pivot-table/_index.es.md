---
title: Actualizar tablas dinámicas y cachés de tablas dinámicas en Aspose.Cells for Python via Java
linktitle: Actualizar tablas dinámicas y cachés de tablas dinámicas en Aspose.Cells for Python via Java
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for Python via Java usando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, Python via Java, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece una API de actualización en capas que permite recargar los datos de las tablas dinámicas en cuatro niveles diferentes, desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for Python via Java v26.7**, el método heredado `PivotTable.refreshData()` está marcado como obsoleto y debe reemplazarse por las API más eficientes y conscientes de la caché que se describen en este artículo.
{{% /alert %}}

## Introduction
Actualizar una tabla dinámica rara vez es una operación única. Entre bastidores, Aspose.Cells mantiene una cadena de datos en capas que conecta los datos de origen originales con los valores renderizados que se ven en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cada situación.
La cadena de datos de cuatro capas es:
1. **Origen de datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Un `PivotTable` lee *solamente* de su `PivotCache`, nunca directamente del origen de datos.
4. **Cells** — el `Cells` de la hoja de cálculo en el que el `PivotTable` renderiza sus valores calculados y estilos.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de la v26.7, `PivotCache.refresh()` admite solo los tipos de origen **`SHEET`** y **`CONSOLIDATION`**, es decir, datos que residen en rangos de hojas de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no se pueden actualizar mediante la API de caché.
Debido a esta cadena, existen dos rutas fundamentales de actualización en Aspose.Cells:
- **`PivotTable.calculateData()`** — recalcula la visualización de un `PivotTable` a partir de los datos ya almacenados en caché, sin volver al origen de datos.
Todos los escenarios de este artículo usan datos de origen de celdas de la hoja de cálculo, por lo que el tipo de origen es `SHEET` y las operaciones de actualización se comportan como se describe.
{{% /alert %}}

## Quick Start
Si solo necesita el código más breve posible que actualice todas las tablas dinámicas del libro, basta con una sola llamada:

```python
import jpype
from asposecells.api import Workbook

workbook = Workbook("input.xlsx")
workbook.refreshAll()
workbook.save("output.xlsx")
```

Todo lo demás de este artículo explica cuándo elegir una API más específica en su lugar.

## Required Imports
Todos los ejemplos de Python de este artículo dependen de las siguientes importaciones porque los tipos de tablas dinámicas se encuentran en el espacio de nombres `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
El módulo `jpype` se usa para iniciar la JVM, mientras que `aspose.cells` expone los tipos de libro/hoja de cálculo/celda/tabla dinámica utilizados en todo el artículo.

## Refresh All Pivot Tables in the Workbook
Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica del libro reflejen los datos de origen más recientes, la API más sencilla y completa es `Workbook.refreshAll()`. Una sola llamada recorre todo el libro, actualiza cada `PivotCache` desde su origen y luego recalcula cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales de todo el documento cuando el rendimiento no es un problema.
El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Importe, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `refreshAll()` para actualizar todo en una sola llamada.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll()
# Save the workbook
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh All Pivot Tables on a Single Worksheet
A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica, por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas no están relacionadas y no deben tocarse. Para este caso, Aspose.Cells ofrece `Worksheet.refreshPivotTables()`, que está limitada a una sola instancia de `Worksheet`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh a Single Pivot Table
Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de qué haya cambiado realmente: los datos de origen subyacentes, o solo la configuración de vista/diseño de la propia tabla dinámica.

### Source Data Changed — Use `PivotCache.refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.getPivotCache().refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

### Only View/Layout Changed — Use `calculateData()`
Si los datos de origen *no* han cambiado pero solo se han modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente o se ha activado/desactivado la configuración de actualizar al abrir), no es necesario volver al origen de datos. La caché ya contiene los datos correctos; solo es necesario recalcular el `PivotTable` renderizado. En este caso, `pivotTable.calculateData()` es la opción correcta.
El siguiente ejemplo modifica una propiedad no relacionada con el origen de la tabla dinámica y luego llama a `calculateData()` para volver a renderizarla desde la caché existente.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivotTable.calculateData()
# Save the workbook to disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de la caché compartida, use `PivotCache.getPivotTables()`. Este método devuelve la colección de cada `PivotTable` que depende de la caché indicada.

## Migrating from the Obsolete `PivotTable.refreshData()`
Antes de Aspose.Cells for Python via Java v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.refreshData()` en cada tabla dinámica individualmente. A partir de la v26.7, ese método está marcado como **obsoleto** y debe reemplazarse por las API conscientes de la caché descritas anteriormente.
Hay dos razones por las que el enfoque `refreshData()` por tabla es problemático en libros del mundo real:
- Recupera datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
Los reemplazos recomendados son:
El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con varias tablas dinámicas que comparten una sola caché.

## Which Refresh API Should I Use?
La tabla siguiente resume las API de actualización disponibles y cuándo elegir cada una.
| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo el libro | `Workbook.refreshAll()` | Una sola llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una hoja | `Worksheet.refreshPivotTables()` | Limitada a una hoja de cálculo. |
| Cambiaron los datos de origen para una caché | `pivotTable.getPivotCache().refresh()` | Actualiza TODAS las tablas dinámicas en esa caché compartida. |
| Solo cambiaron los ajustes de vista/diseño | `pivotTable.calculateData()` | Evita viajes innecesarios al origen. |
| Listar todas las tablas dinámicas en una caché compartida | `pivotCache.getPivotTables()` | Úsela para enumerar antes de una actualización masiva. |
En la práctica, prefiera las API basadas en caché sobre el obsoleto `refreshData()` por tabla. Son conscientes de las cachés compartidas, evitan lecturas redundantes del origen y le permiten elegir el alcance más pequeño que satisfaga su requisito de actualización.

## Common Pitfalls
- **Olvidar actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores renderizados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica celdas de origen, llame a `PivotCache.refresh()` (o `Workbook.refreshAll()`) antes de `Workbook.save()`, de lo contrario, el archivo guardado seguirá conteniendo los valores agregados antiguos.
- **Llamar al obsoleto `RefreshData()` por tabla.** En la v26.7, `PivotTable.RefreshData()` está marcado como obsoleto y recupera el origen en cada llamada. Con varias tablas dinámicas que comparten una caché, esto significa N lecturas redundantes del origen. Reemplácelo con una sola llamada a `PivotCache.refresh()` seguida de `calculateData()` por tabla.
- **Actualizar cuando solo cambió el diseño.** Si solo cambió la vista de una tabla dinámica (orden de columnas, `ConsolidationFunction`, etc.) sin tocar los datos de origen, `PivotCache.refresh()` es innecesario y lento. Llame a `pivotTable.calculateData()` para volver a renderizar desde la caché existente.
- **Origen externo no compatible con `PivotCache.refresh()`.** Si el origen de la tabla dinámica proviene de una conexión externa (base de datos, cubo OLAP, etc.), `PivotCache.refresh()` no puede actualizarla en la v26.7; actualmente solo admite los tipos de origen `Sheet` y `Consolidation`. Para orígenes externos, vuelva a abrir el libro o reconstruya la caché desde el origen.

{{< app/cells/assistant language="python" >}}