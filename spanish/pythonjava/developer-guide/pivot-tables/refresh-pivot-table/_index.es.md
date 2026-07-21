---
title: Actualización de tablas dinámicas en Aspose.Cells for Python via Java
linktitle: Actualización de tablas dinámicas en Aspose.Cells for Python via Java
description: Aprenda cómo actualizar tablas dinámicas en Aspose.Cells for Python via Java utilizando la API de actualización de pivote v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos de código prácticos.
keywords: Aspose.Cells, Python via Java, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells ofrece una API de actualización en capas que le permite recargar datos de pivote en cuatro alcances diferentes, desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for Aspose.Cells for Python via Java v26.7**, el método heredado `PivotTable.refreshData()` está marcado como obsoleto y debe reemplazarse con las APIs más eficientes y conscientes de la caché descritas en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una sola operación. Entre bastidores, Aspose.Cells mantiene una cadena de datos en capas que conecta sus datos de origen originales con los valores renderizados que ve en la hoja de cálculo. Comprender esta cadena es clave para elegir la API de actualización adecuada para cualquier situación.

La cadena de datos de cuatro capas es:

1. **Fuente de datos** — los rangos de la hoja de cálculo originales, la consulta a la base de datos o el rango de consolidación donde viven los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solo* desde su `PivotCache`, nunca directamente desde la fuente de datos.
4. **Celdas** — las `Cells` de la hoja de cálculo donde la `PivotTable` renderiza sus valores calculados y estilos.

Un concepto particularmente importante es la **caché compartida**. Cuando varias tablas dinámicas en un libro hacen referencia al mismo rango de origen, comparten *una* instancia de `PivotCache`. Un solo `PivotCache` puede ser referenciado por muchas tablas dinámicas, y actualizar esa caché actualiza cada `PivotTable` dependiente a la vez.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de la v26.7, `PivotCache.refresh()` admite solo los tipos de origen **`SHEET`** y **`CONSOLIDATION`**, es decir, datos que viven en rangos de hoja de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no se pueden actualizar a través de la API de caché.

{{% /alert %}}

Debido a esta cadena, existen dos rutas de actualización fundamentales en Aspose.Cells:

- **`PivotCache.refresh()`** — recarga origen → caché Y recalcula todas las `PivotTable`s dependientes en una sola operación.
- **`PivotTable.calculateData()`** — recalcula la visualización de una `PivotTable` a partir de datos ya en caché, sin volver a la fuente de datos.

Todos los escenarios en este artículo utilizan datos de origen de celdas de hoja de cálculo, por lo que el tipo de origen es `SHEET` y las operaciones de actualización se comportan como se describe.

## Importaciones Requeridas

Todos los ejemplos de Python en este artículo dependen de las siguientes importaciones porque los tipos de pivote viven en el espacio de nombres `aspose.cells.pivot`:

- `import jpype`
- `import aspose.cells as cells`

El módulo `jpype` se utiliza para arrancar la JVM, mientras que `aspose.cells` expone los tipos de libro/hoja de cálculo/celda/pivote utilizados a lo largo del artículo.

## Actualizar Todas las Tablas Dinámicas en el Libro

Cuando necesita asegurarse de que cada caché de pivote y cada tabla dinámica en el libro refleje los datos de origen más recientes, la API más simple y completa es `Workbook.refreshAll()`. Una sola llamada recorre todo el libro, actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales de documentos completos donde el rendimiento no es una preocupación.

El siguiente ejemplo construye un libro con un rango de origen Fruta/Año/Monto, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `refreshAll()` para poner todo al día en una sola llamada.

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

# Actualizar todas las tablas dinámicas / caché dinámica en el libro de trabajo
workbook.refreshAll()

# Guardar el libro de trabajo
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Actualizar Todas las Tablas Dinámicas en una Sola Hoja de Cálculo

A veces solo necesita actualizar las tablas dinámicas que viven en una hoja de cálculo específica, por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas de cálculo no están relacionadas y no deben tocarse. Para este caso, Aspose.Cells proporciona `Worksheet.refreshPivotTables()`, que está limitado a una sola instancia de `Worksheet`.

Esto es más selectivo que `Workbook.refreshAll()`: solo se actualizan las tablas dinámicas en la hoja de cálculo objetivo, dejando intactas las tablas dinámicas en otras hojas de cálculo.

El siguiente ejemplo completa los mismos datos de origen Fruta/Año/Monto, agrega una tabla dinámica en la primera hoja de cálculo, modifica algunos valores de origen y luego actualiza solo las tablas dinámicas en esa hoja de cálculo.

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

## Actualizar una Sola Tabla Dinámica

Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente cambió: los datos de origen subyacentes, o solo la configuración de vista/diseño de la tabla dinámica misma.

### Cambiaron los Datos de Origen — Use `PivotCache.refresh()`

Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivotTable.getPivotCache().refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

{{% alert color="primary" %}}

Debido a que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.refresh()` recalcula **todas** las tablas dinámicas construidas sobre esa misma caché, no solo la que usted referencia. Si dos tablas dinámicas comparten el mismo rango de origen, actualizar una caché actualiza ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas en el mismo rango de origen para demostrar este comportamiento de caché compartida, modifica algunos valores de origen y luego actualiza a través de una referencia de caché.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crear un nuevo libro de trabajo y acceder a la primera hoja
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Escribir fila de encabezado: Fruta / Año / Cantidad
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Escribir aproximadamente 9 filas de datos (uva / arándano / kiwi / cereza a través de 2020-2021)
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
# Debido a que Pivot1 y Pivot2 comparten el mismo PivotCache, esta única llamada
# actualiza AMBAS tablas dinámicas (datos + estilo) desde el origen actualizado.
pivotTable1.getPivotCache().refresh()

# Guardar el libro de trabajo
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Solo Cambió la Vista/Diseño — Use `calculateData()`

Si los datos de origen *no* han cambiado pero solo se han modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, un campo se ha movido a un área diferente, o se ha alternado una configuración de actualización al abrir), no hay necesidad de volver a la fuente de datos. La caché ya contiene los datos correctos; solo la `PivotTable` renderizada necesita recálculo. En este caso, `pivotTable.calculateData()` es la opción correcta.

Esto evita la obtención innecesaria de la fuente y es significativamente más rápido cuando muchas tablas dinámicas comparten la misma caché.

El siguiente ejemplo modifica una propiedad que no es de origen de la tabla dinámica y luego llama a `calculateData()` para volver a renderizarla desde la caché existente.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Escribir la fila de encabezado Fruit / Year / Amount
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

# Agregar una tabla dinámica llamada "Pivot1" colocada en la celda de destino E3, con origen en A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Asignar campos: Fruit a Fila, Year a Columna, Amount a Datos
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Modificar una propiedad de vista/disposición — este es un cambio solo de presentación,
# por lo que NO requiere volver a leer los datos de origen a través de PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# calculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) a partir de
# los datos ya almacenados en el PivotCache. Debido a que los datos de origen no cambiaron,
# no se realiza ningún viaje de ida y vuelta al origen — solo se recalculan los valores en caché
# en las celdas de la hoja de cálculo.
pivotTable.calculateData()

# Guardar el libro de trabajo en disco
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Obtener Todas las Tablas Dinámicas que Comparten el Mismo PivotCache

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes, o para diagnosticar el impacto de la caché compartida, use `PivotCache.getPivotTables()`. Este método devuelve la colección de cada `PivotTable` que depende de la caché dada.

Esta es también la forma más directa de confirmar que dos tablas dinámicas efectivamente comparten la misma instancia de `PivotCache`: puede comparar referencias de caché, o simplemente iterar la colección devuelta por `getPivotTables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas en el mismo rango de origen, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas de la caché.

```python
[code]

But the developer says don't use 

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# código portado aquí
workbook = Workbook()
...

Wait, but the developer forbids 
Code

But developer says no 

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

## Migración desde el Obsoleto `PivotTable.refreshData()`

Antes de Aspose.Cells for Aspose.Cells for Python via Java v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.refreshData()` en cada tabla dinámica individualmente. A partir de la v26.7, ese método está marcado como **obsoleto** y debe reemplazarse con las APIs conscientes de la caché descritas anteriormente.

Hay dos razones por las que el enfoque `refreshData()` por tabla es problemático en libros del mundo real:

- Vuelve a obtener datos de la fuente *cada* vez que se llama, incluso cuando la fuente no ha cambiado.
- Cada llamada actualiza toda la caché compartida. Cuando muchas tablas dinámicas comparten una caché, llamar repetidamente a `refreshData()` por tabla dinámica hace que la misma caché se vuelva a obtener una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas en el libro** → use `workbook.refreshAll();`
- **Actualizar ALGUNAS de ellas** → use `pivotTable.getPivotCache().refresh();` para una caché. Debido a que la caché es compartida, esta sola llamada actualiza cada tabla dinámica construida sobre esa caché. Otras tablas dinámicas que se asientan sobre una caché ya actualizada se pueden omitir de forma segura.
- **Solo cambió la vista/diseño del pivote** → use `pivotTable.calculateData();` para volver a renderizar desde la caché existente sin ningún viaje de ida y vuelta a la fuente.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con múltiples tablas dinámicas que comparten una sola caché.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crear un nuevo libro de trabajo y acceder a la primera hoja
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

# --- Agregar la SEGUNDA tabla dinámica (Pivot2) sobre el MISMO rango de origen ---
# Tanto Pivot1 como Pivot2 comparten UN único PivotCache subyacente.
# Este es exactamente el escenario en el que el enfoque heredado por tabla RefreshData()
# se vuelve ineficiente: al actualizar una tabla se vuelve a obtener todo el
# caché compartido, por lo que actualizar N tablas realiza la misma obtención costosa N veces.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Modificar varios valores de Amount en los datos de origen ---
sheet.getCells().get("C2").putValue(5000)   # Grape  2020
sheet.getCells().get("C5").putValue(7500)   # Cherry 2020
sheet.getCells().get("C9").putValue(9500)   # Cherry 2021

# --- Patrón OBSOLETO (anterior a 26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // vuelve a obtener los datos del origen y actualiza todo el caché
# pivotTable2.RefreshData();  // vuelve a obtener NUEVAMENTE — ¡el caché ya está actualizado!
# Cada llamada reconstruye el caché compartido, por lo que N tablas = N obtenciones redundantes.

# --- NUEVO patrón v26.7+: actualizar el caché UNA VEZ y luego volver a renderizar según sea necesario ---
# Una sola llamada a PivotCache.Refresh() extrae los valores modificados al caché compartido
# Y recalcula la visualización de CADA tabla dinámica que hace referencia a él.
# Dado que Pivot1 y Pivot2 comparten un único PivotCache, esta única llamada actualiza
# ambas tablas — no se requiere un segundo viaje de ida y vuelta al origen.
pivotTable1.getPivotCache().refresh()

# CalculateData() solo vuelve a renderizar la visualización de una tabla dinámica (datos + estilo)
# a partir de los datos que ya están almacenados en el caché — NO toca el origen.
# Lo llamamos en Pivot2 aquí puramente para demostrar la API: después de que el caché
# se haya actualizado una vez, cualquier tabla dependiente puede volver a renderizarse sin
# volver al origen. Use CalculateData() por sí sola cuando solo haya cambiado la configuración
# de vista/disposición de la tabla dinámica y el caché esté actualizado.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## ¿Qué API de Actualización Debo Usar?

La tabla a continuación resume las APIs de actualización disponibles y cuándo elegir cada una.

| Objetivo | API Recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro | `Workbook.refreshAll()` | Una llamada; cubre todas las cachés y tablas. |
| Actualizar solo tablas dinámicas en una sola hoja | `Worksheet.refreshPivotTables()` | Limitado a una hoja de cálculo. |
| Cambiaron los datos de origen para una caché | `pivotTable.getPivotCache().refresh()` | Actualiza TODAS las tablas dinámicas en esa caché compartida. |
| Solo cambiaron las configuraciones de vista/diseño | `pivotTable.calculateData()` | Omite el viaje innecesario a la fuente. |
| Listar todas las tablas dinámicas en una caché compartida | `pivotCache.getPivotTables()` | Úselo para enumerar antes de una actualización masiva. |

En la práctica, prefiera las APIs basadas en caché sobre el obsoleto `refreshData()` por tabla. Son conscientes de las cachés compartidas, evitan obtenciones redundantes de la fuente y le permiten elegir el alcance más pequeño que satisfaga su requisito de actualización.

{{< app/cells/assistant language="python" >}}