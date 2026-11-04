---
title: تنسيق جزء من جدول محوري
linktitle: تنسيق جزء من جدول محوري
description: تنسيق جزء من جدول محوري في Aspose.Cells for Java عن طريق تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea عبر PivotTable.format، مع حفظ التنسيقات في PivotTable.getPivotFormats والحفاظ عليها عندما يتم تحديث جدول المحوري.
keywords: Aspose.Cells for Java, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /ar/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
`PivotTable.formatAll` يطبّق نمطًا واحدًا على جدول محوري بالكامل وقد تم تغطيته في الصفحة الأصلية. لا يميّز بين الملصقات، القيم، الإجماليات، أو المناطق الخاصة بالتقرير.  
في الممارسة العملية، عادةً ما يحتاج جزء فقط من جدول محوري إلى التمييز. تشمل الأهداف الشائعة الملصقات التابعة لحقل صف واحد، خلايا القيم التي ينتجها حقل معين، صف الإجمالي الكلي، أو مستطيل عشوائي مثل أول صفّين من العناصر.  
تطبيق نمط مباشرةً على خلايا ورقة عمل خاصة بجدول محوري ليس مكافئًا. Excel يخزن تنسيق جدول محوري كمناطق `PivotArea` دلالية بدلاً من سجلات نمط خلايا عادية. يظل تنسيق منطقة الـ pivot مرتبطًا بمنطقة مثل ملصقات الحقل أو قيم البيانات، ويُعاد حلّها عندما يُعاد حساب جدول محوري أو يُحدّث أو يُوسّع. من ناحية أخرى، النمط المكتوب مباشرةً إلى خلية يخص موقع الخلية ولا يتتبعه نموذج الـ pivot.  
Aspose.Cells يوفّر عائلة التحميل الزائد `PivotTable.format` الكاملة بحيث تكون كلتا طريقتي التنسيق متاحتين:
- `format(PivotArea, Style)` يربط نمطًا بمنطقة دلالية تُبنى باستخدام `PivotArea.select` أو `PivotArea.selectField`.
- `format(CellArea, Style)` يربط نمطًا بمستطيل ورقة عمل داخل جدول محوري.
- `format(int row, int column, Style)` يستهدف خلية واحدة.
- `formatAll(Style)` ينسق جدول محوري بأكمله.

## **تنسيق Pivot Area**
إن طريقة العمل للمنطقة الدلالية هي النهج الموصى به عندما يجب أن يظل التمييز مرتبطًا بحقل أو بمنطقة في التقرير.
1. أنشئ كائنًا من النوع `PivotArea` باستخدام `new PivotArea(pivotTable)`. يصف الكائن منطقة دلالية تنتمي إلى ذلك الجدول المحوري المحدد.
2. حدّد حقلًا وفقًا لموضعه الصفري على محور معين باستخدام `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` يختار كلًا من الملصقات والبيانات الخاصة بالحقل.
   - `PivotTableSelectionType.LABEL_ONLY` يختار ملصقات الحقل فقط.
   - `PivotTableSelectionType.DATA_ONLY` يختار خلايا بيانات الحقل فقط.
3. حدّد حقلًا بالاسم باستخدام `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. عندما يُحدّد حقل صف بالاسم، تُحَلّ المنطقة إلى خلايا القيم التي ينتجها عناصر ذلك الحقل.
4. أنشئ كائنًا من النوع `Style` باستخدام `Workbook.createStyle()`، واضبط الخط، لون الخلفية، ونمط خلفية صلبة، ثم مرّر النمط إلى `PivotTable.format(area, style)`.
5. كل استدعاء لـ `PivotArea` يضيف إدخالًا واحدًا من النوع `PivotTableFormat` إلى `PivotTable.getPivotFormats()`.
6. تُطبق التنسيقات المرتبطة بالحقل عندما تُحسب بيانات الـ pivot. لذلك، استدعِ `PivotTable.calculateData()` بعد تطبيق التنسيقات حتى تصبح الأنماط مرئية.  
المثال التالي يبني جدول محوري صغير لمبيعات الفواكه، ينسق ملصقات صف `Fruit` باستخدام `PivotArea.select` و`PivotTableSelectionType.LABEL_ONLY`، ينسق خلايا القيم الناتجة عن نفس حقل الصف باستخدام `PivotArea.selectField`، ثم يعيد حساب جدول المحوري بحيث يتم طباعة كلا النمطين.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **تنسيق Cell Area من جدول Pivot**
استخدم `PivotTable.format(CellArea, Style)` عندما تكون المنطقة المستهدفة مستطيلًا عاديًا في ورقة عمل بدلاً من منطقة محورية دلالية.  
يُوصف `CellArea` بواسطة الخصائص `getStartRow()`, `getStartColumn()`, `getEndRow()`, و `getEndColumn()`. القيم هي إحداثيات ورقة عمل صفرية الأساس، وتحديد الإحداثيات النهائية يُحدّد آخر صف وعمود يُضمّن في المستطيل، لذا يغطي المنطقة الخلايا من الموضع الابتدائي حتى الموضع النهائي شاملًا.  
على عكس التنسيق المرتبط بحقل، يُطبّق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء إضافي لـ `calculateData()` ليظهر النمط.  
قد يحتوي مستطيل `CellArea` على خلايا ملصق وخلايا قيمة معًا. يصف القسم التالي كيف تمثّل Aspose.Cells وExcel ذلك المستطيل داخليًا.  
المثال التالي ينسق المستطيل `E4:F5` في جدول محوري بنمط مائل، بلون أزرق فاتح، ثم يحفظ المصنف دون أي حساب إضافي.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **كيفية تطابق Pivot Areas و Cell Areas**
Excel يخزن تنسيق جدول محوري كسجلات `pivotArea` بدلاً من سجلات نمط الخلايا العادية في ورقة عمل. يستخدم Aspose.Cells نفس النموذج، لذا يُترجم طلب التنسيق إلى مناطق pivot عند تسجيله.  
العلاقة بين `CellArea` التي يزودها المستخدم ومناطق pivot المخزنة داخليًا هي علاقة متعددة إلى متعددة في كلا الاتجاهين.
- قد ينتج `CellArea` واحد عدة مناطق pivot. إذا كان المستطيل يغطي كلًا من خلايا الملصق والخلايا القيمة، يُقسم إلى قواعد ملصق وبيانات منفصلة، لأن نموذج الـ pivot يعالج تنسيق الملصق والبيانات بشكل مستقل.
- قد تحلّ منطقة pivot واحدة إلى عدة كائنات `CellArea` منفصلة. يمكن لمنطقة دلالية مثل صف الإجمالي الكلي، أو حقل لا تكون عناصره متجاورة، أن يغطي مستطيلات متعددة. لهذا السبب تُعيد `PivotArea.getCellAreas()` مجموعة بدلاً من مستطيل واحد.
كل عملية تنسيق تُجرى عبر `PivotTable.format` تُسجل في `PivotTable.getPivotFormats()`. كل إدخال من النوع `PivotTableFormat` يكشف عن الـ `PivotArea` المرتبطة والنمط `Style` المطبق عليها. يضيف استدعاء `PivotArea` إدخالًا واحدًا بالضبط لكل استدعاء، بينما قد يضيف استدعاء `CellArea` الذي يحتوي على مناطق دلالية مختلفة إدخالات متعددة.  
للتفريق بين المناطق المخزنة، يكشف كل `PivotArea` عن علمي `getOnlyLabel()` و `getOnlyData()`. المثال أدناه ينسق مستطيلًا واحدًا يغطي كلًا من الملصقات والقيم، يفحص `PivotTable.getPivotFormats()`، ويطبع إحداثيات `CellArea` التي تُعيد كل منطقة pivot مخزنة حلها.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
نظرًا لأن التنسيقات تُخزن كمناطق pivot بدلاً من أنماط خلايا عادية، فإنها تبقى صالحة بعد إعادة الحساب والتحديث. عندما يتم تحديث جدول محوري باستخدام `PivotTable.refreshData`، أو يُعاد حسابه عبر `calculateData`، أو يُحفظ ويُعاد تحميله، كل منطقة pivot مخزنة تُعيد حلّ موقعها الحالي وتُطبق نمطها مرة أخرى.
{{% /alert %}}

استخدم `PivotArea` المبني بـ `select` أو `selectField` عندما يجب أن يظل التمييز مرتبطًا بحقل أو بمنطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عندما يكون تنسيق مستطيل ثابت في تخطيط جدول محوري الحالي كافيًا. التحميل الزائد `format(int row, int column, Style)` يستهدف خلية واحدة. استخدم `formatAll`، المغطى في الصفحة الأصلية، عندما ينبغي إعادة تنسيق جدول محوري بالكامل مرة واحدة.

## **مقالات ذات صلة**
- [تطبيق نمط على جدول Pivot](/cells/ar/java/apply-style-to-pivot-table/)
- [إضافة حقول صف وعمود إلى جدول Pivot](/cells/ar/java/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في جدول Pivot](/cells/ar/java/manage-value-fields/)
- [تحديث جدول Pivot](/cells/ar/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}