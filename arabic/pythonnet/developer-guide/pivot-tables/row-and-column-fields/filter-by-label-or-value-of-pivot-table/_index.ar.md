---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Python via .NET إمكانيات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات، ومرشحات التاريخ، ومرشحات القيم، ومرشحات أعلى 10، ومن خلال إخفاء أو إظهار عناصر الجدول المحوري.
keywords: Aspose.Cells, مكتبة Python via .NET, جدول بيانات, جدول محوري, تصفية, مرشح تسميات, مرشح قيم, مرشح تاريخ, مرشح أعلى 10, عنصر الجدول المحوري, إخفاء عنصر الجدول المحوري
type: docs
weight: 10
url: /ar/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة المستندة إلى النصوص، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا من نوع التاريخ والوقت أو خلايا فارغة فقط، وتطبيق مرشحات القيم مقابل الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري الفردية يدويًا باستخدام الخاصية `is_hidden`. تُتاح كل استراتيجية من خلال واجهات برمجية مخصصة في فئتي `PivotField` و`PivotItem`.
{{% /alert %}}

## **Introduction**
تُعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى تقديمها. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري وصولًا إلى الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يعكس Aspose.Cells for Python via .NET إمكانيات التصفية المتوفرة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تتناول هذه المقالة استراتيجيات التصفية التالية:
1. **مرشح التسميات** — يُصفّي عناصر حقل الصف أو العمود استنادًا إلى تسمياتها النصية.
2. **مرشح التاريخ** — يُصفّي حقول الصفوف أو الأعمدة التي تحتوي على قيم التاريخ والوقت فقط (أو خلايا فارغة).
3. **مرشح القيم** — يُصفّي العناصر استنادًا إلى القيم المجمعة لحقل بيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أدنى عدد N من العناصر مرتبة حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر فردي في حقل ما.
يستخدم كل أسلوب طريقة مختلفة في فئة `PivotField` أو خاصية في فئة `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `refresh_data()` و`calculate_data()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **Label Filter**
يتيح لك مرشح التسميات تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون ذلك مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو تحتوي على كلمة بعينها، أو تطابق معيارًا آخر قائمًا على التسمية.
يعرض Aspose.Cells تصفية التسميات من خلال الطريقة `PivotField.filter_by_label(PivotFilterType, label_string)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وغيرها. تُزوَّد الوسيطة الثانية بسلسلة التسمية المستخدمة في المقارنة.
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري موجود، ويطبق مرشح تسميات بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة فقط مرئية، ثم يُحدّث الجدول المحوري، ويحفظ النتيجة.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = ac.Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the first row PivotField
row_field = pivot_table.row_fields[0]
# Apply the label filter — show only row items whose labels begin with the supplied prefix
row_field.filter_by_label(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivot_table.pivot_cache.refresh()
# Save the workbook back to disk
workbook.save(fileName)
```

## **Date Filter**
تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري وفق معايير قائمة على التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخي محدد. وهي مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا من نوع التاريخ والوقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم نسخ صالحة من `datetime` أو خلايا فارغة قبل تطبيق هذا المرشح.
يعرض Aspose.Cells تصفية التاريخ من خلال الطريقة `PivotField.filter_by_date(PivotFilterType, *date_times)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. بناءً على نوع المرشح المختار، تمرر قيمة `datetime` واحدة أو قيمتين (بالنسبة لـ `Between`، تمرر تاريخي البداية والنهاية).
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري توجد في منطقة الصفوف به حقل تاريخ، ويطبق مرشح تاريخ يقصر العناصر المرئية على نطاق تاريخ معين، ثم يُحدّث الجدول المحوري، ويحفظ المصنف.
{{% /alert %}}

```python
import os
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotFilterType
input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"
if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)
# Load the existing workbook that contains the pivot table
workbook = ac.Workbook(input_path)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
date_field = pivot_table.row_fields[0]
# Define the date criterion for the Between filter
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
# Apply the date filter on the pivot field
date_field.filter_by_date(PivotFilterType.DATE_BETWEEN, start_date, end_date)
# Refresh and recalculate the pivot table so the filter takes effect
pivot_table.pivot_cache.refresh()
# Persist the workbook
workbook.save(output_path)
```

## **Value Filter**
تعمل مرشحات القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. وبدلًا من مطابقة تسميات النصوص، فإنها تقارن الإجماليات الرقمية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو عرض المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.
يعرض Aspose.Cells تصفية القيم من خلال الطريقة `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. يستخدم معامل `PivotFilterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. يحدد معامل `value_field` حقل البيانات الذي يجب تقييمه، في حين تُمرَّر قيمة العتبة (أو قيمها) في الوسيطات الأخيرة.
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري، ويطبق مرشح قيم يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة عتبة عددية، ثم يُحدّث الجدول المحوري، ويحفظ المصنف.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]
row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
data_field_index = -1
for i in range(len(pivot_table.data_fields)):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break
if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, PivotFilterType.VALUE_GREATER_THAN, 5000.0, float('inf'))
pivot_table.pivot_cache.refresh()
workbook.save("output.xlsx")
```

## **Top 10 Filter**
مرشح أعلى 10 هو شكل متخصص من مرشح القيم يحتفظ فقط بأعلى أو أدنى عدد N من العناصر بناءً على حقل قيمة مختار. يُستخدم بشكل شائع في تقارير الترتيب مثل "أفضل 10 منتجات من حيث الإيرادات" أو "أسوأ 5 مناطق من حيث عدد المبيعات".

{{% alert color="primary" %}}
لا يكون مرشح أعلى 10 فعالًا إلا عندما يحتوي الجدول المحوري على حقل قيمة محوري واحد أو أكثر في منطقة البيانات. فبدون وجود حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر وفقًا له، ولا يمكن تطبيق المرشح.
يعرض Aspose.Cells تصفية أعلى 10 من خلال الطريقة `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)`. يحدد معامل `item_count` عدد العناصر التي يجب الاحتفاظ بها، ويشير `is_top` إلى الاحتفاظ بأعلى العناصر (True) أو أدنى العناصر (False)، ويُحيل `value_field` إلى حقل البيانات المستخدم للترتيب، بينما يتحكم `PivotFilterType` في كيفية حساب القيمة (عادةً `Sum`، وكذلك `Count` و`Percent`).
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري يضم حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر من حيث مجموع المبيعات، ثم يُحدّث الجدول المحوري، ويحفظ المصنف.
{{% /alert %}}

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivotTable = worksheet.pivot_tables[0]
# Confirm there is at least one value PivotField in the data area
if len(pivotTable.data_fields) == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.row_fields[0]
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filter_top10(10, acp.PivotFilterType.SUM, True, valueFieldIndex)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.pivot_cache.refresh()
# Save the workbook
workbook.save(outputPath)
```

## **Filter by Hiding or Unhiding Pivot Items**
بالإضافة إلى واجهات التصفية البرمجية المنظمة، يتيح لك Aspose.Cells التحكم في رؤية كل عنصر محوري فردي بشكل مباشر. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل الخاصية `is_hidden`، يمكنك إخفاء عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي تعيين `is_hidden = True` إلى إخفاء العنصر من الجدول المحوري؛ بينما يؤدي تعيين `is_hidden = False` إلى إظهاره مجددًا وجعله مرئيًا.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر ما، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يقوم المثال أدناه بتحميل جدول محوري، وإخفاء عنصر معين بالاسم، وعرض كيفية إظهاره، ثم تحديث الجدول المحوري، وحفظ المصنف.

```python
import aspose.cells as ac
# Load an existing workbook containing a pivot table
workbook = ac.Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.worksheets[0]
# Access the pivot table by index (the first pivot table on the sheet)
pivot_table = sheet.pivot_tables[0]
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivot_field = pivot_table.row_fields[0]
# Iterate through the PivotItems collection of the selected PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]
    # Hide pivot items that match a specific name/criterion
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.name == "Item3":
        item.is_hidden = False
# Refresh and recalculate the pivot table so changes take effect
pivot_table.pivot_cache.refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
```

## **Summary**
يوفر Aspose.Cells for Python via .NET مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تطابق تلك المتوفرة في Microsoft Excel. تغطي مرشحات التسميات والتاريخ والقيم معظم السيناريوهات التحليلية الشائعة، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. وعندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.is_hidden` حلاً مرنًا على مستوى العناصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسميات ثم إخفاء عناصر محددة — إنشاء تقارير جداول محورية مستهدفة بدقة بالكامل من خلال الكود.

## Related Articles
- [إدراج جدول محوري](/cells/ar/python-net/create-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for Python via .NET](/cells/ar/python-net/pivot-table-add-row-and-column-fields/)
- [إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for Python via .NET](/cells/ar/python-net/add-page-field-in-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for Python via .NET](/cells/ar/python-net/manage-value-fields/)
- [تحديث الجداول المحورية وذاكرات التخزين المؤقت في Aspose.Cells for Python via .NET](/cells/ar/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}