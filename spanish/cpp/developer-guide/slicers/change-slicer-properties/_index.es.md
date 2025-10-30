---
title: Cambiar propiedades del Segmentador con C++
linktitle: Cambiar propiedades del rebanador
type: docs
weight: 70
url: /es/cpp/change-slicer-properties/
description: Cambia las propiedades de un segmentador en archivos de Excel usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Puede haber situaciones en las que desee cambiar las propiedades del filtro, como la ubicación o la altura de la fila. Aspose.Cells le brinda la opción de actualizar estas propiedades.

## **Cambiar propiedades del rebanador**

Por favor, consulta el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](sampleCreateSlicerToExcelTable.xlsx) que contiene una tabla. Luego, crea el rebanador basado en la primera columna y cambia sus propiedades como altura de fila, ancho, es imprimible, título, etc. Guarda el libro de trabajo como [outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
