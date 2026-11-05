---
title: إضافة تنسيق شرطي إلى جدول محوري
linktitle: إضافة تنسيق شرطي إلى جدول محوري
description: إضافة تنسيق شرطي إلى جدول محوري في Aspose.Cells for JavaScript via C++ - ربط قاعدة بمنطقة البيانات باستخدام applyTo ونوع النطاق PivotConditionFormatScopeType، أو تعريف الهدف باستخدام addCellArea وpivotAreas، ثم إرفاق القواعد والأنماط عبر formatConditions.addCondition.
keywords: Aspose.Cells for JavaScript via C++, جدول محوري, تنسيق شرطي, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /ar/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
الأنماط الموضحة في الصفحة الأم والصفحة الشقيقة ثابتة - يُطبق تنسيق على منطقة `PivotArea` أو `CellArea` مرة واحدة وتظل تنسيقها كما هو بغض النظر عن القيم. التنسيق الشرطي هو المقابل القائم على القواعد - إبراز كل مبلغ يزيد عن 200، تظليل الخمسين بالمئة الوسطى، أو وضع علامة على العناصر ذات الترتيب الأدنى - ويستمر الإبراز في متابعة القيم كلما أعيد حساب جدول محوري أو تم تحديثه.  
في Aspose.Cells، يقع التنسيق الشرطي للجدول المحوري في مجموعة `pivotTable.conditionalFormats`. كل إدخال هو `PivotConditionalFormat` يجيب على سؤالين بشكل مستقل:
- **أين تُطبق القاعدة؟** يتم تعريف منطقة الهدف إما عبر `applyTo(row, column, scope)` التي تحاكي أداة اختيار النطاق في واجهة مستخدم Excel، أو عبر `addCellArea(cellArea)` ومجموعة `pivotAreas` التي تحدد المنطقة صراحةً.
- **ماذا تختبر القاعدة؟** يتم إضافة شرط أو أكثر إلى `formatConditions` باستخدام `addCondition(type, operatorType, formula1, formula2)`، وكل شرط يحمل نمطه الخاص.

{{% alert color="primary" %}}
لا تقم باستدعاء `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` أو `formatConditions.addArea(cellArea)` على كائن `formatConditions` لتنسيق شرطي للجدول المحوري. هاتان الطريقتان الموروثتان من واجهة برمجة التطبيقات العادية لتنسيق الخلايا الشرطي في ورقة العمل لا تعملان مع الجداول المحورية - لا يتم تحويل مساحة الخلية إلى مساحة جدول محوري، لذا يتم تجاهل الطلب صامتًا. احرص دائمًا على تعريف المنطقة على `PivotConditionalFormat` نفسه (`applyTo`، `addCellArea`، أو `pivotAreas`) وإضافة القاعدة باستخدام إحدى إصدارات `addCondition`.
{{% /alert %}}

## **تطبيق قاعدة بنطاق (طريقة واجهة Excel)**
الطريقة الأولى تضع القاعدة كما تفعل واجهة Excel. تُسمى خلية في جدول محوري بإحداثيات ورقة عمل صفرية الأساس، ويخبر نطاق `PivotConditionFormatScopeType` Aspose.Cells إلى أي مدى يجب أن تصل القاعدة من تلك الخلية:
- `PivotConditionFormatScopeType.Data` - جميع خلايا القيم التي ينتجها الجدول المحوري، بما في ذلك المجاميع الكلية.
- `PivotConditionFormatScopeType.Field` - خلايا القيم التي تنتمي إلى الحقل الذي تحدده الخلية، باستثناء المجاميع الكلية. يجب أن تكون الخلية خلية حقل مثل تسمية حقل الصف؛ تمرير خلية قيمة يؤدي إلى استثناء.
- `PivotConditionFormatScopeType.Selection` - فقط خلايا القيم عند التقاطع التي تختارها الخلية، عادةً خلية قيمة واحدة.  
يبني المثال أدناه جدولًا محوريًا لمبيعات الفواكه حيث الزاوية العلوية اليسرى في الخلية E3، يربط تنسيقًا شرطيًا بالخلية F4 (صف 3، عمود 5) بنطاق `Data`، ويبرز كل مبلغ أكبر من 200 بخط أبيض عريض على خلفية حمراء. مع القيم تفاح 220، موز 330، كرز 200، والمجموع الكلي 750، تقوم القاعدة بتلوين F4 وF5 وF7 - المنطقة المحلولة هي كامل عمود البيانات F4:F7، وفقط الخلايا التي تتجاوز القاعدة تُضاء.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Anchor the conditional format at F4 (row 3, column 5) with the Data scope
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Rule - highlight amounts greater than 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) returns the file as bytes
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

ربط القاعدة نفسها بملصق حقل الصف E4 (صف 3، عمود 4) بنطاق `Field` يحل إلى F4:F6 بدلاً من ذلك - نفس عمود البيانات بدون صف المجموع الكلي - لأن النطاق الآن يصف حقل `Fruit` بدلاً من مساحة القيم بالكامل. النطاق `Selection` المرتبط بـ F4 يحل إلى F4 فقط.

## **تعريف المنطقة يدويًا**
الطريقة الثانية تتجاوز أداة اختيار النطاق وتحدد المنطقة صراحةً على `PivotConditionalFormat`.

### **مستطيل ورقة عمل باستخدام addCellArea**
`addCellArea(cellArea)` يسجل المستطيل المقدم كهدف للقاعدة. الإحداثيات هي إحداثيات ورقة عمل صفرية الأساس، والمنطقة هي بالضبط المستطيل المزوَّد - لا توسيع إلى عمود البيانات ولا منطق للمجموع الكلي. استخدمه عندما تكون الخلايا المطلوبة مستطيلًا ثابتًا معروفًا في تخطيط الجدول المحوري الحالي.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Target the rectangle F4:F6 (the value cells without the grand total)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Rule - italic on light yellow for amounts between 150 and 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **منطقة جدول محوري دلالية باستخدام pivotAreas**
`pivotAreas` هو نفس نموذج المنطقة الدلالية الذي تستخدمه الصفحة الشقيقة للأنماط الثابتة. أنشئ `PivotArea`، اختر حقلًا أو منطقة باستخدام `select` أو `selectField`، وأضفه باستخدام `pivotAreas.addPivotArea(pivotArea)`. تبقى المنطقة الدلالية مرتبطة بحقلها، لذا يتبع التنسيق الشرطي الحقل عندما يتم تحديث جدول محوري ويتغير التخطيط. التحميل `pivotAreas.add(pivotArea)` لا يزال يعمل لكنه مُعلَّم كمتقَدَّم - يُفضَّل استخدام `addPivotArea`.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Attach the rule to the Amount data field as a semantic region
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Rule - grey text for amounts below 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **أين تُخزن القواعد وكيفية بقاءها بعد إعادة التحميل**
كل استدعاء `conditionalFormats.add()` يضيف `PivotConditionalFormat` واحدًا إلى جدول محوري. تُحفظ الشروط وصيغها وأنماطها مع المصنف - عند إعادة فتح الملف المحفوظ من المثال الأول في Node يُظهر نفس القاعدة مع نوعها ومعاملها وصيغتها بدون تعديل، وتُظهر `getCellAreas()` نفس المنطقة. على هذه المنصة تُظهر خاصيتي `type` و `operator` للشرط كقيم عددية للعددية enum. تُحذف الإدخالات التي لم تتلقَ شرطًا أبداً عند حفظ المصنف، بالطريقة نفسها التي يتخلص منها Excel من تنسيق شرطي لا يحتوي على قاعدة.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Reload the file written by the first example
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // This prints:
    // Conditional formats: 1
    // Format 0: 1 2 formula1==200   (type 1 = CellValue, operator 2 = GreaterThan)
    //     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
    process.exit(0);
});
```

## **مقالات ذات صلة**
- [تطبيق نمط على جدول محوري](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)
- [تنسيق جزء من جدول محوري](/cells/ar/javascript-cpp/format-part-of-pivot-table/)
- [أعلى 10 إظهار أو تصفية في جدول محوري](/cells/ar/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}