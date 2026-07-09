---
title: Convertir minigráficos a imagen y HTML en Aspose.Cells for .NET
linktitle: Convert Sparkline to Image and HTML
description: Aprenda a renderizar minigráficos de Aspose.Cells a imágenes independientes para incrustarlas en celdas y exportar hojas de cálculo con minigráficos a HTML mediante HtmlSaveOptions.
keywords: Aspose.Cells, .NET, minigráfico, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizar minigráfico, convertir minigráfico a imagen, exportar minigráfico a HTML
type: docs
weight: 120
url: /es/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son gráficos en miniatura colocados dentro de las celdas de la hoja de cálculo. Aspose.Cells le permite extraer cada minigráfico como una imagen independiente (para incrustarla en otra celda o en un informe externo) y también exportar toda la hoja de cálculo con minigráficos a HTML para su distribución en el navegador. La propiedad `Cell.EmbeddedImage` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y versiones posteriores**.
{{% /alert %}}

## **Introducción**

Los minigráficos son una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Mientras que los usuarios de Excel los ven en su lugar, muchos escenarios del mundo real requieren que un minigráfico salga de la celda; por ejemplo, para incrustarse en una celda diferente como imagen estática, adjuntarse a un correo electrónico automatizado o renderizarse como parte de un informe HTML publicado en la web.

Aspose.Cells admite ambas operaciones. El método `Sparkline.ToImage` renderiza un minigráfico individual a un flujo, y los bytes resultantes se pueden asignar a `Cell.EmbeddedImage` para que la imagen se almacene dentro de una sola celda del libro. Por separado, `HtmlSaveOptions` le permite convertir todo el libro, incluidos los minigráficos, en un archivo HTML autónomo. Este artículo explica ambos flujos de trabajo de principio a fin.

## **Flujo de trabajo 1 — Renderizar minigráficos a imágenes e incrustarlos en celdas**

En este flujo de trabajo creará una hoja de cálculo que contiene un pequeño rango de valores de origen, adjuntará tres grupos de minigráficos diferentes (Línea, Columna y Apilado/Ganancia-Pérdida) a ese rango, renderizará cada grupo como PNG y escribirá esos bytes PNG en celdas adyacentes como imágenes incrustadas. El resultado final es un único archivo `.xlsx` que contiene tanto los minigráficos activos como sus contrapartes de imagen renderizadas.

### **Instrucciones paso a paso**

1. Defina un directorio de trabajo y asegúrese de que exista en disco.
2. Cree un nuevo `Workbook` y obtenga una referencia a la primera `Worksheet`.
3. Rellene las celdas `A1` a `E1` con cinco valores numéricos de muestra (por ejemplo, ventas diarias o lecturas de temperatura).
4. Agregue tres objetos `SparklineGroup` a la hoja de cálculo llamando a `worksheet.SparklineGroups.Add(...)`:
   - Un grupo `SparklineType.Line` anclado en `F1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Column` anclado en `G1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Stacked` (ganancia/pérdida) anclado en `H1`, con rango de datos `A1:E1`.
5. Construya una instancia de `ImageOrPrintOptions` y establezca su `ImageType` en `ImageType.Png` para que cada minigráfico se renderice como un PNG transparente.
6. Para cada uno de los tres grupos, renderice su único minigráfico usando `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, convierta el `MemoryStream` a un `byte[]` y asigne el arreglo a `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` y `worksheet.Cells["H2"].EmbeddedImage` respectivamente.
7. Guarde el libro como `output_with_sparklines.xlsx`.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// Crear un nuevo libro de trabajo y acceder a la primera hoja de cálculo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Poblar datos de muestra en las celdas A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Agregar un grupo de minigráficos de Línea anclado en F1 (columna 5, fila 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// Agregar un grupo de minigráficos de Columna anclado en G1 (columna 6, fila 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) anclado en H1 (columna 7, fila 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configurar las opciones de imagen para la salida PNG
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// Convertir el minigráfico de Línea a imagen e incrustarlo en la celda F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// Convertir el minigráfico de Columna a imagen e incrustarlo en la celda G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// Convertir el minigráfico de Ganancia/Pérdida a imagen e incrustarlo en la celda H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// Guardar el libro de trabajo en disco
workbook.Save("output_with_sparklines.xlsx");
```

El código anterior produce un libro donde cada representación visual de un minigráfico se duplica de dos formas: el minigráfico nativo y activo anclado en la fila 1, y una imagen PNG estática incrustada directamente en una celda vecina de la fila 2. Debido a que las imágenes viven dentro del propio archivo, el libro sigue siendo un artefacto único y autónomo que se puede enviar por correo electrónico o archivar sin romper las referencias de imagen incrustadas. Renderice cada grupo de minigráficos como PNG, convierta el `MemoryStream` a un `byte[]` y asigne el arreglo a la propiedad `EmbeddedImage` de la celda de destino; la asignación es lo que hace que la imagen forme parte del contenido almacenado de la celda.

{{% alert color="primary" %}}
Dado que cada grupo de minigráficos está anclado a una sola celda, puede acceder a él mediante el indexador `group.Sparklines[0]` en lugar de enumerar con `foreach`. Esto mantiene el código de renderizado corto y coincide con el patrón típico de "un minigráfico por celda ancla". Almacenar los bytes de la imagen mediante `Cell.EmbeddedImage` requiere Aspose.Cells 26.5 o posterior.
{{% /alert %}}

## **Flujo de trabajo 2 — Exportar la hoja de cálculo con minigráficos a HTML**

Una vez que el libro contiene minigráficos activos (y opcionalmente las contrapartes de imagen incrustadas), toda la hoja de cálculo se puede publicar en la web guardándola como HTML. La clase `HtmlSaveOptions` expone los controles que necesita para gestionar esta exportación; en este flujo de trabajo reutilizará el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 y lo convertirá en un documento HTML limpio y de una sola página.

### **Instrucciones paso a paso**

1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 esté disponible en disco en su directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y establezca su propiedad `ExportActiveWorksheetOnly` en `true` para que el archivo HTML resultante contenga solo la hoja de cálculo activa en lugar de todo el libro.
4. Llame a `workbook.Save("sparklines.html", htmlOptions)` para escribir la salida HTML en disco.

```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

El código anterior toma el libro con minigráficos del Flujo de trabajo 1 y lo convierte en un archivo HTML portátil. Los minigráficos se conservan como representaciones SVG en línea o PNG dentro del HTML generado, según el modo de exportación, de modo que los usuarios finales pueden ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `ExportActiveWorksheetOnly` en `true`, evita publicar accidentalmente hojas ocultas o datos auxiliares; solo se exporta la hoja de cálculo visible actualmente para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar la salida, como `ExportHiddenWorksheet`, `ExportImagesAsBase64` y `Encoding`. Ajústelas según sea necesario para su destino de implementación.
{{% /alert %}}

## **Resumen de la API**

Los flujos de trabajo anteriores dependen de un pequeño conjunto de API de Aspose.Cells que trabajan en conjunto.

- `SparklineGroup` y el descriptor de acceso de colección `worksheet.SparklineGroups` se utilizan para declarar el tipo (Line, Column, Stacked), el rango de datos y la celda ancla de cada grupo de minigráficos. En este artículo, cada grupo está anclado a una sola celda, por lo que se accede al grupo mediante `worksheet.SparklineGroups[i]`.
- `Sparkline` y el indexador `group.Sparklines[0]` devuelven el minigráfico individual dentro de un grupo. Dado que cada grupo del ejemplo contiene exactamente un minigráfico, no se requiere un bucle `foreach`.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` es el método de renderizado que escribe una imagen del minigráfico en un `Stream` proporcionado. El método devuelve `void`; usted lee los bytes del flujo después de la llamada.
- `Cell.EmbeddedImage` es una propiedad `byte[]` que almacena una imagen dentro de una sola celda. Está disponible en **Aspose.Cells 26.5 y versiones posteriores** y es la forma recomendada de reintegrar un minigráfico renderizado por `ToImage` de vuelta al mismo libro.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas de `HtmlSaveOptions` al generar informes de una sola página.
- `ImageOrPrintOptions.ImageType` se encuentra en el espacio de nombres `Aspose.Cells.Drawing` y selecciona el formato de imagen (por ejemplo, `ImageType.Png`) utilizado al renderizar con `ToImage` y al imprimir hojas de cálculo como imágenes.

## **Artículos relacionados**

- [Minigráficos en Aspose.Cells for .NET](/cells/es/net/sparkline/)
- [Insertar una imagen en una celda](/cells/es/net/inserting-an-image-into-a-cell/)
- [Renderizado de matrices de una sola celda con SmartMarker | Aspose.Cells .NET](/cells/es/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}