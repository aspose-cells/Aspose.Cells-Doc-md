---
title: Get External Connection Data Source of Pivot Table with C++
linktitle: Get External Connection Data Source of Pivot Table
type: docs
weight: 150
url: /cpp/get-external-connection-data-source-of-pivot-table/
description: Learn how to retrieve the external connection data source of a pivot table using Aspose.Cells for C++.
---

## **Get External Connection Data Source of Pivot Table**

Aspose.Cells provides the ability to get the external connection data source of the pivot table. For this, the API provides the [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) property of the [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) class. The [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) property returns the [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/) object. The following code snippet demonstrates the use of the [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) property to get the external connection data source of the pivot table.

## Sample Code

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample file
    Workbook workbook(srcDir + u"SamplePivotTableExternalConnection.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Print External Connection Details
    std::cout << "External Connection Data Source" << std::endl;

    // Get the source data connections
    Vector<ExternalConnection> connections = pivotTable.GetSourceDataConnections();

    // Iterate through each connection and print details
    for (const auto& conn : connections)
    {
        std::cout << "Name: " << conn.GetName().ToUtf8() << std::endl;
        std::cout << "Type: " << static_cast<int>(conn.GetSourceType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

The source file used in the code snippet is attached for reference.

[Source File](104398862.xlsx)