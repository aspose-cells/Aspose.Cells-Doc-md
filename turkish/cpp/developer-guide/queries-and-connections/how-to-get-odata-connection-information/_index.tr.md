---
title: C++ kullanarak OData Bağlantı Bilgilerini Nasıl Alırım
linktitle: OData Bağlantı Bilgilerini Nasıl Alınır
type: docs
weight: 60
url: /tr/cpp/how-to-get-odata-connection-information/
description: Excel dosyalarından OData bağlantı bilgilerinin nasıl çıkarılacağını Aspose.Cells for C++ kullanarak öğrenin.
---

## **OData Bağlantı Bilgilerini Alın**

Bazı durumlarda, geliştiricilerin Excel dosyasından OData bilgisi çıkarması gerekebilir. Aspose.Cells, Excel dosyasında bulunan DataMashup bilgisini döndürür ve bu bilgi [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) sınıfı ile temsil edilir. [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) sınıfı, [**GetPowerQueryFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/getpowerqueryformulas/) özelliği ile [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) koleksiyonunu döndürür. [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) ile [**PowerQueryFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformula/) ve [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) erişebilirsiniz.

Aşağıdaki kod parçası, bu sınıfları kullanarak OData bilgisini almayı göstermektedir.

Aşağıdaki kod parçasında kullanılan Kaynak dosyası, referansınız için ekte bulunmaktadır.

[Kaynak Dosyası](96928098.xlsx)

### **Örnek Kod**

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

### **Konsol Çıktısı**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
