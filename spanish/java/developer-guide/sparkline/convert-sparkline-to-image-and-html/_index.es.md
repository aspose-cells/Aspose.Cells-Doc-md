---
title: Convertir minigráficos a imagen y HTML en Aspose.Cells for Java
linktitle: Convert Sparkline to Image and HTML
description: Aprenda cómo renderizar minigráficos de Aspose.Cells como imágenes independientes para incrustar en celdas y exportar hojas de cálculo con minigráficos a HTML usando HtmlSaveOptions.
keywords: Aspose.Cells, Java, minigráfico, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizar minigráfico, convertir minigráfico a imagen, exportar minigráfico a HTML
type: docs
weight: 120
url: /es/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son gráficos en miniatura colocados dentro de las celdas de la hoja de cálculo. Aspose.Cells le permite extraer cada minigráfico como una imagen independiente (para incrustarla en otra celda o en un informe externo) y también exportar la hoja de cálculo completa con minigráficos a HTML para su distribución basada en navegador. La propiedad `Cell.EmbeddedImage` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y posteriores**.
{{% /alert %}}

## **Introducción**

Los minigráficos son una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Mientras que los usuarios de Excel los ven en su lugar, muchos escenarios del mundo real requieren que un minigráfico salga de la celda — por ejemplo, para ser incrustado en una celda diferente como una imagen estática, adjunto a un correo electrónico automatizado, o renderizado como parte de un informe HTML publicado en la web.

Aspose.Cells admite ambas operaciones. El método `Sparkline.toImage` renderiza un minigráfico individual a un flujo, y los bytes resultantes se pueden asignar a `Cell.EmbeddedImage` (mediante `setEmbeddedImage`) para que la imagen se almacene dentro de una sola celda del libro. Por separado, `HtmlSaveOptions` le permite convertir el libro completo — con todos los minigráficos — en un archivo HTML autónomo. Este artículo recorre ambos flujos de trabajo de principio a fin.

## **Flujo de trabajo 1 — Renderizar minigráficos a imágenes e incrustarlos en celdas**

En este flujo de trabajo, creará una hoja de cálculo que contiene un pequeño rango de valores fuente, adjuntará tres grupos de minigráficos diferentes (Línea, Columna y Apilado/Ganancia-Pérdida) a ese rango, renderizará cada grupo como un PNG, y escribirá esos bytes PNG en celdas adyacentes como imágenes incrustadas. El resultado final es un único archivo `.xlsx` que contiene tanto los minigráficos en vivo como sus contrapartes de imagen renderizadas.

### **Instrucciones paso a paso**

1. Defina un directorio de trabajo y asegúrese de que exista en disco.
2. Cree un nuevo `Workbook` y obtenga una referencia a la primera `Worksheet`.
3. Rellene las celdas `A1` a `E1` con cinco valores numéricos de muestra (por ejemplo, ventas diarias o lecturas de temperatura).
4. Agregue tres objetos `SparklineGroup` a la hoja de cálculo llamando a `worksheet.getSparklineGroups().add(...)`:
   - Un grupo `SparklineType.LINE` anclado en `F1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.COLUMN` anclado en `G1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.STACKED` (ganancia/pérdida) anclado en `H1`, con rango de datos `A1:E1`.
5. Construya una instancia de `ImageOrPrintOptions` y llame a `setImageType(ImageType.PNG)` para que cada minigráfico se renderice como un PNG transparente.
6. Para cada uno de los tres grupos, renderice su único minigráfico usando `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)`, convierta el `ByteArrayOutputStream` a un `byte[]`, y asigne el arreglo mediante `worksheet.getCells().get("F2").setEmbeddedImage(...)`, `worksheet.getCells().get("G2").setEmbeddedImage(...)`, y `worksheet.getCells().get("H2").setEmbeddedImage(...)` respectivamente.
7. Llame a `workbook.save("output_with_sparklines.xlsx")` para guardar el libro en disco.

```java
import com.aspose.cells.*;
import java.io.*;

// Crear un nuevo libro y acceder a la primera hoja de cálculo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Poblar datos de muestra en las celdas A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Agregar un grupo de minigráficos de línea anclado en F1 (columna 5, fila 0)
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// Agregar un grupo de minigráficos de columna anclado en G1 (columna 6, fila 0)
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) anclado en H1 (columna 7, fila 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// Configurar opciones de imagen para salida PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// Convertir el minigráfico de línea a imagen e incrustarlo en la celda F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Convertir el minigráfico de columna a imagen e incrustarlo en la celda G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Convertir el minigráfico de Ganancia/Pérdida a imagen e incrustarlo en la celda H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Guardar el libro en disco
workbook.save("output_with_sparklines.xlsx");
```

El código anterior produce un libro donde cada representación visual de un minigráfico se duplica en dos formas: el minigráfico nativo en vivo anclado en la fila 1, y una imagen PNG estática incrustada directamente en una celda vecina de la fila 2. Debido a que las imágenes viven dentro del archivo mismo, el libro sigue siendo un único artefacto autónomo que se puede enviar por correo electrónico o archivar sin romper las referencias de imágenes incrustadas. Renderice cada grupo de minigráficos como un PNG, convierta el `ByteArrayOutputStream` a un `byte[]`, y asigne el arreglo a la propiedad `EmbeddedImage` de la celda destino mediante `setEmbeddedImage(byte[])` — la asignación es lo que hace que la imagen forme parte del contenido almacenado de la celda.

{{% alert color="primary" %}}
Dado que cada grupo de minigráficos está anclado a una sola celda, puede acceder a él mediante el indexador `group.getSparklines().get(0)` en lugar de enumerar con un bucle `for`. Esto mantiene corto el código de renderizado y coincide con el patrón típico de "un minigráfico por celda ancla". Almacenar los bytes de la imagen mediante `Cell.EmbeddedImage` (establecido a través de `setEmbeddedImage`) requiere Aspose.Cells 26.5 o posterior.
{{% /alert %}}

## **Flujo de trabajo 2 — Exportar la hoja de cálculo con minigráficos a HTML**

Una vez que el libro contiene minigráficos en vivo (y opcionalmente sus contrapartes de imagen incrustadas), la hoja de cálculo completa se puede publicar en la web guardándola como HTML. La clase `HtmlSaveOptions` expone los controles que necesita para gestionar esta exportación; en este flujo de trabajo reutilizará el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 y lo convertirá en un documento HTML limpio de una sola página.

### **Instrucciones paso a paso**

1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 esté disponible en disco en su directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y llame a `setExportActiveWorksheetOnly(true)` para que el archivo HTML resultante contenga solo la hoja de cálculo activa en lugar del libro completo.
4. Llame a `workbook.save("sparklines.html", htmlOptions)` para escribir la salida HTML en disco.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

El código anterior toma el libro con minigráficos del Flujo de trabajo 1 y lo convierte en un archivo HTML portátil. Los minigráficos se conservan como renderizaciones SVG o PNG en línea dentro del HTML generado, dependiendo del modo de exportación, para que los usuarios finales puedan ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `ExportActiveWorksheetOnly` en `true` mediante `setExportActiveWorksheetOnly(true)`, evita publicar accidentalmente hojas ocultas o datos auxiliares — solo se exporta la hoja de cálculo actualmente visible para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar la salida, como `ExportHiddenWorksheet`, `ExportImagesAsBase64`, y `Encoding`. Ajústelas según sea necesario para su destino de implementación.
{{% /alert %}}

## **Resumen de la API**

Los flujos de trabajo anteriores dependen de un pequeño conjunto de APIs de Aspose.Cells que trabajan en conjunto.

- `SparklineGroup` y el descriptor de acceso de la colección `worksheet.getSparklineGroups()` se utilizan para declarar el tipo (Línea, Columna, Apilado), el rango de datos, y la celda ancla de cada grupo de minigráficos. En este artículo, cada grupo está anclado a una sola celda, por lo que se accede al grupo mediante `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` y el indexador `group.getSparklines().get(0)` devuelven el minigráfico individual dentro de un grupo. Dado que cada grupo en el ejemplo contiene exactamente un minigráfico, no se requiere un bucle `for`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` es el método de renderizado que escribe una imagen del minigráfico en un `Stream` proporcionado. El método devuelve `void`; usted lee los bytes del flujo después de la llamada.
- `Cell.EmbeddedImage` es una propiedad `byte[]` (asignada mediante `cell.setEmbeddedImage(byte[])`) que almacena una imagen dentro de una sola celda. Está disponible en **Aspose.Cells 26.5 y posteriores** y es la forma recomendada de devolver un minigráfico renderizado por `toImage` al mismo libro.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas en `HtmlSaveOptions` cuando se generan informes de una sola página.
- `ImageOrPrintOptions.setImageType(ImageType)` reside en el paquete `com.aspose.cells.drawing` y selecciona el formato de imagen (por ejemplo, `ImageType.PNG`) utilizado al renderizar con `toImage` y al imprimir hojas de cálculo a imágenes.

## **Artículos relacionados**

- [Minigráficos en Aspose.Cells for Aspose.Cells for Java](/cells/es/java/sparkline/)
- [Insertar una imagen en una celda](/cells/es/java/inserting-an-image-into-a-cell/)
- [Renderizado de matrices en una sola celda con SmartMarker | Aspose.Cells Java](/cells/es/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}