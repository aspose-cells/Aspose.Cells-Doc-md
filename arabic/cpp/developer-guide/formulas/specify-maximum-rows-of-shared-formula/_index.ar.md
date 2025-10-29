---
title: تحديد الحد الأقصى لعدد الصفوف للصيغة المشتركة باستخدام C++
linktitle: كما يمكن استخدام الخاصية {0} لتحديد الصفوف القصوى للصيغة المشتركة.
type: docs
weight: 40
url: /ar/cpp/specify-maximum-rows-of-shared-formula/
description: تعلم كيفية تحديد الحد الأقصى لعدد الصفوف للصيغة المشتركة في ملفات Excel باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 الحد الأقصى الافتراضي لعدد الصفوف للصيغة المشتركة هو 64. يمكن أن يكون أي رقم، على سبيل المثال، يمكن أن يكون 1000. تتغير أداء الصيغة المشتركة مع رقم الصفوف المختلف. لذلك، يوفر Aspose.Cells الخاصية [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) التي يمكن استخدامها لتحديد الحد الأقصى لعدد الصفوف للصيغة المشتركة. سيتم تقسيم الصيغة المشتركة إلى عدة صيغ مشتركة إذا كانت إجمالي الصفوف أكبر من الحد، كما هو موضح في لقطة الشاشة التالية.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **تحديد الصفوف القصوى للصيغة المشتركة**

يوضح رمز المثال التالي استخدام خاصية [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/). يحدد الحد الأقصى لعدد الصفوف للصيغة المشتركة إلى 5، ويضيف الصيغة المشتركة في الخلية D1 لعدد 100 صف ويحفظها في [ملف Excel الإخراج](61767856.xlsx). إذا قمت باستخراج محتويات ملف Excel الناتج وفحص *sheet1.xml*، سترى أن الصيغة المشتركة تتقسم بعد كل 5 صفوف، كما هو مميز في لقطة الشاشة أعلاه.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
