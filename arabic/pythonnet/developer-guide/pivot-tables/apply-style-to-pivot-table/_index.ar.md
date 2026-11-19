---
title: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python via .NET
linktitle: تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python via .NET
description: تعرف على كيفية تطبيق الأنماط المضمنة والمخصصة على الجداول المحورية في Aspose.Cells for Python via .NET، بما في ذلك التنسيقات التلقائية القديمة لملفات XLS، والأنماط المسماة الحديثة في Excel 2007+، وأنماط الجدول المحوري المخصصة، واختصار _format_all.
keywords: Aspose.Cells Python via .NET نمط الجدول المحوري, PivotTableStyleType, AutoFormatType, FormatAll, نمط مخصص, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ar/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تطبيق كل من التنسيقات التلقائية القديمة للجداول المحورية (المخصصة لملفات `.xls`) والأنماط المسماة الحديثة أو المخصصة للجدول المحوري (المخصصة لملفات `.xlsx` و`.xlsm` و`.xlsb`). يعتمد استدعاء واجهة برمجة التطبيقات (API) على تنسيق الملف الذي يتم حفظ المصنف به، وليس على التنسيق الذي تم تحميله منه.
{{% /alert %}}

## **مقدمة**
يوفر Aspose.Cells واجهتي API متوازيتين للأنماط الخاصة بالجداول المحورية. يعتمد الاختيار بينهما على تنسيق الملف الذي تحفظ المصنف به، وليس على التنسيق الذي تقرأه منه. يمكن إعادة حفظ مصنف تم تحميله من ملف `.xls` بصيغة `.xlsx`، وفي هذه الحالة يتم تطبيق واجهة API الحديثة للأنماط بدلاً من القديمة.
- يحدد `PivotTable.pivot_table_style_type` أحد الأنماط المسماة المضمنة (السمات الفاتحة والداكنة، بما في ذلك الأنماط المضافة في Excel 2017). هذه الإعدادات المسبقة للقراءة فقط.
- يحدد `PivotTable.pivot_table_style_name` نمطًا مخصصًا تحدده بنفسك من خلال `workbook.worksheets.table_styles.add_pivot_table_style(...)`. الأنماط المخصصة مطلوبة كلما أردت تعديل الألوان أو الحدود أو الخطوط بما يتجاوز ما تقدمه الإعدادات المسبقة.
بالإضافة إلى ذلك، فإن `PivotTable.format_all(Style)` هو اختصار يطبق كائن `Style` واحد على كل خلية من خلايا الجدول المحوري، متجاوزًا أي شيء يتم تعيينه من خلال أي من واجهتي API لاسم النمط أعلاه. يكون هذا مفيدًا عندما يكون المظهر الموحد مطلوبًا بغض النظر عن السمة الأساسية.

## **تطبيق تنسيق تلقائي مسبق لملفات XLS القديمة**
يقبل `PivotTable.auto_format_type` قيمة من تعداد `aspose.cells.pivot.PivotTableAutoFormatType`. القيم المتاحة هي `REPORT_1` إلى `REPORT_10`، و`CLASSIC`، و`TABLE_1` إلى `TABLE_10`.
يحمل المثال التالي مصنفًا جديدًا، ويملأ بيانات العينة الخاصة بـ Fruit/Year/Amount، ويضيف جدولًا محوريًا، ويطبق `PivotTableAutoFormatType.REPORT5`، ويحفظ النتيجة بصيغة `.xls`.

{{% alert color="primary" %}}
**لماذا لا توجد حقول أعمدة؟** تم تصميم التنسيقات التلقائية من السلسلة Report (Report1 إلى Report10، وTable1 إلى Table10) في Excel الكلاسيكي لـ **الجداول المحورية أحادية البعد** التي تحتوي على حقول صفوف وقيم فقط - فهي لا تحتوي على تنسيق مضمن لرؤوس حقول الأعمدة. إذا كان الجدول المحوري الخاص بك يحتاج إلى حقول أعمدة، فاستخدم إعدادات `PivotTableStyleType` المسبقة الحديثة من [السيناريو 2](#apply-a-modern-named-preset-pivot-table-style) بدلاً من ذلك، وهي مصممة لتخطيط ثنائي الأبعاد يستخدمه Excel الحديث.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotTableAutoFormatType
# Scenario 1: Apply a legacy XLS preset autoformat
# API in use: PivotTable.AutoFormatType
# Target file format: .xls (legacy)
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Create a new workbook
workbook = ac.Workbook()
# Get the first worksheet
sheet = workbook.worksheets[0]
# Populate the source data with header row (Fruit, Year, Amount)
# and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.cells.get(0, 0).put_value("Fruit")
sheet.cells.get(0, 1).put_value("Year")
sheet.cells.get(0, 2).put_value("Amount")
sheet.cells.get(1, 0).put_value("grape")
sheet.cells.get(1, 1).put_value(2020)
sheet.cells.get(1, 2).put_value(50)
sheet.cells.get(2, 0).put_value("blueberry")
sheet.cells.get(2, 1).put_value(2020)
sheet.cells.get(2, 2).put_value(30)
sheet.cells.get(3, 0).put_value("kiwi")
sheet.cells.get(3, 1).put_value(2020)
sheet.cells.get(3, 2).put_value(25)
sheet.cells.get(4, 0).put_value("cherry")
sheet.cells.get(4, 1).put_value(2020)
sheet.cells.get(4, 2).put_value(40)
sheet.cells.get(5, 0).put_value("grape")
sheet.cells.get(5, 1).put_value(2021)
sheet.cells.get(5, 2).put_value(60)
sheet.cells.get(6, 0).put_value("blueberry")
sheet.cells.get(6, 1).put_value(2021)
sheet.cells.get(6, 2).put_value(35)
sheet.cells.get(7, 0).put_value("kiwi")
sheet.cells.get(7, 1).put_value(2021)
sheet.cells.get(7, 2).put_value(28)
sheet.cells.get(8, 0).put_value("cherry")
sheet.cells.get(8, 1).put_value(2021)
sheet.cells.get(8, 2).put_value(45)
sheet.cells.get(9, 0).put_value("grape")
sheet.cells.get(9, 1).put_value(2020)
sheet.cells.get(9, 2).put_value(45)
# Add a pivot table at destination cell E3, using source range A1:C10
pivot_table = sheet.pivot_tables.add("A1:C10", 2, 4)
# Assign fields: Fruit -> Rows, Amount -> Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Apply the legacy XLS preset autoformat "Report5"
# Note: This property is only meaningful when saving as .xls.
# When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
# and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivot_table.auto_format_type = PivotTableAutoFormatType.REPORT5
# Save the workbook in legacy .xls format
workbook.save("output.xls")
```

## **تطبيق نمط جدول محوري حديث مسمى ومحدد مسبقًا**
`pivot_table.pivot_table_style_type` يحدد واحدًا من أنماط التسمية المدمجة التي أدخلتها Excel 2007 للجداول المحورية. يوفر تعداد `PivotTableStyleType` ثلاث عائلات من الأنماط: العائلة الفاتحة من `PIVOT_TABLE_STYLE_LIGHT1` إلى `PIVOT_TABLE_STYLE_LIGHT28`، وعائلة المتوسطة من `PIVOT_TABLE_STYLE_MEDIUM1` إلى `PIVOT_TABLE_STYLE_MEDIUM28`، وعائلة الداكنة من `PIVOT_TABLE_STYLE_DARK1` إلى `PIVOT_TABLE_STYLE_DARK28`. كما يحدد `None` و`Custom`. الأعضاء ذو الأرقام الأعلى في كل عائلة هي الأنماط التي أُضيفت في Excel 2017.
هذه الأنماط الجاهزة للقراءة فقط. بمجرد أن تحتاج إلى تغيير الألوان أو الحدود أو الخطوط بما يتجاوز ما توفره الأنماط الجاهزة، فعليك تعريف نمط جدول محوري مخصص بدلاً من ذلك، كما هو موضح في [السيناريو 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**لماذا الأنماط الحديثة الجاهزة بدلاً من التنسيقات التلقائية لسلسلة التقارير؟** قيم `Report1` إلى `Report10` وقيم `Table1` إلى `Table10` في `PivotTableAutoFormatType` تسبق حقول أعمدة الجداول المحورية، لذلك لا تتضمن أي تنسيقات لفواصل حقول الأعمدة، ويعرض Excel تلك الفواصل دون تنسيق. صُممت الأنماط الجاهزة لـ `PivotTableStyleType` للتخطيط ثنائي الأبعاد الذي يستخدمه Excel الحديث، وتنسق فواصل حقول الصفوف وحقول الأعمدة على حد سواء.
{{% /alert %}}

يعيد هذا السيناريو استخدام مجموعة بيانات Fruit/Year/Amount من السيناريو 1، ويضيف `Year` إلى منطقة الأعمدة إلى جانب حقل الصف `Fruit` عبر `PivotFieldType.COLUMN`، ويطبق النمط الجاهز ذي السمة الداكنة `PIVOT_TABLE_STYLE_DARK1` باستخدام `pivot_table.pivot_table_style_type`، ويحفظ النتيجة بصيغة `.xlsx` — الصيغة التي يكون فيها `PivotTableStyleType` ذا معنى.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotTableStyleType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. PivotTableStyleType lives in aspose.cells.pivot,
# so it is imported explicitly alongside PivotFieldType.
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Header row: Fruit / Year / Amount
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(180)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(120)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(170)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(210)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(190)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(130)
# Add a pivot table at E3, sourced from A1:C10
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PIVOT_TABLE_STYLE_DARK1 belongs to the dark-theme
# family (PIVOT_TABLE_STYLE_DARK1..PIVOT_TABLE_STYLE_DARK28), and the same enum also exposes
# the newer Excel 2017 themes (PIVOT_TABLE_STYLE_LIGHT1..LIGHT28 / DARK1..DARK28).
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_DARK1
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
```

## **تعريف وتطبيق نمط جدول محوري مخصص**
لا يمكن تعديل الإعدادات المسبقة المضمنة. كلما احتجت إلى تجاوز الألوان أو الحدود أو الخطوط، يجب عليك تعريف نمط جدول محوري مخصص. تتكون سير العمل من ثلاث خطوات:
1. أضف نمطًا مخصصًا إلى مجموعة `table_styles` الخاصة بالمصنف عبر `workbook.worksheets.table_styles.add_pivot_table_style(name)`. يُرجع هذا فهرس النمط الذي تم إنشاؤه حديثًا.
2. قم بتهيئة النمط بإضافة عناصر (مثل `WHOLE_TABLE` أو `GRAND_TOTAL_ROW`) من خلال `table_style.table_style_elements.add(TableStyleElementType)`، ثم خصص كائن `Style` لكل عنصر عبر `table_style_element.set_element_style(Style)`.
3. طبق النمط المخصص على الجدول المحوري عن طريق تعيين `PivotTable.pivot_table_style_name` إلى اسم النمط. لا تستخدم `pivot_table_style_type` هنا، لأن تلك الخاصية تختار الإعدادات المسبقة المضمنة.

{{% alert color="primary" %}}
`pivot_table_style_name` و`pivot_table_style_type` ليسا قابلين للتبديل. استخدم `pivot_table_style_type` للإعدادات المسبقة المضمنة، و`pivot_table_style_name` للأنماط المخصصة التي قمت بتعريفها من خلال `add_pivot_table_style`. تعيين كلاهما غير ضار، ولكن فقط الذي يطابق المصدر المطلوب يتم عرضه.
تتضمن قيم `TableStyleElementType` المتاحة `WHOLE_TABLE` و`FIRST_ROW` و`LAST_ROW` و`FIRST_COLUMN` و`LAST_COLUMN` و`GRAND_TOTAL_ROW` و`GRAND_TOTAL_COLUMN` و`PAGE_FIELD_LABELS` و`PAGE_FIELD_VALUES`.
يحدد المثال التالي نمط جدول محوري مخصصًا بحد أسود رفيع على `WHOLE_TABLE` وخط أحمر غامق على `GRAND_TOTAL_ROW`، ثم يطبقه عبر `pivot_table_style_name` ويحفظ بصيغة `.xlsx`.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.tables import TableStyleElementType
from aspose.pydrawing import Color
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Populate source data: header row + 9 data rows (A1:C10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(500)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(600)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(700)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(800)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(900)
# Add pivot table sourced from A1:C10, anchored at E3
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Step 1: register a new custom pivot table style and capture its index
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]
# Step 2: add a WholeTable element and apply thin black borders on all four sides
whole_table_element_index = table_style.table_style_elements.add(TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).color = Color.black
whole_table_element.set_element_style(whole_table_style)
# Step 3: add a GrandTotalRow element and apply bold red font
grand_total_element_index = table_style.table_style_elements.add(TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = Color.red
grand_total_element.set_element_style(grand_total_style)
# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **تطبيق نمط واحد على كل خلية في الجدول المحوري باستخدام format_all**
`PivotTable.format_all(Style)` هو اختصار يطبق كائن `Style` واحد على كل خلية من خلايا الجدول المحوري، بما في ذلك منطقة البيانات ورؤوس الصفوف والأعمدة والإجماليات. يتم تجاوز أي شيء تم تعيينه سابقًا من خلال `pivot_table_style_type` أو `pivot_table_style_name`.

{{% alert color="primary" %}}
`format_all` يتجاوز كلاً من `pivot_table_style_type` و`pivot_table_style_name`. استخدمه فقط عندما يكون المظهر الموحد المستقل عن السمة مطلوبًا عبر الجدول المحوري بأكمله.
ينشئ المثال التالي `Style` بتعبئة صفراء صلبة وخط أزرق داكن غامق وحواف سوداء رفيعة على جميع الجوانب، ثم يطبقه باستخدام `format_all` ويحفظ بصيغة `.xlsx`.
{{% /alert %}}

```python
from aspose.pydrawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# Scenario 4: Apply a single Style to every pivot table cell using format_all
# API in use: PivotTable.format_all(Style)
# Target format: .xlsx
# GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(5000)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(3000)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(4000)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(2000)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(6000)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(3500)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(4500)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(2500)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(5500)
# Add pivot table: source range A1:C10, destination cell E3
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Build a Style that will be forced onto every cell of the pivot table
style = workbook.create_style()
style.foreground_color = Color.yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.dark_blue
style.borders.get(BorderType.TOP_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.TOP_BORDER).color = Color.black
style.borders.get(BorderType.BOTTOM_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.BOTTOM_BORDER).color = Color.black
style.borders.get(BorderType.LEFT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.LEFT_BORDER).color = Color.black
style.borders.get(BorderType.RIGHT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.RIGHT_BORDER).color = Color.black
# Apply format_all: forces this single style onto every cell of the pivot table,
# overriding any PivotTableStyleType / PivotTableStyleName previously set
pivot_table.format_all(style)
# Save the workbook in the modern .xlsx format
workbook.save("output.xlsx")
```

## **أي واجهة API للأنماط يجب أن أستخدم؟**
يعتمد اختيار واجهة API للأنماط على تنسيق الملف الذي تحفظ إليه. استخدم الجدول التالي كمرجع سريع.
| تنسيق الملف الهدف | واجهة API التي يجب استخدامها | ملاحظات |
|---|---|---|
| `.xls` (قديم) | `PivotTable.auto_format_type` | القيم من `aspose.cells.pivot.PivotTableAutoFormatType` (مثل `REPORT_1`–`REPORT_10`، و`CLASSIC`، و`TABLE_1`–`TABLE_10`). يتم تجاهلها عند الحفظ بتنسيقات حديثة. |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مضمن) | `PivotTable.pivot_table_style_type` | القيم من `aspose.cells.PivotTableStyleType` (السمات الفاتحة والداكنة، بما في ذلك إضافات Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (حديث، نمط مخصص) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | استخدم عندما لا تكون الإعدادات المسبقة المضمنة كافية. قم بالتهيئة عبر `table_style_element.set_element_style(...)`. |
| أي تنسيق (تجاوز موحد) | `PivotTable.format_all(Style)` | اختصار يتجاوز كل إعداد نط آخر عبر الجدول المحوري بأكمله. |
في حالة الشك، احفظ بصيغة `.xlsx` واستخدم `pivot_table_style_type` للسمات المضمنة، أو `pivot_table_style_name` للسمات المخصصة.

{{< app/cells/assistant language="python-net" >}}