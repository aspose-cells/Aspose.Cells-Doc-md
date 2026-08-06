---
title: تعديل تخطيط حقل الصفحة في الجدول المحوري
linktitle: تعديل تخطيط حقل الصفحة في الجدول المحوري
description: تعلم كيفية التحكم في تخطيط منطقة حقل الصفحة في الجدول المحوري باستخدام Aspose.Cells for Python عبر .NET، بما في ذلك تعيين ترتيب العرض، وعدد الالتفاف، وترتيب حقول الصفحة في الجزء العلوي من الجدول المحوري
keywords: Aspose.Cells، مكتبة Python عبر .NET، جدول بيانات، جدول محوري، حقل صفحة، ترتيب حقل الصفحة، عدد التفاف حقل الصفحة، نقل حقل الصفحة
type: docs
weight: 191
url: /ar/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
هذه المقالة هي تتمة لموضوع **إضافة حقل صفحة في الجدول المحوري**. توضح كيفية التحكم في تخطيط منطقة حقل الصفحة — شريط عناصر تحكم التصفية في الجزء العلوي من الجدول المحوري — بما في ذلك ترتيب العرض، وعدد الالتفاف، وإعادة ترتيب الحقول.
{{% /alert %}}
## **مقدمة**
يعرض الجدول المحوري في Microsoft Excel **منطقة حقل صفحة** مخصصة تقع فوق جسم الصفوف/الأعمدة/البيانات في الجدول. يتم عرض هذه المنطقة كشريط من عناصر تحكم التصفية المنسدلة (واحد لكل حقل صفحة) وهو ما ينقر عليه المستخدمون النهائيون لتقسيم الجدول المحوري حسب معايير مثل السنة أو المنطقة. يقوم Aspose.Cells for Python عبر .NET بنمذجة هذه المنطقة من خلال مجموعة `pivot_table.page_fields` ويعرض ثلاث خصائص تتحكم في كيفية عرض الشريط بصريًا:
- `pivot_table.page_field_order` (قيمة من النوع `PrintOrderType`) يحدد ما إذا كانت حقول الصفحة الإضافية موضوعة *بجانب* الحقول الموجودة أو *أسفلها*.
- `pivot_table.page_field_wrap_count` يحدد عدد حقول الصفحة الموضوعة لكل صف أو عمود قبل الالتفاف.
- `pivot_table.page_fields.move(curr_index, dest_index)` يعيد ترتيب حقول الصفحة دون تغيير وضع الترتيب.
تستعرض هذه المقالة ثلاثة أمثلة برمجية توضح كل عملية من هذه العمليات على مجموعة بيانات مشتركة، حتى تتمكن من مقارنة التخطيطات الناتجة جنبًا إلى جنب.
## **بيانات المصدر**
تحمّل جميع الأمثلة الثلاثة أدناه صفوف بيانات المبيعات الثمانية هذه في ورقة عمل باسم `PivotData`. تحتوي البيانات على مرشحين لحقول الصفحة (`Year`، `Region`)، ومرشحًا واحدًا لحقل الصف (`Fruit`)، ومقياسًا واحدًا (`Amount`)، مما يجعل شريط حقل الصفحة جديرًا بالتفحص.
يتم تعبئة جميع الصفوف الثمانية في كل مثال برمجي، بنفس الترتيب، لذلك لا تختلف بيانات المصدر أبدًا بين السيناريوهات — فقط خصائص تخطيط حقل الصفحة هي التي تختلف.
## **المثال 1: أفقي ثم عمودي**
في السيناريو الأول، نكوّن حقلي الصفحة (`Year`، `Region`) ليظهروا **جنبًا إلى جنب في صف واحد** في الجزء العلوي من الجدول المحوري. نخصص `Fruit` لمحور الصف، ونضع `Year` أولاً و`Region` ثانيًا على محور الصفحة (يحدد ترتيب استدعاءات `add_field_to_area` الفهرس الابتدائي)، ونضيف `Amount` (Sum) كحقل بيانات، ثم نعين `page_field_order` إلى `PrintOrderType.OverThenDown` مع `page_field_wrap_count = 2`. مع `OverThenDown` وعدد التفاف 2، يتم عرض حقلي الصفحة أفقيًا جنبًا إلى جنب في صف واحد في الجزء العلوي من الجدول المحوري، بحيث يشغل الشريط صفًا واحدًا بعرض اثنين.
```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# رؤوس الأعمدة (الصف 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# الصف 1: تفاح، 2022، الشمال، 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# الصف 2: تفاح، 2023، الشمال، 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# الصف 3: موز، 2022، الجنوب، 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# الصف 4: موز، 2023، الجنوب، 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# الصف 5: كرز، 2022، الشرق، 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# الصف 6: كرز، 2023، الشرق، 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# الصف 7: عنب، 2022، الغرب، 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# الصف 8: عنب، 2023، الغرب، 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# إضافة ورقة تقرير الجدول المحوري
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# إنشاء جدول محوري مصدره PivotData!A1:D9 موضوع في A1 على PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# إضافة الحقول
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # الفاكهة
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # السنة
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # المنطقة
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # المبلغ
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# تكوين تخطيط منطقة حقل الصفحة: ضع حقول الصفحة أفقياً أولاً، مع الالتفاف بعد كل 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# تحديث وحساب
pivot_table.calculate_data()

# حفظ
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```
## **المثال 2: عمودي ثم أفقي**
في هذا المثال نضع `Fruit` على محور الصف، و`Year` و`Region` على محور الصفحة (مع `Year` أولاً)، و`Amount` (Sum) كحقل بيانات — تمامًا كما في المثال 1. ثم نعين `page_field_order` إلى `PrintOrderType.DownThenOver` و`page_field_wrap_count` إلى `2`. مع `DownThenOver` وعدد التفاف 2، يتم تكديس حقلي الصفحة عموديًا — `Year` في الأعلى، `Region` مباشرة أدناه — مكونًا عمودًا واحدًا في الجزء العلوي من الجدول المحوري. لذلك يشغل الشريط صفين بعرض واحد، على عكس المثال 1.
```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```
## **المثال 3: نقل حقل صفحة**
في السيناريو الثالث، نحتفظ بمجموعة البيانات وتخصيص الحقول هذا، ونضع تخطيطًا محايدًا (`OverThenDown` مع عدد التفاف `2`)، ثم نوضح عملية `page_fields.move`. ينقل استدعاء `move(0, 1)` حقل الصفحة عند الفهرس 0 (`Year`) إلى الموضع 1، وينتقل حقل الصفحة الذي كان في الموضع 1 (`Region`) إلى الموضع 0. بعد هذا الاستدعاء، يكون `Region` هو حقل الصفحة الأول و`Year` هو الثاني. لم يتغير وضع الالتفاف والترتيب، لذلك لا يزال يتم عرض الشريط أفقيًا جنبًا إلى جنب — فقط تم تبديل ترتيب القائمتين المنسدلتين.
```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```
## **مقالات ذات صلة**
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/python-net/add-page-field-in-pivot-table/) — الصفحة الأصلية التي تقدم كيفية إضافة حقول الصفحة إلى الجدول المحوري.
- [حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/python-net/row-and-column-fields/) — يغطي تخصيص الحقول لمحوري الصفوف والأعمدة، مما يكمل العمل على محور الصفحة الموضح هنا.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/python-net/manage-value-fields/) — يوضح كيفية تكوين منطقة البيانات (القيم)، بما في ذلك تجميع `Sum` المستخدم في هذه المقالة.
- [تحديث الجدول المحوري](/cells/ar/python-net/refresh-pivot-table/) — يشرح `refresh_data` و`calculate_data`، المطلوب استخدامهما بعد إعادة ترتيب حقول الصفحة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/python-net/apply-style-to-pivot-table/) — يوضح كيفية تنسيق الجدول المحوري الذي تم عرضه بعد وضع شريط حقل الصفحة.
{{< app/cells/assistant language="python-net" >}}