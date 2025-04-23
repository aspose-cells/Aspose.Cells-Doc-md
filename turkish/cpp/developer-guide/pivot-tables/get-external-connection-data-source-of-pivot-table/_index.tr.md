---
title: Pivot Tablo nun Dış Bağlantı Veri Kaynağını Alma (C++)
linktitle: Pivot Tablosunun Harici Bağlantı Veri Kaynağını Alın
type: docs
weight: 150
url: /tr/cpp/get-external-connection-data-source-of-pivot-table/
description: Pivot tablonun dış bağlantı veri kaynağını nasıl alacağınızı Aspose.Cells for C++ kullanarak öğrenin.
---

## **Pivot Tablosunun Harici Bağlantı Veri Kaynağını Alın**

Aspose.Cells, pivot tablonun dış bağlantı veri kaynağını alabilme özelliği sağlar. Bunu yapmak için API, [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) özelliğini [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) sınıfında sağlar. [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) özelliği, [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/) nesnesini döner. Aşağıdaki kod, pivot tablonun dış bağlantı veri kaynağını almak için [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) özelliğinin kullanımını gösterir.

## Örnek Kod

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

Kod örneğinde kullanılan kaynak dosya, referans için ekte bulunmaktadır.

[Kaynak Dosya](104398862.xlsx)
