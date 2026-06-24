---
title: Convertir Sparkline a Imagen y HTML en Aspose.Cells for Node.js via C++
linktitle: Convert Sparkline to Image and HTML
description: Aprenda cómo renderizar sparklines de Aspose.Cells a imágenes independientes para incrustarlas en celdas y exportar hojas de cálculo con sparklines a HTML usando HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via C++, sparkline, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, renderizar sparkline, convertir sparkline a imagen, exportar sparkline a HTML
type: docs
weight: 120
url: /es/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los sparklines son minigráficos colocados dentro de las celdas de una hoja de cálculo. Aspose.Cells le permite extraer cada sparkline como una imagen independiente (para incrustarla en otra celda o en un informe externo) y también exportar la hoja de cálculo completa con sparklines a HTML para su distribución en el navegador. La propiedad `cell.embeddedImage` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y versiones posteriores**.
{{% /alert %}}

## **Introducción**

Los sparklines son una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Mientras que los usuarios de Excel los ven en su lugar, muchos escenarios del mundo real requieren que un sparkline salga de la celda — por ejemplo, para incrustarse en una celda diferente como una imagen estática, adjuntarse a un correo electrónico automatizado, o renderizarse como parte de un informe HTML publicado en la web.

Aspose.Cells admite ambas operaciones. El método `Sparkline.toImage` renderiza un sparkline individual a un flujo, y los bytes resultantes pueden asignarse a `cell.embeddedImage` para que la imagen se almacene dentro de una sola celda del libro de trabajo. Por separado, `HtmlSaveOptions` le permite convertir el libro de trabajo completo — sparklines incluidos — en un archivo HTML autónomo. Este artículo recorre ambos flujos de trabajo de principio a fin.

## **Flujo de trabajo 1 — Renderizar Sparklines a Imágenes e Incrustarlos en Celdas**

En este flujo de trabajo, construirá una hoja de cálculo que contiene un pequeño rango de valores fuente, adjuntará tres grupos de sparklines diferentes (Línea, Columna y Apilado/Win-Loss) a ese rango, renderizará cada grupo como un PNG, y escribirá esos bytes PNG en celdas adyacentes como imágenes incrustadas. El resultado final es un único archivo `.xlsx` que contiene tanto los sparklines activos como sus contrapartes de imagen renderizadas.

### **Instrucciones Paso a Paso**

1. Defina un directorio de trabajo y asegúrese de que exista en disco.
2. Cree un nuevo `Workbook` y obtenga una referencia a la primera `Worksheet`.
3. Rellene las celdas `A1` a `E1` con cinco valores numéricos de muestra (por ejemplo, ventas diarias o lecturas de temperatura).
4. Agregue tres objetos `SparklineGroup` a la hoja de cálculo llamando a `worksheet.sparklineGroups.add(...)`:
   - Un grupo `SparklineType.Line` anclado en `F1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Column` anclado en `G1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Stacked` (win/loss) anclado en `H1`, con rango de datos `A1:E1`.
5. Construya una instancia de `ImageOrPrintOptions` y establezca su `ImageType` a `ImageType.Png` para que cada sparkline se renderice como un PNG transparente.
6. Para cada uno de los tres grupos, renderice su único sparkline usando `group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)`, convierta el flujo a un `Buffer` (o `Uint8Array`), y asigne los bytes a `worksheet.cells["F2"].embeddedImage`, `worksheet.cells["G2"].embeddedImage`, y `worksheet.cells["H2"].embeddedImage` respectivamente.
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
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// Convertir el minigráfico de columna a imagen e incrustarlo en la celda G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// Convertir el minigráfico de Ganancia/Pérdida a imagen e incrustarlo en la celda H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// Guardar el libro de trabajo en disco
workbook.save("output_with_sparklines.xlsx");
```

El código anterior produce un libro de trabajo donde cada representación visual de un sparkline se duplica en dos formas: el sparkline nativo y activo anclado en la fila 1, y una imagen PNG estática incrustada directamente en una celda vecina de la fila 2. Debido a que las imágenes viven dentro del propio archivo, el libro de trabajo sigue siendo un único artefacto autónomo que puede enviarse por correo electrónico o archivarse sin romper las referencias de imagen incrustadas. Renderice cada grupo de sparkline como un PNG, convierta el flujo a un `Buffer`, y asigne el arreglo a la propiedad `embeddedImage` de la celda de destino — la asignación es lo que hace que la imagen sea parte del contenido almacenado de la celda.

{{% alert color="primary" %}}
Dado que cada grupo de sparkline está anclado a una sola celda, puede acceder a él mediante el indexador `group.sparklines[0]` en lugar de enumerar con `forEach`. Esto mantiene el código de renderizado corto y coincide con el patrón típico de "un sparkline por celda ancla". Almacenar los bytes de la imagen a través de `cell.embeddedImage` requiere Aspose.Cells 26.5 o posterior.
{{% /alert %}}

## **Flujo de trabajo 2 — Exportar la Hoja de Cálculo con Sparklines a HTML**

Una vez que el libro de trabajo contiene sparklines activos (y opcionalmente contrapartes de imágenes incrustadas), toda la hoja de cálculo puede publicarse en la web guardándola como HTML. La clase `HtmlSaveOptions` expone los controles que necesita para controlar esta exportación; en este flujo de trabajo reutilizará el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 y lo convertirá en un documento HTML limpio de una sola página.

### **Instrucciones Paso a Paso**

1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 esté disponible en disco en su directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y establezca su propiedad `exportActiveWorksheetOnly` a `true` para que el archivo HTML resultante contenga solo la hoja de cálculo activa en lugar del libro de trabajo completo.
4. Llame a `workbook.save("sparklines.html", htmlOptions)` para escribir la salida HTML en disco.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

El código anterior toma el libro de trabajo con sparklines del Flujo de trabajo 1 y lo convierte en un archivo HTML portable. Los sparklines se conservan como SVG en línea o renderizaciones PNG dentro del HTML generado, dependiendo del modo de exportación, por lo que los usuarios finales pueden ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `exportActiveWorksheetOnly` a `true`, evita publicar accidentalmente hojas ocultas o datos auxiliares — solo se exporta la hoja de cálculo actualmente visible para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar la salida, como `exportHiddenWorksheet`, `exportImagesAsBase64`, y `encoding`. Ajústelas según sea necesario para su destino de despliegue.
{{% /alert %}}

## **Resumen de la API**

Los flujos de trabajo anteriores dependen de un pequeño conjunto de APIs de Aspose.Cells que trabajan juntas.

- `SparklineGroup` y el descriptor de acceso de colección `worksheet.sparklineGroups` se utilizan para declarar el tipo (Línea, Columna, Apilado), el rango de datos y la celda ancla para cada grupo de sparklines. En este artículo, cada grupo está anclado a una sola celda, por lo que se accede al grupo a través de `worksheet.sparklineGroups[i]`.
- `Sparkline` y el indexador `group.sparklines[0]` devuelven el sparkline individual dentro de un grupo. Dado que cada grupo en el ejemplo contiene exactamente un sparkline, no se requiere un bucle `forEach`.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` es el método de renderizado que escribe una imagen del sparkline en un `Stream` proporcionado. El método devuelve `void`; usted lee los bytes del flujo después de la llamada.
- `cell.embeddedImage` es una propiedad `Buffer` (o `Uint8Array`) que almacena una imagen dentro de una sola celda. Está disponible en **Aspose.Cells 26.5 y versiones posteriores** y es la forma recomendada de hacer un round-trip de un sparkline renderizado por `toImage` de vuelta al mismo libro de trabajo.
- `htmlSaveOptions.exportActiveWorksheetOnly` (un `bool`) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas de `HtmlSaveOptions` al generar informes de una sola página.
- `imageOrPrintOptions.imageType` reside en el namespace `Aspose.Cells.Drawing` y selecciona el formato de imagen (por ejemplo, `ImageType.Png`) utilizado al renderizar con `toImage` y al imprimir hojas de cálculo a imágenes.

## **Artículos Relacionados**

- [Sparklines en Aspose.Cells para Aspose.Cells for Node.js via C++](/cells/es/nodejs-cpp/sparkline/)
- [Insertar una Imagen en una Celda](/cells/es/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Renderizado de Arreglo de Celda Única con SmartMarker | Aspose.Cells Node.js via C++](/cells/es/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}