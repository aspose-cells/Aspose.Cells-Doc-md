---
title: كيفية تعيين نقطة كمجموع باستخدام C++
linktitle: كيفية تعيين نقطة كمجموع
description: في بعض مخططات إكسل، على سبيل المثال، مخطط WaterFall، قد تحتاج إلى تعيين نقطة كمجموع. يوضح هذا المقال كيفية استخدام Aspose.Cells مع C++ للقيام بذلك.
keywords: مخطط WaterFall، نقطة، تعيين كمجموع
type: docs
weight: 72
url: /ar/cpp/how-to-set-point-as-total/
---

## ما هو "تعيين نقطة كمجموع" في مخطط إكسل

في رسم بياني Excel معين، على سبيل المثال، رسم صفحة الماء، بعض نقاط البيانات هي مجموع النقاط السابقة، قد تحتاج إلى "تعيين النقطة كمجموع". سنعرض رمز العينة والتوضيح أدناه.

## رسم بياني صفحة الماء بحاجة إلى "تعيين النقطة كمجموع" 

![todo:image_alt_text](set-as-total1.png)

يعرض هذا الصورة رسم بياني صفحة الماء في Excel. يمكننا أن نرى أن هناك أربع نقاط بيانات تبدأ بـ "المجموع"، وتُستخدم لحساب جميع النقاط السابقة.
في هذه الصورة، الإعدادات ليست صحيحة تمامًا، عند تحديد نقطة "المجموع 2024" ويمكننا أن نرى أن خيار "ضبط كمجموع" غير مُحدد في Excel.
مرفق أدناه ملف Excel [نموذج](SampleSheet.xlsx) الذي يحتاج إلى تعديل، وسنستخدم Aspose.Cells لإعداده بشكل صحيح.

## استخدام Aspose.Cells لـ "تعيين النقطة كمجموع" 

نستخدم الكود التالي لضبط الملف بشكل صحيح:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

يمكنك الحصول على [ملف الناتج الصحيح](output.xlsx) التالي

كما هو موضح في الشكل أدناه، تم ضبط النقاط الأربعة "مجموع" بشكل صحيح، ويمكنك رؤية الفرق عن المخطط السابق.

![todo:image_alt_text](set-as-total2.png)
