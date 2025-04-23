---
title: Actualizar y calcular tablas dinámicas con elementos calculados usando C++
linktitle: Actualizar y Calcular tabla dinámica con elementos calculados
type: docs
weight: 40
url: /es/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Actualizar y calcular tablas dinámicas con elementos calculados usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Ahora Aspose.Cells admite refrescar y calcular tabla dinámica con elementos calculados. Utilice [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) y [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) como de costumbre para realizar esta función.

{{% /alert %}}

## **Actualizar y Calcular Tabla Dinámica con Elementos Calculados**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5115238.xlsx) que contiene una tabla dinámica con tres elementos calculados como "add", "div", "div2". Primero cambiamos el valor de la celda D2 a 20 y luego actualizamos y calculamos la tabla dinámica usando las API de Aspose.Cells y guardamos el libro en formato PDF. Los resultados en el [PDF de salida](5115229.pdf) muestran que Aspose.Cells actualizó y calculó la tabla dinámica con elementos calculados con éxito. Puede verificarlo usando Microsoft Excel ingresando manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica mediante la tecla de método abreviado Alt+F5 o haciendo clic en el botón de actualización de la tabla dinámica.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
