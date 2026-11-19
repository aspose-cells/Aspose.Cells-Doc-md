---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Pivot tablo veri alanı değerlerini toplamın yüzde olarak, bir temel öğeden fark olarak, kümülatif toplamlar, sıralamalar ve daha fazlası şeklinde Aspose.Cells for Python via Java ile görüntüleyin.
keywords: Aspose.Cells, özet tablo, değerleri göster, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /tr/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir özet tablo, her veri alanını `SUM` veya `COUNT` gibi bir toplama işleviyle birleştirir. Excel’in **Show Values As** özelliği, her gösterilen sonucu bu toplama dayanarak türetilen ikincil bir hesaplamayla (örneğin, toplamın yüzdesi, kümülatif toplam, seçilen bir temel öğeden fark veya sıralama) değiştirir; böylece yardımcı formüller ya da hesaplanmış sütunlar kullanmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım durumları, satır, sütun veya toplamın yüzdeleri gibi toplam payı analizleri; bir dönem alanında kümülatif raporlama için çalışan toplam; bir temel öğeye göre fark ya da yüzde fark ile kıyaslama; ve değerleri en küçüğünden en büyüğüne ya da tersine sıralamayı içerir.  
Aspose.Cells for Python via Java’da, `PivotShowValuesAsType` enum’ı ikincil hesaplamayı seçer. Salt okunur `PivotField.getShowValuesSetting()` yöntemi bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin `setShowValuesAs(...)`, `setBaseFieldIndex(...)` ve `setBaseItemIndex(...)` metodları davranışı yapılandırır; aynı ayarları tek bir çağrıda uygulayan kullanım kolaylığı yöntemi ise `PivotField.showValuesAs(...)`’dır. Bu ayarları, `PivotTable.getDataFields()` üzerinden elde edilen bir veri ya da değer alanına uygulayın.

## **PivotShowValuesAsType Enum Üyeleri**
Veri alanı `SUM` veya `COUNT` gibi toplama işlevini korurken, Show Values As yalnızca birleştirilmiş değerin nasıl görüntüleneceğini değiştirir.  
`PivotShowValuesSetting` ayarlayıcılarını doğrudan kullanmanın (son bölüme bakın) yanı sıra, aynı yapılandırmayı tek çağrıyla uygulayan bir kullanım kolaylığı yöntemi de vardır. Bu iki biçim, birincisi temel alan ve temel öğeyi indeksle, ikincisi ise isimle belirtir:

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| Parametre | Anlamı | Gerekli Olduğu Durum |
| --- | --- | --- |
| `show_values_as_type` | Uygulanacak `PivotShowValuesAsType` ikincil hesaplaması. | Her zaman. |
| `base_field` | Özet tablosunun temel alanları arasındaki temel alanın sıfır‑bazlı indeksi (örneğin, temel öğenin bulunduğu satır alanının indeksi) veya isim biçiminde temel alanın adı. | Aşağıdaki sekiz temel‑göreli biçim (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_SMALLEST_TO_SMALLEST`) için gereklidir; diğer biçimler için `0` (veya isim biçiminde `None`) gönderin. |
| `base_item` | Temel öğenin sıfır‑bazlı indeksi; iki özel değer: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) önceki öğeyi, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) sonraki öğeyi seçer. İsim biçiminde temel öğenin başlığı kullanılır ve temel öğe gerektirmeyen biçimler için `None` gönderilir. | Yalnızca üç temel‑öğe biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) temel öğeyi değerlendirir; beş alan‑göreli biçim (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, her iki sıralama) bunu yok sayar — `0` veya `None` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğesi Parametreleri |
| --- | --- | --- |
| `NORMAL` | İkincil hesaplama yok; birleştirilmiş değer olduğu gibi gösterilir (varsayılan). | — |
| `DIFFERENCE_FROM` | Değeri, temel alan içindeki bir temel öğenin değerinden fark olarak gösterir. | `base_field` + `base_item` (indeks, başlık veya önceki/sonraki özel değer) |
| `PERCENTAGE_OF` | Değeri, temel alan içindeki bir temel öğenin değerinin yüzdesi olarak gösterir. | `base_field` + `base_item` |
| `PERCENTAGE_DIFFERENCE_FROM` | Değeri, temel alan içindeki bir temel öğenin değerine göre yüzde farkı olarak gösterir. | `base_field` + `base_item` |
| `RUNNING_TOTAL_IN` | Değeri, temel alanın öğeleri üzerinden birikimli toplam olarak gösterir. | `base_field` (temel alan) |
| `PERCENTAGE_OF_ROW` | Değeri, satır toplamının yüzde olarak gösterir. | — |
| `PERCENTAGE_OF_COLUMN` | Değeri, sütun toplamının yüzde olarak gösterir. | — |
| `PERCENTAGE_OF_TOTAL` | Değeri, genel toplamın yüzde olarak gösterir. | — |
| `INDEX` | Değeri, Excel indeks formülü ((değer * genel toplam) / (satır toplamı * sütun toplamı)) ile gösterir. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Değeri, üst satır toplamının yüzde olarak gösterir (iç içe satır alanları için). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Değeri, üst sütun toplamının yüzde olarak gösterir (iç içe sütun alanları için). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Değeri, üst toplamın yüzde olarak gösterir. | `base_field` (referans toplamın üst alanı) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Değeri, temel alandaki birikimli toplamın yüzde olarak gösterir. | `base_field` (temel alan) |
| `RANK_SMALLEST_TO_LARGEST` | Değeri en küçüğünden en büyüğüne (1’den başlayarak) sıralar. | `base_field` (sıralama kapsamını tanımlayan alan) |
| `RANK_LARGEST_TO_SMALLEST` | Değeri en büyüğünden en küçüğüne (1’den başlayarak) sıralar. | `base_field` (sıralama kapsamını tanımlayan alan) |

{{% alert color="primary" %}}
`showValuesAs(...)` yöntemi, `setShowValuesAs`, `setBaseFieldIndex` ve `setBaseItemIndex` aracılığıyla `PivotShowValuesSetting` değerlerini yazar — yöntem ve ayar nesnesi aynı durumu iki şekilde yapılandırır; bu, Excel’in Show Values As iletişim kutusundaki temel alan ve temel öğe seçicilerine benzer.
{{% /alert %}}

## **Değerleri Toplamın Yüzdesi Olarak Göster**
`PivotField.showValuesAs` yöntemini `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` ile çağırarak her veri‑alanı hücresini, genel toplam dahil, toplamın payı olarak dönüştürün. Görüntülenen sayılar böylece tüm sonucun oranı olarak okunur. Bu biçim yalnızca genel toplam karşısında ölçüm yapar; bu yüzden temel alan veya temel öğe gerekmez — son parametreler (`0`, `0`) biçim tarafından yok sayılan yer tutuculardır, tablo açıklamasında belirtildiği gibi.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **PivotField.getShowValuesSetting()’i Al ve Yapılandır**
Mevcut yapılandırmayı `PivotField.getShowValuesSetting()` ile okuyun: salt okunur yöntem, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin özellikleri etkin Show Values As hesabını tanımlar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs` yöntemini çağırın — bu, tüm ayarları tek bir çağrıda yazar; böylece özellikleri tek tek ayarlamanıza gerek kalmaz.  
`PivotShowValuesSetting` nesnesi, `showValuesAs`’ın yazdığı durumu ortaya koyar:
- `getShowValuesAs()` ikincil `PivotShowValuesAsType` hesabını döndürür, `setShowValuesAs(...)` ise bunu değiştirir.
- `getBaseFieldIndex()` ve `setBaseFieldIndex(...)` temel alanın sıfır‑bazlı indeksini belirtir; temel‑göreli biçimler bunu kullanır.
- `getBaseItemIndex()` ve `setBaseItemIndex(...)` temel öğeyi belirtir: belirli bir özet öğenin sıfır‑bazlı indeksi ya da iki özel değer — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) önceki öğe, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) sonraki öğe. Temel‑öğe biçimleri bunu kullanır.
- `getBaseFieldName()` ve `getBaseItemCaption()` salt okunur görünümler olup, çözümlenmiş temel alan adını ve temel öğe başlığını rapor eder; örneğin önceki‑öğe özel değeri seçildiğinde `getBaseItemCaption()` `(previous)` döndürür.
`showValuesAs` çağrıldıktan sonra, `PivotTable.calculateData()` yöntemini tekrar çağırarak özet tablo gövdesinin yeniden hesaplanmasını ve güncellenmiş yapılandırma ile yeniden çizilmesini sağlayın.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **İlgili Makaleler**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/python-java/manage-value-fields/)
- [Özet Tablosunu Yenileme](/cells/tr/python-java/refresh-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}