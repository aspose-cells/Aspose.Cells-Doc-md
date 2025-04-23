---
title: Nascondere e ordinare i dati nella tabella pivot con C++
linktitle: Nascondi e ordina i dati nella tabella pivot
type: docs
weight: 120
url: /it/cpp/pivot-table-hide-and-sort-data/
description: Impara come nascondere e ordinare i dati nelle tabelle pivot usando Aspose.Cells con C++.
---

## **Nascondi e ordina i dati nella tabella pivot**
Aspose.Cells supporta la possibilità di nascondere e ordinare i dati nella tabella pivot. Il seguente frammento di codice dimostra questa funzionalità ordinando la colonna Score in ordine decrescente e quindi nascondendo le righe con un punteggio inferiore a 60.

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

 I file Excel di origine e di output usati nel frammento di codice sono allegati per riferimento.

[File di origine](96928093.xlsx)

[File di output](96928094.xlsx)
