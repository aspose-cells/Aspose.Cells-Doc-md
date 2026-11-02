---
title: Özet Tabloda İlk 10 Öğeyi Gösterme veya Filtreleme
linktitle: Özet Tabloda İlk 10 Öğeyi Gösterme veya Filtreleme
description: Aspose.Cells for Node.js via C++ kullanarak bir özet tablo alanının yalnızca en yüksek veya en düşük sıralı öğelerini nasıl göstereceğinizi öğrenin. Bu makale; Excel 97-2003 için Top10AutoShow yöntemini, Top10AutoShowSettings ile seçeneklerin okunmasını ve Excel 2007-365 için FilterTop10 aracılığıyla İlk 10 Filtresi'ni ele alır.
keywords: Aspose.Cells, Node.js via C++, özet tablo, ilk 10, otomatik gösterim, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /tr/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alan onlarca öğe içerdiğinde okunması zor olabilir. İlk 10 raporu yalnızca en yüksek veya en düşük sıralı öğeleri içerir; bu özellik, sıralama raporlarının ihtiyacını karşılar — "gelire göre ilk 5 ürün" veya "satış sayısına göre en düşük 3 bölge". Aspose.Cells bunun için iki mekanizmayı destekler ve bunlar Microsoft Excel'in iki farklı nesline karşılık gelir.
- **Excel 97-2003 AutoShow** — `pivotField.top10AutoShow()` yöntemi. Bu, doğrudan özet tablo alanında saklanan klasik "Üst/Alt N Öğeyi Göster" ayarıdır. Hem eski hem de yeni tüm Excel sürümlerinde çalışır; çünkü ilk özet tablo biçiminin bir parçasıdır.
- **Excel 2007-365 İlk 10 Filtresi** — `pivotField.filterTop10()` yöntemi. Bu, alan menüsünde, Değer Filtreleri altında bulunan modern İlk 10 değer filtresidir. Alana bağlı bir `PivotFilter` nesnesi olarak saklanır ve hem öğe sayısına hem de yüzdeye dayalı sıralama seçenekleri sunar.

## **Excel 97-2003'te İlk 10 Gösterimi (top10AutoShow)**
Klasik AutoShow, `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)` çağrısıyla yapılandırılır:
- `isAutoShow` — alandaki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `isTop` — `true` en yüksek sıralı öğeleri (Üst), `false` ise en düşük sıralı öğeleri (Alt) korur.
- `count` — korunacak öğe sayısı; örneğin klasik bir İlk 10 raporu için 10.
- `rankBy` — öğelerin sıralamasını belirleyen **veri alanının** sıfırdan başlayan dizini. Öğeleri alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama, bir değer alanına veya alanın kendisine göre yapılabilir. Aşağıda iki temel kullanım biçimi gösterilmektedir.

### **Değer Alanına Göre Sıralama**
Satır alanının öğelerini, "Sum of Sales" gibi sıradan bir değer alanına göre sıralayın. Aşağıdaki örnek, tek bir satır alanı (`Sport`) ve tek bir veri alanı (`Sales`) içeren bir özet tablo oluşturur; ardından satışlara göre en yüksek sıralı 2 sporu gösterir. `rankBy` değeri 0'dır; çünkü "Sum of Sales", 0 dizinindeki veri alanıdır.

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Alanın Kendisine Göre Sıralama**
Bir alan kendisiyle de sıralanabilir; bunun için `rankBy` olarak -1 değerini geçirin. Bu varyant için ek bir veri alanı gerekmez; alanın satır (veya sütun) alanında bulunması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en düşük 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 biçimin varsayılan değeri olduğundan `rankBy` özniteliği özet tablo XML'inden çıkarılır; `top10AutoShowSettings.getRankBy()` çağrısı ise -1 değerini döndürür.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Geçerli Seçeneklerin Okunması (Top10AutoShowSettings)**
`pivotField.getTop10AutoShowSettings()` erişimcisi, alanda hâlihazırda saklanan AutoShow seçeneklerini içeren bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Mevcut bir çalışma kitabında veya az önce yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için bunu kullanın — dosyadan yüklenen çalışma kitapları dâhil.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Dört özellik, özet tablo XML'ine yazılan klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir; bu nedenle geri okunan değerler, tüm Excel sürümlerinde dikkate alınan değerlerdir.

## **Not**

{{% alert color="primary" %}}
- Doğrudan `PivotField` erişimcileri olan `isAutoShow`, `getIsAscendShow()`, `getAutoShowCount()` ve `getAutoShowField()` eskimiş olarak işaretlenmiştir. Bunun yerine `Top10AutoShowSettings` nesnesini kullanın: `pivotField.isAutoShow` yerine `top10AutoShowSettings.isAutoShow`, `pivotField.getIsAscendShow()` yerine `top10AutoShowSettings.isTop`, `pivotField.getAutoShowCount()` yerine `top10AutoShowSettings.getAutoShowCount()` ve `pivotField.getAutoShowField()` yerine `top10AutoShowSettings.getRankBy()` kullanılır. `pivotField.top10AutoShow()` yöntemi, ayarları değiştirmek için desteklenen yöntemdir.
- `top10AutoShow()`, satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alan bu şekilde sıralanamaz, çünkü öğeleri özet tablo gövdesinde yer almaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (filterTop10)**
Modern Excel sürümlerinde İlk 10, alan menüsünde bir değer filtresi olarak sunulur (Değer Filtreleri, İlk 10...). Aspose.Cells, oluşturulan `PivotFilter` nesnesini döndüren `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)` yöntemiyle bu özelliği modeller:
- `valueFieldIndex` — öğeleri toplulaştırılmış değerlerine göre sıralayan veri alanının sıfırdan başlayan dizini.
- `type` — `itemCount` değerinin ne anlama geldiğini belirtir. `PivotFilterType.Count`, belirli bir sayıda öğeyi korur (iletişim kutusunun Öğeler seçeneği). `PivotFilterType.Percent`, öğelerin bir yüzdesini korur; bu nedenle `itemCount` değerinin kendisi yüzdedir — 30 değeri, en üst yüzde 30'u korur. `PivotFilterType.SUM`, kümülatif değer kapsamına göre sıralar.
- `isTop` — Üst için `true`, Alt için `false`.
- `itemCount` — İlk N'deki N değeri; birimi `type` değerine bağlıdır.

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` ve `filterTop10` iki ayrı işlevdir. AutoShow, özet tablo alanında ayarlanan klasik `autoShow` öznitelik kümesini yazar ve Excel 97'den itibaren tüm Excel sürümlerinde dikkate alınır. `filterTop10`, Excel 2007 veya sonrasını gerektiren modern bir `PivotFilter` girdisi oluşturur. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan bir özet tablo tüm öğeleri gösterir. Eski araçlarla gidiş-dönüş işlemi yapılması gereken belgelerde `top10AutoShow` tercih edilmelidir; modern çalışma kitaplarında ise diğer değer filtreleriyle birleşebildiği için `filterTop10` tercih edilmelidir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Özet Tablosundaki Alanları Gruplandırma](/cells/tr/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/)
- [Özet Tablosuna Sayfa Alanı Ekleme](/cells/tr/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}