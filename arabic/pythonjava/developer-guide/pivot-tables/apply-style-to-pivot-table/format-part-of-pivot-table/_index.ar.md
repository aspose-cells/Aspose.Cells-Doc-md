---
title: تنسيق جزء من جدول محوري
linktitle: تنسيق جزء من جدول محوري
description: قم بتنسيق جزء من جدول محوري في Aspose.Cells for Python via Java عن طريق تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea عبر PivotTable.format، حيث تُحفظ الأنماط في PivotTable.getPivotFormats() وتستمر عند تحديث جدول المحوري.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /ar/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
`PivotTable.formatAll` يطبق نمطًا واحدًا على جدول محوري كامل ويتم تغطيته في الصفحة الأساسية. لا يميز بين العناوين أو القيم أو إجماليات أو مناطق معينة من التقرير.  
في الواقع، عادةً ما يحتاج جزء فقط من جدول محوري إلى الإبراز. تشمل الأهداف الشائعة العناوين التي تنتمي إلى حقل صف واحد، خانات القيم التي ينتجها حقل واحد، صف الإجمالي العام، أو مستطيل عشوائي مثل الصفين الأولين من العناصر.  
تطبيق نمط مباشرةً على خلايا ورقة العمل الخاصة بجدول محوري ليس مكافئًا. Excel يخزن تنسيق الجدول المحوري كمناطق PivotArea دلالية بدلاً من سجلات نمط خلايا عادية. يبقى تنسيق منطقة Pivot مرتبطًا بمنطقة مثل عناوين الحقل أو قيم البيانات، ويُعاد حسابه عندما يُعاد حساب الجدول المحوري أو يُحدث أو يُوسع. أما النمط المكتوب مباشرةً إلى خلية، فهو يخص موقع تلك الخلية ولا يتم تتبعه من قبل نموذج الجدول المحوري.  
Aspose.Cells يوضح عائلة التحميل الزايد `PivotTable.format` بحيث تكون كلتا الطريقتين متاحتين:
- `format(PivotArea, Style)` يربط نمطًا بمنطقة دلالية تُنشأ باستخدام `PivotArea.select` أو `PivotArea.selectField`.
- `format(CellArea, Style)` يربط نمطًا بمستطيل ورقة عمل داخل جدول محوري.
- `format(int row, int column, Style)` يستهدف خلية واحدة.
- `formatAll(Style)` ينسق كامل جدول محوري.

## **تنسيق PivotArea**
تعد عملية العمل على المنطقة الدلالية هي النهج الموصى به عندما يجب أن يبقى التمييز مرتبطًا بحقل أو منطقة من التقرير.  
1. إنشاء `PivotArea` باستخدام `PivotArea(pivot_table)`. يصف الكائن منطقة دلالية تنتمي إلى ذلك الجدول المحوري المحدد.  
1. اختيار حقل بناءً على موضعه الصفري على محور محدد باستخدام `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DATA_AND_LABEL` يحدد كلًا من عناوين الحقل وبياناته.  
   - `PivotTableSelectionType.LABEL_ONLY` يحدد فقط عناوين الحقل.  
   - `PivotTableSelectionType.DATA_ONLY` يحدد فقط خلايا بيانات الحقل.  
1. اختيار حقل بالاسم باستخدام `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. عندما يُختار حقل صف بالاسم، تُحل المنطقة إلى خلايا القيم التي ينتجها عناصر ذلك الحقل.  
1. إنشاء `Style` باستخدام `workbook.createStyle()`، وتكوين الخط، ولون المقدمة، ونمط الخلفية الصلبة، وتمرير النمط إلى `PivotTable.format(area, style)`.  
1. كل استدعاء للتحميل الزايد `PivotArea` يضيف إدخالًا واحدًا من نوع `PivotTableFormat` إلى `PivotTable.getPivotFormats()`.  
1. تُرسم التنسيقات المرتبطة بالحقل عندما تُحسب بيانات المحوري. لذلك، استدعِ `PivotTable.calculateData()` بعد تطبيق التنسيقات حتى تظهر الأنماط.  
المثال التالي يبني جدول محوري صغير لمبيعات الفواكه، ينسق عناوين الصف `Fruit` باستخدام `PivotArea.select` و`PivotTableSelectionType.LABEL_ONLY`، ينسق خلايا القيم التي ينتجها نفس الحقل باستخدام `PivotArea.selectField`، ثم يعيد حساب جدول المحوري بحيث تُظهر كلا النمطين.

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
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
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
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **تنسيق CellArea لجدول محوري**
استخدم `PivotTable.format(CellArea, Style)` عندما تكون المنطقة المطلوبة مستطيل ورقة عمل عادي بدلاً من منطقة Pivot دلالية.  
يتم وصف `CellArea` بواسطة الخصائص `getStartRow()`, `getStartColumn()`, `getEndRow()`, و`getEndColumn()`. القيم هي إحداثيات ورقة عمل صفرية الأساس، وتحدد إحداثيات النهاية الصف والعمود الأخيرين المشمولين في المستطيل، لذا يغطي المجال الخلايا من الموقع البداية إلى الموقع النهاية شاملًا.  
على عكس تنسيق مرتبط بحقل، يتم تطبيق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء آخر لـ `PivotTable.calculateData()` لظهور النمط.  
قد يحتوي مستطيل `CellArea` على خلايا عناوين وخلايا قيم معًا. يصف القسم التالي كيف تمثل Aspose.Cells وExcel ذلك المستطيل داخليًا.  
المثال التالي ينسق المستطيل `E4:F5` من جدول المحوري بنمط مائل، أزرق فاتح، ويحفظ المصنف دون أي حساب إضافي.

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
    CellArea,
    PivotFieldType,
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
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **كيفية ربط PivotAreas وCellAreas**
Excel يخزن تنسيق الجدول المحوري كسجلات `pivotArea` بدلاً من سجلات نمط خلايا ورقة عمل عادية. يستخدم Aspose.Cells نفس النموذج، لذا يُترجم طلب التنسيق إلى مناطق Pivot عند تسجيله.  
العلاقة بين `CellArea` التي يزودها المستخدم ومناطق Pivot المخزنة داخليًا هي علاقة متعدد إلى متعدد في كلا الاتجاهين.  
- قد ينتج `CellArea` واحد عدة مناطق Pivot. إذا كان المستطيل يغطي كلًا من خلايا العناوين والقيم، يتم تفكيكه إلى قواعد عناوين وبيانات منفصلة، لأن نموذج Pivot يعالج تنسيق العناوين وتنسيق البيانات بشكل مستقل.  
- قد تُحل منطقة Pivot إلى عدة مثيلات `CellArea` منفصلة. يمكن لمنطقة دلالية مثل صف إجمالي عام، أو حقل لا تكون عناصره متجاورة، أن تغطي مستطيلات متعددة. لهذا السبب تُعيد `PivotArea.getCellAreas()` مجموعة بدلاً من مستطيل واحد.  
كل عملية تنسيق تُجرى عبر `PivotTable.format` تُسجل في `PivotTable.getPivotFormats()`. كل إدخال من نوع `PivotTableFormat` يُظهر `PivotArea` المرتبطة و`Style` المطبقة عليها. التحميل الزايد `PivotArea` يضيف إدخالًا واحدًا بالضبط لكل استدعاء، بينما `CellArea` التي تحتوي على مناطق دلالية مختلفة يمكن أن تضيف عدة إدخالات.  
للتمييز بين المناطق المخزنة، تُظهر كل `PivotArea` علمي `getOnlyLabel()` و`getOnlyData()`. المثال أدناه ينسق مستطيلًا واحدًا يغطي كلًا من العناوين والقيم، يفحص `PivotTable.getPivotFormats()`، ويطبع إحداثيات `CellArea` التي تُحل كل منطقة Pivot مخزنة إليها.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
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
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
نظرًا لأن التنسيقات تُخزن كمناطق Pivot بدلًا من أنماط خلايا عادية، فإنها تبقى بعد إعادة الحساب والتحديث. عندما يُحدث جدول المحوري باستخدام `PivotTable.refreshData()`، أو يُعاد حسابه بـ `PivotTable.calculateData()`، أو يُحفظ ثم يُعاد تحميله، تُعيد كل منطقة Pivot مخزنة حساب موقعها الحالي وتُطبق النمط مرة أخرى.
{{% /alert %}}

استخدم `PivotArea` التي تُبنى بـ `select` أو `selectField` عندما يجب أن يبقى التمييز مرتبطًا بحقل أو منطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عندما يكون تنسيق مستطيل ثابت في تخطيط جدول المحوري الحالي كافيًا. التحميل الزايد للخلية الواحدة `format(int row, int column, Style)` يستهدف خلية فردية. استخدم `formatAll`، الموضح في الصفحة الأصلية، عندما تريد إعادة تنسيق جدول محوري كامل دفعة واحدة.

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/python-java/apply-style-to-pivot-table/)
- [إضافة حقول صف وعمود إلى جدول محوري](/cells/ar/python-java/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في جدول محوري](/cells/ar/python-java/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}