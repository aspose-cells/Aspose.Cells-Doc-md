---
title: Özet Tablosunda İlk 10 Öğeyi Göster veya Filtrele
linktitle: Özet Tablosunda İlk 10 Öğeyi Göster veya Filtrele
description: Aspose.Cells for Python via Java kullanarak bir pivot alanında yalnızca en üst veya en alt sıralı öğelerin nasıl gösterileceğini öğrenin. Bu makale; Excel 97-2003 top10AutoShow yöntemini, Top10AutoShowSettings ile seçeneklerin okunmasını ve filterTop10 aracılığıyla Excel 2007-365 İlk 10 Filtresi'ni ele alır.
keywords: Aspose.Cells for Python via Java, özet tablo, ilk 10, otomatik gösterim, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /tr/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alan onlarca üye içerdiğinde okunması zor olabilir. İlk 10 raporu yalnızca en yüksek veya en düşük sıralı öğeleri korur; sıralama raporlarının gerektiği tam olarak budur — "gelire göre ilk 5 ürün" veya "satış sayısına göre son 3 bölge". Aspose.Cells bunun için iki mekanizma destekler ve bu mekanizmalar Microsoft Excel'in iki nesline karşılık gelir.
- **Excel 97-2003 AutoShow** — `PivotField.top10AutoShow()` yöntemi. Bu, pivot alanında doğrudan saklanan klasik "En üst/en alt N öğeyi göster" ayarıdır. Eski ve yeni sürümler dâhil tüm Excel sürümlerinde çalışır; çünkü özgün özet tablo biçiminin bir parçasıdır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.filterTop10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri bölümünde bulunan modern İlk 10 değer filtresidir. Alanla ilişkilendirilmiş bir `PivotFilter` nesnesi olarak saklanır ve öğe sayısına ve yüzdeye dayalı sıralama sunar.

## **Excel 97-2003'te İlk 10 Gösterimi (top10AutoShow)**
Klasik AutoShow, `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` yöntemine yapılan tek bir çağrıyla yapılandırılır:
- `isAutoShow` — alandaki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `isTop` — `True`, en yüksek sıralı öğeleri (Üst) korur; `False`, en düşük sıralı öğeleri (Alt) korur.
- `count` — kaç öğenin korunacağını belirtir; örneğin klasik bir İlk 10 raporu için 10.
- `rankBy` — öğeleri sıralayan **veri alanının** sıfırdan başlayan dizini. Öğeleri alanın kendisine göre sıralamak için -1 değerini belirtin.
Sıralama, bir değer alanı veya alanın kendisi tarafından belirlenebilir. Aşağıda bu iki doğal varyant gösterilmektedir.

### **Değer Alanına Göre Sıralama**
Satır alanının öğelerini, Satışların Toplamı gibi standart bir değer alanına göre sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur ve ardından satışlara göre ilk 2 sporu gösterir. `rankBy` 0'dır; çünkü "Satışların Toplamı", 0 dizinindeki veri alanıdır.

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
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Alanın Kendisine Göre Sıralama**
Bir alan kendisi üzerinden de sıralanabilir — `rankBy` olarak -1 değerini geçirin. Bu varyant için ek bir veri alanı gerekmez; alanın yalnızca satır (veya sütun) alanında bulunması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en düşük 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 biçimin varsayılan değeri olduğu için `rankBy` özniteliği özet tablo XML'inden çıkarılır ve `Top10AutoShowSettings.getRankBy()` çağrısı -1 değerini döndürür.

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
# Alanın kendisine göre sıralanan en alt 3 öğeyi göster (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Mevcut Seçenekleri Okuma (Top10AutoShowSettings)**
`PivotField.getTop10AutoShowSettings()` yöntemi, alanda hâlihazırda saklanan AutoShow seçeneklerini sunan bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Mevcut bir çalışma kitabında veya yeni yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için bu yöntemi kullanın; dosyadan yüklenen çalışma kitapları da kapsamdadır.

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

Dört özellik, özet tablo XML'ine yazılan klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir. Bu nedenle geri okunan değerler, her Excel sürümünün dikkate alacağı değerlerdir.

## **Not**

{{% alert color="primary" %}}
- Doğrudan `PivotField` erişimcileri `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` ve `getAutoShowField()` kullanımdan kaldırılmış olarak işaretlenmiştir. Bunun yerine `Top10AutoShowSettings` nesnesini kullanın: `PivotField.isAutoShow()` karşılığı `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` karşılığı `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` karşılığı `Top10AutoShowSettings.getAutoShowCount()` ve `PivotField.getAutoShowField()` karşılığı `Top10AutoShowSettings.getRankBy()` olur. `top10AutoShow()` yöntemi, ayarları değiştirmek için desteklenen yöntemdir.
- `top10AutoShow`, satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alan, öğeleri özet tablo gövdesinde yerleşmediği için bu şekilde sıralanamaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (filterTop10)**
Modern Excel sürümleri, İlk 10 filtresini alan menüsünde bir değer filtresi olarak sunar (Değer Filtreleri, İlk 10...). Aspose.Cells bunu, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` yöntemiyle temsil eder:
- `valueFieldIndex` — öğelerin sıralamasını belirleyen toplulaştırılmış değerlerin ait olduğu veri alanının sıfırdan başlayan dizini.
- `type` — `itemCount` değerinin neyi belirttiğini tanımlar. `PivotFilterType.COUNT` sabit sayıda öğe korur (iletişim kutusunun Öğeler seçeneği). `PivotFilterType.PERCENT` öğelerin belirli bir yüzdesini korur; dolayısıyla `itemCount` doğrudan yüzde değeridir — 30 değeri, en üst yüzde 30'luk öğe kümesini korur. `PivotFilterType.SUM` kümülatif değer kapsamına göre sıralar.
- `isTop` — `True`, Üst seçeneğini; `False`, Alt seçeneğini belirtir.
- `itemCount` — İlk N'deki N değeridir; birimi `type` değerine bağlıdır.

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
    # İlk 10 Filtresi — öğeleri "Satışların Toplamı" ölçütüne göre en üst 2 ile sınırlayın (veri alanı dizini 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # Bunun yerine yüzdeye dayalı bir filtre kullanmak için öğelerin en üst %30'unu koruyun:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` ve `filterTop10` iki ayrı özelliğidir. AutoShow, pivot alanında ayarlanan klasik `autoShow` özniteliğini yazar ve Excel 97'den başlayarak tüm Excel sürümlerinde dikkate alınır. `filterTop10`, Excel 2007 veya sonrasını gerektiren modern bir `PivotFilter` kaydı yazar. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan bir özet tablo tüm öğeleri gösterme durumuna geri döner. Eski araçlarla işlenip yeniden kaydedilmesi gereken belgelerde `top10AutoShow` tercih edin; modern çalışma kitaplarında ise diğer değer filtreleriyle birleştirilebildiği için `filterTop10` tercih edin.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablolarını Etiket veya Değere Göre Filtreleme](/cells/tr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-java/pivot-table-add-row-and-column-fields/)
- [Özet Tablosundaki Pivot Alanlarını Gruplandırma](/cells/tr/python-java/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/python-java/refresh-pivot-table/)
- [Özet Tablosuna Sayfa Alanı Ekleme](/cells/tr/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}