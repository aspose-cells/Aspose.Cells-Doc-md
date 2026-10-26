---
title: تحديث الجداول المحورية وذاكرات التخزين المؤقت في Aspose.Cells for Node.js via C++
linktitle: تحديث الجداول المحورية وذاكرات التخزين المؤقت في Aspose.Cells for Node.js via C++
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Node.js via C++ باستخدام واجهة pivot-refresh API في v26.7+. تغطي هذه المقالة refreshAll وrefreshPivotTables وPivotCache.refresh وcalculateData وgetPivotTables مع أمثلة برمجية عملية.
keywords: Aspose.Cells, Node.js via C++, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells واجهة تحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجداول المحورية عبر أربعة نطاقات مختلفة، من المصنف بأكمله إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Node.js via C++ v26.7**، أصبحت الطريقة القديمة `PivotTable.RefreshData()` مهملة، ويجب استبدالها بواجهات أكثر كفاءة تعتمد على ذاكرة التخزين المؤقت، كما هو موضح في هذه المقالة.
{{% /alert %}}

## Introduction
نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. في الخلفية، تحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة في ورقة العمل. ويعد فهم هذه السلسلة هو المفتاح لاختيار واجهة التحديث المناسبة لأي حالة.
سلسلة البيانات ذات الطبقات الأربع هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية أو استعلام قاعدة البيانات أو نطاق التوحيد الذي توجد فيه القيم الخام.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. كل جدول محوري مبني على `PivotCache`، وتُجمع البيانات وتُلخص في هذه الذاكرة.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم وعوامل التصفية. لا يقرأ `PivotTable` إلا من `PivotCache`، ولا يقرأه مباشرةً من مصدر البيانات.
4. **Cells** — خلايا ورقة العمل `Cells` التي يُدرج فيها `PivotTable` قيمه المحسوبة وأنماطه.

{{% alert color="primary" %}}
تحدد السمة `PivotCache.SourceType`، وهي نوع التعداد `PivotTableSourceType`، مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من v26.7، لا يدعم `PivotCache.refresh()` سوى نوعَي المصدر **`Sheet`** و**`Consolidation`**، أي البيانات الموجودة في نطاقات أوراق العمل. ولا تزال المصادر الخارجية، مثل قواعد البيانات والاتصالات الخارجية، غير مدعومة عبر واجهة ذاكرة التخزين المؤقت.
نظرًا لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.calculateData()`** — يعيد حساب عرض جدول محوري واحد من البيانات الموجودة بالفعل في ذاكرة التخزين المؤقت، دون الحاجة إلى رحلة ذهاب وإياب إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة خلايا ورقة العمل كمصدر للبيانات، لذلك يكون نوع المصدر `Sheet` وتتصرف عمليات التحديث كما هو موضح.
{{% /alert %}}

## Quick Start
إذا كنت تحتاج فقط إلى أقصر код ممكن لتحديث كل جدول محوري في المصنف، فستكفيك مكالمة واحدة:

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

يوضح كل ما يتبقى في هذه المقالة متى ينبغي اختيار واجهة أكثر تحديدًا بدلاً من ذلك.

## Required Imports
تفترض جميع أمثلة JavaScript في هذه المقالة أنه تم تحميل وحدة Aspose.Cells for Node.js via C++ وأن أنواع الجداول المحورية موجودة في namespace ‏`Aspose.Cells.Pivot`. أحد الإعدادات المعتادة هو:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` أو الوصول إليها عبر `AsposeCells.Pivot.PivotFieldType`

## Refresh All Pivot Tables in the Workbook
عندما تريد التأكد من أن جميع ذاكر التخزين المؤقت وجميع الجداول المحورية في المصنف تعكس أحدث بيانات المصدر، تكون أبسط واجهة وأكثرها شمولًا هي `Workbook.refreshAll()`. تعبر المكالمة الواحدة المصنف بأكمله، فتعيد تحديث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` يعتمد عليه. هذه هي الطريقة الموصى بها للتحديث العام لكامل المستند عندما لا يمثل الأداء مصدر قلق.
يبني المثال التالي مصنفًا يتضمن نطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ثم يعدل بعض قيم المصدر، ويستخدم `refreshAll()` لتحديث جميع العناصر في مكالمة واحدة.

```javascript
const AsposeCells = require("aspose.cells.node");
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
// إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// تعيين حقول الجدول المحوري: Fruit إلى الصفوف، Year إلى الأعمدة، Amount إلى البيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// تعديل عدة قيم Amount في بيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// تحديث كل جدول محوري / ذاكرة تخزين مؤقت في المصنف
workbook.refreshAll();
// حفظ المصنف
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
في بعض الحالات، قد تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل محددة، على سبيل المثال، عندما يكون واضحًا أن الجداول المحورية في أوراق العمل الأخرى غير مرتبطة ولا ينبغي المساس بها. في هذه الحالة، توفر Aspose.Cells الواجهة `Worksheet.refreshPivotTables()`، وهي مقتصرة على مثيل `Worksheet` واحد.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
عندما تحتاج إلى التحكم الدقيق في جدول محوري واحد، توفر واجهة التحديث المعتمدة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعلًا: بيانات المصدر الأساسية، أم إعدادات العرض أو التخطيط الخاصة بالجدول المحوري نفسه.

### Source Data Changed — Use `PivotCache.refresh()`
إذا تغيرت بيانات المصدر الأساسية، تكون نقطة الدخول المناسبة هي `pivotTable.PivotCache.refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت، ثم تعيد حساب كل `PivotTable` يعتمد على هذه الذاكرة.

### Only View/Layout Changed — Use `calculateData()`
إذا لم تتغير بيانات المصدر، ولكن تم تعديل إعدادات العرض أو التخطيط الخاصة بالجدول المحوري فقط، مثل نقل حقل إلى منطقة أخرى أو تغيير إعداد التحديث عند الفتح، فلا حاجة إلى رحلة ذهاب وإياب إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة، ولا يلزم سوى إعادة حساب `PivotTable` المعروض. في هذه الحالة، يكون `pivotTable.calculateData()` هو الخيار المناسب.
يعدّل المثال التالي خاصية لا تتعلق بالمصدر للجدول المحوري، ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الحالية.

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// كتابة صف الرأس Fruit / Year / Amount
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
// إضافة جدول محور باسم موضوعًا في خلية الوجهة E3، مع مصدر A1:C9
var pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// تعيين الحقول: Fruit إلى Row، Year إلى Column، Amount إلى Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// تعديل خاصية عرض/تخطيط — وهذا تغيير خاص بالعرض فقط،
// لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// يعيد calculateData() عرض هذا الجدول المحوري (بيانات + نمط) من
// البيانات الموجودة بالفعل في PivotCache. وبما أن بيانات المصدر لم تتغير،
// فلا يتم تنفيذ رحلة ذهاب وإياب إلى المصدر — بل تُعاد فقط القيم المخزنة مؤقتًا
// إلى خلايا ورقة العمل.
pivotTable.calculateData();
// حفظ المصنف على القرص
workbook.save("output.xlsx");
```

غالبًا ما يحتوي المصنف على عدة جداول محورية تعتمد جميعها على ذاكرة تخزين مؤقت مشتركة واحدة. لحصرها، على سبيل المثال، قبل تنفيذ تحديث جماعي أو لتشخيص أثر ذاكرة التخزين المؤقت المشتركة، استخدم `PivotCache.getPivotTables()`. تعيد هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المحددة.

## Migrating from the Obsolete `PivotTable.RefreshData()`
قبل Aspose.Cells for Node.js via C++ v26.7، كانت الطريقة المعتادة لتحديث الجدول المحوري هي استدعاء `PivotTable.RefreshData()` لكل جدول محوري على حدة. اعتبارًا من v26.7، أصبحت هذه الطريقة **مهملة**، ويجب استبدالها بواجهات التحديث المعتمدة على ذاكرة التخزين المؤقت والموضحة أعلاه.
هناك سببان يجعل نهج `RefreshData()` لكل جدول مشكلة في المصنفات المستخدمة في العالم الحقيقي:
- يعيد جلب البيانات من المصدر *كل* مرة يُستدعى فيها، حتى عندما لا تكون بيانات المصدر قد تغيرت.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الجديد الأكثر كفاءة للمصنفات التي تحتوي على جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت واحدة.

## Which Refresh API Should I Use?
يلخص الجدول التالي واجهات التحديث المتاحة ومتى ينبغي اختيار كل منها.
| الهدف | واجهة API المقترحة | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | مكالمة واحدة تشمل جميع ذاكر التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة عمل واحدة فقط | `Worksheet.refreshPivotTables()` | مقتصرة على ورقة عمل واحدة. |
| تغيرت بيانات المصدر الخاصة بذاكرة تخزين مؤقت واحدة | `pivotTable.PivotCache.refresh()` | تحدّث جميع الجداول المحورية المرتبطة بذاكرة التخزين المؤقت المشتركة. |
| تغيرت إعدادات العرض أو التخطيط فقط | `pivotTable.calculateData()` | تتجنب الانتقال غير الضروري إلى المصدر. |
| حصر جميع الجداول المحورية المرتبطة بذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | استخدمها للحصر قبل التحديث المجمع. |
في الواقع، تُفضّل واجهات API المعتمدة على ذاكرة التخزين المؤقت بدلًا من `RefreshData()` المهملة لكل جدول. فهي تراعي ذاكر التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر المكررة، وتتيح لك اختيار أصغر نطاق يحقق متطلبات التحديث.

## Common Pitfalls
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة البيانات التي يعتمد عليها. إذا عدلت خلايا المصدر، فاستدعِ `PivotCache.refresh()` أو `Workbook.refreshAll()` قبل `Workbook.save()`، وإلا فسيظل الملف المحفوظ يحتوي على القيم المجمّعة القديمة.
- **استدعاء `RefreshData()` المهملة لكل جدول.** في v26.7، أصبحت `PivotTable.RefreshData()` مهملة، كما أنها تعيد جلب المصدر في كل استدعاء. مع وجود عدة جداول محورية تشترك في ذاكرة التخزين المؤقت، يعني ذلك N عمليات جلب زائدة عن الحاجة للمصدر. استبدلها باستدعاء واحد لـ `PivotCache.refresh()` يليه `calculateData()` لكل جدول.
- **تحديث المصدر عند تغير التخطيط فقط.** إذا غيّرت عرض الجدول المحوري فقط، مثل ترتيب الأعمدة أو `ConsolidationFunction`، دون المساس ببيانات المصدر، فلا داعي إلى `PivotCache.refresh()`، إذ سيبطئه ذلك. استدعِ `pivotTable.calculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الحالية.
- **مصدر خارجي لا يدعمه `PivotCache.refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي، مثل قاعدة بيانات أو مكعب OLAP أو ما إلى ذلك، فلن يستطيع `PivotCache.refresh()` تحديثه في v26.7، لأنه لا يدعم حاليًا سوى نوعَي المصدر `Sheet` و`Consolidation`. أما المصادر الخارجية، فأعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="nodejs-cpp" >}}