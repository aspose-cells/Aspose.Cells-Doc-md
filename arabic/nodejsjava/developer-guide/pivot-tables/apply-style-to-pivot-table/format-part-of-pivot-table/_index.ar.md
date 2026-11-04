---
title: تنسيق جزء من جدول محوري
linktitle: تنسيق جزء من جدول محوري
description: تنسيق جزء من جدول محوري في Aspose.Cells for Node.js via Java عن طريق تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea عبر PivotTable.format، مع تخزين التنسيقات في PivotTable.getPivotFormats() وبقاءها عند تحديث جدول محوري.
keywords: Aspose.Cells for Node.js via Java, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /ar/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
`PivotTable.formatAll` يطبّق نمطًا واحدًا على جدول محوري بالكامل ويغطى في الصفحة الأصلية. لا يميّز بين التسميات والقيم والإجماليات أو المناطق المحددة من التقرير.  
في الواقع، عادةً ما يحتاج جزء فقط من جدول محوري إلى إبراز. تشمل الأهداف الشائعة التسميات التي تخص حقل صف واحد، خلايا القيم التي ينتجها حقل واحد، صف الإجمالي الكلي، أو مستطيل عشوائي مثل الصفين الأولين من العناصر.  
تطبيق نمط مباشرةً على خلايا ورقة العمل الخاصة بجدول محوري ليس مكافئًا. Excel يخزن تنسيق جدول محوري كمناطق دلالية `PivotArea` بدلاً من سجلات نمط خلايا عادية. يبقى تنسيق منطقة pivot مرتبطًا بمنطقة مثل تسميات الحقل أو قيم البيانات، ويُعاد حلّها عندما يُعاد حساب جدول محوري أو يُحدَّث أو يُوسّع. أما النمط المكتوب مباشرةً إلى خلية، فهو ينتمي إلى موقع تلك الخلية ولا يتتبعه نموذج pivot.  
توفر Aspose.Cells عائلة التحميل الزائد `PivotTable.format` بالكامل بحيث تتوفر كلا النوعين من التنسيق:
- `format(PivotArea, Style)` يُثبت نمطًا إلى منطقة دلالية تُبنى باستخدام `PivotArea.select` أو `PivotArea.selectField`.
- `format(CellArea, Style)` يُثبت نمطًا إلى مستطيل ورقة عمل داخل جدول محوري.
- `format(int row, int column, Style)` يستهدف خلية واحدة.
- `formatAll(Style)` ينسّق جدول محوري بالكامل.

## **تنسيق PivotArea**
طريقة العمل مع المنطقة الدلالية هي النهج الموصى به عندما يجب أن يتبع التمييز حقلًا أو منطقة من التقرير.
1. أنشئ كائن `PivotArea` باستخدام `new PivotArea(pivotTable)`. يصف الكائن منطقة دلالية تنتمي إلى جدول محوري محدد.
2. اختر حقلًا بحسب موقعه الصفري على محور معين باستخدام `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` يختار كلًا من التسميات والبيانات الخاصة بالحقل.
   - `PivotTableSelectionType.LABEL_ONLY` يختار تسميات الحقل فقط.
   - `PivotTableSelectionType.DATA_ONLY` يختار خلايا بيانات الحقل فقط.
3. اختر حقلًا بحسب اسمه باستخدام `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. عندما يُختار حقل صف بالاسم، تُعيد المنطقة إلى خلايا القيم التي ينتجها عناصر ذلك الحقل.
4. أنشئ كائن `Style` باستخدام `Workbook.createStyle()`، واضبط خطه، ولون الخلفية، ونمط الخلفية الصلبة، ثم مرّر النمط إلى `PivotTable.format(area, style)`.
5. كل استدعاء للتحميل الزائد `PivotArea` يضيف إدخالًا واحدًا من نوع `PivotTableFormat` إلى `PivotTable.getPivotFormats()`.
6. تُرسم التنسيقات المرتبطة بالحقل عندما تُحسب بيانات pivot. لذا، استدعِ `PivotTable.calculateData()` بعد تطبيق التنسيقات لتظهر الأنماط.
المثال التالي يُنشئ جدول محوري لمبيعات الفواكه، يُنسّق تسميات صف `Fruit` باستخدام `PivotArea.select` و`PivotTableSelectionType.LABEL_ONLY`، يُنسّق خلايا القيم التي ينتجها نفس حقل الصف باستخدام `PivotArea.selectField`، ثم يُعيد حساب جدول محوري لتُظهر كلا النمطين.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **تنسيق Cell Area لجدول محوري**
استخدم `PivotTable.format(CellArea, Style)` عندما تكون المنطقة المطلوبة مستطيل ورقة عمل عادي وليس منطقة pivot دلالية.  
يُوصف `CellArea` بالحقول العامة `StartRow`، `StartColumn`، `EndRow`، و`EndColumn`. القيم صِفرية الأساس لإحداثيات ورقة العمل، وتحدد الإحداثيات النهائية الصف والعمود الأخيرين المشمولين بالمستطيل، لذا يغطي المستطيل الخلايا من الموضع الابتدائي حتى الموضع النهائي شاملًا.  
على عكس تنسيق مرتبط بحقل، يُطبّق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء إضافي لـ `calculateData()` لظهور النمط.  
قد يحتوي مستطيل `CellArea` على خلايا تسميات وخلايا قيم معًا. يصف القسم التالي كيف تمثّل Aspose.Cells وExcel ذلك المستطيل داخليًا.  
المثال التالي يُنسّق المستطيل `E4:F5` من جدول محوري بنمط مائل ولون أزرق فاتح، ويحفظ المصنف دون أي حساب إضافي.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **كيفية ربط Pivot Areas و Cell Areas**
تخزن Excel تنسيق جدول محوري كسجلات `pivotArea` بدلاً من سجلات نمط خلايا ورقة العمل العادية. يستخدم Aspose.Cells النموذج نفسه، لذا تُترجم طلبات التنسيق إلى مناطق pivot عند تسجيلها.  
العلاقة بين `CellArea` التي يُدخلها المستخدم ومناطق pivot المخزنة داخليًا هي علاقة متعددة إلى متعددة في كلا الاتجاهين.
- قد تُنتج `CellArea` واحدة عدة مناطق pivot. إذا امتد المستطيل عبر خلايا تسميات وخلايا قيم، فإنه يُقسم إلى قواعد تسميات وبيانات منفصلة، لأن نموذج pivot يعامل تنسيق التسميات وتنسيق البيانات بشكل مستقل.
- قد تُعيد منطقة pivot إلى عدة مثيلات `CellArea` غير متصلة. يمكن لمنطقة دلالية مثل صف إجمالي كلي، أو حقل لا تكون عناصره متجاورة، أن تغطي مستطيلات متعددة. لهذا تُعيد `PivotArea.getCellAreas()` مجموعة بدلاً من مستطيل واحد.
كل عملية تنسيق تُجرى عبر `PivotTable.format` تُسجل في `PivotTable.getPivotFormats()`. كل إدخال `PivotTableFormat` يُظهر `PivotArea` المرتبطة و`Style` المُطبق عليها. التحميل الزائد `PivotArea` يضيف إدخالًا واحدًا لكل استدعاء، في حين أن `CellArea` التي تحتوي على مناطق دلالية مختلفة يمكن أن تُضيف إدخالات متعددة.  
للتفريق بين المناطق المخزَّنة، تُظهر كل `PivotArea` العلامات `getOnlyLabel()` و`getOnlyData()`. المثال أدناه يُنسّق مستطيلًا واحدًا يغطي التسميات والقيم، يفتش `PivotTable.getPivotFormats()`، ويطبع إحداثيات `CellArea` التي تُعيد كل منطقة pivot مخزنة إلى موقعها.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
        );
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
نظرًا لأن التنسيقات تُخزن كمناطق pivot بدلاً من أنماط خلايا عادية، فإنها تبقى بعد إعادة الحساب والتحديث. عندما يُحدث جدول محوري باستخدام `PivotTable.refreshData()`، أو يُعاد حسابه بـ `calculateData()`، أو يُحفظ ويُعاد تحميله، فإن كل منطقة pivot مخزَّة تُعيد حلّها إلى الموضع الحالي لمنطقتها وتُطبق نمطها من جديد.
{{% /alert %}}

استخدم `PivotArea` المبنية باستخدام `select` أو `selectField` عندما يجب أن يبقى التمييز مرتبطًا بحقل أو منطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عندما يكون تنسيق مستطيل ثابت في تخطيط جدول محوري الحالي كافيًا. التحميل الزائد `format(int row, int column, Style)` يستهدف خلية فردية. استخدم `formatAll`، المغطى في الصفحة الأصلية، عندما يجب إعادة تنسيق جدول محوري بالكامل مرة واحدة.

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/nodejs-java/apply-style-to-pivot-table/)
- [إضافة حقول صف وعمود إلى جدول محوري](/cells/ar/nodejs-java/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في جدول محوري](/cells/ar/nodejs-java/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}