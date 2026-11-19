---
title: Özet Tabloda İlk 10 Öğeyi Gösterme veya Filtreleme
linktitle: Özet Tabloda İlk 10 Öğeyi Gösterme veya Filtreleme
description: Aspose.Cells for Python via Java kullanarak bir özet tablo alanında yalnızca en üst veya en alt sıralı öğelerin nasıl gösterileceğini öğrenin. Bu makale, Excel 97-2003 top10AutoShow yöntemini, Top10AutoShowSettings ile seçeneklerin okunmasını ve filterTop10 aracılığıyla Excel 2007-365 İlk 10 Filtresini ele alır.
keywords: Aspose.Cells for Python via Java, özet tablo, ilk 10, otomatik gösterim, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /tr/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alanda düzinelerce üye bulunduğunda okunması zor olabilir. İlk 10 raporu yalnızca en yüksek veya en düşük sıralı öğeleri tutar; bu da sıralama raporlarının ihtiyaç duyduğu işlevi sağlar: "satış gelirine göre ilk 5 ürün" veya "satış sayısına göre en düşük 3 bölge". Aspose.Cells bunun için iki mekanizmayı destekler ve bu mekanizmalar Microsoft Excel'in iki nesline karşılık gelir.
- **Excel 97-2003 Otomatik Gösterme (`AutoShow`)** — `PivotField.top10AutoShow()` yöntemi. Bu, doğrudan özet tablo alanında saklanan klasik "En üst/En alt N öğeyi göster" ayarıdır. Excel'in hem eski hem yeni tüm sürümlerinde çalışır; çünkü ilk özet tablo biçiminin bir parçasıdır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.filterTop10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri, İlk 10... seçeneğinde bulunan modern İlk 10 değer filtresidir. Alanla ilişkilendirilmiş `PivotFilter` nesnesi olarak saklanır ve öğe sayısına ve yüzdeye dayalı sıralama sunar.

## **Excel 97-2003'te İlk 10 Gösterimi (top10AutoShow)**
Klasik AutoShow, `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` çağrısıyla yapılandırılır:
- `isAutoShow` — alandaki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `isTop` — `True`, en yüksek sıralı öğeleri (Üst) tutar; `False`, en düşük sıralı öğeleri (Alt) tutar.
- `count` — korunacak öğe sayısı; örneğin klasik İlk 10 raporu için 10.
- `rankBy` — öğeleri sıralayan **veri alanının** sıfırdan başlayan indeksi. Öğeleri alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama, bir değer alanına veya alanın kendisine göre belirlenebilir. Aşağıda bu iki doğal varyant gösterilmektedir.

### **Bir Değer Alanına Göre Sıralama**
Satır alanının öğelerini `Sum of Sales` gibi olağan bir değer alanına göre sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur; ardından satışlara göre en üst 2 sporu gösterir. `rankBy` değeri 0'dır; çünkü `Sum of Sales`, 0. dizindeki veri alanıdır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Alanın Kendisine Göre Sıralama**
Bir alan kendisiyle de sıralanabilir; bu durumda `rankBy` parametresine -1 değerini geçirin. Bu varyant için ek bir veri alanı gerekmez; alanın satır (veya sütun) alanına yerleştirilmiş olması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en alt 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 biçimin varsayılan değeri olduğundan `rankBy` özniteliği özet tablo XML'inden çıkarılır ve `Top10AutoShowSettings.getRankBy()` -1 değerini döndürür.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Geçerli Seçenekleri Okuma (Top10AutoShowSettings)**
`PivotField.getTop10AutoShowSettings()` yöntemi, alanda hâlihazırda saklanan AutoShow seçeneklerini sunan bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Mevcut bir çalışma kitabında veya yeni yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için kullanın; bu, dosyadan yüklenen çalışma kitapları için de geçerlidir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

Dört özellik, özet tablo XML'ine yazılan klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir. Dolayısıyla okunan değerler, Excel'in her sürümünün dikkate alacağı değerlerdir.

## **Not**

{{% alert color="primary" %}}
- Doğrudan `PivotField` erişim yöntemleri `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` ve `getAutoShowField()` kullanımdan kaldırılmış olarak işaretlenmiştir. Bunun yerine `Top10AutoShowSettings` nesnesini kullanın: `PivotField.isAutoShow()` yerine `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` yerine `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` yerine `Top10AutoShowSettings.getAutoShowCount()` ve `PivotField.getAutoShowField()` yerine `Top10AutoShowSettings.getRankBy()` kullanılır. `top10AutoShow()` yöntemi, ayarları değiştirmek için desteklenen yöntemdir.
- `top10AutoShow`, satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alan bu şekilde sıralanamaz; çünkü öğeleri özet tablo gövdesinde yer almaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (filterTop10)**
Modern Excel sürümleri, İlk 10'u alan menüsünde bir değer filtresi olarak sunar (Değer Filtreleri, İlk 10...). Aspose.Cells bunu, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` yöntemiyle temsil eder:
- `valueFieldIndex` — öğeleri toplulaştırılmış değerlerine göre sıralayan veri alanının sıfırdan başlayan indeksi.
- `type` — `itemCount` değerinin ne anlama geldiğini belirtir. `PivotFilterType.COUNT` sabit sayıda öğe tutar (iletişim kutusunun Öğeler seçeneği). `PivotFilterType.PERCENT` öğelerin belirli bir yüzdesini tutar; dolayısıyla `itemCount` yüzde değerinin kendisidir — 30 değeri, öğelerin en üst %30'unu tutar. `PivotFilterType.SUM` kümülatif değer kapsamına göre sıralar.
- `isTop` — Üst için `True`, Alt için `False`.
- `itemCount` — İlk N içindeki N; birimi `type` değerine bağlıdır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` ve `filterTop10` iki ayrı özelliktir. AutoShow, özet tablo alanında ayarlanan klasik `autoShow` özniteliğini yazar ve Excel 97'den itibaren tüm Excel sürümlerinde dikkate alınır. `filterTop10` ise modern bir `PivotFilter` kaydı yazar ve Excel 2007 veya sonrasını gerektirir. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan bir özet tablo tüm öğeleri gösterir duruma geri döner. Eski araçlarda korunup yeniden yüklenmesi gereken belgelerde `top10AutoShow`; modern çalışma kitaplarında ise diğer değer filtreleriyle birleştirilebildiği için `filterTop10` tercih edilmelidir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-java/pivot-table-add-row-and-column-fields/)
- [Özet Tablosunda Özet Tablo Alanlarını Gruplama](/cells/tr/python-java/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/python-java/refresh-pivot-table/)
- [Özet Tablosuna Sayfa Alanı Ekleme](/cells/tr/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}