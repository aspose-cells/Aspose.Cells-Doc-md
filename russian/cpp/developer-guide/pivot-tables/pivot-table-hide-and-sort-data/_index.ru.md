---
title: Скрытие и сортировка данных сводной таблицы с помощью C++
linktitle: Скрытие и сортировка данных сводной таблицы
type: docs
weight: 120
url: /ru/cpp/pivot-table-hide-and-sort-data/
description: Узнайте, как скрывать и сортировать данные в сводных таблицах с помощью Aspose.Cells и C++.
---

## **Скрытие и сортировка данных в сводной таблице**
Aspose.Cells поддерживает скрытие и сортировку данных в сводной таблице. В следующем фрагменте кода демонстрируется эта функция путем сортировки столбца Score по убыванию, а затем скрытия строк с оценкой менее 60.

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

Исходные и итоговые файлы Excel, используемые в примере кода, прикреплены для справки.

[Исходный файл](96928093.xlsx)

[Выходной файл](96928094.xlsx)
{{< app/cells/assistant language="cpp" >}}
