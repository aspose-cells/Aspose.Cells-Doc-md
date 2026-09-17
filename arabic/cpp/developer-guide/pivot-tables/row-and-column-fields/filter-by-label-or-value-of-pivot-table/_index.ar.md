---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for C++ إمكانيات تصفية شاملة للجداول المحورية. تشرح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات ومرشحات التاريخ ومرشحات القيم ومرشحات أعلى 10 وإخفاء أو إظهار العناصر المحورية.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر محوري, إخفاء العنصر المحوري
type: docs
weight: 10
url: /ar/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في جدول محوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة النصية، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا تاريخ-وقت فقط أو خلايا فارغة، وتطبيق مرشحات القيم مقابل الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار العناصر المحورية الفردية يدويًا باستخدام الخاصية `IsHidden`. يتم الكشف عن كل استراتيجية من خلال واجهات برمجية مخصصة على فئتي `PivotField` و`PivotItem`.
{{% /alert %}}

## **Introduction**
تعد الجداول المحورية أدوات تحليلية قوية، ولكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى عرضه. التصفية هي الآلية الأساسية لتضييق نطاق جدول محوري إلى الصفوف أو الأعمدة أو القيم التي تهم تقريرًا معينًا. يعكس Aspose.Cells for C++ إمكانيات التصفية المتاحة في Microsoft Excel، ويكشف عنها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تتناول هذه المقالة استراتيجيات التصفية التالية:
1. **Label Filter** — يصنف عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **Date Filter** — يصنف حقول الصفوف أو الأعمدة التي تحتوي على قيم تاريخ-وقت فقط (أو خلايا فارغة).
3. **Value Filter** — يصنف العناصر بناءً على القيم المجمعة لحقل بيانات.
4. **Top 10 Filter** — يعرض فقط أعلى أو أدنى N من العناصر مرتبة حسب حقل قيمة.
5. **Hide / Unhide Pivot Items** — يتحكم يدويًا في رؤية كل عنصر فردي في حقل.
يستخدم كل أسلوب طريقة مختلفة على فئة `PivotField` أو خاصية على فئة `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `RefreshData()` و`CalculateData()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **Label Filter**
يسمح لك مرشح التسمية بتصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية مع نمط. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو تحتوي على كلمة معينة، أو تطابق معيارًا آخر قائمًا على التسمية.
يكشف Aspose.Cells عن التصفية حسب التسمية من خلال الطريقة `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وما إلى ذلك. توفر الوسيطة الثانية سلسلة التسمية المستخدمة للمقارنة.
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة مرئية فقط، ويقوم بتحديث الجدول المحوري، ويحفظ النتيجة.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // تحميل ملف العمل الموجود الذي يحتوي على جدول محوري
    Workbook wb(fileName);
    // الوصول إلى ورقة العمل عن طريق الفهرس (ورقة العمل الأولى)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // الوصول إلى الجدول المحوري عن طريق الفهرس
    PivotTable pt = ws.GetPivotTables().Get(0);
    // استرجاع حقل المحور الأول للصف
    PivotField rowField = pt.GetRowFields().Get(0);
    // تطبيق مرشح التسمية — إظهار عناصر الصف فقط التي تبدأ تسمياتها بالبادئة المقدمة
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // تحديث وإعادة حساب بيانات الجدول المحوري حتى يسري المرشح
    pt.RefreshData();
    // حفظ ملف العمل على القرص
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Date Filter**
تتيح لك مرشحات التاريخ تضييق نطاق جدول محوري بناءً على معايير قائمة على التاريخ مثل اليوم أو الأسبوع الماضي أو هذا الشهر أو الربع القادم أو نطاق تاريخ معين. هذه مرشحات متخصصة تعمل فقط مقابل الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا تاريخ-وقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ صالحة من `DateTime` أو خلايا فارغة قبل تطبيق هذا المرشح.
{{% /alert %}}

يكشف Aspose.Cells عن التصفية حسب التاريخ من خلال الطريقة `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. بناءً على نوع المرشح المختار، تمرر قيمة `DateTime` واحدة أو قيمتين (بالنسبة لـ `Between`، تمرر تاريخ البدء وتاريخ الانتهاء).
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري توجد به منطقة الصف حقل تاريخ، ويطبق مرشح تاريخ يقيد العناصر المرئية على نطاق تاريخ معين، ويحدث الجدول المحوري، ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";
    if (!std::filesystem::exists(inputPath))
    {
        // لم يتم العثور على مصنف المصدر.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // قم بتحميل المصنف الموجود الذي يحتوي على الجدول المحوري
    Workbook workbook(U16String(inputPath.c_str()));
    // الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (حسب الفهرس)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // الوصول إلى الجدول المحوري حسب الفهرس
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // استرجاع حقل التاريخ PivotField من منطقة الصفوف
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // تحديد معيار التاريخ لمرشح Between
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // تطبيق مرشح التاريخ على حقل المحور
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // تحديث الجدول المحوري وإعادة حسابه حتى يصبح المرشح ساري المفعول
    // حفظ المصنف
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Value Filter**
تعمل مرشحات القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. بدلاً من مطابقة تسميات النص، فإنها تقارن الإجماليات الرقمية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.
يكشف Aspose.Cells عن التصفية حسب القيمة من خلال الطريقة `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. تستخدم وسيطة `filterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. تحدد وسيطة `valueField` حقل البيانات الذي يجب تقييمه، وتوفر الوسيطة (الوسائط) النهائية قيمة (قيم) العتبة.
يقوم المثال التالي بتحميل مصنف به جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة عتبة رقمية، ويحدث الجدول المحوري، ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }
    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Top 10 Filter**
مرشح أعلى 10 هو شكل متخصص من مرشح القيمة يحتفظ فقط بأعلى أو أدنى N من العناصر بناءً على حقل قيمة مختار. يشيع استخدامه لتقارير الترتيب مثل "أفضل 10 منتجات حسب الإيرادات" أو "أسوأ 5 مناطق حسب عدد المبيعات".

{{% alert color="primary" %}}
يكون مرشح أعلى 10 فعالًا فقط عندما يحتوي الجدول المحوري على حقل قيمة محوري واحد أو أكثر في منطقة البيانات. بدون حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر مقابله، ولا يمكن تطبيق المرشح.
{{% /alert %}}

يكشف Aspose.Cells عن تصفية أعلى 10 من خلال الطريقة `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. تحدد وسيطة `itemCount` عدد العناصر التي يجب الاحتفاظ بها، وتشير `isTop` إلى ما إذا كان سيتم الاحتفاظ بأعلى العناصر (صحيح) أو أدنى العناصر (خطأ)، وتشير `valueField` إلى حقل البيانات المستخدم للترتيب، ويتحكم `filterType` في كيفية حساب القيمة (عادةً `Sum`، ولكن أيضًا `Count` و`Percent`).
يقوم المثال التالي بتحميل مصنف به جدول محوري يحتوي على حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر حسب مجموع المبيعات، ويحدث الجدول المحوري، ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");
    Workbook workbook(inputPath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }
    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    int valueFieldIndex = 0;
    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filter by Hiding or Unhiding Pivot Items**
بالإضافة إلى واجهات التصفية المنظمة، يتيح لك Aspose.Cells التحكم في رؤية كل عنصر محوري فردي مباشرةً. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل الخاصية `IsHidden`، يمكنك منع عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يخفي ضبط `IsHidden = true` العنصر من الجدول المحوري؛ ويظهر ضبط `IsHidden = false` العنصر ويجعله مرئيًا مرة أخرى.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المسماة التي لا ينبغي أن تظهر في تقرير معين. يقوم المثال أدناه بتحميل جدول محوري، وإخفاء عنصر معين بالاسم، وعرض كيفية إظهاره، وتحديث الجدول المحوري، وحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // تحميل مصنف موجود يحتوي على جدول محوري
    Workbook workbook(u"pivot_table_sample.xlsx");
    // الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // الوصول إلى الجدول المحوري حسب الفهرس (أول جدول محوري في الورقة)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // استرجاع حقل المحور المستهدف (أول حقل تسمية صف سنقوم بإخفاء/إظهار العناصر فيه)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // التكرار عبر مجموعة عناصر المحور لحقل المحور المحدد
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // إخفاء عناصر المحور التي تطابق اسمًا/معيارًا محددًا
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // توضيح إلغاء الإخفاء: إعادة عرض عنصر محور تم إخفاؤه مسبقًا
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // تحديث وإعادة حساب الجدول المحوري حتى تسري التغييرات
    pivotTable.CalculateData();
    // حفظ المصنف — تبقى العناصر المخفية في البيانات الأساسية
    // ولكن يتم استبعادها من مخرجات الجدول المحوري المعروضة
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Summary**
يوفر Aspose.Cells for C++ مجموعة كاملة من إمكانيات تصفية الجدول المحوري التي تتطابق مع تلك الموجودة في Microsoft Excel. تغطي مرشحات التسميات والتاريخ والقيم معظم السيناريوهات التحليلية الشائعة، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.IsHidden` بديلاً مرنًا على مستوى العنصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جدول محوري مستهدفة بدقة بالكامل من التعليمات البرمجية.

## Related Articles
- [Insert Pivot Table](/cells/ar/cpp/pivot-tables/)
- [Add Pivot Table Row and Column Fields in Aspose.Cells for C++](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for C++](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for C++](/cells/ar/cpp/manage-value-fields/)
- [Refresh Pivot Tables and Pivot Caches in Aspose.Cells for C++](/cells/ar/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}