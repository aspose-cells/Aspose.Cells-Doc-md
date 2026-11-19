---
title: Özet Tablosunda Değerleri Göster
description: Özet tablosu veri alanı değerlerini toplamın yüzde, bir temel öğeden fark, kümülatif toplamlar, sıralamalar ve daha fazlası olarak Aspose.Cells for Python via .NET ile görüntüleyin.
linktitle: Değerleri Göster
keywords: Aspose.Cells, özet tablo, değerleri göster, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /tr/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir özet tablo genellikle her veri alanını `SUM` veya `COUNT` gibi bir toplama işleviyle birleştirir. Excel’in **Show Values As** özelliği, her gösterilen sonucu bu toplama dayanarak türetilen ikincil bir hesaplama ile değiştirir; örneğin, toplamın yüzdesi, kümülatif toplam, seçilen bir temel öğeden fark veya bir sıralama gibi—bu sayede yardımcı formüller veya hesaplanan sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım alanları arasında toplam payı analizi (satır, sütun veya genel toplamın yüzde oranları), bir dönem alanında kümülatif raporlama, bir temel öğe üzerinden fark veya yüzde fark kullanarak bir referans öğeye karşı varyans analizi ve en küçükten büyüğe ya da en büyüğünden küçüğe değerlerin sıralanması bulunur.  
Aspose.Cells for Python via .NET içinde `PivotShowValuesAsType` enum’ı ikincil hesaplamayı seçer. Salt okunur `PivotField.show_values_setting` özelliği bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin yazılabilir `show_values_as`, `base_field_index` ve `base_item_index` özellikleri davranışı yapılandırır; kullanım kolaylığı sağlayan `PivotField.show_values_as(...)` yöntemi aynı ayarları tek bir çağrıda uygular. Bu ayarları `PivotTable.data_fields` üzerinden elde edilen bir veri veya değer alanına uygulayın.

## **PivotShowValuesAsType Enum Üyeleri**
Veri alanı `SUM` veya `COUNT` gibi toplama işlevini korur, ancak Show Values As yalnızca birleştirilmiş değerin nasıl görüntüleneceğini dönüştürür.  
`PivotShowValuesSetting` özelliklerini doğrudan yazmanın yanı sıra (bkz. son bölüm), aynı yapılandırmayı tek çağrıda uygulayan bir kullanım kolaylığı yöntemi de vardır. Bu yöntem iki biçimde sunulur — biri taban alanı ve taban öğesini indeksle, diğeri ise isimle adresler:

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| Parametre | Anlamı | Ne Zaman Gerekli |
| --- | --- | --- |
| `show_values_as_type` | Uygulanacak `PivotShowValuesAsType` ikincil hesaplama. | Her zaman. |
| `base_field` | Özet tablosunun taban alanları arasındaki taban alanın sıfır‑tabanlı indeksi (örneğin, taban öğenin ait olduğu satır alanının indeksi) veya — isim biçiminde — taban alanın adı. | Aşağıdaki sekiz taban‑göreceli biçim (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`) için gereklidir; diğer tüm biçimler için `0` (veya isim biçiminde `None`) gönderilir. |
| `base_item` | Taban öğenin sıfır‑tabanlı indeksi; iki özel değer vardır: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) bir önceki öğeyi, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) ise sonraki öğeyi seçer. İsim biçimi taban öğenin başlığını alır ve formatın taban öğeye ihtiyacı yoksa `None` gönderilir. | Yalnızca üç taban‑öğe biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) taban öğeyi değerlendirir; beş alan‑göreceli biçim (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, her iki sıralama) bunu yoksayar — `0` ya da `None` gönderilir. |

| Hesaplama Türü | Davranış | Taban Öğesi Parametreleri |
| --- | --- | --- |
| `NORMAL` | İkincil hesaplama yok; birleştirilmiş değer olduğu gibi gösterilir (öntanım). | — |
| `DIFFERENCE_FROM` | Değeri, taban alandaki bir taban öğenin değerinden fark olarak gösterir. | `base_field` + `base_item` (indeks, başlık veya önceki/sonraki özel değer) |
| `PERCENTAGE_OF` | Değeri, taban alandaki bir taban öğenin değerinin yüzdesi olarak gösterir. | `base_field` + `base_item` (indeks, başlık veya önceki/sonraki özel değer) |
| `PERCENTAGE_DIFFERENCE_FROM` | Değeri, taban alandaki bir taban öğenin değerinden yüzde fark olarak gösterir. | `base_field` + `base_item` (indeks, başlık veya önceki/sonraki özel değer) |
| `RUNNING_TOTAL_IN` | Değeri, taban alanın ardışık öğeleri için kümülatif toplam olarak gösterir. | `base_field` (toplamı yönlendiren alan) |
| `PERCENTAGE_OF_ROW` | Değeri, satır toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_COLUMN` | Değeri, sütun toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_TOTAL` | Değeri, genel toplamın yüzdesi olarak gösterir. | — |
| `INDEX` | Değeri, Excel indeks formülü ((değer * genel toplam) / (satır toplamı * sütun toplamı)) ile gösterir. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Değeri, üst satır toplamının yüzde oranı olarak gösterir (iç içe satır alanları için). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Değeri, üst sütun toplamının yüzde oranı olarak gösterir (iç içe sütun alanları için). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Değeri, üst toplamın yüzde oranı olarak gösterir. | `base_field` (referans toplamın bulunduğu üst alan) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Değeri, taban alandaki kümülatif toplamın yüzde oranı olarak gösterir. | `base_field` (akümülatif alan) |
| `RANK_SMALLEST_TO_LARGEST` | Değeri, en küçüğünden (1) en büyüğüne doğru sıralar. | `base_field` (sıralama kapsamını tanımlayan alan) |
| `RANK_LARGEST_TO_SMALLEST` | Değeri, en büyüğünden (1) en küçüğüne doğru sıralar. | `base_field` (sıralama kapsamını tanımlayan alan) |

{{% alert color="primary" %}}
`show_values_as(...)` yöntemi `PivotShowValuesSetting` özelliklerini (`show_values_as`, `base_field_index`, `base_item_index`) yazar — yöntem ve özellik nesnesi aynı durumu yapılandırmanın iki yoludur; Excel’in Show Values As iletişim kutusundaki taban alanı ve taban öğesi seçimlerini yansıtır.
{{% /alert %}}

## **Toplamın Yüzdesi Olarak Değerleri Göster**
`PivotField.show_values_as` yöntemini `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` ile çağırarak her veri‑alanı hücresini, genel toplam da dahil, genel toplamın payı olarak dönüştürün. Görüntülenen sayılar bu nedenle tam sonuç kümesinin oranları şeklinde okunur. Bu biçim yalnızca genel toplamı temel alır; bu yüzden taban alanı veya taban öğesine ihtiyaç duymaz — son argümanlar (`0`, `0`) biçim tarafından yok sayılan yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **PivotField.show_values_setting Özelliğini Okuma ve Yapılandırma**
Mevcut yapılandırmayı `PivotField.show_values_setting` aracılığıyla okuyun: salt okunur özellik, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin özellikleri etkin Show Values As hesaplamasını açıklar. Yapılandırmayı değiştirmek için `PivotField.show_values_as` yöntemini çağırın — bu yöntem tüm ayarları tek bir çağrıda yazar, böylece özellikleri tek tek atamanıza gerek kalmaz.  
`PivotShowValuesSetting` nesnesi, `show_values_as` tarafından yazılan durumu ortaya koyar:
- `show_values_as` `PivotShowValuesAsType` ikincil hesabını seçer.
- `base_field_index` taban alanının özet alanları içindeki sıfır‑tabanlı indeksini belirtir. Taban‑göreceli biçimler tarafından kullanılır.
- `base_item_index` taban öğeyi belirtir: belirli bir özet öğenin sıfır‑tabanlı indeksi ya da iki özel değer — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) önceki öğe, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) sonraki öğe. Taban‑öğe biçimleri tarafından kullanılır.
- `base_field_name` ve `base_item_caption` salt okunur görünümler olup, çözümlenmiş taban alanı adı ve taban öğe başlığını rapor eder; örneğin, önceki‑öğe özel değeri seçildikten sonra `base_item_caption` `(previous)` olarak okunur.  
`show_values_as` metodunu çağırdıktan sonra `PivotTable.calculate_data()` metodunu tekrar çalıştırarak özet gövdesinin yeniden hesaplanıp güncellenmiş yapılandırmayla yeniden çizilmesini sağlayın.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **İlgili Makaleler**
- [Özet Tablosunda Değer Alanlarını Yönetme](/cells/tr/python-net/manage-value-fields/)
- [Özet Tablosunu Yenileme](/cells/tr/python-net/refresh-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}