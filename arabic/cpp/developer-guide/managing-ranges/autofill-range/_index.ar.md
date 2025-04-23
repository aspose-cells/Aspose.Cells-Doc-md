---
title: ملء تلقائي لنطاق ملف Excel باستخدام C++
linktitle: نطاق ملء تلقائي
type: docs
weight: 105
url: /ar/cpp/autofill-ranges/
description: تعلم كيفية إجراء عملية الملء التلقائي في نطاق محدد من ملف Excel باستخدام Aspose.Cells مع C++.
---

## **إجراء ملء تلقائي في النطاق المحدد في Excel**

في Excel، اختر نطاقًا، حرك الماوس إلى الزاوية اليمنى السفلى، وُقم بسحب علامة "+" لملء البيانات تلقائيًا.

## **ملء تلقائي للنطاقات باستخدام Aspose.Cells**

يوضح المثال التالي كيفية إجراء عملية تعبئة تلقائية على نطاق. إليك الملف النموذجي الذي يمكن تحميله لاختبار هذه الميزة:

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
