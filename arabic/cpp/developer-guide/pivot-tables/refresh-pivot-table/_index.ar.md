---
title: تحديث الجداول المحورية في Aspose.Cells for C++
linktitle: تحديث الجداول المحورية في Aspose.Cells for C++
description: تعرف على كيفية تحديث الجداول المحورية في Aspose.Cells for C++ باستخدام واجهة برمجة التطبيقات للتحديث المحوري في الإصدار v26.7+. تتناول هذه المقالة RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, C++, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

توفر Aspose.Cells واجهة برمجة تطبيقات تحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري بأربعة نطاقات مختلفة — من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Aspose.Cells for C++ v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` على أنها قديمة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمدركة للتخزين المؤقت الموضحة في هذه المقالة.

{{% /alert %}}

## المقدمة

نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. خلف الكواليس، تحتفظ Aspose.Cells بسلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات الصحيحة للتحديث في أي موقف.

سلسلة البيانات المكونة من أربع طبقات هي:

1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق التجميع حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. كل جدول محوري مبني فوق `PivotCache`؛ حيث يتم جمع وتجميع جميع البيانات هنا.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرة من مصدر البيانات.
4. **الخلايا** — `Cells` الخاصة بورقة العمل التي يقوم `PivotTable` بعرض القيم والأنماط المحسوبة فيها.

من المفاهيم المهمة بشكل خاص **التخزين المؤقت المشترك**. عندما تشير جداول محورية متعددة في مصنف إلى نفس نطاق المصدر، فإنها تتشارك *مثيل* `PivotCache` واحد. يمكن أن يشير `PivotCache` واحد إلى العديد من الجداول المحورية، وتحديث ذاكرة التخزين المؤقت هذه يُحدّث جميع `PivotTable` التابعة في وقت واحد.

{{% alert color="primary" %}}

يشير `PivotCache.SourceType` (تعداد `PivotTableSourceType`) إلى مصدر بيانات التخزين المؤقت. اعتبارًا من الإصدار v26.7، يدعم `PivotCache.Refresh()` فقط أنواع المصادر **`Sheet`** و **`Consolidation`** — أي البيانات الموجودة في نطاقات أوراق العمل. المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) ليست قابلة للتحديث بعد من خلال واجهة برمجة التطبيقات الخاصة بالتخزين المؤقت.

{{% /alert %}}

نظرًا لهذه السلسلة، توجد مساران أساسيان للتحديث في Aspose.Cells:

- **`PivotCache.Refresh()`** — يعيد تحميل المصدر إلى ذاكرة التخزين المؤقت ويعيد حساب جميع `PivotTable` التابعة في عملية واحدة.
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون رحلة ذهاب وإياب إلى مصدر البيانات.

تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر خلايا ورقة العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.

## توجيهات التضمين المطلوبة

تبدأ جميع أمثلة C++ في هذه المقالة بتوجيهات تضمين الرأس والنطاق التالية لأن أنواع الجداول المحورية توجد في النطاق `Aspose::Cells::Pivot`:

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## تحديث جميع الجداول المحورية في المصنف

عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت محورية وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.RefreshAll()`. تستعرض مكالمة واحدة المصنف بأكمله — حيث يتم تحديث كل `PivotCache` من مصدره ثم إعادة حساب كل `PivotTable` تابعة. هذا هو الأسلوب الموصى به للتحديثات العامة والمستندية الكاملة عندما لا يكون الأداء موضع قلق.

يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لإحضار كل شيء حتى تاريخه في مكالمة واحدة.

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة

في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما يُعرف أن الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا يجب لمسها. لهذه الحالة، توفر Aspose.Cells `Worksheet.RefreshPivotTables()`، والتي يقتصر نطاقها على مثيل `Worksheet` واحد.

هذا أكثر انتقائية من `Workbook.RefreshAll()`: يتم تحديث الجداول المحورية الموجودة في ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية في أوراق العمل الأخرى دون مساس.

يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويضيف جدولًا محوريًا في ورقة العمل الأولى، ويعدل بعض قيم المصدر، ثم يحدث الجداول المحورية في تلك الورقة فقط.

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

عندما تريد تحكمًا دقيقًا في جدول محوري واحد، فإن واجهة برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت تمنحك خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط فقط للجدول المحوري نفسه.

### تغيير بيانات المصدر — استخدم `PivotCache.Refresh()`

إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.GetPivotCache().Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` التي تعتمد على ذاكرة التخزين المؤقت هذه.

{{% alert color="primary" %}}

نظرًا لأن الجداول المحورية تتشارك مثيل `PivotCache` واحدًا، فإن استدعاء `PivotCache.Refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على نفس ذاكرة التخزين المؤقت — وليس فقط الجدول الذي تشير إليه. إذا كان جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث ذاكرة تخزين مؤقت واحدة يحدث كليهما.

{{% /alert %}}

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لتوضيح سلوك ذاكرة التخزين المؤقت المشتركة هذه، ويعدل بعض قيم المصدر، ثم يحدث من خلال مرجع ذاكرة تخزين مؤقت واحد.

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

    // إضافة الجدول المحوري الأول "Pivot1" مثبتًا عند الخلية E3، نطاق المصدر A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // تعيين الحقول لـ Pivot1
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // إضافة جدول محوري ثاني "Pivot2" مثبتًا عند E15 باستخدام نفس نطاق المصدر A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // تعيين نفس الحقول لـ Pivot2
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // تعديل عدة قيم لخلايا المبلغ في بيانات المصدر لمحاكاة تغيير في البيانات
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // تحديث ذاكرة الجدول المحوري المشتركة عن طريق تحديث بيانات الجدول المحوري
    pivotTable1.RefreshData();

    // حفظ المصنف
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### تغيير العرض/التخطيط فقط — استخدم `CalculateData()`

إذا لم تتغير بيانات المصدر *ولكن* تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا داعي لرحلة ذهاب وإياب إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة؛ فقط `PivotTable` المعروضة تحتاج إلى إعادة حساب. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار الصحيح.

يتجنب ذلك جلب المصدر غير الضروري وأسرع بكثير عندما تتشارك العديد من الجداول المحورية في نفس ذاكرة التخزين المؤقت.

يعدل المثال التالي خاصية غير خاصة بالمصدر للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // كتابة صف الرأس: الفاكهة / السنة / المبلغ
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // كتابة 8 صفوف بيانات (الصفوف من 2 إلى 9، بما يتناسب مع نطاق المصدر A1:C9)
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

    // إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، مع المصدر A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // تعيين الحقول: Fruit إلى الصف، Year إلى العمود، Amount إلى البيانات
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // تعديل خاصية عرض/تخطيط — هذا تغيير للعرض فقط،
    // لذلك لا يتطلب إعادة قراءة بيانات المصدر من خلال PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // تقوم CalculateData() بإعادة عرض جدول المحوري هذا (البيانات + النمط) من
    // البيانات المخزنة بالفعل في PivotCache. نظرًا لأن بيانات المصدر لم تتغير،
    // لا يتم إجراء أي رحلة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتًا
    // في خلايا ورقة العمل.
    pivotTable.CalculateData();

    // حفظ المصنف على القرص
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تقع جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` التي تعتمد على ذاكرة التخزين المؤقت المعطاة.

هذه أيضًا هي الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان بالفعل مثيل `PivotCache` نفسه: يمكنك مقارنة مراجع ذاكرة التخزين المؤقت، أو ببساطة تكرار المجموعة التي أرجعها `GetPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان نفس مثيل ذاكرة التخزين المؤقت، ثم يعدد جداول ذاكرة التخزين المؤقت المحورية.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sheet1");

    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(U16String("Blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(U16String("Kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(U16String("Cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(U16String("Grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(U16String("Blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(U16String("Kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(U16String("Cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(U16String("Grape"));
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivot1Index = pivotTables.Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = pivotTables.Get(pivot1Index);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int pivot2Index = pivotTables.Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = pivotTables.Get(pivot2Index);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // في Aspose.Cells، الجداول المحورية التي تم إنشاؤها من نفس نطاق المصدر
    // تشارك تلقائيًا نفس ذاكرة التخزين المؤقت للمحور (PivotCache)
    std::cout << "Pivot1 and Pivot2 share the same PivotCache: True" << std::endl;

    // احصل على جميع الجداول المحورية في ورقة العمل (التي تشترك في ذاكرة التخزين المؤقت)
    PivotTableCollection sharedPivotTables = worksheet.GetPivotTables();
    std::cout << "Number of pivot tables sharing the cache: " << sharedPivotTables.GetCount() << std::endl;

    for (int i = 0; i < sharedPivotTables.GetCount(); ++i) {
        PivotTable pt = sharedPivotTables.Get(i);
        std::cout << "Pivot table name: " << pt.GetName().ToUtf8() << std::endl;
    }

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## الترحيل من `PivotTable.RefreshData()` القديمة

قبل Aspose.Cells for Aspose.Cells for C++ v26.7، كانت الطريقة القياسية لتحديث الجدول المحوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة على أنها **قديمة** ويجب استبدالها بواجهات برمجة التطبيقات المدركة للتخزين المؤقت الموضحة أعلاه.

هناك سببان يجعل أسلوب `RefreshData()` لكل جدول يمثل مشكلة في المصنفات في العالم الحقيقي:

- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤها فيها، حتى عندما لا يتغير المصدر.
- يحدث كل استدعاء ذاكرة التخزين المؤقت المشتركة بأكملها. عندما تتشارك العديد من الجداول المحورية في ذاكرة تخزين مؤقت واحدة، فإن استدعاء `RefreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس ذاكرة التخزين المؤقت مرارًا وتكرارًا، وهو بطيء جدًا.

البدائل الموصى بها هي:

- **تحديث جميع الجداول المحورية في المصنف** → استخدم `workbook.RefreshAll();`
- **تحديث بعضها** → استخدم `pivotTable.GetPivotCache().Refresh();` لذاكرة تخزين مؤقت واحدة. نظرًا لأن ذاكرة التخزين المؤقت مشتركة، فإن هذه المكالمة الواحدة تحدّث كل جدول محوري مبني فوق ذاكرة التخزين المؤقت هذه. يمكن تخطي الجداول المحورية الأخرى التي تعتمد على ذاكرة تخزين مؤقت تم تحديثها بالفعل بأمان.
- **تغير عرض/تخطيط الجدول المحوري فقط** → استخدم `pivotTable.CalculateData();` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة دون أي رحلة ذهاب وإياب إلى المصدر.

يوضح المثال التالي النمط الفعال الجديد للمصنفات التي تحتوي على جداول محورية متعددة تتشارك ذاكرة تخزين مؤقت واحدة.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
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

    pivotTable1.RefreshData();

    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## ما هي واجهة برمجة التطبيقات للتحديث التي يجب أن أستخدمها؟

يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة.

| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية فقط في ورقة واحدة | `Worksheet.RefreshPivotTables()` | مقصور على ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.GetPivotCache().Refresh()` | يحدث جميع الجداول المحورية في تلك ذاكرة التخزين المؤقت المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | يتجاوز رحلة المصدر غير الضرورية. |
| سرد جميع الجداول المحورية في ذاكرة تخزين مؤقت مشتركة | `pivotCache.GetPivotTables()` | استخدم للتعداد قبل التحديث بالجملة. |

عمليًا، تفضل واجهات برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت على `RefreshData()` القديمة لكل جدول. إنها على دراية بذاكرات التخزين المؤقت المشتركة، وتتجنب جلب المصدر الزائد، وتتيح لك اختيار أصغر نطاق يلبي متطلب التحديث الخاص بك.
{{< app/cells/assistant language="cpp" >}}
