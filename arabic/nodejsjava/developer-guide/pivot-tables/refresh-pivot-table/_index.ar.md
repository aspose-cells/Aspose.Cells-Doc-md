---
title: تحديث الجداول المحورية وذاكرة التخزين المؤقتة للجداول المحورية في Aspose.Cells for Node.js via Java
linktitle: تحديث الجداول المحورية وذاكرة التخزين المؤقتة للجداول المحورية في Aspose.Cells for Node.js via Java
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Node.js via Java باستخدام واجهة برمجة التطبيقات لتحديث الجداول المحورية في الإصدار v26.7+. تتناول هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, Node.js, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة برمجة تطبيقات تحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري ضمن أربعة نطاقات مختلفة، من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءًا من إصدار **Aspose.Cells for Node.js via Java v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` باعتبارها متقادمة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمدركة لذاكرة التخزين المؤقت الموضحة في هذه المقالة.
{{% /alert %}}

## مقدمة
نادرًا ما يكون تحديث جدول محوري عملية واحدة. وراء الكواليس، يحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات الصحيحة للتحديث في أي موقف.
سلسلة البيانات المكونة من أربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية أو استعلام قاعدة البيانات أو نطاق الدمج حيث توجد القيم الأولية.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ حيث يتم جمع جميع البيانات وتجميعها هنا.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والفلاتر. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرة من مصدر البيانات.
4. **الخلايا** — `Cells` ورقة العمل التي يعرض فيها `PivotTable` القيم المحسوبة والأنماط.

{{% alert color="primary" %}}
يشير `PivotCache.SourceType` (التعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، يدعم `PivotCache.Refresh()` فقط أنواع المصادر **`Sheet`** و **`Consolidation`**، أي البيانات الموجودة في نطاقات أوراق العمل. لا يمكن تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ.) بعد من خلال واجهة برمجة التطبيقات لذاكرة التخزين المؤقت.
{{% /alert %}}

نظرًا لهذه السلسلة، توجد مسارات تحديث أساسية في Aspose.Cells:
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون الرجوع إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات المصدر من خلايا ورقة العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.

## بداية سريعة
إذا كنت تحتاج فقط إلى أقصر كود ممكن لتحديث كل جدول محوري في المصنف، فمكالمة واحدة تكفي:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

يوضح كل شيء آخر في هذه المقالة متى تختار واجهة برمجة تطبيقات أضيق نطاقًا بدلاً من ذلك.

## الاستيرادات المطلوبة
- `const aspose = require('aspose.cells');`
- أو للاستيرادات المحددة: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى ضمان أن كل ذاكرة تخزين مؤقت للجداول المحورية وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.RefreshAll()`. تتجاوز مكالمة واحدة المصنف بأكمله، حيث تعمل على تحديث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` التابع. هذه هي الطريقة الموصى بها للتحديثات العامة والشاملة للمستندات حيث لا يكون الأداء مصدر قلق.
يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لجلب كل شيء حتى تاريخه في مكالمة واحدة.

```javascript
const AsposeCells = require("aspose.cells");
// إنشاء مصنف جديد
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// كتابة صف العناوين في الخلايا A1:C1
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
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
// تعيين حقول الجدول المحوري: Fruit إلى الصفوف، Year إلى الأعمدة، Amount إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// تعديل عدة قيم في Amount في البيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// تحديث جميع الجداول المحورية / ذاكرة التخزين المؤقتة للجدول المحوري في المصنف
workbook.refreshAll();
// حفظ المصنف
workbook.save("output.xlsx");
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة، على سبيل المثال، عندما يُعرف أن الجداول المحورية في أوراق العمل الأخرى غير مرتبطة بها ولا ينبغي لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.RefreshPivotTables()`، وهو مقصور على نسخة `Worksheet` واحدة.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## تحديث جدول محوري واحد
عندما تريد تحكمًا دقيقًا في جدول محوري واحد، توفر لك واجهة برمجة التطبيقات المعتمدة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو مجرد إعدادات العرض/التخطيط للجدول المحوري نفسه.

### تغيرت بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت هذه.

### تغير العرض/التخطيط فقط — استخدم `CalculateData()`
إذا لم تتغير بيانات المصدر *ولكن* تم تعديل إعدادات عرض الجدول المحوري أو تخطيطه فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا حاجة للرجوع إلى مصدر البيانات. تحتفظ ذاكرة التخزين المؤقت بالفعل بالبيانات الصحيحة؛ فقط يحتاج `PivotTable` المعروض إلى إعادة حساب. في هذه الحالة، `pivotTable.CalculateData()` هو الخيار الصحيح.
يعدل المثال التالي خاصية غير متعلقة بالمصدر في الجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// كتابة صف العناوين Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// كتابة 8 صفوف من البيانات (الصفوف 2-9، بما يتناسب مع نطاق المصدر A1:C9)
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
// إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، مع المصدر من A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// تعيين الحقول: Fruit إلى الصف، Year إلى العمود، Amount إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// تعديل خاصية عرض/تخطيط — هذا تغيير للعرض فقط،
// لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() يعيد عرض جدول المحوري هذا (البيانات + النمط) من
// البيانات الموجودة بالفعل في PivotCache. نظرًا لأن بيانات المصدر لم تتغير،
// لا يتم تنفيذ رحلة ذهاب وإياب إلى المصدر — فقط يتم إعادة حساب القيم المخزنة مؤقتًا
// في خلايا ورقة العمل.
pivotTable.calculateData();
// حفظ المصنف على القرص
workbook.save("output.xlsx");
```

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها، على سبيل المثال قبل تنفيذ تحديث دفعة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة، استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.

## الانتقال من `PivotTable.RefreshData()` المتقادمة
قبل Aspose.Cells for Node.js via Java v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة باعتبارها **متقادمة** ويجب استبدالها بواجهات برمجة التطبيقات المدركة لذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان يجعل نهج `RefreshData()` لكل جدول يمثل مشكلة في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤه فيها، حتى عندما لا يتغير المصدر.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الجديد الفعال للمصنفات ذات الجداول المحورية المتعددة التي تشترك في ذاكرة تخزين مؤقت واحدة.

## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل منها.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.RefreshPivotTables()` | مقصورة على ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.Refresh()` | يحدّث جميع الجداول المحورية على ذاكرة التخزين المؤقت المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.CalculateData()` | يتخطى الجولة غير الضرورية إلى المصدر. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.GetPivotTables()` | تستخدم للتعداد قبل التحديث المجمع. |
عمليًا، يفضل استخدام واجهات برمجة التطبيقات المعتمدة على ذاكرة التخزين المؤقت على `RefreshData()` المتقادمة لكل جدول. إنها مدركة لذاكرة التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر المكررة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث.

## المزالق الشائعة
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة البيانات الخاصة به. إذا قمت بتعديل خلايا المصدر، فاستدعِ `PivotCache.Refresh()` (أو `Workbook.RefreshAll()`) قبل `Workbook.save()`، وإلا فإن الملف المحفوظ لا يزال يحتوي على القيم المجمعة القديمة.
- **استدعاء `RefreshData()` المتقادمة لكل جدول.** في الإصدار v26.7، تم وضع علامة على `PivotTable.RefreshData()` كمتقادمة وتعيد جلب المصدر لكل مكالمة. مع وجود جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت، يعني ذلك N من عمليات جلب المصدر المكررة. استبدلها بمكالمة واحدة `PivotCache.Refresh()` متبوعة بـ `CalculateData()` لكل جدول.
- **التحديث عند تغير التخطيط فقط.** إذا قمت فقط بتغيير عرض الجدول المحوري (ترتيب الأعمدة، `ConsolidationFunction`، إلخ.) دون لمس بيانات المصدر، فإن `PivotCache.Refresh()` غير ضروري وبطيء. استدعِ `pivotTable.CalculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة.
- **المصدر الخارجي غير مدعوم من `PivotCache.Refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، إلخ)، فلا يمكن لـ `PivotCache.Refresh()` تحديثه في الإصدار v26.7 — فهو يدعم حاليًا أنواع المصادر `Sheet` و `Consolidation` فقط. بالنسبة للمصادر الخارجية، أعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="nodejs-java" >}}