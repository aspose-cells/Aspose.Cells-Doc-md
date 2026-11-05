---
title: إضافة تنسيق شرطي إلى جدول محوري
linktitle: إضافة تنسيق شرطي إلى جدول محوري
description: إضافة تنسيق شرطي إلى جدول محوري في Aspose.Cells for Java - ربط قاعدة بمنطقة البيانات باستخدام applyTo ونوع نطاق PivotConditionFormatScopeType، أو تعريف الهدف باستخدام addCellArea و getPivotAreas، ثم إرفاق القواعد والأنماط عبر FormatConditions.addCondition.
keywords: Aspose.Cells for Java, جدول محوري, التنسيق الشرطي, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /ar/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
الأنماط الموضحة في الصفحة الأصلية والصفحة الشقيقة ثابتة - يتم تلوين منطقة `PivotArea` أو `CellArea` مرة واحدة وتحتفظ بنمطها بغض النظر عن القيم. التنسيق الشرطي هو المقابل القائم على القواعد - إبراز كل مبلغ يزيد عن 200، تظليل الخمسين بالمائة الوسطى، أو وضع علامة على العناصر ذات الترتيب الأدنى - ويتبع الإبراز القيم كلما تم إعادة حساب أو تحديث الجدول المحوري.  
في Aspose.Cells، يعيش التنسيق الشرطي للجدول المحوري داخل مجموعة `PivotTable.getConditionalFormats()` . كل إدخال هو `PivotConditionalFormat` يجيب على سؤالين بشكل مستقل:
- **أين تُطبّق القاعدة؟** يتم تعريف منطقة الهدف إما عبر `applyTo(int row, int column, PivotConditionFormatScopeType scope)`، التي تعكس أداة اختيار النطاق في واجهة Excel، أو عبر `addCellArea(CellArea)` ومجموعة `getPivotAreas()` التي تحدد المنطقة صراحةً.
- **ما الذي تختبره القاعدة؟** يتم إضافة شرط أو أكثر إلى `getFormatConditions()` باستخدام `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`، ويحمل كل شرط نمطًا (`Style`) خاصًا به.

{{% alert color="primary" %}}
لا تستدعِ `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` أو `FormatConditionCollection.addArea(CellArea)` على مجموعة `getFormatConditions()` لتنسيق شرطي محوري. هذين الأسلوبين المستبدلين موروثان من واجهة برمجة التطبيقات لتنسيق الشرطي في ورقة العمل العادية ولا يعملان مع الجداول المحورية - لا يتم تحويل منطقة الخلية إلى منطقة محورية، لذا يتم تجاهل الطلب صامتًا. احرص دائمًا على تعريف المنطقة على `PivotConditionalFormat` نفسه (`applyTo`، `addCellArea`، أو `getPivotAreas()`) وإضافة القاعدة باستخدام أحد أساليب `addCondition`.
{{% /alert %}}

## **تطبيق قاعدة بنطاق (طريقة واجهة Excel)**
الطريقة الأولى توضع القاعدة كما تفعل واجهة Excel. يُسمى خلية في الجدول المحوري بإحداثيات ورقة عمل تبدأ من الصفر، ويُحدّد نطاق `PivotConditionFormatScopeType` مدى وصول القاعدة من تلك الخلية إلى Aspose.Cells:
- `PivotConditionFormatScopeType.DATA` - جميع خلايا القيم التي ينتجها الجدول المحوري، بما في ذلك المجاميع الكلية.
- `PivotConditionFormatScopeType.FIELD` - خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، مع استثناء المجاميع الكلية. يجب أن تكون الخلية خلية حقل مثل تسمية حقل صف؛ تمرير خلية قيمة يُسبب استثناء.
- `PivotConditionFormatScopeType.SELECTION` - فقط خلايا القيم عند التقاطع التي تختارها الخلية، عادةً خلية قيمة واحدة.  
المثال أدناه يُنشئ جدولًا محوريًا لمبيعات الفواكه حيث زاويةه العلوية اليسرى في E3، ويربط تنسيقًا شرطيًا بالخلية F4 (الصف 3، العمود 5) باستخدام نطاق `DATA`، ويُبرز كل مبلغ أكبر من 200 بنص أبيض عريض على خلفية حمراء. مع القيم تفاح 220، موز 330، كرز 200، والمجموع الكلي 750، تقوم القاعدة بتلوين F4 وF5 وF7 - المنطقة المحددة هي عمود البيانات بالكامل F4:F7، وتضيء فقط الخلايا التي تتجاوز القاعدة قيمتها.

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
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Rule - highlight amounts greater than 200
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

ربط القاعدة نفسها بتسمية حقل الصف E4 (الصف 3، العمود 4) باستخدام نطاق `FIELD` ينتج المنطقة F4:F6 بدلاً من ذلك - نفس عمود البيانات بدون صف المجموع الكلي - لأن النطاق الآن يصف حقل `Fruit` بدلاً من مساحة القيم بالكامل. النطاق `SELECTION` المرتبط بـ F4 ينتج فقط الخلية F4.

## **تحديد المنطقة يدويًا**

### **مستطيل ورقة عمل باستخدام addCellArea**
`addCellArea(CellArea)` يسجل المستطيل المعطى كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة عمل تبدأ من الصفر، والمنطقة هي بالضبط المستطيل المقدم - دون توسيع إلى عمود البيانات ولا منطق المجاميع الكلية. يستخدم ذلك عندما تكون الخلايا المهمة مستطيلًا ثابتًا معروفًا في تخطيط الجدول المحوري الحالي.

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
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **منطقة محورية دلالية باستخدام getPivotAreas**
`getPivotAreas()` تُعيد نفس نموذج المنطقة الدلالية الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. قم بإنشاء `PivotArea`، اختر حقلًا أو منطقة باستخدام `select` أو `selectField`، وأضفها باستخدام `getPivotAreas().addPivotArea(PivotArea)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذلك يتبع التنسيق الشرطي الحقل عندما يتم تحديث الجدول المحوري ويتغير التخطيط. ما زال الأسلوب `getPivotAreas().add(PivotArea)` موجود لكنه مُعلَّم كمهمل - يفضَّل استخدام `addPivotArea`.

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
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **أين يتم تخزين القواعد وكيفية بقاءها بعد إعادة التحميل**
كل استدعاء `getConditionalFormats().add()` يضيف `PivotConditionalFormat` واحد إلى الجدول المحوري. تُحفظ الشروط وصيغها وأنماطها مع المصنف - إعادة فتح الملف في المثال أدناه تُظهر القاعدة نفسها مع الأنواع والعمليات والصيغ بحالة سليمة، وتُظهر `getCellAreas()` نفس المناطق. تُحذف الإدخالات التي لم تتلقَ شرطًا أبدًا عند حفظ المصنف، بنفس طريقة حذف Excel لتنسيق شرطي لا يحتوي على قاعدة.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/java/apply-style-to-pivot-table/)
- [تنسيق جزء من جدول محوري](/cells/ar/java/format-part-of-pivot-table/)
- [عرض أو تصفية أعلى 10 في جدول محوري](/cells/ar/java/top-10-show-or-filter-in-pivot-table/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}