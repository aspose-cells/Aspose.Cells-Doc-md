---
title: تحديث الجداول المحورية وذواكر التخزين المؤقت في Aspose.Cells for Java
linktitle: تحديث الجداول المحورية وذواكر التخزين المؤقت في Aspose.Cells for Java
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Java باستخدام واجهة برمجة API لتحديث الجداول المحورية في الإصدار v26.7+. تغطي هذه المقالة refreshAll وrefreshPivotTables وPivotCache.refresh وcalculateData وgetPivotTables مع أمثلة برمجية عملية.
keywords: Aspose.Cells, Java, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells واجهة برمجة API متدرجة للتحديث تتيح لك إعادة تحميل بيانات الجداول المحورية ضمن أربعة نطاقات مختلفة، من المصنف بأكمله إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Java v26.7**، تم وضع علامة مهجورة على الطريقة القديمة `PivotTable.refreshData()`، وينبغي استبدالها بواجهات برمجة API أكثر كفاءة ومدركة لذاكرة التخزين المؤقت، والموضحة في هذه المقالة.
{{% /alert %}}

## Introduction
نادرًا ما تكون عملية تحديث جدول محوري عملية واحدة. في الخلفية، تحافظ Aspose.Cells على سلسلة بيانات متدرجة تصل بين بيانات المصدر الأصلية والقيم المعروضة في ورقة العمل. يُعد فهم هذه السلسلة هو مفتاح اختيار واجهة برمجة API المناسبة للتحديث في كل حالة.
تتكوّن سلسلة البيانات ذات الطبقات الأربع مما يأتي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية أو استعلام قاعدة البيانات أو نطاق التوحيد، حيث توجد القيم الأولية.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. يعتمد كل جدول محوري على `PivotCache`؛ فهنا يتم جمع جميع البيانات وإجراء التجميعات.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والمرشحات. يقرأ `PivotTable` من `PivotCache` *فقط*، ولا يقرأ بيانات المصدر مباشرةً.
4. **Cells** — خلايا ورقة العمل التي يكتب فيها `PivotTable` القيم المحسوبة والأنماط التي يعرضها.

{{% alert color="primary" %}}
تشير `PivotCache.getSourceType()`، باستخدام التعداد `PivotTableSourceType`، إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، تدعم `PivotCache.refresh()` نوعي المصدر **`Sheet`** و**`Consolidation`** فقط، أي البيانات الموجودة في نطاقات ورقة العمل. لا يمكن تحديث المصادر الخارجية، مثل قواعد البيانات والاتصالات الخارجية، بعد الآن عبر واجهة برمجة API الخاصة بذاكرة التخزين المؤقت.
نتيجة لهذه السلسلة، هناك مساران أساسيان للتحديث في Aspose.Cells:
- **`PivotTable.calculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، من دون رحلة ذهاب وعودة إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر من خلايا ورقة العمل، لذلك يكون نوع المصدر هو `Sheet`، وتعمل عمليات التحديث كما هو موضح.
{{% /alert %}}

## Quick Start
إذا كنت تحتاج فقط إلى أصغر قدر من التعليمات البرمجية لتحديث كل جدول محوري في المصنف، فاستدعاء واحد يكفي:

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

يشرح كل ما يليه في هذه المقالة متى ينبغي اختيار واجهة برمجة API أضيق نطاقًا بدلاً من ذلك.

## Required Import Statements
تبدأ جميع أمثلة Java في هذه المقالة تعليمات الاستيراد التالية، لأن أنواع الجداول المحورية موجودة في حزمة `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
عندما تحتاج إلى ضمان أن تعكس كل ذاكرات التخزين المؤقت وكل جداول المحورية في المصنف أحدث بيانات المصدر، تكون واجهة برمجة API الأبسط والأكثر شمولاً هي `Workbook.refreshAll()`. يمر الاستدعاء الواحد عبر المصنف بأكمله، حيث يحدّث كل `PivotCache` من مصدره ثم يعيد حساب كل `PivotTable` تابع له. يُعد هذا هو الأسلوب الموصى به للتحديثات العامة للوثيقة كاملة عندما لا يكون الأداء مصدرًا للقلق.
يبني المثال التالي مصنفًا يحتوي على نطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدّل بعض قيم المصدر، ثم يستخدم `refreshAll()` لتحديث كل شيء باستدعاء واحد.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
في بعض الأحيان، لا تحتاج إلا إلى تحديث الجداول المحورية الموجودة في ورقة عمل محددة، على سبيل المثال عندما تكون الجداول المحورية في أوراق عمل أخرى غير مرتبطة بشكل مؤكد ولا ينبغي المساس بها. في هذه الحالة، توفر Aspose.Cells واجهة برمجة API `Worksheet.refreshPivotTables()`، ويكون نطاقها محددًا بمثيل `Worksheet` واحد.

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
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
عندما تريد التحكم الدقيق في جدول محوري واحد، توفر واجهة برمجة API المستندة إلى ذاكرة التخزين المؤقت لك خيارين. يعتمد الاختيار بينهما على ما إذا كانت البيانات المصدر الأساسية قد تغيرت أم إعدادات العرض أو التخطيط الخاصة بالجدول المحوري نفسه فقط.

### Source Data Changed — Use `PivotCache.refresh()`
إذا تغيرت بيانات المصدر الأساسية، تكون نقطة الدخول الصحيحة هي `pivotTable.getPivotCache().refresh()`. يعيد هذا الاستدعاء قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت ثم يعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت تلك.

### Only View/Layout Changed — Use `calculateData()`
إذا لم تتغير بيانات المصدر، ولكن تم تعديل إعدادات العرض أو التخطيط الخاصة بالجدول المحوري فقط، مثل نقل حقل إلى منطقة مختلفة أو تبديل إعداد التحديث عند الفتح، فليست هناك حاجة إلى رحلة ذهاب وعودة إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة، ولا حاجة إلا إلى إعادة حساب `PivotTable` المعروض. في هذه الحالة، يكون `pivotTable.calculateData()` هو الخيار الصحيح.
يعدّل المثال التالي خاصية غير مرتبطة بالمصدر في الجدول المحوري ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الحالية.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
// Add a pivot table placed at destination cell E3, sourcing from A1:C9
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify a view/layout property -- this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

يحتوي المصنف غالبًا على عديد من الجداول المحورية التي تعمل جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها، مثلًا قبل تنفيذ تحديث جماعي أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة، استخدم `PivotCache.getPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` الذي يعتمد على ذاكرة التخزين المؤقت المحددة.

## Migrating from the Obsolete `PivotTable.refreshData()`
قبل Aspose.Cells for Java v26.7، كانت الطريقة المعيارية لتحديث جدول محوري هي استدعاء `PivotTable.refreshData()` على كل جدول محوري بشكل فردي. اعتبارًا من الإصدار v26.7، أصبحت هذه الطريقة **مهجورة**، وينبغي استبدالها بواجهات برمجة API المدركة لذاكرة التخزين المؤقت والموضحة أعلاه.
هناك سببان يجعل أسلوب `refreshData()` لكل جدول مشكلة في مصنفات العمل الواقعية:
- يعيد جلب البيانات من المصدر *في كل مرة* يتم فيها استدعاؤه، حتى عندما لا يكون المصدر قد تغير.
بدائل التوصية هي:
يوضح المثال التالي النمط الجديد والفعّال للمصنفات التي تحتوي على جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت واحدة.

## Which Refresh API Should I Use?
تلخص الجدول التالي واجهات برمجة API المتاحة للتحديث ومتى ينبغي اختيار كل منها.
| الهدف | واجهة برمجة API الموصى بها | الملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | استدعاء واحد يغطي جميع ذواكر التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة عمل واحدة فقط | `Worksheet.refreshPivotTables()` | يقتصر على ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.getPivotCache().refresh()` | يحدّث جميع الجداول المحورية الموجودة على ذاكرة التخزين المؤقت المشتركة تلك. |
| تغيرت إعدادات العرض أو التخطيط فقط | `pivotTable.calculateData()` | يتجنب رحلة غير ضرورية إلى المصدر. |
| سرد جميع الجداول المحورية الموجودة على ذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | استخدمه للتعداد قبل التحديث الجماعي. |
عمليًا، فضّل واجهات برمجة API المستندة إلى ذاكرة التخزين المؤقت بدلًا من `refreshData()` المهجورة الخاصة بكل جدول. فهي تراعي ذواكر التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر المكررة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث.

## Common Pitfalls
- **عدم التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عندما يتم تحديث سلسلة البيانات الخاصة به. إذا عدلت خلايا المصدر، فاستدعِ `PivotCache.refresh()` أو `Workbook.refreshAll()` قبل `Workbook.save()`، وإلا فسيحتوي الملف المحفوظ على القيم التجميعية القديمة.
- **استدعاء `refreshData()` المهجورة لكل جدول.** في الإصدار v26.7، تم وضع علامة مهجورة على `PivotTable.refreshData()`، وهي تعيد جلب المصدر في كل استدعاء. ومع وجود جداول محورية متعددة تشترك في ذاكرة تخزين مؤقت، يعني ذلك عددًا من عمليات جلب المصدر المكررة. استبدلها باستدعاء واحد لـ `PivotCache.refresh()` يليه `calculateData()` لكل جدول.
- **التحديث عندما يكون التخطيط فقط هو ما تغير.** إذا كنت قد غيّرت عرض الجدول المحوري فقط، مثل ترتيب الأعمدة أو `ConsolidationFunction`، من دون المساس ببيانات المصدر، فإن `PivotCache.refresh()` غير ضروري وبطيء. استدعِ `pivotTable.calculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الحالية.
- **مصدر خارجي غير مدعوم من قبل `PivotCache.refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي، مثل قاعدة بيانات أو مكعب OLAP، فيتعذر على `PivotCache.refresh()` تحديثه في الإصدار v26.7، لأنه يدعم حاليًا نوعي مصدر `Sheet` و`Consolidation` فقط. أما المصادر الخارجية، فيجب إعادة فتح المصنف أو إعادة بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="java" >}}