---
title: Aspose.Cells for Python via Java'da Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
linktitle: Aspose.Cells for Python via Java'da Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
description: v26.7+ pivot yenileme API'sini kullanarak Aspose.Cells for Python via Java'da pivot tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables API'lerini pratik kod örnekleriyle ele almaktadır.
keywords: Aspose.Cells, Python via Java, pivot tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, dört farklı kapsamda — çalışma kitabının tamamından tek bir pivot tablosuna kadar — pivot verilerini yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Python via Java v26.7** ile birlikte eski `PivotTable.refreshData()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.
{{% /alert %}}

## Giriş
Bir pivot tablosunu yenileme nadiren tek bir işlemdir. Sahnenin arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şudur:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her pivot tablosu bir `PivotCache` üzerine inşa edilir; tüm verilerin toplandığı ve toplulaştırıldığı yer burasıdır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` verileri yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından değil.
4. **Cells** — `PivotTable`'nin hesaplanan değerlerini ve stillerini işlediği çalışma sayfası `Cells`'i.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`), önbellek verilerinin nereden geldiğini gösterir. v26.7 itibarıyla `PivotCache.refresh()` yalnızca **`SHEET`** ve **`CONSOLIDATION`** kaynak türlerini desteklemektedir — yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) önbellek API'si üzerinden henüz yenilenememektedir.
{{% /alert %}}

Bu zincir nedeniyle Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotTable.calculateData()`** — bir `PivotTable`'ın görüntüsünü, veri kaynağına geri dönüş olmaksızın zaten önbelleğe alınmış verilerden yeniden hesaplar.
Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynak verilerini kullanır, dolayısıyla kaynak türü `SHEET`'tir ve yenileme işlemleri açıklandığı şekilde çalışır.

## Hızlı Başlangıç
Çalışma kitabındaki her pivotu yenileyen mümkün olan en kısa kodu istiyorsanız, tek bir çağrı yeterlidir:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Yeni bir çalışma kitabı oluştur
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# A1:C1 hücrelerine başlık satırı yaz
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# A2:C9 hücrelerine veri satırları yaz (2020 ve 2021 yıllarına dağıtılmış 8 satır meyve verisi)
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
# Pivot alanlarını ata: Fruit Satırlara, Year Sütunlara, Amount Veriye
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Amount değerini değiştir
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Çalışma kitabındaki tüm özet tabloları / özet önbelleklerini yenile
workbook.refreshAll()
# Çalışma kitabını kaydet
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Bu makaledeki diğer her şey, bunun yerine daha dar kapsamlı bir API'nin ne zaman seçileceğini açıklar.

## Gerekli İçe Aktarmalar
Bu makaledeki tüm Python örnekleri aşağıdaki içe aktarmalara dayanır çünkü pivot türleri `aspose.cells.pivot` namespace'inde bulunur:
- `import jpype`
- `import aspose.cells as cells`
`jpype` modülü JVM'i başlatmak için kullanılırken, `aspose.cells` ise bu makale boyunca kullanılan workbook/worksheet/cell/pivot türlerini sunar.

## Çalışma Kitabındaki Tüm Pivot Tablolarını Yenileme
Çalışma kitabındaki her pivot önbelleğinin ve her pivot tablosunun en güncel kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kendi kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Performansın kritik olmadığı genel, tam belge yenilemeleri için önerilen yaklaşım budur.
Aşağıdaki örnek, bir Fruit/Year/Amount kaynak aralığıyla bir çalışma kitabı oluşturur, bir pivot tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından tek bir çağrıyla her şeyi güncel hale getirmek için `refreshAll()` yöntemini kullanır.

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

## Tek Bir Çalışma Sayfasındaki Tüm Pivot Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan pivot tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki pivot tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.refreshPivotTables()` yöntemini sunar.

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
# 8 veri satırı yaz (2-9. satırlar, A1:C9 kaynak aralığına uygun)
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
# "Pivot1" adında, hedef hücre E3'e yerleştirilen ve A1:C9'dan veri alan bir pivot tablo ekle
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunumla ilgili bir değişikliktir,
# bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTIRMEZ.
pivotTable.setRefreshDataOnOpeningFile(False)
# CalculateData(), BU pivot tablonun görünümünü (veri + stil) PivotCache'te zaten
# tutulan verilerden yeniden oluşturur. Kaynak veri değişmediği için kaynağa
# gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler yeniden hesaplanarak
# çalışma sayfası hücrelerine yazılır.
pivotTable.calculateData()
# Çalışma kitabını diske kaydet
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Tek Bir Pivot Tablosunu Yenileme
Tek bir pivot tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca pivot tablosunun görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.refresh()` Kullanın
Temel kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.getPivotCache().refresh()` yöntemidir. Bu çağrı kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

### Yalnızca Görünüm/Düzen Değişti — `calculateData()` Kullanın
Kaynak veriler değişmediyse ancak yalnızca pivot tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir bölgeye taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönüşe gerek yoktur. Önbellek zaten doğru verileri tutmaktadır; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda `pivotTable.calculateData()` doğru seçimdir.
Aşağıdaki örnek, pivot tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculateData()` yöntemini çağırır.
Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerinde oturan birçok pivot tablosu içerir. Bunları numaralandırmak için — örneğin, toplu bir yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini incelemek için — `PivotCache.getPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

## Kullanımdan Kaldırılan `PivotTable.refreshData()` Yönteminden Geçiş
Aspose.Cells for Python via Java v26.7'den önce, bir pivot tablosunu yenilemenin standart yolu her pivot tablosunda ayrı ayrı `PivotTable.refreshData()` çağırmaktı. v26.7 itibarıyla bu yöntem **kullanımdan kaldırılmış** (obsolete) olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `refreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Kaynaktan verileri, kaynak değişmemiş olsa bile *her* çağrıldığında yeniden getirir.
Önerilen alternatifler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok pivot tablosu içeren çalışma kitapları için yeni verimli kalıbı göstermektedir.

## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, mevcut yenileme API'lerini ve her birinin ne zaman seçileceğini özetlemektedir.
| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki pivot tablolarını yenileme | `Worksheet.refreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Tek bir önbellek için kaynak veriler değişti | `pivotTable.getPivotCache().refresh()` | Paylaşılan önbellek üzerindeki TÜM pivot tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan önbellek üzerindeki tüm pivot tablolarını listeleme | `pivotCache.getPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Pratikte, kullanımdan kaldırılan tablo başına `refreshData()` yöntemi yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerinden kaçınır ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

## Yaygın Tuzaklar
- **Kaydetmeden önce yenilemeyi unutmak.** Bir pivot tablosu, işlenmiş değerlerini çalışma sayfasına yalnızca veri zinciri yenilendiğinde yazar. Kaynak hücreleri değiştirirseniz, `Workbook.save()` çağrısından önce `PivotCache.Refresh()` (veya `Workbook.RefreshAll()`) çağırın; aksi takdirde kaydedilen dosya hâlâ eski toplulaştırılmış değerleri içerir.
- **Tablo başına kullanımdan kaldırılan `RefreshData()` yöntemini çağırmak.** v26.7'de `PivotTable.RefreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrı için kaynağı yeniden getirir. Bir önbelleği paylaşan birden çok pivot tablosuyla bu, N gereksiz kaynak getirmesi anlamına gelir. Bunun yerine, tek bir `PivotCache.Refresh()` çağrısının ardından tablo başına `CalculateData()` kullanın.
- **Yalnızca düzen değiştiğinde yenileme yapmak.** Yalnızca bir pivot tablosunun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirdiyseniz ve kaynak verilere dokunmadıysanız, `PivotCache.Refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData()` çağırın.
- **`PivotCache.Refresh()` tarafından desteklenmeyen harici kaynak.** Pivot tablosunun kaynağı harici bir bağlantıdan geliyorsa (veritabanı, OLAP küpü vb.), v26.7'de `PivotCache.Refresh()` onu yenileyemez — şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini desteklemektedir. Harici kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python" >}}