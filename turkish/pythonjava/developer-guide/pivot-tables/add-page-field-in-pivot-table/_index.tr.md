---
title: Aspose.Cells for .NET'te PivotTable'a filtre alanları ekleme
linktitle: Filtre Alanları Ekleme
description: Aspose.Cells for Python via Java kullanarak özet tablolarda filtre alanlarını eklemeyi ve yapılandırmayı öğrenin; filtre alanı ekleme, tekli seçim filtreleme ve çoklu seçim filtreleme dahil.
keywords: Aspose.Cells, Python, Java, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter, özet tablo, filtre alanı, filtreleme
type: docs
weight: 250
url: /tr/python-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, özet tablolardaki filtre alanlarının tüm yaşam döngüsünü destekler. Bir filtre alanını üst düzey kolaylık API'si veya alt düzey `page_fields` koleksiyonu aracılığıyla ekleyebilir, filtreni tekli seçim modunda çalıştırabilir, her sayfa öğesini göstermek için temizleyebilir ya da Excel'deki onay kutusu kullanıcı arayüzü aracılığıyla kullanıcıların aynı anda birden fazla sayfa öğesi seçmesine olanak tanımak için alanı çoklu seçime geçirebilirsiniz.
{{% /alert %}}

## **Giriş**

Bir filtre alanı, özet tablo gövdesinin kaynak verilerin *hangi alt kümesini* görüntüleyeceğini kontrol eden bir pivot alanıdır. Son kullanıcılar bunu Excel'de işlenmiş bir pivot tablonun üst kısmında bir açılır liste olarak görür ve mevcut sayfa öğelerinden birini seçmek, özet tablo gövdesini yalnızca o sayfa öğesine ait kayıtların özetleneceği şekilde yeniden oluşturur. Bir pivot alanı, `PivotFieldType.ROW`, `PivotFieldType.COLUMN` veya `PivotFieldType.DATA` yerine `PivotFieldType.PAGE` olarak kaydedildiğinde filtre alanı haline gelir.

Bir filtre alanı iki davranışta çalışabilir. Varsayılan **tekli seçim** davranışında aynı anda yalnızca bir sayfa öğesi görünür, dolayısıyla özet tablo gövdesi tam olarak bir alt kümeyi özetler. **Çoklu seçim** davranışında ise alan bir onay kutusu listesi sunar ve özet tablo gövdesi işaretlenen her sayfa öğesinin birleşimini özetler. Aynı kaynak alan, tek bir özellik değiştirilerek bu davranışlar arasında ileri geri taşınabilir.

Aspose.Cells for Python via Java, bir filtre alanını kaydetmek için iki eşdeğer yol sunar. Üst düzey API, kaynak sütun adını alan ve tek bir çağrıda alanı ekleyen `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` yöntemidir. Alt düzey API ise zaten bir `PivotField` referansına sahip olduğunuzda ve aynı alan örneğini filtre alanına eklemek istediğinizde kullanılan `PivotTable.page_fields.add(PivotField)` yöntemidir. Her iki API de aynı `page_fields` koleksiyonunu doldurur ve bu makalenin devamında bunlar arasında nasıl seçim yapılacağı ve her bir filtreleme modunun nasıl çalıştırılacağı gösterilmektedir.

## **filtre alanı Ekleme**

Bir pivot alanını filtre alanına kaydetmenin iki yolu vardır. Üst düzey çağrı, kaynak sütun adını bir dize olarak alır ve en yaygın yoldur. Alt düzey çağrı, mevcut bir `PivotField` örneğini kabul eder ve aynı alan nesnesinin birden fazla pivot alanında yeniden kullanılması gerektiğinde kullanışlıdır. Her iki çağrı da alanı `PivotTable.page_fields` içine yerleştirir; ardından alan, işlenmiş pivot tablonun üst kısmında sayfa açılır listesi olarak görünür.

### add_field_to_area ile filtre alanı Ekleme

Aşağıdaki örnek, küçük bir Meyve / Yıl / Tutar veri kümesi oluşturur, E3 hücresine bir özet tablo yerleştirir; satır alanında `Fruit`, veri alanında `Amount` ve filtre alanında `Year` bulunur, pivot tabloyu yeniler ve çalışma kitabını kaydeder.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Yeni bir çalışma kitabı oluştur
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Başlık satırını ayarla
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 satır örnek veri doldur: Meyve, Yıl, Miktar
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# E3 hücresine sabitlenmiş bir özet tablo ekle
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Alanları ilgili alanlara ekle: Fruit Satır, Amount Veri, Year Sayfa alanı olarak
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Özet tablo verilerini yenile ve hesapla
pivotTable.refreshData()
pivotTable.calculateData()

# Çalışma kitabını kaydet
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### page_fields.add ile filtre alanı Ekleme

Zaten bir `PivotField` örneği ile çalışıyorsanız, onu doğrudan `PivotTable.page_fields.add` yöntemine geçebilirsiniz. Özet tablo ve filtre alanı, önceki senaryodaki ile tam olarak aynı şekilde oluşturulur; yalnızca son filtre alanı kayıt işlemi alt düzey API çağrısıyla değiştirilir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — Pivot tablosu ve sayfa alanı tam olarak Senaryo 1a'daki gibi
#   oluşturulur (Fruit/Year/Amount verileri, pivot E3'te, Fruit→Satır,
#   Amount→Veri). Aşağıda, Year PivotField'ını BaseFields koleksiyonundan
#   alıp PageFields.Add'a geçiriyoruz — AddFieldToArea'nın düşük seviyeli
#   alternatifidir. Sonuç işlevsel olarak Senaryo 1a ile aynıdır.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Başlıklar
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# Örnek veri (9 satır)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# E3 konumunda A1:C10 aralığını kapsayan pivot tablo ekle
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Fruit -> Satır, Amount -> Veri (Year aşağıda Sayfa alanına eklenecek)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Düşük seviyeli yaklaşım: mevcut Year PivotField'ını BaseFields üzerinden
# alıp PageFields.Add(PivotField) ile Sayfa alanına kaydedin.
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# Yeni sayfa alanının kaydedilen çalışma kitabına yansıtılması için yenile
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Tekli Seçim Filtreleme (Bir Sayfa Öğesi Gösterme)**

Varsayılan tekli seçim davranışında, filtre alanı tek bir açılır liste olarak işlenir ve `PivotField.current_page_item` tamsayısı, özet tablo gövdesini hangi sayfa öğesinin çalıştıracağını seçer. Belirli bir indeks atamak o tek öğeyi seçer; özel koruyucu değer olan `0x7FFD` (ondalık 32765) atamak ise filtreyi temizler, böylece her sayfa öğesi aynı anda özetlenir. Tekli seçim varsayılandır; bunu açıkça etkinleştirmeniz gerekmez.

### Tüm Öğeleri Gösterme

`current_page_item` öğesini sihirli değer olan `0x7FFD` olarak ayarlamak, filtreni temizlemekle eşdeğerdir: özet tablo gövdesi, hiçbir filtre uygulanmamış gibi her sayfa öğesini özetler.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Yeni bir çalışma kitabı oluştur
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Meyve/Yıl/Miktar verilerini doldur
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# E3 konumunda özet tablo oluştur
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# Özet alanlarını yapılandır: Fruit→Satır, Amount→Veri, Year→Sayfa
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.refreshData()
pivotTable.calculateData()

# Sayfa filtresini temizle, böylece sayfa alanındaki her öğe görünür olsun.
# 0x7FFD (ondalık 32765), "tüm öğeler" anlamına gelen özel sentinel değeridir —
# Excel'deki sayfa alanı açılır menüsünde "(Tümü)" seçmeye eşdeğerdir.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Tek Bir Belirli Öğeyi Gösterme

`current_page_item` öğesini gerçek bir indekse ayarlamak yalnızca o tek sayfa öğesini seçer. İndeks, filtre alanının sıralanmış öğe listesindeki öğenin konumudur; dolayısıyla örneğin `1` sıralamadan sonraki ikinci öğeyi seçer.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Çalışma kitabı oluştur
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Örnek veri ekle (Meyve/Yıl/Tutar)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# E3'e özet tablo ekle
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Alan ekle: Meyve→Satır, Tutar→Veri, Yıl→Sayfa
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Sayfa alanına özel işlemler
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = sıralı listedeki ikinci öğe (ör. "2021")

# Özet tabloyu yenile ve hesapla
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Çoklu Seçim Filtreleme**

Çoklu seçim filtreleme, sayfa açılır listesini bir onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birden fazla sayfa öğesi seçmesine olanak tanır. Aspose.Cells, birlikte çalışan iki özellik sunar. Çoklu seçim kullanıcı arayüzünün hiç etkili olmaması için `PivotField.is_multiple_item_selection_allowed` öğesinin önce `True` olarak ayarlanması gerekir. Etkinleştirildikten sonra, `PivotItem.is_hidden` öğesinin onay kutusu listesinde hangi öğelerin görüneceğini kontrol etmesi sağlanır; böylece her öğeyi gösterebilir veya yalnızca belirli öğeleri beyaz listeye alabilirsiniz.

Aşağıdaki kod, Senaryo 1a'da oluşturulan aynı Year filtre alanında çoklu seçimi etkinleştirir ve ardından iki model gösterir: Bölüm A, her giriş için `is_hidden` öğesini `False` olarak bırakarak her sayfa öğesini ortaya çıkarır; Bölüm B ise yalnızca seçtiğiniz kaynak değerleri beyaz listeye alır ve bir `switch (pivot_items[i].get_string_value())` bloğu aracılığıyla diğer her şeyi gizler.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — Pivot tablosu ve sayfa alanı tam olarak şu şekilde oluşturulur
#   Senaryo 1a'da olduğu gibi (Fruit/Year/Amount verileri, E3'te pivot, Fruit→Satır,
#   Amount→Veri, Year→Sayfa AddFieldToArea aracılığıyla).
#   Aşağıda sayfa alanına çoklu seçim filtreleme uyguluyoruz.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Örnek veri: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Sayfa alanında çoklu seçimi etkinleştir
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Bölüm A — TÜM öğeleri seç (her öğeyi görünür yap)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Bölüm B — Yalnızca kaynak değere göre belirli öğeleri seç
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **Not:** `PivotItem.is_hidden` aracılığıyla çoklu seçim filtreleme kullanılırken, **en az bir `PivotItem` görünür kalmalıdır** (`is_hidden == False`). Tüm öğeler gizlenirse, Excel dosyayı açarken ya çöker ya da boş bir pivot tablo işler. Çoklu seçim beyaz listenizin kaynak verilerinizden en az bir öğe içerdiğini her zaman doğrulayın.

## **Hangi API'yi ve Hangi Modu Kullanmalıyım?**

Aşağıdaki tablo, her senaryoyu ayrıntılı olarak okumadan doğru kombinasyonu seçebilmeniz için her API'nin ve modun ne zaman kullanılacağını özetler.

| Senaryo / Kullanım Durumu | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| Kaynak sütun adına göre filtre alanı ekleme (en yaygın) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/a | Üst düzey, tek satır. Bir `PivotField` referansına ihtiyacınız olmadığı sürece bunu kullanın. |
| Zaten bir `PivotField` nesneniz olduğunda filtre alanı ekleme | `PivotTable.page_fields.add(PivotField)` | n/a | Alan nesnesi başka yerden alındığında veya yeniden kullanılması gerektiğinde kullanın. |
| Tek bir sayfa öğesine filtreleme (varsayılan mod) | `PivotField.current_page_item` | belirli bir indekse ayarlayın | Örneğin, `1` sıralanmış listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / filtreni temizleme | `PivotField.current_page_item` | `0x7FFD` olarak ayarlayın | Sihirli değer olan `0x7FFD` (ondalık 32765), "tüm öğeler" için koruyucu değerdir. |
| Excel'de çoklu seçim kullanıcı arayüzünü etkinleştirme | `PivotField.is_multiple_item_selection_allowed` | `True` olarak ayarlayın | Herhangi bir `is_hidden` çağrısının etkili olmasından önce gereklidir. |
| Çoklu seçim listesinde tek tek öğeleri gizleme / gösterme | `PivotItem.is_hidden` | öğe başına ayarlayın | En az bir öğe görünür kalmalıdır (`is_hidden == False`). |

{{% alert color="primary" %}}
Çoklu seçim filtrelemeyi yapılandırırken görünürlük kısıtlamasını her zaman hatırlayın. Çoklu seçim filtre alanındaki her `PivotItem` gizlenmişse, Excel dosyayı açarken çöker veya boş bir pivot tablo işler. Beyaz listenizi, en az bir öğenin görünür kalacağı şekilde kaynak verilerinize göre oluşturun; böylece kaydedilen çalışma kitaplarınız her makinede güvenilir şekilde açılır.
{{% /alert %}}



{{< app/cells/assistant language="python" >}}