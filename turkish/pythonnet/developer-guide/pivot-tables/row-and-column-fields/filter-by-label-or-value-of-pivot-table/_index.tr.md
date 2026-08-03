---
title: Pivot Tablolarını Etikete veya Değere Göre Filtreleme
linktitle: Pivot Tablolarını Etikete veya Değere Göre Filtreleme
description: Aspose.Cells for Python via .NET, kapsamlı pivot tablo filtreleme özelliklerini destekler. Bu makale, pivot tablo verilerini etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri ve pivot öğelerini gizleyerek veya görünür hale getirerek nasıl filtreleyeceğinizi açıklar.
keywords: Aspose.Cells, Python via .NET kütüphanesi, elektronik tablo, pivot tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, pivot öğesi, pivot öğesini gizle
type: docs
weight: 10
url: /tr/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, bir pivot tabloda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde tarih filtreleri kullanabilir, toplam sayılara karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtreleri kullanabilir veya `is_hidden` özelliğini kullanarak tek tek pivot öğelerini manuel olarak gizleyip görünür hale getirebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıflarındaki özel API'ler aracılığıyla kullanıma sunulur.

{{% /alert %}}

## **Giriş**

Pivot tablolar güçlü analitik araçlardır, ancak ham özetler genellikle sunmanız gerekenden çok daha fazla bilgi içerir. Filtreleme, bir pivot tablosunu belirli bir rapor için önemli olan satır, sütun veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for Python via .NET, Microsoft Excel'de bulunan filtreleme özelliklerini yansıtarak bunları programatik olarak sunar; böylece rapor oluşturma tamamen otomatikleştirilebilir.

Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:

1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boş değerler) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplam değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralanmış yalnızca en yüksek veya en düşük N öğeyi gösterir.
5. **Pivot Öğelerini Gizle / Görünür Hale Getir** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.

Her yaklaşım, `PivotField` sınıfında farklı bir yöntem veya `PivotItem` sınıfında farklı bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için pivot tabloda `refresh_data()` ve `calculate_data()` çağırmanız gerekir.

## **Etiket Filtresi**

Etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı ölçüte uyan ürünleri görüntülemek istediğinizde kullanışlıdır.

Aspose.Cells, etiket filtrelemeyi `PivotField.filter_by_label(PivotFilterType, label_string)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzeri değerler içerir. İkinci bağımsız değişken, karşılaştırma için kullanılan etiket dizesini sağlar.

Aşağıdaki örnek, mevcut bir pivot tablo içeren bir çalışma kitabını yükler, yalnızca başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, pivot tablosunu yeniler ve sonucu kaydeder.

```python
import aspose.cells as ac

fileName = "sample.xlsx"
prefix = "B"

# Mevcut çalışma kitabını, içinde bir pivot tablo bulunduran şekilde yükle
workbook = ac.Workbook(fileName)

# Çalışma sayfasına dizin ile eriş (ilk çalışma sayfası)
worksheet = workbook.worksheets[0]

# Pivot tabloya dizin ile eriş
pivot_table = worksheet.pivot_tables[0]

# İlk satır PivotField öğesini al
row_field = pivot_table.row_fields[0]

# Etiket filtresini uygula — etiketleri sağlanan ön ek ile başlayan satır öğelerini göster
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGNS_WITH, prefix, "")

# Filtre etkili olsun diye pivot tablo verilerini yenile ve yeniden hesapla
pivot_table.pivot_cache.refresh()

# Çalışma kitabını diske geri kaydet
workbook.save(fileName)
```

## **Tarih Filtresi**

Tarih filtreleri, bir pivot tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı ölçütlere göre daraltmanıza olanak tanır. Bunlar yalnızca tarih-saat bilgilerini depolayan alanlara karşı çalışan özel filtrelerdir.

{{% alert color="primary" %}}

Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alandaki alan sayılar veya metin gibi başka veri türleri içeriyorsa, tarih filtresi beklenen sonucu vermeyecektir. Filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.

{{% /alert %}}

Aspose.Cells, tarih filtrelemeyi `PivotField.filter_by_date(PivotFilterType, *date_times)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak, bir veya iki `DateTime` değeri iletirsiniz (`Between` için başlangıç ve bitiş tarihlerini iletirsiniz).

Aşağıdaki örnek, satır alanında bir tarih alanı bulunan pivot tabloya sahip bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```python
from datetime import datetime

input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"

if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)

# Mevcut pivot tablosunu içeren çalışma kitabını yükleyin
workbook = ac.Workbook(input_path)

# Pivot tablosunu barındıran çalışma sayfasına erişin (dizine göre)
worksheet = workbook.worksheets[0]

# Pivot tablosuna dizine göre erişin
pivot_table = worksheet.pivot_tables[0]

# Satır alanından tarih PivotField'ını alın
# (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde çalışır)
date_field = pivot_table.row_fields[0]

# Between filtresi için tarih kriterini tanımlayın
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# Pivot alanına tarih filtresini uygulayın
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# Pivot tablosunu yenileyin ve yeniden hesaplayın, böylece filtre etkili olur
pivot_table.pivot_cache.refresh()

# Çalışma kitabını kaydedin
workbook.save(output_path)
```

## **Değer Filtresi**

Değer filtreleri, bir pivot tablosunun veri alanında hesapladığı toplam değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değeriyle karşılaştırır. Tipik kullanım durumları arasında yalnızca satış toplamı bir hedef tutarı aşan ürünleri veya yalnızca işlem sayısı bir aralık içinde olan bölgeleri göstermek yer alır.

Aspose.Cells, değer filtrelemeyi `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)` yöntemi aracılığıyla sunar. `PivotFilterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. `value_field` parametresi, hangi veri alanının değerlendirileceğini belirtir ve son bağımsız değişken(ler) eşik değerini/değerlerini sağlar.

Aşağıdaki örnek, pivot tablo içeren bir çalışma kitabını yükler, yalnızca toplam satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```python
import aspose.cells as ac

workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# PivotFieldCollection'da IndexOf olmadığından veri alanı dizinini manuel olarak bul
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break

if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivot_table.pivot_cache.refresh()

workbook.save("output.xlsx")
```

## **İlk 10 Filtresi**

İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan özel bir değer filtresi biçimidir. "Gelire göre ilk 10 ürün" veya "Satış sayısına göre en düşük 5 bölge" gibi sıralama raporları için yaygın olarak kullanılır.

{{% alert color="primary" %}}

İlk 10 filtresi, yalnızca pivot tablosunun veri alanında bir veya daha fazla değer pivot alanı olduğunda etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplam bir ölçü yoktur ve filtre uygulanamaz.

{{% /alert %}}

Aspose.Cells, ilk 10 filtrelemeyi `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)` yöntemi aracılığıyla sunar. `item_count` parametresi kaç öğenin tutulacağını tanımlar, `is_top` en yüksek öğelerin (True) mi yoksa en düşük öğelerin (False) mi tutulacağını belirtir, `value_field` sıralama için kullanılan veri alanına başvurur ve `PivotFilterType` değerin nasıl hesaplanacağını kontrol eder (genellikle `Sum`, ayrıca `Count` ve `Percent`).

Aşağıdaki örnek, bir değer alanı içeren pivot tabloya sahip bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için bir ilk 10 filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

# Pivot tablosunu içeren mevcut çalışma kitabını yükle
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)

# Pivot tablosunu tutan çalışma sayfasına eriş (indeks 0)
worksheet = workbook.worksheets[0]

# Pivot tablosuna indekse göre eriş
pivotTable = worksheet.pivot_tables[0]

# Veri alanında en az bir değer PivotField olduğunu doğrula
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# Hedef satır PivotField'ını al (Top 10 uygulamak istediğimiz alan)
rowField = pivotTable.row_fields[0]

# İlk (ve tek) veri alanı indeks 0'da; Top 10 ona göre sıralar.
valueFieldIndex = 0

# Satır alanına Top 10 filtresini uygula:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (ilk N; false alt N anlamına gelir)
#   - valueFieldIndex = öğeleri sıralamak için kullanılan veri alanının indeksi
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# Pivot tablo verilerini yenile ve filtrenin geçerli olması için yeniden hesapla
pivotTable.pivot_cache.refresh()

# Çalışma kitabını kaydet
workbook.save(outputPath)
```

## **Pivot Öğelerini Gizleyerek veya Görünür Hale Getirerek Filtreleme**

Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir pivot öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField`'in `PivotItems` koleksiyonunda yineleme yaparak ve `is_hidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `is_hidden = True` ayarı, öğeyi pivot tablodan gizler; `is_hidden = False` ayarı onu görünür hale getirir ve tekrar görünür kılar.

Bu yaklaşım, filtreleme kuralı düzensiz veya öğeye özgü olduğunda kullanışlıdır; örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlemek gibi. Aşağıdaki örnek bir pivot tabloyu yükler, ada göre belirli bir öğeyi gizler, onu görünür hale getirmeyi gösterir, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```python
import aspose.cells as ac

# Pivot tablo içeren mevcut bir çalışma kitabını yükleyin
workbook = ac.Workbook("pivot_table_sample.xlsx")

# Pivot tabloyu içeren ilk çalışma sayfasına erişin
sheet = workbook.worksheets[0]

# Pivot tabloya dizine göre erişin (sayfadaki ilk pivot tablo)
pivot_table = sheet.pivot_tables[0]

# Hedef PivotField'ı alın (öğelerini gizleyeceğimiz/göstereceğimiz ilk satır etiket alanı)
pivot_field = pivot_table.row_fields[0]

# Seçilen PivotField'ın PivotItems koleksiyonu boyunca yineleyin
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # Belirli bir ad/ölçütle eşleşen pivot öğelerini gizleyin
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # Gizlemeyi kaldırmayı gösterin: daha önce gizlenmiş bir pivot öğesini yeniden gösterin
    if item.name == "Item3":
        item.is_hidden = False

# Pivot tabloyu yenileyin ve yeniden hesaplayın, böylece değişiklikler etkili olur
pivot_table.pivot_cache.refresh()

# Çalışma kitabını kaydedin — gizli öğeler temel verilerde kalır
# ancak görüntülenen pivot tablo çıktısından hariç tutulur
workbook.save("output_pivot_filtered.xlsx")
```

## **Özet**

Aspose.Cells for Python via .NET, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir pivot tablo filtreleme özellikleri seti sağlar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsarken, ilk 10 filtresi sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.is_hidden` özelliği esnek, öğe düzeyinde bir yedek sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas hedefli pivot tablo raporları oluşturmanıza olanak tanır.
{{< app/cells/assistant language="python-net" >}}
