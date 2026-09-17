---
title: Aspose.Cells for Python via Java ile Pivot Tablosuna Filtre Alanları Ekleme
linktitle: Aspose.Cells for Python via Java ile Pivot Tablosuna Filtre Alanları Ekleme
description: Aspose.Cells for Python via Java kullanarak Pivot Tablolarında filtre alanlarını nasıl ekleyeceğinizi ve yapılandıracağınızı öğrenin; filtre alanı ekleme, tekli seçim filtreleme ve çoklu seçim filtreleme dahil.
keywords: Aspose.Cells, Python, Java, Pivot Tablosu, filtre alanı, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /tr/python-java/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Pivot Tablolarında filtre alanlarının tüm yaşam döngüsünü destekler. Üst düzey bir kolaylık API'si veya alt düzey `page_fields` koleksiyonu aracılığıyla bir filtre alanı ekleyebilir, filtreyi tekli seçim modunda yönetebilir, her filtre öğesini göstermek için temizleyebilir ya da alanı çoklu seçime geçirerek kullanıcıların Excel'deki onay kutusu arayüzü aracılığıyla aynı anda birkaç filtre öğesi seçmesine olanak tanıyabilirsiniz.
{{% /alert %}}

## **Giriş**
Bir filtre alanı, Pivot Tablosu gövdesinin kaynak verilerin *hangi alt kümesini* görüntüleyeceğini kontrol eden bir Pivot alanıdır. Son kullanıcılar bunu Excel'de işlenmiş bir Pivot Tablosunun üst kısmında bir açılır menü olarak görür ve kullanılabilir filtre öğelerinden birinin seçilmesi, Pivot Tablosu gövdesini yalnızca o filtre öğesine ait kayıtların özetleneceği şekilde yeniden oluşturur. Bir Pivot alanı, `PivotFieldType.ROW`, `PivotFieldType.COLUMN` veya `PivotFieldType.DATA` yerine `PivotFieldType.PAGE` olarak kaydedildiğinde filtre alanı haline gelir.

## **Filtre Alanı Ekleme**

### add_field_to_area ile Filtre Alanı Ekleme
Aşağıdaki örnek, küçük bir Meyve / Yıl / Tutar veri kümesi oluşturur, E3 hücresine bir Pivot Tablosu yerleştirir; satır alanında `Fruit` (Meyve), veri alanında `Amount` (Tutar) ve filtre alanında `Year` (Yıl) bulunur, Pivot Tablosunu yeniler ve çalışma kitabını kaydeder.

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
# 9 satır örnek veri doldur: Fruit, Year, Amount
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
# E3 hücresine sabitlenmiş bir pivot tablo ekle
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Alanları bölgelerine ekle: Satır olarak Fruit, Veri olarak Amount, Sayfa alanı olarak Year
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")
# Pivot tablo verilerini yenile ve hesapla
pivotTable.calculateData()
# Çalışma kitabını kaydet
workbook.save("pageFieldSample.xlsx")
jpype.shutdownJVM()
```

### page_fields.add ile Filtre Alanı Ekleme
Zaten bir `PivotField` örneğiyle çalışıyorsanız, onu doğrudan `PivotTable.page_fields.add` yöntemine geçirebilirsiniz. Pivot Tablosu ve filtre alanı önceki senaryodakiyle tamamen aynı şekilde oluşturulur; yalnızca son filtre alanı kaydı alt düzey API çağrısıyla değiştirilir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType
# — Pivot tablosu ve sayfa alanı tam olarak Senaryo 1a'daki gibi oluşturulur
#   (Meyve/Yıl/Tutar verileri, pivot E3'te, Meyve→Satır,
#   Tutar→Veri). Aşağıda BaseFields koleksiyonundan Year PivotField'ını
#   alıp PageFields.Add'a geçiriyoruz — bu, AddFieldToArea'nın
#   düşük seviyeli alternatifidir. Sonuç, Senaryo 1a ile işlevsel olarak
#   aynıdır.
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
# Başlıklar
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")
# Örnek veriler (9 satır)
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
# Meyve -> Satır, Tutar -> Veri (Year aşağıda Sayfa alanına gidecek)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Düşük seviyeli yaklaşım: mevcut Year PivotField'ını BaseFields'tan al
# ve PageFields.Add(PivotField) ile Sayfa alanına kaydet.
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)
# Yeni sayfa alanının kaydedilen çalışma kitabında yansıtılması için yenile
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Tekli Seçim Filtreleme (Tek Bir Filtre Öğesi Gösterme)**
Varsayılan tekli seçim davranışında, filtre alanı tek bir açılır menü olarak işlenir ve `PivotField.current_page_item` tamsayısı, Pivot Tablosu gövdesini hangi filtre öğesinin yönlendireceğini seçer. Belirli bir dizin atamak o öğeyi seçer; özel sınır değeri `0x7FFD` (ondalık 32765) atamak filtreyi temizler ve böylece her filtre öğesi aynı anda özetlenir. Tekli seçim varsayılan davranıştır; bunu açıkça etkinleştirmeniz gerekmez.

### Tüm Öğeleri Gösterme
`current_page_item` değerini sihirli değer olan `0x7FFD` olarak ayarlamak, filtreyi temizlemek ile eşdeğerdir: Pivot Tablosu gövdesi, hiçbir filtre uygulanmamış gibi her filtre öğesini özetler.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Yeni bir çalışma kitabı oluştur
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
# Fruit/Year/Amount verilerini doldur
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
# E3 konumunda pivot tablo oluştur
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)
# Pivot alanlarını yapılandır: Fruit→Satır, Amount→Veri, Year→Sayfa
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
pivotTable.calculateData()
# Sayfa filtresini temizle, böylece sayfa alanındaki her öğe görünür olsun.
# 0x7FFD (ondalık 32765), "tüm öğeler" anlamına gelen özel sentinel değeridir —
# Excel'in sayfa alanı açılır menüsünde "(Tümü)" seçmeye eşdeğerdir.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

### Tek Bir Belirli Öğeyi Gösterme
`current_page_item` değerini gerçek bir dizine ayarlamak yalnızca o filtre öğesini seçer. Dizin, filtre alanının sıralanmış öğe listesindeki öğenin konumudur; dolayısıyla örneğin `1` sıralamadan sonra ikinci öğeyi seçer.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create workbook
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Add sample data (Fruit/Year/Amount)
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
# Add pivot table at E3
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)
# Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")
# Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = second item in sorted order (e.g. "2021")
# Refresh and calculate pivot table
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Çoklu Seçim Filtreleme**
Çoklu seçim filtreleme, filtre açılır menüsünü bir onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birkaç filtre öğesi seçmesine olanak tanır. Aspose.Cells birlikte çalışan iki özellik sunar. Çoklu seçim kullanıcı arayüzünün geçerli olabilmesi için `PivotField.is_multiple_item_selection_allowed` değerinin `True` olarak ayarlanması gerekir. Etkinleştirildikten sonra, `PivotItem.is_hidden` onay kutusu listesinde hangi öğelerin görüneceğini kontrol eder; böylece her öğeyi gösterebilir veya yalnızca belirli öğeleri beyaz listeye alabilirsiniz.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re
# — Pivot tablosu ve sayfa alanı tam olarak
#   Senaryo 1a'daki gibi oluşturulur (Fruit/Year/Amount verileri, pivot E3'te, Fruit→Satır,
#   Amount→Veri, Year→Sayfa AddFieldToArea aracılığıyla).
#   Aşağıda sayfa alanında çoklu seçim filtrelemesi uyguluyoruz.
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
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

> **Not:** `PivotItem.is_hidden` aracılığıyla çoklu seçim filtreleme kullanılırken, **en az bir `PivotItem` görünür kalmalıdır** (`is_hidden == False`). Her öğe gizliyse, Excel dosyayı açarken ya kilitlenir ya da boş bir Pivot Tablosu işler. Çoklu seçim beyaz listenizin kaynak verilerinizden en az bir öğe içerdiğini her zaman doğrulayın.

## **Hangi API'yi ve Hangi Modu Kullanmalıyım?**
Aşağıdaki tablo, her senaryoyu ayrıntılı olarak okumak zorunda kalmadan doğru kombinasyonu seçebilmeniz için her API'nin ve modun ne zaman kullanılacağını özetler.
| Senaryo / Kullanım Durumu | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| Kaynak sütun adına göre filtre alanı ekleme (en yaygın) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | yok | Üst düzey, tek satırlık. Bir `PivotField` referansına ihtiyacınız olmadığı sürece bunu kullanın. |
| Zaten bir `PivotField` nesneniz olduğunda filtre alanı ekleme | `PivotTable.page_fields.add(PivotField)` | yok | Alan nesnesi başka yerden alındığında veya yeniden kullanılması gerektiğinde kullanın. |
| Tek bir filtre öğesine filtreleme (varsayılan mod) | `PivotField.current_page_item` | belirli bir dizine ayarla | Örneğin, `1` sıralanmış listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / filtreyi temizleme | `PivotField.current_page_item` | `0x7FFD` olarak ayarla | Sihirli değer olan `0x7FFD` (ondalık 32765), "tüm öğeler" için sınır değeridir. |
| Excel'de çoklu seçim kullanıcı arayüzünü etkinleştirme | `PivotField.is_multiple_item_selection_allowed` | `True` olarak ayarla | `is_hidden` çağrılarının geçerli olabilmesi için önce ayarlanmalıdır. |
| Çoklu seçim listesinde tek tek öğeleri gizleme / gösterme | `PivotItem.is_hidden` | öğe başına ayarla | En az bir öğe görünür kalmalıdır (`is_hidden == False`). |

{{% alert color="primary" %}}
Çoklu seçim filtrelemeyi yapılandırırken görünürlük kısıtlamasını her zaman hatırlayın. Çoklu seçim filtre alanındaki her `PivotItem` gizliyse, Excel açılışta kilitlenir veya boş bir Pivot Tablosu işler. Beyaz listenizi kaynak verilerinize göre oluşturarak en az bir öğenin görünür kalmasını sağlayın; böylece kaydedilen çalışma kitaplarınız her makinede güvenilir şekilde açılır.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}