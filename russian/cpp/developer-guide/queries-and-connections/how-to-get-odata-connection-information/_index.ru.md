---
title: Как получить информацию о подключении OData с помощью C++
linktitle: Как получить информацию о подключении OData
type: docs
weight: 60
url: /ru/cpp/how-to-get-odata-connection-information/
description: Узнайте, как извлечь информацию о соединениях OData из файлов Excel с помощью Aspose.Cells for C++.
---

## **Получение информации о подключении OData**

Могут возникнуть ситуации, когда разработчикам необходимо извлечь информацию о OData из файла Excel. Aspose.Cells предоставляет свойство [**Workbook.GetDataMashup()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getdatamashup/), которое возвращает информацию DataMashup, содержащуюся в файле Excel. Эта информация представлена классом [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/). Класс [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) предоставляет свойство [**GetPowerQueryFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/getpowerqueryformulas/), которое возвращает коллекцию [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/). Из [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/) вы можете получить доступ к [**PowerQueryFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformula/) и [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/).

В следующем фрагменте кода демонстрируется использование этих классов для извлечения информации OData.

Исходный файл, использованный в следующем фрагменте кода, прикреплен для вашего ознакомления.

[Исходный файл](96928098.xlsx)

### **Образец кода**

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

### **Вывод в консоль**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
