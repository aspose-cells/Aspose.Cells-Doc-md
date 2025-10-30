---
title: Hur man hämtar OData anslutningsinformation med C++
linktitle: Hur man får OData anslutningsinformation
type: docs
weight: 60
url: /sv/cpp/how-to-get-odata-connection-information/
description: Lär dig hur man extraherar OData anslutningsinformation från Excel filer med Aspose.Cells for C++.
---

## **Få OData-anslutningsinformation**

Det kan finnas fall där utvecklare behöver extrahera OData-information från Excel-filen. Aspose.Cells ger egenskapen [**Workbook.GetDataMashup()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getdatamashup/) som returnerar DataMashup-informationen som finns i Excel-filen. Denna information representeras av [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) klassen. [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) klassen tillhandahåller egenskapen [**GetPowerQueryFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/getpowerqueryformulas/) som returnerar [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) samlingen. Från [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) kan du få tillgång till [**PowerQueryFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformula/) och [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/).

Följande kodsnutt visar användningen av dessa klasser för att hämta OData-informationen.

Källfilen som används i den följande kodsnutten bifogas för din referens.

[Källfil](96928098.xlsx)

### **Exempelkod**

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

### **Konsoloutput**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
