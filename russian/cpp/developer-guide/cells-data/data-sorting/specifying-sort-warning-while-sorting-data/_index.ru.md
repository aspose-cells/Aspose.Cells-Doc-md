---
title: Указание предупреждения сортировки при сортировке данных с помощью C++
linktitle: Указание предупреждения сортировки при сортировке данных
type: docs
weight: 140
url: /ru/cpp/specifying-sort-warning-while-sorting-data/
description: Узнайте, как указать предупреждение сортировки при сортировке данных с помощью API Aspose.Cells for C++.
keywords: Добавить предупреждение о сортировке при сортировке данных, установить предупреждение о сортировке при сортировке данных, выбрать предупреждение о сортировке при сортировке данных.
---

## **Возможные сценарии использования**

Пожалуйста, учтите этот текстовый набор, т.е. {11, 111, 22}. Этот текстовый набор сортируется, потому что в терминах текста 111 идет перед 22. Но, если вы хотите отсортировать этот набор не как текст, а как числа, то он станет {11, 22, 111}, потому что по числовому значению 111 идет после 22. Aspose.Cells предоставляет свойство {0} для решения этой проблемы. Пожалуйста, установите это свойство в **true**, и ваш текстовый набор будет сортироваться как числовые данные. Ниже показано предупреждение о сортировке, отображаемое Microsoft Excel, когда текстовые данные, похожие на числовые, сортируются.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Образец кода**

В следующем образце кода показано использование свойства [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/), как объяснено ранее. Пожалуйста, проверьте его [образцовый файл Excel](43352075.xlsx) и [выходной файл Excel](43352076.xlsx) для получения дополнительной помощи.

```c++
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

    // Create workbook
    Workbook workbook(srcDir + u"sampleSortAsNumber.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create cell area
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A20");

    // Create data sorter
    DataSorter sorter = workbook.GetDataSorter();

    // Find the index of column A
    int idx = CellsHelper::ColumnNameToIndex(u"A");

    // Add key in sorter for sorting in ascending order
    sorter.AddKey(idx, SortOrder::Ascending);
    sorter.SetSortAsNumber(true);

    // Perform sort
    sorter.Sort(worksheet.GetCells(), ca);

    // Save the output workbook
    workbook.Save(outDir + u"outputSortAsNumber.xlsx");

    std::cout << "Sorting completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
