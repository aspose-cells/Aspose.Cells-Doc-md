---
title: تحديث الجداول المحورية وذاكرات التخزين المؤقت للجداول المحورية في Aspose.Cells for C++
linktitle: تحديث الجداول المحورية وذاكرات التخزين المؤقت للجداول المحورية في Aspose.Cells for C++
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for C++ باستخدام واجهة برمجة تطبيقات تحديث الجداول المحورية v26.7+. تغطّي هذه المقالة RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على الشيفرة.
keywords: Aspose.Cells, C++, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells واجهة برمجة تطبيقات تحديث متدرجة تسمح لك بإعادة تحميل بيانات الجداول المحورية بأربع نطاقات مختلفة — من المصنف بالكامل إلى جدول محوري واحد. بدءًا من **Aspose.Cells for C++ v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` بأنها مهجورة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والتي تدرك الـ PivotCache المذكورة في هذه المقالة.
{{% /alert %}}

## مقدمة
عادةً لا يكون تحديث جدول محوري عملية واحدة فقط. خلف الكواليس، تحتفظ Aspose.Cells بسلسلة بيانات متدرجة تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي حالة.  
سلسلة البيانات ذات الطبقات الأربع هي:
1. **Data Source** — النطاقات الأصلية لورقة العمل، استعلام قاعدة البيانات، أو نطاق التجميع حيث تتواجد القيم الأولية.  
2. **PivotCache** — النسخة المؤقتة في الذاكرة من بيانات المصدر. كل جدول محوري يُبنى فوق `PivotCache`؛ هنا تُجمّع وتُلخّص جميع البيانات.  
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف، الأعمدة، القيم، والمرشحات. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، ولا يقرأ مباشرةً من مصدر البيانات.  
4. **Cells** — خلايا ورقة العمل `Cells` التي يقوم `PivotTable` بإدراج القيم المحسوبة والأنماط فيها.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`) يحدد من أين جاءت بيانات الـ PivotCache. اعتبارًا من v26.7، تدعم `PivotCache.Refresh()` نوعي المصدر **`Sheet`** و **`Consolidation`** فقط — أي البيانات الموجودة في نطاقات ورقة العمل. المصادر الخارجية (قواعد بيانات، اتصالات خارجية، إلخ) لا يمكن تحديثها بعد عبر واجهة برمجة التطبيقات للذاكرة المؤقتة.  
نظرًا لهذه السلسلة، هناك مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد باستخدام البيانات المخزّنة مسبقًا في الـ PivotCache، دون أي جولة مرة أخرى إلى مصدر البيانات.  
جميع السيناريوهات في هذه المقالة تستخدم بيانات مصدر خلايا ورقة العمل، لذا يكون نوع المصدر `Sheet` وتعمل عمليات التحديث كما هو موضح.
{{% /alert %}}

## البدء السريع
إذا كنت بحاجة إلى أقصر شفرة ممكنة تقوم بتحديث كل جدول محوري في المصنف، يكفي استدعاء واحد:

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

كل ما تبقى في هذه المقالة يوضح متى يجب اختيار واجهة برمجة تطبيقات أضيق.

## توجيهات الـ Include المطلوبة
جميع أمثلة C++ في هذه المقالة تبدأ بتضمين رؤوس الملفات وتوجيهات النطاقات التالية لأن أنواع الجداول المحورية موجودة في النطاق `Aspose::Cells::Pivot`:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## تحديث جميع الجداول المحورية في المصنف
عند الحاجة إلى التأكد من أن كل ذاكرة مؤقتة للجدول المحوري وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، أبسط وأكثر شمولًا هو واجهة برمجة التطبيقات `Workbook.RefreshAll()`. استدعاء واحد يجوب المصنف بالكامل — يحدّث كل `PivotCache` من مصدره ثم يعيد حساب كل `PivotTable` تابع. هذا هو النهج الموصى به للتحديثات العامة لكامل المستند عندما لا تكون الأداء مصدر قلق.  
المثال التالي يبني مصنفًا بنطاق مصدر يحتوي على الفاكهة/السنة/المبلغ، ينشئ جدولًا محوريًا واحدًا، يغيّر بعض قيم المصدر، ثم يستخدم `RefreshAll()` لتحديث كل شيء في استدعاء واحد.

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
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
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
أحيانًا قد تحتاج فقط إلى تحديث الجداول المحورية الموجودة على ورقة عمل واحدة محددة — على سبيل المثال، عندما تكون الجداول المحورية على أوراق عمل أخرى غير ذات صلة ولا ينبغي تعديلها. في هذه الحالة، توفر Aspose.Cells الدالة `Worksheet.RefreshPivotTables()`، التي تقتصر على نسخة `Worksheet` واحدة.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
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
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
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
عندما تريد تحكمًا دقيقًا في جدول محوري واحد، توفر واجهة برمجة التطبيقات القائمة على الـ PivotCache خيارين. يعتمد الاختيار بينهما على ما تغيّر فعليًا: بيانات المصدر الأساسية، أو فقط إعدادات العرض/التخطيط للجدول المحوري نفسه.

### تغير بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.GetPivotCache().Refresh()`. هذا الاستدعاء يعيد قراءة بيانات المصدر إلى الـ PivotCache ثم يعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة.

### تغير فقط العرض/التخطيط — استخدم `CalculateData()`
إذا لم تتغير بيانات المصدر ولكن تم تعديل عرض أو إعدادات تخطيط جدول محوري (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تشغيل/إيقاف إعداد التحديث عند الفتح)، فلا حاجة للعودة إلى مصدر البيانات. الـ PivotCache تحتفظ بالفعل بالبيانات الصحيحة؛ فقط `PivotTable` المظهر يحتاج إلى إعادة حساب. في هذه الحالة، يكون `pivotTable.CalculateData()` هو الخيار المناسب.  
المثال التالي يغيّر خاصية غير مرتبطة بالمصدر للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من الـ PivotCache الحالية.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Write Fruit / Year / Amount header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
 // Add a pivot table placed at destination cell E3, sourcing from A1:C9
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    // Assign fields: Fruit to Row, Year to Column, Amount to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modify a view/layout property — this is a presentation-only change,
    // so it does NOT require re-reading the source data through PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() re-renders THIS pivot table's display (data + style) from the
    // data already held in the PivotCache. Because the source data did not change,
    // no round-trip to the source is performed — only the cached values are recalculated
    // into worksheet cells.
    pivotTable.CalculateData();
    // Save the workbook to disk
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تشترك جميعًا في PivotCache واحدة مشتركة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعي، أو لتشخيص تأثير الذاكرة المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الدالة مجموعة كل `PivotTable` تعتمد على الـ PivotCache المعطاة.

## الانتقال من الطريقة المهجورة `PivotTable.RefreshData()`
قبل Aspose.Cells for C++ v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من v26.7، تم وضع علامة على هذه الطريقة بأنها **مهجورة** ويجب استبدالها بواجهات برمجة التطبيقات التي تدرك الـ PivotCache المذكورة أعلاه.  
هناك سببان يجعلان نهج `RefreshData()` لكل جدول مشكلة في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤه، حتى عندما لا يكون المصدر قد تغير.  

البدائل الموصى بها هي:
المثال التالي يوضح النمط الجديد الفعّال للمصنفات التي تحتوي على جداول محورية متعددة تشترك في PivotCache واحدة.

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
    PivotTable pivotTable1 = sheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotTable pivotTable2 = sheet.GetPivotTables().Add(u"A1:C9", 14, 4);
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

## أي واجهة برمجة تطبيقات تحديث يجب أن أستخدم؟
الجدول أدناه يلخص واجهات برمجة التطبيقات المتاحة للتحديث ومتى يجب اختيار كلٍ منها.

| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-------------------------------|----------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | استدعاء واحد؛ يغطي جميع الـ PivotCaches والجداول. |
| تحديث فقط الجداول المحورية في ورقة واحدة | `Worksheet.RefreshPivotTables()` | يقتصر على ورقة عمل واحدة. |
| تغير بيانات المصدر لذاكرة مؤقتة واحدة | `pivotTable.GetPivotCache().Refresh()` | يقوم بتحديث جميع الجداول المحورية على تلك الذاكرة المشتركة. |
| تغير فقط إعدادات العرض/التخطيط | `pivotTable.CalculateData()` | يتخطى جولة غير ضرورية إلى المصدر. |
| قائمة بجميع الجداول المحورية على ذاكرة مشتركة | `pivotCache.GetPivotTables()` | استخدم للتعداد قبل التحديث الجماعي. |

عمليًا، يُفضَّل استخدام واجهات برمجة التطبيقات القائمة على الـ PivotCache على الطريقة المهجورة `RefreshData()` لكل جدول. فهي تدرك الذاكرات المشتركة، وتجنب جلب البيانات الزائد من المصدر، وتسمح لك باختيار أصغر نطاق يفي بمتطلبات التحديث.

## الأخطاء الشائعة
- **نسيان التحديث قبل الحفظ.** لا يكتب جدول محوري قيمه المعروضة في ورقة العمل إلا عندما يتم تحديث سلسلة البيانات الخاصة به. إذا قمت بتعديل خلايا المصدر، استدعِ `PivotCache.Refresh()` (أو `Workbook.RefreshAll()`) قبل `Workbook.Save()`، وإلا سيظل الملف المحفوظ يحتوي على القيم المجمّعة القديمة.  
- **استدعاء الطريقة المهجورة `RefreshData()` لكل جدول.** في v26.7، تم وضع علامة على `PivotTable.RefreshData()` بأنها مهجورة وتعيد جلب المصدر في كل استدعاء. مع وجود جداول محورية متعددة تشترك في PivotCache واحدة، يعني ذلك N عمليات جلب غير ضرورية من المصدر. استبدلها بـ `PivotCache.Refresh()` مرة واحدة ثم `CalculateData()` لكل جدول.  
- **التحديث عندما يتغير التخطيط فقط.** إذا قمت فقط بتغيير عرض جدول محوري (ترتيب الأعمدة، `ConsolidationFunction`، إلخ) دون لمس بيانات المصدر، فإن `PivotCache.Refresh()` غير ضروري وبطيء. استدعِ `pivotTable.CalculateData()` لإعادة العرض من الذاكرة الحالية.  
- **المصدر الخارجي غير مدعوم من قبل `PivotCache.Refresh()`.** إذا كان مصدر جدول محوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، إلخ)، لا يمكن لـ `PivotCache.Refresh()` تحديثه في v26.7 — فهو يدعم حاليًا نوعي المصدر `Sheet` و `Consolidation` فقط. بالنسبة للمصادر الخارجية، أعد فتح المصنف أو أعد بناء الـ PivotCache من المصدر.

{{< app/cells/assistant language="cpp" >}}