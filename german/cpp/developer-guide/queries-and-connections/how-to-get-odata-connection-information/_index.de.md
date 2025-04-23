---
title: Wie man OData Verbindungsinformationen mit C++ erhält
linktitle: Wie man OData Verbindungsinformationen abruft
type: docs
weight: 60
url: /de/cpp/how-to-get-odata-connection-information/
description: Lernen Sie, wie Sie OData Verbindungsinformationen aus Excel Dateien mit {Aspose.Cells for C++} extrahieren.
---

## **OData-Verbindungsinformationen abrufen**

Es kann Fälle geben, in denen Entwickler OData-Informationen aus Excel-Dateien extrahieren müssen. Aspose.Cells bietet die Eigenschaft [**Workbook.GetDataMashup()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getdatamashup/), die die DataMashup-Informationen in der Excel-Datei zurückgibt. Diese Informationen werden durch die Klasse [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) repräsentiert. Die Klasse [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) bietet die Eigenschaft [**GetPowerQueryFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/getpowerqueryformulas/), die die [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/)-Sammlung zurückgibt. Über die [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) können Sie auf [**PowerQueryFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformula/) und [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) zugreifen.

Der folgende Code-Ausschnitt zeigt die Verwendung dieser Klassen zum Abrufen der OData-Informationen.

Die im folgenden Code-Ausschnitt verwendete Quelldatei ist zur Referenz angehängt.

[Quelldatei](96928098.xlsx)

### **Beispielcode**

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

### **Konsolenausgabe**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
