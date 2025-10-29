---
title: 使用C++对列中的数据进行排序并使用自定义排序列表
linktitle: 在包含自定义排序列表的列中排序数据
type: docs
weight: 290
url: /zh/cpp/sort-data-in-column-with-custom-sort-list/
description: 学习如何使用Aspose.Cells for C++ API，将列中的数据根据自定义列表排序。
keywords: 使用自定义排序列表对列中的数据进行排序，使用自定义列表对数据进行排序。
---

## **可能的使用场景**

你可以使用自定义列表对列中的数据进行排序。这可以通过 [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) 方法完成。然而，此方法仅在自定义列表中的项目没有逗号时有效。如果项目中有逗号，比如 "USA,US"、"中国,CN" 等，则必须使用 [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) 方法。这里，最后一个参数不是字符串，而是字符串数组。

## **使用自定义排序列表对列中的数据进行排序**

以下示例代码说明了如何使用 [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) 方法通过自定义排序列表对数据进行排序。请查看此代码所用的 [示例Excel文件](50528327.xlsx) 和由其生成的 [输出Excel文件](50528328.xlsx)。下图显示了代码执行后对样本Excel文件的效果。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
