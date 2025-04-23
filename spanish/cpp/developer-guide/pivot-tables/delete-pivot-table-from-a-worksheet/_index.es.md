---
title: Eliminar tabla dinámica de una hoja de trabajo con C++
linktitle: Eliminar tabla dinámica
type: docs
weight: 60
url: /es/cpp/delete-pivot-table-from-a-worksheet/
description: Código C++ para eliminar la tabla dinámica en hojas de Excel usando Aspose.Cells.
keywords: c++ elimina la tabla dinámica de la hoja de trabajo, c++ elimina la tabla dinámica de Excel, cómo eliminar la tabla dinámica con c++, elimina la tabla dinámica con c++, elimina la tabla dinámica de Excel con c++, c++ eliminar tabla dinámica, c++ eliminar tabla dinámica, elimina tabla dinámica, elimina la tabla dinámica, cómo eliminar la tabla dinámica
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una función para eliminar o quitar la Tabla Dinámica de una hoja de cálculo. Puede eliminar la tabla dinámica usando el objeto de tabla dinámica o la posición de la tabla dinámica. Utilice el método [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) para eliminar la tabla dinámica usando el objeto de tabla dinámica y el método [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) para eliminar el objeto de tabla dinámica usando su posición dentro de la colección de tablas dinámicas.

{{% /alert %}}

El siguiente código de ejemplo elimina dos tablas dinámicas de la hoja de trabajo. Primero elimina la tabla dinámica usando [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) método y luego elimina otra usando [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) método.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
