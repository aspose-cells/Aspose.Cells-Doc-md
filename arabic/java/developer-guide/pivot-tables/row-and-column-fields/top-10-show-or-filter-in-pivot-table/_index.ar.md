---
title: عرض أو تصفية أفضل 10 في الجدول المحوري
linktitle: عرض أو تصفية أفضل 10 في الجدول المحوري
description: تعلّم كيفية عرض العناصر الأعلى أو الأدنى ترتيبًا فقط في حقل جدول محوري باستخدام Aspose.Cells for Java. يتناول هذا المقال طريقة Top10AutoShow في Excel 97-2003، وقراءة الخيارات باستخدام Top10AutoShowSettings، وتصفية أفضل 10 في Excel 2007-365 عبر FilterTop10.
keywords: Aspose.Cells, Java, الجدول المحوري, أفضل 10, العرض التلقائي, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /ar/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يصعب قراءة جدول محوري يسرد كل عنصر في حقل صف إذا احتوى الحقل على عشرات العناصر. يحتفظ تقرير «أفضل 10» بالعناصر الأعلى أو الأدنى ترتيبًا فقط، وهو ما تحتاجه تقارير الترتيب تحديدًا، مثل «أفضل 5 منتجات حسب الإيرادات» أو «أسفل 3 مناطق حسب عدد المبيعات». يدعم Aspose.Cells آليتين لذلك، تقابلان جيلين من Microsoft Excel.
- **العرض التلقائي في Excel 97-2003** — الطريقة `PivotField.top10AutoShow()`. هذا هو الإعداد الكلاسيكي «عرض أفضل N عناصر أو أسفل N عناصر» المخزن مباشرةً على حقل الجدول المحوري. يعمل في جميع إصدارات Excel، القديمة والجديدة، لأنه جزء من تنسيق الجدول المحوري الأصلي.
- **تصفية أفضل 10 في Excel 2007-365** — الطريقة `PivotField.filterTop10()`. هذا هو مرشح القيمة الحديث لأفضل 10 الموجود ضمن مرشحات القيم في قائمة الحقل. يُخزَّن في صورة كائن `PivotFilter` مرتبط بالحقل، ويتيح الترتيب استنادًا إلى عدد العناصر أو نسبتها المئوية.

## **عرض أفضل 10 في Excel 97-2003 (top10AutoShow)**
يُهيَّأ العرض التلقائي الكلاسيكي باستدعاء واحد للطريقة `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — يتيح إعداد العرض التلقائي على الحقل أو يعطله.
- `isTop` — إذا كان `true`، يتم الاحتفاظ بالعناصر الأعلى ترتيبًا (الأعلى)، وإذا كان `false`، يتم الاحتفاظ بالعناصر الأدنى (الأسفل).
- `count` — عدد العناصر التي يجب الاحتفاظ بها، مثل 10 لتقرير كلاسيكي لأفضل 10.
- `rankBy` — الفهرس بدءًا من الصفر لحقل **البيانات** الذي تُرتَّب العناصر وفق قيمه. مرّر -1 لترتيب العناصر وفق الحقل نفسه.
يمكن أن يستند الترتيب إلى حقل قيمة أو إلى الحقل نفسه. توجد حالتان طبيعيتان، يوضحهما المثالان التاليان.

### **الترتيب حسب حقل قيمة**
رتّب عناصر حقل الصف وفق حقل قيمة عادي مثل "Sum of Sales". يبني المثال التالي جدولًا محوريًا فيه حقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أفضل رياضتين من حيث المبيعات. قيمة `rankBy` هي 0 لأن "Sum of Sales" هو حقل البيانات الموجود عند الفهرس 0.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// إظهار أفضل عنصرين مصنفين حسب "Sum of Sales" (فهرس حقل البيانات 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **الترتيب حسب الحقل نفسه**
يمكن ترتيب الحقل وفق نفسه أيضًا — مرر -1 كقيمة لـ `rankBy`. لا يتطلب هذا الأسلوب حقل بيانات إضافيًا؛ يكفي أن يوضع الحقل في منطقة الصفوف (أو الأعمدة). يوضح المثال التالي أدنى 3 رياضات مرتبة وفق الحقل نفسه. عند حفظ هذا الإعداد، لا تُدرج سمة `rankBy` في XML للجدول المحوري لأن -1 هي القيمة الافتراضية للتنسيق، وتعيد `Top10AutoShowSettings.getRankBy()` إرجاع القيمة -1.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// عرض آخر 3 عناصر مرتبة حسب الحقل نفسه (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **قراءة الخيارات الحالية (Top10AutoShowSettings)**
تعيد الطريقة `PivotField.getTop10AutoShowSettings()` كائن `PivotFieldTop10AutoShowSettings` يتيح الوصول إلى خيارات العرض التلقائي المخزنة حاليًا على الحقل. استخدمه للاطلاع على كيفية عرض العناصر في مصنف موجود، أو في جدول محوري أعدت تهيئته للتو، بما في ذلك المصنفات المحمَّلة من ملف.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

تتوافق الخصائص الأربع مع سمات العرض التلقائي الكلاسيكية المكتوبة في XML للجدول المحوري (`autoShow`، `topAutoShow`، `itemPageCount`، `rankBy`)، ولذلك تعكس القيم المقروءة ما سطبقه جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- الخصائص المباشرة لـ `PivotField`، التي يوفّرها `isAutoShow()` و`isAscendShow()` و`getAutoShowCount()` و`getAutoShowField()`، مهملة. استخدم كائن `Top10AutoShowSettings` بدلاً منها: تحل `Top10AutoShowSettings.isAutoShow()` محل `PivotField.isAutoShow()`، وتحل `Top10AutoShowSettings.isTop()` محل `PivotField.isAscendShow()`، وتحل `Top10AutoShowSettings.getAutoShowCount()` محل `PivotField.getAutoShowCount()`، وتحل `Top10AutoShowSettings.getRankBy()` محل `PivotField.getAutoShowField()`. وتُعد طريقة `PivotField.top10AutoShow()` الطريقة المدعومة لتغيير هذه الإعدادات.
- تعمل `top10AutoShow` مع حقول الصفوف والأعمدة. لا يمكن ترتيب حقل يقع فقط في منطقة الصفحة (التصفية) بهذه الطريقة لأن عناصره لا تظهر في متن الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: تصفية أفضل 10 (filterTop10)**
تتيح إصدارات Excel الحديثة الوصول إلى أفضل 10 بوصفه مرشح قيمة في قائمة الحقل (مرشحات القيم، أفضل 10...). ويمثل Aspose.Cells هذا الخيار من خلال الطريقة `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`، التي تُرجع كائن `PivotFilter` الذي أُنشئ:
- `valueFieldIndex` — الفهرس بدءًا من الصفر لحقل البيانات الذي تُرتَّب العناصر وفق قيمه المجمَّعة.
- `type` — معنى `itemCount`. يحتفظ `PivotFilterType.COUNT` بعدد ثابت من العناصر (خيار «العناصر» في مربع الحوار). يحتفظ `PivotFilterType.PERCENT` بنسبة مئوية من العناصر، لذا تكون `itemCount` هي النسبة المئوية نفسها؛ أي أن قيمة 30 تحتفظ بأفضل 30 في المئة. يرتب `PivotFilterType.SUM` العناصر وفق التغطية التراكمية للقيم.
- `isTop` — استخدم `true` للأعلى و`false` للأسفل.
- `itemCount` — يمثل العدد N في «أفضل N»، وتعتمد وحدته على `type`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// مرشح أفضل 10 - احتفظ بأفضل عنصرين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// لمرشح قائم على النسبة بدلاً من ذلك، احتفظ بأفضل 30٪ من العناصر:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
تمثل `top10AutoShow` و`filterTop10` ميزتين منفصلتين. يكتب العرض التلقائي سمة `autoShow` الكلاسيكية على حقل الجدول المحوري، وهي مدعومة في جميع إصدارات Excel منذ Excel 97. ويكتب `filterTop10` مدخل `PivotFilter` حديثًا، ويتطلب Excel 2007 أو إصدارًا أحدث. عند فتح مصنف في إصدار أقدم من Excel، يعود الجدول المحوري الذي يستخدم المرشح الحديث إلى عرض جميع العناصر. وبالنسبة إلى المستندات التي يجب أن تخضع لدورة قراءة وكتابة عبر أدوات قديمة، فضّل `top10AutoShow`؛ أما المصنفات الحديثة، ففضّل `filterTop10` لأنه يتكامل مع مرشحات القيم الأخرى.
{{% /alert %}}

## **مقالات ذات صلة**
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/java/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/java/pivot-table-add-row-and-column-fields/)
- [تجميع حقول الجدول المحوري في الجدول المحوري](/cells/ar/java/group-pivot-fields-in-the-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/java/refresh-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}