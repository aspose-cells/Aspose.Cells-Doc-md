---
title: Actualizar tablas dinámicas y cachés dinámicos en Aspose.Cells for Python via .NET
description: Aprenda a actualizar tablas dinámicas en Aspose.Cells for Python via .NET usando la API de actualización de tablas dinámicas v26.7+. Este artículo cubre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData y GetPivotTables con ejemplos prácticos de código.
linktitle: Actualizar tablas dinámicas
keywords: Aspose.Cells, Python via .NET, tabla dinámica, actualizar, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /es/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells proporciona una API de actualización por capas que le permite recargar datos de tablas dinámicas en cuatro alcances diferentes, desde todo el libro hasta una sola tabla dinámica. A partir de **Aspose.Cells for Python via .NET v26.7**, el método heredado `PivotTable.refresh_data()` está marcado como obsoleto y debe sustituirse por las API más eficientes y conscientes de la caché descritas en este artículo.
{{% /alert %}}

## Introducción
Actualizar una tabla dinámica rara vez es una operación única. Tras bambalinas, Aspose.Cells mantiene una cadena de datos en capas que conecta sus datos de origen originales con los valores representados que ve en la hoja de cálculo. Comprender esta cadena es la clave para elegir la API de actualización adecuada para cualquier situación.
La cadena de datos de cuatro capas es:
1. **Fuente de datos** — los rangos de la hoja de cálculo originales, la consulta a la base de datos o el rango de consolidación donde residen los valores sin procesar.
2. **PivotCache** — la instantánea en memoria de los datos de origen. Cada tabla dinámica se construye sobre un `PivotCache`; aquí es donde se recopilan y agregan todos los datos.
3. **PivotTable** — el objeto de vista que define los campos de fila, columna, valor y filtro. Una `PivotTable` lee *solo* desde su `PivotCache`, nunca directamente desde la fuente de datos.
4. **Celdas** — las `Cells` de la hoja de cálculo en las que la `PivotTable` representa sus valores calculados y estilos.

{{% alert color="primary" %}}
`PivotCache.source_type` (enumeración `PivotTableSourceType`) indica de dónde provienen los datos de la caché. A partir de v26.7, `PivotCache.refresh()` solo admite los tipos de origen **`Sheet`** y **`Consolidation`**, es decir, datos que residen en rangos de la hoja de cálculo. Las fuentes externas (bases de datos, conexiones externas, etc.) aún no se pueden actualizar mediante la API de caché.
{{% /alert %}}

Debido a esta cadena, hay dos rutas de actualización fundamentales en Aspose.Cells:
- **`PivotTable.calculate_data()`** — recalcula la visualización de una `PivotTable` a partir de los datos ya almacenados en caché, sin volver a la fuente de datos.
Todos los escenarios de este artículo utilizan datos de origen de celdas de la hoja de cálculo, por lo que el tipo de origen es `Sheet` y las operaciones de actualización se comportan como se describe.

## Inicio rápido
Si solo necesita el código más breve posible que actualice cada tabla dinámica del libro, una sola llamada es suficiente:

```python
import aspose.cells as ac
# Crear un nuevo libro de trabajo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Escribir la fila de encabezado en las celdas A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Escribir filas de datos en las celdas A2:C9 (8 filas de datos de frutas en 2020 y 2021)
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

Todo lo demás en este artículo explica cuándo elegir una API más específica en su lugar.

## Importaciones requeridas
Todos los ejemplos de Python en este artículo comienzan con las siguientes tres sentencias de importación porque los tipos de tablas dinámicas se encuentran en el espacio de nombres `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Actualizar todas las tablas dinámicas del libro
Cuando necesite asegurarse de que cada caché dinámico y cada tabla dinámica del libro reflejen los últimos datos de origen, la API más sencilla y completa es `Workbook.refresh_all()`. Una sola llamada recorre todo el libro, actualizando cada `PivotCache` desde su fuente y luego recalculando cada `PivotTable` dependiente. Este es el enfoque recomendado para actualizaciones generales y completas del documento donde el rendimiento no es un problema.
El siguiente ejemplo crea un libro con un rango de origen Fruta/Año/Importe, crea una tabla dinámica, modifica algunos valores de origen y luego utiliza `refresh_all()` para actualizar todo en una sola llamada.

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

## Actualizar todas las tablas dinámicas en una sola hoja de cálculo
A veces solo necesita actualizar las tablas dinámicas que se encuentran en una hoja de cálculo específica; por ejemplo, cuando se sabe que las tablas dinámicas de otras hojas no están relacionadas y no deben modificarse. Para este caso, Aspose.Cells proporciona `Worksheet.refresh_pivot_tables()`, que está limitada a una sola instancia de `Worksheet`.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Escribir fila de encabezado Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Escribir 8 filas de datos (filas 2-9, ajustándose al rango fuente A1:C9)
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
# Agregar una tabla dinámica llamada "Pivot1" colocada en la celda de destino E3, con origen en A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Asignar campos: Fruit a Fila, Year a Columna, Amount a Datos
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modificar una propiedad de vista/diseño — este es un cambio solo de presentación,
# por lo que NO requiere volver a leer los datos fuente a través de PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False
# CalculateData() vuelve a renderizar la visualización de ESTA tabla dinámica (datos + estilo) desde los
# datos ya almacenados en el PivotCache. Debido a que los datos fuente no cambiaron,
# no se realiza un viaje de ida y vuelta a la fuente — solo los valores en caché se recalculan
# en las celdas de la hoja de cálculo.
pivot_table.calculate_data()
# Guardar el libro de trabajo en disco
workbook.save("output.xlsx")
```

## Actualizar una sola tabla dinámica
Cuando desea un control detallado sobre una sola tabla dinámica, la API basada en caché le ofrece dos opciones. La elección entre ellas depende de qué haya cambiado realmente: los datos de origen subyacentes, o solo la configuración de vista/diseño de la propia tabla dinámica.

### Cambiaron los datos de origen — Use `PivotCache.refresh()`
Si los datos de origen subyacentes han cambiado, el punto de entrada correcto es `pivot_table.pivot_cache.refresh()`. Esta llamada vuelve a leer los datos de origen en la caché y luego recalcula cada `PivotTable` que depende de esa caché.

### Solo cambió la vista/diseño — Use `calculate_data()`
Si los datos de origen *no* han cambiado, pero solo se han modificado la vista o la configuración del diseño de la tabla dinámica (por ejemplo, se ha movido un campo a un área diferente, o se ha activado/desactivado una opción de actualización al abrir), no es necesario volver a la fuente de datos. La caché ya contiene los datos correctos; solo es necesario recalcular la `PivotTable` renderizada. En este caso, `pivot_table.calculate_data()` es la elección correcta.
El siguiente ejemplo modifica una propiedad que no es de origen de la tabla dinámica y luego llama a `calculate_data()` para volver a renderizarla desde la caché existente.
Un libro a menudo contiene muchas tablas dinámicas que se asientan sobre una caché compartida. Para enumerarlas, por ejemplo, antes de realizar una actualización por lotes o para diagnosticar el impacto de la caché compartida, use `PivotCache.get_pivot_tables()`. Este método devuelve la colección de cada `PivotTable` que depende de la caché dada.

## Migración desde el obsoleto `PivotTable.refresh_data()`
Antes de Aspose.Cells for Python via .NET v26.7, la forma estándar de actualizar una tabla dinámica era llamar a `PivotTable.refresh_data()` en cada tabla dinámica individualmente. A partir de v26.7, ese método está marcado como **obsoleto** y debe sustituirse por las API conscientes de la caché descritas anteriormente.
Hay dos razones por las que el enfoque `refresh_data()` por tabla es problemático en libros del mundo real:
- Recupera datos de la fuente *cada* vez que se llama, incluso cuando la fuente no ha cambiado.
Los reemplazos recomendados son:
El siguiente ejemplo muestra el nuevo patrón eficiente para libros con varias tablas dinámicas que comparten una sola caché.

## ¿Qué API de actualización debo usar?
La tabla siguiente resume las API de actualización disponibles y cuándo elegir cada una.
| Objetivo | API recomendada | Notas |
|----------|-----------------|-------|
| Actualizar todo en el libro | `Workbook.refresh_all()` | Una llamada; cubre todas las cachés y tablas. |
| Actualizar solo las tablas dinámicas de una sola hoja | `Worksheet.refresh_pivot_tables()` | Limitada a una hoja de cálculo. |
| Cambiaron los datos de origen de una caché | `pivot_table.pivot_cache.refresh()` | Actualiza TODAS las tablas dinámicas de esa caché compartida. |
| Solo cambió la configuración de vista/diseño | `pivot_table.calculate_data()` | Evita el viaje innecesario a la fuente. |
| Listar todas las tablas dinámicas de una caché compartida | `pivot_cache.get_pivot_tables()` | Úselo para enumerar antes de una actualización masiva. |
En la práctica, prefiera las API basadas en caché sobre el obsoleto `refresh_data()` por tabla. Son conscientes de las cachés compartidas, evitan lecturas redundantes de la fuente y le permiten elegir el alcance más pequeño que satisface su requisito de actualización.

## Errores comunes
- **Olvidar actualizar antes de guardar.** Una tabla dinámica solo escribe sus valores renderizados en la hoja de cálculo cuando se actualiza su cadena de datos. Si modifica celdas de origen, llame a `PivotCache.Refresh()` (o `Workbook.RefreshAll()`) antes de `Workbook.save()`, de lo contrario el archivo guardado aún contendrá los valores agregados antiguos.
- **Llamar al obsoleto `RefreshData()` por tabla.** En v26.7, `PivotTable.RefreshData()` está marcado como obsoleto y vuelve a obtener los datos de la fuente en cada llamada. Con varias tablas dinámicas que comparten una caché, esto significa N lecturas redundantes de la fuente. Sustitúyalo por una sola llamada a `PivotCache.Refresh()` seguida de `CalculateData()` por tabla.
- **Actualizar cuando solo cambió el diseño.** Si solo cambió la vista de una tabla dinámica (orden de columnas, `ConsolidationFunction`, etc.) sin tocar los datos de origen, `PivotCache.Refresh()` es innecesario y lento. Llame a `pivotTable.CalculateData()` para volver a renderizar desde la caché existente.
- **Fuente externa no admitida por `PivotCache.Refresh()`.** Si la fuente de la tabla dinámica proviene de una conexión externa (base de datos, cubo OLAP, etc.), `PivotCache.Refresh()` no puede actualizarla en v26.7; actualmente solo admite los tipos de origen `Sheet` y `Consolidation`. Para fuentes externas, vuelva a abrir el libro o reconstruya la caché desde la fuente.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python-net" >}}