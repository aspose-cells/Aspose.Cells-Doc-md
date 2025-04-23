---
title: Desactivar las cintas de la tabla dinámica con C++
linktitle: Desactivar los paneles de control de la tabla dinámica
type: docs
weight: 90
url: /es/cpp/disable-pivot-table-ribbons/
description: Aprende cómo desactivar las cintas de la tabla dinámica en archivos de Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Los informes basados en tablas dinámicas son útiles, pero propensos a errores si los usuarios destinatarios no tienen conocimientos detallados de Excel para configurarlos. En estas circunstancias, las organizaciones querrán restringir a los usuarios la capacidad de modificar estos informes. Funciones comunes de la tabla dinámica, como agregar filtros adicionales, segmentos, campos o cambiar el orden de ciertos elementos en el informe, generalmente no se recomiendan para todos los usuarios. Por otro lado, estos usuarios también deberían poder actualizar el informe y usar filtros o segmentos existentes. Aspose.Cells ha proporcionado esta capacidad a los desarrolladores para restringir a los usuarios la modificación de estos informes durante su creación. Para ello, Excel ofrece una función para desactivar la cinta de la tabla dinámica, y la misma opción la ofrece Aspose.Cells. Los desarrolladores pueden desactivar la cinta que contiene controles para modificar estos informes.

{{% /alert %}}

## **Deshabilitar la cinta de opciones de la tabla dinámica utilizando PivotTable.EnableWizard**

El siguiente código demuestra esta función accediendo a una tabla dinámica de una hoja y luego estableciendo [**GetEnableWizard()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getenablewizard/) en **falso**. Un archivo de ejemplo de tabla dinámica se puede descargar desde este [enlace](pivot_table_test.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
