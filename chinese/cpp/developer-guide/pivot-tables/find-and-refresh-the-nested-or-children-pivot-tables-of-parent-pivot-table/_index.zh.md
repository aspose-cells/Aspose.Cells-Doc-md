---
title: 用 C++ 查找并刷新父数据透视表的嵌套或子数据透视表
linktitle: 查找并刷新嵌套或子数据透视表
type: docs
weight: 60
url: /zh/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: 学习如何使用 Aspose.Cells for C++ 查找和刷新父数据透视表的嵌套或子数据透视表。
---

## **可能的使用场景**

有时，一个数据透视表使用另一个数据透视表作为数据源，因此被称为子数据透视表或嵌套数据透视表。您可以使用[**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/)方法找到父数据透视表的子数据透视表。

## **查找并刷新父数据透视表的嵌套或子数据透视表**

以下是加载包含三个数据透视表的[样本Excel文件](61767747.xlsx)的示例代码。下面两个数据透视表是上面数据透视表的子级，如此屏幕截图所示。代码使用[**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/)方法查找子级数据透视表，然后逐个刷新它们。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath = u"sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access third pivot table
    PivotTable ptParent = ws.GetPivotTables().Get(2);

    // Access the children of the parent pivot table
    Vector<PivotTable> ptChildren = ptParent.GetChildren();

    // Refresh all the children pivot table
    int count = ptChildren.GetLength();
    for (int idx = 0; idx < count; idx++)
    {
        // Access the child pivot table
        PivotTable ptChild = ptChildren[idx];

        // Refresh the child pivot table
        ptChild.RefreshData();
        ptChild.CalculateData();
    }

    std::cout << "Children pivot tables refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
