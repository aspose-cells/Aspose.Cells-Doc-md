---
title: Pivot Tablolarını Etiket veya Değere Göre Filtreleme
linktitle: Pivot Tablolarını Etiket veya Değere Göre Filtreleme
description: Aspose.Cells for Python via Java, kapsamlı özet tablo filtreleme yeteneklerini destekler. Bu makale, özet tablo verilerini etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri kullanarak ve özet öğeleri gizleyerek veya göstererek nasıl filtreleyeceğinizi açıklar.
keywords: Aspose.Cells, Python via Java kitaplığı, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet öğe, özet öğeyi gizle
type: docs
weight: 10
url: /tr/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells, bir özet tablosunda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde tarih filtreleri kullanabilir, toplama sayılarına karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtreleri kullanabilir veya `is_hidden` özelliğini kullanarak tek tek özet öğeleri manuel olarak gizleyebilir ve gösterebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıfları üzerindeki özel API'ler aracılığıyla kullanıma sunulur.
{{% /alert %}}
## **Giriş**
Özet tablolar güçlü analitik araçlardır, ancak ham özetler genellikle sunmanız gereken bilgilerden çok daha fazlasını içerir. Filtreleme, özet tablosunu belirli bir rapor için önemli olan satır, sütun veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for Python via Java, Microsoft Excel'de bulunan filtreleme yeteneklerini yansıtır ve bunları programatik olarak sunarak rapor oluşturmanın tamamen otomatikleştirilmesini sağlar.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boş değerler) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplama değerlerine göre filtreler.
4. **İlk 10 Filtresi** — yalnızca bir değer alanına göre sıralanmış en yüksek veya en düşük N öğeyi gösterir.
5. **Özet Öğeleri Gizleme / Gösterme** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.
Her yaklaşım, `PivotField` sınıfı üzerinde farklı bir yöntem veya `PivotItem` sınıfı üzerinde bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tablosunda `refresh_data()` ve `calculate_data()` çağırmalısınız.
## **Etiket Filtresi**
Etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir desenle karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı ölçüte uyan ürünleri görüntülemek istediğinizde kullanışlıdır.
Aspose.Cells, etiket filtrelemeyi `PivotField.filter_by_label(PivotFilterType, str)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` gibi değerler içerir. İkinci bağımsız değişken, karşılaştırma için kullanılan etiket dizesini sağlar.
Aşağıdaki örnek, mevcut bir özet tablosu içeren bir çalışma kitabını yükler, yalnızca başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, özet tablosunu yeniler ve sonucu kaydeder.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# Özet tablo içeren mevcut çalışma kitabını yükle
workbook = Workbook(fileName)

# Çalışma sayfasına dizine göre eriş (ilk çalışma sayfası)
worksheet = workbook.getWorksheets().get(0)

# Özet tabloya dizine göre eriş
pivotTable = worksheet.getPivotTables().get(0)

# İlk satır PivotField alanını al
rowField = pivotTable.getRowFields().get(0)

# Etiket filtresi uygula — yalnızca etiketleri sağlanan önekle başlayan satır öğelerini göster
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# Filtrenin geçerli olması için özet tablo verilerini yenile ve yeniden hesapla
pivotTable.getPivotCache().refresh()

# Çalışma kitabını diske geri kaydet
workbook.save(fileName)

jpype.shutdownJVM()
```
## **Tarih Filtresi**
Tarih filtreleri, bir özet tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı ölçütlerle daraltmanıza olanak tanır. Bunlar, yalnızca tarih-saat bilgilerini depolayan alanlara karşı çalışan özel filtrelerdir.
{{% alert color="primary" %}}
Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alan sayılar veya metin gibi başka veri türleri içeriyorsa, tarih filtresi beklenen sonucu üretmeyecektir. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.
{{% /alert %}}
Aspose.Cells, tarih filtrelemeyi `PivotField.filter_by_date(PivotFilterType, values)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak bir veya iki `DateTime` değeri geçirirsiniz (`Between` için başlangıç ve bitiş tarihlerini geçirirsiniz).
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan bir özet tablosu içeren bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"

if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")

# Pivot tablosunu içeren mevcut çalışma kitabını yükleyin
workbook = Workbook(inputPath)

# Pivot tablosunu tutan çalışma sayfasına erişin (dizine göre)
worksheet = workbook.getWorksheets().get(0)

# Pivot tablosuna dizine göre erişin
pivotTable = worksheet.getPivotTables().get(0)

# Satır alanından tarih PivotField'ını alın
# (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde çalışır)
dateField = pivotTable.getRowFields().get(0)

# Between filtresi için tarih kriterini tanımlayın
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# Pivot alanına tarih filtresini uygulayın
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# Filtrenin etkili olması için pivot tablosunu yenileyin ve yeniden hesaplayın
pivotTable.getPivotCache().refresh()

# Çalışma kitabını kaydedin
workbook.save(outputPath)

jpype.shutdownJVM()
```
## **Değer Filtresi**
Değer filtreleri, bir özet tablosunun veri alanında hesapladığı toplama değerleri üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değeriyle karşılaştırırlar. Tipik kullanım örnekleri arasında yalnızca satış toplamı bir hedef tutarı aşan ürünleri veya işlem sayısı belirli bir aralıkta olan bölgeleri göstermek yer alır.
Aspose.Cells, değer filtrelemeyi `PivotField.filter_by_value(value_field, filter_type, values)` yöntemi aracılığıyla sunar. `filter_type` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. `value_field` parametresi hangi veri alanının değerlendirileceğini belirtir ve son bağımsız değişken(ler) eşik değerini sağlar.
Aşağıdaki örnek, bir özet tablosu içeren bir çalışma kitabını yükler, yalnızca toplama satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)

rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)

# PivotFieldCollection'da IndexOf olmadığından veri alanı indeksini manuel olarak bul
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break

if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivotTable.getPivotCache().refresh()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## **İlk 10 Filtresi**
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan, özel bir değer filtresi biçimidir. Genellikle "gelire göre ilk 10 ürün" veya "satış sayısına göre en düşük 5 bölge" gibi sıralama raporları için kullanılır.
{{% alert color="primary" %}}
İlk 10 filtresi yalnızca özet tablosunun veri alanında bir veya daha fazla değer pivot alanı varsa etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplama bir ölçü yoktur ve filtre uygulanamaz.
{{% /alert %}}
Aspose.Cells, ilk 10 filtrelemeyi `PivotField.filter_top10(item_count, is_top, value_field, filter_type)` yöntemi aracılığıyla sunar. `item_count` parametresi kaç öğenin tutulacağını tanımlar, `is_top` en yüksek öğelerin mi (true) yoksa en düşük öğelerin mi (false) tutulacağını belirtir, `value_field` sıralama için kullanılan veri alanına başvurur ve `filter_type` değerin nasıl hesaplanacağını kontrol eder (genellikle `Sum`, ancak `Count` ve `Percent` da olabilir).
Aşağıdaki örnek, bir değer alanı içeren bir özet tablosu bulunan bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için ilk 10 filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# Pivot tablosunu içeren mevcut çalışma kitabını yükleyin
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# Pivot tablosunu tutan çalışma sayfasına erişin (indeks 0)
worksheet = workbook.getWorksheets().get(0)

# Pivot tablosuna indeks ile erişin
pivotTable = worksheet.getPivotTables().get(0)

# Veri alanında en az bir değer PivotField olduğunu doğrulayın
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)

# Hedef satır PivotField'ını alın (Top 10 filtresini uygulamak istediğimiz alan)
rowField = pivotTable.getRowFields().get(0)

# İlk (ve tek) veri alanı 0 indeksindedir; Top 10 buna göre sıralar.
valueFieldIndex = 0

# Satır alanına Top 10 filtresini uygulayın:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (ilk N; false alt N anlamına gelir)
#   - valueFieldIndex = öğeleri sıralamak için kullanılan veri alanının indeksi
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# Pivot tablosu verilerini yenileyin ve filtrenin geçerli olması için yeniden hesaplayın
pivotTable.getPivotCache().refresh()

# Çalışma kitabını kaydedin
workbook.save(outputPath)

jpype.shutdownJVM()
```
## **Özet Öğeleri Gizleyerek veya Göstererek Filtreleme**
Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir özet öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField` öğesinin `PivotItems` koleksiyonunda dolaşarak ve `is_hidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `is_hidden = True` ayarı, öğeyi özet tablosundan gizler; `is_hidden = False` ayarı ise öğeyi gösterir ve tekrar görünür hale getirir.
Bu yaklaşım, filtreleme kuralının düzensiz veya öğeye özgü olduğu durumlarda kullanışlıdır; örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlemek gibi. Aşağıdaki örnek, bir özet tablosu yükler, ada göre belirli bir öğeyi gizler, nasıl gösterileceğini gösterir, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# Pivot tablosu içeren mevcut bir çalışma kitabını yükle
workbook = Workbook("pivot_table_sample.xlsx")

# Pivot tablosunu içeren ilk çalışma sayfasına eriş
sheet = workbook.getWorksheets().get(0)

# Pivot tablosuna dizine göre eriş (sayfadaki ilk pivot tablosu)
pivotTable = sheet.getPivotTables().get(0)

# Hedef PivotField'ı al (öğelerini gizleyeceğimiz/göstereceğimiz ilk satır etiket alanı)
pivotField = pivotTable.getRowFields().get(0)

# Seçilen PivotField'ın PivotItems koleksiyonu boyunca yinele
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # Belirli bir ad/ölçütle eşleşen pivot öğelerini gizle
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # Gizlemeyi kaldırmayı göster: daha önce gizlenmiş bir pivot öğesini yeniden göster
    if item.getName() == "Item3":
        item.setIsHidden(False)

# Değişikliklerin geçerli olması için pivot tablosunu yenile ve yeniden hesapla
pivotTable.getPivotCache().refresh()

# Çalışma kitabını kaydet — gizli öğeler temel verilerde kalır
# ancak görüntülenen pivot tablosu çıktısından hariç tutulur
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```
## **Özet**
Aspose.Cells for Python via Java, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir özet tablo filtreleme özellikleri seti sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsar; ilk 10 filtresi ise sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.is_hidden` özelliği esnek, öğe düzeyinde bir geri dönüş seçeneği sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas şekilde hedeflenmiş özet tablo raporları oluşturmanıza olanak tanır.
{{< app/cells/assistant language="python" >}}