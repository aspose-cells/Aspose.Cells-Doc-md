---
title: إدارة حقول قيم الجداول المحورية في Aspose.Cells for .Net
linktitle: إدارة حقول قيم الجداول المحورية في Aspose.Cells for .Net
description: تعلم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في جدول محوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيم على محور الصف أو العمود في Aspose.Cells for .Net.
keywords: Aspose.Cells, .NET, جدول محوري, حقل القيم, PivotField, PivotField.Function, حقل البيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تعد إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تحديد كيفية تجميع بيانات المصدر في الجدول المحوري. يتيح Aspose.Cells استدعاء `PivotTable.AddFieldToArea(PivotFieldType, string)`، وهي طريقة محمّلة بشكل زائد تقبل الثابت `PivotFieldType.Data` واسم عمود المصدر. وبمجرد إضافة حقل إلى منطقة البيانات، تتيح واجهة API الوصول إليه من خلال مجموعة `PivotTable.DataFields`، وفق ترتيب إضافة الحقول. افتراضيًا، يُلخّص عمود المصدر الرقمي باستخدام `ConsolidationFunction.Sum`، بينما تُستخدم الدالة `Count` للأعمدة غير الرقمية.

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:D9", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```

## تغيير دالة التلخيص
عند وجود الحقل في منطقة البيانات، تتيح Aspose.Cells الوصول إليه من خلال كائن `PivotField` في `PivotTable.DataFields`. يحتوي كل كائن `PivotField` على خاصية `Function` قابلة للكتابة من النوع `ConsolidationFunction`، وهي تتحكم في التجميع المطبَّق على القيم المصدرية للحقل. يُعد `ConsolidationFunction` نوع تعداد يحتوي على الأعضاء `Sum` و`Count` و`Average` و`Max` و`Min` و`Product` و`StdDev` و`StdDevp` و`Var` و`Varp`. يغطي الأعضاء الستة الأولى الغالبية العظمى من حالات الاستخدام الواقعية، بينما تمثل الأعضاء الأربعة الأخيرة تجميعات إحصائية مفيدة في تحليل التباين.

{{% alert color="primary" %}}
لا يؤثر تغيير `Function` إلا على التجميع؛ إذ يبقى عمود المصدر وبنية الصفوف والأعمدة في الجدول المحوري دون تغيير. لتغيير التجميع لحقل بيانات موجود، اضبط `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` ثم استدعِ `pivotTable.CalculateData()` لإعادة عرض الجدول المحوري.
{{% /alert %}}

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:D9", 2, 5);
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

## رسم حقول القيم على محور الصف أو العمود
عندما يحتوي الجدول المحوري على حقلين أو أكثر من حقول البيانات، يعرض Aspose.Cells حقلًا ظاهريًا إضافيًا يُسمى `PivotTable.ValuesField`. يمثل هذا الحقل الظاهري تجميع جميع حقول البيانات الموجودة في منطقة البيانات. يمكنك سحبه إلى منطقة الصف أو العمود كحقل أساسي في الجدول المحوري، وهو مفيد لتخطيط مقاييس متعددة جنبًا إلى جنب.

{{% alert color="primary" %}}
لا يعمل `PivotTable.ValuesField` إذا لم يوجد حقل قيم أو إذا كان عدد حقول القيم واحدًا فقط.
{{% /alert %}}

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
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:D9", 2, 5);
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