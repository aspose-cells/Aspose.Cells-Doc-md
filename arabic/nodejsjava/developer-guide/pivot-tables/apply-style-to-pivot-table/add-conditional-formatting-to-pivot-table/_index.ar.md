---
title: إضافة التنسيق الشرطي إلى جدول محوري
linktitle: إضافة التنسيق الشرطي إلى جدول محوري
description: إضافة التنسيق الشرطي إلى جدول محوري في Aspose.Cells for Node.js via Java - ربط قاعدة بمنطقة البيانات باستخدام applyTo ونوع نطاق PivotConditionFormatScopeType، أو تحديد الهدف باستخدام addCellArea و getPivotAreas، ثم إرفاق القواعد والأنماط عبر getFormatConditions().addCondition.
keywords: Aspose.Cells, جدول محوري, التنسيق الشرطي, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /ar/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
الأنماط الواردة في الصفحة الأصلية والصفحة الشقيقة ثابتة – يتم رسم منطقة `PivotArea` أو `CellArea` مرة واحدة وتظل أنماطها ثابتة بغض النظر عن القيم. التنسيق الشرطي هو النظير القائم على القواعد – يميّز كل مبلغ يزيد عن 200، يظلل الخمسين بالمائة الوسطى، أو يضع علامة على العناصر ذات الترتيب الأدنى – ويتبع التمييز القيم كلما أعيد حساب الجدول المحوري أو تم تحديثه.  
في Aspose.Cells for Node.js via Java، يعيش التنسيق الشرطي للجدول المحوري في مجموعة `pivotTable.getConditionalFormats()`. كل إدخال هو `PivotConditionalFormat` يجيب على سؤالين بشكل مستقل:
- **أين تُطبق القاعدة؟** يتم تعريف المنطقة المستهدفة إما عبر `applyTo(int row, int column, PivotConditionFormatScopeType scope)`، التي تعكس أداة اختيار النطاق في واجهة Excel، أو عبر `addCellArea(CellArea)` ومجموعة `getPivotAreas()` التي تسمي المنطقة صراحةً.
- **ما الذي تختبره القاعدة؟** تُضاف شرط أو أكثر إلى `getFormatConditions()` باستخدام `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`، ويحمل كل شرط نمطه الخاص عبر `getStyle()`.

{{% alert color="primary" %}}
لا تستدعِ `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` أو `FormatConditionCollection.addArea(CellArea)` على كائن `getFormatConditions()` لتنسيق شرطي محوري. هذان الأسلوبان موروثان من واجهة برمجة التطبيقات للتنسيق الشرطي العادي في ورقة العمل ولا يعملان للجدول المحوري – لا يتم تحويل منطقة الخلية إلى منطقة محورية، لذا يتم تجاهل الطلب بصمت. عرّف المنطقة دائمًا على `PivotConditionalFormat` نفسه (`applyTo`، `addCellArea` أو `getPivotAreas()`) وأضف القاعدة باستخدام أحد الأسلوبين `addCondition`.
{{% /alert %}}

## **تطبيق قاعدة بنطاق (طريقة واجهة مستخدم Excel)**
الطريقة الأولى تضع القاعدة كما تفعل واجهة مستخدم Excel. تُسمى خلية جدول محوري بإحداثيات ورقة عمل صفرية، ويخبر نطاق `PivotConditionFormatScopeType` Aspose.Cells إلى أي مدى يجب أن تمتد القاعدة من تلك الخلية:
- `PivotConditionFormatScopeType.DATA` – جميع خلايا القيم التي ينتجها جدول محوري، بما في ذلك الإجماليات العامة.
- `PivotConditionFormatScopeType.FIELD` – خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، مستبعدة الإجماليات العامة. يجب أن تكون الخلية خلية حقل مثل تسمية حقل صف؛ تمرير خلية قيمة يؤدي إلى استثناء.
- `PivotConditionFormatScopeType.SELECTION` – فقط خلايا القيم عند التقاطع التي تحددها الخلية، عادةً خلية قيمة واحدة.
المثال أدناه يُنشئ جدولًا محوريًا لمبيعات الفواكه بحيث تكون زاوية العلوية اليسرى عند الخلية E3، ويربط تنسيقًا شرطيًا بالخلية F4 (صف 3، عمود 5) بنطاق `DATA`، ويُميز كل مبلغ يزيد عن 200 بخط عريض أبيض على خلفية حمراء. مع القيم Apple 220، Banana 330، Cherry 200، والإجمالي 750، تُطبق القاعدة على F4 وF5 وF7 – المنطقة المحسوبة هي عمود البيانات بالكامل F4:F7، وتُضاء فقط الخلايا التي تتجاوز القاعدة قيمتها.

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
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Rule - highlight amounts greater than 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

ربط القاعدة نفسها بتسمية حقل الصف E4 (صف 3، عمود 4) بنطاق `FIELD` يُحل إلى F4:F6 بدلاً من ذلك – أي عمود البيانات نفسه بدون صف الإجماليات العامة – لأن النطاق الآن يُشير إلى حقل `Fruit` وليس إلى مساحة القيم بالكامل. النطاق `SELECTION` المرتبط بـ F4 يُحل إلى F4 فقط.

## **تحديد المنطقة يدويًا**
الطريقة الثانية تتخطى أداة اختيار النطاق وتسمي المنطقة صراحةً على `PivotConditionalFormat`.

### **مستطيل ورقة عمل باستخدام addCellArea**
`addCellArea(CellArea)` يسجل المستطيل المعطى كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة عمل صفرية، وتكون المنطقة هي المستطيل المُزود بالضبط – دون توسيع إلى عمود البيانات ولا منطق إجمالي عام. استخدمها عندما تكون الخلايا ذات الأهمية مستطيلًا ثابتًا معروفًا في تخطيط الجدول الحالي.

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
// Target the rectangle F4:F6 (the value cells without the grand total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **منطقة محورية دلالية باستخدام PivotAreas**
`getPivotAreas()` هو نموذج المنطقة الدلالية نفسه الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. أنشئ `PivotArea`، واختر حقلًا أو منطقةً باستخدام `select` أو `selectField`، وأضفه عبر `getPivotAreas().addPivotArea(PivotArea)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذا يتبع التنسيق الشرطي الحقل عندما يُعاد تحديث جدول محوري ويتغير التخطيط. ما يزال الأسلوب `getPivotAreas().add(PivotArea)` يجمع لكنه مُعلَّم قديمًا – يفضَّل استخدام `addPivotArea`.

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
// Attach the rule to the Amount data field as a semantic region
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **مكان تخزين القواعد وكيفية بقاءها بعد إعادة التحميل**
كل استدعاء `add()` على `getConditionalFormats()` يضيف `PivotConditionalFormat` واحدًا إلى جدول محوري. تُحفظ الشروط وصيغها وأنماطها مع المصنف – إعادة فتح الملف في المثال أدناه تُظهر القاعدة نفسها مع أنواعها، عواملها، وصيغها كاملة، وتُعيد `getCellAreas()` نفس المناطق. تُحذف الإدخالات التي لم تتلقى شرطًا عندما يُحفظ المصنف، بنفس الطريقة التي يتخلص بها Excel من تنسيق شرطي لا يحتوي على قاعدة.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **مقالات ذات صلة**
- [تطبيق النمط على جدول محوري](/cells/ar/nodejs-java/apply-style-to-pivot-table/)
- [تنسيق جزء من جدول محوري](/cells/ar/nodejs-java/format-part-of-pivot-table/)
- [عرض أو تصفية أعلى 10 في جدول محوري](/cells/ar/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}