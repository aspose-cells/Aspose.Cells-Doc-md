---
title: Pivot Table Hide and Sort Data with C++
linktitle: Pivot Table Hide and Sort Data
type: docs
weight: 120
url: /cpp/pivot-table-hide-and-sort-data/
description: Learn how to hide and sort data in pivot tables using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Pivot Table Hide and Sort Data**
Aspose.Cells supports hiding and sorting data in pivot tables. The following code snippet demonstrates this feature by sorting the score column in descending order and then hiding the rows with a score less than 60.

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

The source and output Excel files used in the code snippet are attached for reference.

[Source File](96928093.xlsx)

[Output File](96928094.xlsx)
{{< app/cells/assistant language="cpp" >}}
