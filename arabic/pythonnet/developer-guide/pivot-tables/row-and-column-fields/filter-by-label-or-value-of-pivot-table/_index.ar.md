---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Python via .NET إمكانيات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات، ومرشحات التاريخ، ومرشحات القيم، ومرشحات أعلى 10، ومن خلال إخفاء أو إظهار عناصر الجدول المحوري.
keywords: Aspose.Cells, Python via .NET library, spreadsheet, pivot table, filter, label filter, value filter, date filter, top 10 filter, pivot item, hide pivot item
type: docs
weight: 10
url: /ar/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة المستندة إلى النصوص، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا من نوع التاريخ والوقت أو خلايا فارغة فقط، وتطبيق مرشحات القيم مقابل الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري الفردية يدويًا باستخدام الخاصية `is_hidden`. تُتاح كل استراتيجية من خلال واجهات برمجية مخصصة في فئتي `PivotField` و`PivotItem`.
{{% /alert %}}
## **المقدمة**
تُعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما تحتاج إلى تقديمها. التصفية هي الآلية الأساسية لتضييق نطاق الجدول المحوري وصولًا إلى الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يعكس Aspose.Cells for Python via .NET إمكانيات التصفية المتوفرة في Microsoft Excel، ويعرضها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تتناول هذه المقالة استراتيجيات التصفية التالية:
1. **مرشح التسميات** — يُصفّي عناصر حقل الصف أو العمود استنادًا إلى تسمياتها النصية.
2. **مرشح التاريخ** — يُصفّي حقول الصفوف أو الأعمدة التي تحتوي على قيم التاريخ والوقت فقط (أو خلايا فارغة).
3. **مرشح القيم** — يُصفّي العناصر استنادًا إلى القيم المجمعة لحقل بيانات.
4. **مرشح أعلى 10** — يعرض فقط أعلى أو أدنى عدد N من العناصر مرتبة حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في رؤية كل عنصر فردي في حقل ما.
يستخدم كل أسلوب طريقة مختلفة في فئة `PivotField` أو خاصية في فئة `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `refresh_data()` و`calculate_data()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.
## **مرشح التسميات**
يتيح لك مرشح التسميات تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية بنمط معين. يكون ذلك مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو تحتوي على كلمة بعينها، أو تطابق معيارًا آخر قائمًا على التسمية.
يعرض Aspose.Cells تصفية التسميات من خلال الطريقة `PivotField.filter_by_label(PivotFilterType, label_string)`. يتضمن تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank` وغيرها. تُزوَّد الوسيطة الثانية بسلسلة التسمية المستخدمة في المقارنة.
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري موجود، ويطبق مرشح تسميات بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة فقط مرئية، ثم يُحدّث الجدول المحوري، ويحفظ النتيجة.
```python
import aspose.cells as ac

fileName = "sample.xlsx"
prefix = "B"

# تحميل ملف العمل الموجود الذي يحتوي على جدول محوري
workbook = ac.Workbook(fileName)

# الوصول إلى ورقة العمل حسب الفهرس (ورقة العمل الأولى)
worksheet = workbook.worksheets[0]

# الوصول إلى الجدول المحوري حسب الفهرس
pivot_table = worksheet.pivot_tables[0]

# استرجاع حقل الصف الأول PivotField
row_field = pivot_table.row_fields[0]

# تطبيق مرشح التسمية — عرض عناصر الصفوف التي تبدأ تسمياتها بالبادئة المقدمة فقط
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")

# تحديث وإعادة حساب بيانات الجدول المحوري حتى يتم تطبيق المرشح
pivot_table.pivot_cache.refresh()

# حفظ ملف العمل على القرص
workbook.save(fileName)
```
## **مرشح التاريخ**
تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري وفق معايير قائمة على التاريخ مثل اليوم، أو الأسبوع الماضي، أو هذا الشهر، أو الربع القادم، أو نطاق تاريخي محدد. وهي مرشحات متخصصة تعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.
{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا من نوع التاريخ والوقت فقط أو قيم فارغة. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم نسخ صالحة من `DateTime` أو خلايا فارغة قبل تطبيق هذا المرشح.
{{% /alert %}}
يعرض Aspose.Cells تصفية التاريخ من خلال الطريقة `PivotField.filter_by_date(PivotFilterType, *date_times)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. بناءً على نوع المرشح المختار، تمرر قيمة `DateTime` واحدة أو قيمتين (بالنسبة لـ `Between`، تمرر تاريخي البداية والنهاية).
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري توجد في منطقة الصفوف به حقل تاريخ، ويطبق مرشح تاريخ يقصر العناصر المرئية على نطاق تاريخ معين، ثم يُحدّث الجدول المحوري، ويحفظ المصنف.
```python
from datetime import datetime

input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"

if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)

# تحميل المصنف الموجود الذي يحتوي على الجدول المحوري
workbook = ac.Workbook(input_path)

# الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (بالفهرس)
worksheet = workbook.worksheets[0]

# الوصول إلى الجدول المحوري بواسطة الفهرس
pivot_table = worksheet.pivot_tables[0]

# استرجاع حقل التاريخ PivotField من منطقة الصفوف
# (يعمل مرشح التاريخ فقط عندما تحتوي منطقة الصفوف/الأعمدة على خلايا تاريخ-وقت فقط أو خلايا فارغة)
date_field = pivot_table.row_fields[0]

# تحديد معيار التاريخ لمرشح Between
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# تطبيق مرشح التاريخ على الحقل المحوري
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# تحديث وإعادة حساب الجدول المحوري ليصبح المرشح ساري المفعول
pivot_table.pivot_cache.refresh()

# حفظ المصنف
workbook.save(output_path)
```
## **مرشح القيم**
تعمل مرشحات القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. وبدلًا من مطابقة تسميات النصوص، فإنها تقارن الإجماليات الرقمية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو عرض المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.
يعرض Aspose.Cells تصفية القيم من خلال الطريقة `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`. يستخدم معامل `PivotFilterType` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. يحدد معامل `value_field` حقل البيانات الذي يجب تقييمه، في حين تُمرَّر قيمة العتبة (أو قيمها) في الوسيطات الأخيرة.
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري، ويطبق مرشح قيم يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة عتبة عددية، ثم يُحدّث الجدول المحوري، ويحفظ المصنف.
```python
import aspose.cells as ac

workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# العثور على فهرس حقل البيانات يدويًا نظرًا لأن PivotFieldCollection لا يحتوي على IndexOf
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break

if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivot_table.pivot_cache.refresh()

workbook.save("output.xlsx")
```
## **مرشح أعلى 10**
مرشح أعلى 10 هو شكل متخصص من مرشح القيم يحتفظ فقط بأعلى أو أدنى عدد N من العناصر بناءً على حقل قيمة مختار. يُستخدم بشكل شائع في تقارير الترتيب مثل "أفضل 10 منتجات من حيث الإيرادات" أو "أسوأ 5 مناطق من حيث عدد المبيعات".
{{% alert color="primary" %}}
لا يكون مرشح أعلى 10 فعالًا إلا عندما يحتوي الجدول المحوري على حقل قيمة محوري واحد أو أكثر في منطقة البيانات. فبدون وجود حقل قيمة واحد على الأقل، لا يوجد مقياس مجمع لترتيب العناصر وفقًا له، ولا يمكن تطبيق المرشح.
{{% /alert %}}
يعرض Aspose.Cells تصفية أعلى 10 من خلال الطريقة `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)`. يحدد معامل `item_count` عدد العناصر التي يجب الاحتفاظ بها، ويشير `is_top` إلى الاحتفاظ بأعلى العناصر (True) أو أدنى العناصر (False)، ويُحيل `value_field` إلى حقل البيانات المستخدم للترتيب، بينما يتحكم `PivotFilterType` في كيفية حساب القيمة (عادةً `Sum`، وكذلك `Count` و`Percent`).
يقوم المثال التالي بتحميل مصنف يحتوي على جدول محوري يضم حقل قيمة، ويطبق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر من حيث مجموع المبيعات، ثم يُحدّث الجدول المحوري، ويحفظ المصنف.
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

# تحميل المصنف الحالي الذي يحتوي على الجدول المحوري
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)

# الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (الفهرس 0)
worksheet = workbook.worksheets[0]

# الوصول إلى الجدول المحوري عن طريق الفهرس
pivotTable = worksheet.pivot_tables[0]

# التحقق من وجود حقل قيمة واحد على الأقل في منطقة البيانات
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# استرجاع حقل الصف المستهدف (الحقل الذي نريد تطبيق Top 10 عليه)
rowField = pivotTable.row_fields[0]

# حقل البيانات الأول (والوحيد) يقع عند الفهرس 0؛ Top 10 تصنف بناءً عليه.
valueFieldIndex = 0

# تطبيق مرشح Top 10 على حقل الصف:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (أعلى N؛ false تعني أدنى N)
#   - valueFieldIndex = فهرس حقل البيانات المستخدم لتصنيف العناصر
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# تحديث بيانات الجدول المحوري وإعادة حسابها حتى يصبح المرشح ساري المفعول
pivotTable.pivot_cache.refresh()

# حفظ المصنف
workbook.save(outputPath)
```
## **التصفية عن طريق إخفاء أو إظهار عناصر الجدول المحوري**
بالإضافة إلى واجهات التصفية البرمجية المنظمة، يتيح لك Aspose.Cells التحكم في رؤية كل عنصر محوري فردي بشكل مباشر. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ `PivotField` وتبديل الخاصية `is_hidden`، يمكنك إخفاء عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي تعيين `is_hidden = True` إلى إخفاء العنصر من الجدول المحوري؛ بينما يؤدي تعيين `is_hidden = False` إلى إظهاره مجددًا وجعله مرئيًا.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر ما، مثل إخفاء عدد صغير من الفئات المسماة التي يجب ألا تظهر في تقرير معين. يقوم المثال أدناه بتحميل جدول محوري، وإخفاء عنصر معين بالاسم، وعرض كيفية إظهاره، ثم تحديث الجدول المحوري، وحفظ المصنف.
```python
import aspose.cells as ac

# تحميل مصنف موجود يحتوي على جدول محوري
workbook = ac.Workbook("pivot_table_sample.xlsx")

# الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
sheet = workbook.worksheets[0]

# الوصول إلى الجدول المحوري بواسطة الفهرس (الجدول المحوري الأول في الورقة)
pivot_table = sheet.pivot_tables[0]

# استرجاع حقل الجدول المحوري المستهدف (حقل تسمية الصف الأول الذي سنخفي/نظهر العناصر فيه)
pivot_field = pivot_table.row_fields[0]

# التكرار عبر مجموعة عناصر الحقل المحوري المحدد
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # إخفاء عناصر الجدول المحوري التي تطابق اسمًا/معيارًا محددًا
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # عرض توضيحي لإظهار العنصر: إعادة عرض عنصر محوري مخفي سابقًا
    if item.name == "Item3":
        item.is_hidden = False

# تحديث وإعادة حساب الجدول المحوري حتى تصبح التغييرات سارية المفعول
pivot_table.pivot_cache.refresh()

# حفظ المصنف — تبقى العناصر المخفية في البيانات الأساسية
# ولكن يتم استبعادها من مخرجات الجدول المحوري المعروضة
workbook.save("output_pivot_filtered.xlsx")
```
## **الملخص**
يوفر Aspose.Cells for Python via .NET مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تطابق تلك المتوفرة في Microsoft Excel. تغطي مرشحات التسميات والتاريخ والقيم معظم السيناريوهات التحليلية الشائعة، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. وعندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.is_hidden` حلاً مرنًا على مستوى العناصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسميات ثم إخفاء عناصر محددة — إنشاء تقارير جداول محورية مستهدفة بدقة بالكامل من خلال الكود.
{{< app/cells/assistant language="python-net" >}}