---
title: Ocultar y ordenar datos en tablas dinámicas con C++
linktitle: Ocultar y ordenar datos en tablas dinámicas
type: docs
weight: 120
url: /es/cpp/pivot-table-hide-and-sort-data/
description: Aprenda cómo ocultar y ordenar datos en tablas dinámicas usando Aspose.Cells con C++.
---

## **Ocultar y ordenar datos en tablas dinámicas**
Aspose.Cells admite ocultar y ordenar datos en la tabla dinámica. El siguiente fragmento de código demuestra esta característica ordenando la columna de Puntuación en orden descendente y luego ocultando las filas con una puntuación inferior a 60.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"PivotTableHideAndSortSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    CellArea dataBodyRange = pivotTable.GetDataBodyRange();
    int currentRow = 3;
    int rowsUsed = dataBodyRange.EndRow;

    // Sorting score in descending order
    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Hiding rows with score less than 60
    while (currentRow < rowsUsed)
    {
        Cell cell = worksheet.GetCells().Get(currentRow, 1);
        double score = cell.GetDoubleValue();
        if (score < 60)
        {
            worksheet.GetCells().HideRow(currentRow);
        }
        currentRow++;
    }

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the Excel file
    workbook.Save(outDir + u"PivotTableHideAndSort_out.xlsx");

    std::cout << "Pivot table hide and sort completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

Los archivos de Excel de origen y salida utilizados en el fragmento de código están adjuntos como referencia.

[Archivo de origen](96928093.xlsx)

[Archivo de salida](96928094.xlsx)
