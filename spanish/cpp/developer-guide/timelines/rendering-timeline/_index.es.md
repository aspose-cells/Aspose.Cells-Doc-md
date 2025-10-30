---
title: Renderización de Línea de Tiempo con C++
type: docs
weight: 40
url: /es/cpp/rendering-timeline/
description: Gestiona cronogramas de archivos de Excel con Aspose.Cells con C++.
keywords: Renderización de línea de tiempo sin Office 2013, Office 2016, Office 2019 y Office 365
---

## **Escenarios de uso posibles**
Aspose.Cells admite la renderización de la forma de línea de tiempo sin usar Office 2013, Office 2016, Office 2019 y Office 365. Si convierte su hoja de cálculo en una imagen o guarda su libro de trabajo en formatos PDF o HTML, verá que las líneas de tiempo se renderizan correctamente.

## **Renderización de Línea de tiempo**
El siguiente código de muestra carga el [archivo de Excel de muestra](input.xlsx) que contiene una línea de tiempo existente. Obtenga el objeto de forma según el nombre de la línea de tiempo y luego renderícelo en una imagen a través del método Shape.ToImage(). La imagen resultante es la [imagen de salida](out.png) que muestra la línea de tiempo renderizada. Como puede ver, la línea de tiempo se ha renderizado correctamente y se ve igual que en el archivo de Excel de muestra.

![todo:image_alt_text](out.png)
### **Código de muestra**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
