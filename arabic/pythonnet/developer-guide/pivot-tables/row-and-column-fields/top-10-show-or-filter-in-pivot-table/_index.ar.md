---
title: عرض أو تصفية أعلى 10 عناصر في الجدول المحوري
linktitle: عرض أو تصفية أعلى 10 عناصر في الجدول المحوري
description: تعلّم كيفية عرض العناصر الأعلى أو الأدنى تصنيفًا فقط في حقل محوري باستخدام Aspose.Cells for Python عبر .NET. تتناول هذه المقالة طريقة top_10_auto_show في Excel 97-2003، وقراءة الخيارات باستخدام top_10_auto_show_settings، وتصفية أعلى 10 في Excel 2007-365 عبر filter_top10.
keywords: Aspose.Cells, Python عبر .NET, جدول محوري, أعلى 10, العرض التلقائي, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /ar/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يصعب قراءة الجدول المحوري الذي يسرد جميع عناصر حقل الصف عندما يحتوي الحقل على عشرات العناصر. يحتفظ تقرير أعلى 10 بالعناصر الأعلى أو الأدنى تصنيفًا فقط، وهو ما تحتاجه تقارير الترتيب تحديدًا، مثل «أفضل 5 منتجات حسب الإيرادات» أو «أدنى 3 مناطق حسب عدد المبيعات». يدعم Aspose.Cells آليتين لذلك، تقابلان جيلين من إصدارات Microsoft Excel.
- **العرض التلقائي في Excel 97-2003** — طريقة `PivotField.top_10_auto_show()`. هذا هو الإعداد الكلاسيكي «عرض أعلى/أسفل N عناصر» المخزن مباشرةً على الحقل المحوري. يعمل في جميع إصدارات Excel، القديمة والجديدة، لأنه جزء من تنسيق الجدول المحوري الأصلي.
- **تصفية أعلى 10 في Excel 2007-365** — طريقة `PivotField.filter_top10()`. هذا هو عامل تصفية القيم الحديث المعروف باسم «أعلى 10»، الموجود ضمن «مرشحات القيم» في قائمة الحقل. يُخزَّن في صورة كائن `PivotFilter` مرتبط بالحقل، ويوفر ترتيبًا قائمًا على عدد العناصر أو النسبة المئوية.

## **عرض أعلى 10 في Excel 97-2003 (top_10_auto_show)**
يُهيَّأ الإعداد الكلاسيكي للعرض التلقائي باستدعاء واحد لطريقة `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)`:
- `is_auto_show` — يفعّل إعداد العرض التلقائي على الحقل أو يعطله.
- `is_top` — إذا كانت القيمة `True`، فيتم الاحتفاظ بالعناصر الأعلى تصنيفًا (أعلى)؛ وإذا كانت `False`، فيتم الاحتفاظ بالعناصر الأدنى (أسفل).
- `count` — عدد العناصر التي يُحتفظ بها، مثل 10 لتقرير كلاسيكي لأعلى 10.
- `rank_by` — الفهرس المبني على الصفر لحقل **البيانات** الذي تُستخدم قيمه لترتيب العناصر. مرّر -1 لترتيب العناصر وفق الحقل نفسه.
يمكن أن يتم الترتيب بواسطة حقل قيم أو بواسطة الحقل نفسه. وفيما يلي عرضان طبيعيان لهذا الإعداد.

### **الترتيب حسب حقل قيم**
رتّب عناصر حقل الصف وفق حقل قيم عادي مثل `Sum of Sales`. ينشئ المثال التالي جدولًا محوريًا يحتوي على حقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أعلى رياضتين من حيث المبيعات. قيمة `rank_by` هي 0 لأن `Sum of Sales` هو حقل البيانات الموجود عند الفهرس 0.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# إظهار أفضل عنصرين مرتبين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **الترتيب حسب الحقل نفسه**
يمكن أيضًا ترتيب الحقل حسب نفسه — مرّر -1 كقيمة لـ `rank_by`. لا يحتاج هذا الأسلوب إلى حقل بيانات إضافي؛ يكفي أن يكون الحقل في منطقة الصفوف (أو الأعمدة). يعرض المثال التالي أدنى 3 رياضات مرتبة وفق الحقل نفسه. عند حفظ هذا الإعداد، لا تُدرج سمة `rank_by` في XML للجدول المحوري لأن -1 هي القيمة الافتراضية للتنسيق، وتقرأ `top_10_auto_show_settings.rank_by` القيمة -1.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **قراءة الخيارات الحالية (top_10_auto_show_settings)**
تعيد الخاصية `PivotField.top_10_auto_show_settings` كائن `PivotFieldTop10AutoShowSettings` الذي يعرض خيارات العرض التلقائي المخزنة حاليًا على الحقل. استخدمه لفحص كيفية عرض العناصر في مصنف موجود أو في جدول محوري تهيئته للتو، بما في ذلك المصنفات المحمّلة من ملف.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

تقابل الخصائص الأربع سمات العرض التلقائي الكلاسيكية المكتوبة في XML للجدول المحوري (`autoShow` و`topAutoShow` و`itemPageCount` و`rankBy`)، لذا تكون القيم المقروءة هي القيم التي ستطبّقها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- تعد الخصائص المباشرة `is_auto_show` و`is_ascend_show` و`auto_show_count` و`auto_show_field` على `PivotField` معلَّمة كمهملة. استخدم كائن `top_10_auto_show_settings` بدلًا منها: تصبح `is_auto_show` هي `top_10_auto_show_settings.is_auto_show`، وتصبح `is_ascend_show` هي `top_10_auto_show_settings.is_top`، وتصبح `auto_show_count` هي `top_10_auto_show_settings.auto_show_count`، وتصبح `auto_show_field` هي `top_10_auto_show_settings.rank_by`. طريقة `top_10_auto_show()` نفسها هي الطريقة المدعومة لتغيير الإعدادات.
- تعمل `top_10_auto_show` مع حقول الصفوف والأعمدة. لا يمكن ترتيب حقل موجود فقط في منطقة الصفحات (التصفية) بهذه الطريقة لأن عناصره لا تُدرج ضمن جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: تصفية أعلى 10 (filter_top10)**
تعرض إصدارات Excel الحديثة خيار «أعلى 10» كعامل تصفية للقيم في قائمة الحقل («مرشحات القيم»، «أعلى 10...»). وينمذج Aspose.Cells هذه الميزة باستخدام طريقة `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)`، التي تعيد كائن `PivotFilter` الذي تم إنشاؤه:
- `value_field_index` — الفهرس المبني على الصفر لحقل البيانات الذي تُستخدم قيمه المجمّعة لترتيب العناصر.
- `type` — يحدد معنى `item_count`. يحتفظ `PivotFilterType.COUNT` بعدد ثابت من العناصر (خيار «العناصر» في مربع الحوار). ويحتفظ `PivotFilterType.PERCENT` بنسبة مئوية من العناصر، لذا تكون `item_count` هي النسبة نفسها؛ أي أن القيمة 30 تحتفظ بأعلى 30 في المئة. ويرتب `PivotFilterType.SUM` العناصر وفق التغطية التراكمية للقيم.
- `is_top` — `True` للأعلى و`False` للأسفل.
- `item_count` — القيمة N في «أعلى N»؛ وتعتمد وحدتها على `type`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# مرشح أعلى 10 — الاحتفاظ بأعلى عنصرين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# بدلاً من ذلك، يمكن استخدام مرشح قائم على النسبة للاحتفاظ بأعلى 30٪ من العناصر:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` و`filter_top10` ميزتان منفصلتان. يكتب العرض التلقائي مجموعة سمات `autoShow` الكلاسيكية على الحقل المحوري، وتطبّقها جميع إصدارات Excel منذ Excel 97. ويكتب `filter_top10` إدخالًا حديثًا من نوع `PivotFilter`، وهو ما يتطلب Excel 2007 أو إصدارًا أحدث. عند فتح مصنف في إصدار أقدم من Excel، يلجأ الجدول المحوري الذي يستخدم عامل التصفية الحديث إلى عرض جميع العناصر. بالنسبة إلى المستندات التي يجب أن تمر عبر دورة كاملة من الحفظ والفتح باستخدام أدوات الإصدارات القديمة، فضّل `top_10_auto_show`؛ أما في المصنفات الحديثة، ففضّل `filter_top10` لأنه يتكامل مع عوامل تصفية القيم الأخرى.
{{% /alert %}}

## **المقالات ذات الصلة**
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-net/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/python-net/pivot-table-add-row-and-column-fields/)
- [تجميع حقول الجدول المحوري](/cells/ar/python-net/group-pivot-fields-in-the-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/python-net/refresh-pivot-table/)
- [إضافة حقل صفحة إلى الجدول المحوري](/cells/ar/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}