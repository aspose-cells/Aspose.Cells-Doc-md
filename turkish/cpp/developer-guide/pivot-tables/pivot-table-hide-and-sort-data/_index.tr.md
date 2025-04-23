---
title: C++ ile Pivot Tabloda Veri Gizleme ve Sıralama
linktitle: Pivot Tablo Veri Gizleme ve Sıralama
type: docs
weight: 120
url: /tr/cpp/pivot-table-hide-and-sort-data/
description: Aspose.Cells kullanarak pivot tablolarında veri gizleme ve sıralama yapmayı nasıl öğrenebilirsiniz.
---

## **Pivot Tablo Veri Gizleme ve Sıralama**
Aspose.Cells, özet tabloda verilerin gizlenmesini ve sıralanmasını destekler. Aşağıdaki kod parçacığı, Puan sütununu azalan sıraya göre sıralayarak ve ardından 60'tan küçük bir puanı olan satırları gizleyerek bu özelliği gösterir.

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

 Kod örneğinde kullanılan kaynak ve çıktı Excel dosyaları referans olması için eklenmiştir.

[Kaynak Dosyası](96928093.xlsx)

[Çıktı Dosyası](96928094.xlsx)
