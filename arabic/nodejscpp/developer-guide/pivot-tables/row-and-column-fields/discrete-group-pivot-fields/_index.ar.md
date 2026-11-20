---
title: تجميع منفصل لعناصر حقل الجدول المحوري
linktitle: تجميع منفصل
description: تعلم كيفية تجميع عناصر حقل الجدول المحوري في مجموعات مسماة مخصصة مثل الفواكه والخضروات باستخدام DiscreteGroupItem و PivotFieldGroupOptions.DiscreteGroupItems في Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, جدول محوري, تجميع منفصل, DiscreteGroupItem, PivotFieldGroupOptions, تجميع عناصر الجدول المحوري, مجموعات مخصصة, PivotField.Group, Node.js, Excel جدول محوري
type: docs
weight: 90
url: /ar/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يجمع التجميع التلقائي العناصر حسب نوع البيانات، مثل تحويل التواريخ إلى أشهر وأرباع أو الأعداد إلى نطاقات. يحل التجميع المنفصل المشكلة العكسية، حيث يجمع عناصر محددة غير مترابطة في مجموعات مسماة مخصصة، على سبيل المثال المنتجات إلى فواكه وخضروات، المتاجر إلى مناطق، أو الحسابات إلى أقسام. توفر Aspose.Cells for Node.js via C++ التجميع المنفصل عبر فئة `DiscreteGroupItem` و خاصية `PivotFieldGroupOptions.discreteGroupItems`.
- `DiscreteGroupItem` هو اسم مجموعة بالإضافة إلى العناصر التي تنتمي إليها. يمكن تحديد العناصر بطريقتين، إما بأسمائها (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) أو بمواقعها ذات الفهرس الصفري في البيانات المصدر (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). كلا الشكلين ينتجان النتيجة نفسها.
- يتم تطبيق التجميع المنفصل على حقل في منطقة الصفوف أو منطقة الأعمدة في جدول محوري عن طريق تمرير الخيارات إلى `pivotField.group(pivotFieldGroupOptions)`.

## **تجميع عناصر حقل الجدول المحوري حسب أسماء العناصر**
المثال التالي يبني قائمة مبيعات صغيرة (منتج، تاريخ ومبلغ)، ينشئ جدولًا محوريًا منها مع وضع `product` في منطقة الصفوف، و `date` في منطقة الأعمدة، و `amount` في منطقة البيانات، ثم يعرّف مجموعتين مخصصتين حسب أسماء العناصر، الفاكهة (grape, cherry) والخضروات (carrot, potato). النتيجة تُظهر تخطيط صفوف بمستويين، حيث يكون اسم المجموعة هو المستوى الخارجي والعناصر الأصلية متداخلة تحته، مما يسمح بقراءة الاتجاهات لكل مجموعة مخصصة ولكل عنصر.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

بعد استدعاء `calculateData()` تُظهر منطقة الصفوف في جدول محوري الفاكهة (grape 50, cherry 80) والخضروات (carrot 60, potato 70) مع إجمالي شامل يبلغ 260، وتبقى تسميات الأعمدة الأربعة تواريخ (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **تجميع عناصر حقل الجدول المحوري حسب فهارس العناصر**
عندما تكون أسماء العناصر طويلة أو مُعربة، يُحدد المنشئ الثاني من `DiscreteGroupItem` العناصر بحسب الفهرس. الفهارس هي مواقع صفرية للعنصر في البيانات المصدر وفق الترتيب الذي تظهر فيه، وليس حسب الترتيب الأبجدي. في البيانات النموذجية أعلاه، العنب هو العنصر 0، والجزر هو العنصر 1، والبطاطس هي العنصر 2 والكرز هو العنصر 3، لذا تكون الفاكهة `{ 0, 3 }` والخضروات `{ 1, 2 }`. النتيجة مطابقة للمثال القائم على الأسماء.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **ملاحظة**

{{% alert color="primary" %}}
- العناصر التي لم يتم تعيينها إلى أي مجموعة مخصصة لا تُفقد. تبقى في جدول محوري على نفس مستوى المجموعات المخصصة، كل منها كإدخال عنصر واحد منفرد. في المثال أعلاه، تعريف مجموعة الفاكهة فقط يترك الجزر والبطاطس في منطقة الصفوف كإدخالات مستقلة بجانب مجموعة الفاكهة.
- تتحكم خاصية `PivotFieldGroupOptions.newPivotField` في تخطيط التجميع المنفصل. القيمة الافتراضية هي true، مما يُضيف الحقل المُجَمَّع كحقل خارجي جديد بجوار الحقل الأصلي، مُنتجًا تخطيطًا ذا مستويين كما هو موضح أعلاه (`rowFields` يزداد إلى 2). اضبطها على false لاستبدال الحقل الأصلي بدلاً من ذلك، وستُظهر منطقة الصفوف مستوى واحد يحتوي فقط على أسماء المجموعات مع القيم المجمعة، الفاكهة 130 (50 + 80) والخضروات 130 (60 + 70).
- يمكن خلط المنشئات القائمة على الأسماء وتلك القائمة على الفهارس لـ `DiscreteGroupItem` داخل نفس مصفوفة `PivotFieldGroupOptions.discreteGroupItems`.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري في جدول محوري](/cells/ar/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [إضافة حقول الصف والعمود في جدول محوري](/cells/ar/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [تطبيق نمط على جدول محوري](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)
- [تحديث جدول محوري](/cells/ar/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}