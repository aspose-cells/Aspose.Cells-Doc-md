---
title: Aspose.Cells for Python via Java'da Özet Tabloları Yenileme
linktitle: Aspose.Cells for Python via Java'da Özet Tabloları Yenileme
description: Aspose.Cells for Python via Java'da v26.7+ pivot-refresh API kullanarak özet tabloların nasıl yenileneceğini öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables yöntemlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, Python via Java, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells, özet verilerini dört farklı kapsamda — çalışma kitabının tamamından tek bir özet tablosuna kadar — yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sağlar. **Aspose.Cells for Python via Java v26.7** sürümünden itibaren, eski `PivotTable.refreshData()` yöntemi artık kullanımdan kaldırılmış (obsolete) olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'ler ile değiştirilmelidir.

{{% /alert %}}

## Giriş

Bir özet tablosunu yenilemek nadiren tek bir işlemdir. Arkasında, Aspose.Cells orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.

Dört katmanlı veri zinciri şudur:

1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsü. Her özet tablo bir `PivotCache` üzerine inşa edilir; tüm verilerin toplandığı ve toplulaştırıldığı yer burasıdır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` *yalnızca* kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Cells** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.

Özellikle önemli bir kavram **paylaşılan önbellektir**. Bir çalışma kitabındaki birden fazla özet tablo aynı kaynak aralığa başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok özet tablo tarafından başvurulabilir ve o önbelleğin yenilenmesi, ona bağlı her `PivotTable`'ı bir seferde yeniler.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.refresh()` yalnızca **`SHEET`** ve **`CONSOLIDATION`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında yaşayan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) henüz önbellek API'si üzerinden yenilenemez.

{{% /alert %}}

Bu zincir nedeniyle, Aspose.Cells'te iki temel yenileme yolu vardır:

- **`PivotCache.refresh()`** — kaynaktan önbelleğe yeniden yükler VE tek bir işlemde tüm bağımlı `PivotTable`'ları yeniden hesaplar.
- **`PivotTable.calculateData()`** — zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar; veri kaynağına geri dönüş yapılmaz.

Bu makaledeki tüm senaryolarda çalışma sayfası hücre kaynak verileri kullanılır, dolayısıyla kaynak türü `SHEET`'tir ve yenileme işlemleri açıklandığı gibi çalışır.

## Gerekli İçe Aktarmalar

Bu makaledeki tüm Python örnekleri, pivot türlerinin `aspose.cells.pivot` namespace'inde bulunması nedeniyle aşağıdaki içe aktarmalara dayanır:

- `import jpype`
- `import aspose.cells as cells`

`jpype` modülü JVM'i başlatmak için kullanılırken, `aspose.cells` boyunca kullanılan çalışma kitabı/çalışma sayfası/hücre/pivot türlerini sunar.

## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme

Çalışma kitabındaki her pivot önbelleğinin ve her özet tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kendi kaynağından yeniler ve ardından tüm bağımlı `PivotTable`'ları yeniden hesaplar. Performansın önemli olmadığı genel, tam belge yenilemeleri için önerilen yaklaşım budur.

Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablo oluşturur, bazı kaynak değerleri değiştirir ve ardından her şeyi tek bir çağrıyla güncellemek için `refreshAll()` yöntemini kullanır.

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

# A2:C9 hücrelerine veri satırlarını yaz (2020 ve 2021 yılları arasında 8 satır meyve verisi)
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

# Bir pivot tablo ekle: kaynak aralık "A1:C9", hedef hücre "E3", ad "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Pivot alanlarını ata: Satırlar'a Fruit, Sütunlar'a Year, Veri'ye Amount
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Amount değerini değiştir
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Çalışma kitabındaki tüm pivot tabloları / pivot önbelleğini yenile
workbook.refreshAll()

# Çalışma kitabını kaydet
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme

Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu bilindiğinde ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.refreshPivotTables()` yöntemini sağlar.

Bu, `Workbook.refreshAll()` yönteminden daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki özet tabloları yenilenir, diğer çalışma sayfalarındaki özet tablolarına dokunulmaz.

Aşağıdaki örnek aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir özet tablo ekler, bazı kaynak değerleri değiştirir ve ardından yalnızca o çalışma sayfasındaki özet tablolarını yeniler.

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

Tek bir özet tablosu üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca özet tablosunun kendi görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.refresh()` Kullanın

Temel kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.getPivotCache().refresh()` yöntemidir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

{{% alert color="primary" %}}

Özet tabloları tek bir `PivotCache` örneğini paylaştığından, `PivotCache.refresh()` çağrısı o aynı önbellek üzerine inşa edilmiş **tüm** özet tablolarını yeniden hesaplar — yalnızca başvurduğunuz birini değil. İki özet tablo aynı kaynak aralığı paylaşıyorsa, bir önbelleği yenilemek her ikisini de yeniler.

{{% /alert %}}

Aşağıdaki örnek, bu paylaşılan önbellek davranışını göstermek için aynı kaynak aralığa sahip iki özet tablo oluşturur, bazı kaynak değerleri değiştirir ve ardından tek bir önbellek başvurusu üzerinden yenileme yapar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Başlık satırını yaz: Meyve / Yıl / Miktar
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Yaklaşık 9 veri satırı yaz (üzüm / yaban mersini / kivi / kiraz, 2020-2021 arası)
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

# İlk pivot tablosunu "Pivot1" E3 hücresine bağlı, kaynak aralığı A1:C9 olarak ekle
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Pivot1 için alanları ata
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Aynı kaynak aralığı A1:C9 kullanarak E15'e bağlı İKİNCİ pivot tablosunu "Pivot2" ekle
# Hem Pivot1 hem de Pivot2, kaynak aralığı aynı olduğu için tek bir PivotCache'i paylaşır.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Pivot2 için aynı alanları ata
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Veri değişikliğini simüle etmek için kaynak verilerdeki birkaç Miktar hücre değerini değiştir
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Paylaşılan PivotCache'i yenile.
# Pivot1 ve Pivot2 aynı PivotCache'i paylaştığı için bu tek çağrı
# güncellenmiş kaynaktan HER İKİ pivot tablosunu da (veri + stil) yeniler.
pivotTable1.getPivotCache().refresh()

# Çalışma kitabını kaydet
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Yalnızca Görünüm/Düzen Değişti — `calculateData()` Kullanın

Kaynak veriler değişmediyse ancak yalnızca özet tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönme gereği yoktur. Önbellek zaten doğru verileri tutuyor; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekiyor. Bu durumda, `pivotTable.calculateData()` doğru seçimdir.

Bu, gereksiz kaynak alımını önler ve birçok özet tablosu aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.

Aşağıdaki örnek, özet tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculateData()` yöntemini çağırır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Meyve / Yıl / Tutar başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 8 veri satırı yaz (2-9 arası satırlar, A1:C9 kaynak aralığına uyuyor)
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

# E3 hedef hücresine yerleştirilen, A1:C9'dan beslenen "Pivot1" adlı bir pivot tablo ekle
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunuma yönelik bir değişikliktir,
# dolayısıyla PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTİRMEZ.
pivotTable.setRefreshDataOnOpeningFile(False)

# calculateData(), BU pivot tablosunun görüntüsünü (veri + stil) PivotCache'te zaten
# tutulan verilerden yeniden oluşturur. Kaynak veri değişmediği için kaynağa geri gidiş
# yapılmaz — yalnızca önbelleğe alınmış değerler çalışma sayfası hücrelerine yeniden hesaplanır.
pivotTable.calculateData()

# Çalışma kitabını diske kaydet
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Aynı PivotCache'i Paylaşan Tüm Özet Tablolarını Alma

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerinde oturan birçok özet tablo içerir. Bunları numaralandırmak için — örneğin, toplu bir yenileme yapmadan önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.getPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

Bu aynı zamanda iki özet tablosunun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilir veya `getPivotTables()` tarafından döndürülen koleksiyonu yineleyip hangi özet tablolarının göründüğünü gözlemleyebilirsiniz.

Aşağıdaki örnek, aynı kaynak aralığa sahip iki özet tablo oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin özet tablolarını numaralandırır.


## Kullanımdan Kaldırılan `PivotTable.refreshData()` Yönteminden Geçiş

Aspose.Cells for Python via Java v26.7'den önce, bir özet tablosunu yenilemenin standart yolu her özet tablosunda ayrı ayrı `PivotTable.refreshData()` çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış** (obsolete) olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'ler ile değiştirilmelidir.

Gerçek dünya çalışma kitaplarında tablo başına `refreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:

- Kaynak değişmemiş olsa bile her çağrıldığında kaynaktan verileri yeniden alır.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok özet tablosu tek bir önbelleği paylaştığında, özet tablo başına tekrar tekrar `refreshData()` çağırmak aynı önbelleğin sürekli yeniden alınmasına neden olur, bu da çok yavaştır.

Önerilen değiştirmeler şunlardır:

- **Çalışma kitabındaki TÜM özet tablolarını yenileme** → `workbook.refreshAll();` kullanın
- **Bazılarını yenileme** → tek bir önbellek için `pivotTable.getPivotCache().refresh();` kullanın. Önbellek paylaşıldığından, bu tek çağrı o önbelleğin üzerine inşa edilmiş her özet tablosunu günceller. Zaten yenilenmiş bir önbelleğin üzerinde oturan diğer özet tabloları güvenle atlanabilir.
- **Yalnızca pivot görünümü/düzeni değişti** → kaynak veriye geri dönüş olmadan mevcut önbellekten yeniden işlemek için `pivotTable.calculateData();` kullanın.

Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok özet tablosu olan çalışma kitapları için yeni verimli kalıbı gösterir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Kaynak veriyi oluştur: Meyve / Yıl / Tutar (başlık + 9 satır) ---
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

# --- İlk pivot tablosunu (Pivot1) E3 hedef hücresine ekle ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- İKİNCİ pivot tablosunu (Pivot2) AYNI kaynak aralığı üzerine ekle ---
# Hem Pivot1 hem de Pivot2 TEK bir PivotCache'i paylaşır.
# Bu tam olarak eski tablo başına RefreshData() yaklaşımının verimsiz hale geldiği senaryodur:
# bir tabloyu yenilemek tüm paylaşılan önbelleği yeniden çeker,
# bu nedenle N tabloyu yenilemek aynı pahalı çekme işlemini N kez yapar.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Kaynak verideki birkaç Tutar değerini değiştir ---
sheet.getCells().get("C2").putValue(5000)   # Üzüm 2020
sheet.getCells().get("C5").putValue(7500)   # Kiraz 2020
sheet.getCells().get("C9").putValue(9500)   # Kiraz 2021

# --- ESKİ model (26.7 öncesi) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // kaynaktan yeniden çeker, tüm önbelleği yeniler
# pivotTable2.RefreshData();  // TEKRAR yeniden çeker — önbellek zaten taze!
# Her çağrı paylaşılan önbelleği yeniden oluşturur, bu nedenle N tablo = N gereksiz çekme işlemi.

# --- YENİ v26.7+ model: önbelleği BİR KEZ yenile, ardından gerektiğinde yeniden görüntüle ---
# PivotCache.Refresh() için tek bir çağrı, değiştirilen değerleri paylaşılan önbelleğe çeker
# VE ona başvuran HER pivot tablosunun görüntüsünü yeniden hesaplar.
# Pivot1 ve Pivot2 tek bir PivotCache'i paylaştığı için bu tek çağrı
# her iki tabloyu da günceller — ikinci bir kaynak gidip gelmesi gerekmez.
pivotTable1.getPivotCache().refresh()

# CalculateData() yalnızca bir pivot tablosunun görüntüsünü (veri + stil) önbellekte
# zaten tutulan verilerden yeniden oluşturur — kaynağa DOKUNMAZ.
# Burada Pivot2 üzerinde yalnızca API'yi göstermek için çağırıyoruz: önbellek
# bir kez yenilendikten sonra, bağımlı herhangi bir tablo kaynağa geri dönmeden
# yeniden görüntülenebilir. CalculateData()'yı yalnızca pivot tablosunun görünüm/düzen
# ayarları değiştiğinde ve önbellek güncel olduğunda kendi başına kullanın.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Hangi Yenileme API'sini Kullanmalıyım?

Aşağıdaki tablo, mevcut yenileme API'lerini ve her birinin ne zaman seçilmesi gerektiğini özetlemektedir.

| Amaç | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki özet tablolarını yenileme | `Worksheet.refreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlı. |
| Tek bir önbellek için kaynak veriler değişti | `pivotTable.getPivotCache().refresh()` | O paylaşılan önbellekteki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan bir önbellekteki tüm özet tablolarını listeleme | `pivotCache.getPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |

Pratikte, kullanımdan kaldırılan tablo başına `refreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak alımlarını önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.{{< app/cells/assistant language="python" >}}
