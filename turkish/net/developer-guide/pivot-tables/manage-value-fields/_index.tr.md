---
title: Aspose.Cells for .NET'te PivotTable değer alanlarını yönetme
linktitle: Değer Alanları
description: Aspose.Cells for .NET'te özet tablonun veri bölgesine temel alanların nasıl ekleneceğini, PivotField.Function ile özet fonksiyonunun nasıl değiştirileceğini ve değer alanının Satır veya Sütun eksenine nasıl yerleştirileceğini öğrenin.
keywords: Aspose.Cells, .NET, özet tablo, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /tr/net/pivot-table-manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Veri Bölgesine Alan Ekleme
Veri (değer) bölgesine bir temel alan eklemek, özet tablonun kaynak verilerinizi nasıl toplayacağını şekillendirmenin ilk adımıdır. Aspose.Cells, `PivotFieldType.Data` sabitini ve kaynak-sütun adını kabul eden `PivotTable.AddFieldToArea(PivotFieldType, string)` aşırı yüklemesini kullanıma sunar. Bir alan veri bölgesine eklendikten sonra, API bu alanı `PivotTable.DataFields` koleksiyonu aracılığıyla, alanların eklendiği sırayla sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.Sum` ile özetlenirken, sayısal olmayan bir sütun `Count` ile özetlenir.
## Özet Fonksiyonunu Değiştirme
Veri bölgesine yerleştirilen her alan dahili olarak bir `PivotField` örneği olarak sarılır ve onun `Function` özelliği `ConsolidationFunction` enum'undan bir değer döndürür. Aynı `Function` ayarlayıcısı, `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` ve `Varp` dahil olmak üzere kullanılabilir toplamlar arasında geçiş yapmanızı sağlar.
{{% alert color="primary" %}}
`Function`'ı değiştirmek yalnızca toplamı etkiler, kaynak sütun değişmez.
{{% /alert %}}
Bu nedenle, tek bir özet içinde, bir veri alanını `Sum` olarak bırakırken aynı kaynak sütunu hedefleyen ancak `Count` veya `Average` kullanan ikinci bir veri alanı ekleyebilirsiniz.
## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
Bir özet tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.ValuesField` adlı ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Onu Satır veya Sütun bölgesine temel bir özet alanı olarak sürükleyebilirsiniz; bu, birden çok ölçümü yan yana düzenlemek için kullanışlıdır.
{{% alert color="primary" %}}
`PivotTable.ValuesField`, hiç değer alanı yoksa veya yalnızca bir değer alanı varsa çalışmaz.
{{% /alert %}}
Aşağıdaki senaryolar, yukarıda açıklanan her bir yeteneği aynı özet yapısı üzerinde gösteren uçtan uca üç örnek üzerinden ilerler.
## Senaryo 1 — Temel Bir Alanı Değer Bölgesine Sürükleme
Bu senaryo, tek bir temel alanın (`Amount`) mevcut bir özet tablonun veri bölgesine nasıl yerleştirileceğini gösterir. Paylaşılan özet yapısı, `Category` ve `Item` alanlarını Satır eksenine, `Year` alanını ise Sütun eksenine yerleştirir. İşlemden sonra, `Amount` veri bölgesinde görünür ve varsayılan olarak `Amount` değerinin `Sum` olarak hesaplanır.
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// A1:D1 aralığında başlıklar
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

// j değişkenine göre dallanan iç içe döngüler kullanarak A2:D9 veri satırları
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

// F3 hücresine PivotTable1 adında bir pivot tablo ekle
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Pivot düzeni: Satırda Category ve Item, Sütunda Year, veri alanı olarak Amount
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```
## Senaryo 2 — Özet Fonksiyonunu Değiştirme
Bu senaryo, Senaryo 1 ile aynı özet yapısından başlar, ancak `Amount` alanını veri bölgesine iki kez ekler. Her iki veri alanı da aynı kaynak sütuna başvurur; ancak ikinci alan, `PivotField.Function` ayarlayıcısı kullanılarak varsayılan `Sum` yerine `Count` olacak şekilde geçersiz kılınır.
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
## Senaryo 3 — Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
İki veri alanı yerinde olduğunda, `PivotTable.ValuesField` kullanılabilir hale gelir. Bu senaryo, bu toplam sanal alanını Sütun bölgesine sürükler, böylece veri bölgesindeki her ölçüm `Year` alanının yanında kendi sütun bloku olarak görünür.
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
Birlikte ele alındığında, bu üç senaryo Aspose.Cells for .NET'te değer alanı manipülasyonunun tüm yönlerini kapsar; varsayılan `Sum` ile tek bir veri alanından, sanal `ValuesField`'ın Satır veya Sütun eksenindeki düzeni kontrol ettiği çok ölçümlü bir özet tabloya kadar.

{{< app/cells/assistant language="csharp" >}}
