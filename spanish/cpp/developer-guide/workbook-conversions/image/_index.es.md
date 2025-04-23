---
title: Convertir Excel en Imagen con C++
linktitle: Convertir Excel a Imagen
type: docs
weight: 300
url: /es/cpp/convert-excel-to-image/
description: Aprende a convertir hojas de cálculo de Excel en imágenes, incluyendo formatos TIFF y SVG, usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells le permite exportar una hoja de cálculo del libro y convertirla a diferentes formatos. Este artículo explica cómo convertir una hoja de cálculo a diferentes formatos.

{{% /alert %}}

## Convirtiendo el libro a TIFF

Un archivo de Excel puede contener varias hojas con múltiples páginas. [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) permite convertir Excel a TIFF con múltiples páginas. Además, puedes controlar varias opciones para TIFF, como [Compresión](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Resolución([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

El siguiente fragmento de código muestra cómo convertir Excel a TIFF con múltiples páginas. Se adjuntan el [archivo de Excel de origen](workbook-to-tiff-with-mulitiple-pages.xlsx) y la [imagen TIFF generada](workbook-to-tiff-with-mulitiple-pages.tiff) para tu referencia.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Conversión de hoja de cálculo a imagen**

Las hojas de cálculo contienen datos que quieres analizar. Por ejemplo, una hoja de cálculo puede contener parámetros, totales, porcentajes, excepciones y cálculos.

Como desarrollador, es posible que necesites presentar hojas de cálculo como imágenes. Por ejemplo, es posible que necesites utilizar una imagen de una hoja de cálculo en una aplicación o página web. Es posible que desees insertar una imagen en un documento de Microsoft Word, un archivo PDF, una presentación de PowerPoint u otro tipo de documento. En resumen, querrás una hoja de cálculo renderizada como una imagen para poder utilizarla en otro lugar.

Aspose.Cells soporta convertir hojas de cálculo de Excel en imágenes. Para usar esta función, necesitas importar el espacio de nombres [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) en tu programa o proyecto. Tiene varias clases útiles para renderizado e impresión, por ejemplo [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), y otras.

La clase [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) representa una hoja de cálculo para renderizar como imágenes. Tiene un método sobrecargado, [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), que puede convertir una hoja en archivos de imagen con diferentes atributos u opciones. Devuelve un objeto `System.Drawing.Bitmap` y puedes guardar un archivo de imagen en disco o en flujo. Se soportan varios formatos de imagen, como BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

El siguiente fragmento de código muestra cómo convertir una hoja de cálculo en un archivo de Excel a un archivo de imagen.

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Actualmente, la API para convertir hojas de cálculo en imágenes no admite gráficos de burbujas 3D.

{{% /alert %}}

## **Conversión de hoja de cálculo a SVG**

SVG significa Gráficos Vectoriales Escalables. SVG es una especificación basada en estándares XML para gráficos vectoriales bidimensionales. Es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

Aspose.Cells for C++ ha podido convertir hojas de cálculo en imágenes SVG desde la versión 7.1.0. El siguiente fragmento de código muestra cómo convertir una hoja de un archivo Excel en un archivo de imagen SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Convertir un gráfico de Excel a imagen](/cells/es/cpp/convert-an-excel-chart-to-image/)
- [Convertir Gráfico a Imagen en Formato SVG](/cells/es/cpp/converting-chart-to-image-in-svg-format/)
- [Exportar gráfico a SVG con atributo viewBox](/cells/es/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Seguir el progreso de conversión de Excel a TIFF](/cells/es/cpp/track-conversion-progress-of-excel-to-tiff/)
