---
title: أعلى 10 عرض أو تصفية في جدول محوري
linktitle: أعلى 10 عرض أو تصفية في جدول محوري
description: تعرّف على كيفية عرض العناصر ذات الترتيب الأعلى أو الأدنى فقط لحقل محوري في Aspose.Cells for Python via Java، يتناول هذا المقال طريقة Excel 97‑2003 top10AutoShow، قراءة الخيارات باستخدام Top10AutoShowSettings، ومرشح Excel 2007‑365 أعلى 10 عبر filterTop10.
keywords: Aspose.Cells for Python via Java, جدول محوري, أعلى 10, إظهار تلقائي, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ar/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
قد يكون جدول محوري يُظهر كل عنصر من عناصر حقل الصف صعب القراءة عندما يحتوي الحقل على عشرات الأعضاء. يُبقي تقرير أعلى 10 العناصر فقط العناصر الأعلى أو الأدنى تصنيفًا، وهو ما تحتاجه تقارير التصنيف — "أعلى 5 منتجات حسب الإيرادات" أو "أدنى 3 مناطق حسب عدد المبيعات". يدعم Aspose.Cells آليتين لهذه الميزة، ويتوافق كل منهما مع جيلين من Microsoft Excel.
- **Excel 97‑2003 AutoShow** — طريقة `PivotField.top10AutoShow()` تُعد الإعداد الكلاسيكي “عرض أعلى/أدنى N عناصر” المخزّن مباشرةً على الحقل المحوري. يعمل في جميع إصدارات Excel، القديمة والجديدة، لأنه جزء من تنسيق جدول محوري الأصلي.
- **Excel 2007‑365 Top 10 Filter** — طريقة `PivotField.filterTop10()` هي مرشح القيمة “أعلى 10” الحديث الموجود ضمن قائمة مرشحات القيمة في حقل القائمة.

## **عرض أعلى 10 في Excel 97‑2003 (top10AutoShow)**
يتم تكوين AutoShow الكلاسيكي باستدعاء واحد إلى `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — يفعِّل أو يلغي إعداد AutoShow على الحقل.
- `isTop` — `True` يبقي العناصر ذات أعلى تصنيف (Top)، `False` يبقي الأدنى (Bottom).
- `count` — عدد العناصر التي سيتم الاحتفاظ بها، على سبيل المثال 10 لتقرير أعلى 10 الكلاسيكي.
- `rankBy` — الفهرس الصفري لحقل البيانات الذي تُرتّب قيمه العناصر. استخدم -1 لترتيب العناصر وفقًا للحقل نفسه.

يمكن أن يتم الترتيب بناءً على حقل قيمة أو على الحقل نفسه. يوجد نوعان طبيعيان موضحان أدناه.

### **الترتيب حسب حقل قيمة**
رتّب عناصر حقل الصف بحسب حقل قيمة عادي مثل مجموع المبيعات. المثال التالي يبني جدولًا محوريًا بحقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يُظهر أعلى رياضتين حسب المبيعات. `rankBy` يساوي 0 لأن “Sum of Sales” هو حقل البيانات في الفهرس 0.

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
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **الترتيب حسب الحقل نفسه**
يمكن أيضًا ترتيب الحقل نفسه — مرّر -1 كقيمة `rankBy`. لا يلزم حقل بيانات إضافي لهذا النوع؛ يجب أن يكون الحقل موجودًا في منطقة الصف (أو العمود) فقط. المثال التالي يُظهر أدنى 3 رياضات مرتبة حسب الحقل نفسه. عند حفظ هذا الإعداد، تُحذف سمة `rankBy` من XML جدول محوري لأن -1 هو القيمة الافتراضية للتنسيق، وتُعيد `Top10AutoShowSettings.getRankBy()` القيمة -1.

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
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **قراءة الخيارات الحالية (Top10AutoShowSettings)**
طريقة `PivotField.getTop10AutoShowSettings()` تُعيد كائن `PivotFieldTop10AutoShowSettings` يتيح الاطلاع على خيارات AutoShow المخزّنة حاليًا على الحقل. استخدمه لفحص كيفية عرض العناصر في مصنف موجود أو جدول محوري قمت بتكوينه مؤخرًا — بما في ذلك المصنفات التي تم تحميلها من ملف.

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

الخصائص الأربعة تُطابق سمات AutoShow الكلاسيكية المكتوبة في XML جدول محوري (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), لذا القيم المقروءة هي القيم التي تحترمها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- تُعتبر وصوليات `PivotField` المباشرة `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` و `getAutoShowField()` قديمة (obsolete). استخدم كائن `Top10AutoShowSettings` بدلاً منها: يتحول `PivotField.isAutoShow()` إلى `Top10AutoShowSettings.isAutoShow()`, و `PivotField.isAscendShow()` إلى `Top10AutoShowSettings.isTop()`, و `PivotField.getAutoShowCount()` إلى `Top10AutoShowSettings.getAutoShowCount()`, و `PivotField.getAutoShowField()` إلى `Top10AutoShowSettings.getRankBy()`. طريقة `top10AutoShow()` نفسها هي الطريقة المدعومة لتغيير الإعدادات.
- يعمل `top10AutoShow` مع حقول الصف والعمود. لا يمكن ترتيب حقل يكون فقط في منطقة الصفحة (التصفية) بهذه الطريقة لأن عناصره لا تُعرض في جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007‑365: مرشح أعلى 10 (filterTop10)**
تُظهر إصدارات Excel الحديثة مرشح أعلى 10 كقيمة ضمن قائمة مرشحات القيمة (Value Filters, Top 10…). يُنمذج Aspose.Cells ذلك باستخدام طريقة `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` التي تُعيد كائن `PivotFilter` المُنشأ:
- `valueFieldIndex` — الفهرس الصفري لحقل البيانات الذي تُرتّب قيمه العناصر المجمعة.
- `type` — ما الذي يعنيه `itemCount`. `PivotFilterType.COUNT` يحتفظ بعدد ثابت من العناصر (خيار Items في الحوار). `PivotFilterType.PERCENT` يحتفظ بنسبة مئوية من العناصر، لذا فإن `itemCount` هو النسبة نفسها — 30 يعني أعلى 30 ٪. `PivotFilterType.SUM` يرتّب حسب تغطية القيمة التراكمية.
- `isTop` — `True` للترتيب الأعلى, `False` للترتيب الأدنى.
- `itemCount` — الـ N في أعلى N؛ وحدته تعتمد على `type`.

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
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` و `filterTop10` ميزتان منفصلتان. يكتب AutoShow السمة الكلاسيكية `autoShow` المُحددة على الحقل المحوري ويُحترم من جميع إصدارات Excel بدءًا من Excel 97. يكتب `filterTop10` إدخال `PivotFilter` حديث، والذي يتطلب Excel 2007 أو أحدث. عندما يُفتح المصنف في إصدار Excel أقدم، يعود جدول محوري يستخدم المرشح الحديث إلى عرض جميع العناصر. بالنسبة للمستندات التي يجب أن تمر عبر أدوات قديمة، يُفضَّل `top10AutoShow`; بالنسبة للمصنفات الحديثة، يُفضَّل `filterTop10` لأنه يتكامل مع مرشحات القيم الأخرى.
{{% /alert %}}

## **مقالات ذات صلة**
- [تصفية جداول محورية حسب التسمية أو القيمة](/cells/ar/python-java/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقول صف وعمود إلى جدول محوري](/cells/ar/python-java/pivot-table-add-row-and-column-fields/)
- [تجميع حقول محورية في جدول محوري](/cells/ar/python-java/group-pivot-fields-in-the-pivot-table/)
- [تحديث جدول محوري](/cells/ar/python-java/refresh-pivot-table/)
- [إضافة حقل صفحة في جدول محوري](/cells/ar/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}