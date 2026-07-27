---
title: إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: إضافة حقول التصفية
description: تعلّم كيفية إضافة وتكوين حقول الصفحة في الجداول المحورية باستخدام Aspose.Cells for Python via .NET، بما في ذلك إضافة حقول الصفحة، والتصفية أحادية التحديد، والتصفية متعددة التحديد.
keywords: Aspose.Cells, Python via .NET, جدول محوري, حقل صفحة, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, تصفية
type: docs
weight: 250
url: /ar/python-net/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells دورة الحياة الكاملة لحقول الصفحة في الجداول المحورية. يمكنك إضافة حقل صفحة من خلال واجهة برمجة عالية المستوى أو من خلال مجموعة `page_fields` منخفضة المستوى، ويمكنك تشغيل مرشح الصفحة في وضع التحديد الفردي، أو مسحه لإظهار كل عناصر الصفحة، أو تبديل الحقل إلى التحديد المتعدد بحيث يمكن للمستخدمين اختيار عدة عناصر صفحة في وقت واحد من خلال واجهة مربعات الاختيار في Excel.
{{% /alert %}}

## **مقدمة**

حقل التصفية هو حقل محوري يتحكم في *أي مجموعة فرعية* من البيانات المصدر يعرضها جسم المحور. يراه المستخدمون النهائيون كقائمة منسدلة في أعلى المحور المعروض في Excel، ويؤدي اختيار أحد عناصر الصفحة المتاحة إلى إعادة بناء جسم المحور بحيث يتم تلخيص السجلات التي تنتمي إلى عنصر التصفية هذا فقط. يصبح الحقل المحوري حقل صفحة عند تسجيله كـ `PivotFieldType.PAGE` بدلاً من `PivotFieldType.ROW` أو `PivotFieldType.COLUMN` أو `PivotFieldType.DATA`.

يمكن أن يعمل حقل التصفية بسلوكين. في سلوك **التحديد الفردي** الافتراضي، لا يظهر إلا عنصر صفحة واحد في كل مرة، لذلك يلخص جسم المحور مجموعة فرعية واحدة بالضبط. في سلوك **التحديد المتعدد**، يعرض الحقل قائمة مربعات اختيار، ويلخص جسم المحور اتحاد كل عناصر الصفحة المحددة. يمكن نقل نفس حقل المصدر ذهاباً وإياباً بين هذه السلوكيات عن طريق تبديل خاصية واحدة.

يعرض Aspose.Cells for Python via .NET طريقتين متكافئتين لتسجيل حقل صفحة. واجهة المستوى العالي هي `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")`، التي تأخذ اسم عمود المصدر وتضيف الحقل في استدعاء واحد. واجهة المستوى المنخفض هي `PivotTable.page_fields.add(PivotField)`، التي تُستخدم عندما يكون لديك بالفعل مرجع `PivotField` وتريد إضافة نفس مثيل الحقل إلى منطقة التصفية. تنتهي كلتا الواجهتين إلى ملء نفس مجموعة `page_fields`، وتوضح بقية هذه المقالة كيفية الاختيار بينهما وكيفية تشغيل كل وضع تصفية.

## **إضافة حقل صفحة**

توجد طريقتان لتسجيل حقل محوري في منطقة التصفية. يأخذ استدعاء المستوى العالي اسم عمود المصدر كسلسلة نصية وهو المسار الأكثر شيوعاً. يقبل استدعاء المستوى المنخفض مثيل `PivotField` موجوداً وهو مناسب عندما يجب إعادة استخدام نفس كائن الحقل عبر مناطق محورية متعددة. يضع كلا الاستدعاءين الحقل في `PivotTable.page_fields`، وبعد ذلك يظهر كقائمة منسدلة للصفحة في أعلى المحور المعروض.

### إضافة حقل صفحة باستخدام add_field_to_area

يبني المثال التالي مجموعة بيانات صغيرة مكونة من Fruit / Year / Amount، ويضع جدولاً محورياً عند الخلية E3 مع `Fruit` في منطقة الصفوف، و`Amount` في منطقة البيانات، و`Year` في منطقة التصفية، ويحدّث الجدول المحوري، ويحفظ المصنف.

```python
import aspose.cells as ac

# إنشاء مصنف جديد
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# إعداد صف الرأس
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# تعبئة 9 صفوف من البيانات النموذجية: الفاكهة، السنة، المبلغ
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# إضافة جدول محوري مثبت عند الخلية E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# إضافة الحقول إلى مناطقها: الفاكهة كصف، المبلغ كبيانات، السنة كحقل صفحة
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# تحديث وحساب بيانات الجدول المحوري
pivot_table.refresh_data()
pivot_table.calculate_data()

# حفظ المصنف
workbook.save("pageFieldSample.xlsx")
```

### إضافة حقل صفحة باستخدام page_fields.add

عندما تعمل بالفعل مع مثيل `PivotField`، يمكنك تمريره مباشرة إلى `PivotTable.page_fields.add`. يتم إنشاء الجدول المحوري وحقل التصفية تماماً كما في السيناريو السابق؛ فقط تسجيل منطقة التصفية النهائية يتم استبداله باستدعاء واجهة المستوى المنخفض.

```python
import aspose.cells as ac

# — يتم إنشاء الجدول المحوري وحقل الصفحة تمامًا كما في
#   السيناريو 1a (بيانات الفاكهة/السنة/المبلغ، الجدول المحوري في E3، الفاكهة→الصف،
#   المبلغ→البيانات). أدناه نحصل على حقل السنة المحوري من
#   مجموعة BaseFields ونمرره إلى PageFields.Add — البديل
#   منخفض المستوى لـ AddFieldToArea. النتيجة هي
#   مطابقة وظيفيًا للسيناريو 1a.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# العناوين
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# بيانات العينة (9 صفوف)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# إضافة جدول محوري في E3 يغطي A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# الفاكهة -> الصف، المبلغ -> البيانات (ستذهب السنة إلى الصفحة أدناه)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# نهج منخفض المستوى: احصل على حقل السنة المحوري الموجود من BaseFields
# وقم بتسجيله في منطقة الصفحة عبر PageFields.Add(PivotField).
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# قم بالتحديث حتى ينعكس حقل الصفحة الجديد في المصنف المحفوظ
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **التصفية أحادية التحديد (عرض عنصر صفحة واحد)**

في سلوك التحديد الفردي الافتراضي، يُعرض حقل التصفية كقائمة منسدلة واحدة ويحدد العدد الصحيح `PivotField.current_page_item` عنصر التصفية الذي يقود جسم المحور. يؤدي تعيين فهرس محدد إلى اختيار هذا العنصر فقط؛ ويؤدي تعيين القيمة الحارسية الخاصة `0x7FFD` (عشري 32765) إلى مسح المرشح بحيث يتم تلخيص كل عناصر الصفحة في وقت واحد. التحديد الفردي هو الوضع الافتراضي؛ لست بحاجة إلى تفعيله صراحةً.

### عرض جميع العناصر

يكون تعيين `current_page_item` إلى القيمة السحرية `0x7FFD` مكافئاً لمسح مرشح الصفحة: يلخص جسم المحور كل عنصر صفحة كما لو لم يتم تطبيق أي مرشح.

```python
import aspose.cells as ac

# إنشاء مصنف جديد
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# تعبئة بيانات الفاكهة/السنة/المبلغ
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# إنشاء جدول محوري في E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# تكوين حقول الجدول المحوري: الفاكهة→صف، المبلغ→بيانات، السنة→صفحة
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.refresh_data()
pivot_table.calculate_data()

# مسح مرشح الصفحة بحيث يكون كل عنصر في حقل الصفحة مرئياً.
# 0x7FFD (عشري 32765) هي القيمة الحارسية الخاصة التي تعني "جميع العناصر" —
# مكافئة لتحديد "(الكل)" في القائمة المنسدلة لحقل الصفحة في Excel.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### عرض عنصر محدد واحد

يؤدي تعيين `current_page_item` إلى فهرس حقيقي إلى اختيار عنصر التصفية هذا فقط. الفهرس هو موضع العنصر في قائمة العناصر المرتبة لحقل التصفية، فعلى سبيل المثال يحدد `1` العنصر الثاني بعد الفرز.

```python
import aspose.cells as ac

# إنشاء مصنف
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# إضافة بيانات تجريبية (الفاكهة/السنة/المبلغ)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# إضافة جدول محوري في E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# إضافة الحقول: الفاكهة→صف، المبلغ→بيانات، السنة→صفحة
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# عمليات خاصة بحقل الصفحة
pivot_table.page_fields[0].current_page_item = 1  # 1 = العنصر الثاني بالترتيب (مثلاً "2021")

# تحديث وحساب الجدول المحوري
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **التصفية متعددة التحديد**

تحوّل التصفية متعددة التحديد قائمة الصفحة المنسدلة إلى قائمة مربعات اختيار وتسمح للمستخدم النهائي باختيار عدة عناصر صفحة في وقت واحد. يعرض Aspose.Cells خاصيتين تعملان معاً. يجب تعيين `PivotField.is_multiple_item_selection_allowed` إلى `True` قبل أن تصبح واجهة التحديد المتعددة فعالة على الإطلاق. بعد تفعيلها، تتحكم `PivotItem.is_hidden` في العناصر التي تظهر في قائمة مربعات الاختيار، بحيث يمكنك إما إظهار كل العناصر أو السماح فقط بعناصر محددة.

يمكّن الكود أدناه التحديد المتعدد على نفس حقل صفحة Year المُنشأ في السيناريو 1a، ثم يعرض نمطين: الجزء A يكشف كل عنصر صفحة عن طريق ترك `is_hidden` معيناً على `False` لكل إدخال، بينما يسمح الجزء B فقط بقيم المصدر التي تختارها ويخفي كل شيء آخر من خلال كتلة `if` / `elif` التي تختبر `pivot_items[i].get_string_value()`.

```python
import aspose.cells as ac

# — يتم إنشاء الجدول المحوري وحقل الصفحة تمامًا كما في
#   السيناريو 1أ (بيانات الفاكهة/السنة/المبلغ، الجدول المحوري عند E3، الفاكهة→الصف،
#   المبلغ→البيانات، السنة→الصفحة عبر AddFieldToArea).
#   أدناه نقوم بتطبيق التصفية متعددة التحديد على حقل الصفحة.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# بيانات تجريبية: الفاكهة | السنة | المبلغ
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — تمكين التحديد المتعدد على حقل الصفحة
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# الجزء أ — تحديد جميع العناصر (جعل كل عنصر مرئيًا)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# الجزء ب — تحديد عناصر محددة فقط حسب القيمة المصدرية
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **ملاحظة:** عند استخدام التصفية متعددة التحديد من خلال `PivotItem.is_hidden`، **يجب أن يظل عنصر `PivotItem` واحد على الأقل مرئياً** (`is_hidden == False`). إذا تم إخفاء كل العناصر، فإن Excel إما يتعطل عند فتح الملف أو يعرض محوراً فارغاً. تحقق دائماً من أن قائمة السماح متعددة التحديد تتضمن عنصراً واحداً على الأقل من بيانات المصدر.

## **أي واجهة برمجة وأي وضع يجب أن أستخدم؟**

يلخص الجدول أدناه متى تستخدم كل واجهة برمجة ووضع بحيث يمكنك اختيار المجموعة الصحيحة دون قراءة كل سيناريو بالتفصيل.

| السيناريو / حالة الاستخدام | واجهة البرمجة الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل صفحة باسم عمود المصدر (الأكثر شيوعاً) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | غير متاح | مستوى عالٍ، سطر واحد. استخدم هذا ما لم تكن بحاجة إلى مرجع `PivotField`. |
| إضافة حقل صفحة عندما يكون لديك بالفعل كائن `PivotField` | `PivotTable.page_fields.add(PivotField)` | غير متاح | استخدم عندما تم الحصول على كائن الحقل من مكان آخر أو يحتاج إلى إعادة الاستخدام. |
| التصفية إلى عنصر صفحة واحد (الوضع الافتراضي) | `PivotField.current_page_item` | تعيين إلى فهرس محدد | على سبيل المثال، يعرض `1` العنصر الثاني في القائمة المرتبة. |
| عرض جميع العناصر / مسح مرشح الصفحة | `PivotField.current_page_item` | تعيين إلى `0x7FFD` | القيمة السحرية `0x7FFD` (عشري 32765) هي القيمة الحارسة لـ "كل العناصر". |
| تفعيل واجهة التحديد المتعدد في Excel | `PivotField.is_multiple_item_selection_allowed` | تعيين إلى `True` | مطلوب قبل أن يصبح أي استدعاء لـ `is_hidden` فعالاً. |
| إخفاء / إظهار العناصر الفردية في قائمة التحديد المتعدد | `PivotItem.is_hidden` | تعيين لكل عنصر | يجب أن يظل عنصر واحد على الأقل مرئياً (`is_hidden == False`). |

{{% alert color="primary" %}}
تذكر دائماً قيد الرؤية عند تكوين التصفية متعددة التحديد. إذا تم إخفاء كل `PivotItem` في حقل صفحة متعدد التحديد، فإن Excel يتعطل عند الفتح أو يعرض محوراً فارغاً. ابنِ قائمة السماح الخاصة بك مقابل بيانات المصدر بحيث يظل عنصر واحد على الأقل مرئياً، وستفتح المصنفات المحفوظة بشكل موثوق على كل جهاز.
{{% /alert %}}


{{< app/cells/assistant language="python" >}}