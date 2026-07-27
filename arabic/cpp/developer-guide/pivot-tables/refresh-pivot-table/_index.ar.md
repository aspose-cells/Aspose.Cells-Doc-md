---
title: تحديث الجداول المحورية في Aspose.Cells for C++
linktitle: تحديث الجداول المحورية في Aspose.Cells for C++
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for C++ باستخدام واجهة برمجة التطبيقات للتحديث v26.7+. تتناول هذه المقالة RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, C++, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة برمجة تطبيقات للتحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري بأربعة نطاقات مختلفة — من المصنف بأكمله إلى جدول محوري واحد. بدءًا من **Aspose.Cells for C++ v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` باعتبارها مهجورة، ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمطلعة على الذاكرة المؤقتة الموضحة في هذه المقالة.
{{% /alert %}}
## المقدمة
نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. وراء الكواليس، يحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة هو مفتاح اختيار واجهة برمجة التطبيقات الصحيحة للتحديث في أي موقف.
سلسلة البيانات المكونة من أربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ تجتمع جميع البيانات هنا ويتم تجميعها.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرةً من مصدر البيانات.
4. **Cells** — خلايا ورقة العمل `Cells` التي يرسم فيها `PivotTable` قيمه وأنماطه المحسوبة.
من المفاهيم المهمة بشكل خاص مفهوم **الذاكرة المؤقتة المشتركة**. عندما تشير جداول محورية متعددة في مصنف إلى نفس نطاق المصدر، فإنها تتشارك *ذاكرة مؤقتة واحدة* من `PivotCache`. يمكن الإشارة إلى `PivotCache` واحد من خلال جداول محورية متعددة، ويؤدي تحديث تلك الذاكرة المؤقتة إلى تحديث كل `PivotTable` تابع لها في وقت واحد.
{{% alert color="primary" %}}
يشير `PivotCache.SourceType` (التعداد `PivotTableSourceType`) إلى مصدر بيانات الذاكرة المؤقتة. اعتبارًا من الإصدار v26.7، يدعم `PivotCache.Refresh()` فقط أنواع المصادر **`Sheet`** و **`Consolidation`** — أي البيانات الموجودة في نطاقات ورقة العمل. لا يمكن بعد تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) من خلال واجهة برمجة التطبيقات للذاكرة المؤقتة.
{{% /alert %}}
نظرًا لهذه السلسلة، هناك مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotCache.Refresh()`** — يعيد تحميل المصدر إلى الذاكرة المؤقتة ويعيد حساب جميع `PivotTable` التابعة في عملية واحدة.
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون رحلة ذهاب وإياب إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر لخلايا ورقة العمل، لذا يكون نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.
## توجيهات التضمين المطلوبة
تبدأ جميع أمثلة C++ في هذه المقالة بتوجيهات تضمين الرأس وتوجيهات مساحة الأسماء التالية لأن أنواع الجدول المحوري توجد في مساحة الاسم `Aspose::Cells::Pivot`:
## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى التأكد من أن كل ذاكرة مؤقتة محورية وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط واجهة برمجة تطبيقات وأكثرها شمولاً هي `Workbook.RefreshAll()`. تستعرض مكالمة واحدة المصنف بالكامل — حيث تحدّث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` تابع. هذه هي الطريقة الموصى بها للتحديثات العامة والشاملة للمستندات حيث لا يكون الأداء مصدر قلق.
يُنشئ المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويُعدّل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لجلب كل شيء حتى تاريخه في مكالمة واحدة.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);

    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);

    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);

    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);

    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);

    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);

    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);

    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);

    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان، تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى معروفة بأنها غير ذات صلة ولا يجب لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.RefreshPivotTables()`، وهي مقيدة بنسخة `Worksheet` واحدة.
هذا أكثر انتقائية من `Workbook.RefreshAll()`: يتم تحديث الجداول المحورية الموجودة في ورقة العمل المستهدفة فقط، تاركًا أي جداول محورية في أوراق العمل الأخرى دون مساس.
يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويُضيف جدولًا محوريًا في ورقة العمل الأولى، ويُعدّل بعض قيم المصدر، ثم يُحدث فقط الجداول المحورية في ورقة العمل تلك.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);

    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);

    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);

    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);

    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);

    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);

    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);

    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);

    worksheet.RefreshPivotTables();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## تحديث جدول محوري واحد
عندما تريد التحكم الدقيق في جدول محوري واحد، فإن واجهة برمجة التطبيقات القائمة على الذاكرة المؤقتة تمنحك خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه فقط.
### تغيرت بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.GetPivotCache().Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر إلى الذاكرة المؤقتة ثم تعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة المؤقتة.
{{% alert color="primary" %}}
نظرًا لأن الجداول المحورية تتشارك نسخة واحدة من `PivotCache`، فإن استدعاء `PivotCache.Refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على تلك الذاكرة المؤقتة نفسها — وليس فقط الجدول الذي تشير إليه. إذا كان جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث ذاكرة مؤقتة واحدة يُحدث كلاهما.
{{% /alert %}}
يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لإظهار سلوك الذاكرة المؤقتة المشتركة، ويُعدّل بعض قيم المصدر، ثم يُحدث من خلال مرجع ذاكرة مؤقتة واحد.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // صف الرأس: الفاكهة / السنة / المبلغ
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // صفوف البيانات
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // إضافة جدول محوري أول "Pivot1" مثبت عند الخلية E3، نطاق المصدر A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // تعيين الحقول لـ Pivot1
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // إضافة جدول محوري ثاني "Pivot2" مثبت عند E15 باستخدام نفس نطاق المصدر A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // تعيين نفس الحقول لـ Pivot2
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // تعديل عدة قيم خلايا المبلغ في بيانات المصدر لمحاكاة تغيير البيانات
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // تحديث ذاكرة التخزين المؤقت المشتركة للجدول المحوري عن طريق تحديث بيانات الجدول المحوري
    pivotTable1.RefreshData();

    // حفظ المصنف
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
### تغير العرض/التخطيط فقط — استخدم `CalculateData()`
إذا لم تتغير بيانات المصدر ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة لرحلة ذهاب وإياب إلى مصدر البيانات. تحتوي الذاكرة المؤقتة بالفعل على البيانات الصحيحة؛ فقط `PivotTable` المعروض يحتاج إلى إعادة حساب. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار الصحيح.
يتجنب ذلك جلب المصدر غير الضروري وهو أسرع بكثير عندما تتشارك جداول محورية متعددة في نفس الذاكرة المؤقتة.
يُعدّل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من الذاكرة المؤقتة الموجودة.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // كتابة صف الرأس Fruit / Year / Amount
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // كتابة 8 صفوف بيانات (الصفوف 2-9، تناسب نطاق المصدر A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);

    // إضافة جدول محوري اسمه "Pivot1" يوضع في خلية الوجهة E3، ويستمد البيانات من A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // تعيين الحقول: Fruit إلى الصف، Year إلى العمود، Amount إلى البيانات
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // تعديل خاصية العرض/التخطيط — هذا تغيير خاص بالعرض فقط،
    // لذلك لا يتطلب إعادة قراءة بيانات المصدر من خلال PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() يعيد عرض الجدول المحوري الحالي (البيانات + النمط) من
    // البيانات المحفوظة بالفعل في PivotCache. نظراً لأن بيانات المصدر لم تتغير،
    // لا يتم تنفيذ رحلة ذهاب وإياب إلى المصدر — فقط يتم إعادة حساب القيم المخزنة مؤقتاً
    // في خلايا ورقة العمل.
    pivotTable.CalculateData();

    // حفظ المصنف على القرص
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache
غالبًا ما يحتوي المصنف على جداول محورية متعددة كلها مبنية فوق ذاكرة مؤقتة مشتركة واحدة. لتعدادها — على سبيل المثال، قبل تنفيذ تحديث دفعة، أو لتشخيص تأثير الذاكرة المؤقتة المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على الذاكرة المؤقتة المعطاة.
هذه أيضًا هي الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان فعلاً في نفس نسخة `PivotCache`: يمكنك مقارنة مراجع الذاكرة المؤقتة، أو ببساطة تكرار المجموعة التي يعرضها `GetPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.
يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان نفس نسخة الذاكرة المؤقتة، ثم يُعدّد جداول الذاكرة المؤقتة المحورية.

## الترحيل من `PivotTable.RefreshData()` المهجور
قبل Aspose.Cells for C++ v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من v26.7، تم وضع علامة على هذه الطريقة باعتبارها **مهجورة** ويجب استبدالها بواجهات برمجة APIs المطلعة على الذاكرة المؤقتة الموضحة أعلاه.
هناك سببان يجعلان نهج `RefreshData()` لكل جدول يمثل مشكلة في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤها، حتى عندما لم يتغير المصدر.
- كل مكالمة تُحدث الذاكرة المؤقتة المشتركة بأكملها. عندما تتشارك جداول محورية متعددة في ذاكرة مؤقتة واحدة، فإن استدعاء `RefreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس الذاكرة المؤقتة مرارًا وتكرارًا، وهو بطيء جدًا.
البدائل الموصى بها هي:
- **تحديث جميع الجداول المحورية في المصنف** → استخدم `workbook.RefreshAll();`
- **تحديث بعضها** → استخدم `pivotTable.GetPivotCache().Refresh();` لذاكرة مؤقتة واحدة. نظرًا لأن الذاكرة المؤقتة مشتركة، فإن هذه المكالمة الواحدة تُحدث كل جدول محوري مبني فوق تلك الذاكرة المؤقتة. يمكن تخطي الجداول المحورية الأخرى التي تستند إلى ذاكرة مؤقتة تم تحديثها بالفعل بأمان.
- **تغير عرض/تخطيط الجدول المحوري فقط** → استخدم `pivotTable.CalculateData();` لإعادة العرض من الذاكرة المؤقتة الموجودة دون أي رحلة ذهاب وإياب إلى المصدر.
يوضح المثال التالي النمط الجديد الفعّال للمصنفات ذات الجداول المحورية المتعددة التي تتشارك ذاكرة مؤقتة واحدة.
```cpp
namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");

    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);

    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);


    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات للتحديث المتاحة ومتى تختار كل واحدة.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع الذواكر المؤقتة والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.RefreshPivotTables()` | مقيدة بورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة مؤقتة واحدة | `pivotTable.GetPivotCache().Refresh()` | تُحدث جميع الجداول المحورية على تلك الذاكرة المؤقتة المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | تتجنب رحلة المصدر غير الضرورية. |
| سرد جميع الجداول المحورية على ذاكرة مؤقتة مشتركة | `pivotCache.GetPivotTables()` | استخدمها للتعداد قبل التحديث بالجملة. |
عمليًا، يُفضل استخدام واجهات برمجة التطبيقات القائمة على الذاكرة المؤقتة على `RefreshData()` المهجور لكل جدول. إنها مطلعة على الذواكر المؤقتة المشتركة، وتتجنب جلب المصدر الزائد، وتتيح لك اختيار أصغر نطاق يلبي متطلب التحديث لديك.

{{< app/cells/assistant language="cpp" >}}
