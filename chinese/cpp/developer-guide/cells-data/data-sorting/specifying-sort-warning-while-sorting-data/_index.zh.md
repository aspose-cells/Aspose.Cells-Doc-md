---
title: 用C++在排序数据时指定排序警告
linktitle: 在排序数据时指定排序警告
type: docs
weight: 140
url: /zh/cpp/specifying-sort-warning-while-sorting-data/
description: 学习如何使用Aspose.Cells for C++ API在排序数据时指定排序警告。
keywords: 在对数据进行排序时添加排序警告，设置排序警告，在对数据进行排序时选择排序警告。
---

## **可能的使用场景**

请考虑这段文本数据，即{11, 111, 22}。此文本数据被排序，因为在文本方面，111排在22前面。但是，如果您想将这些数据不作为文本而作为数字进行排序，那么它将变为{11, 22, 111}，因为从数字角度看，111在22之后。Aspose.Cells提供了{0}属性来解决这个问题。请将此属性设置为**true**，您的文本数据将作为数值数据进行排序。以下截图展示了当类似数值数据的文本数据排序时，Microsoft Excel显示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **示例代码**

下面的示例代码说明了如何使用前面解释的[**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/)属性。有关更多帮助，请查看其[示例Excel文件](43352075.xlsx)和[输出Excel文件](43352076.xlsx)。

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
