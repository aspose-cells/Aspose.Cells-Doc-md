---
title: How to get OData Connection Information with C++
linktitle: How to get OData Connection Information
type: docs
weight: 60
url: /cpp/how-to-get-odata-connection-information/
description: Learn how to extract OData connection information from Excel files using Aspose.Cells for C++.
---

## **Get OData Connection Information**

There might be cases where developers need to extract OData information from the Excel file. Aspose.Cells provides the [**Workbook.GetDataMashup()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getdatamashup/) property which returns the DataMashup information present in the Excel file. This information is represented by the [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) class. The [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) class provides the [**GetPowerQueryFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/getpowerqueryformulas/) property that returns the [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) collection. From the [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/), you can get access to [**PowerQueryFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformula/) and [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/).

The following code snippet demonstrates the use of these classes to retrieve the OData information.

The Source file used in the following code snippet is attached for your reference.

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

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}