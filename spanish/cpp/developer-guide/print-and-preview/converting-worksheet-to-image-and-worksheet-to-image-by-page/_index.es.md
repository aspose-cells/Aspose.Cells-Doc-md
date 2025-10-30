---
title: Convertir Hoja de cálculo a Imagen y Hoja de cálculo a Imagen por Página con C++
linktitle: Convertir hoja de cálculo a imagen y hoja de cálculo a imagen por página
type: docs
weight: 80
url: /es/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: Aprende cómo convertir una hoja de cálculo a un archivo de imagen y una hoja de múltiples páginas a un archivo de imagen por página usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Este documento está diseñado para proporcionar a los desarrolladores una comprensión detallada de cómo convertir una hoja de cálculo a un archivo de imagen y una hoja con múltiples páginas a un archivo de imagen por página.

A veces, es posible que necesites presentar hojas de cálculo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Puedes necesitar insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint, o utilizarlas en otro escenario. Básicamente, quieres renderizar la hoja de cálculo como una imagen. Aspose.Cells admite la conversión de hojas de cálculo en archivos de imagen de Excel. Además, Aspose.Cells admite la conversión de un libro de trabajo a múltiples archivos de imagen, uno por página.

Podrías usar Office Automation para lograr esto, pero la automatización de Office tiene sus propios inconvenientes. Hay varias razones y problemas involucrados: por ejemplo, seguridad, estabilidad, escalabilidad/velocidad, precio y características. En resumen, hay muchas razones, pero la principal es que Microsoft mismo recomienda encarecidamente no usar Office Automation.

{{% /alert %}}

## **Usar Aspose.Cells para convertir hoja de cálculo a archivo de imagen**

Este artículo muestra cómo crear una aplicación de consola en Visual Studio, convertir una hoja de cálculo a una imagen y convertir una hoja de cálculo en una imagen para cada hoja de cálculo con algunas líneas de código simples utilizando la API de Aspose.Cells.

Necesitas incluir el espacio de nombres [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) en tu programa/proyecto. Tiene varias clases valiosas, como [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), y así sucesivamente. La clase [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) representa una hoja de cálculo para renderizar imágenes de la hoja y tiene un método [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) sobrecargado que puede convertir una hoja de cálculo en archivos de imagen directamente con cualquier atributo u opción configurada. Puede devolver un objeto `System.Drawing.Bitmap`, y puedes guardar un archivo de imagen en disco/flujo. Se admiten varios formatos de imagen, por ejemplo, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, y otros.

Este artículo explica cómo:

- Convertir una hoja de cálculo a una imagen
- Convertir cada página en una hoja de cálculo a una imagen

Esta tarea muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo de plantilla a un archivo de imagen.

### **Configurar Proyecto**

1. Primero, [descarga Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Instálalo en tu ordenador de desarrollo. Todos los componentes de [Aspose](http://www.aspose.com/) al ser instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos. Ahora inicia Visual Studio y crea una nueva aplicación de consola. Este ejemplo usa una aplicación de consola en C++. Añade una referencia a Aspose.Cells en el proyecto creado.

### **Convertir Hoja de Cálculo a Archivo de Imagen**

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook.xlsx** (1 hoja de cálculo). A continuación, convierte la hoja de cálculo Sheet1 del archivo de plantilla en un archivo de imagen llamado SheetImage.jpg.

A continuación se muestra el código utilizado por el componente para llevar a cabo la tarea. Convierte Sheet1 en **Testbook.xlsx** a un archivo de imagen para explicar lo sencilla que es esta conversión.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Usar Aspose.Cells para convertir hoja de cálculo a archivo de imagen por página**

Este ejemplo muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo que tiene varias páginas a un archivo de imagen por página.

### **Convertir hoja de cálculo en imagen por página**

Creé un nuevo libro de trabajo en Microsoft Excel y agregué algunos datos en la primera hoja de cálculo: **Testbook2.xlsx** (1 hoja de cálculo).

Ahora, convierte la hoja de cálculo del archivo de plantilla en archivos de imagen (un archivo por página). Como ya creé la aplicación de consola para realizar la tarea de copia, omitiré esos pasos de creación de la aplicación de consola y pasaré directamente a los pasos de conversión de la hoja de cálculo.

El siguiente es el código utilizado por el componente para realizar la tarea. Convierte la hoja Sheet1 en Testbook2.xlsx en archivos de imagen por página.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

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
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
