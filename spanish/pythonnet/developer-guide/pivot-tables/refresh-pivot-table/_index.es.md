---
title: Actualizar tablas dinámicas en Aspose.Cells for Python via .NET
linktitle: Actualizar tablas dinámicas en Aspose.Cells for Python via .NET
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for Python via .NET utilizando la API de actualización de tablas dinámicas de la versión 26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos de código prácticos.
keywords: Aspose.Cells, Python via .NET, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells ofrece una API de actualización en capas que le permite recargar datos dinámicos en cuatro ámbitos diferentes, desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for Python via .NET v26.7**, el método heredado `PivotTable.refresh_data()` está marcado como obsoleto y debe reemplazarse por las API más eficientes y conscientes de la caché descritas en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una operación única. Detrás de escena, Aspose.Cells mantiene una cadena de datos en capas que conecta los datos de origen originales con los valores representados que se ven en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cualquier situación.

La cadena de datos de cuatro capas es:

1. **Origen de datos** — los rangos de la hoja de cálculo originales, la consulta de base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solo* de su `PivotCache`, nunca directamente del origen de datos.
4. **Cells** — las `Cells` de la hoja de cálculo en las que la `PivotTable` representa sus valores calculados y estilos.

Un concepto particularmente importante es la **caché compartida**. Cuando varias tablas dinámicas en un libro hacen referencia al mismo rango de origen, comparten *una* instancia de `PivotCache`. Una sola `PivotCache` puede ser referenciada por muchas tablas dinámicas, y al actualizar esa caché se actualizan todas las `PivotTable` dependientes a la vez.

{{% alert color="primary" %}}

`PivotCache.source_type` (enum `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de la versión 26.7, `PivotCache.refresh()` admite solo los tipos de origen **`Sheet`** y **`Consolidation`**; es decir, datos que residen en rangos de hojas de cálculo. Los orígenes externos (bases de datos, conexiones externas, etc.) aún no se pueden actualizar mediante la API de caché.

{{% /alert %}}

Debido a esta cadena, existen dos rutas fundamentales de actualización en Aspose.Cells:

- **`PivotCache.refresh()`** — recarga el origen a la caché Y recalcula todas las `PivotTable` dependientes en una sola operación.
- **`PivotTable.calculate_data()`** — recalcula la visualización de una `PivotTable` a partir de los datos ya almacenados en caché, sin volver al origen de datos.

Todos los escenarios de este artículo utilizan datos de origen de celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Importaciones requeridas

Todos los ejemplos de Python en este artículo comienzan con las siguientes tres sentencias de importación porque los tipos de tablas dinámicas se encuentran en el namespace `aspose.cells.pivot`:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Actualizar todas las tablas dinámicas del libro

Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica del libro refleje los datos de origen más recientes, la API más sencilla y completa es `Workbook.refresh_all()`. Una sola llamada recorre todo el libro, actualizando cada `PivotCache` desde su origen y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento cuando el rendimiento no es una preocupación.

El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `refresh_all()` para actualizar todo en una sola llamada.

```python
import aspose.cells as ac

# Crear un nuevo libro de trabajo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Escribir fila de encabezado en las celdas A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Escribir filas de datos en las celdas A2:C9 (8 filas de datos de frutas entre 2020 y 2021)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)

# Agregar una tabla dinámica: rango de origen "A1:C9", celda de destino "E3", nombre "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Asignar campos dinámicos: Fruit a Filas, Year a Columnas, Amount a Datos
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modificar varios valores de Amount en los datos de origen para simular cambios
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Actualizar todas las tablas dinámicas / caché dinámica en el libro de trabajo
workbook.refresh_all()

# Guardar el libro de trabajo
workbook.save("output.xlsx")
```

## Actualizar todas las tablas dinámicas de una sola hoja de cálculo

A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica; por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas de cálculo no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells proporciona `Worksheet.refresh_pivot_tables()`, que está limitado a una sola instancia de `Worksheet`.

Esto es más selectivo que `Workbook.refresh_all()`: solo se actualizan las tablas dinámicas de la hoja de cálculo objetivo, dejando intactas las tablas dinámicas de otras hojas de cálculo.

El siguiente ejemplo rellena los mismos datos de origen Fruta/Año/Cantidad, agrega una tabla dinámica en la primera hoja de cálculo, modifica algunos valores de origen y luego actualiza solo las tablas dinámicas de esa hoja de cálculo.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)

pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)

worksheet.refresh_pivot_tables()

workbook.save("output.xlsx")
```

## Actualizar una sola tabla dinámica

Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente haya cambiado: los datos de origen subyacentes, o solo la configuración de vista/diseño de la propia tabla dinámica.

### Cambiaron los datos de origen — Utilice `PivotCache.refresh()`

Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivot_table.pivot_cache.refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

{{% alert color="primary" %}}

Dado que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.refresh()` recalcula **todas** las tablas dinámicas construidas sobre esa misma caché, no solo la que usted referencia. Si dos tablas dinámicas comparten el mismo rango de origen, al actualizar una caché se actualizan ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen para demostrar este comportamiento de caché compartida, modifica algunos valores de origen y luego actualiza a través de una referencia de caché.

```python
import aspose.cells as ac

# Crear un nuevo libro de trabajo y acceder a la primera hoja de trabajo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Escribir la fila de encabezado: Fruta / Año / Cantidad
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Escribir aproximadamente 9 filas de datos (uva / arándano / kiwi / cereza en 2020-2021)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# Agregar la primera tabla dinámica "Pivot1" anclada en la celda E3, rango de origen A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Asignar campos para Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Agregar una SEGUNDA tabla dinámica "Pivot2" anclada en E15 usando el MISMO rango de origen A1:C9
# Tanto Pivot1 como Pivot2 comparten un único PivotCache porque el rango de origen es idéntico.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Asignar los mismos campos para Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modificar varios valores de celdas de Cantidad en los datos de origen para simular un cambio de datos
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Refrescar el PivotCache compartido.
# Debido a que Pivot1 y Pivot2 comparten el mismo PivotCache, esta única llamada
# refresca AMBAS tablas dinámicas (datos + estilo) desde el origen actualizado.
pivotTable1.pivot_cache.refresh()

# Guardar el libro de trabajo
workbook.save("output.xlsx")
```

### Solo cambió la vista/diseño — Utilice `calculate_data()`

Si los datos de origen *no* han cambiado pero solo se han modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente o se ha cambiado una configuración de actualización al abrir), no es necesario volver al origen de datos. La caché ya contiene los datos correctos; solo es necesario recalcular la `PivotTable` representada. En este caso, `pivot_table.calculate_data()` es la opción correcta.

Esto evita la recuperación innecesaria del origen y es significativamente más rápido cuando muchas tablas dinámicas comparten la misma caché.

El siguiente ejemplo modifica una propiedad que no es de origen de la tabla dinámica y luego llama a `calculate_data()` para volver a representarla desde la caché existente.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Escribir fila de encabezado Fruta / Año / Cantidad
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Escribir 8 filas de datos (filas 2-9, ajustándose al rango de origen A1:C9)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)

# Agregar una tabla dinámica llamada "Pivot1" ubicada en la celda de destino E3, con origen en A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Asignar campos: Fruta a Fila, Año a Columna, Cantidad a Datos
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Modificar una propiedad de vista/disposición — este es un cambio solo de presentación,
# por lo que NO requiere volver a leer los datos de origen mediante PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) desde los
# datos ya almacenados en el PivotCache. Como los datos de origen no cambiaron,
# no se realiza un viaje de ida y vuelta al origen — solo se recalculan los valores en caché
# en las celdas de la hoja de cálculo.
pivot_table.calculate_data()

# Guardar el libro de trabajo en disco
workbook.save("output.xlsx")
```

## Obtener todas las tablas dinámicas que comparten la misma PivotCache

Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de la caché compartida, utilice `PivotCache.get_pivot_tables()`. Este método devuelve la colección de cada `PivotTable` que depende de la caché indicada.

Esta es también la forma más directa de confirmar que dos tablas dinámicas realmente comparten la misma instancia de `PivotCache`: puede comparar referencias de caché, o simplemente iterar la colección devuelta por `get_pivot_tables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango de origen, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas de la caché.


## Migración desde el método obsoleto `PivotTable.refresh_data()`

Antes de Aspose.Cells for Python via .NET v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.refresh_data()` en cada tabla dinámica individualmente. A partir de la versión 26.7, ese método está marcado como **obsoleto** y debe reemplazarse por las API conscientes de la caché descritas anteriormente.

Hay dos razones por las que el enfoque `refresh_data()` por tabla es problemático en libros del mundo real:

- Vuelve a obtener datos del origen *cada* vez que se llama, incluso cuando el origen no ha cambiado.
- Cada llamada actualiza toda la caché compartida. Cuando muchas tablas dinámicas comparten una caché, llamar repetidamente a `refresh_data()` por tabla dinámica hace que la misma caché se vuelva a obtener una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas del libro** → use `workbook.refresh_all();`
- **Actualizar ALGUNAS de ellas** → use `pivot_table.pivot_cache.refresh();` para una caché. Dado que la caché es compartida, esta única llamada actualiza cada tabla dinámica construida sobre esa caché. Otras tablas dinámicas que se asientan sobre una caché ya actualizada se pueden omitir de forma segura.
- **Solo cambió la vista/diseño de la tabla dinámica** → use `pivot_table.calculate_data();` para volver a representar desde la caché existente sin ninguna ida y vuelta al origen.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros con varias tablas dinámicas que comparten una sola caché.

```python
import aspose.cells as ac

# Crear un nuevo libro de trabajo y acceder a la primera hoja
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Construir los datos de origen: Fruta / Año / Cantidad (encabezado + 9 filas) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- Agregar la primera tabla dinámica (Pivot1) en la celda de destino E3 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Agregar la SEGUNDA tabla dinámica (Pivot2) en el MISMO rango de origen ---
# Tanto Pivot1 como Pivot2 comparten UN único PivotCache subyacente.
# Este es exactamente el escenario donde el enfoque heredado por tabla RefreshData()
# se vuelve ineficiente: al actualizar una tabla se vuelve a obtener todo
# el caché compartido, por lo que actualizar N tablas realiza la misma obtención costosa N veces.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Modificar varios valores de Cantidad en los datos de origen ---
sheet.cells["C2"].put_value(5000)   # Uva 2020
sheet.cells["C5"].put_value(7500)   # Cereza 2020
sheet.cells["C9"].put_value(9500)   # Cereza 2021

# --- Patrón OBSOLETO (anterior a 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # vuelve a obtener datos del origen, actualiza todo el caché
# pivot_table2.refresh_data();  # vuelve a obtener datos DE NUEVO — ¡el caché ya está actualizado!
# Cada llamada reconstruye el caché compartido, por lo que N tablas = N obtenciones redundantes.

# --- NUEVO patrón v26.7+: actualizar el caché UNA VEZ, luego volver a renderizar según sea necesario ---
# Una sola llamada a PivotCache.Refresh() extrae los valores modificados en el caché compartido
# Y recalcula la visualización de TODAS las tablas dinámicas que lo referencian.
# Dado que Pivot1 y Pivot2 comparten un único PivotCache, esta única llamada actualiza
# ambas tablas — no se requiere un segundo viaje al origen.
pivot_table1.pivot_cache.refresh()

# CalculateData() solo vuelve a renderizar la visualización (datos + estilo) de una tabla dinámica
# a partir de los datos ya contenidos en el caché — NO toca el origen.
# Lo llamamos en Pivot2 aquí puramente para demostrar la API: después de que el caché
# se haya actualizado una vez, cualquier tabla dependiente se puede volver a renderizar sin
# volver al origen. Use CalculateData() por sí solo cuando solo la
# configuración de vista/disposición de la tabla dinámica haya cambiado y el caché esté actualizado.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## ¿Qué API de actualización debo usar?

La tabla siguiente resume las API de actualización disponibles y cuándo elegir cada una.

| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo el libro | `Workbook.refresh_all()` | Una sola llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una sola hoja | `Worksheet.refresh_pivot_tables()` | Limitado a una hoja de cálculo. |
| Cambiaron los datos de origen de una caché | `pivot_table.pivot_cache.refresh()` | Actualiza TODAS las tablas dinámicas de esa caché compartida. |
| Solo cambió la configuración de vista/diseño | `pivot_table.calculate_data()` | Omite la ida y vuelta innecesaria al origen. |
| Listar todas las tablas dinámicas de una caché compartida | `pivot_cache.get_pivot_tables()` | Úselo para enumerar antes de una actualización masiva. |

En la práctica, prefiera las API basadas en caché sobre el método obsoleto `refresh_data()` por tabla. Son conscientes de las cachés compartidas, evitan búsquedas redundantes en el origen y le permiten elegir el ámbito más pequeño que satisface su requisito de actualización.

{{< app/cells/assistant language="python" >}}
