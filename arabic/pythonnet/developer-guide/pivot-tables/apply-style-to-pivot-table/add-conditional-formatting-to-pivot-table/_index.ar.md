---
title: إضافة التنسيق الشرطي إلى جدول محوري
linktitle: إضافة التنسيق الشرطي إلى جدول محوري
description: إضافة التنسيق الشرطي إلى جدول محوري في Aspose.Cells for Python via .NET - ربط قاعدة بمنطقة البيانات باستخدام apply_to ونوع نطاق PivotConditionFormatScopeType، أو تعريف الهدف باستخدام add_cell_area و pivot_areas، ثم إرفاق القواعد والأنماط عبر format_conditions.add_condition.
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, جدول محوري, التنسيق الشرطي, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /ar/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
الأنماط الموضحة في الصفحة الأصلية والصفحة الشقيقة هي أنماط ثابتة – يتم تلوين منطقة `PivotArea` أو `CellArea` مرة واحدة وتبقى على نمطها بغض النظر عن القيم. التنسيق الشرطي هو النظير القائم على القواعد – إبراز كل مبلغ يزيد عن 200، تظليل الخمسين بالمئة الوسطى، أو وضع علامة على العناصر ذات الترتيب الأدنى – ويتبع التمييز القيم كلما تم إعادة حساب أو تحديث الجدول المحوري.  
في Aspose.Cells، يعيش التنسيق الشرطي للجدول المحوري في مجموعة `pivot_table.conditional_formats`. كل إدخال هو `PivotConditionalFormat` يجيب على سؤالين بشكل مستقل:
- **أين تُطبق القاعدة؟** يتم تعريف منطقة الهدف إما عبر `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)` التي تعكس أداة اختيار النطاق في واجهة مستخدم Excel، أو عبر `add_cell_area(cell_area: CellArea)` ومجموعة `pivot_areas` التي تُحدد المنطقة صراحةً.
- **ما الذي تختبره القاعدة؟** يتم إضافة شرط أو أكثر إلى `format_conditions` باستخدام `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)`، ولكل شرط `style` الخاص به.

{{% alert color="primary" %}}
لا تقم باستدعاء `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` أو `format_conditions.add_area(cell_area: CellArea)` على كائن `format_conditions` لتنسيق شرطي للجدول المحوري. هذان التحميلان المزدوجان ورثان من واجهة برمجة تطبيقات التنسيق الشرطي للورقة العادية ولا يعملان للجداول المحورية – فإن منطقة الخلية لا تُحوَّل أبداً إلى منطقة جدولية، لذا يتم تجاهل الطلب بصمت. يجب دائماً تعريف المنطقة على `pivot_conditional_format` نفسه (`apply_to`، `add_cell_area`، أو `pivot_areas`) وإضافة القاعدة باستخدام أحد تحميلات `add_condition`.
{{% /alert %}}

## **تطبيق قاعدة بنطاق (طريقة واجهة Excel)**
الطريقة الأولى تضع القاعدة كما تفعل واجهة Excel. يتم تسمية خلية من الجدول المحوري بإحداثيات ورقة العمل التي تبدأ من الصفر، ويخبر نطاق `PivotConditionFormatScopeType` Aspose.Cells إلى أي مدى يجب أن تمتد القاعدة من تلك الخلية:
- `PivotConditionFormatScopeType.DATA` – جميع خلايا القيم التي ينتجها الجدول المحوري، بما في ذلك الإجماليات العامة.
- `PivotConditionFormatScopeType.FIELD` – خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، مستثنية الإجماليات العامة. يجب أن تكون الخلية خلية حقل مثل تسمية حقل صف؛ تمرير خلية قيمة سيؤدي إلى استثناء.
- `PivotConditionFormatScopeType.SELECTION` – فقط خلايا القيم في التقاطع التي تحددها الخلية، عادةً خلية قيمة واحدة.  
يبني المثال أدناه جدولاً محوريًا لمبيعات الفواكه يكون زاويته العليا اليسرى عند E3، يربط تنسيقًا شرطيًا بخلية F4 (الصف 3، العمود 5) باستخدام نطاق `PivotConditionFormatScopeType.DATA`، ويُبرز كل مبلغ أكبر من 200 بخط عريض أبيض على خلفية حمراء. مع القيم Apple 220، Banana 330، Cherry 200، والإجمالي العام 750، تقوم القاعدة بتلوين F4 وF5 وF7 – المنطقة المُحددة هي كامل عمود البيانات F4:F7، وتضيء فقط الخلايا التي تتجاوز قيمتها القاعدة.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

ربط نفس القاعدة بملصق حقل الصف E4 (الصف 3، العمود 4) باستخدام نطاق `PivotConditionFormatScopeType.FIELD` يحدد المنطقة إلى F4:F6 بدلاً من ذلك – نفس عمود البيانات بدون صف الإجمالي العام – لأن النطاق الآن يصف حقل `Fruit` بدلاً من منطقة القيم بالكامل. نطاق `PivotConditionFormatScopeType.SELECTION` المرتبط بخلية F4 يحدد إلى F4 فقط.

## **تعريف المنطقة يدويًا**
الطريقة الثانية تتجاوز اختيار النطاق وتحدد المنطقة صراحةً على `PivotConditionalFormat`.

### **مستطيل ورقة عمل باستخدام add_cell_area**
`add_cell_area(cell_area: CellArea)` يسجل المستطيل المعطى كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة العمل التي تبدأ من الصفر، وتكون المنطقة تمامًا المستطيل المزوَّد – بدون توسيع إلى عمود البيانات ولا أي منطق للإجمالي العام. استخدمه عندما تكون الخلايا المثيرة للاهتمام مستطيلًا ثابتًا معروفًا في تخطيط الجدول المحوري الحالي.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
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
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **منطقة جدولية دلالية باستخدام pivot_areas**
`pivot_areas` هو نفس نموذج المنطقة الدلالية الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. قم بإنشاء `PivotArea`، اختر حقلًا أو منطقة باستخدام `select` أو `select_field`، وأضفه باستخدام `pivot_areas.add_pivot_area(pivot_area)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذا يتبع التنسيق الشرطي الحقل عند تحديث الجدول المحوري وتغيّر التخطيط. تحميل `pivot_areas.add(pivot_area)` لا يزال يُترجم لكنه مُعلَّم كقديم – يفضَّل استخدام `add_pivot_area`.

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
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Rule - grey text for amounts below 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **أين تُخزن القواعد وكيفية بقاءها بعد إعادة التحميل**
كل استدعاء `pivot_table.conditional_formats.add()` يضيف `PivotConditionalFormat` واحد إلى الجدول المحوري. تُحفظ الشروط وصيغها وأنماطها مع المصنف – إعادة فتح الملف في المثال أدناه تُظهر القاعدة نفسها مع أنواعها ومشغليها وصيغها سليمة، وتُظهر `get_cell_areas()` نفس المناطق. يتم حذف الإدخالات التي لم تتلقَ شرطًا عند حفظ المصنف، كما يتخلص Excel من تنسيق شرطي لا يحتوي على قاعدة.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/python-net/apply-style-to-pivot-table/)
- [تنسيق جزء من جدول محوري](/cells/ar/python-net/format-part-of-pivot-table/)
- [أبرز 10 عرض أو تصفية في جدول محوري](/cells/ar/python-net/top-10-show-or-filter-in-pivot-table/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}