---
title: Convertir minigráficos a imágenes y HTML en Aspose.Cells for C++
linktitle: Convertir minigráficos a imágenes y HTML en Aspose.Cells for C++
description: Aprenda a generar imágenes independientes de los minigráficos de Aspose.Cells para incrustarlas en celdas y exportar a HTML hojas de cálculo con minigráficos mediante HtmlSaveOptions.
keywords: Aspose.Cells, C++, minigráfico, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, generar minigráfico, convertir minigráfico en imagen, exportar minigráfico a HTML
type: docs
weight: 120
url: /es/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son gráficos en miniatura colocados dentro de las celdas de una hoja de cálculo. Aspose.Cells permite extraer cada minigráfico como una imagen independiente (para incrustarlo en otra celda o en un informe externo) y también exportar toda la hoja de cálculo con minigráficos a HTML para su distribución mediante navegadores. La propiedad `Cell.EmbeddedImage` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y versiones posteriores**.

## **Introducción**
Los minigráficos son una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Aunque los usuarios de Excel los ven en las celdas, en muchos escenarios reales es necesario extraer un minigráfico de ellas; por ejemplo, para insertarlo como imagen estática en otra celda, adjuntarlo a un correo electrónico automatizado o incluirlo como imagen en un informe HTML publicado en la web.
Aspose.Cells admite ambas operaciones. El método `Sparkline.ToImage` genera una imagen de un minigráfico individual en forma de vector de bytes `Vector<uint8_t>`, y los bytes resultantes se pueden asignar a `Cell.EmbeddedImage` para almacenar la imagen dentro de una sola celda del libro de trabajo. Por otra parte, `HtmlSaveOptions` permite convertir el libro de trabajo completo, incluidos los minigráficos, en un archivo HTML autocontenido. Este artículo explica ambos flujos de trabajo de principio a fin.

## **Flujo de trabajo 1 — Generar minigráficos como imágenes e incrustarlos en celdas**
En este flujo de trabajo, creará una hoja de cálculo que contiene un rango reducido de valores de origen, asociará tres grupos diferentes de minigráficos (Línea, Columna y Apilado/Ganancia-Pérdida) a ese rango, generará cada minigráfico en formato PNG y guardará los bytes de cada imagen en celdas adyacentes como imágenes incrustadas. El resultado final será un único archivo `.xlsx` que contiene tanto los minigráficos activos como sus imágenes estáticas equivalentes.

### **Instrucciones paso a paso**
1. Defina un directorio de trabajo y asegúrese de que exista en disco.
2. Cree un nuevo `Workbook` y obtenga una referencia al primer `Worksheet`.
3. Introduzca cinco valores numéricos de ejemplo en las celdas `A1` a `E1` (por ejemplo, ventas diarias o lecturas de temperatura).
4. Añada tres objetos `SparklineGroup` a la hoja de cálculo mediante una llamada a `worksheet.SparklineGroups.Add(...)`:
   - Un grupo `SparklineType.Line` con `F1` como celda de anclaje y `A1:E1` como rango de datos.
   - Un grupo `SparklineType.Column` con `G1` como celda de anclaje y `A1:E1` como rango de datos.
   - Un grupo `SparklineType.Stacked` (ganancia/pérdida) con `H1` como celda de anclaje y `A1:E1` como rango de datos.
5. Cree una instancia de `ImageOrPrintOptions` y establezca su propiedad `ImageType` en `ImageType.Png` para generar cada minigráfico como una imagen PNG transparente.
6. En cada uno de los tres grupos, genere su único minigráfico mediante `group.Sparklines[0].ToImage(imageOptions)`. La llamada devuelve directamente los bytes de la imagen como un `Vector<uint8_t>`; a continuación, asigne respectivamente el vector a `worksheet.GetCells().Get("F2"].EmbeddedImage`, `worksheet.GetCells().Get("G2"].EmbeddedImage` y `worksheet.GetCells().Get("H2"].EmbeddedImage`.
7. Guarde el libro de trabajo como `output_with_sparklines.xlsx`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);
    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);
    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);
    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);
    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);
    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);
    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);
    workbook.Save(u"output_with_sparklines.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

El código anterior crea un libro de trabajo en el que cada representación visual de un minigráfico se duplica en dos formatos: el minigráfico nativo y activo, anclado en la fila 1, y una imagen PNG estática insertada directamente en una celda adyacente de la fila 2. Dado que las imágenes se almacenan en el propio archivo, el libro de trabajo constituye un único artefacto autocontenido que se puede enviar por correo electrónico o archivar sin que se rompan las referencias a las imágenes incrustadas. Genere cada minigráfico como una imagen PNG — `Sparkline.ToImage(ImageOrPrintOptions)` devuelve directamente los bytes de la imagen en forma de `Vector<uint8_t>` — y asigne el vector a la propiedad `EmbeddedImage` de la celda de destino; esta asignación es la que incorpora la imagen al contenido almacenado de la celda.

{{% alert color="primary" %}}
Como cada grupo de minigráficos está asociado a una sola celda, puede obtenerlo mediante el operador de indexación `group.Sparklines[0]` en lugar de recorrer la colección con `foreach`. Esto reduce el código necesario para generar las imágenes y se ajusta al patrón habitual de «un minigráfico por celda de anclaje». Guardar los bytes de la imagen mediante `Cell.EmbeddedImage` requiere Aspose.Cells 26.5 o posterior.

## **Flujo de trabajo 2 — Exportar la hoja de cálculo con minigráficos a HTML**
Una vez que el libro de trabajo contiene minigráficos activos (y, opcionalmente, imágenes estáticas equivalentes), la hoja de cálculo se puede publicar en la web guardándola como HTML. La clase `HtmlSaveOptions` ofrece las opciones necesarias para controlar esta exportación. En este flujo de trabajo, reutilizará el archivo `output_with_sparklines.xlsx` producido por el flujo de trabajo 1 y lo convertirá en un documento HTML limpio de una sola página.

### **Instrucciones paso a paso**
1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido por el flujo de trabajo 1 esté disponible en disco dentro de su directorio de trabajo.
2. Cargue el archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y establezca su propiedad `ExportActiveWorksheetOnly` en `true` para que el archivo HTML resultante contenga únicamente la hoja de cálculo activa, en lugar del libro de trabajo completo.
4. Llame a `workbook.Save("sparklines.html", htmlOptions)` para guardar la salida HTML en disco.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);
    Aspose::Cells::Cleanup();
    return 0;
}
```

El código anterior convierte el libro de trabajo con minigráficos del flujo de trabajo 1 en un archivo HTML portable. Los minigráficos se conservan como representaciones SVG o PNG en línea dentro del HTML generado, según el modo de exportación, de modo que los usuarios finales pueden consultar las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `ExportActiveWorksheetOnly` en `true`, evita publicar accidentalmente hojas ocultas o datos auxiliares; únicamente se exporta la hoja de cálculo que el usuario ve actualmente.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar con precisión la salida, como `ExportHiddenWorksheet`, `ExportImagesAsBase64` y `Encoding`. Ajústelas según las necesidades de su entorno de implementación.

## **Resumen de la API**
Los flujos de trabajo anteriores se basan en un pequeño conjunto de API de Aspose.Cells que funcionan conjuntamente.
- `SparklineGroup` y la propiedad de colección `worksheet.SparklineGroups` permiten especificar el tipo (Línea, Columna, Apilado), el rango de datos y la celda de anclaje de cada grupo de minigráficos. En este artículo, cada grupo está anclado a una sola celda, por lo que se puede obtener mediante `worksheet.SparklineGroups[i]`.
- `Sparkline` y el operador de indexación `group.Sparklines[0]` permiten obtener el minigráfico individual de un grupo. Como cada grupo del ejemplo contiene exactamente un minigráfico, no es necesario usar un bucle `foreach`.
- `Sparkline.ToImage(ImageOrPrintOptions)` es el método de generación de imágenes que devuelve directamente una imagen del minigráfico en forma de vector de bytes `Vector<uint8_t>`.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades de `HtmlSaveOptions` más utilizadas cuando se generan informes de una sola página.
- `ImageOrPrintOptions.ImageType` se encuentra en el namespace `Aspose.Cells.Drawing` y permite seleccionar el formato de imagen, por ejemplo, `ImageType.Png`, utilizado al generar una imagen con `ToImage` y al imprimir hojas de cálculo como imágenes.

## **Artículos relacionados**
- [Minigráficos en Aspose.Cells for C++](/cells/es/cpp/sparkline/)
- [Insertar una imagen en una celda](/cells/es/cpp/inserting-an-image-into-a-cell/)
- [Renderizado de una matriz de una sola celda mediante SmartMarker | Aspose.Cells for C++](/cells/es/cpp/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}