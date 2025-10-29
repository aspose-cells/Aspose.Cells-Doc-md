---
title: 用 C++ 获取数据透视表的外部连接数据源
linktitle: 获取数据透视表的外部连接数据源
type: docs
weight: 150
url: /zh/cpp/get-external-connection-data-source-of-pivot-table/
description: 学习如何使用 Aspose.Cells for C++ 获取数据透视表的外部连接数据源。
---

## **获取数据透视表的外部连接数据源**

Aspose.Cells 提供获取数据透视表外部连接数据源的能力。API 提供了 [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) 属性，属于 [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) 类。[**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) 属性返回 [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/) 对象。以下代码片段演示了如何使用 [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) 属性获取数据透视表的外部连接数据源。

## 示例代码

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

代码片段中使用的源文件已附上供参考。

[源文件](104398862.xlsx)
{{< app/cells/assistant language="cpp" >}}
