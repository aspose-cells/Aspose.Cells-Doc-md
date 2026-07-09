---
title: Convertir minigráficos a imagen y HTML en Aspose.Cells for Python via .NET
linktitle: Convert Sparkline to Image and HTML
description: Aprenda a renderizar minigráficos de Aspose.Cells como imágenes independientes para incrustarlas en celdas y exportar hojas de cálculo con minigráficos a HTML usando HtmlSaveOptions en Python via .NET.
keywords: Aspose.Cells, Python via .NET, minigráfico, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, renderizar minigráfico, convertir minigráfico a imagen, exportar minigráfico a HTML
type: docs
weight: 120
url: /es/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son gráficos en miniatura colocados dentro de celdas de la hoja de cálculo. Aspose.Cells le permite extraer cada minigráfico como una imagen independiente (para incrustarla en otra celda o en un informe externo) y también exportar la hoja de cálculo completa con minigráficos a HTML para su distribución en el navegador. La propiedad `cell.embedded_image` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y versiones posteriores**.
{{% /alert %}}

## **Introducción**

Los minigráficos son una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Mientras que los usuarios de Excel los ven en su lugar, muchos escenarios del mundo real requieren que un minigráfico salga de la celda, por ejemplo, para ser incrustado en una celda diferente como una imagen estática, adjunto a un correo electrónico automatizado o renderizado como parte de un informe HTML publicado en la web.

Aspose.Cells admite ambas operaciones. El método `sparkline.to_image` renderiza un minigráfico individual a un flujo, y los bytes resultantes se pueden asignar a `cell.embedded_image` para que la imagen se almacene dentro de una sola celda del libro de trabajo. Por separado, `HtmlSaveOptions` le permite convertir el libro de trabajo completo, con todos los minigráficos, en un archivo HTML autónomo. Este artículo recorre ambos flujos de trabajo de principio a fin.

## **Flujo de trabajo 1 — Renderizar minigráficos a imágenes e incrustarlos en celdas**

En este flujo de trabajo, construirá una hoja de cálculo que contiene un pequeño rango de valores de origen, adjuntará tres grupos de minigráficos diferentes (Línea, Columna y Apilado/Ganancia-Pérdida) a ese rango, renderizará cada grupo como PNG y escribirá esos bytes PNG en celdas adyacentes como imágenes incrustadas. El resultado final es un único archivo `.xlsx` que contiene tanto los minigráficos activos como sus contrapartes de imágenes renderizadas.

### **Instrucciones paso a paso**

1. Defina un directorio de trabajo y asegúrese de que exista en disco.
2. Cree un nuevo `Workbook` y obtenga una referencia a la primera `Worksheet`.
3. Rellene las celdas `A1` a `E1` con cinco valores numéricos de muestra (por ejemplo, ventas diarias o lecturas de temperatura).
4. Agregue tres objetos `SparklineGroup` a la hoja de cálculo llamando a `worksheet.sparkline_groups.add(...)`:
   - Un grupo `SparklineType.LINE` anclado en `F1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.COLUMN` anclado en `G1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.STACKED` (ganancia/pérdida) anclado en `H1`, con rango de datos `A1:E1`.
5. Construya una instancia de `ImageOrPrintOptions` y establezca su `image_type` en `ImageType.PNG` para que cada minigráfico se renderice como un PNG transparente.
6. Para cada uno de los tres grupos, renderice su único minigráfico usando `group.sparklines[0].to_image(memory_stream, image_options)`, convierta el flujo `BytesIO` en un objeto `bytes` y asigne el arreglo a `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` y `worksheet.cells["H2"].embedded_image` respectivamente.
7. Guarde el libro de trabajo como `output_with_sparklines.xlsx`.

```python
import aspose.cells as ac

# Crear un nuevo libro de trabajo y acceder a la primera hoja de cálculo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Rellenar datos de muestra en las celdas A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Agregar un grupo de minigráficos de líneas anclado en F1 (columna 5, fila 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# Agregar un grupo de minigráficos de columnas anclado en G1 (columna 6, fila 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilados) anclado en H1 (columna 7, fila 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# Configurar las opciones de imagen para la salida PNG
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Convertir el minigráfico de líneas a imagen e incrustarlo en la celda F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Convertir el minigráfico de columnas a imagen e incrustarlo en la celda G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Convertir el minigráfico de Ganancia/Pérdida a imagen e incrustarlo en la celda H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Guardar el libro de trabajo en disco
workbook.save("output_with_sparklines.xlsx")
```

El código anterior produce un libro de trabajo donde cada representación visual de un minigráfico se duplica en dos formas: el minigráfico nativo y activo anclado en la fila 1, y una imagen PNG estática incrustada directamente en una celda vecina en la fila 2. Dado que las imágenes viven dentro del propio archivo, el libro de trabajo sigue siendo un único artefacto autónomo que se puede enviar por correo electrónico o archivar sin romper las referencias de imágenes incrustadas. Renderice cada grupo de minigráficos como PNG, convierta el flujo `BytesIO` en un objeto `bytes` y asigne los bytes a la propiedad `embedded_image` de la celda de destino; la asignación es lo que hace que la imagen forme parte del contenido almacenado de la celda.

{{% alert color="primary" %}}
Dado que cada grupo de minigráficos está anclado a una sola celda, puede acceder a él mediante el indizador `group.sparklines[0]` en lugar de enumerar con un bucle `for`. Esto mantiene el código de renderización corto y coincide con el patrón típico de "un minigráfico por celda de anclaje". Almacenar los bytes de la imagen mediante `cell.embedded_image` requiere Aspose.Cells 26.5 o versiones posteriores.
{{% /alert %}}

## **Flujo de trabajo 2 — Exportar la hoja de cálculo con minigráficos a HTML**

Una vez que el libro de trabajo contiene minigráficos activos (y opcionalmente contrapartes de imágenes incrustadas), la hoja de cálculo completa se puede publicar en la web guardándola como HTML. La clase `HtmlSaveOptions` expone los controles que necesita para gestionar esta exportación; en este flujo de trabajo, reutilizará el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 y lo convertirá en un documento HTML limpio y de una sola página.

### **Instrucciones paso a paso**

1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 esté disponible en disco en su directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y establezca su propiedad `export_active_worksheet_only` en `True` para que el archivo HTML resultante contenga solo la hoja de cálculo activa en lugar del libro de trabajo completo.
4. Llame a `workbook.save("sparklines.html", html_options)` para escribir la salida HTML en disco.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

El código anterior toma el libro de trabajo con minigráficos del Flujo de trabajo 1 y lo convierte en un archivo HTML portátil. Los minigráficos se conservan como renderizaciones SVG o PNG en línea dentro del HTML generado, según el modo de exportación, por lo que los usuarios finales pueden ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `export_active_worksheet_only` en `True`, evita publicar accidentalmente hojas ocultas o datos auxiliares; solo se exporta la hoja de cálculo actualmente visible para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar la salida, como `export_hidden_worksheet`, `export_images_as_base64` y `encoding`. Ajústelas según sea necesario para su destino de implementación.
{{% /alert %}}

## **Resumen de la API**

Los flujos de trabajo anteriores dependen de un pequeño conjunto de APIs de Aspose.Cells que trabajan juntas.

- `SparklineGroup` y el descriptor de acceso de colección `worksheet.sparkline_groups` se utilizan para declarar el tipo (Línea, Columna, Apilado), el rango de datos y la celda de anclaje para cada grupo de minigráficos. En este artículo, cada grupo está anclado a una sola celda, por lo que se accede al grupo mediante `worksheet.sparkline_groups[i]`.
- `Sparkline` y el indizador `group.sparklines[0]` devuelven el minigráfico individual dentro de un grupo. Dado que cada grupo en el ejemplo contiene exactamente un minigráfico, no se requiere un bucle `for`.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` es el método de renderización que escribe una imagen del minigráfico en un flujo proporcionado. El método devuelve `None`; lea los bytes del flujo después de la llamada.
- `cell.embedded_image` es una propiedad `bytes` que almacena una imagen dentro de una sola celda. Está disponible en **Aspose.Cells 26.5 y versiones posteriores** y es la forma recomendada de devolver un minigráfico renderizado por `to_image` al mismo libro de trabajo.
- `html_save_options.export_active_worksheet_only` (un `bool`) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas en `HtmlSaveOptions` al generar informes de una sola página.
- `image_or_print_options.image_type` se encuentra en el espacio de nombres `aspose.cells.drawing` y selecciona el formato de imagen (por ejemplo, `ImageType.PNG`) utilizado al renderizar con `to_image` y al imprimir hojas de cálculo como imágenes.

## **Artículos relacionados**

- [Minigráficos en Aspose.Cells para Python via .NET](/cells/es/python-net/sparkline/)
- [Insertar una imagen en una celda](/cells/es/python-net/inserting-an-image-into-a-cell/)
- [Renderización de matriz de una sola celda de SmartMarker | Aspose.Cells para Python via .NET](/cells/es/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}