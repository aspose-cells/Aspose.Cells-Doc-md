---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Pivot tablo veri alanı değerlerini toplamın yüzdesi, temel bir öğeden fark, çalışan toplamlar, sıralamalar ve daha fazlası olarak Aspose.Cells for Node.js via Java ile görüntüleyin.
keywords: Aspose.Cells, Pivot Tablosu, değerleri göster, veri gösterim biçimi, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /tr/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir pivot tablo, genellikle her veri alanını `SUM` veya `COUNT` gibi bir toplama işleviyle toplar. Excel'in **Show Values As** özelliği, her görüntülenen sonucu, bu toplama dayalı ikincil bir hesaplamayla değiştirir; örneğin, toplamın yüzdesi, çalışan toplam, seçilen bir temel öğeden fark veya sıralama gibi—böylece yardımcı formüller veya hesaplanan sütunlar kullanmadan karşılaştırmalı analiz yapabilirsiniz. Tipik kullanım alanları, toplam payı analizini, satır, sütun veya genel toplamın yüzdelerini; bir dönem alanında çalışan toplam kullanarak kümülatif raporlamayı; bir temel öğeye göre fark veya yüzde farkı kullanarak bir kıyaslama öğesine karşı varyans analizini; ve değerleri en küçüğünden en büyüğüne ya da en büyüğünden en küçüğüne sıralamayı içerir. Aspose.Cells for Node.js via Java'da `PivotFieldDataDisplayFormat`, ikincil hesaplamayı seçer. Salt okunur `PivotField.getShowValuesSetting()` yöntemi bir `PivotShowValuesSetting` nesnesi döndürür. Bu nesnenin `setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()` ve `setBaseItemIndex()` yöntemleri davranışı yapılandırır; kolaylık yöntemi `PivotField.showValuesAs(...)` aynı dört ayarı tek bir çağrıda uygular. Bu ayarları `PivotTable.getDataFields()` ile elde edilen bir veri veya değer alanına uygulayın.

## **PivotFieldDataDisplayFormat Üyeleri**
Veri alanı, SUM veya COUNT gibi toplama işlevini korurken, Show Values As yalnızca toplama değerinin nasıl gösterileceğini dönüştürür. `PivotShowValuesSetting` ayarlarını doğrudan yazmanın (son bölüme bakın) yanı sıra, tek çağrılı bir kolaylık yöntemi aynı yapılandırmayı uygular:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| Parametre | Anlam | Ne Zaman Gereklidir |
| --- | --- | --- |
| `displayFormat` | Uygulanacak `PivotFieldDataDisplayFormat` ikincil hesaplaması. | Her zaman. |
| `baseField` | Pivot tablosunun temel alanları arasındaki temel alanın sıfır tabanlı indeksi (örneğin, temel öğenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItemPositionType` | Mevcut öğeye göre temel öğenin nasıl seçildiği: `PivotItemPositionType.PREVIOUS`, `.NEXT` veya `.CUSTOM`. | Yalnızca üç taban öğesi biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItem` | Temel öğenin sıfır tabanlı indeksi. | Yalnızca `baseItemPositionType` `CUSTOM` olduğunda (`baseItem` tam temel öğeyi seçer); `PREVIOUS` / `NEXT` ve diğer temel olmayan formatlar için yok sayılır — `0` geçirin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `NORMAL` | İkincil bir hesaplama yok; toplama değeri olduğu gibi gösterilir (varsayılan). | — |
| `DIFFERENCE_FROM` | Değeri, temel alanda bir temel öğenin değerinden fark olarak gösterir. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` yalnızca `CUSTOM` ile) |
| `PERCENTAGE_OF` | Değeri, temel alanda bir temel öğenin değerinin yüzdesi olarak gösterir. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` yalnızca `CUSTOM` ile) |
| `PERCENTAGE_DIFFERENCE_FROM` | Değeri, temel alanda bir temel öğenin değerinden yüzde farkı olarak gösterir. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` yalnızca `CUSTOM` ile) |
| `RUNNING_TOTAL_IN` | Değeri, temel alanın art arda gelen öğeleri için çalışan toplam olarak gösterir. | `baseField` (birikmeyi yönlendiren alan) |
| `PERCENTAGE_OF_ROW` | Değeri, satır toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_COLUMN` | Değeri, sütun toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_TOTAL` | Değeri, genel toplamın yüzdesi olarak gösterir. | — |
| `INDEX` | Değeri, Excel indeks formülü ((değer * genel toplam) / (satır toplamı * sütun toplamı)) kullanarak gösterir. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Değeri, üst satır toplamının yüzdesi olarak gösterir (iç içe satır alanları için). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Değeri, üst sütun toplamının yüzdesi olarak gösterir (iç içe sütun alanları için). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Değeri, üst toplamının yüzdesi olarak gösterir. | `baseField` (referans üst alan) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Değeri, temel alandaki bir çalışan toplamın yüzdesi olarak gösterir. | `baseField` (birikme alanı) |
| `RANK_SMALLEST_TO_LARGEST` | Değeri, en küçüğünden (1) en büyüğüne doğru sıralar. | — |
| `RANK_LARGEST_TO_SMALLEST` | Değeri, en büyüğünden (1) en küçüğüne doğru sıralar. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` `PivotShowValuesSetting` ayarını (`setCalculationType()`, `setBaseFieldIndex()`, `setBaseItemPositionType()`, ve `setBaseItemIndex()`) yazar — yöntem ve ayar nesnesi aynı durumu yapılandırmanın iki yoludur, Excel'in Show Values As iletişim kutusundaki temel alan ve temel öğe seçimcilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplamın Yüzdesi Olarak Göster**
`PivotField.showValuesAs()` yöntemini `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` ile çağırarak, genel toplam dahil her veri alanı hücresini genel toplamın payına dönüştürün. Görüntülenen sayılar böylece tam sonuç kümesinin oranları olarak okunur. Bu biçim, her değeri yalnızca genel toplamla karşılaştırır, bu yüzden temel alan veya temel öğeye ihtiyaç duymaz — sondaki argümanlar (`0`, `PivotItemPositionType.PREVIOUS`, `0`) biçim tarafından yok sayılan yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

```javascript
const AsposeCells = require("aspose.cells");
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
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting()'i Al ve Yapılandır**
`PivotField.getShowValuesSetting()` üzerinden mevcut yapılandırmayı okuyun: salt okunur yöntem, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin dört ayarı etkin Show Values As hesaplamasını açıklar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs()` yöntemini çağırın — bu yöntem tüm dört ayarı tek bir çağrıda yazar, böylece her birini ayrı ayrı atamanıza gerek kalmaz. `PivotShowValuesSetting` nesnesi `showValuesAs()` tarafından yazılan dört ayarı ortaya koyar:
- `getCalculationType()` / `setCalculationType()` `PivotFieldDataDisplayFormat` ikincil hesaplamasını seçer.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` pivot alanları içindeki temel alanın sıfır tabanlı indeksini belirtir. Taban ilgili biçimler tarafından kullanılır.
- `getBaseItemPositionType()` / `setBaseItemPositionType()` temel öğenin mevcut öğeye göre konumunu belirler ve `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` veya `PivotItemPositionType.CUSTOM` değerlerini kabul eder.
- `getBaseItemIndex()` / `setBaseItemIndex()` sıfır tabanlı temel öğe indeksini belirtir ve `getBaseItemPositionType()` `CUSTOM` olduğunda kullanılır.
`showValuesAs()` çağrıldıktan sonra, pivot gövdesinin güncellenmiş yapılandırmayla yeniden hesaplanıp yeniden render edilmesi için `PivotTable.calculateData()` yöntemini tekrar çağırın.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **İlgili Makaleler**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-java/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}