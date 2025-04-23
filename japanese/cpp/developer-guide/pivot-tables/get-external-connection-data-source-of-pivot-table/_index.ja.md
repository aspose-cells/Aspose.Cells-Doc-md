---
title: C++を使用してピボットテーブルの外部接続データソースを取得する
linktitle: ピボットテーブルの外部接続データソースの取得
type: docs
weight: 150
url: /ja/cpp/get-external-connection-data-source-of-pivot-table/
description: Aspose.Cells for C++を使用してピボットテーブルの外部接続データソースを取得する方法を学びます。
---

## **ピボットテーブルの外部接続データソースの取得**

 Aspose.Cellsはピボットテーブルの外部接続データソースを取得する機能を提供します。 このために、APIは [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) クラスの [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) プロパティを提供します。 [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) プロパティは [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/) オブジェクトを返します。 次のコードスニペットは、 [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) プロパティを使用してピボットテーブルの外部接続データソースを取得する方法を示しています。

## サンプルコード

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

コードスニペットで使用されるソースファイルは、参照用に添付されています。

[ソースファイル](104398862.xlsx)
