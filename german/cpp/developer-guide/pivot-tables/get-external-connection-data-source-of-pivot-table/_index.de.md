---
title: Externe Datenquelle einer Pivot Tabelle mit C++ abrufen
linktitle: Abrufen der externen Verbindungsdatenquelle der Pivot Tabelle
type: docs
weight: 150
url: /de/cpp/get-external-connection-data-source-of-pivot-table/
description: Lernen Sie, wie Sie die externe Datenquelle einer Pivot Tabelle mit Aspose.Cells for C++ abrufen.
---

## **Abrufen der externen Verbindungsdatenquelle der Pivot-Tabelle**

Aspose.Cells ermöglicht das Abrufen der externen Datenquellen für Pivot-Tabellen. Hierfür bietet die API die Eigenschaft [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) der Klasse [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/). Die Eigenschaft [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) gibt das [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/) Objekt zurück. Das folgende Codebeispiel zeigt, wie die Eigenschaft [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) verwendet wird, um die externe Datenquelle der Pivot-Tabelle zu erhalten.

## Beispielcode

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

Die im Codeausschnitt verwendete Quelldatei ist zur Referenz angehängt.

[Quelldatei](104398862.xlsx)
