---
title: إخفاء وفرز البيانات في جدول Pivot باستخدام C++
linktitle: إخفاء وفرز البيانات في جدول Pivot
type: docs
weight: 120
url: /ar/cpp/pivot-table-hide-and-sort-data/
description: تعلم كيفية إخفاء وفرز البيانات في جداول Pivot باستخدام Aspose.Cells مع C++.
---

## **إخفاء وفرز البيانات في جدول Pivot**
يدعم Aspose.Cells إخفاء البيانات وفرزها في جدول البيانات المحوري. يوضح مقتطف الكود التالي هذه الميزة من خلال فرز عمود النقاط بترتيب تنازلي ثم إخفاء الصفوف التي لديها نقاط أقل من 60.

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

الملفات المصدرية والإخراجية لملف إكسل المستخدم في مقتطف الكود مرفقة للرجوع إليها.

[ملف المصدر](96928093.xlsx)

[ملف الناتج](96928094.xlsx)
{{< app/cells/assistant language="cpp" >}}
