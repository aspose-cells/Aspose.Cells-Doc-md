---
title: Convertir minigráfico a imagen y HTML en Aspose.Cells for Node.js via Java
linktitle: Convert Sparkline to Image and HTML
description: Aprenda cómo renderizar minigráficos de Aspose.Cells a imágenes independientes para incrustar en celdas y exportar hojas de cálculo con minigráficos a HTML usando HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via Java, minigráfico, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizar minigráfico, convertir minigráfico a imagen, exportar minigráfico a HTML
type: docs
weight: 120
url: /es/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son gráficos en miniatura colocados dentro de las celdas de la hoja de cálculo. Aspose.Cells le permite extraer cada minigráfico como una imagen independiente (para incrustarlo en otra celda o en un informe externo) y también exportar toda la hoja de cálculo con minigráficos a HTML para su distribución basada en navegador. La propiedad `Cell.EmbeddedImage` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y versiones posteriores**.
{{% /alert %}}

## **Introducción**

Los minigráficos son una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Mientras que los usuarios de Excel los ven en su lugar, muchos escenarios del mundo real requieren que un minigráfico salga de la celda — por ejemplo, para ser incrustado en una celda diferente como una imagen estática, adjuntado a un correo electrónico automatizado, o renderizado como parte de un informe HTML publicado en la web.

Aspose.Cells admite ambas operaciones. El método `Sparkline.toImage` renderiza un minigráfico individual a un flujo, y los bytes resultantes se pueden asignar a `Cell.EmbeddedImage` para que la imagen quede almacenada dentro de una sola celda del libro de trabajo. Por separado, `HtmlSaveOptions` le permite convertir todo el libro de trabajo — con minigráficos y todo — en un archivo HTML autónomo. Este artículo recorre ambos flujos de trabajo de extremo a extremo.

## **Flujo de Trabajo 1 — Renderizar Minigráficos a Imágenes e Incrustarlos en Celdas**

En este flujo de trabajo, construirá una hoja de cálculo que contiene un pequeño rango de valores de origen, adjuntará tres grupos de minigráficos diferentes (Línea, Columna y Apilado/Ganancia-Pérdida) a ese rango, renderizará cada grupo como PNG, y escribirá esos bytes PNG en celdas adyacentes como imágenes incrustadas. El resultado final es un único archivo `.xlsx` que contiene tanto los minigráficos en vivo como sus contrapartes de imagen renderizadas.

### **Instrucciones Paso a Paso**

1. Defina un directorio de trabajo y asegúrese de que exista en el disco.
2. Cree un nuevo `Workbook` y obtenga una referencia a la primera `Worksheet`.
3. Rellene las celdas `A1` a `E1` con cinco valores numéricos de muestra (por ejemplo, ventas diarias o lecturas de temperatura).
4. Agregue tres objetos `SparklineGroup` a la hoja de cálculo llamando a `worksheet.sparklineGroups.add(...)`:
   - Un grupo `SparklineType.Line` anclado en `F1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Column` anclado en `G1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Stacked` (ganancia/pérdida) anclado en `H1`, con rango de datos `A1:E1`.
5. Construya una instancia de `ImageOrPrintOptions` y establezca su `ImageType` a `ImageType.Png` para que cada minigráfico se renderice como un PNG transparente.
6. Para cada uno de los tres grupos, renderice su único minigráfico usando `group.sparklines[0].toImage(outputStream, imageOptions)`, convierta el `ByteArrayOutputStream` a un `byte[]`, y asigne el arreglo a `worksheet.cells.get("F2").setEmbeddedImage(...)`, `worksheet.cells.get("G2").setEmbeddedImage(...)`, y `worksheet.cells.get("H2").setEmbeddedImage(...)` respectivamente.
7. Guarde el libro de trabajo como `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Poblar datos de muestra en las celdas A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Agregar un grupo de minigráficos de línea anclado en F1 (columna 5, fila 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Agregar un grupo de minigráficos de columna anclado en G1 (columna 6, fila 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) anclado en H1 (columna 7, fila 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configurar opciones de imagen para salida PNG
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Convertir el minigráfico de línea a imagen e incrustarlo en la celda F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Convertir el minigráfico de columna a imagen e incrustarlo en la celda G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Convertir el minigráfico de Ganancia/Pérdida a imagen e incrustarlo en la celda H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Guardar el libro de trabajo en disco
workbook.save("output_with_sparklines.xlsx");
```

El código anterior produce un libro de trabajo donde cada representación visual de un minigráfico se duplica en dos formas: el minigráfico nativo y en vivo anclado en la fila 1, y una imagen PNG estática incrustada directamente en una celda vecina en la fila 2. Debido a que las imágenes viven dentro del archivo mismo, el libro de trabajo sigue siendo un único artefacto autónomo que se puede enviar por correo electrónico o archivar sin romper las referencias de imágenes incrustadas. Renderice cada grupo de minigráfico como PNG, convierta el `ByteArrayOutputStream` a un `byte[]`, y asigne el arreglo a la propiedad `setEmbeddedImage` de la celda objetivo — la asignación es lo que hace que la imagen forme parte del contenido almacenado de la celda.

{{% alert color="primary" %}}
Dado que cada grupo de minigráficos está anclado a una sola celda, puede acceder a él a través del indexador `group.sparklines[0]` en lugar de enumerar con `forEach`. Esto mantiene el código de renderizado corto y coincide con el patrón típico de "un minigráfico por celda ancla". Almacenar los bytes de la imagen a través de `Cell.EmbeddedImage` requiere Aspose.Cells 26.5 o posterior.
{{% /alert %}}

## **Flujo de Trabajo 2 — Exportar la Hoja de Cálculo con Minigráficos a HTML**

Una vez que el libro de trabajo contiene minigráficos en vivo (y opcionalmente contrapartes de imágenes incrustadas), toda la hoja de cálculo se puede publicar en la web guardándola como HTML. La clase `HtmlSaveOptions` expone los controles que necesita para controlar esta exportación; en este flujo de trabajo, reutilizará el archivo `output_with_sparklines.xlsx` producido por el Flujo de Trabajo 1 y lo convertirá a un documento HTML limpio de una sola página.

### **Instrucciones Paso a Paso**

1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido por el Flujo de Trabajo 1 esté disponible en el disco en su directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y establezca su propiedad `ExportActiveWorksheetOnly` a `true` para que el archivo HTML resultante contenga solo la hoja de cálculo activa en lugar del libro de trabajo completo.
4. Llame a `workbook.save("sparklines.html", htmlOptions)` para escribir la salida HTML en el disco.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

El código anterior toma el libro de trabajo con minigráficos del Flujo de Trabajo 1 y lo convierte en un archivo HTML portátil. Los minigráficos se conservan como SVG en línea o renderizaciones PNG dentro del HTML generado, según el modo de exportación, para que los usuarios finales puedan ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `ExportActiveWorksheetOnly` a `true`, evita publicar accidentalmente hojas ocultas o datos auxiliares — solo se exporta la hoja de cálculo actualmente visible para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar la salida, como `ExportHiddenWorksheet`, `ExportImagesAsBase64`, y `Encoding`. Ajústelas según sea necesario para su objetivo de implementación.
{{% /alert %}}

## **Resumen de la API**

Los flujos de trabajo anteriores se basan en un pequeño conjunto de APIs de Aspose.Cells que trabajan juntas.

- `SparklineGroup` y el accesor de colección `worksheet.sparklineGroups` se utilizan para declarar el tipo (Línea, Columna, Apilado), el rango de datos y la celda ancla para cada grupo de minigráficos. En este artículo, cada grupo está anclado a una sola celda, por lo que se accede al grupo a través de `worksheet.sparklineGroups[i]`.
- `Sparkline` y el indexador `group.sparklines[0]` devuelven el minigráfico individual dentro de un grupo. Dado que cada grupo en el ejemplo contiene exactamente un minigráfico, no se requiere un bucle `forEach`.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` es el método de renderizado que escribe una imagen del minigráfico en un `OutputStream` proporcionado. El método devuelve `void`; usted lee los bytes del flujo después de la llamada.
- `Cell.EmbeddedImage` es una propiedad `byte[]` que almacena una imagen dentro de una sola celda. Está disponible en **Aspose.Cells 26.5 y versiones posteriores** y es la forma recomendada de regresar un minigráfico renderizado por `toImage` al mismo libro de trabajo.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `boolean`) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas en `HtmlSaveOptions` al generar informes de una sola página.
- `ImageOrPrintOptions.ImageType` reside en el espacio de nombres `com.aspose.cells.drawing` y selecciona el formato de imagen (por ejemplo, `ImageType.Png`) utilizado al renderizar con `toImage` y al imprimir hojas de cálculo como imágenes.

## **Artículos Relacionados**

- [Minigráficos en Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/sparkline/)
- [Insertar una imagen en una celda](/cells/es/nodejs-java/inserting-an-image-into-a-cell/)
- [Renderizado de arreglo de celda única de SmartMarker | Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Poblar datos de muestra en las celdas A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Agregar un grupo de minigráficos de línea anclado en F1 (columna 5, fila 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Agregar un grupo de minigráficos de columna anclado en G1 (columna 6, fila 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) anclado en H1 (columna 7, fila 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configurar opciones de imagen para salida PNG
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Convertir el minigráfico de línea a imagen e incrustarlo en la celda F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Convertir el minigráfico de columna a imagen e incrustarlo en la celda G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Convertir el minigráfico de Ganancia/Pérdida a imagen e incrustarlo en la celda H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Guardar el libro de trabajo en disco
workbook.save("output_with_sparklines.xlsx");javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

El código anterior toma el libro de trabajo con minigráficos del Flujo de Trabajo 1 y lo convierte en un archivo HTML portátil. Los minigráficos se conservan como SVG en línea o como renderizaciones PNG dentro del HTML generado, según el modo de exportación, de modo que los usuarios finales puedan ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `ExportActiveWorksheetOnly` a `true`, evita publicar accidentalmente hojas ocultas o datos auxiliares: solo se exporta la hoja de cálculo actualmente visible para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar la salida, como `ExportHiddenWorksheet`, `ExportImagesAsBase64` y `Encoding`. Ajústelas según sea necesario para el destino de su implementación.
{{% /alert %}}

## **Resumen de la API**

Los flujos de trabajo anteriores se basan en un pequeño conjunto de APIs de Aspose.Cells que trabajan de forma conjunta.

- `SparklineGroup` y el descriptor de acceso a la colección `worksheet.sparklineGroups` se utilizan para declarar el tipo (Línea, Columna, Apilado), el rango de datos y la celda ancla de cada grupo de minigráficos. En este artículo, cada grupo está anclado a una sola celda, por lo que se accede al grupo mediante `worksheet.sparklineGroups[i]`.
- `Sparkline` y el indizador `group.sparklines[0]` devuelven el minigráfico individual dentro de un grupo. Dado que cada grupo del ejemplo contiene exactamente un minigráfico, no se requiere ningún bucle `forEach`.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` es el método de renderizado que escribe una imagen del minigráfico en un `OutputStream` proporcionado. El método devuelve `void`; los bytes se leen desde el flujo después de la llamada.
- `Cell.EmbeddedImage` es una propiedad `byte[]` que almacena una imagen dentro de una sola celda. Está disponible en **Aspose.Cells 26.5 y versiones posteriores** y es la forma recomendada de devolver un minigráfico renderizado por `toImage` al mismo libro de trabajo.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (de tipo `boolean`) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas en `HtmlSaveOptions` al generar informes de una sola página.
- `ImageOrPrintOptions.ImageType` reside en el espacio de nombres `com.aspose.cells.drawing` y selecciona el formato de imagen (por ejemplo, `ImageType.Png`) utilizado al renderizar con `toImage` y al imprimir hojas de cálculo como imágenes.

## **Artículos Relacionados**

- [Minigráficos en Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/sparkline/)
- [Insertar una imagen en una celda](/cells/es/nodejs-java/inserting-an-image-into-a-cell/)
- [Renderizado de arreglos de celda única con SmartMarker | Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}