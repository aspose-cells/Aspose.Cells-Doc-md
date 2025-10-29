---
title: تغيير تنسيق خلية باستخدام C++
linktitle: تغيير تنسيق الخلية
description: كيفية استخدام مكتبة Aspose.Cells في C++ لتغيير تنسيق الخلايا، بما في ذلك الخط، اللون، الحدود، وغيرها. من خلال تعديل هذه الخصائص، يمكنك التحكم بشكل أكبر في مظهر الخلايا وظهورها.
keywords: Aspose.Cells، تنسيق الخلايا، C++، الخط، اللون، الحدود
type: docs
weight: 20
url: /ar/cpp/how-to-change-format-of-cell/
---

## **سيناريوهات الاستخدام المحتملة**
عندما ترغب في تسليط الضوء على بعض البيانات، يمكنك تغيير نمط الخلايا.

## **كيفية تغيير تنسيق الخلية في إكسل**

لتغيير تنسيق خلية واحدة في إكسل، اتبع هذه الخطوات:

1. افتح إكسل وافتح الدفتر الذي يحتوي على الخلية التي ترغب في تنسيقها.

2. اعثر على الخلية التي ترغب في تنسيقها.

3. انقر بزر الماوس الأيمن على الخلية وحدد "تنسيق الخلايا" من قائمة السياق. كبديل، يمكنك تحديد الخلية والانتقال إلى علامة التبويب الرئيسية في شريط أدوات إكسل، انقر فوق قائمة "تنسيق" في مجموعة "الخلايا" وحدد "تنسيق الخلايا".

4. سيظهر مربع حوار "تنسيق الخلايا". هنا، يمكنك اختيار خيارات التنسيق المختلفة لتطبيقها على الخلية المحددة. على سبيل المثال، يمكنك تغيير نمط الخط، حجم الخط، لون الخط، تنسيق الأرقام، الحدود، لون الخلفية، إلخ. استكشف الألسنة المختلفة في مربع الحوار للوصول إلى خيارات التنسيق المختلفة.

5. بعد إجراء التغييرات في التنسيق المطلوب، انقر على زر "موافق" لتطبيق التنسيق على الخلية المحددة.

## **كيفية تغيير تنسيق خلية باستخدام C++**

لتغيير تنسيق خلية باستخدام Aspose.Cells، يمكنك استخدام الطرق التالية:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)

## **الكود المثالي**
في هذا المثال، نقوم بإنشاء دفتر عمل Excel، وإضافة بعض البيانات التجريبية، والوصول إلى ورقة العمل الأولى، والحصول على خليين ("A2" و "B3"). ثم، نحصل على نمط الخلية، ونضبط خيارات التنسيق المختلفة (مثل لون الخط، والعريض)، ونقوم بتغيير الشكل إلى الخلية. وأخيرًا، نحفظ الدفتر الدفتر العمل في ملف جديد.
![todo:image_alt_text](change-format.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

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

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell a2 = worksheet.GetCells().Get(u"A2");
    Style style = a2.GetStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFontColor(true);
    a2.SetStyle(style, flag);

    Cell b3 = worksheet.GetCells().Get(u"B3");
    Style style2 = b3.GetStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    b3.SetStyle(style2);

    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
