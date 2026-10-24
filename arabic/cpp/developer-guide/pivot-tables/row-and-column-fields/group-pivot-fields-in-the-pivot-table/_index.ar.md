---
title: تجميع الحقول المحورية في الجدول المحوري
linktitle: تجميع الحقول المحورية في الجدول المحوري
description: تعلّم كيفية تجميع الحقول المحورية للصفوف والأعمدة في جدول محوري إلى فترات زمنية مثل الأشهر والأرباع، وإلى نطاقات رقمية باستخدام PivotField.Group وPivotFieldGroupOptions في Aspose.Cells for C++.
keywords: Aspose.Cells, جدول محوري, تجميع حقل محوري, PivotField.Group, PivotFieldGroupOptions, تجميع حسب التاريخ, تجميع الأرقام, أشهر, أرباع, نطاق رقمي, C++
type: docs
weight: 80
url: /ar/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
- يكون تجميع الحقول المحورية مفيدًا عندما يحتوي حقل الصف أو العمود في جدول محوري على عناصر متعددة ومتباينة، مثل حقل تاريخ يحتوي على مئات التواريخ أو حقل رقمي يحتوي على قيم متفرقة كثيرة. يعمل التجميع على طي هذه العناصر في أقسام ذات معنى: التواريخ إلى أشهر وأرباع وسنوات، والأرقام إلى نطاقات مثل 0-1 و2-3 و4-5. وبهذا يصبح الجدول المحوري الكبير مدمجًا وأسهل في التحليل. توفر Aspose.Cells هذه الإمكانية من خلال أسلوب `PivotField.Group()` (التجميع التلقائي حسب نوع البيانات) و`PivotField.Group(PivotFieldGroupOptions)` (خيارات التجميع المخصصة).
- يقوم تجميع التواريخ بلف التواريخ الفردية في فترات أكبر مثل الأيام والأشهر والأرباع والسنوات، ويبني تسلسلًا زمنيًا هرميًا (مثل السنوات، الأرباع، الأشهر). بذلك تصبح الاتجاهات عبر الزمن مرئية بنظرة سريعة، وتصبح كل مستوى من الفترات حقلاً محوريًا مستقلًا في منطقة الصفوف أو الأعمدة في الجدول المحوري.
- يتوفر التجميع فقط للحقول الموضوعة في منطقة الصفوف (ROW) أو الأعمدة (COLUMN) في الجدول المحوري. لا يمكن تجميع حقل بيانات (قيمة) مباشرةً. لتجميع مثل هذا الحقل يجب أولًا إضافته إلى منطقة الصفوف أو الأعمدة في الجدول المحوري.

## **تجميع الحقول المحورية تلقائيًا**
يفحص إصدار التحميل الزائد `PivotField.Group()` بدون معاملات نوع بيانات الحقل ويقوم بتجميعه تلقائيًا. الحقل الذي يحتوي على تواريخ فقط (مع خلايا فارغة) يتم تجميعه حسب الأشهر. والحقل الذي يحتوي على أرقام فقط (مع خلايا فارغة) يتم تجميعه في نطاقات رقمية باستخدام فاصل زمني تلقائي.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تجميع الحقول المحورية باستخدام خيارات مخصصة**
توفر فئة `PivotFieldGroupOptions` إعدادات التجميع المخصصة. لحقول التواريخ، عيّن `StartDate` و`EndDate` و`GroupTypes`. أما للحقول الرقمية، فعيّن `StartNumber` و`EndNumber` و`Interval`. تتحكم الخاصية `NewPivotField` فيما إذا كان التجميع ينشئ حقولاً محورية جديدة بجانب الحقل الأصلي (راجع قسم الملاحظات في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الأشهر والأرباع**
يقوم المثال التالي بتجميع حقل صف التاريخ في الجدول المحوري النموذجي حسب الأشهر والأرباع بين تاريخ بداية وتاريخ نهاية. يقوم الكود بتحميل [ملف Excel النموذجي](sampleGroupPivotFieldsInPivotTable.xlsx)، وينفذ عملية التجميع، ويحسب بيانات الجدول المحوري، ويحفظ النتيجة المجمعة. تُظهر لقطة الشاشة التأثير: أصبح حقل صف التاريخ الآن مجمعًا حسب الأرباع والأشهر.
لاحظ أن ترتيب القيم في `options.GroupTypes` يتم تجاهله. بغض النظر عن الترتيب الذي تُدرج به أنواع المجموعات، فإن الحقول المجمعة تُعرض دائمًا من الفترة الأكبر إلى الأصغر: السنوات، الأرباع، الأشهر، الأيام، الساعات، الدقائق، الثواني. في هذا المثال تُدرج الأشهر قبل الأرباع في `options.GroupTypes`، ومع ذلك يتم عرض الأرباع كمستوى خارجي والأشهر كمستوى داخلي.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // تحميل مصنف العينة
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // الوصول إلى ورقة العمل الثانية وجدول المحاور الخاص بها
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // تجميع حقل الصف الأول (حقل تاريخ) حسب الأشهر والربع
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // تعيين أنواع المجموعات: الأشهر والربع
    ArrayPtr<PivotGroupByType> groupTypes = ArrayPtr<PivotGroupByType>(new PivotGroupByType[2]{ PivotGroupByType::Months, PivotGroupByType::Quarters });
    options.SetGroupTypes(groupTypes);
    // تطبيق التجميع على حقل الصف الأول
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // حساب بيانات جدول المحاور وحفظ ملف الإخراج
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![جدول محوري مجمع حسب الأشهر والأرباع](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي إلى نطاقات**
يكون `FieldTwo` في الجدول المحوري النموذجي في البداية حقل بيانات (قيمة). وبما أنه لا يمكن تجميع سوى حقول الصفوف أو الأعمدة، يقوم الكود أولًا باستدعاء `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصفوف، ثم يقوم بتحديث الجدول المحوري، وبعد ذلك يجمع الحقل الرقمي في النطاقات 0-1 و2-3 و4-5 باستخدام `StartNumber = 0` و`EndNumber = 5` و`Interval = 2`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **ملاحظة**

{{% alert color="primary" %}}
- إن إصدارات التحميل الزائد لأسلوب `PivotField.GroupBy()` قديمة وتمت إزالتها من واجهة برمجة التطبيقات. تُعدّ `PivotField.Group()` و`PivotField.Group(PivotFieldGroupOptions)` البدائل عنها.
- في Microsoft Excel، يؤدي تجميع حقل رقمي إلى استبدال الحقل المحوري الأصلي بنطاقات مجمعة، بينما يؤدي تجميع حقل تاريخ إلى إنشاء حقول محورية جديدة (واحد لكل مستوى تجميع، مثل الأرباع والأشهر) بجانب الحقل الأصلي. ابتداءً من Aspose.Cells 26.10، تتبع أساليب `PivotField.Group()` نفس سلوك Excel. توجد الخاصية `PivotFieldGroupOptions.NewPivotField` للتوافق مع الإصدارات الأقدم: قيمتها الافتراضية هي false لتجميع الأرقام وtrue لتجميع التاريخ والوقت؛ قم بتعيينها إلى false إذا كنت تريد أن يحل تجميع التاريخ محل الحقل المحوري الأصلي بدلًا من إنشاء حقول محورية جديدة.
- لا تنطبق الخاصية `PivotFieldGroupOptions.Interval` إلا على تجميع الأرقام وتجميع التواريخ حسب الأيام (مثل تجميع التواريخ في فترات مدتها 7 أيام)؛ ويتم تجاهلها عند تجميع التواريخ حسب الأشهر أو الأرباع أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/cpp/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/cpp/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/cpp/add-page-field-in-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/cpp/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}