---
title: How to get OData Connection Information with C++
linktitle: How to get OData Connection Information
type: docs
weight: 60
url: /cpp/how-to-get-odata-connection-information/
description: Learn how to extract OData connection information from Excel files using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get OData Connection Information**

There might be cases where developers need to extract OData information from an Excel file. Aspose.Cells provides the `Workbook.GetDataMashup()` property, which returns the DataMashup information present in the Excel file. This information is represented by the **DataMashup** class. The **DataMashup** class provides the `GetPowerQueryFormulas()` property that returns a **PowerQueryFormulaCollection**. From the **PowerQueryFormulaCollection**, you can get access to **PowerQueryFormula** and **PowerQueryFormulaItem**.

The following code snippet demonstrates the use of these classes to retrieve the OData information.

The source file used in the following code snippet is attached for your reference.

[Source File](96928098.xlsx)

### **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook
    Workbook workbook(srcDir + u"ODataSample.xlsx");

    // Get PowerQueryFormulaCollection from DataMashup
    PowerQueryFormulaCollection PQFcoll = workbook.GetDataMashup().GetPowerQueryFormulas();

    // Iterate through each PowerQueryFormula in the collection
    for (int i = 0; i < PQFcoll.GetCount(); ++i)
    {
        PowerQueryFormula PQF = PQFcoll.Get(i);
        std::cout << "Connection Name: " << PQF.GetName().ToUtf8() << std::endl;

        // Get PowerQueryFormulaItemCollection from PowerQueryFormula
        PowerQueryFormulaItemCollection PQFIcoll = PQF.GetPowerQueryFormulaItems();

        // Iterate through each PowerQueryFormulaItem in the collection
        for (int j = 0; j < PQFIcoll.GetCount(); ++j)
        {
            PowerQueryFormulaItem PQFI = PQFIcoll.Get(j);
            std::cout << "Name: " << PQFI.GetName().ToUtf8() << std::endl;
            std::cout << "Value: " << PQFI.GetValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Console Output**

{{< highlight cpp >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
