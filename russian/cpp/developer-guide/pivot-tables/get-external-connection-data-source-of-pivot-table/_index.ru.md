---
title: Получить внешние данные соединения источника данных сводной таблицы через C++
linktitle: Получить внешний источник подключения сводной таблицы
type: docs
weight: 150
url: /ru/cpp/get-external-connection-data-source-of-pivot-table/
description: Научитесь извлекать источник данных внешнего соединения сводной таблицы с помощью Aspose.Cells for C++.
---

## **Получить внешний источник подключения сводной таблицы**

Aspose.Cells предоставляет возможность получить источник данных внешнего соединения сводной таблицы. Для этого API предоставляет свойство [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) класса [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/). Свойство [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) возвращает объект [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/). Следующий пример кода демонстрирует использование свойства [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) для получения внешнего источника данных сводной таблицы.

## Образец кода

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

Исходный файл, использованный во фрагменте кода, прикреплен для справки.

[Исходный файл](104398862.xlsx)
{{< app/cells/assistant language="cpp" >}}
