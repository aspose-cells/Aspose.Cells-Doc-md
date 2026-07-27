---
title: Aspose.Cells for .NET'te PivotTable değer alanlarını yönetme
linktitle: Değer Alanları
description: Aspose.Cells for Node.js via Java'da bir pivot tablonun veri bölgesine temel alanların nasıl ekleneceğini, PivotField.Function ile özet fonksiyonunun nasıl değiştirileceğini ve değer alanının Satır veya Sütun eksenine nasıl yerleştirileceğini öğrenin.
keywords: Aspose.Cells, Node.js via Java, pivot tablo, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /tr/nodejs-java/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Veri Bölgesine Alan Ekleme
Temel bir alanı veri (değer) bölgesine eklemek, pivot tablonun kaynak verilerinizi nasıl topladığını şekillendirmedeki ilk adımdır. Aspose.Cells, `PivotFieldType.DATA` sabitini ve kaynak sütun adını kabul eden `PivotTable.addFieldToArea(PivotFieldType, string)` aşırı yüklemesini sunar. Bir alan veri bölgesine eklendikten sonra, API bunu alanların eklendiği sırayla `PivotTable.getDataFields()` koleksiyonu aracılığıyla sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.SUM` ile özetlenirken, sayısal olmayan bir sütun `COUNT` varsayılan değerini alır.
## Özet Fonksiyonunu Değiştirme
Veri bölgesine yerleştirilen her alan dahili olarak bir `PivotField` örneği olarak sarılır ve `getFunction()` özelliği `ConsolidationFunction` enum'undan bir değer döndürür. Aynı `setFunction()` ayarlayıcısı, `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` ve `VARP` dahil olmak üzere kullanılabilir toplamlar arasında geçiş yapmanızı sağlar.
{{% alert color="primary" %}}
`Function` özelliğini değiştirmek yalnızca toplamı etkiler; kaynak sütun değişmez.
{{% /alert %}}
Bu nedenle, bir veri alanını `SUM` olarak bırakırken aynı kaynak sütunu hedefleyen ancak `COUNT` veya `AVERAGE` kullanan ikinci bir veri alanını tek bir pivot içinde ekleyebilirsiniz.
## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
Bir pivot tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.getValuesField()` adlı ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Onu bir temel pivot alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz; bu, birden fazla ölçümü yan yana düzenlemek için kullanışlıdır.
{{% alert color="primary" %}}
Herhangi bir değer alanı yoksa veya yalnızca bir tane varsa `PivotTable.getValuesField()` çalışmaz.
{{% /alert %}}
Aşağıdaki senaryolar, yukarıda açıklanan her bir yeteneği aynı pivot yapısı üzerinde gösteren üç uçtan uca örneği ele almaktadır.
## Senaryo 1 — Temel Bir Alanı Değer Bölgesine Sürükleme
Bu senaryo, mevcut bir pivot tablonun veri bölgesine tek bir temel alanın (`Amount`) nasıl yerleştirileceğini gösterir. Paylaşılan pivot yapısı, `Category` ve `Item` alanlarını Satır eksenine, `Year` alanını ise Sütun eksenine yerleştirir. İşlem sonrasında `Amount` veri bölgesinde görünür ve varsayılan olarak `Sum of Amount` olarak hesaplanır.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Başlıklar A1:D1'de
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Veri satırları A2:D9, j'ye göre dallanan iç içe döngüler kullanılarak
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// F3'e PivotTable1 adında pivot tablo ekle
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot düzeni: Satırda Kategori ve Öğe, Sütunda Yıl, veri alanı olarak Tutar
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## Senaryo 2 — Özet Fonksiyonunu Değiştirme
Bu senaryo, Senaryo 1'deki aynı pivot yapısından başlar, ancak `Amount` alanını veri bölgesine iki kez ekler. Her iki veri alanı da aynı kaynak sütuna başvurur, ancak ikinci alan `PivotField.setFunction()` ayarlayıcısı kullanılarak varsayılan `SUM` yerine `COUNT` olacak şekilde geçersiz kılınır.
## Senaryo 3 — Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
İki veri alanı yerinde olduğunda `PivotTable.getValuesField()` kullanılabilir hale gelir. Bu senaryo, bu toplam sanal alanını Sütun bölgesine sürükler, böylece veri bölgesindeki her ölçüm `Year` alanının yanında kendi sütun bloğu olarak görünür.
Bir araya getirildiğinde, bu üç senaryo Aspose.Cells for Node.js via Java'da değer alanı yönetiminin her yönünü kapsar; varsayılan `SUM` ile tek bir veri alanından, sanal `ValuesField`'ın Satır veya Sütun eksenindeki düzeni kontrol ettiği çok ölçümlü bir pivota kadar uzanır.
## İlgili Makaleler
- [Aspose.Cells for Node.js via Java'da Pivot Tablo Satır ve Sütun Alanları](/cells/tr/nodejs-java/row-and-column-fields/)
- [Pivot Tablolarda Sayfa Alanları](/cells/tr/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java'da Pivot Tabloları Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)
- [Pivot Tablolarına Stiller Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}
