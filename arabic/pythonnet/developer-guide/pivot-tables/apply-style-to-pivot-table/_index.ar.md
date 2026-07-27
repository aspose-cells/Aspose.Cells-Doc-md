---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells لـ .NET
linktitle: تطبيق أنماط الجداول المحورية
description: تعرف على كيفية تطبيق الأنماط المضمنة والمخصصة على الجداول المحورية في Aspose.Cells for Python via .NET، بما في ذلك التنسيقات التلقائية القديمة لـ XLS، وأنماط Excel 2007+ الحديثة المسماة، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells Python via .NET نمط الجدول المحوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تطبيق كل من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) وأنماط الجداول المحورية الحديثة المسماة أو المخصصة (المخصصة لملفات `.xlsx` و `.xlsm` و `.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يتم حفظ المصنف به، وليس على التنسيق الذي تم تحميله منه.

{{% /alert %}}

## **مقدمة**

يكشف Aspose.Cells عن واجهتي برمجة تطبيقات متوازيتين للأنماط الخاصة بالجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ المصنف المحمّل من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة يتم تطبيق واجهة برمجة التطبيقات للأنماط الحديثة بدلاً من القديمة.

لمخرجات `.xls` القديمة، استخدم خاصية `PivotTable.auto_format_type` مع تعداد `aspose.cells.pivot.PivotTableAutoFormatType`. تتوافق واجهة برمجة التطبيقات هذه مع منتقي التنسيق التلقائي الذي كان يوفره Excel الكلاسيكي للجداول المحورية.

لمخرجات `.xlsx` و `.xlsm` و `.xlsb` الحديثة، يتوفر نوعان من واجهات برمجة التطبيقات للأنماط:

- `PivotTable.pivot_table_style_type` يحدد أحد الأنماط المسماة المضمنة (سمات فاتحة وداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- `PivotTable.pivot_table_style_name` يحدد نمطًا مخصصًا تحدده بنفسك من خلال `workbook.worksheets.table_styles.add_pivot_table_style(...)`. الأنماط المخصصة مطلوبة كلما أردت تعديل الألوان أو الحدود أو الخطوط بخلاف ما تقدمه الإعدادات المسبقة.

بالإضافة إلى ذلك، يعد `PivotTable.format_all(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أي من واجهتي برمجة التطبيقات لاسم النمط أعلاه. يكون هذا مفيدًا عندما يكون المظهر الموحد مطلوبًا بغض النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مسبق للـ XLS القديم**

يقبل `PivotTable.auto_format_type` قيمة من تعداد `aspose.cells.pivot.PivotTableAutoFormatType`. القيم المتاحة هي `REPORT_1` إلى `REPORT_10`، و `CLASSIC`، و `TABLE_1` إلى `TABLE_10`.

{{% alert color="primary" %}}

لا يتم الالتزام بـ `auto_format_type` إلا عند حفظ المصنف بصيغة `.xls`. عندما يتم حفظ نفس المصنف بصيغة `.xlsx` أو `.xlsm` أو `.xlsb`، يتجاهل Excel هذه الخاصية ويعود إلى إعدادات `pivot_table_style_type` و `pivot_table_style_name`.

{{% /alert %}}

يحمل المثال التالي مصنفًا جديدًا، ويملأ بيانات العينة Fruit/Year/Amount، ويضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.REPORT_5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}

**لماذا لا توجد حقول أعمدة؟** تم تصميم التنسيقات التلقائية من سلسلة Report (`Report1` إلى `Report10`، `Table1` إلى `Table10`) في Excel الكلاسيكي لـ **جداول محورية أحادية البُعد** تحتوي على حقول صفوف وقيم فقط — وليس لديها تنسيق مدمج لرؤوس حقول الأعمدة. إذا احتاج الجدول المحوري إلى حقول أعمدة، فاستخدم الإعدادات المسبقة الحديثة `PivotTableStyleType` من السيناريو 2 أدناه بدلاً من ذلك، وهي مصممة للتخطيط ثنائي الأبعاد الذي يستخدمه Excel الحديث.

{{% /alert %}}

```python
import aspose.cells as ac

# السيناريو 1: تطبيق تنسيق تلقائي مسبق الإعداد من XLS القديم
# واجهة برمجة التطبيقات المستخدمة: PivotTable.AutoFormatType
# تنسيق الملف المستهدف: .xls (قديم)
# للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-cells/Aspose.Cells-for-.NET

# إنشاء مصنف جديد
workbook = ac.Workbook()

# الحصول على ورقة العمل الأولى
sheet = workbook.worksheets[0]

# تعبئة البيانات المصدرية بصف الرأس (فاكهة، سنة، مبلغ)
# و 9 صفوف بيانات تغطي العنب، التوت الأزرق، الكيوي، الكرز عبر 2020 و 2021
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")

sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)

sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)

sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)

sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)

sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)

sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)

sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)

sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)

sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)

# إضافة جدول محوري في خلية الوجهة E3، باسم "Pivot1"، باستخدام نطاق المصدر A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# تعيين الحقول: الفاكهة -> الصفوف، السنة -> الأعمدة، المبلغ -> البيانات
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# تطبيق التنسيق التلقائي المسبق الإعداد لـ XLS القديم "Report5"
# ملاحظة: هذه الخاصية ذات معنى فقط عند الحفظ بصيغة .xls.
# عند الحفظ بصيغة .xlsx/.xlsm/.xlsb، يتجاهل Excel AutoFormatType
# ويستخدم ما يحدده PivotTableStyleType / PivotTableStyleName.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# حفظ المصنف بتنسيق .xls القديم
workbook.save("output.xls")
```

## **تطبيق نمط جدول محوري مسمى مسبق حديث**

يقبل `PivotTable.pivot_table_style_type` قيمة من تعداد `aspose.cells.PivotTableStyleType`. يغطي التعداد السمات الفاتحة `PIVOT_TABLE_STYLE_LIGHT_1` إلى `PIVOT_TABLE_STYLE_LIGHT_28` والسمات الداكنة `PIVOT_TABLE_STYLE_DARK_1` إلى `PIVOT_TABLE_STYLE_DARK_28`. يمكن الوصول إلى الأنماط المضافة في Excel 2017 (الموجة الثانية من السمات الفاتحة والداكنة) من خلال نفس التعداد.

هذه هي واجهة برمجة التطبيقات الموصى بها لأي تنسيق ملف حديث. على عكس التنسيق التلقائي القديم، يتم عرض النمط المحدد هنا بشكل دقيق بواسطة Excel ويظل ثابتًا بعد عمليات الحفظ والتحميل عبر أدوات Office الأخرى.

يستخدم المثال التالي نفس بيانات Fruit/Year/Amount، وينشئ جدولًا محوريًا مطابقًا، ويطبق `PIVOT_TABLE_STYLE_DARK_1`، ويحفظ المصنف بصيغة `.xlsx`.

```python
import aspose.cells as ac

# السيناريو 2: تطبيق نمط جاهز مسمى حديث من Excel 2007+ باستخدام PivotTableStyleType.
# تنسيق الملف المستهدف: .xlsx. يوجد تعداد PivotTableStyleType في مساحة الاسم Aspose.Cells
# (وليس في Aspose.Cells.Pivot) — لهذا السبب لا نحتاج إلى أي توجيه using إضافي له.
# مرجع GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# صف العناوين: الفاكهة / السنة / المبلغ
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 صفوف بيانات من الفاكهة / السنة / المبلغ
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# إضافة جدول محوري في E3 باسم "Pivot1"، مصدره من A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# تعيين حقول الجدول المحوري: الفاكهة -> منطقة الصفوف، السنة -> منطقة الأعمدة، المبلغ -> منطقة البيانات
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# تطبيق نمط جدول محوري جاهز مسمى حديث من Excel 2007+.
# PivotTableStyleType هي واجهة برمجة التطبيقات الصحيحة لملفات .xlsx / .xlsm / .xlsb؛ AutoFormatType
# يتم تجاهلها بواسطة Excel لتلك التنسيقات. ينتمي PivotTableStyleDark1 إلى عائلة النمط الداكن
# (PivotTableStyleDark1..PivotTableStyleDark28)، ويكشف نفس التعداد أيضًا عن
# سمات Excel 2017 الأحدث فاتحة/داكنة (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# حفظ كملف .xlsx حديث — هذا هو التنسيق الذي يكون PivotTableStyleType ذا معنى له.
workbook.save("output.xlsx")
```

## **تعريف وتطبيق نمط جدول محوري مخصص**

لا يمكن تعديل الإعدادات المسبقة المضمنة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب عليك تعريف نمط جدول محوري مخصص. تتكون سير العمل من ثلاث خطوات:

1. أضف نمطًا مخصصًا إلى مجموعة `table_styles` في المصنف عبر `workbook.worksheets.table_styles.add_pivot_table_style(name)`. يُرجع هذا فهرس النمط الذي تم إنشاؤه حديثًا.
2. قم بتكوين النمط عن طريق إضافة عناصر (مثل `WHOLE_TABLE` أو `GRAND_TOTAL_ROW`) من خلال `table_style.table_style_elements.add(TableStyleElementType)`، ثم تعيين `Style` لكل عنصر عبر `table_style_element.set_element_style(Style)`.
3. طبق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.pivot_table_style_name` على اسم النمط. لا تستخدم `pivot_table_style_type` هنا، حيث تحدد هذه الخاصية الإعدادات المسبقة المضمنة.

{{% alert color="primary" %}}

`pivot_table_style_name` و `pivot_table_style_type` غير قابلين للتبادل. استخدم `pivot_table_style_type` للإعدادات المسبقة المضمنة، واستخدم `pivot_table_style_name` للأنماط المخصصة التي حددتها من خلال `add_pivot_table_style`. تعيين كليهما غير ضار، ولكن يتم عرض فقط ذلك الذي يطابق المصدر المقصود.

{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة `WHOLE_TABLE` و `FIRST_ROW` و `LAST_ROW` و `FIRST_COLUMN` و `LAST_COLUMN` و `GRAND_TOTAL_ROW` و `GRAND_TOTAL_COLUMN` و `PAGE_FIELD_LABELS` و `PAGE_FIELD_VALUES`.

يحدد المثال التالي نمط جدول محوري مخصص بحد أسود رفيع على `WHOLE_TABLE` وخط أحمر عريض على `GRAND_TOTAL_ROW`، ثم يطبقه عبر `pivot_table_style_name` ويحفظ بصيغة `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# تعبئة البيانات المصدرية: صف الرأس + 9 صفوف بيانات (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

# إضافة جدول محوري مصدره A1:C10، مثبت عند E3، باسم "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# الخطوة 1: تسجيل نمط جدول محوري مخصص جديد والتقاط فهرسه
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]

# الخطوة 2: إضافة عنصر WholeTable وتطبيق حدود سوداء رفيعة على الجوانب الأربعة
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)

# الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر غامق
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، الذي يُستخدم للإعدادات المسبقة المضمنة)
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام FormatAll**

`PivotTable.format_all(Style)` هو اختصار يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات ورؤوس الصفوف والأعمدة والإجماليات. يتم تجاوز أي شيء تم تعيينه مسبقًا من خلال `pivot_table_style_type` أو `pivot_table_style_name`.

{{% alert color="primary" %}}

يتجاوز `format_all` كلًا من `pivot_table_style_type` و `pivot_table_style_name`. استخدمه فقط عندما يكون المظهر الموحد المستقل عن السمة مطلوبًا عبر الجدول المحوري بأكمله.

{{% /alert %}}

ينشئ المثال التالي `Style` بتعبئة صلبة صفراء وخط أزرق داكن عريض وحدود سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `format_all` ويحفظ بصيغة `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# السيناريو 4: تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام FormatAll
# واجهة برمجة التطبيقات المستخدمة: PivotTable.FormatAll(Style)
# تنسيق الهدف: .xlsx
# مرجع GitHub: راجع مستودع Aspose.Cells-for-.NET — أمثلة تنسيق الجدول المحوري

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# تعبئة البيانات المصدرية: صف الرأس (الصف 1) + 9 صفوف بيانات (الصفوف 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# إضافة جدول محوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# تعيين حقول الجدول المحوري: Fruit -> منطقة الصفوف، Year -> منطقة الأعمدة، Amount -> منطقة البيانات
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# إنشاء نمط سيتم فرضه على كل خلية من خلايا الجدول المحوري
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# تطبيق FormatAll: يفرض هذا النمط الفردي على كل خلية من خلايا الجدول المحوري،
# متجاوزًا أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقًا
pivot_table.format_all(style)

# حفظ المصنف بتنسيق .xlsx الحديث
workbook.save("output.xlsx")
```

## **أي واجهة برمجة تطبيقات للأنماط يجب أن أستخدم؟**

يعتمد اختيار واجهة برمجة التطبيقات للأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول أدناه كمرجع سريع.

| تنسيق الملف الهدف | واجهة برمجة التطبيقات للاستخدام | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `PivotTable.auto_format_type` | قيم من `aspose.cells.pivot.PivotTableAutoFormatType` (مثل `REPORT_1`–`REPORT_10`، و `CLASSIC`، و `TABLE_1`–`TABLE_10`). يتم تجاهلها عند الحفظ بتنسيقات حديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `PivotTable.pivot_table_style_type` | قيم من `aspose.cells.PivotTableStyleType` (سمات فاتحة/داكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | استخدم عندما لا تكون الإعدادات المسبقة المضمنة كافية. قم بالتكوين عبر `table_style_element.set_element_style(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.format_all(Style)` | اختصار يتجاوز كل إعداد نمط آخر عبر الجدول المحوري بأكمله. |

في حالة الشك، احفظ بصيغة `.xlsx` واستخدم `pivot_table_style_type` للسمات المضمنة، أو `pivot_table_style_name` للسمات المخصصة.

{{< app/cells/assistant language="python" >}}