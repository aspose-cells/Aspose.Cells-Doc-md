---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Pivot Tablosu veri alanı değerlerini, toplamın yüzde oranı, bir temel öğeden fark, çalışan toplam, sıralama ve daha fazlası şeklinde görüntüleyin, Aspose.Cells for Node.js via C++ ile.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Pivot Tablosu, Değerleri Göster, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /tr/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir Pivot Tablosu genellikle her veri alanını `SUM` veya `COUNT` gibi bir toplama işleviyle toplar. Excel’in **Show Values As** özelliği, her görüntülenen sonucu bu toplama işleminden türetilen ikincil bir hesaplama ile değiştirir — örneğin, toplamın yüzde oranı, çalışan toplam, seçilmiş bir temel öğeden fark veya bir sıralama — böylece yardımcı formüller veya hesaplanmış sütunlar kullanmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım senaryoları, toplam payı analizini içerir; satır, sütun veya toplamın yüzde oranları; bir dönem alanında çalışan toplam kullanılarak kümülatif raporlama; bir temel öğeye göre fark veya yüzde farkı kullanarak bir kıyas öğesine karşı varyans analizi; ve değerlerin en küçükten en büyüğe veya en büyükten en küçüğe sıralanması.  
Aspose.Cells for Node.js via C++'da `PivotShowValuesAsType` ikincil hesabı seçer. Salt okunur `PivotField.getShowValuesSetting()` erişicisi bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin `setShowValuesAs()`, `setBaseFieldIndex()` ve `setBaseItemIndex()` metodları davranışı yapılandırır; kolay kullanım metodu `PivotField.showValuesAs(...)` aynı ayarları tek bir çağrıda uygular. Bu ayarları `PivotTable.getDataFields()` ile elde edilen bir veri veya değer alanına uygulayın.

## **PivotShowValuesAsType Enums Üyeleri**
Veri alanı, `SUM` veya `COUNT` gibi toplama işlevini korurken **Show Values As** yalnızca toplanan değerin nasıl görüntüleneceğini değiştirir.  
`PivotShowValuesSetting` ayarlarını doğrudan yazmanın (son bölüme bakın) yanı sıra, tek‑çağrılı bir kolay kullanım metodu aynı yapılandırmayı uygular. Bu metod iki biçimde gelir — birincisi temel alan ve temel öğeyi indeksle, ikincisi ise adla belirtir:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| Parametre | Anlamı | Ne Zaman Gerekli |
| --- | --- | --- |
| `showValuesAsType` | Uygulanacak `PivotShowValuesAsType` ikincil hesabı. | Her zaman. |
| `baseField` | Pivot Tablosunun temel alanları arasındaki temel alanın sıfır‑tabanlı indeksi (örneğin temel öğenin ait olduğu satır alanının indeksi) ya da ad biçiminde — temel alanın adı. | Aşağıdaki sekiz temel‑bağlı format (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`) için; diğer tüm formatlar için `0` (ya da ad biçiminde `null`) gönderin. |
| `baseItem` | Temel öğenin sıfır‑tabanlı indeksi; iki özel değer: -1 önceki öğeyi ve -2 sonraki öğeyi seçer (Node.js via C++ bağlamı adlandırılmış sabitleri dışarı aktarmaz — doğrudan bu değerleri gönderin). Ad biçimi temel öğenin başlığını alır ve format temel öğe gerektirmiyorsa `null` olur. | Sadece üç temel‑öğe formatı (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) temel öğeyi değerlendirir; beş alan‑bağlı format (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, her iki sıralama) bunu yok sayar — `0` ya da `null` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `Normal` | İkincil hesaplama yok; toplanan değer olduğu gibi görüntülenir (varsayılan). | — |
| `DifferenceFrom` | Değeri, bir temel alandaki temel öğenin değerinden fark olarak gösterir. | `baseField` + `baseItem` (indeks, başlık veya önceki/sonraki özel değer) |
| `PercentageOf` | Değeri, bir temel alandaki temel öğenin değerinin yüzdesi olarak gösterir. | `baseField` + `baseItem` (indeks, başlık veya önceki/sonraki özel değer) |
| `PercentageDifferenceFrom` | Değeri, bir temel alandaki temel öğenin değerinden yüzde farkı olarak gösterir. | `baseField` + `baseItem` (indeks, başlık veya önceki/sonraki özel değer) |
| `RunningTotalIn` | Değeri, bir temel alandaki ardışık öğeler için çalışan toplam olarak gösterir. | `baseField` (toplamın birikimini yöneten alan) |
| `PercentageOfRow` | Değeri, satır toplamının yüzde oranı olarak gösterir. | — |
| `PercentageOfColumn` | Değeri, sütun toplamının yüzde oranı olarak gösterir. | — |
| `PercentageOfTotal` | Değeri, genel toplamın yüzde oranı olarak gösterir. | — |
| `Index` | Değeri, Excel indeks formülü ((değer * toplam) / (satır toplamı * sütun toplamı)) ile gösterir. | — |
| `PercentageOfParentRowTotal` | Değeri, üst satır toplamının yüzde oranı olarak gösterir (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, üst sütun toplamının yüzde oranı olarak gösterir (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, üst toplamın yüzde oranı olarak gösterir. | `baseField` (referans alınan üst toplam alanı) |
| `PercentageOfRunningTotalIn` | Değeri, bir temel alandaki çalışan toplamın yüzde oranı olarak gösterir. | `baseField` (birikim alanı) |
| `RankSmallestToLargest` | Değeri en küçüğünden en büyüğüne (1’dan başlayarak) sıralar. | `baseField` (sıralama kapsamını tanımlayan alan) |
| `RankLargestToSmallest` | Değeri en büyüğünden en küçüğüne (1’dan başlayarak) sıralar. | `baseField` (sıralama kapsamını tanımlayan alan) |

{{% alert color="primary" %}}
`showValuesAs(...)` metodu `PivotShowValuesSetting` ayarlarını (`getShowValuesAs()`/`setShowValuesAs()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, ve `getBaseItemIndex()`/`setBaseItemIndex()`) yazar — bu yöntem ve özellik nesnesi aynı durumu yapılandırmanın iki yoludur; Excel'in Show Values As iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplam Yüzdesi Olarak Göster**
`PivotField.showValuesAs()` metodunu `PivotShowValuesAsType.PercentageOfTotal` ile çağırarak her veri alanı hücresini, genel toplam dahil, toplamın yüzde oranı olarak dönüştürün. Görüntülenen sayılar bu nedenle tam sonuç kümesinin oranları şeklinde gösterilir. Bu format yalnızca genel toplam karşısında her değeri ölçer, bu yüzden temel alan veya temel öğe gerekmez — son parametreler (`0`, `0`) formatın göz ardı ettiği yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

```javascript
const AsposeCells = require("aspose.cells.node");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting()'i Al ve Yapılandır**
`PivotField.getShowValuesSetting()` aracılığıyla mevcut yapılandırmayı okuyun: salt okunur erişici, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin ayarları aktif Show Values As hesabını açıklar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs()` metodunu çağırın — bu, tüm ayarları tek bir çağrıda yazar, böylece her birini ayrı ayrı ayarlamanıza gerek kalmaz.
`PivotShowValuesSetting` nesnesi `showValuesAs()` metodunun yazdığı durumu ortaya çıkar:
- `getShowValuesAs()` ve `setShowValuesAs()` `PivotShowValuesAsType` ikincil hesabını seçer.
- `getBaseFieldIndex()` ve `setBaseFieldIndex()` temel alanın sıfır‑tabanlı indeksini belirtir; temel‑bağlı formatlar tarafından kullanılır.
- `getBaseItemIndex()` ve `setBaseItemIndex()` temel öğeyi belirtir: belirli bir pivot öğesinin sıfır‑tabanlı indeksi ya da iki özel değer — önceki öğe için -1, sonraki öğe için -2 (bağlam adlandırılmış sabitleri dışarı aktarmaz). Temel‑öğe formatları tarafından kullanılır.
- `getBaseFieldName()` ve `getBaseItemCaption()` çözümlenmiş temel alan adını ve temel öğe başlığını raporlayan salt okunur görünümlerdir; örneğin, önceki‑öğe özel değeri seçtikten sonra `getBaseItemCaption()` `(previous)` döndürür.
`showValuesAs()` çağırdıktan sonra `PivotTable.calculateData()` metodunu yeniden çalıştırın; böylece Pivot gövdesi güncellenmiş yapılandırmayla yeniden hesaplanır ve yeniden görüntülenir.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **İlgili Makaleler**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-cpp/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}