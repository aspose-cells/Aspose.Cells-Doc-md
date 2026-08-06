---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for C++ إمكانيات تصفية شاملة للجداول المحورية. تشرح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات، ومرشحات التاريخ، ومرشحات القيم، ومرشحات أعلى 10، ومن خلال إخفاء أو إظهار عناصر الجدول المحوري.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر الجدول المحوري, إخفاء عنصر الجدول المحوري
type: docs
weight: 10
url: /ar/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---



But this document is already using `RefreshData()` and `CalculateData()` together. The rule says: "Do NOT call RefreshData(); CalculateData(); together — pick one."


For the body content, I need to:
1. Translate the alert block
2. Translate the Introduction section
3. Translate each filter section (Label Filter, Date Filter, Value Filter, Top 10 Filter, Hide/Unhide)
4. Translate the Summary
5. Keep Related Articles as is (they're just titles in English)


For the title of the document: "Filtering Pivot Tables by Label or Value" -> "تصفية الجداول المحورية حسب التسمية أو القيمة"

For description: "Aspose.Cells for C++ supports comprehensive pivot table filtering capabilities. This article explains how to filter pivot table data using label filters, date filters, value filters, top 10 filters, and by hiding or unhiding pivot items."


```markdown

```
{{% alert color="primary" %}}

يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة المستندة إلى النص، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا من نوع التاريخ والوقت فقط أو خلايا فارغة، وتطبيق مرشحات القيم على الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل القيمة، أو إخفاء وإظهار عناصر الجدول المحوري الفردية يدويًا باستخدام خاصية `IsHidden`. يتم عرض كل استراتيجية من خلال واجهات برمجة تطبيقات مخصصة على فئتي `PivotField` و`PivotItem`.

{{% /alert %}}

## **المقدمة**

تُعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى تقديمه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري على الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يدعم Aspose.Cells for C++ إمكانيات التصفية المتاحة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن إنشاء التقارير بشكل آلي بالكامل.

يتم تغطية استراتيجيات التصفية التالية في هذه المقالة:

1. **مرشح التسمية** — يصنف عناصر حقل الصف أو العمود استنادًا إلى تسمياتها النصية.
2. **مرشح التاريخ** — يصنف حقول الصفوف أو الأعمدة التي تحتوي على قيم التاريخ والوقت فقط (أو خانات فارغة).
3. **مرشح القيمة** — يصنف العناصر استنادًا إلى القيم المجمعة لحقل البيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أقل عدد N من العناصر مرتبة حسب حقل القيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر فردي في الحقل.

تستخدم كل طريقة أسلوبًا مختلفًا على فئة `PivotField` أو خاصية على فئة `PivotItem`. بعد تطبيق أي مرشح، يجب عليك استدعاء `RefreshData()` و`CalculateData()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **مرشح التسمية**

يتيح لك مرشح التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية مع نمط معين. يكون ذلك مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو التي تحتوي على كلمة محددة، أو التي تطابق معيارًا آخر قائمًا على التسمية.

يعرض Aspose.Cells تصفية التسميات من خلال الأسلوب `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وما إلى ذلك. توفر الوسيطة الثانية سلسلة التسمية المستخدمة للمقارنة.

يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تظهر فقط العناصر التي تبدأ تسمياتها بالبادئة المحددة، ويُحدّث الجدول المحوري، ويحفظ النتيجة.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // تحميل مصنف العمل الموجود الذي يحتوي على جدول محوري
    Workbook wb(fileName);

    // الوصول إلى ورقة العمل عن طريق الفهرس (ورقة العمل الأولى)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // الوصول إلى الجدول المحوري عن طريق الفهرس
    PivotTable pt = ws.GetPivotTables().Get(0);

    // استرداد حقل المحور الأول للصفوف
    PivotField rowField = pt.GetRowFields().Get(0);

    // تطبيق مرشح التسمية — عرض عناصر الصفوف التي تبدأ تسمياتها بالبادئة المقدمة فقط
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // تحديث وإعادة حساب بيانات الجدول المحوري حتى يتم تطبيق المرشح
    pt.RefreshData();

    // حفظ مصنف العمل مرة أخرى على القرص
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مرشح التاريخ**

تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري حسب معايير قائمة على التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخي محدد. وهي مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}

يعمل مرشح التاريخ فقط عندما تحتوي منطقة الصف أو العمود على خلايا من نوع التاريخ والوقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن يُنتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ `DateTime` صالحة أو خلايا فارغة قبل تطبيق هذا المرشح.

{{% /alert %}}

يعرض Aspose.Cells تصفية التاريخ من خلال الأسلوب `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. اعتمادًا على نوع المرشح المختار، تمرر قيمة أو قيمتي `DateTime` (بالنسبة لـ `Between`، تمرر تاريخي البدء والانتهاء).

يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري يحتوي منطقة الصف فيه على حقل تاريخ، ويطبق مرشح تاريخ يقيد العناصر المرئية على نطاق تاريخي معين، ويُحدّث الجدول المحوري، ويحفظ المصنف.

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
        // ملف العمل المصدر غير موجود.
        Aspose::Cells::Cleanup();
        return -1;
    }

    // تحميل ملف العمل الموجود الذي يحتوي على الجدول المحوري
    Workbook workbook(U16String(inputPath.c_str()));

    // الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (حسب الفهرس)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // الوصول إلى الجدول المحوري حسب الفهرس
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // استرجاع حقل المحور التاريخ من منطقة الصفوف
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // تحديد معيار التاريخ لمرشح بين
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // تطبيق مرشح التاريخ على حقل المحور
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // تحديث وإعادة حساب الجدول المحوري حتى يسري المرشح
    // حفظ ملف العمل
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مرشح القيمة**

تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. بدلاً من مطابقة تسميات النص، فإنها تقارن الإجماليات الرقمية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات فقط التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين.

يعرض Aspose.Cells تصفية القيم من خلال الأسلوب `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. تستخدم وسيطة `filterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. تحدد وسيطة `valueField` حقل البيانات الذي يجب تقييمه، وتوفر الوسيطة (الوسيطات) النهائية قيمة (قيم) الحد.

يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا، ويُحدّث الجدول المحوري، ويحفظ المصنف.

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

## **مرشح أعلى 10**

مرشح أعلى 10 هو شكل متخصص من مرشح القيمة يحتفظ فقط بأعلى أو أقل عدد N من العناصر استنادًا إلى حقل القيمة المختار. يُستخدم عادة لتقارير الترتيب مثل "أفضل 10 منتجات من حيث الإيرادات" أو "أسوأ 5 مناطق من حيث عدد المبيعات".

{{% alert color="primary" %}}

يكون مرشح أعلى 10 فعالًا فقط عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. بدون وجود حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر وفقًا له، ولا يمكن تطبيق المرشح.

{{% /alert %}}

يعرض Aspose.Cells تصفية أعلى 10 من خلال الأسلوب `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. تحدد وسيطة `itemCount` عدد العناصر التي يجب الاحتفاظ بها، وتشير `isTop` إلى ما إذا كان يجب الاحتفاظ بأعلى العناصر (true) أو أقل العناصر (false)، وتشير `valueField` إلى حقل البيانات المستخدم للترتيب، ويتحكم `filterType` في كيفية حساب القيمة (عادةً `Sum`، ولكن أيضًا `Count` و`Percent`).

يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري يحتوي على حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر حسب مجموع المبيعات، ويُحدّث الجدول المحوري، ويحفظ المصنف.

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

## **التصفية عن طريق إخفاء أو إظهار عناصر الجدول المحوري**

بالإضافة إلى واجهات برمجة التطبيقات المنظمة للمرشحات، يتيح لك Aspose.Cells التحكم في رؤية كل عنصر فردي من عناصر الجدول المحوري مباشرةً. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل خاصية `IsHidden`، يمكنك منع عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يخفي تعيين `IsHidden = true` العنصر من الجدول المحوري؛ بينما يُظهر تعيين `IsHidden = false` العنصر مرة أخرى ويجعله مرئيًا.

يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يُحمّل المثال التالي جدولًا محوريًا، ويُخفي عنصرًا محددًا بالاسم، ويُظهر كيفية إظهاره مرة أخرى، ويُحدّث الجدول المحوري، ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // تحميل مصنف موجود مسبقًا يحتوي على جدول محوري
    Workbook workbook(u"pivot_table_sample.xlsx");

    // الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // الوصول إلى الجدول المحوري عن طريق الفهرس (الجدول المحوري الأول في الورقة)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // استرجاع حقل المحور المستهدف (أول حقل تسمية صف سنقوم بإخفاء/إظهار عناصره)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // التكرار عبر مجموعة عناصر المحور للحقل المحدد
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

        // عرض توضيحي لإظهار عنصر محوري تم إخفاؤه سابقًا
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // تحديث الجدول المحوري وإعادة حساب بياناته حتى تسري التغييرات
    pivotTable.CalculateData();

    // حفظ المصنف — تبقى العناصر المخفية في البيانات الأساسية
    // لكنها مستبعدة من مخرجات الجدول المحوري المعروضة
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}"Related Articles must be directly relevant. Only include links that are part of the same parent topic as the current document"

The current document is about filtering pivot tables. The related articles are:
- Insert Pivot Table - relevant
- Add Pivot Table Row and Column Fields - relevant
- Add Filter Fields to a Pivot Table - relevant (very relevant to filtering)
- Manage Pivot Table Value Fields - relevant
- Refresh Pivot Tables and Pivot Caches - relevant

All these are relevant pivot table topics. Good.

But the rule also says: "Do NOT include links to: dbf, ofd, splitting-excel-files-into-multiple-files, inserting-an-image-into-a-cell, SmartMarker-Single-Cell-Array-Rendering, sparkline, or any topic unrelated to the parent directory."

None of these are in the list, and they're all pivot-table related, so they should be fine.

1. After Label Filter section
2. After Date Filter section
3. After Value Filter section
4. After Top 10 Filter section
5. After Hide/Unhide section


"- [تحديث الجداول المحورية وذاكرة التخزين المؤقت للمحاور في Aspose.Cells for C++](/cells/ar/cpp/refresh-pivot-table/)"

This is what I have. Good.

One more check - the rule says: "Every prose paragraph, table cell content, and alert-block body must be written in Arabic." I'm following this.


"- [إضافة حقول الصفوف والأعمدة للجدول المحوري في Aspose.Cells for C++](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)"

This has "Aspose.Cells for C++" appearing once. Good.

- [Insert Pivot Table](/cells/ar/cpp/pivot-tables/)
- [Add Pivot Table Row and Column Fields in Aspose.Cells for C++](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for C++](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for C++](/cells/ar/cpp/manage-value-fields/)
- [Refresh Pivot Tables and Pivot Caches in Aspose.Cells for C++](/cells/ar/cpp/refresh-pivot-table/)

- [إدراج جدول محوري](/cells/ar/cpp/pivot-tables/)
- [إضافة حقول الصفوف والأعمدة للجدول المحوري في Aspose.Cells for C++](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for C++](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [إدارة حقول القيم في الجدول المحوري في Aspose.Cells for C++](/cells/ar/cpp/manage-value-fields/)
- [تحديث الجداول المحورية وذاكرة التخزين المؤقت للمحاور في Aspose.Cells for C++](/cells/ar/cpp/refresh-pivot-table/)

Each "Aspose.Cells for C++" appears once. Good.

Original:cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // تحميل مصنف العمل الموجود الذي يحتوي على جدول محوري
    Workbook wb(fileName);

    // الوصول إلى ورقة العمل عن طريق الفهرس (ورقة العمل الأولى)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // الوصول إلى الجدول المحوري عن طريق الفهرس
    PivotTable pt = ws.GetPivotTables().Get(0);

    // استرداد حقل المحور الأول للصفوف
    PivotField rowField = pt.GetRowFields().Get(0);

    // تطبيق مرشح التسمية — عرض عناصر الصفوف التي تبدأ تسمياتها بالبادئة المقدمة فقط
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // تحديث وإعادة حساب بيانات الجدول المحوري حتى يتم تطبيق المرشح
    pt.RefreshData();

    // حفظ مصنف العمل مرة أخرى على القرص
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // تحميل مصنف العمل الموجود الذي يحتوي على جدول محوري
    Workbook wb(fileName);

    // الوصول إلى ورقة العمل عن طريق الفهرس (ورقة العمل الأولى)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // الوصول إلى الجدول المحوري عن طريق الفهرس
    PivotTable pt = ws.GetPivotTables().Get(0);

    // استرداد حقل المحور الأول للصفوف
    PivotField rowField = pt.GetRowFields().Get(0);

    // تطبيق مرشح التسمية — عرض عناصر الصفوف التي تبدأ تسمياتها بالبادئة المقدمة فقط
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // تحديث وإعادة حساب بيانات الجدول المحوري حتى يتم تطبيق المرشح
    pt.RefreshData();

    // حفظ مصنف العمل مرة أخرى على القرص
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}Good - the placeholder is preserved with the same number (0), and the descriptive text inside is translated to Arabic.



```
{{% alert color="primary" %}}

يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة المستندة إلى النصوص، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا من نوع التاريخ والوقت فقط أو خلايا فارغة، وتطبيق مرشحات القيم على الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري الفردية يدويًا باستخدام خاصية `IsHidden`. يتم الكشف عن كل استراتيجية من خلال واجهات برمجة تطبيقات مخصصة على فئتي `PivotField` و`PivotItem`.

{{% /alert %}}

## **المقدمة**

تُعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى تقديمه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري على الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يدعم Aspose.Cells for C++ إمكانيات التصفية المتوفرة في Microsoft Excel، ويكشف عنها برمجيًا بحيث يمكن إنشاء التقارير بشكل آلي بالكامل.

يتم تغطية استراتيجيات التصفية التالية في هذه المقالة:

1. **مرشح التسمية** — يصنف عناصر حقل الصف أو العمود استنادًا إلى تسمياتها النصية.
2. **مرشح التاريخ** — يصنف حقول الصفوف أو الأعمدة التي تحتوي على قيم التاريخ والوقت فقط (أو خانات فارغة).
3. **مرشح القيمة** — يصنف العناصر استنادًا إلى القيم المجمعة لحقل البيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أقل عدد N من العناصر مرتبة حسب حقل القيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر فردي في الحقل.

يستخدم كل أسلوب أسلوبًا مختلفًا على فئة `PivotField` أو خاصية على فئة `PivotItem`. بعد تطبيق أي مرشح، يجب عليك استدعاء `RefreshData()` و`CalculateData()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **مرشح التسمية**

يتيح لك مرشح التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية مع نمط معين. يكون ذلك مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو التي تحتوي على كلمة محددة، أو التي تطابق معيارًا آخر قائمًا على التسمية.

يكشف Aspose.Cells عن تصفية التسميات من خلال الأسلوب `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وما إلى ذلك. توفر الوسيطة الثانية سلسلة التسمية المستخدمة للمقارنة.

يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تظهر فقط العناصر التي تبدأ تسمياتها بالبادئة المحددة، ويُحدّث الجدول المحوري، ويحفظ النتيجة.## **مرشح التاريخ**

تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري حسب معايير قائمة على التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخي محدد. وهي مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}

يعمل مرشح التاريخ فقط عندما تحتوي منطقة الصف أو العمود على خلايا من نوع التاريخ والوقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن يُنتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ `DateTime` صالحة أو خلايا فارغة قبل تطبيق هذا المرشح.

{{% /alert %}}

يكشف Aspose.Cells عن تصفية التاريخ من خلال الأسلوب `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. اعتمادًا على نوع المرشح المختار، تمرر قيمة أو قيمتي `DateTime` (بالنسبة لـ `Between`، تمرر تاريخي البدء والانتهاء).

يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري منطقة الصف فيه تحتوي على حقل تاريخ، ويطبق مرشح تاريخ يقيد العناصر المرئية على نطاق تاريخي معين، ويُحدّث الجدول المحوري، ويحفظ المصنف.## **مرشح القيمة**

تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. بدلاً من مطابقة تسميات النص، فإنها تقارن الإجماليات الرقمية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات فقط التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين.

يكشف Aspose.Cells عن تصفية القيم من خلال الأسلوب `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. تستخدم وسيطة `filterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. تحدد وسيطة `valueField` حقل البيانات الذي يجب تقييمه، وتوفر الوسيطة (الوسيطات) النهائية قيمة (قيم) الحد.

يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا، ويُحدّث الجدول المحوري، ويحفظ المصنف.## **مرشح أعلى 10**

مرشح أعلى 10 هو شكل متخصص من مرشح القيمة يحتفظ فقط بأعلى أو أقل عدد N من العناصر استنادًا إلى حقل القيمة المختار. يُستخدم عادة لتقارير الترتيب مثل "أفضل 10 منتجات من حيث الإيرادات" أو "أسوأ 5 مناطق من حيث عدد المبيعات".

{{% alert color="primary" %}}

يكون مرشح أعلى 10 فعالًا فقط عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. بدون وجود حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر وفقًا له، ولا يمكن تطبيق المرشح.

{{% /alert %}}

يكشف Aspose.Cells عن تصفية أعلى 10 من خلال الأسلوب `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. تحدد وسيطة `itemCount` عدد العناصر التي يجب الاحتفاظ بها، وتشير `isTop` إلى ما إذا كان يجب الاحتفاظ بأعلى العناصر (true) أو أقل العناصر (false)، وتشير `valueField` إلى حقل البيانات المستخدم للترتيب، ويتحكم `filterType` في كيفية حساب القيمة (عادةً `Sum`، ولكن أيضًا `Count` و`Percent`).

يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري يحتوي على حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر حسب مجموع المبيعات، ويُحدّث الجدول المحوري، ويحفظ المصنف.## **التصفية عن طريق إخفاء أو إظهار عناصر الجدول المحوري**

بالإضافة إلى واجهات برمجة التطبيقات المنظمة للمرشحات، يتيح لك Aspose.Cells التحكم في رؤية كل عنصر فردي من عناصر الجدول المحوري مباشرةً. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل خاصية `IsHidden`، يمكنك منع عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يخفي تعيين `IsHidden = true` العنصر من الجدول المحوري؛ بينما يُظهر تعيين `IsHidden = false` العنصر مرة أخرى ويجعله مرئيًا.

يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يُحمّل المثال التالي جدولًا محوريًا، ويُخفي عنصرًا محددًا بالاسم، ويُظهر كيفية إظهاره مرة أخرى، ويُحدّث الجدول المحوري، ويحفظ المصنف.## **الملخص**

يوفر Aspose.Cells for C++ مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تطابق تلك الموجودة في Microsoft Excel. تغطي مرشحات التسميات والتاريخ والقيم معظم السيناريوهات التحليلية الشائعة، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر خاصية `PivotItem.IsHidden` بديلاً مرنًا على مستوى العنصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جدول محوري مستهدفة بدقة بالكامل من خلال التعليمات البرمجية.
{{< app/cells/assistant language="cpp" >}}


