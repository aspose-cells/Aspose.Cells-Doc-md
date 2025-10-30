---
title: Implementar tamaño de papel personalizado de la hoja de trabajo para renderizado con C++
linktitle: Implementar tamaño de papel personalizado de la hoja de cálculo para la representación
type: docs
weight: 70
url: /es/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Este artículo explica cómo usar la API de C++ para establecer tamaño de papel personalizado en las hojas de trabajo deseadas al renderizar archivos de Excel a formato PDF de forma programática.
keywords: establecer tamaño de papel personalizado al convertir Excel a PDF con C++
---

## **Escenarios de uso posibles**

 No hay una opción directa disponible para crear tamaños de papel personalizados en MS Excel; sin embargo, puedes establecer un tamaño de papel personalizado en las hojas de trabajo deseadas al renderizar archivos de Excel a formato PDF. Este documento explica cómo establecer un tamaño de papel personalizado en una hoja de trabajo usando las API de Aspose.Cells.

## **Implementar Tamaño de Papel Personalizado de la Hoja de Cálculo para el Renderizado**

 Aspose.Cells te permite implementar el tamaño de papel deseado de la hoja de trabajo. Puedes usar el método [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/) de la clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) para especificar un tamaño de página personalizado. El siguiente código de ejemplo ilustra cómo especificar un tamaño de papel personalizado para la primera hoja del libro. También mira el [PDF de salida](45056028.pdf) generado con el siguiente código como referencia.

## **Captura de pantalla**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
