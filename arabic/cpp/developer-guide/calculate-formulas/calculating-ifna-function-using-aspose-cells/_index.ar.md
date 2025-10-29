---
title: حساب وظيفة IFNA باستخدام Aspose.Cells مع C++
linktitle: حساب وظيفة IFNA
description: كيفية حساب وظائف IFNA باستخدام مكتبة Aspose.Cells مع C++. عن طريق تحميل ملف إكسل موجود أو إنشاء ملف جديد، يمكننا استخدام الطرق التي تقدمها Aspose.Cells لحساب وظيفة IFNA والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف إكسل المعدل على القرص.
keywords: Aspose.Cells، إكسل، وظائف IFNA، الحسابات، C++
type: docs
weight: 40
url: /ar/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

تدعم Aspose.Cells حساب وظيفة IFNA في Excel. تقوم وظيفة IFNA بإرجاع القيمة التي تحددها إذا عادت الصيغة بقيمة خطأ #N/A. وإلا، ستقوم بإرجاع نتيجة الصيغة.

{{% /alert %}} 

## **حساب وظيفة IFNA باستخدام Aspose.Cells**
الكود النموذجي التالي يوضح حساب وظيفة IFNA باستخدام Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**
فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
