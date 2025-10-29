---
title: إدارة النطاقات باستخدام C++
linktitle: النطاقات
type: docs
weight: 105
url: /ar/cpp/managing-ranges/
description: تعلّم كيفية إدارة النطاقات في ملفات إكسل باستخدام Aspose.Cells مع C++. إنشاء، تعديل، وتنسيق النطاقات برمجياً.
---

## **مقدمة**

في إكسل، يمكنك تحديد خلايا متعددة باستخدام تحديد مربع الماوس، ويُطلق على مجموعة الخلايا المحددة "نطاق".

على سبيل المثال، يمكنك النقر بزر الماوس الأيسر في الخلية "A1" في إكسل ومن ثم سحبها إلى الخلية "C4". يمكن أيضًا إنشاء المنطقة المستطيلة التي حددتها بسهولة باعتبارها كائنًا عن طريق استخدام Aspose.Cells.

هنا كيفية إنشاء نطاق ووضع قيمة وتعيين النمط، والقيام بعمليات أخرى على كائن "النطاق".

## **إدارة النطاقات باستخدام Aspose.Cells**

توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel، وتحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل تمثل بواسطة فئة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **إنشاء المدى**

عندما ترغب في إنشاء منطقة مستطيلية تمتد عبر A1:C4، يمكنك استخدام الشيفرة التالية:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    Aspose::Cells::Cleanup();
}
```

### **وضع قيمة في الخلايا من المدى**

فلنفترض أن لديك مدى من الخلايا يمتد عبر A1:C4. يحتوي المصفوفة على 4 * 3 = 12 خلية. ترتبت الخلايا الفردية للمدى على التوالي: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

توضح الأمثلة التالية كيفية إدخال بعض القيم في الخلايا للنطاق

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    // Put values in specific cells
    range.Get(0, 0).PutValue(u"A1");
    range.Get(0, 1).PutValue(u"B1");
    range.Get(0, 2).PutValue(u"C1");
    range.Get(3, 0).PutValue(u"A4");
    range.Get(3, 1).PutValue(u"B4");
    range.Get(3, 2).PutValue(u"C4");

    // Save the Workbook
    workbook.Save(u"RangeValueTest.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **تعيين أسلوب للخلايا من المدى**

توضح الأمثلة التالية كيفية تعيين نمط الخلايا في النطاق

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells
    WorksheetCollection sheets = workbook.GetWorksheets();
    Cells cells = sheets.Get(0).GetCells();

    // Create Range
    Range range = cells.CreateRange(u"A1:C4");

    // Put value
    range.Get(0, 0).PutValue(u"A1");
    range.Get(3, 2).PutValue(u"C4");

    // Set Style
    Style style00 = workbook.CreateStyle();
    style00.SetPattern(BackgroundType::Solid);
    style00.SetForegroundColor(Color::Red());
    range.Get(0, 0).SetStyle(style00);

    Style style32 = workbook.CreateStyle();
    style32.SetPattern(BackgroundType::HorizontalStripe);
    style32.SetForegroundColor(Color::Green());
    range.Get(3, 2).SetStyle(style32);

    // Save the Workbook
    workbook.Save(u"RangeStyleTest.xlsx");

    std::cout << "Workbook saved successfully with range styles applied!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **الحصول على النطاق الحالي من المدى**

CurrentRegion هو خاصية تقوم بإرجاع كائن Range يمثل المنطقة الحالية 

المنطقة الحالية هي نطاق محصور بأي مزيج من الصفوف الفارغة والأعمدة الفارغة. للقراءة فقط

في Excel، يمكنك الحصول على منطقة الـ CurrentRegion عن طريق:
1. تحديد منطقة (range1) بصندوق الماوس.
2. انقر "الصفحة الرئيسية - تحرير - البحث والتحديد - اذهب إلى خاص - المنطقة الحالية"، أو استخدم "Ctrl+Shift+*"، سترى أن Excel يساعدك تلقائيًا على تحديد منطقة (range2)، الآن قمت بذلك، range2 هو المنطقة الحالية للـ range1.

من خلال Aspose.Cells، يمكنك استخدام خاصية "Range.CurrentRegion" لأداء نفس الوظيفة.

يرجى تحميل الملف الاختبار التالي، افتحه في Excel، استخدم صندوق الماوس لتحديد منطقة "A1:D7"، ثم انقر "Ctrl+Shift+*"، سترى منطقة "A1:C3" محددة.

[current_region.xlsx](current_region.xlsx)

الآن يرجى تشغيل الأمثلة التالية، وشاهد كيفية عمل ذلك في Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"current_region.xlsx");

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to D7
    Range src = cells.CreateRange(u"A1:D7");

    // Get the CurrentRegion of the created range
    Range A1C3 = src.GetCurrentRegion();

    Aspose::Cells::Cleanup();
}
```


## **مواضيع متقدمة**
- [ملء تلقائي لنطاق ملف Excel](/cells/ar/cpp/autofill-ranges/)
- [نسخ النطاقات من Excel](/cells/ar/cpp/copy-ranges-of-Excel/)
- [نسخ بيانات النطاق فقط](/cells/ar/cpp/copy-range-data-only/)
- [نسخ بيانات النطاق بالتنسيق](/cells/ar/cpp/copy-range-data-with-style/)
- [نسخ نمط النطاق فقط](/cells/ar/cpp/copy-range-style-only/)
- [إنشاء مجموعة الاتحاد](/cells/ar/cpp/create-union-range/)
- [قص ولصق النطاق](/cells/ar/cpp/cut-and-paste-cells/)
- [حذف النطاقات](/cells/ar/cpp/delete-ranges-from-Excel/)
- [الحصول على عنوان خلية عدد الإزاحة الكاملة للعمود والصف الكامل للنطاق](/cells/ar/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [إدراج النطاقات](/cells/ar/cpp/insert-ranges-to-Excel/)
- [دمج أو فصل نطاق الخلايا](/cells/ar/cpp/merge-or-unmerge-range-of-cells/)
- [نقل مجموعة من الخلايا في ورقة العمل](/cells/ar/cpp/move-range-of-cells-in-a-worksheet/)
- [إنشاء أسماء مسماة محددة بنطاق العمل وورقة العمل](/cells/ar/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [البحث والاستبدال في بيانات النطاق](/cells/ar/cpp/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="cpp" >}}
