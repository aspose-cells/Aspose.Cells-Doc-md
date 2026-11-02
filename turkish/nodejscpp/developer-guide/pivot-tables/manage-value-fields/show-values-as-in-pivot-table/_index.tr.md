---
title: Özet Tablosunda Değerleri Göster
linktitle: Özet Tablosunda Değerleri Göster
description: Özet tablo veri alanı değerlerini toplamın yüzdesi, bir temel öğeden fark, koşu toplamları, sıralamalar ve daha fazlası olarak göstermek için Aspose.Cells for Node.js via C++ kullanın.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, özet tablo, değerleri göster, veri gösterim biçimi, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /tr/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir özet tablo, genellikle her veri alanını `SUM` veya `COUNT` gibi bir toplama işleviyle toplar. Excel’in **Show Values As** özelliği, her gösterilen sonucu bu toplamanın türettiği ikincil bir hesaplamayla değiştirir—örneğin, genel toplamın yüzdesi, koşu toplamı, seçilen bir temel öğeden fark ya da sıralama—böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım senaryoları, satır, sütun ya da genel toplamın yüzdesini içeren toplam payı analizleri; bir dönem alanında koşu toplamı kullanarak birikimli raporlama; temel öğeye göre fark veya yüzde farkı kullanarak bir temel öğeye karşı varyans analizi; ve değerleri en küçüğünden en büyüğüne ya da en büyüğünden en küçüğüne sıralamayı içerir.

## **PivotFieldDataDisplayFormat Enum Üyeleri**
Veri alanı kendi toplama işlevini (ör. SUM veya COUNT) korurken, Show Values As yalnızca birleştirilmiş değerin nasıl görüntüleneceğini değiştirir.  
Aşağıdaki tek çağrılı kolay kullanım yöntemi aynı yapılandırmayı uygular:

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
function pickEnum(enumType, candidates, fallback) {
    const type = enumType || {};
    for (const name of candidates) {
        if (type[name] !== undefined && type[name] !== null) {
            return type[name];
        }
    }
    return fallback;
}
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().add("PivotData");
const cells = sheet.getCells();
// --- Source data -----------------------------------------------------------
const headers = ["Region", "Product", "Sales"];
for (const [c, header] of headers.entries()) {
    cells.get(0, c).putValue(header);
}
const rows = [
    ["East", "Apple", 100],
    ["East", "Banana", 120],
    ["West", "Apple", 90],
    ["West", "Banana", 60],
    ["North", "Apple", 75],
    ["North", "Banana", 45]
];
for (const [r, row] of rows.entries()) {
    for (const [c, value] of row.entries()) {
        cells.get(r + 1, c).putValue(value);
    }
}
// --- Pivot table ------------------------------------------------------------
const pivotTables = sheet.getPivotTables();
const pivotTableIndex = pivotTables.add("A1:C7", 0, 4);
const pivotTable = pivotTables.get(pivotTableIndex);
pivotTable.getRowFields().add("Region");
pivotTable.getDataFields().add("Sales");
const salesField = pivotTable.getDataFields().get(0);
// --- ShowValuesAs -----------------------------------------------------------
const displayFormat = pickEnum(
    AsposeCells.PivotFieldDataDisplayFormat,
    ["PERCENT_OF_TOTAL", "PercentOfTotal", "PERCENTAGE_OF_TOTAL", "PercentageOfTotal"],
    7
);
const baseItemPositionType = pickEnum(
    AsposeCells.PivotItemPositionType,
    ["DEFAULT", "Default"],
    0
);
showValuesAs(salesField, displayFormat, -1, baseItemPositionType, -1);
// --- Save -------------------------------------------------------------------
workbook.save("ShowValuesAs.xlsx");
console.log("ShowValuesAs applied and workbook saved.");
```

| Parametre | Anlamı | Ne Zaman Gereklidir |
| --- | --- | --- |
| `displayFormat` | Uygulanacak `PivotFieldDataDisplayFormat` ikincil hesaplama. | Her zaman. |
| `baseField` | Özet tablosunun temel alanları içinde temel alanın sıfır tabanlı indeksi (örneğin, temel öğenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItemPositionType` | Temel öğenin mevcut öğeye göre nasıl seçildiği: `PivotItemPositionType.PREVIOUS`, `.NEXT` veya `.CUSTOM`. | Yalnızca üç taban öğesi biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItem` | Temel öğenin sıfır tabanlı indeksi. | Yalnızca `baseItemPositionType` `CUSTOM` olduğunda (`baseItem` (öğe indeksi) tam temel öğeyi seçer); `PREVIOUS` / `NEXT` ve temel olmayan tüm biçimler için yoksayılır — `0` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `NORMAL` | İkincil bir hesaplama yok; birleştirilmiş değer olduğu gibi gösterilir (varsayılan). | — |
| `DIFFERENCE_FROM` | Değeri, bir temel alandaki temel öğenin değerinden fark olarak gösterir. | baseField + PREVIOUS/NEXT/CUSTOM (`baseItem` yalnızca CUSTOM ile) |
| `PERCENTAGE_OF` | Değeri, bir temel alandaki temel öğenin değerinin yüzdesi olarak gösterir. | baseField + PREVIOUS/NEXT/CUSTOM (`baseItem` yalnızca CUSTOM ile) |
| `PERCENTAGE_DIFFERENCE_FROM` | Değeri, bir temel alandaki temel öğenin değerinden yüzde farkı olarak gösterir. | baseField + PREVIOUS/NEXT/CUSTOM (`baseItem` yalnızca CUSTOM ile) |
| `RUNNING_TOTAL_IN` | Değeri, bir temel alandaki ardışık öğeler için koşu toplamı olarak gösterir. | baseField (öğe sırasının birikimi yönlendirdiği alan) |
| `PERCENTAGE_OF_ROW` | Değeri, satır toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_COLUMN` | Değeri, sütun toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_TOTAL` | Değeri, genel toplamın yüzdesi olarak gösterir. | — |
| `INDEX` | Değeri, Excel indeks formülü ((value * grand total) / (row total * column total)) kullanarak gösterir. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Değeri, üst satır toplamının yüzdesi olarak gösterir (iç içe satır alanları için). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Değeri, üst sütun toplamının yüzdesi olarak gösterir (iç içe sütun alanları için). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Değeri, üst toplamının yüzdesi olarak gösterir. | `baseField` (referans üst alan) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Değeri, bir temel alandaki koşu toplamının yüzdesi olarak gösterir. | baseField (birikim alanı) |
| `RANK_SMALLEST_TO_LARGEST` | Değeri en küçüğünden (1) en büyüğüne sıralar. | — |
| `RANK_LARGEST_TO_SMALLEST` | Değeri en büyüğünden (1) en küçüğüne sıralar. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` `PivotShowValuesSetting` ayarını (`getCalculationType()`/`setCalculationType()`, `getBaseFieldIndex()`/`setBaseFieldIndex()`, `getBaseItemPositionType()`/`setBaseItemPositionType()`, ve `getBaseItemIndex()`/`setBaseItemIndex()`) yazar — yöntem ve özellik nesnesi aynı durumu yapılandırmanın iki yoludur; Excel'in Show Values As iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplam Yüzdesi Olarak Göster**
`PivotField.showValuesAs()` yöntemini `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` ile çağırarak her veri alanı hücresini, genel toplam dahil, genel toplamın payına dönüştürün. Gösterilen sayılar bu nedenle tam sonuç kümesinin oranı olarak okunur. Bu biçim, her değeri yalnızca genel toplamla ölçer, bu yüzden bir temel alan veya temel öğe gerekmez — son parametreler (`0`, `PivotItemPositionType.PREVIOUS`, `0`) biçim tarafından yok sayılan yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

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

## **PivotField.getShowValuesSetting()'ı Al ve Yapılandır**
Mevcut yapılandırmayı `PivotField.getShowValuesSetting()` aracılığıyla okuyun: yalnızca okunabilir bu erişici, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin dört özelliği etkin Show Values As hesabını açıklar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs()` yöntemini çağırın — dört ayarı tek bir çağrıda yazar, böylece özellikleri tek tek atamanıza gerek kalmaz.
`PivotShowValuesSetting` nesnesi `showValuesAs()` tarafından yazılan dört ayarı ortaya koyar:
- `getCalculationType()` ve `setCalculationType()` `PivotFieldDataDisplayFormat` ikincil hesabını seçer.
- `getBaseFieldIndex()` ve `setBaseFieldIndex()` temel alanın pivot alanlar içindeki sıfır tabanlı indeksini belirtir. Bu, taban ilgili biçimler tarafından kullanılır.
- `getBaseItemPositionType()` ve `setBaseItemPositionType()` temel öğenin mevcut öğeye göre nasıl konumlandırıldığını belirler ve `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` veya `PivotItemPositionType.CUSTOM` değerlerini kabul eder.
- `getBaseItemIndex()` ve `setBaseItemIndex()` sıfır tabanlı temel öğe indeksini belirtir ve `getBaseItemPositionType()` `CUSTOM` olduğunda kullanılır.
`showValuesAs()` çağrıldıktan sonra, `PivotTable.calculateData()` yöntemini tekrar çağırarak özet tablo gövdesinin yeniden hesaplanmasını ve güncellenmiş yapılandırma ile yeniden render edilmesini sağlayın.

```javascript
const AsposeCells = require("aspose.cells.node");
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
    AsposeCells.Pivot.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.Pivot.PivotItemPositionType.Previous,
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
- [Özet Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-cpp/manage-value-fields/)
- [Özet Tablosunu Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}