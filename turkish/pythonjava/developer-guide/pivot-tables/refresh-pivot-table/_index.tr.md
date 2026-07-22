---
title: Aspose.Cells for Python via Java'da Özet Tabloları Yenileme
linktitle: Aspose.Cells for Python via Java'da Özet Tabloları Yenileme
description: Aspose.Cells for Python via Java'da v26.7+ özet tablo yenileme API'sini kullanarak özet tabloları nasıl yenileyeceğinizi öğrenin. Bu makale, pratik kod örnekleriyle RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables'ı kapsar.
keywords: Aspose.Cells, Python via Java, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, özet verilerini dört farklı kapsamda — çalışma kitabının tamamından tek bir özet tablosuna kadar — yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sağlar. **Aspose.Cells for Python via Java v26.7** ile başlayarak, eski `PivotTable.refreshData()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.

{{% /alert %}}

## Giriş

Bir özet tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri sağlar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.

Dört katmanlı veri zinciri şunlardır:

1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her özet tablo bir `PivotCache`'in üzerine inşa edilir; tüm veriler burada toplanır ve birleştirilir.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Hücreler** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells`.

Özellikle önemli bir kavram **paylaşılan önbellek**tir. Bir çalışma kitabındaki birden çok özet tablo aynı kaynak aralığa başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok özet tablo tarafından başvurulabilir ve o önbelleği yenilemek, ona bağlı her `PivotTable`'ı bir kerede yeniler.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) önbellek verilerinin nereden geldiğini gösterir. v26.7 itibarıyla, `PivotCache.refresh()` yalnızca **`SHEET`** ve **`CONSOLIDATION`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.

{{% /alert %}}

Bu zincir nedeniyle, Aspose.Cells'te iki temel yenileme yolu vardır:

- **`PivotCache.refresh()`** — kaynağı → önbelleği yeniden yükler VE tüm bağımlı `PivotTable`'ları tek bir işlemde yeniden hesaplar.
- **`PivotTable.calculateData()`** — zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar, veri kaynağına geri dönüş olmadan.

Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynak verilerini kullandığından, kaynak türü `SHEET`'tir ve yenileme işlemleri açıklandığı gibi davranır.

## Gerekli İçe Aktarmalar

Bu makaledeki tüm Python örnekleri aşağıdaki içe aktarmalara dayanır çünkü özet tablo türleri `aspose.cells.pivot` namespace'inde bulunur:

- `import jpype`
- `import aspose.cells as cells`

`jpype` modülü JVM'i başlatmak için kullanılırken, `aspose.cells` boyunca kullanılan çalışma kitabı/çalışma sayfası/hücre/özet tablo türlerini sağlar.

## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme

Çalışma kitabındaki her önbelleğin ve her özet tablonun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refreshAll()`'dır. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Bu, performansın endişe olmadığı genel, tam belge yenilemeleri için önerilen yaklaşımdır.

Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablo oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncel hale getirmek için `refreshAll()`'ı kullanır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Yeni bir çalışma kitabı oluştur
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# A1:C1 hücrelerine başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# A2:C9 hücrelerine veri satırlarını yaz (2020 ve 2021 yıllarına ait 8 satır meyve verisi)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)

worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)

worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)

worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)

worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)

worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)

worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)

worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)

# Özet tablo ekle: kaynak aralık "A1:C9", hedef hücre "E3", ad "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Özet tablo alanlarını ata: Fruit'ı Satırlar'a, Year'ı Sütunlar'a, Amount'ı Veri'ye
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Değişiklikleri simüle etmek için kaynak verideki birkaç Amount değerini değiştir
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Çalışma kitabındaki tüm özet tabloları / özet tablo önbelleklerini yenile
workbook.refreshAll()

# Çalışma kitabını kaydet
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme

Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmamalıdır. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı `Worksheet.refreshPivotTables()`'ı sağlar.

Bu, `Workbook.refreshAll()`'dan daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki özet tabloları yenilenir, diğer çalışma sayfalarındaki özet tablolarına dokunulmaz.

Aşağıdaki örnek aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir özet tablo ekler, bazı kaynak değerlerini değiştirir ve ardından yalnızca o çalışma sayfasındaki özet tablolarını yeniler.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)

worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)

worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)

worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)

worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)

pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)

worksheet.refreshPivotTables()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Tek Bir Özet Tablosunu Yenileme

Tek bir özet tablo üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak verileri mi, yoksa yalnızca özet tablonun kendisinin görünüm/düzen ayarları mı.

### Kaynak Verileri Değişti — `PivotCache.refresh()` Kullanın

Temel kaynak verileri değiştiyse, doğru giriş noktası `pivotTable.getPivotCache().refresh()`'tir. Bu çağrı kaynak verilerini önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

{{% alert color="primary" %}}

Özet tablolar tek bir `PivotCache` örneğini paylaştığından, `PivotCache.refresh()` çağrısı yalnızca başvurduğunuz olanı değil, aynı önbellek üzerine inşa edilmiş **TÜM** özet tablolarını yeniden hesaplar. İki özet tablo aynı kaynak aralığı paylaşıyorsa, bir önbelleği yenilemek her ikisini de yeniler.

{{% /alert %}}

Aşağıdaki örnek, bu paylaşılan önbellek davranışını göstermek için aynı kaynak aralığında iki özet tablo oluşturur, bazı kaynak değerlerini değiştirir ve ardından bir önbellek referansı üzerinden yeniler.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Başlık satırını yaz: Meyve / Yıl / Tutar
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Yaklaşık 9 veri satırı yaz (üzüm / yaban mersini / kivi / kiraz, 2020-2021 yılları arasında)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# E3 hücresine bağlı, kaynak aralığı A1:C9 olan ilk pivot tablosunu "Pivot1" olarak ekle
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Pivot1 için alanları atama
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Aynı kaynak aralığı A1:C9 kullanılarak E15 hücresine bağlı İKİNCİ pivot tablosunu "Pivot2" olarak ekle
# Hem Pivot1 hem de Pivot2, kaynak aralığı aynı olduğundan tek bir PivotCache'i paylaşır.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Pivot2 için aynı alanları atama
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Bir veri değişikliğini simüle etmek için kaynak verilerdeki birkaç Tutar hücresi değerini değiştir
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Paylaşılan PivotCache'i yenile.
# Pivot1 ve Pivot2 aynı PivotCache'i paylaştığından, bu tek çağrı
# güncellenen kaynaktan HER İKİ pivot tablosunu da (veri + stil) yeniler.
pivotTable1.getPivotCache().refresh()

# Çalışma kitabını kaydet
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Yalnızca Görünüm/Düzen Değişti — `calculateData()` Kullanın

Kaynak verileri değişmediyse ancak yalnızca özet tablonun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda, `pivotTable.calculateData()` doğru seçimdir.

Bu, gereksiz kaynak getirmeyi önler ve birçok özet tablo aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.

Aşağıdaki örnek, özet tablonun kaynak dışı bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculateData()`'ı çağırır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Fruit / Year / Amount başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 8 veri satırı yaz (2-9 arası satırlar, kaynak aralığı A1:C9'a uygun)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)

# "Pivot1" adlı bir pivot tablosu ekle, hedef hücre E3'e yerleştir, kaynak A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunum amaçlı bir değişikliktir,
# bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını gerektirmez.
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() BU pivot tablosunun görüntüsünü (veri + stil) PivotCache'te
# zaten tutulan verilerden yeniden oluşturur. Kaynak veri değişmediği için,
# kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler çalışma sayfası
# hücrelerine yeniden hesaplanır.
pivotTable.calculateData()

# Çalışma kitabını diske kaydet
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Aynı PivotCache'i Paylaşan Tüm Özet Tablolarını Alma

Bir çalışma kitabı genellikle hepsi tek bir paylaşılan önbelleğin üzerinde oturan birçok özet tablo içerir. Bunları numaralandırmak için — örneğin, toplu yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini teşhis etmek için — `PivotCache.getPivotTables()`'ı kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

Bu aynı zamanda iki özet tablonun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek referanslarını karşılaştırabilir veya `getPivotTables()` tarafından döndürülen koleksiyonu basitçe yineleyebilir ve hangi özet tablolarının içinde göründüğünü gözlemleyebilirsiniz.

Aşağıdaki örnek, aynı kaynak aralığında iki özet tablo oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin özet tablolarını numaralandırır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# buraya taşınan kod
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()
print("Pivot1 and Pivot2 share the same PivotCache: " + str(sameCache))

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Eski `PivotTable.refreshData()`'dan Geçiş

Aspose.Cells for Python via Java v26.7'den önce, bir özet tablosunu yenilemenin standart yolu, her özet tabloda ayrı ayrı `PivotTable.refreshData()` çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış** (obsolete) olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.

Gerçek dünya çalışma kitaplarında tablo başına `refreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:

- Kaynak değişmemiş olsa bile, her çağrıldığında verileri kaynaktan yeniden getirir.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok özet tablo tek bir önbelleği paylaştığında, özet tablo başına `refreshData()`'ı tekrar tekrar çağırmak aynı önbelleğin tekrar tekrar yeniden getirilmesine neden olur, bu da çok yavaştır.

Önerilen değiştirmeler şunlardır:

- **Çalışma kitabındaki TÜM özet tablolarını yenile** → `workbook.refreshAll();` kullanın
- **Bazılarını yenile** → tek bir önbellek için `pivotTable.getPivotCache().refresh();` kullanın. Önbellek paylaşıldığından, bu tek çağrı o önbelleğin üzerine inşa edilmiş her özet tablosunu günceller. Zaten yenilenmiş bir önbellek üzerinde oturan diğer özet tabloları güvenle atlanabilir.
- **Yalnızca özet görünümü/düzeni değişti** → herhangi bir kaynak geri dönüşü olmadan mevcut önbellekten yeniden işlemek için `pivotTable.calculateData();` kullanın.

Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok özet tabloya sahip çalışma kitapları için yeni verimli kalıbı gösterir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Kaynak verileri oluştur: Meyve / Yıl / Tutar (başlık + 9 satır) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- Hedef hücre E3'e ilk pivot tablosunu (Pivot1) ekle ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- AYNI kaynak aralığa İKİNCİ pivot tablosunu (Pivot2) ekle ---
# Hem Pivot1 hem Pivot2 TEK bir temel PivotCache'i paylaşır.
# Bu, eski tablo başına RefreshData() yaklaşımının verimsiz hale geldiği
# tam olarak senaryodur: bir tabloyu yenilemek tüm paylaşılan önbelleği
# yeniden getirir, dolayısıyla N tabloyu yenilemek aynı pahalı getirmeyi N kez yapar.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Kaynak verilerde birkaç Tutar değerini değiştir ---
sheet.getCells().get("C2").putValue(5000)   # Üzüm  2020
sheet.getCells().get("C5").putValue(7500)   # Kiraz 2020
sheet.getCells().get("C9").putValue(9500)   # Kiraz 2021

# --- ESKİ (eski) desen (26.7 öncesi) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // kaynaktan yeniden getirir, tüm önbelleği yeniler
# pivotTable2.RefreshData();  // TEKRAR yeniden getirir — önbellek zaten taze!
# Her çağrı paylaşılan önbelleği yeniden oluşturur, dolayısıyla N tablo = N gereksiz getirme.

# --- YENİ v26.7+ deseni: önbelleği BİR KEZ yenile, ardından gerektiğinde yeniden oluştur ---
# PivotCache.Refresh() için yapılan tek bir çağrı, değiştirilen değerleri paylaşılan
# önbelleğe çeker VE ona başvuran HER pivot tablosunun görüntüsünü yeniden hesaplar.
# Pivot1 ve Pivot2 bir PivotCache'i paylaştığından, bu tek çağrı her iki tabloyu da
# günceller — ikinci bir kaynak gidiş-dönüşü gerekmez.
pivotTable1.getPivotCache().refresh()

# CalculateData() yalnızca bir pivot tablosunun görüntüsünü (veri + stil) önbellekte
# zaten tutulan verilerden yeniden oluşturur — kaynağa DOKUNMAZ.
# Burada onu Pivot2 üzerinde yalnızca API'yi göstermek için çağırıyoruz: önbellek bir kez
# yenilendikten sonra, herhangi bir bağımlı tablo kaynağa geri dönmeden yeniden oluşturulabilir.
# Yalnızca pivot tablosunun görünüm/düzen ayarları değiştiğinde ve önbellek güncel olduğunda
# CalculateData()'yı tek başına kullanın.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Hangi Yenileme API'sini Kullanmalıyım?

Aşağıdaki tablo, mevcut yenileme API'lerini ve her birini ne zaman seçmeniz gerektiğini özetlemektedir.

| Amaç | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenile | `Workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir çalışma sayfasındaki özet tabloları yenile | `Worksheet.refreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlı. |
| Bir önbellek için kaynak verileri değişti | `pivotTable.getPivotCache().refresh()` | O paylaşılan önbellekteki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan önbellekteki tüm özet tablolarını listele | `pivotCache.getPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |

Uygulamada, eski tablo başına `refreshData()` yerine önbellek tabanlı API'leri tercih edin. Paylaşılan önbelleklerin farkındadırlar, gereksiz kaynak getirmelerden kaçınırlar ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanırlar.

{{< app/cells/assistant language="python" >}}