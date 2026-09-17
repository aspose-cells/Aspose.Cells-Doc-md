---
title: Convertir minigráficos a imágenes y HTML con Aspose.Cells for Java
linktitle: Convertir minigráficos a imágenes y HTML con Aspose.Cells for Java
description: Aprenda a representar los minigráficos de Aspose.Cells como imágenes independientes para incrustarlas en celdas y exportar hojas de cálculo con minigráficos a HTML mediante HtmlSaveOptions.
keywords: Aspose.Cells, Java, minigráfico, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, representar minigráficos, convertir minigráficos a imágenes, exportar minigráficos a HTML
type: docs
weight: 120
url: /es/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son pequeños gráficos colocados dentro de las celdas de una hoja de cálculo. Aspose.Cells permite extraer cada minigráfico como una imagen independiente, para incrustarlo en otra celda o en un informe externo, y también exportar a HTML toda la hoja de cálculo que contiene los minigráficos para distribuirla mediante un navegador. La propiedad `Cell.EmbeddedImage` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y versiones posteriores**.

## **Introducción**
Los minigráficos ofrecen una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Aunque los usuarios de Excel los ven en su lugar, muchos escenarios reales requieren que un minigráfico salga de la celda; por ejemplo, para incrustarlo en otra celda como una imagen estática, adjuntarlo a un mensaje de correo electrónico automatizado o representarlo como parte de un informe HTML publicado en la web.
Aspose.Cells admite ambas operaciones. El método `Sparkline.toImage` representa un minigráfico individual en un flujo, y los bytes resultantes pueden asignarse a `Cell.EmbeddedImage` mediante `setEmbeddedImage`, de modo que la imagen quede almacenada dentro de una única celda del libro. Por separado, `HtmlSaveOptions` permite convertir todo el libro, incluidos los minigráficos, en un archivo HTML autocontenido. Este artículo explica ambas secuencias de trabajo de principio a fin.

## **Secuencia de trabajo 1 — Representar minigráficos como imágenes e incrustarlos en celdas**
En esta secuencia de trabajo, creará una hoja de cálculo que contiene un pequeño rango de valores de origen, adjuntará a ese rango tres grupos de minigráficos diferentes (línea, columna y apilado/ganador-perdedor), representará cada grupo como un archivo PNG y escribirá los bytes de esos archivos en celdas adyacentes como imágenes incrustadas. El resultado final será un único archivo `.xlsx` que contiene tanto los minigráficos activos como sus imágenes estáticas equivalentes.

### **Instrucciones paso a paso**
1. Defina un directorio de trabajo y asegúrese de que exista en el disco.
2. Cree un nuevo `Workbook` y obtenga una referencia a la primera `Worksheet`.
3. Rellene las celdas `A1` a `E1` con cinco valores numéricos de ejemplo, como ventas diarias o lecturas de temperatura.
4. Agregue tres objetos `SparklineGroup` a la hoja de cálculo mediante una llamada a `worksheet.getSparklineGroups().add(...)`:
   - Un grupo `SparklineType.LINE` anclado en `F1`, con el rango de datos `A1:E1`.
   - Un grupo `SparklineType.COLUMN` anclado en `G1`, con el rango de datos `A1:E1`.
   - Un grupo `SparklineType.STACKED` (ganador/perdedor) anclado en `H1`, con el rango de datos `A1:E1`.
5. Cree una instancia de `ImageOrPrintOptions` y llame a `setImageType(ImageType.PNG)` para que cada minigráfico se represente como un archivo PNG transparente.
6. Llame a `workbook.save("output_with_sparklines.xlsx")` para guardar el libro en el disco.

```java
import com.aspose.cells.*;
import java.io.*;
// Crear un nuevo libro de trabajo y acceder a la primera hoja de trabajo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Poblar datos de muestra en las celdas A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Agregar un grupo de minigráficos de líneas anclado en F1 (columna 5, fila 0)
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
// Agregar un grupo de minigráficos de columnas anclado en G1 (columna 6, fila 0)
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
// Agregar un grupo de minigráficos de victorias/derrotas (apilados) anclado en H1 (columna 7, fila 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
// Configurar las opciones de imagen para la salida PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);
// Convertir el minigráfico de líneas a imagen e incrustarlo en la celda F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());
// Convertir el minigráfico de columnas a imagen e incrustarlo en la celda G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());
// Convertir el minigráfico de victorias/derrotas a imagen e incrustarlo en la celda H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());
// Guardar el libro de trabajo en disco
workbook.save("output_with_sparklines.xlsx");
```

El código anterior genera un libro en el que cada representación visual de un minigráfico aparece duplicada de dos formas: el minigráfico nativo activo anclado en la fila 1 y una imagen PNG estática incrustada directamente en una celda adyacente de la fila 2. Como las imágenes están contenidas en el propio archivo, el libro sigue siendo un único artefacto autocontenido que puede enviarse por correo electrónico o archivarse sin que se rompan las referencias a las imágenes incrustadas. Represente cada grupo de minigráficos como un archivo PNG, convierta el `ByteArrayOutputStream` en un arreglo `byte[]` y asigne el arreglo a la propiedad `EmbeddedImage` de la celda de destino mediante `setEmbeddedImage(byte[])`; esta asignación es lo que incorpora la imagen al contenido almacenado de la celda.

{{% alert color="primary" %}}
Como cada grupo de minigráficos está anclado a una única celda, puede acceder a él mediante el indexador `group.getSparklines().get(0)` en lugar de enumerar sus elementos con un bucle `for`. Esto permite mantener breve el código de representación y se ajusta al patrón habitual de «un minigráfico por celda de anclaje». El almacenamiento de los bytes de la imagen mediante `Cell.EmbeddedImage`, establecido a través de `setEmbeddedImage`, requiere Aspose.Cells 26.5 o una versión posterior.

## **Secuencia de trabajo 2 — Exportar la hoja de cálculo con minigráficos a HTML**
Una vez que el libro contiene minigráficos activos y, opcionalmente, imágenes equivalentes incrustadas, se puede publicar toda la hoja de cálculo en la web guardándola como HTML. La clase `HtmlSaveOptions` ofrece los controles necesarios para configurar esta exportación. En esta secuencia de trabajo, reutilizará el archivo `output_with_sparklines.xlsx` generado por la Secuencia de trabajo 1 y lo convertirá en un documento HTML limpio de una sola página.

### **Instrucciones paso a paso**
1. Asegúrese de que el archivo `output_with_sparklines.xlsx` generado por la Secuencia de trabajo 1 esté disponible en el disco, dentro de su directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y llame a `setExportActiveWorksheetOnly(true)` para que el archivo HTML resultante contenga únicamente la hoja de cálculo activa, en lugar del libro completo.
4. Llame a `workbook.save("sparklines.html", htmlOptions)` para escribir la salida HTML en el disco.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

El código anterior convierte el libro con minigráficos de la Secuencia de trabajo 1 en un archivo HTML portátil. Los minigráficos se conservan como representaciones SVG o PNG insertadas en el HTML generado, según el modo de exportación, por lo que los usuarios finales pueden consultar las tendencias desde cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `ExportActiveWorksheetOnly` en `true` mediante `setExportActiveWorksheetOnly(true)`, evita publicar accidentalmente hojas de cálculo ocultas o datos auxiliares: solo se exporta la hoja de cálculo que el usuario ve actualmente.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar con precisión la salida, como `ExportHiddenWorksheet`, `ExportImagesAsBase64` y `Encoding`. Ajústelas según sea necesario para el entorno de implementación.

## **Resumen de la API**
Las secuencias de trabajo anteriores se basan en un pequeño conjunto de API de Aspose.Cells que funcionan conjuntamente.
- `SparklineGroup` y el descriptor de acceso de colección `worksheet.getSparklineGroups()` se utilizan para declarar el tipo (línea, columna, apilado), el rango de datos y la celda de anclaje de cada grupo de minigráficos. En este artículo, cada grupo está anclado a una única celda, por lo que se accede a él mediante `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` y el indexador `group.getSparklines().get(0)` devuelven el minigráfico individual dentro de un grupo. Como cada grupo del ejemplo contiene exactamente un minigráfico, no se necesita un bucle `for`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` es el método de representación que escribe una imagen del minigráfico en un `Stream` proporcionado. El método devuelve `void`; los bytes se leen del flujo después de la llamada.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas de `HtmlSaveOptions` al generar informes de una sola página.
- `ImageOrPrintOptions.setImageType(ImageType)` se encuentra en el paquete `com.aspose.cells.drawing` y selecciona el formato de imagen, como `ImageType.PNG`, utilizado al representar con `toImage` y al imprimir hojas de cálculo como imágenes.

## **Artículos relacionados**
- [Minigráficos en Aspose.Cells for Java](/cells/es/java/sparkline/)
- [Inserción de una imagen en una celda](/cells/es/java/inserting-an-image-into-a-cell/)
- [Renderizado de matrices de una única celda con SmartMarker | Aspose.Cells Java](/cells/es/java/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="java" >}}