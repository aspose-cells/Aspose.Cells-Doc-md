---
title: عرض أو تصفية أفضل 10 في الجدول المحوري
linktitle: عرض أو تصفية أفضل 10 في الجدول المحوري
description: تعلّم كيفية عرض أعلى العناصر أو أدناها من حيث الترتيب فقط في حقل من الجدول المحوري باستخدام Aspose.Cells for C++. تتناول هذه المقالة طريقة Top10AutoShow في Excel 97-2003، وقراءة الخيارات باستخدام GetTop10AutoShowSettings، وتطبيق مرشح أفضل 10 في Excel 2007-365 عبر FilterTop10.
keywords: Aspose.Cells, C++, جدول محوري, أفضل 10, العرض التلقائي, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /ar/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
قد يصعب قراءة الجدول المحوري الذي يسرد كل عنصر في حقل صف إذا كان الحقل يحتوي على عشرات العناصر. يحتفظ تقرير أفضل 10 فقط بأعلى العناصر أو أدناها من حيث الترتيب، وهو بالضبط ما تحتاج إليه تقارير الترتيب، مثل «أفضل 5 منتجات حسب الإيرادات» أو «أسفل 3 مناطق حسب عدد المبيعات». يدعم Aspose.Cells آليتين لذلك، تمثّلان جيلين من Microsoft Excel.
- **العرض التلقائي في Excel 97-2003** — الطريقة `PivotField.Top10AutoShow()`. هذا هو الإعداد الكلاسيكي «اعرض أفضل N عناصر أو أسفل N عنصرًا» المخزن مباشرةً في حقل الجدول المحوري. وهو يعمل في جميع إصدارات Excel، القديمة والحديثة، لأنه جزء من صيغة الجدول المحوري الأصلية.
- **مرشح أفضل 10 في Excel 2007-365** — الطريقة `PivotField.FilterTop10()`. هذا هو مرشح القيم الحديث لأفضل 10، والذي يتوفر ضمن «مرشحات القيم» في قائمة الحقل. يتم تخزينه ككائن `PivotFilter` مرتبط بالحقل، ويوفر ترتيبًا قائمًا على عدد العناصر أو نسبتها المئوية.

## **عرض أفضل 10 في Excel 97-2003 (Top10AutoShow)**
يُهيَّأ العرض التلقائي الكلاسيكي باستخدام استدعاء واحد لـ `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)`:
- `isAutoShow` — يتيح إعداد العرض التلقائي على الحقل أو يعطله.
- `isTop` — يؤدي `true` إلى الاحتفاظ بالعناصر الأعلى مرتبة (الأعلى)، و`false` إلى الاحتفاظ بالعناصر الأدنى (الأسفل).
- `count` — عدد العناصر التي يجب الاحتفاظ بها، مثل 10 لتقرير أفضل 10 الكلاسيكي.
- `rankBy` — الفهرس القائم على الصفر لحقل **البيانات** الذي تُرتَّب العناصر وفق قيمه. مرّر -1 لترتيب العناصر حسب الحقل نفسه.
يمكن أن يستند الترتيب إلى حقل قيمة أو إلى الحقل نفسه. وفيما يلي مثالان على الأسلوبين.

### **الترتيب حسب حقل قيمة**
رتّب عناصر حقل الصف وفق حقل قيمة عادي، مثل «مجموع المبيعات». يبني المثال التالي جدولًا محوريًا يحتوي على حقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أفضل رياضتين حسب المبيعات. تكون قيمة `rankBy` مساوية لـ 0 لأن حقل البيانات «مجموع المبيعات» موجود عند الفهرس 0.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // عرض أول عنصرين مرتبين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **الترتيب حسب الحقل نفسه**
يمكن أيضًا ترتيب عناصر الحقل وفق الحقل نفسه، لذا مرّر -1 كقيمة لـ `rankBy`. لا يلزم وجود حقل بيانات إضافي لهذا البديل؛ يكفي أن يكون الحقل في منطقة الصفوف (أو الأعمدة). يعرض المثال التالي أدنى 3 رياضات استنادًا إلى ترتيب الحقل نفسه. عند حفظ هذا الإعداد، لا تتضمن XML للجدول المحوري السمة `rankBy` لأن -1 هي القيمة الافتراضية لهذه الصيغة، وتعيد `GetTop10AutoShowSettings().GetRankBy()` القيمة -1.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // عرض العناصر الثلاثة الأدنى مرتبةً حسب الحقل نفسه (rankBy = -1)
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **قراءة الخيارات الحالية (GetTop10AutoShowSettings)**
تعيد الطريقة `PivotField.GetTop10AutoShowSettings()` كائن `PivotFieldTop10AutoShowSettings` الذي يتيح الوصول إلى خيارات العرض التلقائي المخزنة حاليًا على الحقل. استخدمه لفحص طريقة عرض عناصر الحقل في مصنف موجود أو في جدول محوري قمت بتكوينه للتو، بما في ذلك المصنفات المحمّلة من ملف.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

تُقابل هذه العناصر الأربعة سمات العرض التلقائي الكلاسيكية المكتوبة في XML للجدول المحوري (`autoShow`، `topAutoShow`، `itemPageCount`، `rankBy`)، لذا تكون القيم المقروءة هي القيم التي تعتمدها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- تم إهمال خصائص `PivotField` المباشرة `IsAutoShow` و`IsAscendShow` و`GetAutoShowCount` و`GetAutoShowField`. استخدم كائن `PivotFieldTop10AutoShowSettings` بدلاً منها: يقابل `IsAutoShow` الاستدعاء `GetTop10AutoShowSettings().IsAutoShow()`، ويقابل `IsAscendShow` الاستدعاء `GetTop10AutoShowSettings().IsTop()`، ويقابل `GetAutoShowCount` الاستدعاء `GetTop10AutoShowSettings().GetAutoShowCount()`، ويقابل `GetAutoShowField` الاستدعاء `GetTop10AutoShowSettings().GetRankBy()`. طريقة `Top10AutoShow()` نفسها هي الطريقة المدعومة لتغيير الإعدادات.
- تعمل `Top10AutoShow` مع حقول الصفوف والأعمدة. لا يمكن ترتيب حقل يكون في منطقة الصفحة (التصفية) فقط بهذه الطريقة، لأن عناصره لا تظهر في جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: مرشح أفضل 10 (FilterTop10)**
تتيح إصدارات Excel الحديثة تطبيق أفضل 10 بوصفه مرشحًا للقيم من قائمة الحقل (مرشحات القيم، أفضل 10...). يمثّل Aspose.Cells هذه الخاصية عبر الطريقة `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`، التي تُعيد كائن `PivotFilter` الذي تم إنشاؤه:
- `valueFieldIndex` — الفهرس القائم على الصفر لحقل البيانات الذي تُرتَّب العناصر وفق قيمه المجمّعة.
- `type` — يحدد ما يعنيه `itemCount`. يحتفظ `PivotFilterType::Count` بعدد ثابت من العناصر (خيار «العناصر» في مربع الحوار). ويحتفظ `PivotFilterType::Percent` بنسبة مئوية من العناصر، لذا تكون `itemCount` هي النسبة المئوية نفسها؛ أي أن 30 يحتفظ بأفضل 30٪. ويرتّب `PivotFilterType::Sum` العناصر وفق التغطية التراكمية للقيم.
- `isTop` — يؤدي `true` إلى عرض الأعلى و`false` إلى عرض الأسفل.
- `itemCount` — قيمة N في «أفضل N»، وتعتمد وحدتها على `type`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // مرشح أفضل 10 — الاحتفاظ بأعلى عنصرين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // بدلاً من ذلك، لاستخدام مرشح قائم على النسبة، احتفظ بأعلى 30٪ من العناصر:
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
تعد `Top10AutoShow` و`FilterTop10` ميزتين منفصلتين. يكتب العرض التلقائي سمة `autoShow` الكلاسيكية على حقل الجدول المحوري، وتطبّقها جميع إصدارات Excel منذ Excel 97. ويكتب `FilterTop10` إدخال `PivotFilter` حديثًا، ويتطلب Excel 2007 أو إصدارًا أحدث. عند فتح مصنف في إصدار أقدم من Excel، يعود الجدول المحوري الذي يستخدم المرشح الحديث إلى عرض جميع العناصر. وبالنسبة إلى المستندات التي يجب أن تمر ذهابًا وإيابًا عبر أدوات الإصدارات القديمة، استخدم `Top10AutoShow`؛ أما في المصنفات الحديثة، فاستخدم `FilterTop10` لأنه يتكامل مع مرشحات القيم الأخرى.
{{% /alert %}}

## **مقالات ذات صلة**
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/cpp/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [تجميع حقول الجدول المحوري في الجدول المحوري](/cells/ar/cpp/group-pivot-fields-in-the-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/cpp/refresh-pivot-table/)
- [إضافة حقل صفحة إلى الجدول المحوري](/cells/ar/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}