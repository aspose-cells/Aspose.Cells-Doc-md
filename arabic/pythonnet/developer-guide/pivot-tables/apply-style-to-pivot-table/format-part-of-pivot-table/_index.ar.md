---
title: تنسيق جزء من جدول محوري
linktitle: تنسيق جزء من جدول محوري
description: تنسيق جزء من جدول محوري في Aspose.Cells for Python via .NET عن طريق تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea عبر PivotTable.format، مع تخزين التنسيقات في PivotTable.pivot_formats وحفظها عند تحديث جدول محوري.
keywords: Aspose.Cells for Python via .NET, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /ar/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
`PivotTable.format_all` يطبق نمطًا واحدًا على كامل جدول محوري ويُغطى في الصفحة الأصلية. لا يميز بين التسميات، القيم، الإجماليات أو المناطق المحددة من التقرير.  
في الواقع، عادةً ما يحتاج جزء فقط من جدول محوري إلى إبراز. تشمل الأهداف الشائعة التسميات الخاصة بحقل صف واحد، خلايا القيم التي ينتجها حقل واحد، صف الإجمالي الكلي، أو مستطيل عشوائي مثل الصفين الأولين من العناصر.  
تطبيق نمط مباشرةً على خلايا ورقة عمل جدول محوري ليس مكافئًا. تقوم Excel بتخزين تنسيق جدول محوري كمناطق `PivotArea` دلالية بدلاً من سجلات نمط الخلية العادية. يبقى تنسيق منطقة الـ pivot مرتبطًا بمنطقة مثل تسميات الحقل أو قيم البيانات، ويتم إعادة حلّه عندما يُعاد حساب جدول محوري أو يُحدّث أو يُوسّع. أما النمط المكتوب مباشرةً في الخلية، فيخصّ ذلك الموقع ولا يتعقّب نموذج الـ pivot.  
تُظهر Aspose.Cells عائلة التحميل الزائد `PivotTable.format` بالكامل بحيث يكون كلا النوعين من التنسيقات متاحين:
- `format(PivotArea, Style)` يربط نمطًا بمنطقة دلالية تُبنى باستخدام `PivotArea.select` أو `PivotArea.select_field`.
- `format(CellArea, Style)` يربط نمطًا بمستطيل في ورقة العمل داخل جدول محوري.
- `format(int row, int column, Style)` يستهدف خلية واحدة.
- `format_all(Style)` ينسق كامل جدول محوري.

## **تنسيق PivotArea**
طريقة المنطقة الدلالية هي النهج الموصى به عندما يجب أن يبقى التمييز مرتبطًا بحقل أو بمنطقة من التقرير.  
1. أنشئ كائن `PivotArea` باستخدام `PivotArea(pivot_table)`. يصف هذا الكائن منطقة دلالية تنتمي إلى جدول محوري محدد.  
2. اختر حقلًا بحسب موضعه الصفري على محور معين باستخدام `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)`.  
   - `PivotTableSelectionType.DATA_AND_LABEL` يختار كلًا من التسميات والبيانات الخاصة بالحقل.  
   - `PivotTableSelectionType.LABEL_ONLY` يختار تسميات الحقل فقط.  
   - `PivotTableSelectionType.DATA_ONLY` يختار خلايا بيانات الحقل فقط.  
3. اختر حقلًا بالاسم باستخدام `PivotArea.select_field(PivotFieldType axis_type, string field_name)`. عندما يُختار حقل صف بالاسم، تتحول المنطقة إلى خلايا القيم التي ينتجها عناصر ذلك الحقل.  
4. أنشئ كائن `Style` عبر `Workbook.create_style()`، واضبط الخط، ولون المقدمة، والنمط الخلفي الصلب، ثم مرّر النمط إلى `PivotTable.format(area, style)`.  
5. كل استدعاء للتحميل الزائد للـ `PivotArea` يضيف إدخالًا واحدًا من نوع `PivotTableFormat` إلى `PivotTable.pivot_formats`.  
6. يتم رسم التنسيقات المرتبطة بالحقل عند حساب بيانات الـ pivot. لذلك، استدعِ `PivotTable.calculate_data()` بعد تطبيق التنسيقات حتى تصبح الأنماط مرئية.  
المثال التالي يُنشئ جدول محوري صغير لمبيعات الفواكه، ينسق عناوين الصفوف `Fruit` باستخدام `PivotArea.select` و`PivotTableSelectionType.LABEL_ONLY`، ينسق خلايا القيم التي ينتجها نفس الحقل باستخدام `PivotArea.select_field`، ثم يُعيد حساب جدول المحوري بحيث تُظهر كلا النمطين.

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **تنسيق CellArea لجدول المحوري**
استخدم `PivotTable.format(CellArea, Style)` عندما تكون المنطقة ذات الاهتمام مستطيلًا عاديًا في ورقة عمل وليس منطقة محورية دلالية.  
يُوصف `CellArea` بخصائص `start_row` و`start_column` و`end_row` و`end_column`. القيم هي إحداثيات ورقة عمل صفرية الأساس، وتحدّد الإحداثيات النهائية الصف والعمود الأخيرين المشمولين بالمستطيل، لذا يغطي المجال الخلايا من الموضع الابتدائي حتى الموضع النهائي شاملًا.  
على عكس تنسيق مرتبط بحقل، يُطبق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء آخر لـ `calculate_data()` لإظهار النمط.  
قد يحتوي مستطيل `CellArea` على خلايا تسميات وخلايا قيم معًا. يصف القسم التالي كيفية تمثيل Aspose.Cells وExcel لهذا المستطيل داخليًا.  
المثال التالي ينسق المستطيل `E4:F5` من جدول المحوري بنمط مائل، أزرق فاتح، ويحفظ المصنف دون أي إعادة حساب إضافية.

```python
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **كيفية ربط PivotAreas و CellAreas**
تخزن Excel تنسيق جدول محوري كسجلات `pivotArea` بدلاً من سجلات نمط الخلية العادية. يستخدم Aspose.Cells النموذج نفسه، لذا يتم ترجمة طلب التنسيق إلى مناطق pivot عند تسجيله.  
العلاقة بين `CellArea` التي يزودها المستخدم ومناطق pivot المخزنة داخليًا هي علاقة كثيرة إلى كثيرة في كلا الاتجاهين.  
- قد تُنتج `CellArea` واحدة عدة مناطق pivot. إذا كان المستطيل يضم كلًا من خلايا التسميات وخلايا القيم، فإنه يُفكك إلى قواعد تسميات وبيانات منفصلة، لأن نموذج الـ pivot يعالج تنسيق العناوين وتنفيذ البيانات بشكل مستقل.  
- قد تُحلّ منطقة pivot إلى عدة كائنات `CellArea` منفصلة. يمكن لمنطقة دلالية مثل صف إجمالي كلي، أو حقل لا تتواصل عناصره، أن يغطي مستطيلات متعددة. لهذا السبب تُعيد `PivotArea.get_cell_areas()` مجموعة بدلًا من مستطيل واحد.  
كل عملية تنسيق تُجرى عبر `PivotTable.format` تُسجل في `PivotTable.pivot_formats`. كل إدخال من نوع `PivotTableFormat` يُظهر الـ `PivotArea` المرتبط والنمط `Style` المطبق عليه. يضيف التحميل الزائد للـ `PivotArea` إدخالًا واحدًا بالضبط لكل استدعاء، بينما يمكن أن يضيف `CellArea` يحتوي على مناطق دلالية مختلفة عدة إدخالات.  
للتفريق بين المناطق المخزنة، يكشف كل `PivotArea` عن علمي `only_label` و`only_data`. المثال أدناه ينسق مستطيلًا واحدًا يغطي كلًا من التسميات والقيم، يفتش `PivotTable.pivot_formats`، ويطبع إحداثيات `CellArea` التي تُحلّ كل منطقة pivot مخزنة إليها.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
نظرًا لأن التنسيقات تُخزن كمناطق pivot بدلاً من نمط خلايا عادي، فإنها تبقى بعد إعادة الحساب وتحديث الجدول. عندما يتم تحديث جدول محوري باستخدام `PivotTable.refresh_data`، أو إعادة حسابه بـ `calculate_data`، أو حفظه وإعادة تحميله، فإن كل منطقة pivot مخزنة تُعيد حلّ موقعها الحالي وتُطبق نمطها مرةً أخرى.
{{% /alert %}}

استخدم `PivotArea` التي تم بناؤها باستخدام `select` أو `select_field` عندما يجب أن يبقى التمييز مرتبطًا بحقل أو بمنطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عندما يكون تنسيق مستطيل ثابت في تخطيط جدول محوري الحالي كافيًا. التحميل الزائد `format(int row, int column, Style)` يهدف إلى خلية فردية. استخدم `format_all`، المغطى في الصفحة الأصلية، عندما يرغب المستخدم في إعادة تنسيق كامل جدول محوري مرةً واحدة.

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/python-net/apply-style-to-pivot-table/)
- [إضافة حقول صف وعمود إلى جدول محوري](/cells/ar/python-net/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في جدول محوري](/cells/ar/python-net/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}