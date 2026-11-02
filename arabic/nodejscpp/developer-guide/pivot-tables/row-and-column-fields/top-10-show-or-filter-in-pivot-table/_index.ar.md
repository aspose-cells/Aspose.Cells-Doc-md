---
title: عرض أعلى 10 عناصر أو تصفيةها في الجدول المحوري
linktitle: عرض أعلى 10 عناصر أو تصفيةها في الجدول المحوري
description: تعلّم كيفية عرض العناصر الأعلى أو الأدنى ترتيبًا فقط في حقل محوري باستخدام Aspose.Cells for Node.js عبر C++. تغطي هذه المقالة طريقة Top10AutoShow في Excel 97-2003، وقراءة الخيارات باستخدام Top10AutoShowSettings، وتصفية أعلى 10 في Excel 2007-365 عبر FilterTop10.
keywords: Aspose.Cells, Node.js عبر C++, جدول محوري, أعلى 10, العرض التلقائي, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /ar/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
قد يصعب قراءة جدول محوري يسرد كل عنصر في حقل صف عندما يحتوي الحقل على عشرات العناصر. يحتفظ تقرير أعلى 10 فقط بالعناصر الأعلى أو الأدنى ترتيبًا، وهو ما تحتاج إليه تقارير الترتيب تحديدًا، مثل «أفضل 5 منتجات حسب الإيرادات» أو «أدنى 3 مناطق حسب عدد المبيعات». تدعم Aspose.Cells آليتين لهذا الغرض، يقابلان جيلين من إصدارات Microsoft Excel.
- **العرض التلقائي في Excel 97-2003** — طريقة `pivotField.top10AutoShow()`. يمثّل هذا الإعداد الكلاسيكي «عرض أعلى/أسفل N عنصر» المخزن مباشرةً في الحقل المحوري. يعمل في جميع إصدارات Excel، القديمة والجديدة، لأنه جزء من تنسيق الجداول المحورية الأصلي.
- **تصفية أعلى 10 في Excel 2007-365** — طريقة `pivotField.filterTop10()`. يمثّل هذا مرشح القيمة الحديث «أعلى 10» المتاح ضمن «مرشحات القيم» في قائمة الحقل. يُخزَّن في صورة كائن `PivotFilter` مرتبط بالحقل، ويوفر خيارات ترتيب قائمة على عدد العناصر أو نسبتها المئوية.

## **عرض أعلى 10 في Excel 97-2003 (top10AutoShow)**
يُضبط العرض التلقائي الكلاسيكي باستدعاء واحد لـ `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)`:
- `isAutoShow` — يتيح إعداد العرض التلقائي في الحقل أو يعطله.
- `isTop` — إذا كانت القيمة `true`، فيتم الاحتفاظ بالعناصر الأعلى ترتيبًا؛ وإذا كانت `false`، فيتم الاحتفاظ بالعناصر الأدنى ترتيبًا.
- `count` — عدد العناصر التي يجب الاحتفاظ بها، مثل 10 في تقرير أعلى 10 الكلاسيكي.
- `rankBy` — الفهرس الذي يبدأ من الصفر لحقل **البيانات** الذي تُستخدم قيمه في ترتيب العناصر. مرّر القيمة -1 لترتيب العناصر حسب الحقل نفسه.
يمكن أن يستند الترتيب إلى حقل قيمة أو إلى الحقل نفسه. وفيما يلي خياران شائعان للترتيب.

### **الترتيب حسب حقل قيمة**
رتّب عناصر حقل الصفوف حسب حقل قيمة عادي مثل «مجموع المبيعات». ينشئ المثال التالي جدولًا محوريًا يتكون من حقل صفوف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أعلى الرياضتين من حيث المبيعات. قيمة `rankBy` هي 0 لأن «مجموع المبيعات» هو حقل البيانات الموجود عند الفهرس 0.

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **الترتيب حسب الحقل نفسه**
يمكن ترتيب الحقل حسب نفسه أيضًا، لذا مرّر القيمة -1 كقيمة `rankBy`. لا يلزم وجود حقل بيانات إضافي لهذا الخيار؛ يكفي أن يكون الحقل موجودًا في منطقة الصفوف (أو الأعمدة). يعرض المثال التالي أدنى 3 رياضات مرتبة حسب الحقل نفسه. وعند حفظ هذا الإعداد، لا تُدرج سمة `rankBy` في XML الخاص بالجدول المحوري لأن -1 هي القيمة الافتراضية للتنسيق، وتعيد `top10AutoShowSettings.getRankBy()` قراءة القيمة -1.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **قراءة الخيارات الحالية (Top10AutoShowSettings)**
تعيد طريقة `pivotField.getTop10AutoShowSettings()` كائن `PivotFieldTop10AutoShowSettings` الذي يتيح الوصول إلى خيارات العرض التلقائي المخزنة حاليًا في الحقل. استخدمه لفحص كيفية عرض عناصر مصنف قائم، أو جدول محوري تم إعداده للتو، بما في ذلك المصنفات المحمّلة من ملف.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

تُقابل الخصائص الأربعة سمات العرض التلقائي الكلاسيكية المكتوبة في XML الخاص بالجدول المحوري (`autoShow`، `topAutoShow`، `itemPageCount`، `rankBy`)، لذلك Diving values التي تمت قراءتها هي القيم التي ستعتمدها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- مُعيدات الخصائص المباشرة في `PivotField`، وهي `isAutoShow`، و`getIsAscendShow()`، و`getAutoShowCount()`، و`getAutoShowField()`، مهجورة. استخدم كائن `Top10AutoShowSettings` بدلًا منها: استبدل `pivotField.isAutoShow` بـ `top10AutoShowSettings.isAutoShow`، و`pivotField.getIsAscendShow()` بـ `top10AutoShowSettings.isTop`، و`pivotField.getAutoShowCount()` بـ `top10AutoShowSettings.getAutoShowCount()`، و`pivotField.getAutoShowField()` بـ `top10AutoShowSettings.getRankBy()`. وتعد طريقة `pivotField.top10AutoShow()` الطريقة المدعومة لتغيير الإعدادات.
- تعمل `top10AutoShow()` مع حقول الصفوف والأعمدة. لا يمكن ترتيب حقل يقع حصرًا في منطقة الصفحات (التصفية) بهذه الطريقة، لأن عناصره لا تظهر موزعة في منطقة بيانات الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: تصفية أعلى 10 (filterTop10)**
تتيح إصدارات Excel الحديثة استخدام أعلى 10 كمرشح قيمة في قائمة الحقل (مرشحات القيم، أعلى 10...). توفر Aspose.Cells هذه الميزة من خلال طريقة `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)` التي تُرجع كائن `PivotFilter` الذي تم إنشاؤه:
- `valueFieldIndex` — الفهرس الذي يبدأ من الصفر لحقل البيانات الذي تُستخدم قيمه المجمعة لترتيب العناصر.
- `type` — معنى `itemCount`. يحتفظ `PivotFilterType.Count` بعدد ثابت من العناصر (خيار «العناصر» في مربع الحوار). ويحتفظ `PivotFilterType.Percent` بنسبة من العناصر، بحيث تكون `itemCount` هي النسبة المئوية نفسها؛ أي أن القيمة 30 تحتفظ بأعلى 30 بالمئة. ويرتب `PivotFilterType.SUM` العناصر وفق التغطية التراكمية للقيم.
- `isTop` — تُستخدم `true` للأعلى و`false` للأسفل.
- `itemCount` — الرقم N في تعبير «أعلى N»، وتعتمد وحدته على `type`.

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
تمثّل `top10AutoShow` و`filterTop10` ميزتين منفصلتين. يكتب العرض التلقائي سمة `autoShow` الكلاسيكية في الحقل المحوري، وتعتمدها جميع إصدارات Excel منذ Excel 97. ويكتب `filterTop10` إدخالًا حديثًا من نوع `PivotFilter`، ويتطلب Excel 2007 أو إصدارًا أحدث. وعند فتح مصنف في إصدار أقدم من Excel، يعود الجدول المحوري الذي يستخدم المرشح الحديث إلى عرض جميع العناصر. أما المستندات التي يجب أن تُعالَج ذهابًا وإيابًا عبر أدوات الإصدارات السابقة، فيُفضّل استخدام `top10AutoShow`؛ أما المصنفات الحديثة، فيُفضّل استخدام `filterTop10` لأنه يتكامل مع مرشحات القيم الأخرى.
{{% /alert %}}

## **مقالات ذات صلة**
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [تجميع حقول الجدول المحوري](/cells/ar/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/nodejs-cpp/refresh-pivot-table/)
- [إضافة حقل صفحة إلى الجدول المحوري](/cells/ar/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}