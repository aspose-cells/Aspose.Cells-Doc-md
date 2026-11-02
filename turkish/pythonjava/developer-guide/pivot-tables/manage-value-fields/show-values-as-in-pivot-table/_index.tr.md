---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Pivot tablo veri alanı değerlerini toplamın yüzde olarak, temel öğeden fark, birikimli toplam, sıralama ve daha fazlası olarak Aspose.Cells for Python via Java ile görüntüleyin.
keywords: Aspose.Cells, pivot tablo, değerleri göster, veri gösterim formatı, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /tr/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir pivot tablo genellikle `Sum` veya `Count` gibi bir toplama işleviyle her veri alanını toplar. Excel'in **Show Values As** özelliği, gösterilen her sonucu bu toplamdan türetilen ikincil bir hesaplamayla değiştirir — örneğin, toplamın yüzde olarak, birikimli toplam, seçilen bir temel öğe ile fark veya bir sıralama — böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanımlar arasında toplam payı analizi, bir satır, sütun veya genel toplamın yüzde değerlerini içeren; bir dönem alanında birikimli toplam kullanarak kümülatif raporlama; bir temel öğeye göre fark veya yüzde fark kullanarak benchmark öğesine karşı varyans analizi; ve değerleri en küçükten en büyüğe veya en büyükten en küçüğe sıralama bulunur.

## **PivotFieldDataDisplayFormat Enum Üyeleri**
Veri alanı, Sum veya Count gibi toplama işlevini korurken, Show Values As yalnızca toplu değerin nasıl gösterileceğini değiştirir.  
`PivotShowValuesSetting` özelliklerini doğrudan ayarlamanın (son bölüme bakın) yanı sıra, tek bir çağrı ile aynı yapılandırmayı uygulayan bir kolaylık yöntemi vardır:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| Parametre | Anlamı | Ne Zaman Gereklidir |
| --- | --- | --- |
| `displayFormat` | `PivotFieldDataDisplayFormat` uygulanacak ikincil hesaplama. | Her zaman. |
| `baseField` | Pivot tablosunun temel alanları arasındaki temel alanın sıfır tabanlı indeksi (örneğin, temel öğenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItemPositionType` | Temel öğenin mevcut öğeye göre nasıl seçildiği: `PivotItemPositionType.Previous`, `.Next` veya `.Custom`. | Yalnızca üç taban öğesi biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItem` | Temel öğenin sıfır tabanlı indeksi. | `baseItemPositionType` `Custom` olduğunda yalnızca (öğe indeksi tam temel öğeyi seçer); `Previous` / `Next` için ve temel olmayan formatlar için göz ardı edilir — `0` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `Normal` | İkincil hesaplama yok; toplu değer olduğu gibi gösterilir (öntanımlı). | — |
| `DifferenceFrom` | Değeri, bir temel alanındaki temel öğenin değerinden fark olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` sadece `Custom` ile) |
| `PercentageOf` | Değeri, bir temel alanındaki temel öğenin değerinin yüzde olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` sadece `Custom` ile) |
| `PercentageDifferenceFrom` | Değeri, bir temel alanındaki temel öğenin değerine göre yüzde fark olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` sadece `Custom` ile) |
| `RunningTotalIn` | Değeri, bir temel alanının ardışık öğeleri için birikimli toplam olarak gösterir. | `baseField` (birikimin yönlendirildiği alan) |
| `PercentageOfRow` | Değeri, satır toplamının yüzde değeri olarak gösterir. | — |
| `PercentageOfColumn` | Değeri, sütun toplamının yüzde değeri olarak gösterir. | — |
| `PercentageOfTotal` | Değeri, genel toplamın yüzde değeri olarak gösterir. | — |
| `Index` | Değeri, Excel indeks formülü ((value * grand total) / (row total * column total)) kullanarak gösterir. | — |
| `PercentageOfParentRowTotal` | Değeri, üst satır toplamının yüzde değeri olarak gösterir (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, üst sütun toplamının yüzde değeri olarak gösterir (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, üst toplamın yüzde değeri olarak gösterir. | `baseField` (referans üst alan) |
| `PercentageOfRunningTotalIn` | Değeri, bir temel alandaki birikimli toplamın yüzde değeri olarak gösterir. | `baseField` (birikim alanı) |
| `RankSmallestToLargest` | Değeri en küçükten (1) en büyüğe sıralar. | — |
| `RankLargestToSmallest` | Değeri en büyükten (1) en küçüğe sıralar. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` yöntemi, dört `PivotShowValuesSetting` değerini `setCalculationType`, `setBaseFieldIndex`, `setBaseItemPositionType` ve `setBaseItemIndex` aracılığıyla yazar — yöntem ve ayar nesnesi aynı durumu yapılandırmanın iki yoludur, Excel'in Show Values As iletişim kutusundaki temel alan ve temel öğe seçimcilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplamın Yüzdesi Olarak Göster**
`PivotField.showValuesAs` yöntemini `PivotFieldDataDisplayFormat.PercentageOfTotal` ile çağırarak, genel toplam dahil olmak üzere her veri alanı hücresini genel toplamın payına dönüştürürsünüz. Böylece gösterilen sayılar tam sonuç kümesinin oranları olarak okunur. Bu format, her değeri yalnızca genel toplamla ölçer, bu yüzden temel alan veya temel öğe gerekmez — kalan argümanlar (`0`, `PivotItemPositionType.Previous`, `0`) format tarafından göz ardı edilen yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **PivotField.getShowValuesSetting()'i Al ve Yapılandır**
`PivotField.getShowValuesSetting()` yöntemiyle mevcut yapılandırmayı okuyun: yalnızca okunabilir bu yöntem, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin dört özelliği aktif Show Values As hesaplamasını açıklar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs` yöntemini çağırın — tek bir çağrıda dört ayarı yazar, böylece özellikleri tek tek atamanıza gerek kalmaz.  
`PivotShowValuesSetting` nesnesi, `showValuesAs` tarafından yazılan dört özelliği ortaya çıkarır:
- `getCalculationType()` `PivotFieldDataDisplayFormat` ikincil hesaplamayı döndürür, `setCalculationType(...)` ise bunu değiştirir.
- `getBaseFieldIndex()` ve `setBaseFieldIndex(...)` pivot alanları içindeki temel alanın sıfır tabanlı indeksini belirtir. Taban ilgili biçimler tarafından kullanılır.
- `getBaseItemPositionType()` ve `setBaseItemPositionType(...)` temel öğenin mevcut öğeye göre nasıl konumlandırıldığını belirler ve `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` veya `PivotItemPositionType.Custom` değerlerini kabul eder.
- `getBaseItemIndex()` ve `setBaseItemIndex(...)` sıfır tabanlı temel öğe indeksini belirtir ve `BaseItemPositionType` `Custom` olduğunda kullanılır.
`showValuesAs`ı çağırdıktan sonra, `PivotTable.calculateData()`'yi tekrar çağırın, böylece pivot gövdesi güncellenmiş yapılandırma ile yeniden hesaplanır ve yeniden renderlanır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **İlgili Makaleler**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/python-java/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/python-java/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}