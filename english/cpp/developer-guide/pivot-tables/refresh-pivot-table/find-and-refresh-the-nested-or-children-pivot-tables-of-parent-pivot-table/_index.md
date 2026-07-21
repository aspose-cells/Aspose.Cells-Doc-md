---
title: Find and Refresh the Nested or Child Pivot Tables of a Parent Pivot Table with C++
linktitle: Find and Refresh Nested or Child Pivot Tables
type: docs
weight: 60
url: /cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Learn how to find and refresh nested or child pivot tables of a parent pivot table using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, one pivot table uses another pivot table as a data source, so it is called a child pivot table or nested pivot table. You can find the child pivot tables of a parent pivot table using the **[PivotTable::GetChildren()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/)** method.

## **Find and Refresh the Nested or Child Pivot Tables of a Parent Pivot Table**

The following sample code loads the [sample Excel file](61767747.xlsx) that contains three pivot tables. The bottom two pivot tables are children of the above pivot table, as shown in this screenshot. The code finds the child pivot tables using the **[PivotTable::GetChildren()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/)** method and then refreshes them one by one.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Sample Code**

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

    // Refresh all the child pivot tables
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
