---
title: Obtener la fuente de datos de conexión externa de la tabla dinámica con C++
linktitle: Obtener Fuente de Datos de Conexión Externa de la Tabla Dinámica
type: docs
weight: 150
url: /es/cpp/get-external-connection-data-source-of-pivot-table/
description: Aprende cómo recuperar la fuente de datos de conexión externa de una tabla dinámica usando Aspose.Cells for C++.
---

## **Obtener origen de datos de conexión externa de la tabla dinámica**

Aspose.Cells permite obtener la fuente de datos de conexión externa de la tabla dinámica. Para ello, la API proporciona la propiedad [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) de la clase [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/). La propiedad [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) devuelve el objeto [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/). El siguiente fragmento de código demuestra cómo usar la propiedad [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) para obtener la fuente de datos de conexión externa de la tabla dinámica.

## Código de Muestra

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

El archivo fuente utilizado en el fragmento de código está adjunto para referencia.

[Archivo Fuente](104398862.xlsx)
