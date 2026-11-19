---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for C++ إمكانات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسمية والتاريخ والقيم وأعلى 10، وكذلك عبر إخفاء عناصر الجدول المحوري أو إظهارها.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر جدول محوري, إخفاء عنصر جدول محوري
type: docs
weight: 10
url: /ar/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسمية على حقول الصفوف أو الأعمدة التي تعتمد على النص، أو استخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا التاريخ والوقت فقط أو خلايا فارغة، أو تطبيق مرشحات القيم على الأرقام المجمعة، أو استخدام مرشحات أعلى 10 لترتيب النتائج بحسب حقل قيمة، أو إخفاء عناصر الجدول المحوري الفردية وإظهارها يدويًا باستخدام الخاصية `IsHidden`. تتوفر كل استراتيجية من خلال واجهة API مخصصة في كل من الصنفين `PivotField` و`PivotItem`.
{{% /alert %}}

## **مقدمة**
الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما يلزم لعرضه. التصفية هي الآلية الأساسية لتضييق الجدول المحوري بحيث يقتصر على الصفوف أو الأعمدة أو القيم المهمة في تقرير معين. يوفر Aspose.Cells for C++ إمكانات تصفية مماثلة لما يتوفر في Microsoft Excel، ويتيح الوصول إليها برمجيًا لأتمتة إنشاء التقارير بالكامل.
استراتيجيات التصفية التي يتناولها هذا المقال هي:
1. **مرشح التسمية** — تصفية عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **مرشح التاريخ** — تصفية حقول الصف أو العمود التي تحتوي على قيم التاريخ والوقت فقط (أو خلايا فارغة).
3. **مرشح القيمة** — تصفية العناصر بناءً على القيم المجمعة لحقل بيانات.
4. **مرشح أعلى 10** — عرض أفضل N عناصر أو أدنى N عناصر فقط، مرتبة بحسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — التحكم يدويًا في ظهور كل عنصر فردي في الحقل.
تستخدم كل مقاربة عنصر API مختلفًا: دالة في الصنف `PivotField` أو خاصية في الصنف `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `GetPivotCache().Refresh()` على الجدول المحوري حتى تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **مرشح التسمية**
يتيح لك مرشح التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياته النصية بنمط. ويكون ذلك مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف محدد فقط، أو التي تحتوي على كلمة معينة، أو التي تطابق أي معيار آخر قائم على التسمية.
يوفر Aspose.Cells تصفية التسمية من خلال الطريقة `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وغيرها. وتوفر الوسيطة الثانية سلسلة التسمية المستخدمة في المقارنة.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح تسمية بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة ظاهرة فقط، ثم يحدّث الجدول المحوري ويحفظ النتيجة.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مرشح التاريخ**
تتيح لك مرشحات التاريخ تضييق جدول محوري وفق معايير قائمة على التاريخ، مثل اليوم أو الأسبوع الماضي أو الشهر الحالي أو الربع التالي أو نطاق تاريخ محدد. وهي مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا التاريخ والوقت فقط أو قيم فارغة. إذا احتوى الحقل المصدر على أنواع بيانات أخرى، مثل الأرقام أو النصوص، فلن يُنتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ، وأن تكون جميع القيم إما نسخًا صالحة من `DateTime` أو خلايا فارغة، قبل تطبيق هذا المرشح.
يوفر Aspose.Cells تصفية التاريخ من خلال الطريقة `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. ويحتوي تعداد `PivotFilterType` على قيم تاريخية مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. وبناءً على نوع المرشح المحدد، تمرر قيمة `DateTime` واحدة أو قيمتَي `DateTime`، وفي حالة `Between`، تمرر تاريخي البداية والنهاية.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبّق مرشح تاريخ على حقل تاريخ موجود في منطقة الصفوف، بحيث يقصر العناصر الظاهرة على نطاق تاريخ محدد، ثم يحدّث الجدول المحوري ويحفظ المصنف.
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
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مرشح القيمة**
تعمل مرشحات القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات. بدلاً من مطابقة التسميات النصية، تقارن هذه المرشحات الإجماليات الرقمية بحد معين. ومن أمثلة استخدامها عرض المنتجات التي يزيد مجموع مبيعاتها عن مبلغ مستهدف، أو المناطق التي يقع عدد معاملاتها ضمن نطاق محدد.
يوفر Aspose.Cells تصفية القيم من خلال الطريقة `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. تستخدم الوسيطة `filterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. وتحدد الوسيطة `valueField` حقل البيانات الذي ستُقيَّم قيمه، وتوفر الوسيطة أو الوسيطتان النهائيتان قيمة أو قيم الحد.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة لا يُبقي إلا العناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا، ثم يحدّث الجدول المحوري ويحفظ المصنف.

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
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مرشح أعلى 10**
مرشح أعلى 10 هو شكل متخصص من مرشح القيمة، ولا يحتفظ إلا بعدد N من العناصر الأعلى أو الأدنى، استنادًا إلى حقل قيمة محدد. ويُستخدم عادةً في تقارير الترتيب مثل «أفضل 10 منتجات حسب الإيرادات» أو «أدنى 5 مناطق حسب عدد المبيعات».

{{% alert color="primary" %}}
لا يكون مرشح أعلى 10 فعالًا إلا عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. فبدون حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع يمكن ترتيب العناصر بناءً عليه، ولا يمكن تطبيق المرشح.
يوفر Aspose.Cells تصفية أعلى 10 من خلال الطريقة `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`. تمثل الوسيطة `valueFieldIndex` فهرس حقل البيانات الذي تُرتَّب العناصر وفق قيمه المجمعة، ويحدد `type` وحدة احتساب `itemCount` (يحتفظ `PivotFilterType::Count` بعدد ثابت من العناصر، بينما يحتفظ `PivotFilterType::Percent` بنسبة من العناصر بحيث تكون `itemCount` هي النسبة نفسها)، وتشير `isTop` إلى ما إذا كان ينبغي الاحتفاظ بالعناصر الأعلى (`true`) أو الأدنى (`false`)، ويحدد `itemCount` عدد العناصر أو النسبة المئوية التي يجب الاحتفاظ بها.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري يتضمن حقل قيمة، ويطبق مرشح أعلى 10 للإبقاء على أعلى 10 عناصر فقط بحسب مجموع المبيعات، ثم يحدّث الجدول المحوري ويحفظ المصنف.
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
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **التصفية حسب إخفاء عناصر الجدول المحوري أو إظهارها**
إلى جانب واجهات API المخصصة للتصفية، يتيح لك Aspose.Cells التحكم مباشرة في ظهور كل عنصر فردي في الجدول المحوري. ومن خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل الخاصية `IsHidden`، يمكنك إخفاء عناصر محددة بشكل انتقائي من دون تطبيق مرشح قائم على صيغة. عند تعيين `IsHidden = true`، يُخفى العنصر من الجدول المحوري؛ وعند تعيين `IsHidden = false`، يُعاد إظهاره ويصبح مرئيًا مرة أخرى.
يفيد هذا النهج عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد قليل من الفئات محددة الاسم التي لا ينبغي أن تظهر في تقرير معين. يحمّل المثال التالي جدولًا محوريًا، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره، ثم يحدّث الجدول المحوري ويحفظ المصنف.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الملخص**
يوفر Aspose.Cells for C++ مجموعة كاملة من إمكانات تصفية الجداول المحورية، تطابق ما يتوفر في Microsoft Excel. تغطي مرشحات التسمية والتاريخ والقيم أكثر سيناريوهات التحليل شيوعًا، بينما يعالج مرشح أعلى 10 تقارير الترتيب. وعندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.IsHidden` بديلًا مرنًا على مستوى العنصر. ويمكن الجمع بين هذه الاستراتيجيات، مثل تطبيق مرشح تسمية ثم إخفاء عناصر محددة، لإنشاء تقارير جداول محورية مصممة بدقة من خلال التعليمات البرمجية وحدها.

## المقالات ذات الصلة
- [إدراج جدول محوري](/cells/ar/cpp/create-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for C++](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for C++](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for C++](/cells/ar/cpp/manage-value-fields/)
- [تحديث الجداول المحورية وذاكرات التخزين المؤقت الخاصة بها في Aspose.Cells for C++](/cells/ar/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}