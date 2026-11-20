---
title: التجميع المتقطع لعناصر حقول الجدول المحوري
description: تعلم كيفية تجميع عناصر حقول الجدول المحوري في مجموعات مخصصة ذات أسماء مثل الفواكه والخضروات باستخدام DiscreteGroupItem وPivotFieldGroupOptions.DiscreteGroupItems في Aspose.Cells for .NET.
linktitle: التجميع المتقطع
keywords: Aspose.Cells, جدول محوري, تجميع متقطع, DiscreteGroupItem, PivotFieldGroupOptions, تجميع عناصر الحقل المحوري, مجموعات مخصصة, PivotField.Group, C#, Excel جدول محوري
type: docs
weight: 90
url: /ar/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يجمع التجميع التلقائي العناصر حسب نوع البيانات، مثل تواريخ في أشهر وربعيات أو أرقام في نطاقات. يعالج التجميع المتقطع المشكلة المعاكسة، إذ يجمع عناصر محددة وغير مترابطة في مجموعات مخصصة ذات أسماء، مثل تصنيف المنتجات في فئتي الفواكه والخضروات، أو المتاجر حسب المناطق، أو الحسابات حسب النطاقات الجغرافية. توفر Aspose.Cells التجميع المتقطع عبر فئة `DiscreteGroupItem` والخاصية `PivotFieldGroupOptions.DiscreteGroupItems`.
- يمثل `DiscreteGroupItem` اسم مجموعة مع العناصر المنتمية إليها. يمكن التعرف على العناصر بطريقتين، إما من خلال أسمائها (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) أو من خلال مواضعها التي يبدأ العد فيها من الصفر في بيانات المصدر (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). وينتج عن الصيغتين النتيجة نفسها.
- يُطبق التجميع المتقطع على حقل في منطقة الصفوف أو الأعمدة من الجدول المحوري عن طريق تمرير الخيارات إلى `PivotField.Group(PivotFieldGroupOptions)`.

## **تجميع عناصر حقول الجدول المحوري حسب أسماء العناصر**
يبني المثال التالي قائمة مبيعات صغيرة تتكون من المنتج والتاريخ والمبلغ، وينشئ منها جدولًا محوريًا يضع المنتج في منطقة الصفوف والتاريخ في منطقة الأعمدة والمبلغ في منطقة البيانات، ثم يحدد مجموعتين مخصصتين حسب أسماء العناصر: الفواكه (العنب والكرز) والخضروات (الجزر والبطاطس). وتوضح النتيجة بنية صف ذات مستويين، حيث تظهر أسماء المجموعات في المستوى الخارجي وتُدرج العناصر الأصلية تحتها، مما يتيح قراءة الاتجاهات لكل مجموعة مخصصة وكل عنصر.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

بعد `CalculateData()`، تعرض منطقة الصفوف في الجدول المحوري الفواكه (العنب 50، الكرز 80) والخضروات (الجزر 60، البطاطس 70) مع الإجمالي الكلي 260، وتحتفظ تسميات الأعمدة بالتواريخ الأربعة (2/5/2021، 3/8/2022، 4/10/2023، 5/16/2024).

## **تجميع عناصر حقول الجدول المحوري حسب فهارس العناصر**
عندما تكون أسماء العناصر طويلة أو خاصة بلغة محلية، يحدد المُنشئ الثاني لـ `DiscreteGroupItem` العناصر حسب الفهرس. تكون الفهارس مواضع العناصر التي يبدأ العد فيها من الصفر وفق ترتيب ظهورها في بيانات المصدر، وليست حسب الترتيب الأبجدي. في بيانات العينة أعلاه، يمثل العنب العنصر 0، والجزر العنصر 1، والبطاطس العنصر 2، والكرز العنصر 3؛ لذلك تكون مجموعة الفواكه `{ 0, 3 }` ومجموعة الخضروات `{ 1, 2 }`. والنتيجة مطابقة لمثال التجميع حسب الأسماء.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **ملاحظة**

{{% alert color="primary" %}}
- لا تضيع العناصر غير المخصصة لأي مجموعة مخصصة. تظل في الجدول المحوري عند المستوى نفسه الذي توجد فيه المجموعات المخصصة، ويظهر كل منها كعنصر مستقل. في المثال أعلاه، يؤدي تحديد مجموعة الفواكه فقط إلى بقاء الجزر والبطاطس في منطقة الصفوف كعناصر مستقلة بجوار مجموعة الفواكه.
- تتحكم الخاصية `PivotFieldGroupOptions.NewPivotField` في تخطيط التجميع المتقطع. قيمتها الافتراضية هي `true`، مما يضيف الحقل المجمَّع كحقل خارجي جديد بجوار الحقل الأصلي وينتج تخطيطًا ذي مستويين كما هو موضح أعلاه (يزداد عدد عناصر `RowFields` إلى 2). اضبطها على `false` لاستبدال الحقل الأصلي بدلاً من ذلك، عندئذ تعرض منطقة الصفوف مستوى واحدًا يحتوي فقط على أسماء المجموعات وقيمها المجمعة: الفواكه 130 (50 + 80) والخضروات 130 (60 + 70).
- يمكن خلط المُنشئين المعتمدين على الاسم والفهرس لـ `DiscreteGroupItem` ضمن المصفوفة `DiscreteGroupItems` نفسها.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري في جدول محوري](/cells/ar/net/group-pivot-fields-in-the-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/net/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/net/filter-by-label-or-value-of-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/net/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}