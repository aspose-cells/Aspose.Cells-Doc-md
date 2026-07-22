---
title: Convertir minigráficos a imagen y HTML en Aspose.Cells for C++
linktitle: Convert Sparkline to Image and HTML
description: Aprenda a renderizar minigráficos de Aspose.Cells como imágenes independientes para incrustar en celdas y exportar hojas de cálculo con minigráficos a HTML usando HtmlSaveOptions.
keywords: Aspose.Cells, C++, minigráfico, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, renderizar minigráfico, convertir minigráfico a imagen, exportar minigráfico a HTML
type: docs
weight: 120
url: /es/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Los minigráficos son gráficos en miniatura colocados dentro de las celdas de la hoja de cálculo. Aspose.Cells le permite extraer cada minigráfico como una imagen independiente (para incrustarlo en otra celda o en un informe externo) y también exportar toda la hoja de cálculo con minigráficos a HTML para su distribución en el navegador. La propiedad `Cell.EmbeddedImage` utilizada en este artículo está disponible en **Aspose.Cells 26.5 y posteriores**.
{{% /alert %}}

## **Introducción**

Los minigráficos son una forma compacta de visualizar tendencias directamente dentro de una hoja de cálculo. Mientras que los usuarios de Excel los ven en su lugar, muchos escenarios del mundo real requieren que un minigráfico salga de la celda — por ejemplo, para ser incrustado en una celda diferente como una imagen estática, adjunto a un correo electrónico automatizado, o renderizado como parte de un informe HTML publicado en la web.

Aspose.Cells admite ambas operaciones. El método `Sparkline.ToImage` renderiza un minigráfico individual a un flujo, y los bytes resultantes pueden asignarse a `Cell.EmbeddedImage` de modo que la imagen se almacene dentro de una sola celda del libro de trabajo. Por separado, `HtmlSaveOptions` le permite convertir el libro de trabajo completo — minigráficos y todo — en un archivo HTML autónomo. Este artículo recorre ambos flujos de trabajo de extremo a extremo.

## **Flujo de trabajo 1 — Renderizar minigráficos a imágenes e incrustarlos en celdas**

En este flujo de trabajo construirá una hoja de cálculo que contiene un pequeño rango de valores de origen, adjuntará tres grupos de minigráficos diferentes (Línea, Columna y Apilado/Win-Loss) a ese rango, renderizará cada grupo como un PNG, y escribirá esos bytes PNG en celdas adyacentes como imágenes incrustadas. El resultado final es un único archivo `.xlsx` que contiene tanto los minigráficos activos como sus contrapartes de imagen renderizadas.

### **Instrucciones paso a paso**

1. Defina un directorio de trabajo y asegúrese de que exista en disco.
2. Cree un nuevo `Workbook` y obtenga una referencia a la primera `Worksheet`.
3. Rellene las celdas `A1` a `E1` con cinco valores numéricos de muestra (por ejemplo, ventas diarias o lecturas de temperatura).
4. Agregue tres objetos `SparklineGroup` a la hoja de cálculo llamando a `worksheet.SparklineGroups.Add(...)`:
   - Un grupo `SparklineType.Line` anclado en `F1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Column` anclado en `G1`, con rango de datos `A1:E1`.
   - Un grupo `SparklineType.Stacked` (win/loss) anclado en `H1`, con rango de datos `A1:E1`.
5. Construya una instancia de `ImageOrPrintOptions` y establezca su `ImageType` a `ImageType.Png` para que cada minigráfico se renderice como un PNG transparente.
6. Para cada uno de los tres grupos, renderice su único minigráfico usando `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, convierta el `MemoryStream` a un `Vector<uint8_t>`, y asigne el arreglo a `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage`, y `worksheet.Cells["H2"].EmbeddedImage` respectivamente.
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

El código anterior produce un libro de trabajo donde cada representación visual de un minigráfico se duplica en dos formas: el minigráfico nativo y activo anclado en la fila 1, y una imagen PNG estática incrustada directamente en una celda vecina en la fila 2. Debido a que las imágenes viven dentro del propio archivo, el libro de trabajo sigue siendo un único artefacto autónomo que puede ser enviado por correo electrónico o archivado sin romper las referencias de imagen incrustadas. Renderice cada grupo de minigráficos como un PNG, convierta el `MemoryStream` a un `Vector<uint8_t>`, y asigne el arreglo a la propiedad `EmbeddedImage` de la celda de destino — la asignación es lo que hace que la imagen sea parte del contenido almacenado de la celda.

{{% alert color="primary" %}}
Dado que cada grupo de minigráficos está anclado a una sola celda, puede acceder a él a través del indexador `group.Sparklines[0]` en lugar de enumerar con `foreach`. Esto mantiene corto el código de renderizado y coincide con el patrón típico de "un minigráfico por celda ancla". Almacenar los bytes de la imagen mediante `Cell.EmbeddedImage` requiere Aspose.Cells 26.5 o posterior.
{{% /alert %}}

## **Flujo de trabajo 2 — Exportar la hoja de cálculo con minigráficos a HTML**

Una vez que el libro de trabajo contiene minigráficos activos (y opcionalmente contrapartes de imágenes incrustadas), toda la hoja de cálculo puede ser publicada en la web guardándola como HTML. La clase `HtmlSaveOptions` expone los controles que necesita para controlar esta exportación; en este flujo de trabajo reutilizará el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 y lo convertirá en un documento HTML limpio de una sola página.

### **Instrucciones paso a paso**

1. Asegúrese de que el archivo `output_with_sparklines.xlsx` producido por el Flujo de trabajo 1 esté disponible en disco en su directorio de trabajo.
2. Cargue ese archivo en una nueva instancia de `Workbook`.
3. Cree una instancia de `HtmlSaveOptions` y establezca su propiedad `ExportActiveWorksheetOnly` a `true` para que el archivo HTML resultante contenga solo la hoja de cálculo activa en lugar de todo el libro de trabajo.
4. Llame a `workbook.Save("sparklines.html", htmlOptions)` para escribir la salida HTML en disco.

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

El código anterior toma el libro de trabajo con minigráficos del Flujo de trabajo 1 y lo convierte en un archivo HTML portátil. Los minigráficos se conservan como renderizaciones SVG o PNG en línea dentro del HTML generado, dependiendo del modo de exportación, para que los usuarios finales puedan ver las tendencias en cualquier navegador moderno sin necesidad de tener Excel instalado. Al establecer `ExportActiveWorksheetOnly` a `true`, evita publicar accidentalmente hojas ocultas o datos auxiliares — solo se exporta la hoja de cálculo actualmente visible para el usuario.

{{% alert color="primary" %}}
La clase `HtmlSaveOptions` ofrece propiedades adicionales para ajustar la salida, como `ExportHiddenWorksheet`, `ExportImagesAsBase64` y `Encoding`. Ajústelas según sea necesario para su destino de implementación.
{{% /alert %}}

## **Resumen de la API**

Los flujos de trabajo anteriores dependen de un pequeño conjunto de APIs de Aspose.Cells que trabajan juntas.

- `SparklineGroup` y el descriptor de acceso de colección `worksheet.SparklineGroups` se utilizan para declarar el tipo (Line, Column, Stacked), el rango de datos y la celda ancla para cada grupo de minigráficos. En este artículo cada grupo está anclado a una sola celda, por lo que se accede al grupo a través de `worksheet.SparklineGroups[i]`.
- `Sparkline` y el indexador `group.Sparklines[0]` devuelven el minigráfico individual dentro de un grupo. Dado que cada grupo en el ejemplo contiene exactamente un minigráfico, no se requiere un bucle `foreach`.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` es el método de renderizado que escribe una imagen del minigráfico en un `Stream` proporcionado. El método devuelve `void`; usted lee los bytes del flujo después de la llamada.
- `Cell.EmbeddedImage` es una propiedad `Vector<uint8_t>` que almacena una imagen dentro de una sola celda. Está disponible en **Aspose.Cells 26.5 y posteriores** y es la forma recomendada de devolver un minigráfico renderizado por `ToImage` al mismo libro de trabajo.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (un `bool`) restringe la exportación HTML a la hoja de cálculo activa. Es una de las propiedades más utilizadas de `HtmlSaveOptions` al generar informes de una sola página.
- `ImageOrPrintOptions.ImageType` reside en el espacio de nombres `Aspose.Cells.Drawing` y selecciona el formato de imagen (por ejemplo, `ImageType.Png`) utilizado al renderizar con `ToImage` y al imprimir hojas de cálculo a imágenes.

## **Artículos relacionados**

- [Sparklines in Aspose.Cells for C++](/cells/es/cpp/sparkline/)
- [Inserting an Image into a Cell](/cells/es/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/es/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}