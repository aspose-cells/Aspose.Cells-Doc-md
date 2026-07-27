---
title: إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: إضافة حقول التصفية
description: تعلم كيفية إضافة وتكوين حقول التصفية في الجداول المحورية باستخدام Aspose.Cells for Python عبر Java، بما في ذلك إضافة حقول التصفية، والتصفية أحادية الاختيار، والتصفية متعددة الاختيارات.
keywords: Aspose.Cells, Python, Java, جدول محوري, حقل التصفية, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, تصفية
type: docs
weight: 250
url: /ar/python-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells دورة الحياة الكاملة لحقول التصفية في الجداول المحورية. يمكنك إضافة حقل صفحة من خلال واجهة برمجة تطبيقات عالية المستوى ملائمة أو من خلال مجموعة `page_fields` ذات المستوى الأدنى، ويمكنك تشغيل مرشح الصفحة في وضع الاختيار الفردي، أو مسحه لإظهار كل عنصر من عناصر الصفحة، أو تبديل الحقل إلى الاختيار المتعدد بحيث يمكن للمستخدمين اختيار عدة عناصر من عناصر الصفحة دفعة واحدة من خلال واجهة المستخدم الخاصة بمربعات الاختيار في Excel.
{{% /alert %}}

## **المقدمة**

حقل التصفية هو حقل محوري يتحكم في *أي مجموعة فرعية* من بيانات المصدر يعرضها جسم الجدول المحوري. يرى المستخدمون النهائيون ذلك كقائمة منسدلة في أعلى الجدول المحوري المعروض في Excel، ويؤدي اختيار أحد عناصر الصفحة المتاحة إلى إعادة بناء جسم الجدول المحوري بحيث يتم تلخيص السجلات التي تنتمي إلى عنصر التصفية هذا فقط. يصبح الحقل المحوري حقل صفحة عند تسجيله كـ `PivotFieldType.PAGE` بدلاً من `PivotFieldType.ROW` أو `PivotFieldType.COLUMN` أو `PivotFieldType.DATA`.

يمكن أن يعمل حقل التصفية بسلوكين. في سلوك **الاختيار الفردي** الافتراضي، يكون عنصر صفحة واحد فقط مرئيًا في كل مرة، لذلك يُلخص جسم الجدول المحوري مجموعة فرعية واحدة بالضبط. في سلوك **الاختيار المتعدد**، يعرض الحقل قائمة مربعات اختيار، ويُلخص جسم الجدول المحوري اتحاد كل عنصر صفحة تم تحديده. يمكن نقل نفس حقل المصدر ذهابًا وإيابًا بين هذه السلوكيات عن طريق تبديل خاصية واحدة.

يوفر Aspose.Cells لـ Aspose.Cells for Python via Java طريقتين متكافئتين لتسجيل حقل التصفية. واجهة برمجة التطبيقات عالية المستوى هي `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")`، والتي تأخذ اسم عمود المصدر وتضيف الحقل في استدعاء واحد. واجهة برمجة التطبيقات ذات المستوى الأدنى هي `PivotTable.page_fields.add(PivotField)`، والتي تُستخدم عندما يكون لديك بالفعل مرجع `PivotField` وتريد إضافة نفس مثيل الحقل إلى منطقة التصفية. تنتهي كلتا واجهات برمجة التطبيقات إلى ملء نفس مجموعة `page_fields`، وتوضح بقية هذه المقالة كيفية الاختيار بينهما وكيفية تشغيل كل وضع تصفية.

## **إضافة حقل صفحة**

هناك طريقتان لتسجيل حقل محوري في منطقة التصفية. يأخذ الاستدعاء عالي المستوى اسم عمود المصدر كسلسلة نصية وهو المسار الأكثر شيوعًا. يقبل الاستدعاء ذو المستوى الأدنى مثيل `PivotField` موجودًا وهو مناسب عندما يجب إعادة استخدام نفس كائن الحقل عبر مناطق محورية متعددة. يضع كلا الاستدعاءين الحقل في `PivotTable.page_fields`، وبعد ذلك يظهر كقائمة منسدلة للصفحة في أعلى الجدول المحوري المعروض.

### إضافة حقل صفحة باستخدام add_field_to_area

يبني المثال التالي مجموعة بيانات صغيرة تحتوي على الفاكهة / السنة / المبلغ، ويضع جدولاً محوريًا في الخلية E3 مع `Fruit` في منطقة الصفوف، و`Amount` في منطقة البيانات، و`Year` في منطقة التصفية، ويقوم بتحديث الجدول المحوري، ويحفظ المصنف.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# إنشاء مصنف جديد
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# إعداد صف العناوين
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# ملء 9 صفوف من البيانات النموذجية: الفاكهة، السنة، المبلغ
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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# إضافة جدول محوري مرتبط بالخلية E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# إضافة الحقول إلى مناطقها: الفاكهة كصف، المبلغ كبيانات، السنة كحقل صفحة
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# تحديث وحساب بيانات الجدول المحوري
pivotTable.refreshData()
pivotTable.calculateData()

# حفظ المصنف
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### إضافة حقل صفحة باستخدام page_fields.add

عندما تعمل بالفعل مع مثيل `PivotField`، يمكنك تمريره مباشرة إلى `PivotTable.page_fields.add`. يتم إنشاء الجدول المحوري وحقل التصفية تمامًا كما في السيناريو السابق؛ يتم استبدال تسجيل منطقة التصفية النهائي فقط باستدعاء واجهة برمجة التطبيقات ذات المستوى الأدنى.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — يتم إنشاء الجدول المحوري وحقل الصفحة تمامًا كما في
#   السيناريو 1أ (بيانات الفاكهة/السنة/المبلغ، الجدول المحوري عند E3، الفاكهة→الصف،
#   المبلغ→البيانات). أدناه نحصل على PivotField الخاص بالسنة من
#   مجموعة BaseFields ونمرره إلى PageFields.Add — البديل
#   منخفض المستوى لـ AddFieldToArea. النتيجة مطابقة وظيفيًا
#   للسيناريو 1أ.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# العناوين
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# بيانات عينة (9 صفوف)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# إضافة جدول محوري عند E3 يغطي A1:C10
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# الفاكهة -> الصف، المبلغ -> البيانات (ستذهب السنة إلى الصفحة أدناه)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# نهج منخفض المستوى: احصل على PivotField الموجود للسنة من BaseFields
# وسجله في منطقة الصفحة عبر PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# قم بالتحديث حتى ينعكس حقل الصفحة الجديد في المصنف المحفوظ
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **التصفية أحادية الاختيار (إظهار عنصر صفحة واحد)**

في سلوك الاختيار الفردي الافتراضي، يتم عرض حقل التصفية كقائمة منسدلة مفردة ويحدد العدد الصحيح `PivotField.current_page_item` عنصر التصفية الذي يقود جسم الجدول المحوري. يحدد تعيين فهرس معين هذا العنصر الواحد؛ ويؤدي تعيين الحارس الخاص `0x7FFD` (عشري 32765) إلى مسح المرشح بحيث يتم تلخيص كل عنصر من عناصر الصفحة دفعة واحدة. الاختيار الفردي هو الافتراضي؛ لا تحتاج إلى تمكينه بشكل صريح.

### **إظهار كل العناصر**

يكون تعيين `current_page_item` إلى القيمة السحرية `0x7FFD` مكافئًا لمسح مرشح الصفحة: يُلخص جسم الجدول المحوري كل عنصر من عناصر الصفحة كما لو لم يتم تطبيق أي مرشح.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# إنشاء مصنف جديد
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# تعبئة بيانات الفاكهة/السنة/المبلغ
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

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
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# إنشاء جدول محوري في E3
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# تكوين حقول الجدول المحوري: الفاكهة→الصف، المبلغ→البيانات، السنة→الصفحة
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.refreshData()
pivotTable.calculateData()

# مسح مرشح الصفحة بحيث يكون كل عنصر في حقل الصفحة مرئيًا.
# 0x7FFD (عشري 32765) هو القيمة الخفيرية الخاصة التي تعني "كل العناصر" —
# مكافئ لتحديد "(الكل)" في القائمة المنسدلة لحقل الصفحة في Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### **إظهار عنصر محدد واحد**

يؤدي تعيين `current_page_item` إلى فهرس حقيقي إلى اختيار عنصر التصفية الواحد فقط. الفهرس هو موضع العنصر في قائمة العناصر المرتبة لحقل التصفية، فعلى سبيل المثال يحدد `1` العنصر الثاني بعد الفرز.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# إنشاء مصنف
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# إضافة بيانات نموذجية (فاكهة/سنة/مبلغ)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# إضافة جدول محوري عند E3
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# إضافة الحقول: فاكهة→صف، مبلغ→بيانات، سنة→صفحة
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# عمليات خاصة بحقل الصفحة
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = العنصر الثاني بالترتيب (مثلاً "2021")

# تحديث وحساب الجدول المحوري
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **التصفية متعددة الاختيارات**

تحول التصفية متعددة الاختيارات القائمة المنسدلة للصفحة إلى قائمة مربعات اختيار وتتيح للمستخدم النهائي اختيار عدة عناصر من عناصر الصفحة في وقت واحد. يعرض Aspose.Cells خاصيتين تعملان معًا. يجب تعيين `PivotField.is_multiple_item_selection_allowed` على `True` قبل أن تصبح واجهة المستخدم متعددة الاختيارات فعالة على الإطلاق. بعد تمكينها، تتحكم `PivotItem.is_hidden` في العناصر التي تظهر في قائمة مربعات الاختيار، بحيث يمكنك إما إظهار كل عنصر أو السماح فقط بعناصر محددة.

يعمل الكود أدناه على تمكين الاختيار المتعدد على نفس حقل صفحة Year الذي تم إنشاؤه في السيناريو 1a، ثم يعرض نمطين: الجزء A يكشف عن كل عنصر من عناصر الصفحة عن طريق ترك `is_hidden` معينًا على `False` لكل إدخال، بينما الجزء B يسمح فقط بقيم المصدر التي تختارها وإخفاء كل شيء آخر من خلال كتلة `switch (pivot_items[i].get_string_value())`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — يتم إنشاء الجدول المحوري وحقل الصفحة تمامًا كما في
#   السيناريو 1أ (بيانات الفاكهة/السنة/المبلغ، الجدول المحوري عند E3، الفاكهة→الصف،
#   المبلغ→البيانات، السنة→الصفحة عبر AddFieldToArea).
#   أدناه نطبق التصفية متعددة التحديد على حقل الصفحة.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# بيانات العينة: فاكهة | سنة | مبلغ
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

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
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — تمكين التحديد المتعدد على حقل الصفحة
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# الجزء أ — حدد جميع العناصر (اجعل كل عنصر مرئيًا)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# الجزء ب — حدد عناصر محددة فقط حسب قيمة المصدر
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **ملاحظة:** عند استخدام التصفية متعددة الاختيارات من خلال `PivotItem.is_hidden`، **يجب أن يظل `PivotItem` واحد على الأقل مرئيًا** (`is_hidden == False`). إذا تم إخفاء كل عنصر، فإن Excel إما يتعطل عند فتح الملف أو يعرض جدولاً محوريًا فارغًا. تحقق دائمًا من أن قائمة السماح متعددة الاختيارات الخاصة بك تتضمن عنصرًا واحدًا على الأقل من بيانات المصدر.

## **أي واجهة برمجة تطبيقات وأي وضع يجب أن أستخدم؟**

يلخص الجدول أدناه متى تستخدم كل واجهة برمجة تطبيقات ووضع حتى تتمكن من اختيار المجموعة الصحيحة دون قراءة كل سيناريو بالتفصيل.

| السيناريو / حالة الاستخدام | واجهة برمجة التطبيقات الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل صفحة حسب اسم عمود المصدر (الأكثر شيوعًا) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | غير متاح | عالي المستوى، في سطر واحد. استخدم هذا ما لم تكن بحاجة إلى مرجع `PivotField`. |
| إضافة حقل صفحة عندما يكون لديك بالفعل كائن `PivotField` | `PivotTable.page_fields.add(PivotField)` | غير متاح | استخدم عندما تم الحصول على كائن الحقل من مكان آخر أو يحتاج إلى إعادة الاستخدام. |
| التصفية إلى عنصر صفحة واحد (الوضع الافتراضي) | `PivotField.current_page_item` | عيّن على فهرس محدد | على سبيل المثال، يعرض `1` العنصر الثاني في القائمة المرتبة. |
| إظهار كل العناصر / مسح مرشح الصفحة | `PivotField.current_page_item` | عيّن على `0x7FFD` | القيمة السحرية `0x7FFD` (عشري 32765) هي الحارس لـ "كل العناصر". |
| تمكين واجهة المستخدم متعددة الاختيارات في Excel | `PivotField.is_multiple_item_selection_allowed` | عيّن على `True` | مطلوب قبل أن تصبح أي استدعاءات لـ `is_hidden` فعالة. |
| إخفاء / إظهار العناصر الفردية في قائمة متعددة الاختيارات | `PivotItem.is_hidden` | عيّن لكل عنصر | يجب أن يظل عنصر واحد على الأقل مرئيًا (`is_hidden == False`). |

{{% alert color="primary" %}}
تذكر دائمًا قيد الرؤية عند تكوين التصفية متعددة الاختيارات. إذا تم إخفاء كل `PivotItem` في حقل صفحة متعدد الاختيارات، فإن Excel يتعطل عند الفتح أو يعرض جدولاً محوريًا فارغًا. أنشئ قائمة السماح الخاصة بك مقابل بيانات المصدر الخاصة بك بحيث يظل عنصر واحد على الأقل مرئيًا، وسيفتح المصنف المحفوظ بشكل موثوق على كل جهاز.
{{% /alert %}}



{{< app/cells/assistant language="python" >}}