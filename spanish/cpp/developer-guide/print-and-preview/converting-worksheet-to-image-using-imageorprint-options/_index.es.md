---
title: Convertir Hoja de cálculo a Imagen usando Opciones de Imagen o Impresión con C++
linktitle: Convertir Hoja de cálculo a Imagen
type: docs
weight: 90
url: /es/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Aprende cómo convertir una hoja de cálculo en un archivo de imagen y aplicar diferentes opciones de imagen e impresión usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Este documento está diseñado para proporcionar una comprensión detallada de cómo convertir una hoja de cálculo en un archivo de imagen y aplicar diferentes opciones de imagen e impresión para la imagen, como resolución, compresión TIFF, formato de imagen y calidad de página.

{{% /alert %}}

## **Guardar hojas de cálculo en imágenes - Diferentes enfoques**

A veces, puede necesitar presentar sus hojas de cálculo como una representación pictórica. Es posible que necesite presentar las imágenes de las hojas de cálculo en sus aplicaciones o páginas web, insertarlas en un documento de Word, un archivo PDF, una presentación de PowerPoint o usarlas en algún otro escenario. En pocas palabras, desea que una hoja de cálculo se renderice como una imagen para poder usarla en otro lugar. Aspose.Cells soporta convertir hojas de cálculo en archivos Excel en imágenes. Además, Aspose.Cells soporta configurar diferentes opciones como formato de imagen, resolución (vertical y horizontal), calidad de imagen y otras opciones de imagen e impresión.

Podría considerar la Automatización de Office, pero tiene sus propias desventajas. Hay varias razones y problemas involucrados, como seguridad, estabilidad, escalabilidad, velocidad, precio y funciones. En resumen, hay muchas razones, siendo la principal que Microsoft recomienda encarecidamente en contra de la automatización de Office desde soluciones de software.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio, realizar la conversión de una hoja de cálculo a una imagen utilizando diferentes opciones de imagen y impresión con unas pocas líneas de código simples usando la API Aspose.Cells.

Debe incluir el espacio de nombres [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) en su programa/proyecto. Tiene varias clases útiles, por ejemplo, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), etc.

La clase [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) representa una hoja de cálculo para renderizar imágenes de la hoja de cálculo. Tiene un método [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) sobrecargado que puede convertir directamente una hoja de cálculo en archivos de imagen especificados con sus atributos u opciones deseadas. Puede devolver un objeto bitmap y puede guardar un archivo de imagen en el disco/flujo. Se admiten varios formatos de imagen, como BMP, PNG, GIF, JPEG, TIFF, EMF, entre otros.

## **Uso de Aspose.Cells para convertir una hoja de cálculo en imagen usando opciones ImageOrPrint**

### **Creando un libro de trabajo plantilla en Microsoft Excel**

Creé un nuevo libro de trabajo en MS Excel y añadí algunos datos en la primera hoja de cálculo. Ahora convertiré la hoja de cálculo de la plantilla "Sheet1" en un archivo de imagen "SheetImage.tiff" y aplicaré diferentes opciones de imagen como resoluciones horizontal y vertical, TiffCompression, entre otras.

### **Descargar e instalar Aspose.Cells**

Primero, debe [descargar](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. Instálelo en su computadora de desarrollo. Todos los componentes de [Aspose](http://www.aspose.com/), cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.

### **Crear un proyecto**

Inicie Visual Studio y cree una nueva aplicación de consola. Este ejemplo mostrará una aplicación de consola en C++.

### **Agregar referencias**

Este proyecto usará Aspose.Cells. Por lo tanto, debe agregar una referencia al componente Aspose.Cells en su proyecto. Por ejemplo, agregue una referencia a `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib`.

### **Convertir hoja de cálculo en archivo de imagen**

```c++
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

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Opciones de conversión**

Es posible guardar páginas específicas como imagen. El siguiente código convierte la primera y segunda hoja de cálculo en un libro en imágenes JPG.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Conversión de Imagen usando WorkbookRender**

Una imagen TIFF puede contener más de un cuadro. Puede guardar toda la hoja de trabajo en una sola imagen TIFF con múltiples cuadros o páginas:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
