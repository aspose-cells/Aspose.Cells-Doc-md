---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python via Java
linktitle: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python via Java
description: تعرف على كيفية تطبيق الأنماط المدمجة والمخصصة على الجداول المحورية في Aspose.Cells for Python via Java، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، والأنماط المسماة الحديثة في Excel 2007+، وأنماط الجدول المحوري المخصصة، واختصار formatAll.
keywords: Aspose.Cells, Python via Java, نمط الجدول المحوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تطبيق كلٍّ من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) والأنماط الحديثة المسماة أو المخصصة للجدول المحوري (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). تعتمد واجهة برمجة التطبيقات التي يجب استدعاؤها على تنسيق الملف الذي يتم حفظ المصنف به، وليس على التنسيق الذي تم تحميله منه.
{{% /alert %}}

## **مقدمة**
يوفر Aspose.Cells واجهتي أنماط متوازيتين للجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ المصنف المحمّل من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة تُطبَّق واجهة الأنماط الحديثة بدلاً من واجهة الأنماط القديمة.
- `pivotTable.setPivotTableStyleType(int)` يختار أحد الأنماط المسماة المدمجة (السمات الفاتحة والداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- `pivotTable.setPivotTableStyleName(String)` يختار نمطًا مخصصًا تحدده بنفسك من خلال `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. تُستخدم الأنماط المخصصة كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.
بالإضافة إلى ذلك، فإن `pivotTable.formatAll(Style)` هو اختصار يطبّق كائن `Style` واحدًا على كل خلية في الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أيٍّ من واجهتي اسم النمط المذكورتين أعلاه. يكون ذلك مفيدًا عندما يكون المظهر الموحد مطلوبًا بصرف النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مُعد مسبقًا قديم لـ XLS**
تقبل طريقة `setAutoFormatType` في الجدول المحوري قيمة من تعداد `com.aspose.cells.pivot.PivotTableAutoFormatType`. القيم المتاحة هي `REPORT_1` إلى `REPORT_10`، و`CLASSIC`، و`TABLE_1` إلى `TABLE_10`.
يُحمِّل المثال التالي مصنفًا جديدًا، ويملأ بيانات العينة الخاصة بالفاكهة/السنة/المبلغ، ويضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.REPORT_5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}
**لماذا لا توجد حقول أعمدة؟** صُمِّمت التنسيقات التلقائية من سلسلة التقارير (`Report1` إلى `Report10`، و`Table1` إلى `Table10`) في الإصدار الكلاسيكي من Excel لأجل **جداول محورية أحادية البعد** التي تحتوي على حقول صفوف وقيم فقط، إذ لا تتضمن تنسيقًا مدمجًا لرؤوس حقول الأعمدة. إذا كان الجدول المحوري يحتاج إلى حقول أعمدة، فاستخدم بدلاً من ذلك الإعدادات المسبقة الحديثة `PivotTableStyleType` من [السيناريو 2](#apply-a-modern-named-preset-pivot-table-style)، المصممة لتخطيط ثنائي الأبعاد يستخدمه Excel الحديث.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# السيناريو 1: تطبيق تنسيق تلقائي preset لـ XLS القديم
# API قيد الاستخدام: PivotTable.AutoFormatType
# تنسيق الملف الهدف: .xls (قديم)
# للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-cells/Aspose.Cells-for-.NET
# إنشاء مصنف جديد
workbook = Workbook()
# الحصول على ورقة العمل الأولى
sheet = workbook.getWorksheets().get(0)
# تعبئة بيانات المصدر بصف الرأس (Fruit, Year, Amount)
# و9 صفوف بيانات تغطي grape وblueberry وkiwi وcherry عبر 2020 و2021
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
# إضافة جدول محوري في خلية الوجهة E3، باسم ، باستخدام نطاق المصدر A1:C10
pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4)
# تعيين الحقول: Fruit -> Rows، Amount -> Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# تطبيق التنسيق التلقائي preset القديم لـ XLS وهو "Report5"
# ملاحظة: هذه الخاصية ذات معنى فقط عند الحفظ بصيغة .xls.
# عند الحفظ بصيغة .xlsx/.xlsm/.xlsb، يتجاهل Excel AutoFormatType
# ويستخدم أيًا مما يحدده PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5)
# حفظ المصنف بصيغة .xls القديمة
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **تطبيق نمط جدول محوري مُعد مسبقًا حديث باسم**
يحدد `pivotTable.setPivotTableStyleType(int)` أحد أنماط الجداول المحورية المسماة والمدمجة التي أدخلها Excel 2007. ويتيح التعداد `PivotTableStyleType` ثلاث عائلات من السمات: العائلة الفاتحة من `PIVOT_TABLE_STYLE_LIGHT1` إلى `PIVOT_TABLE_STYLE_LIGHT28`، والعائلة المتوسطة من `PIVOT_TABLE_STYLE_MEDIUM1` إلى `PIVOT_TABLE_STYLE_MEDIUM28`، والعائلة الداكنة من `PIVOT_TABLE_STYLE_DARK1` إلى `PIVOT_TABLE_STYLE_DARK_28`. كما يحدد `None` و`Custom`. وتُعد الأعضاء ذات الأرقام الأعلى في كل عائلة الأنماط التي تمت إضافتها في Excel 2017.
هذه الإعدادات المسبقة للقراءة فقط. وفي اللحظة التي تحتاج فيها إلى تغيير الألوان أو الحدود أو الخطوط بما يتجاوز ما يوفره أي إعداد مسبق، عليك تعريف نمط جدول محوري مخصص بدلاً من ذلك، كما هو موضح في [السيناريو 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**لماذا الإعدادات المسبقة الحديثة وليس التنسيقات التلقائية لسلسلة التقارير؟** Values `Report1` through `Report10` and `Table1` through `Table10` of `PivotTableAutoFormatType` predate pivot column fields, so they carry no styling for column-field headers and Excel renders those headers unstyled. The `PivotTableStyleType` presets were designed for the two-dimensional layout modern Excel uses and style row-field and column-field headers alike.
{{% /alert %}}

يعيد هذا السيناريو استخدام مجموعة بيانات Fruit/Year/Amount المستخدمة في السيناريو 1، ويضيف `Year` إلى منطقة الأعمدة إلى جانب حقل الصف `Fruit` باستخدام `PivotFieldType.COLUMN`، ويطبق الإعداد المسبق `PIVOT_TABLE_STYLE_DARK1` ذو النمط الداكن باستخدام `pivotTable.setPivotTableStyleType`، ثم يحفظ النتيجة بصيغة `.xlsx` — الصيغة التي يكون فيها `PivotTableStyleType` ذا معنى.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 9 data rows of Fruit / Year / Amount
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
# Add a pivot table at E3, sourced from A1:C10
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1)
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **تعريف نمط جدول محوري مخصص وتطبيقه**
لا يمكن تعديل الإعدادات المسبقة المدمجة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب عليك تعريف نمط محوري مخصص. تتكون سير العمل من ثلاث خطوات:
1. أضف نمطًا مخصصًا إلى مجموعة `TableStyles` الخاصة بالمصنف عبر `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. يُرجع ذلك فهرس النمط المُنشأ حديثًا.
2. قم بتكوين النمط بإضافة عناصر (مثل `WHOLE_TABLE` أو `GRAND_TOTAL_ROW`) من خلال `tableStyle.getTableStyleElements().add(TableStyleElementType)`، ثم خصّص نمط `Style` لكل عنصر عبر `tableStyleElement.setElementStyle(Style)`.
3. طبّق النمط المخصص على الجدول المحوري باستدعاء `pivotTable.setPivotTableStyleName(String)` مع اسم النمط. لا تستخدم `setPivotTableStyleType` هنا، لأن تلك الطريقة تختار الإعدادات المسبقة المدمجة.

{{% alert color="primary" %}}
لا يمكن استخدام `setPivotTableStyleName` و`setPivotTableStyleType` بالتبادل. استخدم `setPivotTableStyleType` للإعدادات المسبقة المدمجة، واستخدم `setPivotTableStyleName` للأنماط المخصصة التي قمت بتعريفها عبر `addPivotTableStyle`. تعيين كلاهما لا يضر، ولكن يُعرض فقط النمط المطابق للمصدر المقصود.
تتضمن قيم `TableStyleElementType` المتاحة: `WHOLE_TABLE`، و`FIRST_ROW`، و`LAST_ROW`، و`FIRST_COLUMN`، و`LAST_COLUMN`، و`GRAND_TOTAL_ROW`، و`GRAND_TOTAL_COLUMN`، و`PAGE_FIELD_LABELS`، و`PAGE_FIELD_VALUES`.
يعرّف المثال التالي نمطًا محوريًا مخصصًا بحدود سوداء رفيعة على `WHOLE_TABLE` وخط أحمر عريض على `GRAND_TOTAL_ROW`، ثم يطبّقه عبر `setPivotTableStyleName` ويحفظه بصيغة `.xlsx`.
{{% /alert %}}

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from asposecells.api import Color
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# تعبئة البيانات المصدرية: صف العناوين + 9 صفوف بيانات (A1:C10)
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
# إضافة جدول محوري مصدره A1:C10، مثبت عند E3، باسم
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
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
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
wholeTableElement.setElementStyle(wholeTableStyle)
# الخطوة 3: إضافة عنصر GrandTotalRow وتطبيق خط أحمر عريض
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.getRed())
grandTotalElement.setElementStyle(grandTotalStyle)
# الخطوة 4: تطبيق النمط المخصص بالاسم (وليس عن طريق PivotTableStyleType، الذي يُستخدم للإعدادات المسبقة المدمجة)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام formatAll**
يُعد `pivotTable.formatAll(Style)` اختصارًا يطبّق كائن `Style` واحدًا على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات ورؤوس الصفوف والأعمدة والإجماليات. يتم تجاوز أي شيء تم تعيينه سابقًا من خلال `setPivotTableStyleType` أو `setPivotTableStyleName`.

{{% alert color="primary" %}}
يتجاوز `formatAll` كلًا من `setPivotTableStyleType` و`setPivotTableStyleName`. استخدمه فقط عندما يكون المظهر الموحد المستقل عن السمة مطلوبًا عبر كامل الجدول المحوري.
يُنشئ المثال التالي كائن `Style` بتعبئة صلبة باللون الأصفر وخط عريض باللون الأزرق الداكن وحدود سوداء رفيعة على جميع الجوانب، ثم يطبّقه باستخدام `formatAll` ويحفظه بصيغة `.xlsx`.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# السيناريو 4: تطبيق نمط واحد على كل خلية من خلايا الجدول المحوري باستخدام formatAll
# API المستخدم: PivotTable.formatAll(Style)
# تنسيق الهدف: .xlsx
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
# إضافة جدول محوري: نطاق المصدر A1:C10، خلية الوجهة E3، الاسم
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# تعيين حقول الجدول المحوري: Fruit -> منطقة الصفوف، Year -> منطقة الأعمدة، Amount -> منطقة البيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# بناء كائن Style الذي سيتم فرضه على كل خلية من خلايا الجدول المحوري
style = workbook.createStyle()
style.setForegroundColor(Color.fromArgb(70, 130, 180))
style.setPattern(BackgroundType.SOLID)
style.getFont().setBold(True)
style.getFont().setColor(Color.getDarkBlue())
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
# تطبيق formatAll: يفرض هذا النمط الواحد على كل خلية من خلايا الجدول المحوري،
# متجاوزاً أي PivotTableStyleType / PivotTableStyleName تم تعيينه مسبقاً
pivotTable.formatAll(style)
# حفظ المصنف بتنسيق .xlsx الحديث
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **أي واجهة برمجة تطبيقات للأنماط يجب أن أستخدم؟**
يعتمد اختيار واجهة برمجة التطبيقات للأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول التالي كمرجع سريع.
| تنسيق الملف الهدف | واجهة برمجة التطبيقات التي يجب استخدامها | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `pivotTable.setAutoFormatType(int)` | قيم من `com.aspose.cells.pivot.PivotTableAutoFormatType` (مثل `REPORT_1`–`REPORT_10`، و`CLASSIC`، و`TABLE_1`–`TABLE_10`). يتم تجاهلها عند الحفظ بالتنسيقات الحديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مدمج) | `pivotTable.setPivotTableStyleType(int)` | قيم من `com.aspose.cells.PivotTableStyleType` (السمات الفاتحة والداكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | استخدم عندما لا تكفي الإعدادات المسبقة المدمجة. قم بالتكوين عبر `tableStyleElement.setElementStyle(Style)`. |
| أي تنسيق (تجاوز موحد) | `pivotTable.formatAll(Style)` | اختصار يتجاوز كل إعداد نمط آخر عبر كامل الجدول المحوري. |
في حالة الشك، احفظ بصيغة `.xlsx` واستخدم `setPivotTableStyleType` للسمات المدمجة، أو `setPivotTableStyleName` للسمات المخصصة.

{{< app/cells/assistant language="python" >}}