---
title: Aspose.Cells for .NET'te PivotTable değer alanlarını yönetme
linktitle: Değer Alanları
description: Aspose.Cells for Node.js via C++ içinde temel alanları pivot tablonun veri bölgesine eklemeyi, PivotField.Function ile özetleme işlevini değiştirmeyi ve değer alanını Satır veya Sütun eksenine yerleştirmeyi öğrenin.
keywords: Aspose.Cells, Node.js via C++, pivot tablo, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /tr/nodejs-cpp/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
Değer alanları her pivot tablonun kalbidir, kaynak verileri özetleyen sayısal toplamlardır. Aspose.Cells for Node.js via C++ içinde, bir pivot tablonun veri bölgesi, `PivotTable.addFieldToArea` aracılığıyla temel alanlar eklenerek doldurulur ve bu bölgeye yerleştirilen her alan kendi özetleme işlevine sahip olabilir. İki veya daha fazla veri alanı olduğunda, Aspose.Cells özel bir toplam alanı olan `PivotTable.getValuesField`'ı sunar; bu alan temel bir alan olarak Satır veya Sütun eksenine yerleştirilebilir ve değer alanlarının düzende nasıl görüneceği üzerinde daha hassas kontrol sağlar.
## Veri Bölgesine Alan Ekleme
Bir temel alanı veri (değer) bölgesine eklemek, pivot tablonun kaynak verilerinizi nasıl topladığını şekillendirmede ilk adımdır. Aspose.Cells, `PivotFieldType.Data` sabitini ve kaynak sütun adını kabul eden `PivotTable.addFieldToArea(PivotFieldType, string)` aşırı yüklemesini sunar. Bir alan veri bölgesine eklendiğinde, API bunu `PivotTable.getDataFields()` koleksiyonu aracılığıyla, alanların eklendiği sırayla sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.Sum` ile özetlenirken, sayısal olmayan bir sütun `Count` varsayılan değerini alır.
## Özetleme İşlevini Değiştirme
Veri bölgesine yerleştirilen her alan dahili olarak bir `PivotField` örneği olarak sarılır ve `getFunction()` özelliği `ConsolidationFunction` enum'undan bir değer döndürür. Aynı `setFunction()` ayarlayıcısı, `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` ve `Varp` dahil mevcut toplamlar arasında geçiş yapmanıza olanak tanır.
{{% alert color="primary" %}}
Özetleme işlevini değiştirmek yalnızca toplamı etkiler, kaynak sütun değişmez.
{{% /alert %}}
Bu nedenle bir veri alanını `Sum` olarak bırakırken, aynı kaynak sütunu hedefleyen ancak `Count` veya `Average` kullanan ikinci bir veri alanını tek bir pivot içinde ekleyebilirsiniz.
## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
Bir pivot tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.getValuesField` adlı ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Birden fazla ölçüyü yan yana düzenlemek için kullanışlı olan bu alanı, temel bir pivot alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz.
{{% alert color="primary" %}}
`PivotTable.getValuesField()`, hiç değer alanı yoksa veya yalnızca bir değer alanı varsa çalışmaz.
{{% /alert %}}
Aşağıdaki senaryolar, yukarıda açıklanan her yeteneği aynı pivot yapısına karşı gösteren üç uçtan uca örnek üzerinden ilerler.
## Senaryo 1 — Bir Temel Alanı Değer Bölgesine Sürükleme
Bu senaryo, tek bir temel alanın (`Amount`) mevcut bir pivot tablonun veri bölgesine nasıl yerleştirileceğini gösterir. Paylaşılan pivot yapısı, `Category` ve `Item` öğelerini Satır eksenine ve `Year` öğesini Sütun eksenine yerleştirir. İşlem tamamlandıktan sonra, `Amount` veri bölgesinde görünür ve varsayılan olarak `Amount` değerinin `Sum` toplamı olarak hesaplanır.
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 aralığındaki başlıklar
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// j üzerinde dallanan iç içe döngüler kullanarak A2:D9 veri satırları
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i === 1 || i === 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i === 3 || i === 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i === 5 || i === 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i === 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i === 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i === 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i === 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i === 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i === 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i === 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// F3 konumuna PivotTable1 adıyla pivot tablo ekle
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot düzeni: Satırda Kategori ve Öğe, Sütunda Yıl, veri alanı olarak Tutar
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## Senaryo 2 — Özetleme İşlevini Değiştirme
Bu senaryo, Senaryo 1 ile aynı pivot yapısından başlar ancak `Amount` alanını veri bölgesine iki kez ekler. Her iki veri alanı da aynı kaynak sütuna başvurur, ancak ikinci alan `setFunction()` ayarlayıcısı kullanılarak geçersiz kılınır ve varsayılan `Sum` yerine `Count` olur.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
 worksheet.getCells().get(i, j).putValue(items[i - 1]);
 }
 else if (j == 2)
 {
 let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
 worksheet.getCells().get(i, j).putValue(years[i - 1]);
 }
 else
 {
 let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
 worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```
## Senaryo 3 — Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
İki veri alanı yerinde olduğunda, `PivotTable.getValuesField()` kullanılabilir hale gelir. Bu senaryo, toplam sanal alanını Sütun bölgesine sürükler; böylece veri bölgesindeki her ölçü, `Year` öğesinin yanında kendi sütun bloğu olarak görünür.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

let categories = ["Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable"];
let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
let amounts = [100, 150, 80, 90, 50, 60, 40, 45];

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.getCells().get(i, j).putValue(categories[i - 1]);
 else if (j == 1) worksheet.getCells().get(i, j).putValue(items[i - 1]);
 else if (j == 2) worksheet.getCells().get(i, j).putValue(years[i - 1]);
 else worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField().getName());

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```
Bu üç senaryo birlikte, varsayılan `Sum` ile tek bir veri alanından, sanal `ValuesField`'ın Satır veya Sütun eksenindeki düzeni kontrol ettiği çoklu ölçülü bir pivota kadar Aspose.Cells for Node.js via C++ içinde değer alanı manipülasyonunun her yönünü kapsar.
## İlgili Makaleler
- [Pivot Tablo Satır ve Sütun Alanları in Aspose.Cells for Node.js via C++](/cells/tr/nodejs-cpp/row-and-column-fields/)
- [Pivot Tablolarda Sayfa Alanları](/cells/tr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++ içinde Pivot Tabloları Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/)
- [Pivot Tablolarına Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}