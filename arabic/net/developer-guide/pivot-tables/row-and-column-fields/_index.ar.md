---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: حقول الصفوف والأعمدة
description: تعلم كيفية إضافة الحقول الأساسية إلى مناطق الصفوف والأعمدة في الجدول المحوري والتحكم في الإجماليات الفرعية لـ PivotField باستخدام PivotField.SetSubtotals مع PivotFieldSubtotalType في Aspose.Cells لـ .NET
keywords: Aspose.Cells, .NET, PivotTable, جدول محوري, حقل صف, حقل عمود, PivotField, SetSubtotals, PivotFieldSubtotalType, الإجماليات الفرعية, C#, Excel pivot table
type: docs
weight: 220
url: /ar/net/pivot-table-add-row-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**

تنقل طريقة `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` حقلًا أساسيًا من البيانات المصدر إلى إحدى مناطق المحور الأربع. تقبل وسيطة `fieldType` إحدى قيم `PivotFieldType` التالية.

- `Row` — الحقول الموضوعة عموديًا على اليسار
- `Column` — الحقول الموضوعة أفقيًا عبر الأعلى
- `Data` — الحقول التي يتم تجميع قيمها
- `Page` — الحقول المستخدمة كمرشحات تقارير

بعد إضافة الحقول، يمكنك الوصول إليها من خلال خصائص `PivotTable.RowFields` و`PivotTable.ColumnFields`. تُرجع كل خاصية `PivotFieldCollection`. الحقل عند الفهرس 0 من `RowFields` هو حقل الصف الأبعد، وتمثل الفهارس اللاحقة الحقول المتداخلة داخله. ينطبق نفس اصطلاح الفهرسة على `ColumnFields`.

يهم ترتيب تداخل الحقول. إضافة `Category` إلى منطقة الصفوف أولًا ثم `Item` ينتج محورًا يكون فيه التجميع الخارجي `Category` والتجميع الداخلي `Item`. يؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **الإجماليات الفرعية لحقول المحور**

تتحكم طريقة `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` في صفوف الإجمالي الفرعي التي تظهر لحقل محور. كل استدعاء يبدل نوع إجمالي فرعي واحدًا بشكل مستقل. تمرير `shown = true` يعرض الإجمالي الفرعي، بينما يخفيه `shown = false`. نظرًا لأن كل استدعاء يؤثر على نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم `subtotalType` مختلفة يُنشئ مجموعة فرعية مخصصة من الإجماليات الفرعية.

يحدد التعداد `PivotFieldSubtotalType` أنواع الإجماليات الفرعية المتاحة.

- `Automatic` — يختار Aspose.Cells التحديد الافتراضي (عادةً `Sum` للحقول الرقمية)
- `None` — إلغاء جميع صفوف الإجمالي الفرعي
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
لا تظهر الإجماليات الفرعية إلا عند وجود حقلين محوريين أو أكثر في منطقة الصفوف (أو في منطقة الأعمدة). الحقل الواحد لا يوجد شيء ذو معنى لحساب إجمالي فرعي بينه، لذلك لا يكون لاستدعاءات `SetSubtotals` أي تأثير مرئي في تلك الحالة. لذلك تضع هذه المقالة حقلين من حقول الصفوف (`Category` خارجي، `Item` داخلي) في كل مثال بحيث يكون حد الإجمالي الفرعي بين كل مجموعة `Category` مرئيًا.
{{% /alert %}}

## **السيناريو 1 — الإجماليات الفرعية التلقائية (الافتراضية)**

عندما لا تستدعي `SetSubtotals` على الإطلاق، يطبق Aspose.Cells تحديد `Automatic` على الحقول الرقمية. يؤكد المثال التالي هذا السلوك صراحةً باستدعاء `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` على حقل الصف الخارجي `Category`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);

pivotTable.CalculateData();

workbook.Save("output_automatic.xlsx");
```

## **السيناريو 2 — إلغاء جميع الإجماليات الفرعية (None)**

يُزيل استدعاء `SetSubtotals(PivotFieldSubtotalType.None, true)` كل صف إجمالي فرعي من المحور، تاركًا فقط صفوف الحقول والإجمالي الكلي في الأسفل. يكون ذلك مفيدًا عندما تريد البيانات المجمعة الأولية دون أي صفوف ملخص.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}

object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.CalculateData();

workbook.Save("output_none.xlsx");
```

## **السيناريو 3 — مجموعة الإجماليات الفرعية المخصصة (Sum + Average)**

لست مقيدًا بنوع إجمالي فرعي واحد. يعمل كل استدعاء `SetSubtotals` بشكل مستقل على نوع واحد، لذلك فإن استدعاء الطريقة مرتين — مرة بـ `Sum` ومرة بـ `Average` — ينتج مجموعة فرعية مخصصة من صفّي إجمالي فرعي لكل مجموعة `Category`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);

pivotTable.CalculateData();

workbook.Save("output_custom.xlsx");
```

## **ملخص**

تتشارك السيناريوهات الثلاثة أعلاه في نفس مجموعة البيانات وبنية الجدول المحوري. الفرق الوحيد بينها هو استدعاء `SetSubtotals` المطبق على حقل الصف الخارجي `Category`. تذكر قاعدة الحقلين: الحقل الواحد في المنطقة لا يوجد شيء ذو معنى لحساب إجمالي فرعي بينه، لذلك ضع دائمًا حقلين على الأقل في منطقة الصفوف أو الأعمدة عندما تريد أن يكون لاستدعاء `SetSubtotals` تأثير مرئي.

## **مقالات ذات صلة**

- [حقول الصفحات في الجداول المحورية](/cells/ar/net/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for .NET](/cells/ar/net/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
