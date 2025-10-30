---
title: Formatear Segmentador con C++
linktitle: Formato de filtro
type: docs
weight: 20
url: /es/cpp/formatting-slicer/
description: Formatee segmentadores en Microsoft Excel usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Puede formatear el segmentador en Microsoft Excel configurando su número de columnas o su estilo, etc. Aspose.Cells también le permite hacer esto usando las propiedades [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/) y [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/).

## ** Formatear rebanador**

Por favor, vea el siguiente código; carga el [archivo de Excel de muestra](67338473.xlsx) que contiene un segmentador. Accede al segmentador y establece su número de columnas y tipo de estilo y lo guarda como [archivo de Excel de salida](67338474.xlsx). La captura de pantalla muestra cómo se ve el segmentador después de la ejecución del código de muestra.

![todo:image_alt_text](formatting-slicer_1.png)

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
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
