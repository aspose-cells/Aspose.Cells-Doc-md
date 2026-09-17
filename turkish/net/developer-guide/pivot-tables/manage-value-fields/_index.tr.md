---
title: Aspose.Cells for .NET'te Pivot Tablosu Değer Alanlarını Yönetme
linktitle: Aspose.Cells for .NET'te Pivot Tablosu Değer Alanlarını Yönetme
description: Aspose.Cells for .NET'te bir pivot tablosunun veri bölgesine temel alanların nasıl ekleneceğini, PivotField.Function ile özetleme işlevinin nasıl değiştirileceğini ve değer alanının Satır veya Sütun eksenine nasıl yerleştirileceğini öğrenin.
keywords: Aspose.Cells, .NET, pivot tablosu, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Toplam, Ortalama
type: docs
weight: 230
url: /tr/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Veri Bölgesine Alan Ekleme
Bir temel alanı veri (değer) bölgesine eklemek, bir pivot tablosunun kaynak verileri nasıl toplayacağını şekillendirmede ilk adımdır. Aspose.Cells, `PivotFieldType.Data` sabitini ve kaynak sütun adını kabul eden bir aşırı yükleme olan `PivotTable.AddFieldToArea(PivotFieldType, string)` metodunu sunar. Bir alan veri bölgesine eklendikten sonra, API onu alanların eklenme sırasına göre `PivotTable.DataFields` koleksiyonu aracılığıyla sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.Sum` ile özetlenirken, sayısal olmayan bir sütun varsayılan olarak `Count` kullanır.

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
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```

## Özetleme İşlevini Değiştirme
Bir alan veri bölgesinde bulunduğunda, Aspose.Cells onu `PivotTable.DataFields` üzerindeki `PivotField` nesnesi aracılığıyla sunar. Her `PivotField`, `ConsolidationFunction` türünde, o alanın temel değerlerine uygulanan toplamı kontrol eden yazılabilir bir `Function` özelliğine sahiptir. `ConsolidationFunction`, `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` ve `Varp` üyelerine sahip bir enum'dur; ilk altısı gerçek dünya kullanım durumlarının büyük çoğunluğunu kapsar, son dördü ise varyans analizi için yararlı istatistiksel toplamlardır.

{{% alert color="primary" %}}
`Function` özelliğinin değiştirilmesi yalnızca toplamı etkiler; kaynak sütun ve pivot'un satır/sütun yapısı değiştirilmez. Mevcut bir veri alanı için toplamı değiştirmek üzere `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` ayarlayın ve ardından pivot'u yeniden oluşturmak için `pivotTable.CalculateData()` çağırın.
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

## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
Bir pivot tablosu iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.ValuesField` adı verilen ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Onu temel bir pivot alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz; bu, birden çok ölçümü yan yana düzenlemek için kullanışlıdır.

{{% alert color="primary" %}}
`PivotTable.ValuesField` hiç değer alanı yoksa veya yalnızca bir değer alanı varsa çalışmaz.
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