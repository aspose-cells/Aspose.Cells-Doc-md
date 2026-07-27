---
title: Actualizar tablas dinámicas en Aspose.Cells for Python via Java
linktitle: Actualizar tablas dinámicas en Aspose.Cells for Python via Java
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for Python via Java utilizando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, Python via Java, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece una API de actualización en capas que permite recargar los datos de las tablas dinámicas en cuatro niveles diferentes, desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for Python via Java v26.7**, el método heredado `PivotTable.refreshData()` está marcado como obsoleto y debe sustituirse por las API más eficientes y conscientes de la caché que se describen en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una operación única. Detrás de escena, Aspose.Cells mantiene una cadena de datos en capas que conecta los datos de origen originales con los valores representados en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cada situación.

La cadena de datos de cuatro capas es:

1. **Origen de datos** — los rangos originales de la hoja de cálculo, la consulta a la base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solo* desde su `PivotCache`, nunca directamente desde el origen de datos.
4. **Cells** — las `Cells` de la hoja de cálculo en las que la `PivotTable` representa sus valores calculados y estilos.

Un concepto especialmente importante es la **caché compartida**. Cuando varias tablas dinámicas de un libro hacen referencia al mismo rango de origen, comparten *una* instancia de `PivotCache`. Un solo `PivotCache` puede ser referenciado por muchas tablas dinámicas, y al actualizar esa caché se actualizan todas las `PivotTable` dependientes a la vez.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica de dónde proceden los datos de la caché. A partir de la v26.7, `PivotCache.refresh()` solo admite los tipos de origen **`SHEET`** y **`CONSOLIDATION`**, es decir, datos que residen en rangos de hoja de cálculo. Los orígenes externos (bases de datos, conexiones externas, etc.) aún no se pueden actualizar a través de la API de caché.

{{% /alert %}}

Gracias a esta cadena, existen dos rutas de actualización fundamentales en Aspose.Cells:

- **`PivotCache.refresh()`** — recarga origen → caché Y recalcula todas las `PivotTable` dependientes en una sola operación.
- **`PivotTable.calculateData()`** — recalcula la visualización de una `PivotTable` a partir de los datos ya almacenados en caché, sin volver al origen de datos.

Todos los escenarios de este artículo utilizan datos de origen en celdas de hoja de cálculo, por lo que el tipo de origen es `SHEET` y las operaciones de actualización se comportan como se describe.

## Importaciones necesarias

Todos los ejemplos de Python de este artículo dependen de las siguientes importaciones porque los tipos de tablas dinámicas se encuentran en el espacio de nombres `aspose.cells.pivot`:

- `import jpype`
- `import aspose.cells as cells`

El módulo `jpype` se utiliza para arrancar la JVM, mientras que `aspose.cells` expone los tipos de libro, hoja de cálculo, celda y tabla dinámica utilizados a lo largo del documento.

## Actualizar todas las tablas dinámicas del libro

Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica del libro reflejen los últimos datos de origen, la API más sencilla y completa es `Workbook.refreshAll()`. Una sola llamada recorre todo el libro, actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales de todo el documento donde el rendimiento no sea una preocupación.

El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `refreshAll()` para actualizarlo todo en una sola llamada.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crear un nuevo libro de trabajo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Escribir la fila de encabezado en las celdas A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Escribir filas de datos en las celdas A2:C9 (8 filas de datos de frutas entre 2020 y 2021)
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

# Agregar una tabla dinámica: rango de origen "A1:C9", celda de destino "E3", nombre "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Asignar campos dinámicos: Fruta a Filas, Año a Columnas, Cantidad a Datos
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Modificar varios valores de Cantidad en los datos de origen para simular cambios
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Actualizar todas las tablas dinámicas / cachés dinámicos en el libro de trabajo
workbook.refreshAll()

# Guardar el libro de trabajo
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Actualizar todas las tablas dinámicas de una sola hoja

A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja específica; por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas no están relacionadas y no deben tocarse. Para este caso, Aspose.Cells ofrece `Worksheet.refreshPivotTables()`, que está limitado a una sola instancia de `Worksheet`.

Esta API es más selectiva que `Workbook.refreshAll()`: solo se actualizan las tablas dinámicas de la hoja de destino, dejando intactas las que se encuentren en otras hojas.

El siguiente ejemplo rellena los mismos datos de origen Fruta/Año/Cantidad, añade una tabla dinámica en la primera hoja, modifica algunos valores de origen y luego actualiza únicamente las tablas dinámicas de esa hoja.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
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

## Actualizar una sola tabla dinámica

Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente haya cambiado: los datos de origen subyacentes, o solo la configuración de vista/diseño de la propia tabla dinámica.

### Los datos de origen cambiaron — Use `PivotCache.refresh()`

Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.getPivotCache().refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula todas las `PivotTable` que dependen de esa caché.

{{% alert color="primary" %}}

Dado que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.refresh()` recalcula **todas** las tablas dinámicas construidas sobre esa misma caché, no solo aquella a la que hace referencia. Si dos tablas dinámicas comparten el mismo rango de origen, al actualizar una caché se actualizan ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen para demostrar este comportamiento de caché compartida, modifica algunos valores de origen y luego actualiza a través de una referencia a la caché.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crear un nuevo libro de trabajo y acceder a la primera hoja de cálculo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Escribir la fila de encabezado: Fruta / Año / Cantidad
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Escribir aproximadamente 9 filas de datos (uva / arándano / kiwi / cereza entre 2020-2021)
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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# Agregar la primera tabla dinámica "Pivot1" anclada en la celda E3, rango de origen A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Asignar campos para Pivot1
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Agregar una SEGUNDA tabla dinámica "Pivot2" anclada en E15 usando el MISMO rango de origen A1:C9
# Tanto Pivot1 como Pivot2 comparten un único PivotCache porque el rango de origen es idéntico.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Asignar los mismos campos para Pivot2
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Modificar varios valores de celda de Cantidad en los datos de origen para simular un cambio de datos
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Actualizar el PivotCache compartido.
# Dado que Pivot1 y Pivot2 comparten el mismo PivotCache, esta única llamada
# actualiza AMBAS tablas dinámicas (datos + estilo) desde el origen actualizado.
pivotTable1.getPivotCache().refresh()

# Guardar el libro de trabajo
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Solo cambió la vista/diseño — Use `calculateData()`

Si los datos de origen *no* han cambiado pero solo se han modificado las opciones de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente, o se ha activado/desactivado la opción de actualizar al abrir), no es necesario volver al origen de datos. La caché ya contiene los datos correctos; solo es necesario recalcular la `PivotTable` representada. En este caso, `pivotTable.calculateData()` es la opción correcta.

Esto evita la recuperación innecesaria desde el origen y es significativamente más rápido cuando muchas tablas dinámicas comparten la misma caché.

El siguiente ejemplo modifica una propiedad no relacionada con el origen de la tabla dinámica y luego llama a `calculateData()` para volver a renderizarla desde la caché existente.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Escribir fila de encabezado Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Escribir 8 filas de datos (filas 2-9, ajustándose al rango de origen A1:C9)
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

# Agregar una tabla dinámica llamada "Pivot1" ubicada en la celda de destino E3, con origen en A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Asignar campos: Fruit a Fila, Year a Columna, Amount a Datos
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Modificar una propiedad de vista/disposición — este es un cambio solo de presentación,
# por lo que NO requiere volver a leer los datos de origen mediante PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) a partir de los
# datos ya almacenados en el PivotCache. Debido a que los datos de origen no cambiaron,
# no se realiza un viaje de ida y vuelta al origen — solo los valores en caché se recalculan
# en las celdas de la hoja de cálculo.
pivotTable.calculateData()

# Guardar el libro de trabajo en disco
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Obtener todas las tablas dinámicas que comparten el mismo PivotCache

Un libro a menudo contiene muchas tablas dinámicas que se apoyan en una única caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de la caché compartida, use `PivotCache.getPivotTables()`. Este método devuelve la colección de todas las `PivotTable` que dependen de la caché indicada.

Esta es también la forma más directa de confirmar que dos tablas dinámicas efectivamente comparten la misma instancia de `PivotCache`: puede comparar las referencias a la caché, o simplemente iterar la colección devuelta por `getPivotTables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas de la caché.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# código portado aquí
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()
print("Pivot1 and Pivot2 share the same PivotCache: " + str(sameCache))

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Migración desde el obsoleto `PivotTable.refreshData()`

Antes de Aspose.Cells for Python via Java v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.refreshData()` en cada tabla dinámica de forma individual. A partir de la v26.7, ese método está marcado como **obsoleto** y debe sustituirse por las API conscientes de la caché descritas anteriormente.

Hay dos razones por las que el enfoque `refreshData()` por tabla resulta problemático en libros reales:

- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
- Cada llamada actualiza toda la caché compartida. Cuando muchas tablas dinámicas comparten una misma caché, llamar repetidamente a `refreshData()` por tabla dinámica hace que la misma caché se vuelva a obtener una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas del libro** → use `workbook.refreshAll();`
- **Actualizar ALGUNAS** → use `pivotTable.getPivotCache().refresh();` para una caché. Como la caché es compartida, esta única llamada actualiza todas las tablas dinámicas construidas sobre esa caché. Se pueden omitir de forma segura otras tablas dinámicas que se apoyen en una caché ya actualizada.
- **Solo cambió la vista/diseño** → use `pivotTable.calculateData();` para volver a renderizar desde la caché existente sin volver al origen.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con múltiples tablas dinámicas que comparten una única caché.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crear un nuevo libro de trabajo y acceder a la primera hoja de cálculo
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Construir los datos de origen: Fruta / Año / Monto (encabezado + 9 filas) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- Agregar la primera tabla dinámica (Pivot1) en la celda de destino E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Agregar la SEGUNDA tabla dinámica (Pivot2) en el MISMO rango de origen ---
# Tanto Pivot1 como Pivot2 comparten UN ÚNICO PivotCache subyacente.
# Este es exactamente el escenario donde el enfoque heredado por tabla RefreshData()
# resulta ineficiente: actualizar una tabla vuelve a obtener todo el caché
# compartido, por lo que actualizar N tablas realiza la misma obtención costosa N veces.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Modificar varios valores de Monto en los datos de origen ---
sheet.getCells().get("C2").putValue(5000)   # Grape  2020
sheet.getCells().get("C5").putValue(7500)   # Cherry 2020
sheet.getCells().get("C9").putValue(9500)   # Cherry 2021

# --- Patrón OBSOLETO (pre-26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // vuelve a obtener del origen, actualiza todo el caché
# pivotTable2.RefreshData();  // vuelve a obtener DE NUEVO — ¡el caché ya está actualizado!
# Cada llamada reconstruye el caché compartido, por lo que N tablas = N obtenciones redundantes.

# --- NUEVO patrón v26.7+: actualizar el caché UNA VEZ, luego volver a renderizar según sea necesario ---
# Una llamada a PivotCache.Refresh() extrae los valores modificados en el caché
# compartido Y recalcula la visualización de TODAS las tablas dinámicas que lo referencian.
# Dado que Pivot1 y Pivot2 comparten un PivotCache, esta única llamada actualiza
# ambas tablas — no se requiere un segundo viaje al origen.
pivotTable1.getPivotCache().refresh()

# CalculateData() solo vuelve a renderizar la visualización de una tabla dinámica (datos + estilo)
# a partir de los datos ya contenidos en el caché — NO toca el origen.
# Lo llamamos en Pivot2 aquí únicamente para demostrar la API: después de que el caché
# se ha actualizado una vez, cualquier tabla dependiente puede volver a renderizarse sin
# volver al origen. Use CalculateData() por sí sola cuando solo hayan cambiado
# la vista/disposición de la tabla dinámica y el caché esté actualizado.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## ¿Qué API de actualización debo usar?

La tabla siguiente resume las API de actualización disponibles y cuándo elegir cada una.

| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo el libro | `Workbook.refreshAll()` | Una sola llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una hoja | `Worksheet.refreshPivotTables()` | Limitado a una hoja. |
| Los datos de origen cambiaron para una caché | `pivotTable.getPivotCache().refresh()` | Actualiza TODAS las tablas dinámicas de esa caché compartida. |
| Solo cambió la configuración de vista/diseño | `pivotTable.calculateData()` | Omite el viaje de ida y vuelta al origen innecesario. |
| Listar todas las tablas dinámicas de una caché compartida | `pivotCache.getPivotTables()` | Úselo para enumerar antes de una actualización masiva. |

En la práctica, prefiera las API basadas en caché frente al obsoleto `refreshData()` por tabla. Son conscientes de las cachés compartidas, evitan recuperaciones redundantes del origen y le permiten elegir el alcance más pequeño que satisfaga su requisito de actualización.

## Artículos relacionados

- [Insertar una imagen en una celda](/cells/es/python-java/inserting-an-image-into-a-cell/)
- [Leer y escribir archivos DBF](/cells/es/python-java/dbf/)
- [Dividir archivos Excel en varios archivos](/cells/es/python-java/splitting-excel-files-into-multiple-files/)
- [Minigráficos en Aspose.Cells for Python via Java](/cells/es/python-java/sparkline/)

{{< app/cells/assistant language="python" >}}