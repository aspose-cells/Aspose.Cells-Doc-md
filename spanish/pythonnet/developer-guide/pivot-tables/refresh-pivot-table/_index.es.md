---
title: Actualización de tablas dinámicas en Aspose.Cells for Python via .NET
linktitle: Actualización de tablas dinámicas en Aspose.Cells for Python via .NET
description: Aprenda cómo actualizar tablas dinámicas en Aspose.Cells for Python via .NET utilizando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
keywords: Aspose.Cells, Python via .NET, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una API de actualización en capas que le permite recargar datos de tablas dinámicas en cuatro alcances diferentes, desde todo el libro de trabajo hasta una sola tabla dinámica. A partir de **Aspose.Cells for Python via .NET v26.7**, el método heredado `PivotTable.refresh_data()` está marcado como obsoleto y debe reemplazarse por las APIs más eficientes y conscientes del caché descritas en este artículo.

{{% /alert %}}

## Introducción

Actualizar una tabla dinámica rara vez es una operación única. Detrás de escena, Aspose.Cells mantiene una cadena de datos en capas que conecta sus datos fuente originales con los valores renderizados que ve en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cualquier situación.

La cadena de datos de cuatro capas es:

1. **Fuente de datos**: los rangos de hojas de cálculo originales, la consulta de base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache**: la instantánea en memoria de los datos fuente. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable**: el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solamente* desde su `PivotCache`, nunca directamente desde la fuente de datos.
4. **Celdas**: las `Cells` de la hoja de cálculo en las que la `PivotTable` renderiza sus valores calculados y estilos.

Un concepto particularmente importante es el **caché compartido**. Cuando múltiples tablas dinámicas en un libro de trabajo hacen referencia al mismo rango fuente, comparten *una* instancia de `PivotCache`. Un solo `PivotCache` puede ser referenciado por muchas tablas dinámicas, y actualizar ese caché actualiza cada `PivotTable` dependiente a la vez.

{{% alert color="primary" %}}

`PivotCache.source_type` (enum `PivotTableSourceType`) indica de dónde provienen los datos del caché. A partir de la v26.7, `PivotCache.refresh()` admite solo los tipos de fuente **`Sheet`** y **`Consolidation`**, es decir, datos que residen en rangos de hojas de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no se pueden actualizar a través de la API de caché.

{{% /alert %}}

Debido a esta cadena, hay dos rutas de actualización fundamentales en Aspose.Cells:

- **`PivotCache.refresh()`**: recarga fuente → caché Y recalcula todas las `PivotTable`s dependientes en una sola operación.
- **`PivotTable.calculate_data()`**: recalcula la visualización de una `PivotTable` a partir de los datos ya almacenados en caché, sin volver a la fuente de datos.

Todos los escenarios en este artículo utilizan datos fuente de celdas de hoja de cálculo, por lo que el tipo de fuente es `Sheet` y las operaciones de actualización se comportan como se describe.

## Importaciones requeridas

Todos los ejemplos de Python en este artículo comienzan con las siguientes tres declaraciones de importación porque los tipos de tablas dinámicas viven en el namespace `aspose.cells.pivot`:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Actualizar todas las tablas dinámicas en el libro de trabajo

Cuando necesita asegurarse de que cada caché de tabla dinámica y cada tabla dinámica en el libro de trabajo refleje los últimos datos fuente, la API más sencilla y completa es `Workbook.refresh_all()`. Una sola llamada recorre todo el libro de trabajo, actualizando cada `PivotCache` desde su fuente y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas de documentos donde el rendimiento no es una preocupación.

El siguiente ejemplo crea un libro de trabajo con un rango fuente de Fruta/Año/Cantidad, crea una tabla dinámica, modifica algunos valores fuente y luego utiliza `refresh_all()` para poner todo al día en una sola llamada.

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

# Agregar una tabla dinámica: rango fuente "A1:C9", celda de destino "E3", nombre "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Asignar campos dinámicos: Fruit a Filas, Year a Columnas, Amount a Datos
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modificar varios valores de Amount en los datos fuente para simular cambios
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Actualizar todas las tablas dinámicas / caché dinámico en el libro de trabajo
workbook.refresh_all()

# Guardar el libro de trabajo
workbook.save("output.xlsx")
```

## Actualizar todas las tablas dinámicas en una sola hoja de cálculo

A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica, por ejemplo, cuando se sabe que las tablas dinámicas en otras hojas de cálculo no están relacionadas y no deben tocarse. Para este caso, Aspose.Cells proporciona `Worksheet.refresh_pivot_tables()`, que está limitado a una sola instancia de `Worksheet`.

Esto es más selectivo que `Workbook.refresh_all()`: solo se actualizan las tablas dinámicas en la hoja de cálculo objetivo, dejando intactas las tablas dinámicas en otras hojas de cálculo.

El siguiente ejemplo completa los mismos datos fuente de Fruta/Año/Cantidad, agrega una tabla dinámica en la primera hoja de cálculo, modifica algunos valores fuente y luego actualiza solo las tablas dinámicas en esa hoja de cálculo.

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

Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de lo que realmente cambió: los datos fuente subyacentes, o solo la configuración de vista/diseño de la propia tabla dinámica.

### Datos fuente cambiados — Usar `PivotCache.refresh()`

Si los datos fuente subyacentes han cambiado, el punto de entrada correcto es `pivot_table.pivot_cache.refresh()`. Esta llamada vuelve a leer los datos fuente en el caché y luego recalcula cada `PivotTable` que depende de ese caché.

{{% alert color="primary" %}}

Dado que las tablas dinámicas comparten una sola instancia de `PivotCache`, llamar a `PivotCache.refresh()` recalcula **todas** las tablas dinámicas construidas sobre ese mismo caché, no solo la que usted referencia. Si dos tablas dinámicas comparten el mismo rango fuente, actualizar un caché actualiza ambas.

{{% /alert %}}

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango fuente para demostrar este comportamiento de caché compartido, modifica algunos valores fuente y luego actualiza a través de una referencia de caché.

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

# Agregar la primera tabla dinámica "Pivot1" anclada en la celda E3, rango fuente A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Asignar campos para Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Agregar una SEGUNDA tabla dinámica "Pivot2" anclada en E15 usando el MISMO rango fuente A1:C9
# Tanto Pivot1 como Pivot2 comparten un único PivotCache porque el rango fuente es idéntico.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Asignar los mismos campos para Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Modificar varios valores de celda de Cantidad en los datos fuente para simular un cambio de datos
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Actualizar el PivotCache compartido.
# Debido a que Pivot1 y Pivot2 comparten el mismo PivotCache, esta única llamada
# actualiza AMBAS tablas dinámicas (datos + estilo) desde la fuente actualizada.
pivotTable1.pivot_cache.refresh()

# Guardar el libro de trabajo
workbook.save("output.xlsx")
```

### Solo cambió la vista/diseño — Usar `calculate_data()`

Si los datos fuente *no* han cambiado pero solo se han modificado la configuración de vista o diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente, o se ha activado/desactivado una configuración de actualización al abrir), no es necesario volver a la fuente de datos. El caché ya contiene los datos correctos; solo es necesario recalcular la `PivotTable` renderizada. En este caso, `pivot_table.calculate_data()` es la elección correcta.

Esto evita la obtención innecesaria de la fuente y es significativamente más rápido cuando muchas tablas dinámicas comparten el mismo caché.

El siguiente ejemplo modifica una propiedad no relacionada con la fuente de la tabla dinámica y luego llama a `calculate_data()` para volver a renderizarla desde el caché existente.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Escribir fila de encabezado Fruit / Year / Amount
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

# Asignar campos: Fruit a Fila, Year a Columna, Amount a Datos
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Modificar una propiedad de vista/diseño — este es un cambio solo de presentación,
# por lo que NO requiere volver a leer los datos de origen a través de PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# ¡CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) desde los
# datos ya almacenados en el PivotCache. Debido a que los datos de origen no cambiaron,
# no se realiza un viaje de ida y vuelta al origen — solo los valores en caché se recalculan
# en las celdas de la hoja de cálculo.
pivot_table.calculate_data()

# Guardar el libro de trabajo en disco
workbook.save("output.xlsx")
```

## Obtener todas las tablas dinámicas que comparten el mismo PivotCache

Un libro de trabajo a menudo contiene muchas tablas dinámicas que se asientan sobre un caché compartido. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto del caché compartido, use `PivotCache.get_pivot_tables()`. Este método devuelve la colección de todas las `PivotTable` que dependen del caché dado.

Esta es también la forma más directa de confirmar que dos tablas dinámicas realmente comparten la misma instancia de `PivotCache`: puede comparar referencias de caché o simplemente iterar la colección devuelta por `get_pivot_tables()` y observar qué tablas dinámicas aparecen en ella.

El siguiente ejemplo crea dos tablas dinámicas sobre el mismo rango fuente, verifica que comparten la misma instancia de caché y luego enumera las tablas dinámicas del caché.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

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

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## Migración desde el método obsoleto `PivotTable.refresh_data()`

Antes de Aspose.Cells for Python via .NET v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.refresh_data()` en cada tabla dinámica individualmente. A partir de la v26.7, ese método está marcado como **obsoleto** y debe reemplazarse por las APIs conscientes del caché descritas anteriormente.

Hay dos razones por las que el enfoque por tabla `refresh_data()` es problemático en libros de trabajo del mundo real:

- Recupera datos de la fuente *cada* vez que se llama, incluso cuando la fuente no ha cambiado.
- Cada llamada actualiza todo el caché compartido. Cuando muchas tablas dinámicas comparten un caché, llamar repetidamente a `refresh_data()` por tabla dinámica hace que el mismo caché se recupere una y otra vez, lo cual es muy lento.

Los reemplazos recomendados son:

- **Actualizar TODAS las tablas dinámicas en el libro de trabajo** → use `workbook.refresh_all();`
- **Actualizar ALGUNAS de ellas** → use `pivot_table.pivot_cache.refresh();` para un caché. Debido a que el caché es compartido, esta sola llamada actualiza cada tabla dinámica construida sobre ese caché. Otras tablas dinámicas que se asientan sobre un caché ya actualizado se pueden omitir de forma segura.
- **Solo cambió la vista/diseño de la tabla dinámica** → use `pivot_table.calculate_data();` para volver a renderizar desde el caché existente sin ningún viaje de ida y vuelta a la fuente.

El siguiente ejemplo demuestra el nuevo patrón eficiente para libros de trabajo con múltiples tablas dinámicas que comparten un solo caché.

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
# Tanto Pivot1 como Pivot2 comparten UN PivotCache subyacente.
# Este es exactamente el escenario donde el método heredado por tabla RefreshData()
# se vuelve ineficiente: al actualizar una tabla se vuelve a obtener todo el
# caché compartido, por lo que actualizar N tablas realiza la misma costosa obtención N veces.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Modificar varios valores de Cantidad en los datos de origen ---
sheet.cells["C2"].put_value(5000)   # Uva  2020
sheet.cells["C5"].put_value(7500)   # Cereza 2020
sheet.cells["C9"].put_value(9500)   # Cereza 2021

# --- Patrón OBSOLETO (pre-26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # vuelve a obtener datos del origen, actualiza todo el caché
# pivot_table2.refresh_data();  # vuelve a obtener datos OTRA VEZ — ¡el caché ya está actualizado!
# Cada llamada reconstruye el caché compartido, por lo que N tablas = N obtenciones redundantes.

# --- Patrón NUEVO v26.7+: actualizar el caché UNA VEZ y luego volver a renderizar según sea necesario ---
# Una llamada a PivotCache.Refresh() extrae los valores modificados al caché compartido
# Y recalcula la visualización de TODAS las tablas dinámicas que lo referencian.
# Dado que Pivot1 y Pivot2 comparten un PivotCache, esta única llamada actualiza
# ambas tablas — no se requiere un segundo viaje de ida y vuelta al origen.
pivot_table1.pivot_cache.refresh()

# CalculateData() solo vuelve a renderizar la visualización de una tabla dinámica (datos + estilo)
# a partir de los datos ya almacenados en el caché — NO toca el origen.
# La llamamos en Pivot2 aquí puramente para demostrar la API: después de que el caché
# se ha actualizado una vez, cualquier tabla dependiente se puede volver a renderizar sin
# volver al origen. Use CalculateData() por sí solo cuando solo la
# configuración de vista/diseño de la tabla dinámica haya cambiado y el caché esté actualizado.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## ¿Qué API de actualización debo usar?

La siguiente tabla resume las APIs de actualización disponibles y cuándo elegir cada una.

| Objetivo | API recomendada | Notas |
|------|-----------------|-------|
| Actualizar todo en el libro de trabajo | `Workbook.refresh_all()` | Una sola llamada; cubre todos los cachés y tablas. |
| Actualizar solo las tablas dinámicas en una sola hoja | `Worksheet.refresh_pivot_tables()` | Limitado a una hoja de cálculo. |
| Los datos fuente cambiaron para un caché | `pivot_table.pivot_cache.refresh()` | Actualiza TODAS las tablas dinámicas en ese caché compartido. |
| Solo cambió la configuración de vista/diseño | `pivot_table.calculate_data()` | Omite el viaje innecesario a la fuente. |
| Listar todas las tablas dinámicas en un caché compartido | `pivot_cache.get_pivot_tables()` | Use para enumerar antes de la actualización masiva. |

En la práctica, prefiera las APIs basadas en caché sobre el método obsoleto `refresh_data()` por tabla. Son conscientes de los cachés compartidos, evitan obtenciones redundantes de la fuente y le permiten elegir el alcance más pequeño que satisface su requisito de actualización.

{{< app/cells/assistant language="python" >}}