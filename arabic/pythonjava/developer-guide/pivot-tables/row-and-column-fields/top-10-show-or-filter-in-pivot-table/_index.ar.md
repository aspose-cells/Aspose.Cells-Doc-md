---
title: عرض أو تصفية أعلى 10 عناصر في الجدول المحوري
linktitle: عرض أو تصفية أعلى 10 عناصر في الجدول المحوري
description: تعلم كيفية عرض العناصر الأعلى أو الأدنى تصنيفًا فقط في حقل محوري باستخدام Aspose.Cells for Python via Java. تتناول هذه المقالة طريقة top10AutoShow في Excel 97-2003، وقراءة الخيارات باستخدام Top10AutoShowSettings، وتطبيق تصفية أعلى 10 في Excel 2007-365 عبر filterTop10.
keywords: Aspose.Cells for Python via Java, جدول محوري, أعلى 10, العرض التلقائي, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ar/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
قد يكون من الصعب قراءة جدول محوري يسرد كل عنصر من حقل صف عندما يحتوي ذلك الحقل على عشرات العناصر. يحتفظ تقرير أعلى 10 فقط بالعناصر الأعلى أو الأدنى تصنيفًا، وهو بالضبط ما تحتاجه تقارير الترتيب — «أعلى 5 منتجات حسب الإيرادات» أو «أسفل 3 مناطق حسب عدد المبيعات». يدعم Aspose.Cells أسلوبين لذلك، وهما يقابلان جيلين من إصدارات Microsoft Excel.
- **العرض التلقائي في Excel 97-2003** — طريقة `PivotField.top10AutoShow()`. وهذا هو الإعداد الكلاسيكي «عرض أعلى N عنصر أو أسفلها»، ويُخزَّن مباشرةً على الحقل المحوري. يعمل في جميع إصدارات Excel، القديمة والحديثة، لأنه جزء من تنسيق الجدول المحوري الأصلي.
- **تصفية أعلى 10 في Excel 2007-365** — طريقة `PivotField.filterTop10()`. وهذه تصفية قيمة حديثة لأعلى 10 يمكن الوصول إليها من تصفية القيم في قائمة الحقل. وتُخزَّن في صورة كائن `PivotFilter` مرتبط بالحقل، وتوفر ترتيبًا قائمًا على عدد العناصر أو النسبة المئوية.

## **عرض أعلى 10 في Excel 97-2003 (top10AutoShow)**
يُهيَّأ العرض التلقائي الكلاسيكي من خلال استدعاء واحد لطريقة `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — يمكّن إعداد العرض التلقائي على الحقل أو يعطّله.
- `isTop` — تحدد `True` الإبقاء على العناصر الأعلى تصنيفًا (أعلى)، بينما تحدد `False` الإبقاء على العناصر الأدنى (أسفل).
- `count` — عدد العناصر المطلوب الاحتفاظ بها، مثل 10 لتقرير كلاسيكي لأعلى 10 عناصر.
- `rankBy` — الفهرس الصفري، الذي يبدأ من 0، لحقل البيانات الذي تُرتَّب العناصر وفق قيمه. مرّر -1 لترتيب العناصر حسب الحقل نفسه.
قد يستند الترتيب إلى حقل قيمة أو إلى الحقل نفسه. وتوجد طريقتان طبيعيتان لذلك، كما هو موضح أدناه.

### **الترتيب حسب حقل قيمة**
رتّب عناصر حقل الصف حسب حقل قيمة عادي مثل "Sum of Sales". يبني المثال التالي جدولًا محوريًا يحتوي على حقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أعلى رياضتين حسب المبيعات. تكون `rankBy` بقيمة 0 لأن "Sum of Sales" هو حقل البيانات عند الفهرس 0.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **الترتيب حسب الحقل نفسه**
يمكن أيضًا ترتيب حقل حسب نفسه — أي مرّر -1 كقيمة لـ `rankBy`. لا يلزم وجود حقل بيانات إضافي لهذا البديل؛ يكفي أن يكون الحقل في منطقة الصفوف (أو الأعمدة). يعرض المثال التالي ثلاث رياضات ذات الترتيب الأدنى، مرتبةً وفق الحقل نفسه. وعند حفظ هذا الإعداد، تُحذف سمة `rankBy` من XML الخاص بالجدول المحوري لأن -1 هي القيمة الافتراضية لهذا التنسيق، وتقرأ `Top10AutoShowSettings.getRankBy()` القيمة -1.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# إظهار آخر 3 عناصر مرتبة حسب الحقل نفسه (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **قراءة الخيارات الحالية (Top10AutoShowSettings)**
تعيد طريقة `PivotField.getTop10AutoShowSettings()` كائن `PivotFieldTop10AutoShowSettings` الذي يتيح الوصول إلى خيارات العرض التلقائي المخزنة حاليًا على الحقل. استخدمه لفحص كيفية عرض العناصر في مصنف موجود أو في جدول محوري قمت بتهيئته للتو — بما في ذلك المصنفات المحمّلة من ملف.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

تطابق الخصائص الأربع سمات العرض التلقائي الكلاسيكية التي تُكتب في XML الخاص بالجدول المحوري (`autoShow`، `topAutoShow`، `itemPageCount`، `rankBy`)، لذا تكون القيم المقروءة هي القيم التي ستطبّقها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- أدوات الوصول المباشرة إلى `PivotField`، وهي `isAutoShow()` و`isAscendShow()` و`getAutoShowCount()` و`getAutoShowField()`، مهجورة. استخدم كائن `Top10AutoShowSettings` بدلاً منها، إذ يوفر البدائل المكافئة: `PivotField.isAutoShow()` مقابل `Top10AutoShowSettings.isAutoShow()`، و`PivotField.isAscendShow()` مقابل `Top10AutoShowSettings.isTop()`، و`PivotField.getAutoShowCount()` مقابل `Top10AutoShowSettings.getAutoShowCount()`، و`PivotField.getAutoShowField()` مقابل `Top10AutoShowSettings.getRankBy()`. وتُعد طريقة `top10AutoShow()` الطريقة المدعومة لتغيير الإعدادات.
- تعمل `top10AutoShow` مع حقول الصفوف والأعمدة. لا يمكن ترتيب حقل يقع فقط في منطقة الصفحات (التصفية) بهذه الطريقة، لأن عناصره لا تظهر في جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: تصفية أعلى 10 (filterTop10)**
تتيح إصدارات Excel الحديثة تطبيق تصفية أعلى 10 بوصفها تصفية قيم في قائمة الحقل (تصفية القيم، أعلى 10...). وينفذ Aspose.Cells هذه العملية من خلال طريقة `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`، التي تُرجع كائن `PivotFilter` الذي تم إنشاؤه:
- `valueFieldIndex` — الفهرس الصفري لحقل البيانات الذي تُرتَّب العناصر وفق قيمه المجمّعة.
- `type` — معنى `itemCount`. يحتفظ `PivotFilterType.COUNT` بعدد ثابت من العناصر (خيار العناصر في مربع الحوار). يحتفظ `PivotFilterType.PERCENT` بنسبة مئوية من العناصر، وبذلك تكون `itemCount` هي النسبة نفسها؛ أي أن 30 يحتفظ بأعلى 30٪. أما `PivotFilterType.SUM` فيرتب العناصر بحسب التغطية التراكمية للقيم.
- `isTop` — القيمة `True` تعني الأعلى، والقيمة `False` تعني الأسفل.
- `itemCount` — القيمة N في «أعلى N»، وتعتمد وحدتها على `type`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # مرشح أعلى 10 — احتفظ بأعلى عنصرين وفق "مجموع المبيعات" (فهرس حقل البيانات 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # بدلاً من ذلك، لاستخدام مرشح قائم على النسبة، احتفظ بأعلى 30٪ من العناصر:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` و`filterTop10` هما وظيفتان منفصلتان. يكتب العرض التلقائي سمة `autoShow` الكلاسيكية على الحقل المحوري، وتتعرف عليها جميع إصدارات Excel منذ Excel 97. ويكتب `filterTop10` مدخل `PivotFilter` حديثًا يتطلب Excel 2007 أو إصدارًا أحدث. وعند فتح مصنف في إصدار أقدم من Excel، يعرض الجدول المحوري الذي يستخدم التصفية الحديثة جميع العناصر. للمستندات التي يجب أن تمر ذهابًا وإيابًا عبر أدوات الإصدارات القديمة، فضّل `top10AutoShow`؛ أما المصنفات الحديثة، فاستخدم `filterTop10` لأنه يتكامل مع مرشحات القيم الأخرى.
{{% /alert %}}

## **مقالات ذات صلة**
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-java/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/python-java/pivot-table-add-row-and-column-fields/)
- [تجميع حقول الجدول المحوري في الجدول المحوري](/cells/ar/python-java/group-pivot-fields-in-the-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/python-java/refresh-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}