---
title: Özet Tablosunda İlk 10'u Gösterme veya Filtreleme
linktitle: Özet Tablosunda İlk 10'u Gösterme veya Filtreleme
description: Aspose.Cells for Python via .NET kullanılarak bir özet tablo alanında yalnızca en üst veya en alt sıralı öğelerin nasıl gösterileceğini öğrenin. Bu makale, Excel 97-2003 top_10_auto_show yöntemini, top_10_auto_show_settings ile seçeneklerin okunmasını ve Excel 2007-365 İlk 10 Filtresi'nin filter_top10 aracılığıyla kullanılmasını ele alır.
keywords: Aspose.Cells, Python via .NET, özet tablo, ilk 10, otomatik gösterim, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /tr/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanının her öğesini listeleyen bir özet tablo, alan onlarca öğe içerdiğinde okunması zor olabilir. İlk 10 raporu yalnızca en üst veya en alt sıralı öğeleri içerir; bu tam olarak sıralama raporlarının ihtiyaç duyduğu özelliktir — "gelire göre ilk 5 ürün" veya "satış sayısına göre son 3 bölge" gibi. Aspose.Cells bunun için iki mekanizmayı destekler ve bu mekanizmalar Microsoft Excel'in iki kuşağına karşılık gelir.
- **Excel 97-2003 Otomatik Gösterim** — `PivotField.top_10_auto_show()` yöntemi. Bu, doğrudan özet tablo alanı üzerinde saklanan klasik "En üst/alt N öğeyi göster" ayarıdır. Özgün özet tablo biçiminin bir parçası olduğu için eski ve yeni tüm Excel sürümlerinde çalışır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.filter_top10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri bölümünde bulunan modern İlk 10 değer filtresidir. Alana bağlı bir `PivotFilter` nesnesi olarak saklanır ve öğe sayısına veya yüzdeye dayalı sıralama sunar.

## **Excel 97-2003'te İlk 10'u Gösterme (top_10_auto_show)**
Klasik Otomatik Gösterim, `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)` çağrısıyla yapılandırılır:
- `is_auto_show` — alan üzerindeki Otomatik Gösterim ayarını etkinleştirir veya devre dışı bırakır.
- `is_top` — `True`, en üst sıralı öğeleri (Üst) tutar; `False`, en alt sıralı öğeleri (Alt) tutar.
- `count` — kaç öğenin tutulacağını belirtir; örneğin klasik İlk 10 raporu için 10.
- `rank_by` — öğeleri sıralamak için kullanılan **veri alanının** sıfırdan başlayan dizini. Öğeleri alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama bir değer alanına veya alanın kendisine göre yapılabilir. Aşağıda bu iki varyant gösterilmektedir.

### **Bir Değer Alanına Göre Sıralama**
Satır alanının öğelerini `Sales` gibi sıradan bir değer alanına göre sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur ve ardından satışlara göre ilk 2 sporu gösterir. `rank_by` değeri 0'dır; çünkü `Sum of Sales`, 0 dizinindeki veri alanına karşılık gelir.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# "Satışların Toplamı" değerine göre sıralanan ilk 2 öğeyi göster (veri alanı dizini 0)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **Alanın Kendisiyle Sıralama**
Bir alan kendisiyle de sıralanabilir; bunun için `rank_by` parametresine -1 değerini geçirin. Bu varyant için ek bir veri alanı gerekmez; alanın satır veya sütun alanına yerleştirilmiş olması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en alt 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 XML biçiminin varsayılan değeri olduğu için `rank_by` özniteliği özet tablo XML verisinden çıkarılır ve `top_10_auto_show_settings.rank_by` değeri -1 olarak okunur.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **Mevcut Seçenekleri Okuma (top_10_auto_show_settings)**
`PivotField.top_10_auto_show_settings` özelliği, alan üzerinde saklanan geçerli Otomatik Gösterim seçeneklerini içeren bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Mevcut bir çalışma kitabında veya yeni yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için bu özelliği kullanın; dosyadan yüklenen çalışma kitapları da kapsama dâhildir.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

Dört özellik, özet tablo XML verisine yazılan klasik Otomatik Gösterim özniteliklerine (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) karşılık gelir. Bu nedenle geri okunan değerler, tüm Excel sürümlerinde dikkate alınan değerlerdir.

## **Not**

{{% alert color="primary" %}}
- Doğrudan `PivotField` özellikleri olan `is_auto_show`, `is_ascend_show`, `auto_show_count` ve `auto_show_field` kullanımdan kaldırılmış olarak işaretlenmiştir. Bunun yerine `top_10_auto_show_settings` nesnesini kullanın: `is_auto_show` için `top_10_auto_show_settings.is_auto_show`, `is_ascend_show` için `top_10_auto_show_settings.is_top`, `auto_show_count` için `top_10_auto_show_settings.auto_show_count`, `auto_show_field` için `top_10_auto_show_settings.rank_by` kullanılır. `top_10_auto_show()` yöntemi, ayarları değiştirmek için desteklenen yöntemdir.
- `top_10_auto_show`, satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alanın öğeleri özet tablo gövdesinde yerleştirilmediği için bu şekilde sıralanamaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (filter_top10)**
Modern Excel sürümleri, İlk 10 seçeneğini alan menüsünde bir değer filtresi olarak sunar (Değer Filtreleri, İlk 10...). Aspose.Cells bu özelliği `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)` yöntemiyle destekler. Bu yöntem, oluşturulan `PivotFilter` nesnesini döndürür:
- `value_field_index` — öğelerin sıralanmasında kullanılan, değerleri toplanan veri alanının sıfırdan başlayan dizini.
- `type` — `item_count` değerinin anlamını belirler. `PivotFilterType.COUNT`, belirli sayıda öğe tutar (iletişim kutusunun Öğeler seçeneği). `PivotFilterType.PERCENT`, öğelerin belirli bir yüzdesini tutar; bu nedenle `item_count` değerinin kendisi yüzdeyi belirtir — 30 değeri, öğelerin en üst yüzde 30'luk bölümünü tutar. `PivotFilterType.SUM`, öğeleri kümülatif değer kapsamına göre sıralar.
- `is_top` — Üst için `True`, Alt için `False`.
- `item_count` — İlk N ifadesindeki N değeri; birimi `type` değerine bağlıdır.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# En İlk 10 Filtresi — "Satışların Toplamı" ölçütüyle en üst 2 öğeyi tut (veri alanı dizini 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# Bunun yerine yüzde tabanlı bir filtre kullanmak için, öğelerin en üst yüzde 30'unu tut:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` ve `filter_top10` iki ayrı özelliktir. Otomatik Gösterim, özet tablo alanında klasik `autoShow` özniteliğini yazar ve Excel 97 dahil tüm Excel sürümlerinde dikkate alınır. `filter_top10` ise modern bir `PivotFilter` kaydı oluşturur ve Excel 2007 veya sonraki sürümlerini gerektirir. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan özet tablo varsayılan olarak tüm öğeleri gösterir. Eski araçlarla gidiş-dönüş işlemi gerektiren belgelerde `top_10_auto_show` tercih edilmelidir; modern çalışma kitaplarında ise diğer değer filtreleriyle birlikte kullanılabilmesi nedeniyle `filter_top10` tercih edilmelidir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tabloları Etikete veya Değere Göre Filtreleme](/cells/tr/python-net/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-net/pivot-table-add-row-and-column-fields/)
- [Özet Tablosundaki Alanları Gruplandırma](/cells/tr/python-net/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/python-net/refresh-pivot-table/)
- [Özet Tablosuna Sayfa Alanı Ekleme](/cells/tr/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}