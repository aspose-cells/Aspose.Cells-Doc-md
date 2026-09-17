---
title: تحديث الجداول المحورية وذاكرة التخزين المؤقتة للجداول المحورية في Aspose.Cells for Node.js via C++
linktitle: تحديث الجداول المحورية وذاكرة التخزين المؤقتة للجداول المحورية في Aspose.Cells for Node.js via C++
description: تعلم كيفية تحديث الجداول المحورية في Aspose.Cells for Node.js via C++ باستخدام واجهة برمجة تطبيقات تحديث المحور في الإصدار v26.7+، تتناول هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية على الكود.
keywords: Aspose.Cells, Node.js via C++, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة برمجة تطبيقات تحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات المحور بأربعة نطاقات مختلفة — من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Node.js via C++ v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.RefreshData()` على أنها قديمة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمدركة لذاكرة التخزين المؤقت الموضحة في هذه المقالة.
{{% /alert %}}

## مقدمة
نادرًا ما تكون عملية تحديث جدول محوري عملية واحدة. في الخلفية، يحتفظ Aspose.Cells بسلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو مفتاح اختيار واجهة برمجة التطبيقات المناسبة للتحديث لأي موقف.
سلسلة البيانات المكونة من أربع طبقات هي:
1. **مصدر البيانات** — نطاقات أوراق العمل الأصلية أو استعلام قاعدة البيانات أو نطاق التجميع حيث توجد القيم الخام.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. يتم بناء كل جدول محوري فوق `PivotCache`؛ حيث يتم جمع جميع البيانات وتجميعها.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصف والعمود والقيمة والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس أبدًا من مصدر البيانات مباشرة.
4. **الخلايا** — `Cells` الخاصة بورقة العمل التي يقوم `PivotTable` بعرض القيم والأنماط المحسوبة فيها.

{{% alert color="primary" %}}
يشير `PivotCache.SourceType` (تعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، تدعم `PivotCache.Refresh()` أنواع المصادر **`Sheet`** و**`Consolidation`** فقط — أي البيانات الموجودة في نطاقات أوراق العمل. المصادر الخارجية (قواعد البيانات والاتصالات الخارجية وما إلى ذلك) لا يمكن تحديثها بعد من خلال واجهة برمجة التطبيقات لذاكرة التخزين المؤقت.
{{% /alert %}}

نظرًا لهذه السلسلة، هناك مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.CalculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون الحاجة إلى رحلة ذهاب وإاب إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر خلايا ورقة العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.

## بداية سريعة
إذا كنت تحتاج فقط إلى أقصر كود ممكن يحدث كل محور في المصنف، فمكالمة واحدة كافية:

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// تعيين حقول الجدول المحوري: الفاكهة إلى الصفوف، السنة إلى الأعمدة، المبلغ إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// تعديل عدة قيم للمبلغ في بيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// تحديث جميع الجداول المحورية / ذاكرة التخزين المؤقت المحورية في المصنف
workbook.refreshAll();
// حفظ المصنف
workbook.save("output.xlsx");
```

كل شيء آخر في هذه المقالة يشرح متى تختار واجهة برمجة تطبيقات أضيق بدلاً من ذلك.

## الاستيرادات المطلوبة
تفترض جميع أمثلة JavaScript في هذه المقالة أنه تم تحميل وحدة Aspose.Cells for Node.js via C++ وأن أنواع المحور تعيش في مساحة الاسم `Aspose.Cells.Pivot`. الإعداد النموذجي هو:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (أو الوصول عبر `AsposeCells.Pivot.PivotFieldType`)

## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت للمحور وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.RefreshAll()`. تتنقل مكالمة واحدة عبر المصنف بأكمله — حيث تحدث كل `PivotCache` من مصدرها ثم تعيد حساب كل `PivotTable` التابع. هذا هو النهج الموصى به للتحديثات العامة والشاملة للمستندات حيث لا يمثل الأداء مصدر قلق.
يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `RefreshAll()` لجلب كل شيء حتى التاريخ في مكالمة واحدة.

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

## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية التي تعيش في ورقة عمل واحدة محددة — على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا يجب لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.RefreshPivotTables()`، والتي يتم تحديد نطاقها لمثيل `Worksheet` واحد.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// كتابة 8 دقائق من البيانات (الدقائق 2-9، تناسب نطاق المصدر A1:C9)
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
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// تعيين الحقول: الفاكهة إلى الصف، السنة إلى العمود، المبلغ إلى البيانات
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");
// تعديل خاصية عرض/تخطيط — هذا تغيير للعرض فقط،
// لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() يعيد عرض جدول المحور هذا (البيانات + النمط) من
// البيانات الموجودة بالفعل في PivotCache. نظرًا لأن بيانات المصدر لم تتغير،
// لا يتم تنفيذ رحلة ذهاب وإاب إلى المصدر — فقط يتم إعادة حساب القيم المخزنة مؤقتًا
// في خلايا ورقة العمل.
pivotTable.calculateData();
// حفظ المصنف على القرص
workbook.save("output.xlsx");
```

## تحديث جدول محوري واحد
عندما تريد التحكم الدقيق في جدول محوري واحد، فإن واجهة برمجة التطبيقات المستندة إلى ذاكرة التخزين المؤقت تمنحك خيارين. الاختيار بينهما يعتمد على ما تغير بالفعل: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه فقط.

### تغيرت بيانات المصدر — استخدم `PivotCache.Refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.PivotCache.Refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة المؤقتة.

### تغير العرض/التقييم فقط — استخدم `CalculateData()`
إذا لم تتغير بيانات المصدر ولكن تم تعديل إعدادات العرض أو التقييم للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح), فلا حاجة للذهاب والعودة إلى مصدر البيانات. تحتوي الذاكرة المؤقتة بالفعل على البيانات الصحيحة؛ فقط `PivotTable` المعروض يحتاج إلى إعادة حساب. في هذه الحالة، `pivotTable.CalculateData()` هو الخيار الصحيح.
يعدل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `CalculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.
غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس جميعها فوق ذاكرة تخزين مؤقت واحدة مشتركة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.GetPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.

## الترحيل من `PivotTable.RefreshData()` القديمة
قبل Aspose.Cells for Node.js via C++ v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.RefreshData()` على كل جدول متوري على حدة. اعتبارًا من v26.7، تم وضع علامة على هذه الطريقة على أنها **قديمة** ويجب استبدالها بواجهات برمجة التطبيقات المدركة لذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان يجعل نهج `RefreshData()` لكل جدول إشكاليًا في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر *في كل* مرة يتم استدعاؤه فيها، حتى عندما لم يتغير المصدر.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الفعال الجديد للمصنفات ذات الجداول المحورية المتعددة التي تشترك في ذاكرة تخزين مؤقت واحدة.

## ما هي واجهة برمجة تطبيقات التحديث التي يجب أن أستخدمها؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.RefreshAll()` | مكالمة واحدة؛ تغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية فقط في ورقة واحدة | `Worksheet.RefreshPivotTables()` | محددة ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.Refresh()` | تحدث جميع الجداول المحورية على تلك الذاكرة المؤقتة المشتركة. |
| تغيرت إعدادات العرض/التقييم فقط | `pivotTable.CalculateData()` | تتجاوز رحلة المصدر غير الضرورية. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.GetPivotTables()` | تستخدم للتعداد قبل التحديث المجمع. |
عمليًا، فضل واجهات برمجة التطبيقات المستندة إلى ذاكرة التخزين المؤقت على `RefreshData()` القديمة لكل جدول. إنها مدركة لذاكرة التخزين المؤقت المشتركة، وتتجنب جلب المصدر الزائد عن الحاجة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث الخاصة بك.

## المزالق الشائعة
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة البيانات الخاصة به. إذا قمت بتعديل خلايا المصدر، فاستدعِ `PivotCache.Refresh()` (أو `Workbook.RefreshAll()`) قبل `Workbook.save()`، وإلا فإن الملف المحفوظ لا يزال يحتوي على القيم المجمعة القديمة.
- **استدعاء `RefreshData()` القديمة لكل جدول.** في الإصدار v26.7، تم وضع علامة على `PivotTable.RefreshData()` على أنها قديمة وتعيد جلب المصدر لكل مكالمة. مع وجود جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت، فهذا يعني N من جلب المصدر الزائد. استبدلها بـ `PivotCache.Refresh()` واحدة متبوعة بـ `CalculateData()` لكل جدول.
- **التحديث عند تغيير التقييم فقط.** إذا قمت بتغيير عرض الجدول المحوري فقط (ترتيب الأعمدة، `ConsolidationFunction`، وما إلى ذلك) دون لمس بيانات المصدر، فإن `PivotCache.Refresh()` غير ضروري وبطيء. استدعِ `pivotTable.CalculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة.
- **المصدر الخارجي غير مدعوم من قبل `PivotCache.Refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، وما إلى ذلك)، فلا يمكن لـ `PivotCache.Refresh()` تحديثه في v26.7 — فهو يدعم حاليًا أنواع المصادر `Sheet` و`Consolidation` فقط. بالنسبة للمصادر الخارجية، أعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}