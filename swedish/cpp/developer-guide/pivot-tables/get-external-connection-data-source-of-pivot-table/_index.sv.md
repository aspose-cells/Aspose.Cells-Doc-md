---
title: Hämta Extern anslutningsdatakälla för PivotTabell med C++
linktitle: Hämta extern anslutningsdatakälla för pivottabell
type: docs
weight: 150
url: /sv/cpp/get-external-connection-data-source-of-pivot-table/
description: Lär dig hur man hämtar den externa anslutningsdatakällan för en pivot tabell med Aspose.Cells for C++.
---

## **Hämta extern anslutningsdatakälla för pivottabell**

Aspose.Cells ger möjlighet att hämta den externa anslutningsdatakällan för pivot-tabellen. För detta tillhandahåller API:n egenskapen [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) i [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/)-klassen. [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/)-egenskapen returnerar [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/)-objektet. Följande kodsnutt demonstrerar användningen av [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/)-egenskapen för att hämta den externa anslutningsdatakällan till pivot-tabellen.

## Exempelkod

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
    int32_t connectionCount = connections.GetLength();
    for (int32_t i = 0; i < connectionCount; ++i)
    {
        ExternalConnection conn = connections[i];
        std::cout << "Name: " << conn.GetName().ToUtf8() << std::endl;
        std::cout << "Type: " << static_cast<int>(conn.GetSourceType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Källfilen som används i kodprovet är bifogad för referens.

[Källfil](104398862.xlsx)
{{< app/cells/assistant language="cpp" >}}
