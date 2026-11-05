---
title: إضافة تنسيق شرطي إلى جدول محوري
linktitle: إضافة تنسيق شرطي إلى جدول محوري
description: إضافة تنسيق شرطي إلى جدول محوري في Aspose.Cells for Node.js via C++ - ربط قاعدة بمنطقة البيانات باستخدام applyTo ونوع النطاق PivotConditionFormatScopeType، أو تعريف الهدف باستخدام addCellArea و pivotAreas، ثم إرفاق القواعد والأنماط عبر formatConditions.addCondition.
keywords: Aspose.Cells for Node.js via C++, جدول محوري, تنسيق شرطي, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /ar/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
الأنماط الموضحة في الصفحة الأم والصفحة الشقيقة ثابتة – تُرسم منطقة `PivotArea` أو `CellArea` مرة واحدة وتظل بنمطها بغض النظر عن القيم. التنسيق الشرطي هو المقابل القائم على القواعد – تمييز كل مبلغ يزيد عن 200، تظليل الخمسين بالمئة الوسطى، أو تحديد العناصر ذات الترتيب الأدنى – ويتبع التمييز القيم كلما أُعيد حساب الجدول المحوري أو تم تحديثه.  
في Aspose.Cells، يعيش تنسيق الشرطي للجدول المحوري في مجموعة `pivotTable.getConditionalFormats()`. كل إدخال هو `PivotConditionalFormat` يجيب على سؤالين بشكل مستقل:
- **أين يتم تطبيق القاعدة؟** يتم تعريف منطقة الهدف إما من خلال `applyTo(row, column, scope)`، التي تعكس محدد النطاق في واجهة مستخدم Excel، أو من خلال `addCellArea(cellArea)` ومجموعة `pivotConditionalFormat.getPivotAreas()`، التي تسمي المنطقة صراحةً.  
- **ما الذي تختبره القاعدة؟** يتم إضافة شرط أو أكثر إلى `formatConditions`، يحصل عليها عبر `pivotConditionalFormat.getFormatConditions()`، باستخدام `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`، ويحمل كل شرط نمطًا خاصًا من خلال `getStyle()`.

{{% alert color="primary" %}}
لا تقم باستدعاء `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` أو `formatConditions.addArea(cellArea)` على كائن `formatConditions` لتنسيق شرطي محوري. هذان التحميلان موروثان من واجهة برمجة تطبيقات التنسيق الشرطي العادي للورقة ولا يعملان مع الجداول المحورية – لا يتم تحويل منطقة الخلية إلى منطقة محورية، لذا يُتجاهل الطلب صامتًا. عرّف دائمًا المنطقة على كائن `pivotConditionalFormat` نفسه (`applyTo`، `addCellArea` أو `getPivotAreas()`) وأضف القاعدة بأحد تجاوزات `addCondition`.
{{% /alert %}}

## **تطبيق قاعدة مع نطاق (طريقة واجهة Excel)**
الطريقة الأولى توضع القاعدة كما تفعل واجهة مستخدم Excel. تُسمّى خلية الجدول المحوري بإحداثيات ورقة عمل صفرية الأساس، ويخبر نطاق `PivotConditionFormatScopeType` Aspose.Cells إلى أي مدى يجب أن تمتد القاعدة من تلك الخلية:
- `PivotConditionFormatScopeType.DATA` – جميع خلايا القيم التي ينتجها الجدول المحوري، بما في ذلك المجاميع الكلية.  
- `PivotConditionFormatScopeType.FIELD` – خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، مستثنية المجاميع الكلية. يجب أن تكون الخلية خلية حقل مثل تسمية حقل صف؛ تمرير خلية قيمة سيؤدي إلى استثناء.  
- `PivotConditionFormatScopeType.SELECTION` – فقط خلايا القيم عند التقاطع التي تختارها الخلية، عادةً خلية قيمة واحدة.
المثال أدناه يبني جدولًا محوريًا لمبيعات الفواكه بحيث تكون الزاوية العلوية اليسرى في E3، يربط تنسيقًا شرطيًا بالخلية F4 (الصف 3، العمود 5) بنطاق `DATA`، ويُبرز كل مبلغ أكبر من 200 بخط أبيض عريض على خلفية حمراء. مع القيم تفاح 220، موز 330، كرز 200، ومجموع إجمالي 750، تُلوّن القاعدة الخلايا F4 وF5 وF7 – المنطقة المحلولة هي العمود الكامل للبيانات F4:F7، وتضيء فقط الخلايا التي يجتاز قيمتها القاعدة.

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
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Rule - highlight amounts greater than 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

ربط القاعدة نفسها بتسمية حقل الصف E4 (الصف 3، العمود 4) بنطاق `FIELD` يحل إلى F4:F6 بدلاً من ذلك – نفس عمود البيانات دون صف المجموع الكلي – لأن النطاق الآن يصف حقل `Fruit` بدلاً من منطقة القيم بالكامل. نطاق `SELECTION` المرتبط بـ F4 يحل إلى F4 فقط.

## **تعريف المنطقة يدوياً**
الطريقة الثانية تتخطى محدد النطاق وتسمي المنطقة صراحةً على `PivotConditionalFormat`.

### **مستطيل ورقة عمل باستخدام addCellArea**
`addCellArea(cellArea)` يسجل المستطيل المعطى كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة عمل صفرية الأساس، وتكون المنطقة بالضبط هي المستطيل المقدم – دون توسيع إلى عمود البيانات ودون منطق المجاميع الكلية. استخدمها عندما تكون الخلايا ذات الأهمية مستطيلًا ثابتًا معروفًا في تخطيط الجدول المحوري الحالي.

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
// Target the rectangle F4:F6 (the value cells without the grand total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Rule - italic on light yellow for amounts between 150 and 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **منطقة محورية معنوية باستخدام getPivotAreas**
`pivotConditionalFormat.getPivotAreas()` هو نفس نموذج المنطقة الدلالية الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. أنشئ `PivotArea`، اختر حقلًا أو منطقة باستخدام `select` أو `selectField`، ثم أضفه باستخدام `pivotAreas.addPivotArea(pivotArea)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذا يتبع التنسيق الشرطي الحقل عندما يتم تحديث الجدول المحوري ويتغير التخطيط. التحميل `pivotAreas.add(pivotArea)` ما يزال موجودًا لكنه مُعلَّق – يفضَّل استخدام `addPivotArea`.

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
// Attach the rule to the Amount data field as a semantic region
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **أين يتم تخزين القواعد وكيفية بقاءها بعد إعادة التحميل**
كل استدعاء `conditionalFormats.add()` يضيف `PivotConditionalFormat` إلى الجدول المحوري. تُحفظ الشروط وصيغها وأنماطها مع المصنف – فتح الملف مرة أخرى في المثال أدناه يُظهر نفس القاعدة مع أنواعها ومشغليها وصيغها سليمة، وتُظهر `getCellAreas()` المناطق نفسها. تُحذف الإدخالات التي لم تتلقَ شرطًا عند حفظ المصنف، بنفس الطريقة التي يتجاهل بها Excel تنسيقًا شرطيًا لا يحتوي على قاعدة.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)
- [تنسيق جزء من جدول محوري](/cells/ar/nodejs-cpp/format-part-of-pivot-table/)
- [عرض أو تصفية أعلى 10 في جدول محوري](/cells/ar/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}