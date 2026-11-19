---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Pivot tablo veri alanı değerlerini toplamın yüzdesi, temel bir öğeden fark, çalışan toplamlar, sıralamalar ve daha fazlası olarak Aspose.Cells for Node.js via Java ile gösterin.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, pivot tablo, değerleri göster, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /tr/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir pivot tablo genellikle `SUM` veya `COUNT` gibi bir toplama işleviyle her veri alanını özetler. Excel’in **Show Values As** (Değerleri Göster) özelliği, her gösterilen sonucu, o toplama dayalı ikincil bir hesaplamayla değiştirir—örneğin, toplamın yüzde oranı, çalışan toplam, seçilen bir temel öğeden fark veya bir sıralama—böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım senaryoları, bir satır, sütun veya toplamın yüzde oranı gibi toplam payı analizleri; bir dönem alanındaki çalışan toplamla kümülatif raporlama; bir temel öğeye göre fark veya yüzde farkla kıyaslama; ve değerlerin en küçüğünden en büyüğüne veya tersine sıralanmasıdır.  
Aspose.Cells for Node.js via Java’da, ikincil hesabı seçmek için `PivotShowValuesAsType` enum’ı kullanılır. Salt okunur `PivotField.getShowValuesSetting()` yöntemi bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin `setShowValuesAs()`, `setBaseFieldIndex()` ve `setBaseItemIndex()` metodları davranışı yapılandırır; aynı ayarları tek bir çağrıda uygulayan `PivotField.showValuesAs(...)` yöntemi de vardır. Bu ayarları `PivotTable.getDataFields()` ile elde edilen bir veri veya değer alanına uygulayın.

## **PivotShowValuesAsType Enum Üyeleri**
Veri alanı, `SUM` veya `COUNT` gibi toplama işlevini korur; Show Values As sadece birleştirilmiş değerin nasıl gösterileceğini dönüştürür.  
`PivotShowValuesSetting` ayarlayıcılarını doğrudan kullanmanın yanı sıra (aşağıdaki son bölüme bakınız), aynı yapılandırmayı tek bir çağrıda uygulayan bir yöntem de vardır. Bu yöntem iki biçimde gelir—birincisi temel alan ve temel öğeyi indeksle, ikincisi ise isimle adresler:

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| Parametre | Anlamı | Ne Zaman Gereklidir |
| --- | --- | --- |
| `showValuesAsType` | Uygulanacak `PivotShowValuesAsType` ikincil hesabı. | Her zaman. |
| `baseField` | Pivot tablosunun temel alanları arasındaki temel alanın sıfır bazlı indeksi (örneğin, temel öğenin ait olduğu satır alanının indeksi) ya da isim biçiminde temel alanın adı. | Aşağıdaki sekiz temel‑ilişkili format (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`) için gereklidir; diğer formatlarda `0` (veya isim biçiminde `null`) gönderin. |
| `baseItem` | Temel öğenin sıfır bazlı indeksi; iki özel değer: -1 önceki öğeyi, -2 sonraki öğeyi seçer (paket kökü `PivotShowValuesSetting` sabitlerini dışa aktarmaz — literal değerleri gönderin). İsim biçimi temel öğenin başlığını alır ve format temel öğe gerektirmiyorsa `null` olur. | Yalnızca üç temel‑öğe formatı (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) temel öğeyi değerlendirir; beş alan‑ilişkili format (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, her iki sıralama) bunu yok sayar — `0` ya da `null` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğeler Parametreleri |
| --- | --- | --- |
| `NORMAL` | İkincil hesaplama yok; birleştirilmiş değer olduğu gibi gösterilir (varsayılan). | — |
| `DIFFERENCE_FROM` | Değeri, temel alandaki temel öğenin değerinden fark olarak gösterir. | `baseField` + `baseItem` (indeks, başlık veya önceki/sonraki özel değer) |
| `PERCENTAGE_OF` | Değeri, temel alandaki temel öğenin değerinin yüzdesi olarak gösterir. | `baseField` + `baseItem` |
| `PERCENTAGE_DIFFERENCE_FROM` | Değeri, temel alandaki temel öğenin değerine göre yüzde fark olarak gösterir. | `baseField` + `baseItem` |
| `RUNNING_TOTAL_IN` | Değeri, temel alanın ardışık öğeleri için birikimli toplam olarak gösterir. | `baseField` (birikimin yönlendirildiği alan) |
| `PERCENTAGE_OF_ROW` | Değeri, satır toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_COLUMN` | Değeri, sütun toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_TOTAL` | Değeri, genel toplamın yüzdesi olarak gösterir. | — |
| `INDEX` | Değeri, Excel indeks formülü ((değer * genel toplam) / (satır toplamı * sütun toplamı)) ile gösterir. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Değeri, üst satır toplamının yüzdesi olarak gösterir (iç içe satır alanları için). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Değeri, üst sütun toplamının yüzdesi olarak gösterir (iç içe sütun alanları için). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Değeri, üst toplamının yüzdesi olarak gösterir. | `baseField` (referans alınan üst alan) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Değeri, temel alandaki birikimli toplamın yüzdesi olarak gösterir. | `baseField` (birikim alanı) |
| `RANK_SMALLEST_TO_LARGEST` | Değeri en küçüğünden (1) en büyüğüne kadar sıralar. | `baseField` (sıralama kapsamını tanımlayan alan) |
| `RANK_LARGEST_TO_SMALLEST` | Değeri en büyüğünden (1) en küçüğüne kadar sıralar. | `baseField` (sıralama kapsamını tanımlayan alan) |

{{% alert color="primary" %}}
`showValuesAs(...)` metodu, `setShowValuesAs()`, `setBaseFieldIndex()` ve `setBaseItemIndex()` aracılığıyla `PivotShowValuesSetting` durumunu yazar—metot ve özellik nesnesi, Excel’in Show Values As iletişim penceresindeki temel alan ve temel öğe seçicileriyle aynı durumu iki şekilde yapılandırır.
{{% /alert %}}

## **Toplamın Yüzdesi Olarak Değerleri Göster**
`PivotField.showValuesAs()` yöntemini `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` ile çağırarak her veri‑alanı hücresini, genel toplam dahil, toplamın payı olarak dönüştürün. Görünen sayılar bu nedenle tüm sonuç kümesinin oranı gibi okunur. Bu format sadece genel toplam karşısında değerleri ölçer; bu yüzden temel alan veya temel öğe gerekmez—alt parametreler (`0`, `0`) format tarafından göz ardı edilen yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting()'ı Al ve Yapılandır**
Mevcut yapılandırmayı `PivotField.getShowValuesSetting()` ile okuyun: salt okunur metod, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin ayarları etkin Show Values As hesabını tanımlar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs()` metodunu çağırın—bu metod tüm ayarları tek bir çağrıda yazar, böylece ayrı ayrı ayarlama yapmanız gerekmez.  
`PivotShowValuesSetting` nesnesi, `showValuesAs()` tarafından yazılan durumu ortaya koyar:
- `getShowValuesAs()` / `setShowValuesAs()` `PivotShowValuesAsType` ikincil hesabını seçer.
- `getBaseFieldIndex()` / `setBaseFieldIndex()` temel alanın sıfır bazlı indeksini belirtir; temel‑ilişkili formatlar tarafından kullanılır.
- `getBaseItemIndex()` / `setBaseItemIndex()` temel öğeyi belirtir: belirli bir pivot öğesinin sıfır bazlı indeksi ya da iki özel değer — -1 önceki öğe, -2 sonraki öğe (paket kökü adlandırılmış sabitleri dışa aktarmaz). Temel‑öğe formatları tarafından kullanılır.
- `getBaseFieldName()` ve `getBaseItemCaption()` salt okunur görünümler olup, çözümlenmiş temel alan adını ve temel öğe başlığını rapor eder; örneğin, önceki‑öğe seçildikten sonra `getBaseItemCaption()` `(previous)` döndürür.
`showValuesAs()` çağrıldıktan sonra, pivot gövdesinin yeniden hesaplanıp güncellenmesi için `PivotTable.calculateData()` metodunu tekrar çalıştırın.

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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

## **Related Articles**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-java/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}