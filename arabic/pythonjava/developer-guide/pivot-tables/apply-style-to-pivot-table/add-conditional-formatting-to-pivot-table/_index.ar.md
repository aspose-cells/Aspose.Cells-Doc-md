---
title: إضافة تنسيق شرطي إلى جدول محوري
linktitle: إضافة تنسيق شرطي إلى جدول محوري
description: إضافة تنسيق شرطي إلى جدول محوري في Aspose.Cells for Python via Java - ربط قاعدة بمنطقة البيانات باستخدام applyTo ونوع نطاق PivotConditionFormatScopeType، أو تعريف الهدف باستخدام addCellArea و getPivotAreas، ثم إرفاق القواعد والأنماط عبر getFormatConditions().addCondition.
keywords: Aspose.Cells for Python via Java, جدول محوري, التنسيق الشرطي, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /ar/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
الأنماط الموضحة في الصفحة الأم والصفحة الشقيقة ثابتة – يتم تلوين منطقة `PivotArea` أو `CellArea` مرة واحدة وتحتفظ بنمطها بغض النظر عن القيم. التنسيق الشرطي هو النظير القائم على القواعد – يسلط الضوء على كل مبلغ يزيد عن 200، أو يظلل الخمسين بالمئة الوسطى، أو يميز العناصر ذات الترتيب الأدنى – ويتبع التمييز القيم كلما تم إعادة حساب أو تحديث الجدول المحوري.  
في Aspose.Cells، يعيش التنسيق الشرطي للجدول المحوري في مجموعة `PivotTable.getConditionalFormats()` . كل إدخال هو `PivotConditionalFormat` يجيب على سؤالين بشكل مستقل:
- **أين يتم تطبيق القاعدة؟** يتم تعريف منطقة الهدف إما من خلال `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)`، الذي يعكس محدد النطاق في واجهة Excel، أو من خلال `PivotConditionalFormat.addCellArea(CellArea)` ومجموعة `PivotConditionalFormat.getPivotAreas()`، التي تسمي المنطقة صراحة.
- **ماذا تختبر القاعدة؟** يتم إضافة شرط أو أكثر إلى `PivotConditionalFormat.getFormatConditions()` باستخدام `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`، وتحتوي كل شرط على `Style` خاص به.

{{% alert color="primary" %}}
لا تستدعِ `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` أو `FormatConditionCollection.addArea(CellArea)` على كائن `PivotConditionalFormat.getFormatConditions()` الخاص بتنسيق شرطي للجدول المحوري. هذان التحميلان المزدوجان موروثان من واجهة برمجة تطبيقات التنسيق الشرطي العادية للورقة ولا يعملان للجداول المحورية – لن يتم تحويل منطقة الخلية إلى منطقة محورية، لذا يتم تجاهل الطلب بصمت. عرّف المنطقة دائمًا على `PivotConditionalFormat` نفسه (`applyTo`، `addCellArea`، أو `getPivotAreas()`) وأضف القاعدة باستخدام أحد `addCondition` overloads.
{{% /alert %}}

## **تطبيق قاعدة بنطاق (طريقة واجهة مستخدم Excel)**
الطريقة الأولى تموضع القاعدة كما تفعل واجهة Excel. تُسمّى خلية الجدول المحوري بإحداثيات ورقة عمل صفرية، ويخبر نطاق `PivotConditionFormatScopeType` Aspose.Cells إلى أي مدى يجب أن تصل القاعدة من تلك الخلية:
- `PivotConditionFormatScopeType.DATA` – جميع خلايا القيم التي ينتجها الجدول المحوري، بما فيها الإجماليات الكلية.
- `PivotConditionFormatScopeType.FIELD` – خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، مستثنية الإجماليات الكلية. يجب أن تكون الخلية خلية حقل مثل تسمية حقل صف؛ تمرير خلية قيمة يؤدي إلى استثناء.
- `PivotConditionFormatScopeType.SELECTION` – فقط خلايا القيم عند التقاطع التي تحددها الخلية، عادةً خلية قيمة واحدة.
المثال أدناه يبني جدولًا محوريًا لمبيعات الفواكه يكون زاويته العليا اليسرى عند E3، يربط تنسيقًا شرطيًا بالخلية F4 (الصف 3، العمود 5) بنطاق `DATA`، ويبرز كل مبلغ أكبر من 200 بخط أبيض عريض على خلفية حمراء. مع القيم Apple 220، Banana 330، Cherry 200، والإجمالي الكلي 750، تُلوّن القاعدة الخلايا F4 وF5 وF7 – المنطقة المحلولة هي كامل عمود البيانات F4:F7، وتُضاء فقط الخلايا التي يتجاوز مقدارها القاعدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

ربط نفس القاعدة بتسمية حقل الصف E4 (الصف 3، العمود 4) بنطاق `FIELD` يحل إلى F4:F6 بدلاً من ذلك – نفس عمود البيانات دون صف الإجمالي الكلي – لأن النطاق الآن يُصفّح حقل `Fruit` بدلًا من كامل مساحة القيم. النطاق `SELECTION` المربوط عند F4 يحل إلى F4 فقط.

## **تحديد المنطقة يدوياً**
الطريقة الثانية تتخطى أداة اختيار النطاق وتسمّي المنطقة صراحةً على `PivotConditionalFormat`.

### **مستطيل ورقة عمل باستخدام addCellArea()**
`addCellArea(CellArea)` يسجل المستطيل المقدم كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة عمل صفرية، والمنطقة هي بالضبط المستطيل المزوَّد – لا توسعة إلى عمود البيانات ولا منطق إجمالي. استخدمها عندما تكون الخلايا المثيرة للاهتمام مستطيلًا ثابتًا معروفًا في تخطيط الجدول المحوري الحالي.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **منطقة دلالية للجدول المحوري باستخدام getPivotAreas()**
مجموعة `getPivotAreas()` هي نموذج المنطقة الدلالية نفسه الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. أنشئ `PivotArea`، اختر حقلًا أو منطقة باستخدام `PivotArea.select(...)` أو `PivotArea.selectField(...)`، وأضفها عبر `getPivotAreas().addPivotArea(PivotArea)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذا يتبع التنسيق الشرطي الحقل عند تحديث الجدول المحوري وتحرك التخطيط. التحميل `getPivotAreas().add(PivotArea)` لا يزال يُجمع لكنه مُعلَّم بالقديمة – يُفضَّل استخدام `addPivotArea`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Rule - grey text for amounts below 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **أين تُخزن القواعد وكيفية بقائها بعد إعادة التحميل**
كل استدعاء `PivotTable.getConditionalFormats().add()` يضيف `PivotConditionalFormat` واحد إلى الجدول المحوري. تُحفظ الشروط وصيغها وأنماطها مع المصنف – إعادة فتح الملف في المثال أدناه تظهر القاعدة نفسها مع الأنواع والمشغلات والصيغ سليمة، وتُظهر `PivotConditionalFormat.getCellAreas()` نفس المناطق. تُحذف الإدخالات التي لم تتلقَ شرطًا عندما يُحفظ المصنف، بنفس الطريقة التي يتجاهل فيها Excel تنسيقًا شرطيًا لا يحتوي على قاعدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
jpype.shutdownJVM()
```

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/python-java/apply-style-to-pivot-table/)
- [تنسيق جزء من جدول محوري](/cells/ar/python-java/format-part-of-pivot-table/)
- [أعلى 10 إظهار أو تصفية في جدول محوري](/cells/ar/python-java/top-10-show-or-filter-in-pivot-table/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}