---
title: Hitta och uppdatera de inbäddade eller barnpivot tabellerna för en föräldrapivot tabell med C++
linktitle: Hitta och uppdatera inbäddade eller barnpivot tabeller
type: docs
weight: 60
url: /sv/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Lär dig hur man hittar och uppdaterar inbäddade eller barnpivot tabeller av en föräldrapivot tabell med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland använder en pivottabell en annan pivottabell som datakälla, så det kallas en underordnad pivottabell eller inbäddad pivottabell. Du kan hitta de underordnade pivottablerna i en föräldrapivottabell med hjälp av [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/) metoden.

## **Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen**

Följande kod laddar den [prov-Eexcelfilen](61767747.xlsx) som innehåller tre pivottabeller. De två nedre pivottablerna är barn till den ovanstående pivottabellen som visas i denna skärmdump. Koden hittar de underordnade pivottablerna med hjälp av [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/) metoden och uppdaterar dem en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

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
