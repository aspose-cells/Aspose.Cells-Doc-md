---
title: Quitar Segmentador con C++
linktitle: Eliminar filtro
type: docs
weight: 30
url: /es/cpp/removing-slicer/
description: Aprenda cómo quitar segmentadores en archivos de Excel programáticamente usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Si desea quitar un segmentador en Microsoft Excel, simplemente selecciónelo y presione el botón *Eliminar*. De manera similar, si desea quitarlo usando la API de Aspose.Cells programáticamente, utilice el método [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/). Esto eliminará el segmentador de la hoja de cálculo.

## **Eliminar rebanador**

El siguiente código muestra el [archivo de Excel de muestra](67338478.xlsx) que contiene un slicer existente. Accede a los slicers y luego lo elimina. Finalmente, guarda el libro de trabajo como [archivo de Excel de salida](67338477.xlsx). La siguiente captura de pantalla muestra el slicer que se eliminará después de la ejecución del código de muestra.

![todo:image_alt_text](removing-slicer_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
