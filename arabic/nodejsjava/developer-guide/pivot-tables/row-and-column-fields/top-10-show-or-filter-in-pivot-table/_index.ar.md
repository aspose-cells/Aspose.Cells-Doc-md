---
title: إظهار أو تصفية أعلى 10 في الجدول المحوري
linktitle: إظهار أو تصفية أعلى 10 في الجدول المحوري
description: تعلَّم كيف تعرض فقط العناصر الأعلى أو الأدنى تصنيفًا في حقل جدول محوري باستخدام Aspose.Cells for Node.js عبر Java. تتناول هذه المقالة أسلوب Top10AutoShow في Excel 97-2003، وقراءة الخيارات باستخدام Top10AutoShowSettings، ومرشّح أعلى 10 في Excel 2007-365 عبر FilterTop10.
keywords: Aspose.Cells, Node.js عبر Java, جدول محوري, أعلى 10, عرض تلقائي, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /ar/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون الجدول المحوري الذي يسرد جميع عناصر حقل الصف صعب القراءة عندما يحتوي ذلك الحقل على عشرات العناصر. يحتفظ تقرير أعلى 10 بالعناصر الأعلى أو الأدنى تصنيفًا فقط، وهو بالضبط ما تحتاج إليه تقارير الترتيب، مثل «أعلى 5 منتجات حسب الإيرادات» أو «أدنى 3 مناطق حسب عدد المبيعات». يوفر Aspose.Cells طريقتين لهذا الغرض، تقابلهما جيلان من إصدارات Microsoft Excel.
- **العرض التلقائي في Excel 97-2003** — الأسلوب `PivotField.top10AutoShow()`. هذا هو الإعداد الكلاسيكي «إظهار أعلى/أسفل N عناصر» المخزن مباشرةً على حقل الجدول المحوري. يعمل في جميع إصدارات Excel، القديمة والحديثة، لأنه جزء من تنسيق الجدول المحوري الأصلي.
- **مرشّح أعلى 10 في Excel 2007-365** — الأسلوب `PivotField.filterTop10()`. هذا هو مرشّح القيم الحديث «أعلى 10» الموجود ضمن «مرشّحات القيم» في قائمة الحقل. يُخزَّن ككائن `PivotFilter` مرتبط بالحقل، ويوفّر ترتيبًا بحسب عدد العناصر أو النسبة المئوية.

## **إظهار أعلى 10 في Excel 97-2003 (Top10AutoShow)**
يُهيَّأ العرض التلقائي الكلاسيكي عبر استدعاء واحد فقط إلى `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — يفعّل إعداد العرض التلقائي على الحقل أو يعطّله.
- `isTop` — إذا كانت `true`، فيتم الاحتفاظ بالعناصر الأعلى تصنيفًا (أعلى)، وإذا كانت `false`، فيتم الاحتفاظ بالعناصر الأدنى (أسفل).
- `count` — عدد العناصر التي يتم الاحتفاظ بها، على سبيل المثال 10 لتقرير كلاسيكي لأعلى 10.
- `rankBy` — الفهرس القائم على الصفر لحقل **البيانات** الذي تُرتَّب العناصر وفق قيمه. مرّر -1 لترتيب العناصر حسب الحقل نفسه.
يمكن أن يستند الترتيب إلى حقل قيم أو إلى الحقل نفسه. وفيما يلي خياران شائعان لتطبيقه.

### **الترتيب بواسطة حقل قيم**
رتّب عناصر حقل الصف وفق حقل قيم عادي مثل «مجموع المبيعات». يبني المثال التالي جدولًا محوريًا يحتوي على حقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أعلى رياضتين حسب المبيعات. وتكون قيمة `rankBy` مساوية لـ 0 لأن «مجموع المبيعات» هو حقل البيانات الموجود عند الفهرس 0.

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **الترتيب بواسطة الحقل نفسه**
يمكن أيضًا ترتيب الحقل حسب نفسه، وذلك بتمرير -1 إلى `rankBy`. لا يلزم وجود حقل بيانات إضافي لهذا الخيار؛ يكفي أن يكون الحقل موجودًا في منطقة الصفوف (أو الأعمدة). ويعرض المثال التالي أدنى 3 رياضات مرتبة حسب الحقل نفسه. وعند حفظ هذا الإعداد، لا تُكتب سمة `rankBy` في XML للجدول المحوري لأن -1 هي القيمة الافتراضية للتنسيق، وتعيد `getTop10AutoShowSettings().getRankBy()` قراءة القيمة -1.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **قراءة الخيارات الحالية (Top10AutoShowSettings)**
يُعيد أسلوب `PivotField.getTop10AutoShowSettings()` كائن `PivotFieldTop10AutoShowSettings` يتيح الوصول إلى خيارات العرض التلقائي المحفوظة حاليًا على الحقل. استخدمه للتحقق من طريقة عرض العناصر في مصنف موجود أو في جدول محوري أعددته للتو، بما في ذلك المصنفات المحمّلة من ملف.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

تقابل الدوال `isAutoShow()` و`isTop()` و`getAutoShowCount()` و`getRankBy()` سمات العرض التلقائي الكلاسيكية المكتوبة في XML للجدول المحوري (`autoShow` و`topAutoShow` و`itemPageCount` و`rankBy`)، لذا تكون القيم المقروءة هي القيم التي سيطبّقها كل إصدار من Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- الطرق المباشرة `isAutoShow()` و`isAscendShow()` و`getAutoShowCount()` و`getAutoShowField()` الخاصة بـ `PivotField` معلَّمة بأنها مهملة. استخدم كائن `getTop10AutoShowSettings()` بدلاً منها: استبدل `isAutoShow()` بـ `getTop10AutoShowSettings().isAutoShow()`، و`isAscendShow()` بـ `getTop10AutoShowSettings().isTop()`، و`getAutoShowCount()` بـ `getTop10AutoShowSettings().getAutoShowCount()`، و`getAutoShowField()` بـ `getTop10AutoShowSettings().getRankBy()`. والطريقة المدعومة لتغيير هذه الإعدادات هي `top10AutoShow()` نفسها.
- تعمل `top10AutoShow()` مع حقول الصفوف والأعمدة. ولا يمكن ترتيب حقل موجود في منطقة الصفحة (التصفية) بهذه الطريقة، لأن عناصره لا تُرتَّب داخل جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: مرشّح أعلى 10 (FilterTop10)**
تعرض إصدارات Excel الحديثة «أعلى 10» كمرشّح قيم ضمن قائمة الحقل («مرشّحات القيم»، «أعلى 10...»). ويوفر Aspose.Cells هذه الميزة من خلال أسلوب `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`، الذي يُعيد كائن `PivotFilter` الذي أُنشئ:
- `valueFieldIndex` — الفهرس القائم على الصفر لحقل البيانات الذي تُرتَّب العناصر وفق قيمه المجمّعة.
- `type` — يحدد معنى `itemCount`. يحتفظ `PivotFilterType.COUNT` بعدد ثابت من العناصر، أي خيار «العناصر» في مربع الحوار. أما `PivotFilterType.PERCENT` فيحتفظ بنسبة من العناصر، لذا تكون `itemCount` هي النسبة نفسها؛ أي أن 30 يعني الاحتفاظ بأعلى 30 في المئة. ويرتّب `PivotFilterType.SUM` العناصر وفق التغطية التراكمية للقيم.
- `isTop` — `true` لأعلى، و`false` لأسفل.
- `itemCount` — القيمة N في «أعلى N»، وتتبع وحدتها `type`.

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` و`filterTop10()` هما ميزتان منفصلتان. يكتب العرض التلقائي سمة `autoShow` الكلاسيكية المعيَّنة على حقل الجدول المحوري، وتطبّقها جميع إصدارات Excel منذ Excel 97. ويكتب `filterTop10()` إدخالًا حديثًا من نوع `PivotFilter` يتطلب Excel 2007 أو إصدارًا أحدث. وعند فتح مصنف في إصدار أقدم من Excel، يعود الجدول المحوري الذي يستخدم المرشّح الحديث إلى عرض جميع العناصر. وبالنسبة إلى المستندات التي يجب أن تُمرَّر ذهابًا وإيابًا عبر أدوات الإصدارات السابقة، فضّل `top10AutoShow()`؛ أما في المصنفات الحديثة ففضّل `filterTop10()` لأنه يتكامل مع مرشّحات القيم الأخرى.
{{% /alert %}}

## **المقالات ذات الصلة**
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقول صفوف وأعمدة إلى جدول محوري](/cells/ar/nodejs-java/pivot-table-add-row-and-column-fields/)
- [تجميع حقول الجدول المحوري في الجدول المحوري](/cells/ar/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/nodejs-java/refresh-pivot-table/)
- [إضافة حقل صفحة في جدول محوري](/cells/ar/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}