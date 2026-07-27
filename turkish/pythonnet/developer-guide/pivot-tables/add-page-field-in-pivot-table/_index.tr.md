---
title: Aspose.Cells for .NET'te PivotTable'a filtre alanları ekleme
linktitle: Filtre Alanları Ekleme
description: Aspose.Cells for Python via .NET kullanarak özet tablolarda filtre alanlarını nasıl ekleyeceğinizi ve yapılandıracağınızı, filtre alanı ekleme, tekli seçim filtreleme ve çoklu seçim filtreleme dahil öğrenin.
keywords: Aspose.Cells, Python via .NET, özet tablo, filtre alanı, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /tr/python-net/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, özet tablolardaki filtre alanlarının tüm yaşam döngüsünü destekler. Üst düzey kolaylık API'si veya daha düşük seviyeli `page_fields` koleksiyonu aracılığıyla bir filtre alanı ekleyebilir, filtreni tekli seçim modunda çalıştırabilir, her sayfa öğesini göstermek için temizleyebilir ya da Excel'deki onay kutusu kullanıcı arayüzü aracılığıyla kullanıcıların aynı anda birden fazla sayfa öğesi seçmesine olanak tanımak için alanı çoklu seçime geçirebilirsiniz.
{{% /alert %}}

## **Giriş**

filtre alanı, özet tablo gövdesinin kaynak verilerin *hangi alt kümesini* görüntüleyeceğini kontrol eden bir pivot alanıdır. Son kullanıcılar bunu Excel'de işlenmiş bir özet tablo'nun üst kısmında bir açılır menü olarak görür ve mevcut sayfa öğelerinden birini seçmek, yalnızca o sayfa öğesine ait kayıtların özetlenmesi için özet tablo gövdesini yeniden oluşturur. Bir pivot alanı, `PivotFieldType.ROW`, `PivotFieldType.COLUMN` veya `PivotFieldType.DATA` yerine `PivotFieldType.PAGE` olarak kaydedildiğinde filtre alanı olur.

Bir filtre alanı iki davranışta çalışabilir. Varsayılan **tekli seçim** davranışında aynı anda yalnızca bir sayfa öğesi görünür, böylece özet tablo gövdesi tam olarak bir alt kümeyi özetler. **Çoklu seçim** davranışında ise alan bir onay kutusu listesi sunar ve özet tablo gövdesi, işaretlenen her sayfa öğesinin birleşimini özetler. Aynı kaynak alan, tek bir özelliği değiştirerek bu davranışlar arasında ileri geri taşınabilir.

Aspose.Cells for Python via .NET, bir filtre alanını kaydetmek için eşdeğer iki yol sunar. Üst düzey API, kaynak-sütun adını alan ve alanı tek bir çağrıda ekleyen `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` yöntemidir. Daha düşük seviyeli API ise, zaten bir `PivotField` referansına sahip olduğunuzda ve aynı alan örneğini filtre alanına eklemek istediğinizde kullanılan `PivotTable.page_fields.add(PivotField)` yöntemidir. Her iki API de aynı `page_fields` koleksiyonunu doldurur ve bu makalenin geri kalanı aralarında nasıl seçim yapılacağını ve her filtreleme modunun nasıl çalıştırılacağını gösterir.

## **filtre alanı Ekleme**

Bir pivot alanını filtre alanına kaydetmenin iki yolu vardır. Üst düzey çağrı, kaynak-sütun adını bir dize olarak alır ve en yaygın yoldur. Daha düşük seviyeli çağrı, mevcut bir `PivotField` örneğini kabul eder ve aynı alan nesnesinin birden fazla pivot alanında yeniden kullanılması gerektiğinde kullanışlıdır. Her iki çağrı da alanı `PivotTable.page_fields` içine yerleştirir; bunun ardından işlenmiş özet tablo'nun üst kısmında sayfa açılır menüsü olarak görünür.

### add_field_to_area ile filtre alanı Ekleme

Aşağıdaki örnek, küçük bir Meyve / Yıl / Tutar veri kümesi oluşturur, özet tabloyu E3 hücresine yerleştirir; satır alanında `Meyve`, veri alanında `Tutar` ve filtre alanında `Yıl` bulunur, özet tablo'yu yeniler ve çalışma kitabını kaydeder.

```python
import aspose.cells as ac

# Yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Başlık satırını ayarla
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

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
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# E3 hücresine sabitlenmiş bir pivot tablo ekle
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Alanları ilgili bölgelere ekle: Meyve Satır olarak, Miktar Veri olarak, Yıl Sayfa alanı olarak
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# Pivot tablo verilerini yenile ve hesapla
pivot_table.calculate_data()

# Çalışma kitabını kaydet
workbook.save("pageFieldSample.xlsx")
```

### page_fields.add ile filtre alanı Ekleme

Zaten bir `PivotField` örneğiyle çalışıyorsanız, doğrudan `PivotTable.page_fields.add` yöntemine geçirebilirsiniz. Özet tablo ve filtre alanı, önceki senaryodakiyle tam olarak aynı şekilde oluşturulur; yalnızca son filtre alanı kaydı, daha düşük seviyeli API çağrısıyla değiştirilir.

```python
import aspose.cells as ac

# — Pivot tablo ve sayfa alanı, tam olarak Senaryo 1a'daki gibi oluşturulur
#   (Meyve/Yıl/Tutar verileri, pivot E3'te, Meyve→Satır,
#   Tutar→Veri). Aşağıda Yıl PivotField'ını BaseFields koleksiyonundan alır
#   ve PageFields.Add'a geçiririz — AddFieldToArea'nın
#   düşük seviyeli alternatifidir. Sonuç,
#   işlevsel olarak Senaryo 1a ile aynıdır.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Başlıklar
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# Örnek veri (9 satır)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# A1:C10'u kapsayacak şekilde E3'e pivot tablosu ekle
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Meyve -> Satır, Tutar -> Veri (Yıl aşağıda Sayfa'ya gidecek)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Düşük seviyeli yaklaşım: mevcut Yıl PivotField'ını BaseFields'tan al
# ve PageFields.Add(PivotField) aracılığıyla Sayfa alanına kaydet.
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# Yeni sayfa alanının kaydedilen çalışma kitabına yansıtılması için yenile
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Tekli Seçim Filtreleme (Tek Bir Sayfa Öğesi Gösterme)**

Varsayılan tekli seçim davranışında, filtre alanı tek bir açılır menü olarak işlenir ve `PivotField.current_page_item` tamsayısı, özet tablo gövdesini hangi sayfa öğesinin yönlendireceğini seçer. Belirli bir dizin atamak o öğeyi seçer; özel sentinel `0x7FFD` (ondalık 32765) atamak ise filtreyi temizler, böylece her sayfa öğesi aynı anda özetlenir. Tekli seçim varsayılandır; bunu açıkça etkinleştirmeniz gerekmez.

### Tüm Öğeleri Gösterme

`current_page_item` öğesini sihirli değer olan `0x7FFD` olarak ayarlamak, filtreni temizlemeye eşdeğerdir: özet tablo gövdesi, hiçbir filtre uygulanmamış gibi her sayfa öğesini özetler.

```python
import aspose.cells as ac

# Yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Meyve/Yıl/Miktar verilerini doldur
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

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
        sheet.cells[r + 1, c].put_value(data[r][c])

# E3 konumunda pivot tablo oluştur
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# Pivot alanlarını yapılandır: Fruit→Satır, Amount→Veri, Year→Sayfa
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.calculate_data()

# Sayfa filtresini temizle, böylece sayfa alanındaki her öğe görünür olsun.
# 0x7FFD (ondalık 32765), "tüm öğeler" anlamına gelen özel bekçi değeridir —
# Excel'in sayfa alanı açılır menüsünde "(Tümü)" seçmeye eşdeğerdir.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### Belirli Bir Öğeyi Gösterme

`current_page_item` öğesini gerçek bir dizine ayarlamak yalnızca o sayfa öğesini seçer. Dizin, öğenin filtre alanının sıralanmış öğe listesindeki konumudur; bu nedenle örneğin `1` değeri, sıralamadan sonra ikinci öğeyi seçer.

```python
import aspose.cells as ac

# Çalışma kitabı oluştur
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Örnek veri ekle (Meyve/Yıl/Miktar)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# E3 konumunda pivot tablo ekle
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Alanları ekle: Meyve→Satır, Miktar→Veri, Yıl→Sayfa
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# Sayfa alanına özel işlemler
pivot_table.page_fields[0].current_page_item = 1  # 1 = sıralanmış listedeki ikinci öğe (ör. "2021")

# Pivot tabloyu yenile ve hesapla
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **Çoklu Seçim Filtreleme**

Çoklu seçim filtreleme, sayfa açılır menüsünü bir onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birkaç sayfa öğesi seçmesine olanak tanır. Aspose.Cells, birlikte çalışan iki özellik sunar. Çoklu seçim kullanıcı arayüzünün hiç etkili olmaması için `PivotField.is_multiple_item_selection_allowed` öğesinin `True` olarak ayarlanması gerekir. Etkinleştirildikten sonra, `PivotItem.is_hidden`, onay kutusu listesinde hangi öğelerin görüneceğini kontrol eder; böylece her öğeyi gösterebilir veya yalnızca belirli öğeleri beyaz listeye alabilirsiniz.

Aşağıdaki kod, Senaryo 1a'da oluşturulan aynı Yıl filtre alanında çoklu seçimi etkinleştirir ve ardından iki kalıp gösterir: Bölüm A, her giriş için `is_hidden` öğesini `False` olarak bırakarak her sayfa öğesini ortaya çıkarır; Bölüm B ise yalnızca seçtiğiniz kaynak değerlerini beyaz listeye alır ve `pivot_items[i].get_string_value()` öğesini test eden bir `if` / `elif` bloğu aracılığıyla diğer her şeyi gizler.

```python
import aspose.cells as ac

# — Pivot tablo ve sayfa alanı tam olarak
#   Senaryo 1a'daki gibi oluşturulur (Fruit/Year/Amount verileri, pivot E3'te, Fruit→Satır,
#   Amount→Veri, Year→Sayfa AddFieldToArea aracılığıyla).
#   Aşağıda sayfa alanında çoklu seçim filtrelemesi uyguluyoruz.

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Örnek veri: Fruit | Year | Amount
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

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
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — Sayfa alanında çoklu seçimi etkinleştir
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# Bölüm A — TÜM öğeleri seç (her öğeyi görünür yap)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# Bölüm B — Yalnızca kaynak değere göre belirli öğeleri seç
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **Not:** Çoklu seçim filtrelemesini `PivotItem.is_hidden` aracılığıyla kullanırken, **en az bir `PivotItem` görünür kalmalıdır** (`is_hidden == False`). Her öğe gizlenmişse, Excel dosyayı açarken ya çöker ya da boş bir özet tablo işler. Çoklu seçim beyaz listenizin kaynak verilerinizden en az bir öğe içerdiğini her zaman doğrulayın.

## **Hangi API'yi ve Hangi Modu Kullanmalıyım?**

Aşağıdaki tablo, her API'yi ve modu ne zaman kullanacağınızı özetler, böylece her senaryoyu ayrıntılı olarak okumadan doğru kombinasyonu seçebilirsiniz.

| Senaryo / Kullanım Durumu | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| filtre alanını kaynak-sütun adıyla ekleme (en yaygın) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | yok | Üst düzey, tek satır. Bir `PivotField` referansına ihtiyacınız olmadıkça bunu kullanın. |
| Zaten bir `PivotField` nesneniz olduğunda filtre alanı ekleme | `PivotTable.page_fields.add(PivotField)` | yok | Alan nesnesi başka yerden alındığında veya yeniden kullanılması gerektiğinde kullanın. |
| Tek bir sayfa öğesine filtreleme (varsayılan mod) | `PivotField.current_page_item` | belirli bir dizine ayarla | Örneğin, `1` sıralanmış listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / filtreni temizleme | `PivotField.current_page_item` | `0x7FFD` olarak ayarla | Sihirli değer olan `0x7FFD` (ondalık 32765), "tüm öğeler" için sentinel değerdir. |
| Excel'de çoklu seçim kullanıcı arayüzünü etkinleştirme | `PivotField.is_multiple_item_selection_allowed` | `True` olarak ayarla | Herhangi bir `is_hidden` çağrısının etkili olmasından önce gereklidir. |
| Çoklu seçim listesinde tek tek öğeleri gizleme / gösterme | `PivotItem.is_hidden` | öğe başına ayarla | En az bir öğe görünür kalmalıdır (`is_hidden == False`). |

{{% alert color="primary" %}}
Çoklu seçim filtrelemesini yapılandırırken görünürlük kısıtlamasını her zaman hatırlayın. Çoklu seçim filtre alanındaki her `PivotItem` gizlenmişse, Excel açılırken çöker veya boş bir özet tablo işler. Beyaz listenizi kaynak verilerinize göre oluşturun, böylece en az bir öğe görünür kalır ve kaydedilen çalışma kitaplarınız her makinede güvenilir bir şekilde açılır.
{{% /alert %}}


{{< app/cells/assistant language="python" >}}
