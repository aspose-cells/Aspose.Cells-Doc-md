---
title: الحصول على مصدر بيانات الاتصال الخارجي لجدول محوري باستخدام C++
linktitle: الحصول على مصدر بيانات الاتصال الخارجي لجدول الدوران
type: docs
weight: 150
url: /ar/cpp/get-external-connection-data-source-of-pivot-table/
description: تعلم كيفية استرجاع مصدر بيانات الاتصال الخارجي لجدول محوري باستخدام Aspose.Cells for C++.
---

## **الحصول على مصدر بيانات الاتصال الخارجي لجدول الدوران**

 تقدم Aspose.Cells القدرة على الحصول على مصدر بيانات الاتصال الخارجي للجدول المحوري. لهذا، يوفر API الخاص [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) الخاص بـ [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/). الخاصية [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) تُرجع الكائن [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/). يوضح المقتطف التالي استخدام الخاصية [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) للحصول على مصدر الاتصال الخارجي للجدول المحوري.

## كود عينة

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

الملف المصدر المستخدم في مقتطف الشفرة مرفق للرجوع إليه.

[ملف المصدر](104398862.xlsx)
{{< app/cells/assistant language="cpp" >}}
