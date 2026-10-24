---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: توفر Aspose.Cells for C++ إمكانات شاملة لتصفية الجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسمية والتاريخ والقيمة وأعلى 10، وكذلك عبر إخفاء عناصر الجدول المحوري أو إظهارها.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر الجدول المحوري, إخفاء عنصر الجدول المحوري
type: docs
weight: 10
url: /ar/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسمية على حقول الصفوف أو الأعمدة المستندة إلى نص، أو استخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا التاريخ والوقت فقط أو خلايا فارغة، أو تطبيق مرشحات القيمة على الأرقام المجمعة، أو استخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء عناصر الجدول المحوري الفردية وإظهارها يدويًا باستخدام الخاصية `IsHidden`. تتوفر كل استراتيجية عبر واجهات API مخصصة في الصنفين `PivotField` و`PivotItem`.
{{% /alert %}}

## **مقدمة**
تُعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما يلزم لعرضه. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري بحيث لا يشمل إلا الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يتيح Aspose.Cells for C++ إمكانات التصفية المتاحة في Microsoft Excel برمجيًا، مما يتيح أتمتة إنشاء التقارير بالكامل.
استراتيجيات التصفية التالية موضحة في هذه المقالة:
1. **مرشح التسمية** — يصفية عناصر حقول الصف أو العمود استنادًا إلى تسمياتها النصية.
2. **مرشح التاريخ** — يصفية حقول الصف أو العمود التي لا تحتوي إلا على قيم التاريخ والوقت أو القيم الفارغة.
3. **مرشح القيمة** — يصفية العناصر استنادًا إلى القيم المجمعة لحقل بيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى N عناصر أو أدناها، مرتبة حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — التحكم يدويًا في رؤية كل عنصر فردي في الحقل.
تستخدم كل طريقة اسمًا مختلفًا للأسلوب في `PivotField` أو خاصية في `PivotItem`. نظرًا لأن تطبيق المرشح يغيّر طريقة العرض أو التخطيط، يجب استدعاء `CalculateData()` على الجدول المحوري حتى تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة. وإذا تغيرت بيانات المصدر، استخدم `pivotTable.PivotCache.Refresh()` لتحديث ذاكرة التخزين المؤقت.

## **مرشح التسمية**
يسمح مرشح التسمية بتصفية عناصر حقل صف أو عمود بمقارنة تسمياتها النصية بنمط. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو تحتوي على كلمة معينة، أو تطابق أي معيار آخر قائم على التسمية.
توفر Aspose.Cells تصفية التسمية من خلال أسلوب `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. يضم التعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وغيرها. ويوفر الوسيط الثاني سلسلة التسمية المستخدمة في المقارنة.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث لا تظهر إلا العناصر التي تبدأ تسمياتها ببادئة محددة، ثم يحدّث الجدول المحوري ويحفظ النتيجة.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // تحميل مصنف العمل الحالي الذي يحتوي على جدول محوري
    Workbook wb(fileName);
    // الوصول إلى ورقة العمل حسب الفهرس (ورقة العمل الأولى)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // الوصول إلى الجدول المحوري حسب الفهرس
    PivotTable pt = ws.GetPivotTables().Get(0);
    // استرداد حقل الصف الأول PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // تطبيق مرشح التسميات — عرض عناصر الصف فقط التي تبدأ تسمياتها بالبادئة المقدمة
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // تحديث بيانات الجدول المحوري وإعادة حسابها حتى يصبح المرشح ساري المفعول
    pt.RefreshData();
    // حفظ مصنف العمل على القرص
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مرشح التاريخ**
تتيح مرشحات التاريخ تضييق نطاق الجدول المحوري وفق معايير تستند إلى التاريخ، مثل اليوم أو الأسبوع الماضي أو الشهر الحالي أو الربع التالي أو نطاق تاريخ محدد. وهي مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصفوف أو الأعمدة على خلايا التاريخ والوقت فقط أو على قيم فارغة. إذا احتوى الحقل الأساسي على أنواع بيانات أخرى، مثل الأرقام أو النصوص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم إما نسخ صالحة من `DateTime` أو خلايا فارغة قبل تطبيق هذا المرشح.
توفر Aspose.Cells تصفية التاريخ من خلال أسلوب `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. يحتوي التعداد `PivotFilterType` على قيم تاريخية مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. وبحسب نوع المرشح المحدد، تمرر قيمة `DateTime` واحدة أو قيمتين؛ أما في حالة `Between`، فتمرر تاريخ البداية وتاريخ النهاية.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري تقع في منطقة صفوفه حقل تاريخ، ويطبق مرشح تاريخ يقيّد العناصر الظاهرة بنطاق تاريخ محدد، ثم يحدّث الجدول المحوري ويحفظ المصنف.
{{% /alert %}}

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
    // تحميل مصنف العمل الموجود الذي يحتوي على جدول المحور
    Workbook workbook(U16String(inputPath.c_str()));
    // الوصول إلى ورقة العمل التي تحتوي على جدول المحور (حسب الفهرس)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // الوصول إلى جدول المحور حسب الفهرس
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // استرجاع حقل التاريخ PivotField من منطقة الصفوف
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // تحديد معيار التاريخ لمرشح Between
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // تطبيق مرشح التاريخ على حقل المحور
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // تحديث جدول المحور وإعادة حسابه حتى يسري المرشح
    // حفظ مصنف العمل
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مرشح القيمة**
تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات. بدلاً من مطابقة التسميات النصية، تقارن الإجماليات الرقمية بحد. ومن أمثلة الاستخدامات النموذجية عرض المنتجات التي يزيد مجموع مبيعاتها عن مبلغ محدد فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق محدد فقط.
توفر Aspose.Cells تصفية القيمة من خلال أسلوب `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. يستخدم الوسيط `filterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. ويحدد الوسيط `valueField` حقل البيانات الذي يجب تقييمه، وتوفر الوسائط الأخيرة قيمة الحد أو قيمه.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يُبقي على العناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا فقط، ثم يحدّث الجدول المحوري ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
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
مرشح أعلى 10 هو شكل متخصص من مرشح القيمة يحتفظ فقط بأعلى N عناصر أو أدناها استنادًا إلى حقل قيمة محدد. ويستخدم عادةً في تقارير الترتيب مثل «أعلى 10 منتجات حسب الإيرادات» أو «أدنى 5 مناطق حسب عدد المبيعات».

{{% alert color="primary" %}}
لا يكون مرشح أعلى 10 فعالًا إلا عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. من دون حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع يمكن لترتيب العناصر استنادًا إليه، ولا يمكن تطبيق المرشح.
توفر Aspose.Cells تصفية أعلى 10 من خلال أسلوب `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. يحدد الوسيط `itemCount` عدد العناصر التي يجب الاحتفاظ بها، ويشير `isTop` إلى الاحتفاظ بأعلى العناصر (`true`) أو أدناها (`false`)، ويشير `valueField` إلى حقل البيانات المستخدم في الترتيب، بينما يتحكم `filterType` في طريقة حساب القيمة، وهي عادةً `Sum`، لكن يمكن أيضًا استخدام `Count` و`Percent`.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري يضم حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ بأعلى 10 عناصر فقط استنادًا إلى مجموع المبيعات، ثم يحدّث الجدول المحوري ويحفظ المصنف.
{{% /alert %}}

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

## **التصفية بإخفاء عناصر الجدول المحوري أو إظهارها**
بالإضافة إلى واجهات API للتصفية المهيكلة، تتيح Aspose.Cells التحكم مباشرة في رؤية كل عنصر من عناصر الجدول المحوري. ومن خلال التكرار في المجموعة `PivotItems` الخاصة بالحقل `PivotField` وتبديل الخاصية `IsHidden`، يمكنك استبعاد عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على صيغة. يؤدي تعيين `IsHidden = true` إلى إخفاء العنصر من الجدول المحوري، بينما يؤدي تعيين `IsHidden = false` إلى إظهاره وجعله ظاهرًا مرة أخرى.
يفيد هذا الأسلوب عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعناصر محددة، مثل إخفاء عدد قليل من الفئات ذات الأسماء المحددة التي لا ينبغي أن تظهر في تقرير معين. يحمّل المثال التالي جدولًا محوريًا، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره، ثم يحدّث الجدول المحوري ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // تحميل مصنف موجود يحتوي على جدول محوري
    Workbook workbook(u"pivot_table_sample.xlsx");
    // الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // الوصول إلى الجدول المحوري حسب الفهرس (أول جدول محوري في ورقة العمل)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // استرجاع حقل PivotField الهدف (حقل تسمية الصف الأول الذي سنخفي عناصره أو نظهرها فيه)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // التكرار عبر مجموعة PivotItems الخاصة بحقل PivotField المحدد
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // إخفاء عناصر الجدول المحوري التي تطابق اسمًا/معيارًا محددًا
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // إعادة إظهار عنصر جدول محوري كان مخفيًا سابقًا
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // تحديث الجدول المحوري وإعادة حسابه حتى تسري التغييرات
    pivotTable.CalculateData();
    // حفظ المصنف — تظل العناصر المخفية في البيانات الأساسية
    // لكن يتم استبعادها من إخراج الجدول المحوري المعروض
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الملخص**
توفر Aspose.Cells for C++ مجموعة كاملة من إمكانات تصفية الجداول المحورية بما يطابق ما يتوفر في Microsoft Excel. تغطي مرشحات التسمية والتاريخ والقيمة أكثر السيناريوهات التحليلية شيوعًا، بينما تتولى مرشحات أعلى 10 تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.IsHidden` حلًا بديلًا مرنًا على مستوى العنصر. إن دمج هذه الاستراتيجيات — مثل تطبيق مرشح تسمية ثم إخفاء عناصر محددة — يتيح لك إنشاء تقارير جداول محورية دقيقة وموجهة بالكامل عبر التعليمات البرمجية.

## مقالات ذات صلة
- [إدراج جدول محوري](/cells/ar/cpp/create-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for C++](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for C++](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [إدارة حقول القيم في جدول محوري في Aspose.Cells for C++](/cells/ar/cpp/manage-value-fields/)
- [تحديث الجداول المحورية ومخازنها في Aspose.Cells for C++](/cells/ar/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}