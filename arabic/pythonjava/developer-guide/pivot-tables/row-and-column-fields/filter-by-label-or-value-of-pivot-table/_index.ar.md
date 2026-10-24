---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for Python via Java إمكانيات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسميات، ومرشحات التواريخ، ومرشحات القيم، ومرشحات أعلى 10، وكذلك من خلال إخفاء أو إظهار عناصر الجدول المحوري.
keywords: Aspose.Cells, مكتبة Python عبر Java, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أعلى 10, عنصر الجدول المحوري, إخفاء عنصر الجدول المحوري
type: docs
weight: 10
url: /ar/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في الجدول المحوري. يمكنك تطبيق مرشحات التسميات على حقول الصفوف أو الأعمدة النصية، واستخدام مرشحات التواريخ عندما يحتوي الحقل على خلايا من نوع التاريخ والوقت أو خلايا فارغة فقط، وتطبيق مرشحات القيم على الأرقام المجمعة، واستخدام مرشحات أعلى 10 للترتيب حسب حقل قيمة، أو إخفاء وإظهار عناصر الجدول المحوري يدويًا باستخدام الخاصية `is_hidden`. يتم الكشف عن كل استراتيجية من خلال واجهات برمجة التطبيقات المخصصة في فئتي `PivotField` و`PivotItem`.
{{% /alert %}}

## **Introduction**
تُعد الجداول المحورية أدوات تحليلية قوية، ولكن الملخصات الخام غالبًا ما تحتوي على قدر أكبر بكثير من المعلومات مما تحتاج إلى عرضه. تُعد التصفية الآلية الأساسية لتضييق نطاق الجدول المحوري بحيث يقتصر على الصفوف أو الأعمدة أو القيم المهمة لتقرير معين. يُطابق Aspose.Cells for Python via Java إمكانيات التصفية المتوفرة في Microsoft Excel، ويكشف عنها برمجيًا بحيث يمكن أتمتة إنشاء التقارير بالكامل.
تتناول هذه المقالة استراتيجيات التصفية التالية:
1. **مرشح التسمية** — يُصفّي عناصر حقل الصف أو العمود بناءً على تسمياتها النصية.
2. **مرشح التاريخ** — يُصفّي حقول الصفوف أو الأعمدة التي تحتوي على قيم التاريخ والوقت فقط (أو خلايا فارغة).
3. **مرشح القيمة** — يُصفّي العناصر بناءً على القيم المجمعة لحقل بيانات.
4. **مرشح أعلى 10** — يعرض فقط أفضل أو أسوأ N من العناصر مرتبة حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في ظهور كل عنصر على حدة في الحقل.
يستخدم كل أسلوب أسلوبًا مختلفًا في فئة `PivotField` أو خاصية في فئة `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `refresh_data()` و`calculate_data()` على الجدول المحوري بحيث تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **Label Filter**
يتيح لك مرشح التسمية تصفية عناصر حقل الصف أو العمود عن طريق مقارنة تسمياتها النصية بنمط معين. يكون هذا مفيدًا عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو التي تحتوي على كلمة بعينها، أو التي تطابق معيارًا قائمًا على التسمية.
يكشف Aspose.Cells عن التصفية حسب التسمية من خلال الأسلوب `PivotField.filter_by_label(PivotFilterType, str)`. يشمل تعداد `PivotFilterType` قيمًا مثل `CaptionBeginsWith` و`CaptionContains` و`CaptionEndsWith` و`CaptionDoesNotContain` و`CaptionIsNotBlank` و`CaptionIsBlank`، وغيرها. تُمرر الوسيطة الثانية سلسلة التسمية المستخدمة في المقارنة.
يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويُطبّق مرشح تسمية بحيث تظل العناصر التي تبدأ تسمياتها بادئة محددة فقط مرئية، ثم يُحدّث الجدول المحوري ويحفظ النتيجة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the first row PivotField
rowField = pivotTable.getRowFields().get(0)
# Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook back to disk
workbook.save(fileName)
jpype.shutdownJVM()
```

## **Date Filter**
تتيح لك مرشحات التاريخ تضييق نطاق الجدول المحوري بناءً على معايير قائمة على التاريخ مثل اليوم أو الأسبوع الماضي أو هذا الشهر أو الربع القادم أو نطاق تاريخ محدد. تُعد هذه المرشحات متخصصة وتعمل فقط مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصف أو العمود على خلايا من نوع التاريخ والوقت أو قيم فارغة فقط. إذا كان الحقل الأساسي يحتوي على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن يُنتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ ومن أن جميع القيم هي نسخ صحيحة من `DateTime` أو خلايا فارغة قبل تطبيق هذا المرشح.
يكشف Aspose.Cells عن التصفية حسب التاريخ من خلال الأسلوب `PivotField.filter_by_date(PivotFilterType, values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخ مخصصة مثل `Today` و`Yesterday` و`LastWeek` و`ThisWeek` و`NextWeek` و`LastMonth` و`ThisMonth` و`NextMonth` و`LastQuarter` و`ThisQuarter` و`NextQuarter` و`LastYear` و`ThisYear` و`NextYear` و`Between`. بناءً على نوع المرشح المختار، تُمرر قيمة `DateTime` واحدة أو قيمتين (بالنسبة لـ`Between` تُمرر تاريخ البدء وتاريخ الانتهاء).
يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري توجد في منطقة الصفوف فيه حقل تاريخ، ويُطبّق مرشح تاريخ يقصر العناصر المرئية على نطاق تاريخ معين، ثم يُحدّث الجدول المحوري ويحفظ المصنف.
{{% /alert %}}

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"
if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")
# Load the existing workbook that contains the pivot table
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
dateField = pivotTable.getRowFields().get(0)
# Define the date criterion for the Between filter
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)
# Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate)
# Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh()
# Persist the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Value Filter**
تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات الخاصة به. وبدلًا من مطابقة تسميات النص، فإنها تُقارن الإجماليات الرقمية بحد معين. تتضمن حالات الاستخدام النموذجية عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق معين فقط.
يكشف Aspose.Cells عن التصفية حسب القيمة من خلال الأسلوب `PivotField.filter_by_value(value_field, filter_type, values)`. تستخدم وسيطة `filter_type` قيمًا مثل `ValueGreaterThan` و`ValueLessThan` و`ValueBetween` و`ValueEqual` و`ValueNotEqual` و`ValueGreaterThanOrEqual` و`ValueLessThanOrEqual`. تُحدد وسيطة `value_field` حقل البيانات الذي يجب تقييمه، بينما تُمرر الوسيطة الأخيرة (أو الوسيطات) قيمة (قيم) العتبة.
يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويُطبّق مرشح قيمة يحتفظ فقط بالعناصر التي تتجاوز مبيعاتها المجمعة عتبة رقمية معينة، ثم يُحدّث الجدول المحوري ويحفظ المصنف.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)
rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break
if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))
pivotTable.getPivotCache().refresh()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Top 10 Filter**
يُعد مرشح أعلى 10 شكلًا متخصصًا من مرشحات القيمة يحتفظ فقط بأعلى أو أقل عدد N من العناصر بناءً على حقل قيمة مختار. يُستخدم بشكل شائع في تقارير الترتيب مثل "أفضل 10 منتجات من حيث الإيرادات" أو "أسوأ 5 مناطق من حيث عدد المبيعات".

{{% alert color="primary" %}}
لا يكون مرشح أعلى 10 فعالًا إلا عندما يحتوي الجدول المحوري على حقل قيمة واحد أو أكثر في منطقة البيانات. فبدون وجود حقل قيمة واحد على الأقل، لا يوجد مقياس مُجمّع لترتيب العناصر وفقًا له، ولا يمكن تطبيق المرشح.
يكشف Aspose.Cells عن التصفية حسب أعلى 10 من خلال الأسلوب `PivotField.filter_top10(item_count, is_top, value_field, filter_type)`. تُحدد وسيطة `item_count` عدد العناصر التي يجب الاحتفاظ بها، وتشير `is_top` إلى الاحتفاظ بأفضل العناصر (true) أو أسوأها (false)، ويُشير `value_field` إلى حقل البيانات المستخدم للترتيب، ويتحكم `filter_type` في كيفية حساب القيمة (عادةً `Sum`، ولكن أيضًا `Count` و`Percent`).
يُحمّل المثال التالي مصنفًا يحتوي على جدول محوري يتضمن حقل قيمة، ويُطبّق مرشح أعلى 10 للاحتفاظ فقط بأعلى 10 عناصر من حيث مجموع المبيعات، ثم يُحدّث الجدول المحوري ويحفظ المصنف.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Confirm there is at least one value PivotField in the data area
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.getRowFields().get(0)
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.SUM, True, 10)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Filter by Hiding or Unhiding Pivot Items**
بالإضافة إلى واجهات برمجة APIs المنظمة للمرشحات، يتيح لك Aspose.Cells التحكم في ظهور كل عنصر من عناصر الجدول المحوري على حدة مباشرةً. من خلال التكرار عبر مجموعة `PivotItems` الخاصة بـ`PivotField` وتبديل الخاصية `is_hidden`، يمكنك إخفاء عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي تعيين `is_hidden = True` إلى إخفاء العنصر من الجدول المحوري، بينما يؤدي تعيين `is_hidden = False` إلى إظهاره وجعله مرئيًا مرة أخرى.
يكون هذا الأسلوب مفيدًا عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر معين، مثل إخفاء عدد صغير من الفئات المُسماة التي لا ينبغي أن تظهر في تقرير معين. يُحمّل المثال التالي جدولًا محوريًا، ويُخفي عنصرًا محددًا بالاسم، ويُوضح كيفية إظهاره مرة أخرى، ثم يُحدّث الجدول المحوري ويحفظ المصنف.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem
# Load an existing workbook containing a pivot table
workbook = Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.getWorksheets().get(0)
# Access the pivot table by index (the first pivot table on the sheet)
pivotTable = sheet.getPivotTables().get(0)
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivotField = pivotTable.getRowFields().get(0)
# Iterate through the PivotItems collection of the selected PivotField
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)
    # Hide pivot items that match a specific name/criterion
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setHidden(True)
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.getName() == "Item3":
        item.setHidden(False)
# Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
jpype.shutdownJVM()
```

## **Summary**
يوفر Aspose.Cells for Python via Java مجموعة كاملة من إمكانيات تصفية الجداول المحورية التي تُطابق تلك المتوفرة في Microsoft Excel. تغطي مرشحات التسميات والتواريخ والقيم السيناريوهات التحليلية الأكثر شيوعًا، بينما يتعامل مرشح أعلى 10 مع تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `PivotItem.is_hidden` بديلًا مرنًا على مستوى العناصر. يتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جدول محوري مستهدفة بدقة بالكامل من خلال الكود.

## Related Articles
- [إدراج جدول محوري](/cells/ar/python-java/create-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري في Aspose.Cells for Python via Java](/cells/ar/python-java/pivot-table-add-row-and-column-fields/)
- [إضافة حقول مرشح إلى جدول محوري في Aspose.Cells for Python via Java](/cells/ar/python-java/add-page-field-in-pivot-table/)
- [إدارة حقول قيم الجدول المحوري في Aspose.Cells for Python via Java](/cells/ar/python-java/manage-value-fields/)
- [تحديث الجداول المحورية وذاكرة التخزين المؤقت للمحاور في Aspose.Cells for Python via Java](/cells/ar/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}