---
title: 用 C++ 隐藏和排序数据透视表中的数据
linktitle: 隐藏和排序数据透视表中的数据
type: docs
weight: 120
url: /zh/cpp/pivot-table-hide-and-sort-data/
description: 学习如何使用 Aspose.Cells 和 C++ 在数据透视表中隐藏和排序数据。
---

## **隐藏和排序数据透视表中的数据**
Aspose.Cells支持在数据透视表中隐藏和排序数据。以下代码片段演示了通过按得分列进行降序排序，然后隐藏得分小于60的行的功能。

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

代码示例中使用的源 Excel 文件和输出文件已附在文档中供参考。

[源文件](96928093.xlsx)

[输出文件](96928094.xlsx)
{{< app/cells/assistant language="cpp" >}}
