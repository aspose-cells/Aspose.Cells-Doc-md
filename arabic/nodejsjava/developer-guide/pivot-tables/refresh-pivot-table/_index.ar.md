---
title: تحديث الجداول المحورية وذاكر التخزين المؤقت في Aspose.Cells for Node.js via Java
linktitle: تحديث الجداول المحورية وذاكر التخزين المؤقت في Aspose.Cells for Node.js via Java
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Node.js via Java باستخدام واجهة API لتحديث الجداول المحورية في الإصدار v26.7+. تغطي هذه المقالة refreshAll وrefreshPivotTables وPivotCache.refresh وcalculateData وgetPivotTables مع أمثلة برمجية عملية.
keywords: Aspose.Cells, Node.js, Java, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells واجهة API متعددة الطبقات للتحديث تتيح لك إعادة تحميل بيانات الجدول المحوري عبر أربعة نطاقات مختلفة — من المصنف بأكمله إلى جدول محوري واحد. اعتبارًا من **Aspose.Cells for Node.js via Java v26.7**، أصبحت الطريقة القديمة `PivotTable.RefreshData()` مهملة، وينبغي استبدالها بواجهات API أكثر كفاءة تعتمد على ذاكرة التخزين المؤقت، كما هو موضح في هذه المقالة.
{{% /alert %}}

## مقدمة
لاanzer يكون تحديث الجدول المحوري عادةً عملية واحدة. في الخلفية، تحافظ Aspose.Cells على سلسلة بيانات ذات طبقات تربط بيانات المصدر الأصلية بالقيم المعروضة في ورقة العمل. ويعد فهم هذه السلسلة هو مفتاح اختيار واجهة API المناسبة للتحديث في كل حالة.
تتمثل سلسلة البيانات ذات الطبقات الأربع في:
1. **مصدر البيانات** — نطاقات أوراق العمل الأصلية أو استعلام قاعدة البيانات أو نطاق التوحيد، حيث توجد القيم الخام.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`، وهو المكان الذي يتم فيه جمع جميع البيانات وتلخيصها.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` من `PivotCache` *فقط*، ولا يقرأ من مصدر البيانات مباشرةً.
4. **Cells** — خلايا `Cells` في ورقة العمل، والتي يكتب فيها `PivotTable` قيمه المحسوبة وأنماطه.

{{% alert color="primary" %}}
تشير `PivotCache.SourceType` (تعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، لا تدعم `PivotCache.refresh()` سوى نوعَي المصدر **`Sheet`** و**`Consolidation`** — أي البيانات الموجودة في نطاقات أوراق العمل. ولا تزال المصادر الخارجية، مثل قواعد البيانات والاتصالات الخارجية وما إلى ذلك، غير قابلة للتحديث عبر واجهة API الخاصة بذاكرة التخزين المؤقت.
نتيجةً لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.calculateData()`** — يعيد حساب عرض جدول محوري واحد اعتمادًا على البيانات المخزنة مؤقتًا بالفعل، من دون الانتقال ذهابًا وإيابًا إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر موجودة في خلايا ورقة العمل، لذا يكون نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.
{{% /alert %}}

## بدء سريع
إذا كنت لا تحتاج سوى أقصر شيفرة ممكنة لتحديث جميع الجداول المحورية في المصنف، فكفى استدعاء واحد:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

توضح بقية هذه المقالة متى ينبغي اختيار واجهة API أكثر تحديدًا بدلًا من ذلك.

## الاستيرادات المطلوبة
- `const aspose = require('aspose.cells');`
- أو للاستيرادات المحددة: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى ضمان انعكاس أحدث بيانات المصدر في كل ذاكرة تخزين مؤقت وكل جدول محوري في المصنف، فإن واجهة API الأبسط والأكثر شمولًا هي `Workbook.refreshAll()`. يمرّ الاستدعاء الواحد عبر المصنف بأكمله — فتُحدَّث كل `PivotCache` من مصدرها ثم يُعاد حساب كل `PivotTable` تابع لها. هذه هي الطريقة الموصى بها للتحديث العام على مستوى المستند بالكامل عندما لا يكون الأداء مصدر قلق.
ينشئ المثال التالي مصنفًا يحتوي على نطاق مصدر `Fruit/Year/Amount`، وجدولًا محوريًا واحدًا، ثم يعدّل بعض قيم المصدر ويستخدم `refreshAll()` لتحديث كل شيء إلى أحدث حالة في استدعاء واحد.

```javascript
const AsposeCells = require("aspose.cells");
// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
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
// Add a pivot table: source range "A1:C9", destination cell "E3"
const pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان، لا تحتاج إلا إلى تحديث الجداول المحورية الموجودة في ورقة عمل محددة — على سبيل المثال، عندما يكون من المعروف أن الجداول المحورية في أوراق العمل الأخرى لا علاقة لها بهذا الموضوع ولا ينبغي المساس بها. في هذه الحالة، توفر Aspose.Cells واجهة `Worksheet.refreshPivotTables()`، وهي مقصورة على كائن `Worksheet` واحد.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## تحديث جدول محوري واحد
عندما تحتاج إلى تحكم دقيق في جدول محوري واحد، تمنحك واجهة API المعتمدة على ذاكرة التخزين المؤقت خيارين. ويعتمد الاختيار بينهما على العنصر الذي تغير فعليًا: بيانات المصدر الأساسية، أم إعدادات العرض أو التخطيط للجدول المحوري فحسب.

### تغيرت بيانات المصدر — استخدم `PivotCache.refresh()`
إذا تغيرت بيانات المصدر الأساسية، فالطريقة المناسبة هي `pivotTable.PivotCache.refresh()`. يعيد هذا الاستدعاء قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت، ثم يعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت هذه.

### تغير العرض أو التخطيط فقط — استخدم `calculateData()`
إذا لم تتغير بيانات المصدر، ولم تتغير سوى إعدادات العرض أو التخطيط للجدول المحوري، مثل نقل حقل إلى منطقة أخرى أو تبديل إعداد التحديث عند الفتح، فليست هناك حاجة إلى الانتقال ذهابًا وإيابًا إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة، ولا يلزم سوى إعادة حساب `PivotTable` المعروض. في هذه الحالة، يكون `pivotTable.calculateData()` هو الخيار المناسب.
يعدّل المثال التالي خاصية لا تتعلق بمصدر الجدول المحوري، ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الحالية.

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// كتابة صف رؤوس الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// كتابة 8 صفوف بيانات (الصفوف 2-9، بما يتوافق مع نطاق المصدر A1:C9)
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
// إضافة جدول محوري باسم في الخلية E3، باستخدام A1:C9 كمصدر
var pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// تعيين الحقول: Fruit إلى الصفوف، وYear إلى الأعمدة، وAmount إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// تعديل خاصية عرض أو تخطيط — هذا تغيير pertains إلى العرض فقط،
// لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// يعيد calculateData() عرض هذا الجدول المحوري (البيانات + النمط) من
// البيانات الموجودة بالفعل في PivotCache. وبما أن بيانات المصدر لم تتغير،
// فلا يتم تنفيذ رحلة ذهاب وعودة إلى المصدر — تتم إعادة حساب القيم المخزنة فقط
// في خلايا ورقة العمل.
pivotTable.calculateData();
// حفظ المصنف على القرص
workbook.save("output.xlsx");
```

يحتوي المصنف عادةً على عدة جداول محورية تشترك جميعها في ذاكرة تخزين مؤقت واحدة. ولحصرها — على سبيل المثال، قبل تنفيذ تحديث جماعي أو لتشخيص أثر ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.getPivotTables()`. تعيد هذه الدالة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المحددة.

## الانتقال من الدالة المهملة `PivotTable.RefreshData()`
قبل الإصدار Aspose.Cells for Node.js via Java v26.7، كانت الطريقة المعيارية لتحديث الجدول المحوري هي استدعاء `PivotTable.RefreshData()` لكل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، أصبحت هذه الدالة **مهملة**، وينبغي استبدالها بواجهات API المعتمدة على ذاكرة التخزين المؤقت والموضحة أعلاه.
هناك سببان يجعلان منهج `RefreshData()` المخصص لكل جدول مشكلة في مصنفات العمل الواقعية:
- يعيد جلب البيانات من المصدر *في كل مرة* يُستدعى فيها، حتى عندما لا تكون بيانات المصدر قد تغيرت.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الجديد الأكثر كفاءة للمصنفات التي تحتوي على عدة جداول محورية تشترك في ذاكرة تخزين مؤقت واحدة.

## ما واجهة API التي ينبغي استخدامها للتحديث؟
يلخص الجدول التالي واجهات API المتاحة للتحديث ومتى ينبغي اختيار كل منها.
| الهدف | واجهة API الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | استدعاء واحد؛ يشمل جميع ذاكر التخزين المؤقت والجداول المحورية. |
| تحديث الجداول المحورية في ورقة عمل واحدة فقط | `Worksheet.refreshPivotTables()` | يقتصر على ورقة عمل واحدة. |
| تغيرت بيانات المصدر الخاصة بذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.refresh()` | يحدّث جميع الجداول المحورية المرتبطة بذاكرة التخزين المؤقت المشتركة تلك. |
| تغيرت إعدادات العرض أو التخطيط فقط | `pivotTable.calculateData()` | يتجنب الانتقال غير الضروري إلى المصدر وإعادته. |
| حصر جميع الجداول المحورية المرتبطة بذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | استخدمه للحصر قبل تنفيذ تحديث جماعي. |
في الممارسة العملية، فضّل واجهات API المعتمدة على ذاكرة التخزين المؤقت بدلًا من `RefreshData()` المهملة لكل جدول. فهي تراعي ذاكر التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر الزائدة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث.

## الأخطاء الشائعة
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة بياناته. إذا عدّلت خلايا المصدر، فاستدعِ `PivotCache.refresh()` (أو `Workbook.refreshAll()`) قبل `Workbook.save()`، وإلا فسيظل الملف المحفوظ يحتوي على القيم المجمّعة القديمة.
- **استدعاء `RefreshData()` المهملة لكل جدول.** في v26.7، أصبحت `PivotTable.RefreshData()` مهملة وتعيد جلب المصدر في كل استدعاء. وعند وجود عدة جداول محورية تشترك في ذاكرة تخزين مؤقت واحدة، يعني ذلك N عمليات جلب زائدة للمصدر. استبدل هذه الطريقة باستدعاء واحد لـ `PivotCache.refresh()` يليه استدعاء `calculateData()` لكل جدول.
- **التحديث عندما يكون التخطيط فقط هو ما تغير.** إذا غيّرت عرض الجدول المحوري فقط، مثل ترتيب الأعمدة أو `ConsolidationFunction` أو ما إلى ذلك، دون المساس ببيانات المصدر، فإن استدعاء `PivotCache.refresh()` غير ضروري وبطيء. استدعِ `pivotTable.calculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الحالية.
- **مصدر خارجي لا يدعمه `PivotCache.refresh()`.** إذا كان مصدر الجدول المحوري صادرًا عن اتصال خارجي، مثل قاعدة بيانات أو مكعب OLAP أو ما إلى ذلك، فلا يمكن لـ `PivotCache.refresh()` تحديثه في v26.7؛ فهو يدعم حاليًا نوعَي المصدر `Sheet` و`Consolidation` فقط. أما المصادر الخارجية، فأعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="nodejs-java" >}}