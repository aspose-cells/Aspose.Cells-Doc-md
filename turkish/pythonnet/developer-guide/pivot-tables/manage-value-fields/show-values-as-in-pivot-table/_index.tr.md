---
title: Özet Tablo’da Değerleri Gösterme
linktitle: Özet Tablo’da Değerleri Gösterme
description: Özet tablo veri alanı değerlerini yüzde, temel öğeden fark, koşu toplamı, sıralama ve daha fazlası olarak Aspose.Cells for Python via .NET ile görüntüleyin.
keywords: Aspose.Cells for Python via .NET, özet tablo, değerleri göster, veri görüntüleme biçimi, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /tr/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir özet tablo, genellikle `SUM` veya `COUNT` gibi bir toplama işleviyle her veri alanını özetler. Excel’in **Show Values As** özelliği, bu özetlenmiş sonucun yerine, yüzde, koşu toplamı, seçili bir temel öğeden fark veya sıralama gibi ikincil bir hesaplama göstererek, yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapmanıza olanak tanır.  
Tipik kullanım alanları şunlardır: bir satır, sütun veya genel toplamın yüzdesi olarak pay‑analizi; bir dönem alanında koşu toplamı kullanarak birikimli raporlama; temel bir öğeye göre fark ya da yüzde fark ile kıstas analizi; ve değerleri en küçüğünden en büyüğüne ya da tersine sıralama.  
Aspose.Cells for Python via .NET’te, `PivotFieldDataDisplayFormat` ikincil hesabı seçer. Salt okunur `PivotField.show_values_setting` özelliği bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin yazılabilir `calculation_type`, `base_field_index`, `base_item_position_type` ve `base_item_index` özellikleri davranışı yapılandırır; ayrıca `PivotField.show_values_as(...)` yöntemi aynı dört ayarı tek bir çağrıda uygular. Bu ayarları, `PivotTable.data_fields` üzerinden elde edilen bir veri ya da değer alanına uygulayın.

## **PivotFieldDataDisplayFormat Üyeleri**
Veri alanı, `SUM` veya `COUNT` gibi toplama işlevini korurken, Show Values As yalnızca özetlenmiş değerin nasıl gösterileceğini değiştirir.  
`PivotShowValuesSetting` özelliklerini doğrudan yazmak yerine (aşağıdaki bölüme bakınız), tek‑çağrılı bir kolaylık yöntemi aynı yapılandırmayı uygular:

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| Parametre | Anlamı | Gerekliliği |
| --- | --- | --- |
| `display_format` | Uygulanacak `PivotFieldDataDisplayFormat` ikincil hesabı. | Her zaman. |
| `base_field` | Özet tablonun temel alanları arasındaki temel alanın sıfır‑tabanlı indeksi (örneğin temel öğenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); diğer tüm biçimler tarafından yok sayılır. |
| `base_item_position_type` | Temel öğenin mevcut öğeye göre nasıl seçildiği: `PivotItemPositionType.PREVIOUS`, `.NEXT` veya `.CUSTOM`. | Yalnızca üç taban öğesi biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); diğer tüm biçimler tarafından yok sayılır. |
| `base_item` | Temel öğenin sıfır‑tabanlı indeksi. | `base_item_position_type` `CUSTOM` olduğunda gerekir (öğe indeksi tam temel öğeyi seçer); `PREVIOUS` / `NEXT` ve temel‑öğe olmayan biçimler için yok sayılır — `0` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `NORMAL` | İkincil bir hesaplama yok; özetlenmiş değer olduğu gibi görüntülenir (varsayılan). | — |
| `DIFFERENCE_FROM` | Değeri, temel alandaki bir temel öğenin değerinden fark olarak gösterir. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` yalnız `CUSTOM` ile) |
| `PERCENTAGE_OF` | Değeri, temel alandaki bir temel öğenin değerinin yüzdesi olarak gösterir. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` yalnız `CUSTOM` ile) |
| `PERCENTAGE_DIFFERENCE_FROM` | Değeri, temel alandaki bir temel öğenin değerinden yüzde farkı olarak gösterir. | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM` (`base_item` yalnız `CUSTOM` ile) |
| `RUNNING_TOTAL_IN` | Değeri, temel alandaki ardışık öğeler için koşu toplamı olarak gösterir. | `base_field` (birikim alanını belirler) |
| `PERCENTAGE_OF_ROW` | Değeri, satır toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_COLUMN` | Değeri, sütun toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_TOTAL` | Değeri, genel toplamın yüzdesi olarak gösterir. | — |
| `INDEX` | Değeri, Excel indeks formülü ((değer * genel toplam) / (satır toplamı * sütun toplamı)) ile gösterir. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Değeri, üst satır toplamının yüzdesi olarak gösterir (iç içe satır alanları için). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Değeri, üst sütun toplamının yüzdesi olarak gösterir (iç içe sütun alanları için). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Değeri, üst toplamın yüzdesi olarak gösterir. | `baseField` (referans üst alan) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Değeri, temel alandaki bir koşu toplamının yüzdesi olarak gösterir. | `base_field` (birikim alanı) |
| `RANK_SMALLEST_TO_LARGEST` | Değeri, en küçüğünden en büyüğe doğru derecelendirir. | — |
| `RANK_LARGEST_TO_SMALLEST` | Değeri, en büyükten en küçüğe doğru derecelendirir. | — |

{{% alert color="primary" %}}
`show_values_as(...)` yöntemi `PivotShowValuesSetting` özelliğini (`calculation_type`, `base_field_index`, `base_item_position_type`, `base_item_index`) yazar — bu yöntem ve özellik nesnesi aynı durumu yapılandırmanın iki yoludur ve Excel’in Show Values As iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplamın Yüzdesi Olarak Göster**
`PivotField.show_values_as` yöntemini `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` ile çağırarak, her veri‑alanı hücresini (genel toplam dahil) genel toplamın payı olarak dönüştürün. Görünen sayılar böylece tüm sonuç kümesinin oranı olarak okunur. Bu biçim yalnızca genel toplamı temel alır; bu yüzden temel alan veya temel öğe gerekmez — alt parametreler (`0`, `PivotItemPositionType.PREVIOUS`, `0`) format tarafından yok sayılan yer tutuculardır, tablo açıklamasında belirtildiği gibi.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
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
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **PivotField.show_values_setting Özelliğini Al ve Yapılandır**
Mevcut yapılandırmayı `PivotField.show_values_setting` üzerinden okuyun: salt‑okunur bu özellik, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnedeki dört özellik, etkin “Değerleri Göster” hesabını tanımlar. Yapılandırmayı değiştirmek için `PivotField.show_values_as` yöntemini çağırın — bu yöntem tüm dört ayarı tek bir çağrıda yazar, böylece özellikleri tek tek atamanıza gerek kalmaz.  
`PivotShowValuesSetting` nesnesi `show_values_as` tarafından yazılan dört özelliği ortaya koyar:
- `calculation_type` ikincil `PivotFieldDataDisplayFormat` hesabını seçer.
- `base_field_index` temel alanın sıfır‑tabanlı indeksini belirtir; taban ilgili biçimler tarafından kullanılır.
- `base_item_position_type` temel öğenin mevcut öğeye göre konumunu belirler ve `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` veya `PivotItemPositionType.CUSTOM` değerlerini alır.
- `base_item_index` sıfır‑tabanlı temel öğe indeksini belirtir ve `base_item_position_type` `CUSTOM` olduğunda kullanılır.
`show_values_as` çağrısını yaptıktan sonra, güncellenmiş yapılandırmanın uygulanması ve özet tablonun yeniden çizilmesi için `PivotTable.calculate_data()` yöntemini tekrar çağırın.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **İlgili Makaleler**
- [Özet Tablodaki Değer Alanlarını Yönetme](/cells/tr/python-net/manage-value-fields/)
- [Özet Tabloyu Yenileme](/cells/tr/python-net/refresh-pivot-table/)
- [Özet Tabloya Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}