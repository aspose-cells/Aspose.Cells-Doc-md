---
title: تحديث الجداول المحورية وذاكرة التخزين المؤقتة للجداول المحورية في Aspose.Cells for Java
linktitle: تحديث الجداول المحورية وذاكرة التخزين المؤقتة للجداول المحورية في Aspose.Cells for Java
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Java باستخدام واجهة برمجة التطبيقات للتحديث في الإصدار v26.7 وما بعده. يتناول هذا المقال RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية.
keywords: Aspose.Cells, Java, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells واجهة برمجة تطبيقات تحديث متدرجة الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري بأربعة نطاقات مختلفة — من المصنف بالكامل وحتى جدول محوري واحد. بدءًا من **Aspose.Cells for Java v26.7**، تم وضع علامة "قديم" على الطريقة التقليدية `PivotTable.refreshData()` ويجب استبدالها بواجهات البرمجة الأكثر كفاءة والمطلعة على ذاكرة التخزين المؤقت الموصوفة في هذا المقال.
{{% /alert %}}

## **مقدمة**
لا يُعد تحديث الجدول المحوري عملية واحدة عادةً. في الخلفية، تحتفظ Aspose.Cells بسلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.
سلسلة البيانات رباعية الطبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ حيث يتم جمع وتجميع كافة البيانات هنا.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرةً من مصدر البيانات.
4. **الخلايا** — `Cells` الخاصة بورقة العمل التي يعرض إليها `PivotTable` قيمه وأنماطه المحسوبة.

{{% alert color="primary" %}}
تشير `PivotCache.getSourceType()` (تعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، تدعم `PivotCache.refresh()` أنواع المصادر **`Sheet`** و **`Consolidation`** فقط — أي البيانات الموجودة في نطاقات أوراق العمل. لا يمكن تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) من خلال واجهة برمجة تطبيقات ذاكرة التخزين المؤقت حتى الآن.
{{% /alert %}}

نظرًا لهذه السلسلة، يوجد مسارا تحديث أساسيان في Aspose.Cells:
- **`PivotTable.calculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون العودة إلى مصدر البيانات.
تستخدم كافة السيناريوهات في هذا المقال بيانات مصدر من خلايا ورقة العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موصوف.

## **بداية سريعة**
إذا كنت تحتاج فقط إلى أقصر كود ممكن لتحديث كل جدول محوري في المصنف، فمكالمة واحدة تكفي:

```java
import com.aspose.cells.*;
// إنشاء مصنف جديد
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// كتابة صف الرأس في الخلايا A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر عامي 2020 و2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);
// إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// تعيين حقول الجدول المحوري: Fruit إلى الصفوف، Year إلى الأعمدة، Amount إلى البيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// تعديل عدة قيم Amount في بيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// تحديث كل جدول محوري / ذاكرة التخزين المؤقتة للجدول المحوري في المصنف
workbook.refreshAll();
// حفظ المصنف
workbook.save("output.xlsx");
```

كل شيء آخر في هذا المقال يوضح متى تختار واجهة برمجة تطبيقات أضيق نطاقًا بدلاً من ذلك.

## **عبارات الاستيراد المطلوبة**
تبدأ كافة أمثلة Java في هذا المقال بعبارات الاستيراد التالية لأن أنواع الجداول المحورية توجد في الحزمة `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## **تحديث كافة الجداول المحورية في المصنف**
عندما تحتاج إلى ضمان أن تعكس كل ذاكرة تخزين مؤقت وكل جدول محوري في المصنف أحدث بيانات مصدر، فإن أبسط واجهة برمجة تطبيقات وأكثرها شمولاً هي `Workbook.refreshAll()`. تتجاوز مكالمة واحدة المصنف بالكامل — حيث يتم تحديث كل `PivotCache` من مصدره ثم إعادة حساب كل `PivotTable` تابع. يُعد هذا النهج هو الأسلوب الموصى به لتحديث المستندات الكاملة والعامة حيث لا تمثل الأداء مصدر قلق.
يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويُعدّل بعض القيم المصدر، ثم يستخدم `refreshAll()` لجلب كل شيء حتى التاريخ في مكالمة واحدة.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## **تحديث كافة الجداول المحورية في ورقة عمل واحدة**
تحتاج أحيانًا فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما يُعرف أن الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، توفر Aspose.Cells `Worksheet.refreshPivotTables()`، التي يتم تحديد نطاقها لمثيل `Worksheet` واحد.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// كتابة صف الرأس Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// كتابة 8 صفوف من البيانات (الصفوف 2-9، مطابقة لنطاق المصدر A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);
// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، مصدره A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// تعيين الحقول: Fruit إلى Row، Year إلى Column، Amount إلى Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// تعديل خاصية عرض/تخطيط -- هذا تغيير للعرض فقط،
// لذلك لا يتطلب إعادة قراءة البيانات المصدر من خلال PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() يعيد عرض هذا الجدول المحوري (البيانات + النمط) من
// البيانات الموجودة بالفعل في PivotCache. نظراً لأن البيانات المصدر لم تتغير،
// لا يتم تنفيذ رحلة ذهاب وإياب إلى المصدر -- يتم فقط إعادة حساب القيم المخزنة مؤقتاً
// في خلايا ورقة العمل.
pivotTable.calculateData();
// حفظ المصنف على القرص
workbook.save("output.xlsx");
```

## **تحديث جدول محوري واحد**
عندما تريد تحكمًا دقيقًا في جدول محوري واحد، تمنحك واجهة البرمجة المعتمدة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغيّر فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه فقط.

### **تغيّرت بيانات المصدر — استخدم `PivotCache.refresh()`**
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.getPivotCache().refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة.

### **تغيّر العرض/التخطيط فقط — استخدم `calculateData()`**
إذا *لم* تتغير بيانات المصدر ولكن تم تعديل إعدادات عرض أو تخطيط الجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتفظ ذاكرة التخزين المؤقت بالفعل بالبيانات الصحيحة؛ يحتاج فقط `PivotTable` المعروض إلى إعادة الحساب. في هذه الحالة، `pivotTable.calculateData()` هو الخيار الصحيح.
يُعدّل المثال التالي خاصية غير مصدر للجدول المحوري ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.
غالبًا ما يحتوي المصنف على عدة جداول محورية كلها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل تنفيذ تحديث دفعة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.getPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.

## **الانتقال من `PivotTable.refreshData()` القديمة**
قبل Aspose.Cells for Java v26.7، كانت الطريقة المعيارية لتحديث جدول محوري هي استدعاء `PivotTable.refreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة **قديم** على هذه الطريقة ويجب استبدالها بواجهات البرمجة المطلعة على ذاكرة التخزين المؤقت الموصوفة أعلاه.
هناك سببان لكون نهج `refreshData()` لكل جدول على حدة إشكاليًا في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر *في كل* مرة يتم استدعاؤها، حتى عندما لا يتغير المصدر.
البدائل الموصى بها هي:
يُظهر المثال التالي النمط الفعّال الجديد للمصنفات ذات الجداول المحورية المتعددة التي تشترك في ذاكرة تخزين مؤقت واحدة.

## **أي واجهة برمجة تطبيقات للتحديث ينبغي أن أستخدم؟**
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة منها.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | مكالمة واحدة؛ تغطي كل ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.refreshPivotTables()` | محددة النطاق بورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.getPivotCache().refresh()` | يحدث جميع الجداول المحورية على تلك الذاكرة المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.calculateData()` | يتخطى رحلة العودة غير الضرورية إلى المصدر. |
| سرد كل الجداول المحورية على ذاكرة تخزين مشتركة | `pivotCache.getPivotTables()` | استخدم للتعداد قبل التحديث بالجملة. |
عمليًا، فضّل واجهات البرمجة المعتمدة على ذاكرة التخزين المؤقت على `refreshData()` القديمة لكل جدول على حدة. إنها مطلعة على ذاكرات التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر الزائدة عن الحاجة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث لديك.

## **الأخطاء الشائعة**
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة البيانات الخاصة به. إذا قمت بتعديل خلايا المصدر، فاستدعِ `PivotCache.Refresh()` (أو `Workbook.RefreshAll()`) قبل `Workbook.save()`، وإلا فإن الملف المحفوظ سيظل يحتوي على القيم المجمّعة القديمة.
- **استدعاء `RefreshData()` القديمة لكل جدول.** في الإصدار v26.7، تم وضع علامة قديم على `PivotTable.RefreshData()` وهي تعيد جلب المصدر لكل استدعاء. مع وجود جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت، يعني هذا وجود عدد N من عمليات جلب المصدر الزائدة عن الحاجة. استبدلها بمكالمة `PivotCache.Refresh()` واحدة متبوعة بـ `CalculateData()` لكل جدول.
- **التحديث عند تغير التخطيط فقط.** إذا غيرت فقط عرض الجدول المحوري (ترتيب الأعمدة، `ConsolidationFunction`، إلخ) دون لمس بيانات المصدر، فإن `PivotCache.Refresh()` غير ضروري وبطيء. استدعِ `pivotTable.CalculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة.
- **المصدر الخارجي غير مدعوم من قِبل `PivotCache.Refresh()`.** إذا كان مصدر الجدول المحوري قادمًا من اتصال خارجي (قاعدة بيانات، مكعب OLAP، إلخ)، فلا يمكن لـ `PivotCache.Refresh()` تحديثه في الإصدار v26.7 — فهو حاليًا يدعم فقط أنواع المصادر `Sheet` و `Consolidation`. بالنسبة للمصادر الخارجية، أعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="java" >}}