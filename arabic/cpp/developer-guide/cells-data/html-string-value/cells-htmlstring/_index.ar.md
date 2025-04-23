---
title: إدارة خلايا HTML باستخدام C++
linktitle: إدارة سلاسل HTML للخلايا
type: docs
weight: 600
url: /ar/cpp/manage-cells-html-string/
description: تعلم كيفية إدارة سلسلة HTML للخلايا من خلال API Aspose.Cells for C++.
keywords: إضافة سلسلة HTML داخل الخلية, تعيين سلسلة HTML داخل الخلية, إضافة سلسلة HTML, الحصول على سلسلة HTML للخلية, إدارة سلاسل HTML للخلايا
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج إلى تعيين بيانات منسقة لخلايا معينة، يمكنك تعيين سلسلة HTML إلى الخلية. بالطبع، يمكنك أيضًا الحصول على سلسلة HTML للخلية. تقدم Aspose.Cells هذه الميزة. توفر Aspose.Cells الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **الحصول على سلسلة html وتعيينها باستخدام Aspose.Cells**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل وإضافة بعض البيانات.
1. الحصول على خلية محددة في الجدول الداخلي الأول.
1. تعيين سلسلة HTML للخلية.
1. الحصول على سلسلة HTML للخلية.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");

    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");

    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    Cell c3 = cells.Get(u"C3");
    // Set HTML string for C3 cell
    c3.SetHtmlString(u"<b>test bold</b>");

    Cell c4 = cells.Get(u"C4");
    // Set HTML string for C4 cell
    c4.SetHtmlString(u"<i>test italic</i>");

    // Get the HTML string of specific cell
    std::cout << c3.GetHtmlString().ToUtf8() << std::endl;
    std::cout << c4.GetHtmlString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## الإخراج الذي تم توليده بواسطة رمز العينة

تُظهر اللقطة الشاشية التالية الإخراج الناتج من الكود المثالي السابق.

![todo:image_alt_text](htmlstring.png)
