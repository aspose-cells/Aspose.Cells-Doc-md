---
title: Özet Tabloda İlk 10 Öğeyi Gösterme veya Filtreleme
linktitle: Özet Tabloda İlk 10 Öğeyi Gösterme veya Filtreleme
description: Java üzerinden Aspose.Cells for Node.js kullanarak bir özet tablo alanında yalnızca en üst veya en alt sıralı öğelerin nasıl gösterileceğini öğrenin. Bu makale, Excel 97-2003 Top10AutoShow yöntemini, Top10AutoShowSettings ile seçenekleri okumayı ve FilterTop10 aracılığıyla Excel 2007-365 İlk 10 filtresini kapsar.
keywords: Aspose.Cells, Node.js via Java, özet tablo, ilk 10, otomatik gösterim, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /tr/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Satır alanındaki her öğeyi listeleyen bir özet tablo, alan onlarca öğe içerdiğinde okunması zor olabilir. Yalnızca en yüksek veya en düşük sıralı öğeleri gösteren bir İlk 10 raporu, sıralama raporlarının tam olarak ihtiyaç duyduğu şeydir — "gelire göre ilk 5 ürün" veya "satış sayısına göre son 3 bölge" gibi. Aspose.Cells bunun için iki mekanizma destekler. Bunlar, Microsoft Excel'in iki farklı nesline karşılık gelir.
- **Excel 97-2003 AutoShow** — `PivotField.top10AutoShow()` yöntemi. Bu, doğrudan özet tablo alanı üzerinde depolanan klasik "En üst/en alt N öğeyi göster" ayarıdır. İlk özet tablo biçiminin bir parçası olduğu için eski ve yeni dahil her Excel sürümünde çalışır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.filterTop10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri bölümünde bulunan modern İlk 10 değer filtresidir. Alan üzerinde bir `PivotFilter` nesnesi olarak depolanır ve öğe sayısına ve yüzdeye dayalı sıralama seçenekleri sunar.

## **Excel 97-2003'te İlk 10 Öğeyi Gösterme (Top10AutoShow)**
Klasik AutoShow ayarı, `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` çağrısıyla yapılandırılır:
- `isAutoShow` — alan üzerindeki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `isTop` — `true` olduğunda en yüksek sıralı öğeleri (Üst), `false` olduğunda ise en düşük sıralı öğeleri (Alt) tutar.
- `count` — tutulacak öğe sayısı; klasik bir İlk 10 raporu için örneğin 10.
- `rankBy` — öğeleri sıralayan **veri alanının** sıfır tabanlı dizini. Öğeleri alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama ölçütü bir değer alanı veya alanın kendisi olabilir. Aşağıda iki temel varyant gösterilmektedir.

### **Bir Değer Alanına Göre Sıralama**
Satır alanının öğelerini, `Sum of Sales` gibi olağan bir değer alanına göre sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur ve ardından satışlara göre en üst 2 sporu gösterir. `rankBy` değeri 0'dır; `Sum of Sales` veri alanı 0 dizininde bulunur.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Alanın Kendisine Göre Sıralama**
Bir alan kendi öğelerine göre de sıralanabilir; bu durumda `rankBy` parametresine -1 değerini geçirin. Bu varyant için ek bir veri alanı gerekmez; alanın satır (veya sütun) alanında bulunması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en alt 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 varsayılan değer olduğu için `rankBy` özniteliği özet tablo XML'inde yer almaz. `getTop10AutoShowSettings().getRankBy()` ise -1 değerini geri okur.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Mevcut Seçenekleri Okuma (Top10AutoShowSettings)**
`PivotField.getTop10AutoShowSettings()` yöntemi, alan üzerinde depolanan AutoShow seçeneklerini sunan bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Mevcut bir çalışma kitabında veya az önce yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için bu yöntemi kullanın. Bu işlem, dosyadan yüklenen çalışma kitapları için de geçerlidir.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

`isAutoShow()`, `isTop()`, `getAutoShowCount()` ve `getRankBy()` getter metotları, özet tablo XML'inde yazılan klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir; bu nedenle geri okunan değerler, her Excel sürümünün uyduğu değerlerdir.

## **Not**

{{% alert color="primary" %}}
- `PivotField` üzerindeki doğrudan `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` ve `getAutoShowField()` getter metotları kullanımdan kaldırılmış olarak işaretlenmiştir. Bunun yerine `getTop10AutoShowSettings()` nesnesini kullanın: `isAutoShow()` için `getTop10AutoShowSettings().isAutoShow()`, `isAscendShow()` için `getTop10AutoShowSettings().isTop()`, `getAutoShowCount()` için `getTop10AutoShowSettings().getAutoShowCount()` ve `getAutoShowField()` için `getTop10AutoShowSettings().getRankBy()` kullanın. Ayarı değiştirmek için desteklenen yöntem, `top10AutoShow()` yöntemidir.
- `top10AutoShow()` hem satır hem de sütun alanlarında kullanılabilir. Yalnızca sayfa (filtre) alanında bulunan bir alan bu şekilde sıralanamaz, çünkü öğeleri özet tablo gövdesinde yer almaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (FilterTop10)**
Modern Excel sürümleri, alan menüsünde İlk 10 filtresini değer filtresi olarak sunar (Değer Filtreleri, İlk 10...). Aspose.Cells, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` yöntemiyle bu özelliği destekler:
- `valueFieldIndex` — öğeleri kendi birleştirilmiş değerlerine göre sıralayan veri alanının sıfır tabanlı dizini.
- `type` — `itemCount` değerinin ne anlama geldiğini belirtir. `PivotFilterType.COUNT` sabit sayıda öğe tutar (iletişim kutusunun Öğeler seçeneği). `PivotFilterType.PERCENT` öğelerin belirli bir yüzdesini tutar; bu nedenle `itemCount` doğrudan yüzde oranıdır — 30, öğelerin en üst %30'unu tutar. `PivotFilterType.SUM` kümülatif değer kapsamasına göre sıralar.
- `isTop` — Üst için `true`, Alt için `false`.
- `itemCount` — Üst/Alt N'deki N değeridir; birimi `type` değerine bağlıdır.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` ve `filterTop10()` iki ayrı özelliktir. AutoShow, özet tablo alanında ayarlanan klasik `autoShow` özniteliklerini yazar ve Excel 97 dahil tüm Excel sürümlerinde dikkate alınır. `filterTop10()` ise modern bir `PivotFilter` kaydı yazar ve Excel 2007 veya sonrası gereklidir. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan özet tablo tüm öğeleri göstermeye geri döner. Eski araçlarla kaydedilip yeniden açılması gereken belgelerde `top10AutoShow()` tercih edin; modern çalışma kitapları için ise diğer değer filtreleriyle birlikte çalışabildiği için `filterTop10()` tercih edin.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tabloları Etikete veya Değere Göre Filtreleme](/cells/tr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Özet Tabloya Satır ve Sütun Alanları Ekleme](/cells/tr/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Özet Tablosundaki Özet Alanlarını Gruplama](/cells/tr/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Özet Tabloyu Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)
- [Özet Tabloya Sayfa Alanı Ekleme](/cells/tr/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}