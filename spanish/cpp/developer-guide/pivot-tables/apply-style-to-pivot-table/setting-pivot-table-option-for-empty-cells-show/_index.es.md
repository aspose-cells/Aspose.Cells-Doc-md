---
title: Configurando la opción de tabla dinámica  Mostrar para celdas vacías con C++
linktitle: Configurar Opción de tabla dinámica  Mostrar celdas vacías
type: docs
weight: 40
url: /es/cpp/setting-pivot-table-option-for-empty-cells-show/
description: Aprenda cómo configurar la opción "Para mostrar en celdas vacías" en tablas dinámicas usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Puede establecer diferentes opciones de tabla dinámica utilizando Aspose.Cells. Una de esas opciones es "Mostrar celdas vacías". Al establecer esta opción, todas las celdas vacías en una tabla dinámica se muestran como una cadena especificada.

{{% /alert %}}

## **Configuración de opción de tabla dinámica en Microsoft Excel**

Para encontrar y configurar esta opción en Microsoft Excel:

1. Seleccione una tabla dinámica y haga clic derecho.
2. Seleccione **Opciones de tabla dinámica**.
3. Seleccione la pestaña **Diseño y formato**.
4. Seleccione la opción **Mostrar celdas vacías** y especifique una cadena.

## **Configuración de opción de tabla dinámica utilizando Aspose.Cells**

Aspose.Cells proporciona las propiedades [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) y [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) para establecer la opción de tabla dinámica "Mostrar celdas vacías".

```c++
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
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Artículos relacionados

- [Dar formato a la tabla dinámica](/cells/es/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
