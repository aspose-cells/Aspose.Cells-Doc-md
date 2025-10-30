---
title: Renderizar Segmentador con C++
type: docs
weight: 40
url: /es/cpp/rendering-slicer/
description: Renderice segmentadores en archivos de Excel usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**
Aspose.Cells admite la representación del filtro. Si convierte su hoja de cálculo en una imagen o guarda su libro de trabajo en formatos PDF o HTML, verá que los filtros se representan correctamente.
## **Renderización de rebanador**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](67338479.xlsx) que contiene un segmentador existente. Convierte la hoja de cálculo en una imagen configurando el área de impresión que cubre solo el segmentador. La imagen siguiente es la [imagen de salida](67338480.png) que muestra el segmentador renderizado. Como puede ver, el segmentador ha sido renderizado correctamente y se ve igual que en el archivo de Excel de muestra.

![todo:image_alt_text](rendering-slicer_1)
## **Código de muestra**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
