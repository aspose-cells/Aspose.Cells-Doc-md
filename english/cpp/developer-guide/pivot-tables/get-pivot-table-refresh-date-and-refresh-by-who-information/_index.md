---
title: Get Pivot Table refresh date and refresh by who information with C++
linktitle: Get Pivot Table Refresh Date and Refresh By Who Information
type: docs
weight: 100
url: /cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Learn how to fetch the refresh date and refresh by who information from a workbook using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Aspose.Cells now supports fetching the refresh date and refresh by who information from a workbook.

{{% /alert %}}

[**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) returns the date on which the PivotTable report was last refreshed. Similarly, [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) property returns the name of the user who refreshed the report last time. The following example demonstrates this feature, and the sample file can be downloaded from the following link.

[SourcePivotTable.xlsx](77496335.xlsx)

**Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from source excel file
    Workbook workbook(srcDir + u"sourcePivotTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Access pivot table refresh by who
    std::cout << "Pivot table refresh by who = " << pivotTable.GetRefreshedByWho().ToUtf8() << std::endl;

    // Access pivot table refresh date
    std::cout << "Pivot table refresh date = " << pivotTable.GetRefreshDate().ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```