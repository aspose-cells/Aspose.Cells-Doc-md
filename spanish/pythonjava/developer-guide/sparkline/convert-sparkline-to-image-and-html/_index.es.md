---
title: Convertir Sparkline a Imagen y HTML en Aspose.Cells for Python via Java
linktitle: Convert Sparkline to Image and HTML
description: Aprenda a renderizar minigráficos de Aspose.Cells como imágenes independientes para incrustarlos en celdas y exportar hojas de cálculo con minigráficos a HTML usando HtmlSaveOptions.
keywords: Aspose.Cells, Python via Java, minigráfico, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, renderizar minigráfico, convertir minigráfico a imagen, exportar minigráfico a HTML
type: docs
weight: 120
url: /es/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son gráficos miniatura colocados dentro de celdas de hojas de cálculo. Aspose.Cells le permite extraer cada minigráfico como una imagen independiente (para incrustarlo en otra celda o en un informe externo) y también exportar la hoja de cálculo completa con minigráficos a HTML para su distribución en navegadores. La propiedad `Cell.embedded_image` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y posteriores**.
{{% /alert %}}

## **Introducción**

Los minigráficos son una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Mientras que los usuarios de Excel los ven en su lugar, muchos escenarios del mundo real requieren que un minigráfico salga de la celda — por ejemplo, para incrustarse en una celda diferente como una imagen estática, adjuntarse a un correo electrónico automatizado o renderizarse como parte de un informe HTML publicado en la web.

Aspose.Cells admite ambas operaciones. El método `Sparkline.to_image` renderiza un minigráfico individual a un flujo, y los bytes resultantes pueden asignarse a `Cell.embedded_image` para que la imagen quede almacenada dentro de una sola celda del libro. Por separado, `HtmlSaveOptions` le permite convertir el libro completo — minigráficos incluidos — en un archivo HTML autónomo. Este artículo recorre ambos flujos de trabajo de principio a fin.

## **Flujo de Trabajo 1 — Renderizar Minigráficos a Imágenes e Incrustarlos en Celdas**

En este flujo de trabajo, creará una hoja de cálculo que contiene un pequeño rango de valores fuente, adjuntará tres grupos de minigráficos diferentes (Línea, Columna y Apilado/Ganancia-Pérdida) a ese rango, renderizará cada grupo como PNG y escribirá esos bytes PNG en celdas adyacentes como imágenes incrustadas. El resultado final es un único archivo `.xlsx` que contiene tanto los minigráficos en vivo como sus contrapartes de imagen renderizadas.

### **Instrucciones Paso a Paso**

1. Defina un directorio de trabajo y asegúrese de que exista en disco.
2. Cree un nuevo `Workbook` y obtenga una referencia a la primera `Worksheet`.
3. Rellene las celdas `A1` a `E1` con cinco valores numéricos de muestra (por ejemplo, ventas diarias o lecturas de temperatura).
4. Agregue tres objetos `SparklineGroup` a la hoja de cálculo llamando a `worksheet.sparkline_groups.add(...)`:
   - Un grupo `SparklineType.LINE` anclado en `F1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.COLUMN` anclado en `G1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.STACKED` (ganancia/pérdida) anclado en `H1`, con rango de datos `A1:E1`.
5. Construya una instancia de `ImageOrPrintOptions` y establezca su `image_type` en `ImageType.PNG` para que cada minigráfico se renderice como un PNG transparente.
6. Para cada uno de los tres grupos, renderice su único minigráfico usando `group.sparklines[0].to_image(byte_array_output_stream, image_options)`, convierta el `ByteArrayOutputStream` a un `byte[]` (o lea su `to_byte_array()` en `bytes` de Python), y asigne los bytes a `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` y `worksheet.cells["H2"].embedded_image` respectivamente.
7. Guarde el libro como `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# Crear un nuevo libro de trabajo y acceder a la primera hoja de cálculo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Poblar datos de muestra en las celdas A1:E1
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Agregar un grupo de minigráficos de Línea anclado en F1 (columna 5, fila 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# Agregar un grupo de minigráficos de Columna anclado en G1 (columna 6, fila 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) anclado en H1 (columna 7, fila 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# Configurar opciones de imagen para salida PNG
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# Convertir el minigráfico de Línea a imagen e incrustarlo en la celda F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# Convertir el minigráfico de Columna a imagen e incrustarlo en la celda G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# Convertir el minigráfico de Ganancia/Pérdida a imagen e incrustarlo en la celda H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# Guardar el libro de trabajo en disco
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

El código anterior produce un libro donde cada representación visual de un minigráfico se duplica en dos formas: el minigráfico nativo en vivo anclado en la fila 1, y una imagen PNG estática incrustada directamente en una celda vecina en la fila 2. Debido a que las imágenes viven dentro del archivo mismo, el libro sigue siendo un único artefacto autónomo que puede enviarse por correo electrónico o archivarse sin romper las referencias de las imágenes incrustadas. Renderice cada grupo de minigráficos como PNG, convierta el `ByteArrayOutputStream` a un `byte[]` (o use `to_byte_array()` para obtener un objeto `bytes` de Python), y asigne el arreglo a la propiedad `embedded_image` de la celda destino — la asignación es lo que hace que la imagen forme parte del contenido almacenado de la celda.

{{% alert color="primary" %}}
Debido a que cada grupo de minigráficos está anclado a una sola celda, puede accederlo mediante el indizador `group.sparklines[0]` en lugar de enumerar con un bucle `for`. Esto mantiene el código de renderizado corto y coincide con el patrón típico de "un minigráfico por celda ancla". Almacenar los bytes de la imagen a través de `Cell.embedded_image` requiere Aspose.Cells 26.5 o posterior.
{{% /alert %}}

## **Flujo de Trabajo 2 — Exportar la Hoja de Cálculo con Minigráficos a HTML**

Una vez que el libro contiene minigráficos en vivo (y opcionalmente contrapartes de imágenes incrustadas), toda la hoja de cálculo puede publicarse en la web guardándola como HTML. La clase `HtmlSaveOptions` expone los controles que necesita para gestionar esta exportación; en este flujo de trabajo reutilizará el archivo `output_with_sparklines.xlsx` producido por el Flujo de Trabajo 1 y lo convertirá en un documento HTML limpio de una sola página.

### **Instrucciones Paso a Paso**

1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido por el Flujo de Trabajo 1 esté disponible en disco en su directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y establezca su propiedad `export_active_worksheet_only` en `True` para que el archivo HTML resultante contenga solo la hoja de cálculo activa en lugar del libro completo.
4. Llame a `workbook.save("sparklines.html", html_options)` para escribir la salida HTML en disco.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

El código anterior toma el libro con minigráficos del Flujo de Trabajo 1 y lo convierte en un archivo HTML portátil. Los minigráficos se conservan como renderizados SVG o PNG en línea dentro del HTML generado, dependiendo del modo de exportación, por lo que los usuarios finales pueden ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `export_active_worksheet_only` en `True`, evita publicar accidentalmente hojas ocultas o datos auxiliares — solo se exporta la hoja de cálculo actualmente visible para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar la salida, como `export_hidden_worksheet`, `export_images_as_base64` y `encoding`. Ajústelas según sea necesario para su objetivo de despliegue.
{{% /alert %}}

## **Resumen de la API**

Los flujos de trabajo anteriores se basan en un pequeño conjunto de APIs de Aspose.Cells que trabajan juntas.

- `SparklineGroup` y el descriptor de acceso de colección `worksheet.sparkline_groups` se utilizan para declarar el tipo (Línea, Columna, Apilado), el rango de datos y la celda ancla para cada grupo de minigráficos. En este artículo, cada grupo está anclado a una sola celda, por lo que se accede al grupo mediante `worksheet.sparkline_groups[i]`.
- `Sparkline` y el indizador `group.sparklines[0]` devuelven el minigráfico individual dentro de un grupo. Dado que cada grupo en el ejemplo contiene exactamente un minigráfico, no se requiere ningún bucle `for`.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` es el método de renderizado que escribe una imagen del minigráfico en un `OutputStream` proporcionado (como un `ByteArrayOutputStream`). El método devuelve `void`; lea los bytes del flujo después de la llamada.
- `Cell.embedded_image` es una propiedad `byte[]` que almacena una imagen dentro de una sola celda. Está disponible en **Aspose.Cells 26.5 y posteriores** y es la forma recomendada de regresar un minigráfico renderizado por `to_image` al mismo libro.
- `HtmlSaveOptions.export_active_worksheet_only` (un `bool`) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas en `HtmlSaveOptions` al generar informes de una sola página.
- `ImageOrPrintOptions.image_type` reside en el namespace `com.aspose.cells.drawing` y selecciona el formato de imagen (por ejemplo, `ImageType.PNG`) utilizado al renderizar con `to_image` y al imprimir hojas de cálculo como imágenes.

## **Artículos Relacionados**

- [Minigráficos en Aspose.Cells for Python via Java](/cells/es/python-java/sparkline/)
- [Insertar una Imagen en una Celda](/cells/es/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}