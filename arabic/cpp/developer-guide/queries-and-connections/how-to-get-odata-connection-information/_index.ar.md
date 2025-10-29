---
title: كيفية الحصول على معلومات اتصال OData باستخدام C++
linktitle: كيفية الحصول على معلومات اتصال OData
type: docs
weight: 60
url: /ar/cpp/how-to-get-odata-connection-information/
description: تعلّم كيفية استخراج معلومات اتصال OData من ملفات إكسل باستخدام Aspose.Cells for C++.
---

## **الحصول على معلومات اتصال OData**

قد توجد حالات يحتاج فيها المطورون إلى استخراج معلومات OData من ملف إكسل. يوفر Aspose.Cells الخاصية [**Workbook.GetDataMashup()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getdatamashup/) التي تعيد معلومات DataMashup الموجودة في ملف إكسل. تمثل هذه المعلومات بواسطة فئة [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/). توفر الفئة [**DataMashup**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/) الخاصية [**GetPowerQueryFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/datamashup/getpowerqueryformulas/) التي تعيد مجموعة [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/). من [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulacollection/)، يمكنك الوصول إلى [**PowerQueryFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformula/) و [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/).

توضح مقتطفات الشفرة التالية استخدام هذه الفئات لاسترداد معلومات OData.

الملف المصدر المستخدم في مقطع الكود التالي مرفق للرجوع إليه.

[الملف المصدر](96928098.xlsx)

### **الكود المثالي**

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

### **مخرجات الوحدة**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
