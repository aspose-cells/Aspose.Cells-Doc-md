---
title: تطبيق الأنماط على الجداول المحورية
linktitle: تطبيق الأنماط على الجداول المحورية
description: تعلم كيفية تطبيق الأنماط المضمنة والمخصصة على الجداول المحورية في Aspose.Cells for Python via Java، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، وأنماط Excel 2007+ الحديثة المسماة، وأنماط الجداول المحورية المخصصة، واختصار FormatAll.
keywords: Aspose.Cells Python via Java نمط الجدول المحوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تطبيق كل من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) والأنماط الحديثة المسماة أو المخصصة للجداول المحورية (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يتم حفظ المصنف به، وليس على التنسيق الذي تم تحميله منه.
{{% /alert %}}

## **مقدمة**

يُعرِّض Aspose.Cells واجهتي API متوازيتين للأنماط للجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ المصنف المحمَّل من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة تُطبَّق واجهة API الحديثة للأنماط بدلاً من واجهة API القديمة.

للحصول على مخرجات بتنسيق `.xls` القديم، استخدم الطريقة `pivotTable.setAutoFormatType(int)` مع تعداد `com.aspose.cells.pivot.PivotTableAutoFormatType`. تتوافق واجهة API هذه مع منتقي التنسيق التلقائي الذي كان Excel الكلاسيكي يوفره للجداول المحورية.

بالنسبة لمخرجات `.xlsx` و`.xlsm` و`.xlsb` الحديثة، تتوفر نوعان من واجهة API للأنماط:

- `pivotTable.setPivotTableStyleType(int)` يحدد أحد الأنماط المسماة المضمنة (السمات الفاتحة والداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- `pivotTable.setPivotTableStyleName(String)` يحدد نمطًا مخصصًا تُعرِّفه بنفسك من خلال `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. الأنماط المخصصة مطلوبة كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.

بالإضافة إلى ذلك، تُعد `pivotTable.formatAll(Style)` اختصارًا يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، متجاوزًا أيًا مما يتم تعيينه من خلال أي من واجهتي API لاسم النمط المذكورتين أعلاه. يكون هذا مفيدًا عند الحاجة إلى مظهر موحد بغض النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مُعد مسبقًا بتنسيق XLS القديم**

تقبل الطريقة `setAutoFormatType` في الجدول المحوري قيمة من تعداد `com.aspose.cells.pivot.PivotTableAutoFormatType`. القيم المتاحة هي `REPORT_1` إلى `REPORT_10`، و`CLASSIC`، و`TABLE_1` إلى `TABLE_10`.

{{% alert color="primary" %}}
لا يتم الالتزام بـ `setAutoFormatType` إلا عند حفظ المصنف بصيغة `.xls`. عندما يتم حفظ المصنف نفسه بصيغة `.xlsx` أو `.xlsm` أو `.xlsb`، يتجاهل Excel هذا الإعداد ويعود إلى إعدادات `setPivotTableStyleType` و`setPivotTableStyleName`.
{{% /alert %}}

يُحمِّل المثال التالي مصنفًا جديدًا، ويُعبِّئ بيانات العينة للفاكهة/السنة/المبلغ، ويُضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.REPORT_5`، ويحفظ النتيجة بصيغة `.xls`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# السيناريو 1: تطبيق تنسيق تلقائي محدد مسبقًا لـ XLS القديم
# واجهة برمجة التطبيقات المستخدمة: PivotTable.AutoFormatType
# تنسيق الملف المستهدف: .xls (قديم)
# للحصول على أمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-cells/Aspose.Cells-for-.NET

# إنشاء مصنف جديد
workbook = Workbook()

# الحصول على ورقة العمل الأولى
sheet = workbook.getWorksheets().get(0)

# تعبئة البيانات المصدرية بصف الرأس (فاكهة، سنة، مبلغ)
# و9 صفوف بيانات تغطي العنب، التوت الأزرق، الكيوي، الكرز عبر عامي 2020 و2021
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")

sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)

sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)

sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)

sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)

sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)

sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)

sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)

sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)

sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)

# إضافة جدول محوري في خلية الوجهة E3، باسم "Pivot1"، باستخدام نطاق المصدر A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# تعيين الحقول: الفاكهة -> الصفوف، السنة -> الأعمدة، المبلغ -> البيانات
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# تطبيق التنسيق التلقائي المحدد مسبقًا لـ XLS القديم "Report5"
# ملاحظة: هذه الخاصية ذات معنى فقط عند الحفظ بتنسيق .xls.
# عند الحفظ بتنسيق .xlsx/.xlsm/.xlsb، يتجاهل Excel خاصية AutoFormatType
# ويستخدم ما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# حفظ المصنف بتنسيق .xls القديم
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **تطبيق نمط جدول محوري حديث مسمى مُعد مسبقًا**

تقبل الطريقة `setPivotTableStyleType` في الجدول المحوري قيمة من تعداد `com.aspose.cells.PivotTableStyleType`. يغطي التعداد السمات الفاتحة من `PIVOT_TABLE_STYLE_LIGHT_1` إلى `PIVOT_TABLE_STYLE_LIGHT_28` والسمات الداكنة من `PIVOT_TABLE_STYLE_DARK_1` إلى `PIVOT_TABLE_STYLE_DARK_28`. يمكن الوصول إلى الأنماط المضافة في Excel 2017 (الموجة الثانية من السمات الفاتحة والداكنة) من خلال نفس التعداد.

هذه هي واجهة API الموصى بها لأي تنسيق ملف حديث. على عكس التنسيق التلقائي القديم، يتم عرض النمط المحدد هنا بأمانة بواسطة Excel ويبقى سليمًا عبر عمليات الحفظ والتحميل المتكررة من خلال أدوات Office الأخرى.

يستخدم المثال التالي نفس بيانات الفاكهة/السنة/المبلغ، وينشئ جدولًا محوريًا مطابقًا، ويطبق `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1`، ويحفظ المصنف بصيغة `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# السيناريو 2: تطبيق نمط مسمى حديث من Excel 2007+ باستخدام PivotTableStyleType.
# صيغة الملف الهدف: .xlsx. يعد PivotTableStyleType enum جزءًا من مساحة أسماء Aspose.Cells
# (وليس في Aspose.Cells.Pivot) — ولهذا لا نحتاج إلى أي استخدام إضافي له.
# مرجع GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# صف الرأس: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 صفوف بيانات من الفاكهة / السنة / المبلغ
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)

# إضافة جدول محوري في E3 باسم "Pivot1"، مصدره من A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# تعيين حقول الجدول المحوري: الفاكهة -> منطقة الصف، السنة -> منطقة العمود، المبلغ -> منطقة البيانات
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# تطبيق نمط جدول محوري مسمى حديث من Excel 2007+.
# PivotTableStyleType هي واجهة برمجة التطبيقات الصحيحة لملفات .xlsx / .xlsm / .xlsb؛ AutoFormatType
# يتم تجاهلها بواسطة Excel لتلك الصيغ. ينتمي PivotTableStyleDark1 إلى عائلة
# النسق الداكن (PivotTableStyleDark1..PivotTableStyleDark28)، ويعرض نفس التعداد أيضًا
# نُسق Excel 2017 الفاتحة/الداكنة الأحدث (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# الحفظ بصيغة .xlsx الحديثة — هذه هي الصيغة التي يكون لها PivotTableStyleType معنى.
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **تعريف وتطبيق نمط جدول محوري مخصص**

لا يمكن تعديل الإعدادات المسبقة المضمنة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب عليك تعريف نمط محوري مخصص. تتكون سير العمل من ثلاث خطوات:

1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. يُرجع هذا فهرس النمط الذي تم إنشاؤه حديثًا.
2. قم بتكوين النمط بإضافة عناصر (مثل `WHOLE_TABLE` أو `GRAND_TOTAL_ROW`) من خلال `tableStyle.getTableStyleElements().add(TableStyleElementType)`، ثم عيّن `Style` لكل عنصر عبر `tableStyleElement.setElementStyle(Style)`.
3. طبّق النمط المخصص على الجدول المحوري عن طريق استدعاء `pivotTable.setPivotTableStyleName(String)` باسم النمط. لا تستخدم `setPivotTableStyleType` هنا، حيث تحدد هذه الطريقة الإعدادات المسبقة المضمنة.

{{% alert color="primary" %}}
لا يمكن التبادل بين `setPivotTableStyleName` و`setPivotTableStyleType`. استخدم `setPivotTableStyleType` للإعدادات المسبقة المضمنة، و`setPivotTableStyleName` للأنماط المخصصة التي قمت بتعريفها من خلال `addPivotTableStyle`. تعيين كليهما ليس ضارًا، ولكن لا يتم عرض إلا الإعداد الذي يتطابق مع المصدر المقصود.
{{% /alert %}}

تتضمن قيم `TableStyleElementType` المتاحة `WHOLE_TABLE`، و`FIRST_ROW`، و`LAST_ROW`، و`FIRST_COLUMN`، و`LAST_COLUMN`، و`GRAND_TOTAL_ROW`، و`GRAND_TOTAL_COLUMN`، و`PAGE_FIELD_LABELS`، و`PAGE_FIELD_VALUES`.

يُعرِّف المثال التالي نمطًا محوريًا مخصصًا بحد أسود رفيع على `WHOLE_TABLE` وخط أحمر غامق على `GRAND_TOTAL_ROW`، ثم يطبقه عبر `setPivotTableStyleName` ويحفظ بصيغة `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# تعبئة البيانات المصدرية: صف الرأس + 9 صفوف بيانات (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

# إضافة جدول محوري مصدره A1:C10، مثبت عند E3، باسم "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# الخطوة 1: تسجيل نمط جدول محوري مخصص جديد والتقاط فهرسه
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# الخطوة 2: إضافة عنصر WholeTable وتطبيق حدود سوداء رفيعة على الجوانب الأربعة
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر عريض
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# الخطوة 4: تطبيق النمط المخصص بالاسم (وليس بواسطة PivotTableStyleType، وهو للإعدادات المسبقة المدمجة)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام FormatAll**

`pivotTable.formatAll(Style)` هي اختصار يطبق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات، ورؤوس الصفوف والأعمدة، والإجماليات. يتم تجاوز أي شيء تم تعيينه مسبقًا من خلال `setPivotTableStyleType` أو `setPivotTableStyleName`.

{{% alert color="primary" %}}
يتجاوز `formatAll` كلًا من `setPivotTableStyleType` و`setPivotTableStyleName`. استخدمها فقط عند الحاجة إلى مظهر موحد ومستقل عن السمة عبر الجدول المحوري بأكمله.
{{% /alert %}}

يُنشئ المثال التالي كائن `Style` بتعبئة صلبة صفراء، وخط أزرق داكن غامق، وحدود سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `formatAll` ويحفظ بصيغة `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# السيناريو 4: تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام FormatAll
# واجهة برمجة التطبيقات المستخدمة: PivotTable.FormatAll(Style)
# الصيغة المستهدفة: .xlsx
# مرجع GitHub: راجع مستودع Aspose.Cells-for-.NET — أمثلة تنسيق الجدول المحوري

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# تعبئة بيانات المصدر: صف الرأس (الصف 1) + 9 صفوف بيانات (الصفوف 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)

# إضافة جدول محوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# تعيين حقول الجدول المحوري: Fruit -> منطقة الصف، Year -> منطقة العمود، Amount -> منطقة البيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# بناء نمط Style سيتم فرضه على كل خلية من خلايا الجدول المحوري
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# تطبيق FormatAll: يفرض هذا النمط الواحد على كل خلية من خلايا الجدول المحوري،
# متجاوزًا أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقًا
pivotTable.formatAll(style)

# حفظ المصنف بالصيغة الحديثة .xlsx
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **أي واجهة API للأنماط يجب أن أستخدم؟**

يعتمد اختيار واجهة API للأنماط على تنسيق الملف الذي تحفظ به. استخدم الجدول أدناه كمرجع سريع.

| تنسيق الملف الهدف | واجهة API للاستخدام | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `pivotTable.setAutoFormatType(int)` | القيم من `com.aspose.cells.pivot.PivotTableAutoFormatType` (مثل `REPORT_1`–`REPORT_10`، و`CLASSIC`، و`TABLE_1`–`TABLE_10`). يتم تجاهله عند الحفظ بتنسيقات حديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `pivotTable.setPivotTableStyleType(int)` | القيم من `com.aspose.cells.PivotTableStyleType` (السمات الفاتحة/الداكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | استخدم عندما لا تكون الإعدادات المسبقة المضمنة كافية. قم بالتكوين عبر `tableStyleElement.setElementStyle(Style)`. |
| أي تنسيق (تجاوز موحد) | `pivotTable.formatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر عبر الجدول المحوري بأكمله. |

في حالة الشك، احفظ بصيغة `.xlsx` واستخدم `setPivotTableStyleType` للسمات المضمنة، أو `setPivotTableStyleName` للسمات المخصصة.

{{< app/cells/assistant language="python" >}}
