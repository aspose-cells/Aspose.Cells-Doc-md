---
title: Ottieni la sorgente dati di connessione esterna della pivot table con C++
linktitle: Ottenere la fonte dati della connessione esterna della tabella pivot
type: docs
weight: 150
url: /it/cpp/get-external-connection-data-source-of-pivot-table/
description: Impara come recuperare la sorgente dati di connessione esterna di una pivot table usando Aspose.Cells for C++.
---

## **Ottieni la fonte di dati della connessione esterna della tabella pivot**

Aspose.Cells fornisce la capacità di ottenere la sorgente dati di connessione esterna della pivot table. Per questo, l'API fornisce la proprietà [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) della classe [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/). La proprietà [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) restituisce l'oggetto [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/). Il seguente frammento di codice dimostra come utilizzare la proprietà [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) per ottenere la sorgente dati di connessione esterna della pivot table.

## Codice di esempio

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

Il file di origine utilizzato nel frammento di codice è allegato a scopo di riferimento.

[File di origine](104398862.xlsx)
{{< app/cells/assistant language="cpp" >}}
