---
title: تنسيق جزء من جدول محوري
linktitle: تنسيق جزء من جدول محوري
description: تنسيق جزء من جدول محوري في Aspose.Cells for Node.js via C++ عن طريق تطبيق الأنماط على مناطق PivotArea الدلالية أو مستطيلات CellArea من خلال PivotTable.format، مع تخزين التنسيقات في PivotTable.getPivotFormats() وحفظها عند تحديث جدول محوري.
keywords: Aspose.Cells, Node.js via C++, جدول محوري, تنسيق, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /ar/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
`PivotTable.formatAll` يطبق نمطًا واحدًا على جدول محوري كامل ويتم شرح ذلك في الصفحة الأصلية. لا يميز بين التسميات، القيم، الإجماليات، أو مناطق معينة من التقرير.  
في الواقع، عادةً ما يحتاج جزء فقط من جدول محوري إلى التمييز. تشمل الأهداف الشائعة التسميات الخاصة بحقل صف واحد، خلايا القيم التي ينتجها حقل معين، صف الإجمالي العام، أو مستطيل عشوائي مثل صفوف العنصرين الأولين.  
تطبيق نمط مباشرةً على خلايا ورقة عمل الخاصة بجدول محوري لا يعادل ذلك. Excel يخزن تنسيق الجداول المحورية كمنطقتين `PivotArea` دلاليتين بدلاً من سجلات أنماط خلايا عادية. يبقى تنسيق منطقة Pivot مرتبطًا بمنطقة مثل تسميات الحقل أو قيم البيانات، ويُعاد حله عندما يُعاد حساب جدول محوري أو يُحدّث أو يُوسّع. أما النمط المكتوب مباشرةً إلى خلية فيعلق موقعه في تلك الخلية ولا يتعقّبها نموذج Pivot.  
توفر Aspose.Cells عائلة التحميل الزائد `PivotTable.format` بحيث تكون كلتا الطريقتين متاحتين:
- `format(PivotArea, Style)` يربط نمطًا بمنطقة دلالية تُنشأ باستخدام `PivotArea.select` أو `PivotArea.selectField`.
- `format(CellArea, Style)` يربط نمطًا بمستطيل ورقة عمل داخل جدول محوري.
- `format(number row, number column, Style)` يستهدف خلية واحدة.
- `formatAll(Style)` ينسق جدول محوري كامل.

## **تنسيق منطقة Pivot**
سير العمل القائم على المنطقة الدلالية هو النهج الموصى به عندما يجب أن يبقى التمييز مرتبطًا بحقل أو منطقة من التقرير.
1. أنشئ كائن `PivotArea` باستخدام `new PivotArea(pivotTable)`. يصف هذا الكائن منطقة دلالية تنتمي إلى جدول محوري محدد.
2. اختر حقلًا حسب موقعه الصفري على محور معين باستخدام `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` يختار كلًا من التسميات والبيانات للحقل.
   - `PivotTableSelectionType.LabelOnly` يختار تسميات الحقل فقط.
   - `PivotTableSelectionType.DataOnly` يختار خلايا بيانات الحقل فقط.
3. اختر حقلًا بالاسم باستخدام `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. عندما يُختار حقل صف بالاسم، تُحل المنطقة إلى خلايا القيم التي ينتجها عناصر ذلك الحقل.
4. أنشئ كائن `Style` عبر `workbook.createStyle()`، واضبط الخط، ولون الخط، ونمط الخلفية الصلب، ثم مرّر النمط إلى `pivotTable.format(area, style)`.
5. كل استدعاء لتعددية التحميل `PivotArea` يضيف إدخالًا واحدًا من نوع `PivotTableFormat` إلى `pivotTable.getPivotFormats()`.
6. تُرسم التنسيقات المرتبطة بالحقل عندما تُحسب بيانات Pivot. لذلك، استدعِ `pivotTable.calculateData()` بعد تطبيق التنسيقات لكي تظهر الأنماط.
المثال التالي يُنشئ جدول محوري صغير لمبيعات الفاكهة، يُنسق تسميات صف `Fruit` باستخدام `PivotArea.select` و `PivotTableSelectionType.LabelOnly`، يُنسق خلايا القيم التي ينتجها نفس حقل الصف باستخدام `PivotArea.selectField`، ثم يُعيد حساب جدول محوري بحيث تُرسم كلا النمطين.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **تنسيق مساحة خلية من جدول محوري**
استخدم `PivotTable.format(CellArea, Style)` عندما تكون المنطقة المطلوبة مستطيلًا عاديًا في ورقة العمل وليس منطقة Pivot دلالية.  
يُوصف `CellArea` بخواص `startRow`، `startColumn`، `endRow`، و `endColumn`. القيم هي إحداثيات صفية وأعمدة صفرية في الورقة، وتُحدد الإحداثيات النهائية آخر صف وعمود يُضمّن في المستطيل، لذا يغطي المجال الخلايا من الموضع البداية إلى الموضع النهاية شاملًا.  
على عكس التنسيق المرتبط بالحقل، يُطبق تنسيق `CellArea` على الخلايا فورًا. لا يلزم استدعاء إضافي لـ `pivotTable.calculateData()` لكي يظهر النمط.  
قد يحتوي مستطيل `CellArea` على خلايا تسميات وخلايا قيم معًا. يصف القسم التالي كيف تمثّل Aspose.Cells وExcel هذا المستطيل داخليًا.  
المثال التالي ينسق المستطيل `E4:F5` في جدول محوري بنمط مائل، أزرق فاتح، ويحفظ المصنف دون أي إعادة حساب إضافية.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **كيفية ربط مناطق Pivot ومساحات الخلية**
يخزن Excel تنسيق جداول محورية كسجلات `pivotArea` بدلاً من سجلات أنماط خلايا عادية. يستخدم Aspose.Cells النموذج نفسه، لذا يُترجم طلب التنسيق إلى مناطق Pivot عند تسجيله.  
العلاقة بين `CellArea` التي يقدمها المستخدم ومناطق Pivot المخزّنة داخليًا هي علاقة متعدد إلى متعدد في كلا الاتجاهين.
- قد ينتج عن `CellArea` واحدة عدة مناطق Pivot. إذا كان المستطيل يضم خلايا تسميات وخلايا قيم، يتم تجزيئه إلى قواعد تنسيق تسميات وبيانات منفصلة، لأن نموذج Pivot يتعامل مع تنسيق التسميات وتنسيق البيانات بصورة مستقلة.
- قد تحل منطقة Pivot واحدة إلى عدة مثيلات `CellArea` غير متصلة. يمكن لمنطقة دلالية مثل صف إجمالي عام، أو حقل لا تكون عناصره متجاورة، أن تغطي عدة مستطيلات. لهذا السبب تُعيد `PivotArea.getCellAreas()` مجموعة بدلاً من مستطيل واحد.
كل عملية تنسيق تُجرى عبر `pivotTable.format()` تُسجل في `pivotTable.getPivotFormats()`. كل إدخال من نوع `PivotTableFormat` يُظهر الـ `PivotArea` المرتبط به والـ `Style` المُطبق. تضيف تعددية التحميل `PivotArea` إدخالًا واحدًا بالضبط لكل استدعاء، بينما يمكن أن تضيف `CellArea` يحتوي على مناطق دلالية مختلفة عدة إدخالات.  
لتمييز المناطق المخزّنة، تُظهر كل `PivotArea` العلمين `getOnlyLabel()` و `getOnlyData()`. المثال أدناه ينسق مستطيلًا واحدًا يغطي كلًا من التسميات والقيم، يتحقّق من `pivotTable.getPivotFormats()`، ويطبع إحداثيات `CellArea` التي تُحلّ كل منطقة Pivot مخزّنة إليها.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
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
نظرًا لأن التنسيقات تُخزن كمناطق Pivot بدلاً من أنماط خلية عادية، فإنها تظل محفوظة عبر إعادة الحساب والتحديث. عندما يتم تحديث جدول محوري باستخدام `pivotTable.refreshData()`، أو إعادة حسابه بـ `pivotTable.calculateData()`، أو حفظه وإعادة تحميله، تعيد كل منطقة Pivot مخزّنة حلّ موقعها الحالي وتُعاد تطبيق نمطها.
{{% /alert %}}

استخدم `PivotArea` المُنشأة بـ `select` أو `selectField` عندما يجب أن يبقى التمييز مرتبطًا بحقل أو منطقة دلالية عبر عمليات التحديث، واستخدم `CellArea` عندما يكون تنسيق مستطيل ثابت في تخطيط جدول محوري الحالي كافياً. تستهدف النسخة overload `format(number row, number column, Style)` خلية واحدة. استخدم `formatAll`، المذكور في الصفحة الأصلية، عندما يُراد إعادة تنسيق جدول محوري كامل مرة واحدة.

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)
- [إضافة حقول صف وعمود إلى جدول محوري](/cells/ar/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [إدارة حقول القيم في جدول محوري](/cells/ar/nodejs-cpp/manage-value-fields/)
- [تحديث جدول محوري](/cells/ar/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}