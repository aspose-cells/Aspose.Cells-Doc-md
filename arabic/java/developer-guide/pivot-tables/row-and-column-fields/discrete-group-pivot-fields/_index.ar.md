---
title: التجميع المنفصل لعناصر حقول الجدول المحوري
linktitle: التجميع المنفصل
description: تعرّف على كيفية تجميع عناصر حقول الجدول المحوري في مجموعات مخصصة ذات أسماء مثل الفواكه والخضروات باستخدام DiscreteGroupItem وPivotFieldGroupOptions.DiscreteGroupItems في Aspose.Cells for Java.
keywords: Aspose.Cells for Java, جدول محوري, تجميع منفصل, DiscreteGroupItem, PivotFieldGroupOptions, تجميع عناصر الحقل المحوري, مجموعات مخصصة, PivotField.group, Java, Excel جدول محوري
type: docs
weight: 90
url: /ar/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يجمع التجميع التلقائي العناصر حسب نوع البيانات، مثل تجميع التواريخ في الشهور والأرباع أو الأرقام في نطاقات. يعالج التجميع المنفصل المشكلة المعاكسة، إذ يجمع عناصر محددة وغير مترابطة في مجموعات مخصصة ذات أسماء، مثل تجميع المنتجات في الفواكه والخضروات، والمتاجر في المناطق، والحسابات في النطاقات. يوفر Aspose.Cells التجميع المنفصل من خلال صنف `DiscreteGroupItem` والخاصية `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- يتكون `DiscreteGroupItem` من اسم المجموعة والعناصر التي تنتمي إليها. يمكن تحديد العناصر بإحدى طريقتين: بأسمائها (`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`) أو حسب مواضعها ذات الفهرس الصفري في بيانات المصدر (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). تُنتج كلتا الطريقتين النتيجة نفسها.
- يُطبَّق التجميع المنفصل على حقل في منطقة الصفوف أو الأعمدة في الجدول المحوري، ويتم ذلك بتمرير الخيارات إلى `PivotField.group(PivotFieldGroupOptions)`.

## **تجميع عناصر حقول الجدول المحوري حسب أسماء العناصر**
ينشئ المثال التالي قائمة مبيعات صغيرة (المنتج والتاريخ والمبلغ)، وينشئ جدولًا محوريًا منها مع وضع `product` في منطقة الصفوف، و`date` في منطقة الأعمدة، و`amount` في منطقة البيانات. ثم يعرّف مجموعتين مخصصتين حسب أسماء العناصر: `fruit` (`grape` و`cherry`) و`vegetables` (`carrot` و`potato`). تعرض النتيجة تخطيطًا من مستويين للصفوف، إذ يظهر اسم المجموعة في المستوى الخارجي وتُدرج العناصر الأصلية تحته، مما يتيح قراءة الاتجاهات لكل مجموعة مخصصة ولكل عنصر.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

بعد `calculateData()`، تعرض منطقة الصفوف في الجدول المحوري `fruit` (`grape` 50، `cherry` 80) و`vegetable` (`carrot` 60، `potato` 70)، مع الإجمالي الكلي 260، وتبقى تسميات الأعمدة هي التواريخ الأربعة (2/5/2021، 3/8/2022، 4/10/2023، 5/16/2024).

## **تجميع عناصر حقول الجدول المحوري حسب فهارس العناصر**
عند طول أسماء العناصر أو توطينها، يحدد المُنشئ الثاني لـ `DiscreteGroupItem` العناصر حسب الفهرس. تمثل الفهارس مواضع العناصر ذات الترقيم الصفري وفق ترتيب ظهورها في بيانات المصدر، ولا تتبع الترتيب الأبجدي. في بيانات العينة أعلاه، يمثل `grape` العنصر 0، و`carrot` العنصر 1، و`potato` العنصر 2، و`cherry` العنصر 3، لذا تكون مجموعة `fruit` هي `{ 0, 3 }` ومجموعة `vegetable` هي `{ 1, 2 }`. النتيجة مطابقة لمثال التجميع حسب الاسم.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **ملاحظة**

{{% alert color="primary" %}}
- لا تضيع العناصر غير المخصصة لأي مجموعة مخصصة. وتبقى في الجدول المحوري على المستوى نفسه الموجود عليه المجموعات المخصصة، ويمثل كل عنصر منها مدخلًا مستقلًا من عنصر واحد. في المثال أعلاه، يؤدي تعريف مجموعة `fruit` فقط إلى إبقاء `carrot` و`potato` في منطقة الصفوف كمدخلين مستقلين إلى جانب مجموعة `fruit`.
- تتحكم الخاصية `PivotFieldGroupOptions.getNewPivotField()` في تخطيط التجميع المنفصل. القيمة الافتراضية هي `true`، ويُضيف ذلك الحقل المجمَّع كحقل خارجي جديد إلى جانب الحقل الأصلي، فينتج تخطيط من مستويين كما هو معروض أعلاه (يزداد عدد حقول `getRowFields()` إلى 2). اضبط الخاصية على `false` باستخدام `setNewPivotField(false)` لاستبدال الحقل الأصلي. عندئذٍ، تعرض منطقة الصفوف مستوى واحدًا يحتوي فقط على أسماء المجموعات وقيمها المجمعة: `fruit` 130 (50 + 80) و`vegetable` 130 (60 + 70).
- يمكن مزج المُنشئين المعتمدين على الاسم والفهرس لـ `DiscreteGroupItem` داخل المصفوفة نفسها المستخدمة مع `getDiscreteGroupItems()`.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري](/cells/ar/java/group-pivot-fields-in-the-pivot-table/)
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/java/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/java/filter-by-label-or-value-of-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/java/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}