---
title: كيفية تدوير نص الخلية باستخدام C++
linktitle: كيفية دوران نص الخلية
type: docs
weight: 80
url: /ar/cpp/how-to-rotate-text-of-cell/
description: كود C++ لتدوير نص الخلية باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++
keywords: تدوير نص الخلية بواسطة C++، تدوير نص الخلية برمجياً باستخدام C++ في مفكرة العمل، ضبط زاوية تدوير الخلية برمجياً، كيفية تدوير نص الخلية في إكسل باستخدام C++
---

## **دوران نص الخلية في Aspose.Cells**

مكتبة Aspose.Cells هي مكون قوي بلغة C++ يمكن المطورين من العمل مع جداول إكسل برمجياً. إحدى الميزات التي توفرها Aspose.Cells هي القدرة على تدوير الخلايا، مما يسمح لك بتخصيص اتجاه النص وتحسين العرض البصري لبياناتك. سنستعرض في هذا المستند كيفية تدوير الخلايا باستخدام Aspose.Cells.

## **كيفية تدوير نص الخلية في إكسل**
يمكنك تدوير خلية في إكسل باستخدام الخطوات التالية:
1. افتح برنامج إكسل وحدد الخلية أو مجموعة من الخلايا التي ترغب في تدويرها.
1. انقر بزر الماوس الأيمن على الخلية(الخلايا) المحددة واختر "تنسيق الخلايا" من قائمة السياق. بالإضافة إلى ذلك، يمكنك الانتقال إلى علامة التبويب "الرئيسية" في شريط أدوات إكسل، انقر على القائمة المنسدلة "تنسيق" في مجموعة "الخلايا"، واختر "تنسيق الخلايا".
1. في مربع حوار "تنسيق الخلايا"، انتقل إلى علامة التبويب "توجيه".
1. في قسم "التوجيه"، سترى خيارات لتدوير النص. يمكنك إدخال زاوية التدوير المرغوبة مباشرة في مربع "الدرجات". القيم الإيجابية تدور النص باتجاه عقارب الساعة، والقيم السالبة تدور به عكس اتجاه عقارب الساعة.
<br>
![todo:image_alt_text](alignment.png)
1. بمجرد اختيار الدورة المرغوبة، انقر على "موافق" لتطبيق التغييرات. ستتم إعادة تدوير الخلية(الخلايا) المحددة الآن استنادًا إلى زاوية التدوير أو التوجيه التي اخترتها.

## **كيفية تدوير نص الخلية باستخدام واجهة برمجة تطبيقات Aspose.Cells**

خاصية [**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) تجعل من السهل تدوير الخلايا. لتدوير الخلايا في Aspose.Cells، تحتاج إلى اتباع الخطوات التالية:
1. تحميل دفتر العمل في إكسل
<br>
أولاً، تحتاج إلى تحميل دفتر العمل في إكسل باستخدام Aspose.Cells. يمكنك استخدام فئة Workbook لفتح ملف إكسل موجود أو إنشاء ملف جديد. 

1. الوصول إلى ورقة البيانات
<br>
بمجرد تحميل دفتر العمل، ستحتاج إلى الوصول إلى ورقة البيانات التي ترغب في تدوير الخلايا فيها. يمكنك الوصول إما إلى ورقة البيانات بمؤشرها أو اسمها. 

1. تدوير نص الخلية
<br>
الآن بعد أن لديك وصول إلى ورقة البيانات، يمكنك تدوير الخلايا عن طريق تعديل كائن الأنماط (Style) للخلايا المرغوبة. كائن الأنماط يسمح لك بتعيين مجموعة متنوعة من خيارات التنسيق، بما في ذلك التدوير. 

1. حفظ دفتر العمل
<br>
بعد تدوير الخلايا، يمكنك حفظ دفتر العمل المعدل مرة أخرى في ملف أو تيار باستخدام طريقة الحفظ.

## **كود نموذج C++**

يرجى رؤية الكود التالي، فهو ينشئ كائن دفتر العمل ويضبط زوايا تدوير مختلفة لعدة خلايا. يوضح اللقطة الشاشة النتيجة بعد تنفيذ الكود العيني.
<br>
<img src="rotation.png" width=80% />

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
