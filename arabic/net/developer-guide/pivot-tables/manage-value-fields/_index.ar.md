---
title: إدارة حقول القيم في الجدول المحوري في Aspose.Cells لـ .NET
linktitle: حقول القيم
description: تعلم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيم على محور الصفوف أو الأعمدة في Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, جدول محوري, حقل القيم, PivotField, PivotField.Function, حقل البيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تُعد إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يعرض Aspose.Cells الدالة `PivotTable.AddFieldToArea(PivotFieldType, string)`، وهي طريقة محملة تقبل الثابت `PivotFieldType.Data` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، تعرضه واجهة برمجة التطبيقات من خلال مجموعة `PivotTable.DataFields`، بالترتيب الذي تمت إضافة الحقول به. بشكل افتراضي، يتم تلخيص عمود المصدر الرقمي باستخدام `ConsolidationFunction.Sum`، بينما يكون عمود المصدر غير الرقمي افتراضيًا `Count`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// العناوين في A1:D1
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

// صفوف البيانات A2:D9 باستخدام حلقات متداخلة تتفرع على j
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.Cells[i, j].PutValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.Cells[i, j].PutValue("Apple");
 else if (i == 3 || i == 4) worksheet.Cells[i, j].PutValue("Banana");
 else if (i == 5 || i == 6) worksheet.Cells[i, j].PutValue("Carrot");
 else worksheet.Cells[i, j].PutValue("Daikon");
 break;
 case 2:
 worksheet.Cells[i, j].PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.Cells[i, j].PutValue(100);
 else if (i == 2) worksheet.Cells[i, j].PutValue(150);
 else if (i == 3) worksheet.Cells[i, j].PutValue(80);
 else if (i == 4) worksheet.Cells[i, j].PutValue(90);
 else if (i == 5) worksheet.Cells[i, j].PutValue(50);
 else if (i == 6) worksheet.Cells[i, j].PutValue(60);
 else if (i == 7) worksheet.Cells[i, j].PutValue(40);
 else worksheet.Cells[i, j].PutValue(45);
 break;
 }
 }
}

// إضافة جدول محوري في F3 باسم PivotTable1
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// تخطيط الجدول المحوري: Category و Item في الصف، Year في العمود، Amount كحقل بيانات
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```

## تغيير دالة التلخيص
يتم تغليف كل حقل موضوع في منطقة البيانات داخليًا كمثيل `PivotField`، وتعيد خاصية `Function` قيمة من تعداد `ConsolidationFunction`. يتيح لك نفس مُعيّن `Function` التبديل بين التجميعات المتاحة، بما في ذلك `Sum` و`Count` و`Average` و`Max` و`Min` و`Product` و`StdDev` و`StdDevp` و`Var` و`Varp`.
{{% alert color="primary" %}}
تغيير `Function` يؤثر فقط على التجميع، ولا يتغير عمود المصدر.
{{% /alert %}}
لذلك يمكنك ترك حقل بيانات واحد كـ `Sum` أثناء إضافة حقل بيانات ثانٍ يستهدف نفس عمود المصدر ولكن يستخدم `Count` أو `Average`، كل ذلك في جدول محوري واحد.

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

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.Cells[i, j].PutValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
 worksheet.Cells[i, j].PutValue(items[i - 1]);
 }
 else if (j == 2)
 {
 int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
 worksheet.Cells[i, j].PutValue(years[i - 1]);
 }
 else
 {
 int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };
 worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");

pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;

pivotTable.CalculateData();

workbook.Save("output_function.xlsx");
```

## رسم حقول القيم على محور الصفوف أو الأعمدة
عندما يحتوي الجدول المحوري على حقلين أو أكثر من حقول البيانات، يعرض Aspose.Cells حقلًا افتراضيًا إضافيًا يسمى `PivotTable.ValuesField`. يمثل هذا الحقل الافتراضي تجميع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة كحقل محوري أساسي، وهو أمر مفيد لعرض مقاييس متعددة جنبًا إلى جنب.
{{% alert color="primary" %}}
`PivotTable.ValuesField` لا يعمل إذا لم يكن هناك حقل قيم أو كان هناك حقل قيم واحد فقط.
{{% /alert %}}
تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة توضح كل قدرة موصوفة أعلاه على نفس بنية الجدول المحوري.

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

string[] categories = { "Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable" };
string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.Cells[i, j].PutValue(categories[i - 1]);
 else if (j == 1) worksheet.Cells[i, j].PutValue(items[i - 1]);
 else if (j == 2) worksheet.Cells[i, j].PutValue(years[i - 1]);
 else worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.DataFields[1].Function = ConsolidationFunction.Count;

pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);

pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```

{{< app/cells/assistant language="csharp" >}}