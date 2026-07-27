---
title: تحديث الجداول المحورية وذاكرة التخزين المؤقتة في Aspose.Cells لـ .NET
linktitle: تحديث الجداول المحورية
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Java باستخدام واجهة برمجة التطبيقات v26.7+ الخاصة بتحديث الجداول المحورية. تغطي هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يوفر Aspose.Cells واجهة برمجة تطبيقات تحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري بأربعة نطاقات مختلفة، بدءاً من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءاً من الإصدار **Aspose.Cells for Java v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.refreshData()` على أنها مهملة، ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمبنية على ذاكرة التخزين المؤقت الموضحة في هذه المقالة.

{{% /alert %}}

## مقدمة

نادراً ما تكون عملية تحديث الجدول المحوري عملية واحدة. خلف الكواليس، يحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة مفتاحاً لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.

سلسلة البيانات المكونة من أربع طبقات هي:

1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. كل جدول محوري مبني فوق `PivotCache`؛ حيث يتم جمع جميع البيانات وتجميعها هنا.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` من `PivotCache` الخاص به *فقط*، وليس مباشرة من مصدر البيانات.
4. **الخلايا** — خلايا ورقة العمل `Cells` التي يقوم `PivotTable` بعرض قيمه وأنماطه المحسوبة فيها.

من المفاهيم المهمة بشكل خاص **ذاكرة التخزين المؤقت المشتركة**. عندما تشير جداول محورية متعددة في مصنف إلى نفس نطاق المصدر، فإنها تتشارك *مثيل* واحد من `PivotCache`. يمكن أن يشير العديد من الجداول المحورية إلى `PivotCache` واحد، ويؤدي تحديث ذاكرة التخزين المؤقت تلك إلى تحديث كل `PivotTable` معتمد عليها في وقت واحد.

{{% alert color="primary" %}}

يشير `PivotCache.getSourceType()` (تعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتباراً من الإصدار 26.7، تدعم `PivotCache.refresh()` أنواع المصدر **`Sheet`** و**`Consolidation`** فقط — أي البيانات الموجودة في نطاقات أوراق العمل. لا يمكن تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، وما إلى ذلك) بعد من خلال واجهة برمجة التطبيقات الخاصة بذاكرة التخزين المؤقت.

{{% /alert %}}

نظراً لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:

- **`PivotCache.refresh()`** — يعيد تحميل المصدر إلى ذاكرة التخزين المؤقت ويعيد حساب جميع `PivotTable` المعتمدة في عملية واحدة.
- **`PivotTable.calculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتاً بالفعل، دون العودة إلى مصدر البيانات.

تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر خلايا ورقة العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.

## عبارات الاستيراد المطلوبة

تبدأ جميع أمثلة Java في هذه المقالة بعبارات الاستيراد التالية لأن أنواع الجداول المحورية موجودة في حزمة `com.aspose.cells.pivot`:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## تحديث جميع الجداول المحورية في المصنف

عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت للجدول المحوري وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط واجهات برمجة التطبيقات وأكثرها شمولاً هي `Workbook.refreshAll()`. تعبر هذه المكالمة الواحدة المصنف بأكمله، حيث تقوم بتحديث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` معتمد. هذه هي الطريقة الموصى بها للتحديثات العامة والشاملة للمستند حيث لا يكون الأداء مقلقاً.

يبني المثال التالي مصنفاً بنطاق مصدر Fruit/Year/Amount، وينشئ جدولاً محورياً واحداً، ويعدل بعض قيم المصدر، ثم يستخدم `refreshAll()` لتحديث كل شيء في مكالمة واحدة.

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

// تعديل عدة قيم Amount في البيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// تحديث جميع الجداول المحورية / ذاكرة التخزين المؤقت للمحور في المصنف
workbook.refreshAll();

// حفظ المصنف
workbook.save("output.xlsx");
```

## تحديث جميع الجداول المحورية على ورقة عمل واحدة

في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية الموجودة على ورقة عمل واحدة محددة، على سبيل المثال، عندما يكون من المعروف أن الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا يجب لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.refreshPivotTables()`، والتي تكون محددة النطاق بمثيل `Worksheet` واحد.

هذه الطريقة أكثر انتقائية من `Workbook.refreshAll()`: يتم تحديث الجداول المحورية الموجودة على ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية في أوراق العمل الأخرى دون تغيير.

يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويضيف جدولاً محورياً على ورقة العمل الأولى، ويعدل بعض قيم المصدر، ثم يحدّث فقط الجداول المحورية في ورقة العمل تلك.

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

## تحديث جدول محوري واحد

عندما تريد تحكماً دقيقاً في جدول محوري واحد، تمنحك واجهة برمجة التطبيقات المبنية على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعلياً: بيانات المصدر الأساسية، أو مجرد إعدادات العرض/التخطيط للجدول المحوري نفسه.

### تغيرت بيانات المصدر — استخدم `PivotCache.refresh()`

إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.getPivotCache().refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت هذه.

{{% alert color="primary" %}}

نظراً لأن الجداول المحورية تتشارك مثيل `PivotCache` واحد، فإن استدعاء `PivotCache.refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على نفس ذاكرة التخزين المؤقت، وليس فقط الجدول الذي تشير إليه. إذا كان جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث ذاكرة تخزين مؤقت واحدة يحدّث كليهما.

{{% /alert %}}

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لتوضيح سلوك ذاكرة التخزين المؤقت المشتركة، ويعدل بعض قيم المصدر، ثم يحدّث من خلال مرجع ذاكرة تخزين مؤقت واحد.

```java
import com.aspose.cells.*;

// إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// كتابة صف الرأس: فاكهة / سنة / كمية
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// كتابة حوالي 9 صفوف من البيانات (عنب / توت أزرق / كيوي / كرز عبر 2020-2021)
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// إضافة أول جدول محوري "Pivot1" مرساة في الخلية E3، نطاق المصدر A1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// تعيين الحقول لـ Pivot1
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// إضافة جدول محوري ثانٍ "Pivot2" مرساة في E15 باستخدام نفس نطاق المصدر A1:C9
// كل من Pivot1 و Pivot2 يشتركان في PivotCache واحد لأن نطاق المصدر متطابق.
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// تعيين نفس الحقول لـ Pivot2
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// تعديل عدة قيم خلايا الكمية في بيانات المصدر لمحاكاة تغيير في البيانات
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// تحديث PivotCache المشترك.
// نظرًا لأن Pivot1 و Pivot2 يشتركان في نفس PivotCache، فإن هذه المكالمة الواحدة
// تقوم بتحديث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المحدّث.
pivotTable1.refreshData();

// حفظ المصنف
workbook.save("output.xlsx");
```

### تغير عرض/التخطيط فقط — استخدم `calculateData()`

إذا لم تتغير بيانات المصدر ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا داعي للعودة إلى مصدر البيانات. تحتفظ ذاكرة التخزين المؤقت بالفعل بالبيانات الصحيحة؛ لا يحتاج سوى `PivotTable` المعروض إلى إعادة حساب. في هذه الحالة، يكون `pivotTable.calculateData()` هو الخيار الصحيح.

يتجنب ذلك جلب المصدر غير الضروري وهو أسرع بكثير عندما تتشارك جداول محورية كثيرة في نفس ذاكرة التخزين المؤقت.

يعدل المثال التالي خاصية غير متعلقة بالمصدر في الجدول المحوري ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// كتابة صف الترويسة Fruit / Year / Amount
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

// إضافة جدول محوري باسم "Pivot1" موضوع في الخلية الوجهة E3، مع المصدر من A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تعيين الحقول: Fruit إلى الصف، Year إلى العمود، Amount إلى البيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// تعديل خاصية عرض/تخطيط -- هذا تغيير خاص بالعرض فقط،
// لذلك لا يتطلب إعادة قراءة البيانات المصدر عبر PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() يعيد عرض عرض هذا الجدول المحوري (البيانات + النمط) من
// البيانات المحفوظة بالفعل في PivotCache. نظرًا لأن البيانات المصدر لم تتغير،
// لا يتم إجراء رحلة ذهاب وإياب إلى المصدر -- فقط القيم المخزنة مؤقتًا يتم إعادة حسابها
// في خلايا ورقة العمل.
pivotTable.calculateData();

// حفظ المصنف على القرص
workbook.save("output.xlsx");
```

## الحصول على جميع الجداول المحورية المشاركة في نفس PivotCache

غالباً ما يحتوي المصنف على العديد من الجداول المحورية التي تقع جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها، على سبيل المثال، قبل إجراء تحديث دفعي، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة، استخدم `PivotCache.getPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المحددة.

هذه أيضاً أكثر طريقة مباشرة للتأكد من أن جدولين محوريين يتشاركان فعلاً نفس مثيل `PivotCache`: يمكنك مقارنة مراجع ذاكرة التخزين المؤقت (باستخدام عامل التشغيل `==`)، أو ببساطة تكرار المجموعة التي يعرضها `getPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان نفس مثيل ذاكرة التخزين المؤقت، ثم يعدد جداول ذاكرة التخزين المؤقت المحورية.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

int pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

boolean sameCache = pivotTable1.getPivotCache() == pivotTable2.getPivotCache();
System.out.println("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
System.out.println("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (PivotTable pt : sharedPivotTables)
{
    System.out.println("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## الانتقال من `PivotTable.refreshData()` المهجور

قبل Aspose.Cells for Java v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.refreshData()` على كل جدول محوري على حدة. اعتباراً من الإصدار 26.7، تم وضع علامة **مهجورة** على هذه الطريقة ويجب استبدالها بواجهات برمجة التطبيقات المبنية على ذاكرة التخزين المؤقت والموصوفة أعلاه.

هناك سببان يجعلان نهج `refreshData()` لكل جدول يمثل مشكلة في المصنفات الحقيقية:

- يعيد جلب البيانات من المصدر *في كل* مرة يتم استدعاؤها، حتى عندما لا يتغير المصدر.
- تعمل كل مكالمة على تحديث ذاكرة التخزين المؤقت المشتركة بالكامل. عندما تتشارك جداول محورية كثيرة في ذاكرة تخزين مؤقت واحدة، فإن استدعاء `refreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس ذاكرة التخزين المؤقت مراراً وتكراراً، وهو بطيء جداً.

البدائل الموصى بها هي:

- **تحديث جميع الجداول المحورية في المصنف** ← استخدم `workbook.refreshAll();`
- **تحديث بعضها** ← استخدم `pivotTable.getPivotCache().refresh();` لذاكرة تخزين مؤقت واحدة. نظراً لأن ذاكرة التخزين المؤقت مشتركة، فإن هذه المكالمة الواحدة تحدّث كل جدول محوري مبني فوق ذاكرة التخزين المؤقت تلك. يمكن بأمان تخطي الجداول المحورية الأخرى التي تقع على ذاكرة تخزين مؤقت تم تحديثها بالفعل.
- **تغير عرض/تخطيط الجدول المحوري فقط** ← استخدم `pivotTable.calculateData();` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة دون أي رحلة ذهاب وإياب إلى المصدر.

يوضح المثال التالي النمط الجديد والفعال للمصنفات التي تحتوي على جداول محورية متعددة تتشارك ذاكرة تخزين مؤقت واحدة.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- بناء بيانات المصدر: الفاكهة / السنة / المبلغ (العنوان + 9 صفوف) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- إضافة الجدول المحوري الأول (Pivot1) في خلية الوجهة E3 ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- إضافة الجدول المحوري الثاني (Pivot2) على نفس نطاق المصدر ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- تعديل عدة قيم للمبلغ في بيانات المصدر ---
sheet.getCells().get("C2").putValue(5000);   // عنب 2020
sheet.getCells().get("C5").putValue(7500);   // كرز 2020
sheet.getCells().get("C9").putValue(9500);   // كرز 2021

// --- نمط v26.7+ الجديد: تحديث ذاكرة التخزين المؤقت مرة واحدة، ثم إعادة العرض حسب الحاجة ---
pivotTable1.getPivotCache().refresh();

// إعادة عرض عرض/تخطيط الجدول المحوري الثاني دون لمس المصدر
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟

يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة منها.

| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | مكالمة واحدة؛ تغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية فقط في ورقة واحدة | `Worksheet.refreshPivotTables()` | محددة النطاق بورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.getPivotCache().refresh()` | يحدّث جميع الجداول المحورية على تلك ذاكرة التخزين المؤقت المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.calculateData()` | يتجاوز رحلة الذهاب والإياب غير الضرورية إلى المصدر. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | استخدمه للتعداد قبل التحديث بالجملة. |

عملياً، يُفضل استخدام واجهات برمجة التطبيقات المبنية على ذاكرة التخزين المؤقت على `refreshData()` المهمل لكل جدول. إنها على دراية بذاكرات التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر الزائدة عن الحاجة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث الخاصة بك.

{{< app/cells/assistant language="java" >}}