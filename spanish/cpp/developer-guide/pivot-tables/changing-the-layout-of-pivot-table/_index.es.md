---
title: Cambiar el diseño de la tabla dinámica con C++
linktitle: Cambiando el Diseño de la Tabla Dinámica
type: docs
weight: 10
url: /es/cpp/changing-the-layout-of-pivot-table/
description: Aprende cómo cambiar el diseño de una tabla dinámica en formas Compacta, Esquema y Tabular usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel permite cambiar el diseño de la tabla dinámica usando los comandos *PivotTable Tools > Design > Report Layout*. Puedes cambiar el diseño en estas tres formas:

- Mostrar en Forma Compacta
- Mostrar en Forma de Esquema
- Mostrar en forma tabular

Aspose.Cells también proporciona [**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showincompactform/), [**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showinoutlineform/) y [**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showintabularform/) métodos para cambiar el diseño de la tabla dinámica en estas tres formas.

{{% /alert %}}

El siguiente ejemplo de código primero muestra la Tabla Dinámica en **Forma Compacta**, luego en **Forma en Esquema** y, finalmente, en **Forma en Tabla**.

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
    U16String inputFilePath = srcDir + u"pivotTable_sample.xlsx";

    // Create workbook object from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // 1 - Show the pivot table in compact form
    pivotTable.ShowInCompactForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"CompactForm_out.xlsx");

    // 2 - Show the pivot table in outline form
    pivotTable.ShowInOutlineForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"OutlineForm_out.xlsx");

    // 3 - Show the pivot table in tabular form
    pivotTable.ShowInTabularForm();

    // Refresh the pivot table
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the output
    workbook.Save(outDir + u"TabularForm_out.xlsx");

    std::cout << "Pivot table forms saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
