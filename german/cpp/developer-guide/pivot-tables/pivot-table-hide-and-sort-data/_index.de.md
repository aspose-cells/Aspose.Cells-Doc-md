---
title: Pivot Tabelle verbergen und Daten sortieren mit C++
linktitle: Pivot Tabelle verbergen und Daten sortieren
type: docs
weight: 120
url: /de/cpp/pivot-table-hide-and-sort-data/
description: Erfahren Sie, wie Sie Daten in Pivot Tabellen mit Aspose.Cells und C++ verbergen und sortieren.
---

## **Pivot-Tabelle verbergen und Daten sortieren**
Aspose.Cells unterstützt das Ausblenden und Sortieren von Daten in der Pivot-Tabelle. Der folgende Codeausschnitt demonstriert diese Funktion, indem die Spalte Score absteigend sortiert und dann die Zeilen mit einem Wert von weniger als 60 ausgeblendet werden.

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

Die in dem Codeausschnitt verwendeten Quell- und Ausgabedateien im Excel-Format sind zur Referenz beigefügt.

[Quelldatei](96928093.xlsx)

[Ausgabedatei](96928094.xlsx)
{{< app/cells/assistant language="cpp" >}}
