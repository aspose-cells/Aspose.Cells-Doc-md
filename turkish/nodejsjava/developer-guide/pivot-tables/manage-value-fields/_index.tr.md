---
title: Aspose.Cells for Node.js via Java'da Değer Alanları
linktitle: Aspose.Cells for Node.js via Java'da Değer Alanları
description: Aspose.Cells for Node.js via Java'da bir pivot tablosunun veri bölgesine temel alanların nasıl ekleneceğini, PivotField.Function ile özetleme işlevinin nasıl değiştirileceğini ve değer alanının Satır veya Sütun eksenine nasıl yerleştirileceğini öğrenin.
keywords: Aspose.Cells, Node.js via Java, pivot tablosu, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Toplam, Ortalama
type: docs
weight: 230
url: /tr/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Değer alanları her pivot tablosunun kalbidir; kaynak verileri özetleyen sayısal toplamlardır. Aspose.Cells for Node.js via Java'da bir pivot tablosunun veri bölgesi, `PivotTable.addFieldToArea` aracılığıyla temel alanlar eklenerek doldurulur ve bu bölgeye yerleştirilen her alan kendi özetleme işlevine sahip olabilir. İki veya daha fazla veri alanı mevcut olduğunda, Aspose.Cells özel bir toplam alanı olan `PivotTable.getValuesField()`'ı sunar; bu alan bir temel alan gibi Satır veya Sütun eksenine yerleştirilebilir ve değer alanlarının düzende nasıl görüneceği üzerinde daha ayrıntılı kontrol sağlar.
## Veri Bölgesine Alan Ekleme
Veri (değer) bölgesine bir temel alan eklemek, pivot tablosunun kaynak verilerinizi nasıl toplayacağını şekillendirmede ilk adımdır. Aspose.Cells, `PivotFieldType.DATA` sabitini ve kaynak sütun adını kabul eden bir aşırı yükleme olan `PivotTable.addFieldToArea(PivotFieldType, string)`'ı sunar. Bir alan veri bölgesine eklendikten sonra, API onu alanların eklendiği sırayla `PivotTable.getDataFields()` koleksiyonu aracılığıyla sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.SUM` ile özetlenirken, sayısal olmayan bir sütun varsayılan olarak `COUNT` olur.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Özetleme İşlevini Değiştirme
Veri bölgesine yerleştirilen her alan dahili olarak bir `PivotField` örneği olarak sarılır ve `getFunction()` özelliği `ConsolidationFunction` enum'undan bir değer döndürür. Aynı `setFunction()` ayarlayıcısı, `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` ve `VARP` dahil mevcut toplamlar arasında geçiş yapmanızı sağlar.
{{% alert color="primary" %}}
`Function`'ı değiştirmek yalnızca toplamı etkiler, kaynak sütun değişmez.
{{% /alert %}}
Bu nedenle bir veri alanını `SUM` olarak bırakırken, aynı kaynak sütunu hedefleyen ancak `COUNT` veya `AVERAGE` kullanan ikinci bir veri alanını tek bir pivotta ekleyebilirsiniz.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
Bir pivot tablosu iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.getValuesField()` adlı ek bir sanal alanı sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Bunu bir temel pivot alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz; bu, birden çok ölçüyü yan yana düzenlemek için kullanışlıdır.
{{% alert color="primary" %}}
Hiç değer alanı yoksa veya yalnızca bir değer alanı varsa `PivotTable.getValuesField()` çalışmaz.
{{% /alert %}}
Aşağıdaki senaryolar, yukarıda açıklanan her yeteneği aynı pivot yapısına karşı gösteren üç uçtan uca örnek boyunca ilerler.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

{{< app/cells/assistant language="javascript" >}}