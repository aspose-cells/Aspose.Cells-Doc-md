---
title: تنسيق النطاقات باستخدام C++
linktitle: تنسيق النطاقات
type: docs
weight: 105
url: /ar/cpp/how-to-format-a-range/
description: تعلم كيفية تنسيق النطاقات في Excel باستخدام Aspose.Cells مع C++. طبق الأنماط والخطوط والألوان على نطاقات الخلايا برمجياً.
---

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج إلى تطبيق نمط على النطاق، يمكنك استخدام تنسيق النطاق.

## **كيفية تنسيق نطاق في إكسل**

لتنسيق مجموعة من الخلايا في إكسل، يمكنك استخدام الخيارات المدمجة للتنسيق المقدمة من إكسل. إليك كيف يمكنك تنسيق مجموعة من الخلايا مباشرة في إكسل:

1. افتح إكسل وافتح المصنف الذي يحتوي على النطاق الذي تريد تنسيقه.

2. حدد النطاق من الخلايا التي تريد تنسيقها. يمكنك النقر وسحب لتحديد النطاق، أو يمكنك استخدام اختصارات لوحة المفاتيح مثل Shift + مفاتيح الأسهم لتوسيع التحديد.

3. بمجرد تحديد النطاق، انقر بزر الماوس الأيمن على النطاق المحدد واختر "تنسيق الخلايا" من القائمة المنسدلة. بالإضافة إلى ذلك، يمكنك الانتقال إلى علامة التبويب الرئيسية في الشريط في إكسل، انقر فوق القائمة المنسدلة "تنسيق" في مجموعة "الخلايا"، واختر "تنسيق الخلايا".

4. ستظهر نافذة "تنسيق الخلايا". هنا، يمكنك اختيار خيارات التنسيق المختلفة لتطبيقها على النطاق المحدد. على سبيل المثال، يمكنك تغيير نمط الخط، حجم الخط، لون الخط، تنسيق الأرقام، الحدود، لون الخلفية، إلخ. استكشاف علامات التبويب المختلفة في نافذة الحوار للوصول إلى خيارات التنسيق المختلفة.

5. بعد إجراء التغييرات في التنسيق المطلوب، انقر على زر "موافق" لتطبيق التنسيق على النطاق المحدد.

## **كيفية تنسيق نطاق باستخدام C++**

لتنسيق نطاق باستخدام Aspose.Cells، يمكنك استخدام الطرق التالية:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **الكود المثالي**
في هذا المثال، نقوم بإنشاء دفتر عمل Excel، وإضافة بعض البيانات النموذجية، والوصول إلى الورقة الأولى، وتحديد نطاقين („A1:C3“ و„A4:C5“). ثم، نقوم بإنشاء أنماط جديدة، وتعيين خيارات التنسيق المختلفة (مثل لون الخط، عريض)، وتطبيق النمط على النطاق. أخيراً، نحفظ دفتر العمل إلى ملف جديد.
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
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

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
