---
title: C++によるピボットテーブルの非表示とデータの並べ替え
linktitle: ピボットテーブルの非表示とデータの並べ替え
type: docs
weight: 120
url: /ja/cpp/pivot-table-hide-and-sort-data/
description: Aspose.Cellsを使用してピボットテーブルのデータの非表示と並べ替えを行う方法を学びます。
---

## ** ピボットテーブルの非表示とデータの並べ替え**
Aspose.Cellsは、ピボットテーブルでデータの非表示やソートをサポートしています。以下のコードスニペットは、スコア列を降順でソートし、スコアが60未満の行を非表示にする機能を示しています。

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

 コードスニペットで使用されるソースと出力のExcelファイルは添付されており、参考にしてください。

[ソースファイル](96928093.xlsx)

[出力ファイル](96928094.xlsx)
{{< app/cells/assistant language="cpp" >}}
