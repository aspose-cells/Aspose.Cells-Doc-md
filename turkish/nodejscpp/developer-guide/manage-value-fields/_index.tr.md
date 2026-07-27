---
title: Aspose.Cells for Node.js via C++'da Değer Alanları
linktitle: Aspose.Cells for Node.js via C++'da Değer Alanları
description: Aspose.Cells for Node.js via C++'da pivot tablonun veri bölgesine temel alanların nasıl ekleneceğini, PivotField.Function ile özet fonksiyonunun nasıl değiştirileceğini ve değer alanının Satır veya Sütun eksenine nasıl yerleştirileceğini öğrenin.
keywords: Aspose.Cells, Node.js, C++, pivot tablo, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /tr/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Değer alanları, her pivot tablonun kalbidir; kaynak verileri özetleyen sayısal toplamlardır. Aspose.Cells for Node.js via C++'da pivot tablonun veri bölgesi, `PivotTable.addFieldToArea` aracılığıyla temel alanlar eklenerek doldurulur ve bu bölgeye yerleştirilen her alanın kendi özet fonksiyonu olabilir. İki veya daha fazla veri alanı mevcut olduğunda, Aspose.Cells özel bir toplam alanı olan `PivotTable.ValuesField`'ı kullanıma sunar; bu alan bir temel alan olarak Satır veya Sütun eksenine yerleştirilebilir ve böylece değer alanlarının düzende nasıl görüneceği üzerinde daha ayrıntılı kontrol sağlar.

## Veri Bölgesine Alan Ekleme

Veri (değer) bölgesine bir temel alan eklemek, pivot tablonun kaynak verilerinizi nasıl toplayacağını şekillendirmedeki ilk adımdır. Aspose.Cells, `PivotFieldType.Data` sabitini ve kaynak sütun adını kabul eden bir aşırı yükleme olan `PivotTable.addFieldToArea(PivotFieldType, string)` metodunu kullanıma sunar. Bir alan veri bölgesine eklendikten sonra API, alanları `PivotTable.DataFields` koleksiyonu aracılığıyla, alanların eklendiği sırayla sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.Sum` ile özetlenirken, sayısal olmayan bir sütun varsayılan olarak `Count` kullanır.

## Özet Fonksiyonunu Değiştirme

Veri bölgesine yerleştirilen her alan dahili olarak bir `PivotField` örneği olarak sarılır ve `Function` özelliği `ConsolidationFunction` enum'undan bir değer döndürür. Aynı `Function` ayarlayıcısı, `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` ve `Varp` dahil olmak üzere kullanılabilir toplamlar arasında geçiş yapmanıza olanak tanır.

{{% alert color="primary" %}}
`Function`'ı değiştirmek yalnızca toplamı etkiler; kaynak sütun değişmez.
{{% alert %}}

Bu nedenle tek bir pivot içinde bir veri alanını `Sum` olarak bırakırken, aynı kaynak sütunu hedefleyen ancak `Count` veya `Average` kullanan ikinci bir veri alanı ekleyebilirsiniz.

## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme

Bir pivot tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.ValuesField` adında ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Onu temel bir pivot alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz; bu, birden çok ölçütü yan yana düzenlemek için kullanışlıdır.

{{% alert color="primary" %}}
Hiç değer alanı yoksa veya yalnızca bir tane varsa `PivotTable.ValuesField` çalışmaz.
{{% alert %}}

Aşağıdaki senaryolar, yukarıda açıklanan her bir yeteneği aynı pivot yapısı üzerinde gösteren üç uçtan uca örnek üzerinden ilerler.

## Senaryo 1 — Bir Temel Alanı Değer Bölgesine Sürükleme

Bu senaryo, mevcut bir pivot tablonun veri bölgesine tek bir temel alanın (`Amount`) nasıl yerleştirileceğini gösterir. Paylaşılan pivot yapısı, Satır eksenine `Category` ve `Item`, Sütun eksenine ise `Year` alanlarını yerleştirir. İşlemden sonra `Amount` veri bölgesinde görünür ve varsayılan olarak `Sum of Amount` olarak hesaplanır.

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

// j üzerinde dallanma yapan iç içe döngüler kullanılarak A2:D9 veri satırları
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

// Pivot düzeni: Satır olarak Category ve Item, Sütun olarak Year, veri alanı olarak Amount
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Senaryo 2 — Özet Fonksiyonunu Değiştirme

Bu senaryo, Senaryo 1 ile aynı pivot yapısından başlar, ancak `Amount` alanını veri bölgesine iki kez ekler. Her iki veri alanı da aynı kaynak sütuna başvurur; ancak ikinci alan, varsayılan `Sum` yerine `Count` olacak şekilde `PivotField.Function` ayarlayıcısı kullanılarak geçersiz kılınır.

<!-- CODE_BLOCK:1:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice so that pivotTable.getDataFields().getCount() equals 2. Retrieve the second data field via pivotTable.getDataFields().get(1) and assign countField.setFunction(ConsolidationFunction.Count) to change its summary function from the default Sum to Count; the first data field remains Sum of Amount. Demonstrate that the Function setter can also be assigned ConsolidationFunction.Average, Max, Min, etc. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_function.xlsx"). -->

## Senaryo 3 — Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme

İki veri alanı yerinde olduğunda, `PivotTable.ValuesField` kullanılabilir hale gelir. Bu senaryo, bu sanal toplam alanını Sütun bölgesine sürükler; böylece veri bölgesindeki her ölçüt, `Year` alanının yanında kendi sütun bloğu olarak görünür.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

Birlikte ele alındığında, bu üç senaryo Aspose.Cells for Node.js via C++'da değer alanı işlemenin her yönünü kapsar; varsayılan `Sum` ile tek bir veri alanından, sanal `ValuesField`'ın Satır veya Sütun eksenindeki düzeni kontrol ettiği çoklu ölçütlü bir pivota kadar.

## İlgili Makaleler

- [Aspose.Cells for Node.js via C++'da Pivot Tablo Satır ve Sütun Alanları](/cells/tr/nodejs-cpp/row-and-column-fields/)
- [Pivot Tablolarda Sayfa Alanları](/cells/tr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++'da Pivot Tabloları Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/)
- [Pivot Tablolarına Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}