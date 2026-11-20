---
title: التجميع المنفصل لعناصر حقول الجدول المحوري
linktitle: التجميع المنفصل
description: تعلّم كيفية تجميع عناصر حقول الجدول المحوري في مجموعات مخصصة ذات أسماء، مثل الفواكه والخضروات، باستخدام DiscreteGroupItem وPivotFieldGroupOptions.getDiscreteGroupItems() في Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, الجدول المحوري, التجميع المنفصل, DiscreteGroupItem, PivotFieldGroupOptions, تجميع عناصر الجدول المحوري, مجموعات مخصصة, PivotField.group, Aspose.Cells for Node.js via Java, Excel الجدول المحوري
type: docs
weight: 90
url: /ar/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يجمع التجميع التلقائي العناصر حسب نوع البيانات، مثل تجميع التواريخ في أشهر وأرباع أو الأرقام في نطاقات. ويعالج التجميع المنفصل المشكلة المعاكسة، إذ يجمع عناصر محددة وغير مترابطة في مجموعات مخصصة ذات أسماء، مثل تجميع المنتجات في فواكه وخضروات، والمتاجر في مناطق، والحسابات في نطاقات. يوفر Aspose.Cells التجميع المنفصل من خلال فئة `DiscreteGroupItem` والخاصية `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- يمثل `DiscreteGroupItem` اسم مجموعة مع العناصر التي تنتمي إليها. ويمكن تحديد العناصر بإحدى طريقتين: بأسمائها (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) أو بمواضعها ذات الترقيم الصفري في بيانات المصدر (`new DiscreteGroupItem("fruit", [0, 3])`). وتنتج الصيغتان النتيجة نفسها.
- يُطبَّق التجميع المنفصل على حقل في منطقة الصفوف أو الأعمدة في الجدول المحوري بتمرير الخيارات إلى `PivotField.group(PivotFieldGroupOptions)`.

## **تجميع عناصر حقول الجدول المحوري حسب أسماء العناصر**
يبني المثال التالي قائمة مبيعات صغيرة (المنتج والتاريخ والمبلغ)، وينشئ منها جدولاً محوريًا يضع `product` في منطقة الصفوف و`date` في منطقة الأعمدة و`amount` في منطقة البيانات، ثم يحدد مجموعتين مخصصتين حسب أسماء العناصر: الفواكه (عنب، كرز) والخضروات (جزر، بطاطس). تعرض النتيجة تخطيطًا للصفوف من مستويين، حيث يظهر اسم المجموعة في المستوى الخارجي، وتظهر العناصر الأصلية مدرجة تحته، بحيث يمكن قراءة الاتجاهات لكل مجموعة مخصصة ولكل عنصر.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

بعد `calculateData()`، تعرض منطقة الصفوف في الجدول المحوري الفاكهة (عنب 50، كرز 80) والخضروات (جزر 60، بطاطس 70)، مع الإجمالي الكلي 260، بينما تحتفظ تسميات الأعمدة بالتواريخ الأربعة (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **تجميع عناصر حقول الجدول المحوري حسب فهارس العناصر**
عندما تكون أسماء العناصر طويلة أو مُعرَّبة، يحدد المُنشئ الثاني لـ `DiscreteGroupItem` العناصر حسب الفهرس. تمثل الفهارس مواضع العناصر ذات الترقيم الصفري وفق ترتيب ظهورها في بيانات المصدر، لا وفق الترتيب الأبجدي. في بيانات العينة أعلاه، يُعد العنب العنصر 0، والجزر العنصر 1، والبطاطس العنصر 2، والكرز العنصر 3؛ لذلك تكون الفواكه `{ 0, 3 }` والخضروات `{ 1, 2 }`. والنتيجة مطابقة لمثال التجميع حسب الأسماء.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **ملاحظة**

{{% alert color="primary" %}}
- لا تفقد العناصر التي لم تُسنَد إلى أي مجموعة مخصصة. وتبقى في الجدول المحوري على المستوى نفسه الذي تقع فيه المجموعات المخصصة، إذ يُعرض كل عنصر كإدخال مستقل يتكون من عنصر واحد. في المثال أعلاه، يؤدي تحديد مجموعة الفواكه فقط إلى بقاء الجزر والبطاطس في منطقة الصفوف كإدخالين مستقلين بجوار مجموعة الفواكه.
- تتحكم الخاصية `PivotFieldGroupOptions.getNewPivotField()` في تخطيط التجميع المنفصل. وقيمتها الافتراضية هي true، ما ينشئ الحقل المجمَّع كحقل جديد في المستوى الخارجي بجوار الحقل الأصلي، وينتج التخطيط من مستويين كما هو ظاهر أعلاه (`getRowFields()` يزداد عدد عناصره إلى 2). اضبطها على false باستخدام `PivotFieldGroupOptions.setNewPivotField(false)` لاستبدال الحقل الأصلي بدلًا من ذلك؛ عندئذ، تعرض منطقة الصفوف مستوى واحدًا لا يحتوي إلا على أسماء المجموعات وقيمها المجمعة: الفاكهة 130 (50 + 80) والخضروات 130 (60 + 70).
- يمكن استخدام مُنشئ `DiscreteGroupItem` القائم على الاسم ومُنشئه القائم على الفهرس معًا داخل المصفوفة `getDiscreteGroupItems()` نفسها.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري في الجدول المحوري](/cells/ar/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/nodejs-java/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/nodejs-java/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}