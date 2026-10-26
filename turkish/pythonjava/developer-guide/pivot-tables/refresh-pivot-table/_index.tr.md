---
title: Aspose.Cells for Python via Java ile Özet Tablolarını ve Pivot Önbelleklerini Yenileme
linktitle: Aspose.Cells for Python via Java ile Özet Tablolarını ve Pivot Önbelleklerini Yenileme
description: Aspose.Cells for Python via Java ile v26.7+ özet tablo yenileme API'sini kullanarak özet tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale, refreshAll, refreshPivotTables, PivotCache.refresh, calculateData ve getPivotTables yöntemlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, Python via Java, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, özet tablo verilerini dört farklı kapsamda — çalışma kitabının tamamından tek bir özet tablosuna kadar — yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Python via Java v26.7** sürümünden itibaren, eski `PivotTable.refreshData()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek destekli API'lerle değiştirilmelidir.
{{% /alert %}}

## Introduction
Bir özet tablosunu yenileme genellikle tek bir işlem değildir. Arka planda Aspose.Cells, orijinal kaynak verileri çalışma sayfasında görüntülenen hesaplanmış değerlere bağlayan katmanlı bir veri zinciri yönetir. Bu zinciri anlamak, her durumda doğru yenileme API'sini seçmenin temelidir.
Dört katmanlı veri zinciri şöyledir:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine kurulur; tüm veriler burada toplanır ve toplulaştırılır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` verileri *yalnızca* kendi `PivotCache`'inden okur; veri kaynağından doğrudan asla okumaz.
4. **Cells** — `PivotTable` tarafından hesaplanan değerlerin ve biçimlendirmelerin işlendiği çalışma sayfası `Cells` öğeleri.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`), önbellek verisinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.refresh()` yalnızca **`SHEET`** ve **`CONSOLIDATION`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında bulunan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.
Bu zincir nedeniyle Aspose.Cells içinde iki temel yenileme yolu vardır:
- **`PivotTable.calculateData()`** — veri kaynağına geri dönmeden, zaten önbelleğe alınmış verilerden tek bir `PivotTable` öğesinin görünümünü yeniden hesaplar.
Bu makaledeki tüm senaryolar çalışma sayfası hücrelerinden gelen kaynak verileri kullandığından, kaynak türü `SHEET` olur ve yenileme işlemleri açıklandığı gibi çalışır.
{{% /alert %}}

## Quick Start
Yalnızca çalışma kitabındaki tüm özet tabloları yenilemek için gereken en kısa kodu istiyorsanız, tek bir çağrı yeterlidir:

```python
import jpype
from asposecells.api import Workbook

workbook = Workbook("input.xlsx")
workbook.refreshAll()
workbook.save("output.xlsx")
```

Bu makalenin geri kalanında, ne zaman daha dar kapsamlı bir API seçmeniz gerektiği açıklanmaktadır.

## Required Imports
Bu makaledeki tüm Python örnekleri, özet tablo türlerinin `aspose.cells.pivot` ad alanında bulunması nedeniyle aşağıdaki içe aktarmalara dayanır:
- `import jpype`
- `import aspose.cells as cells`
`jpype` modülü JVM'i başlatmak için kullanılır; `aspose.cells` ise makale boyunca kullanılan çalışma kitabı, çalışma sayfası, hücre ve özet tablo türlerini sunar.

## Refresh All Pivot Tables in the Workbook
Çalışma kitabındaki her pivot önbelleğinin ve her özet tablosunun güncel kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabı boyunca ilerler — her `PivotCache`'i kendi kaynağından yeniler ve ardından bunlara bağlı her `PivotTable`'ı yeniden hesaplar. Bu, performansın önemli olmadığı genel amaçlı ve belgenin tamamını kapsayan yenileme işlemleri için önerilen yaklaşımdır.
Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığı içeren bir çalışma kitabı oluşturur, bir özet tablosu ekler, bazı kaynak değerlerini değiştirir ve ardından `refreshAll()` yöntemini kullanarak tüm özet verilerini tek bir çağrıyla günceller.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
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
# Add a pivot table: source range "A1:C9", destination cell "E3"
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll()
# Save the workbook
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh All Pivot Tables on a Single Worksheet
Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekebilir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmamalıysa. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı `Worksheet.refreshPivotTables()` yöntemini sağlar.

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
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

## Refresh a Single Pivot Table
Tek bir özet tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API iki seçenek sunar. Hangi seçeneğin kullanılacağı, temel kaynak verilerin mi yoksa yalnızca özet tablosunun görünüm/yerleşim ayarlarının mı değiştiğine bağlıdır.

### Source Data Changed — Use `PivotCache.refresh()`
Kaynak verileri değiştiyse, doğru giriş noktası `pivotTable.getPivotCache().refresh()` yöntemidir. Bu çağrı, kaynak verilerini yeniden okuyup önbelleğe alır ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

### Only View/Layout Changed — Use `calculateData()`
Kaynak verileri değişmemişse ve yalnızca özet tablosunun görünüm veya yerleşim ayarları değiştirilmişse (örneğin, bir alan farklı bir bölgeye taşındıysa veya açılışta yenileme ayarı açılıp kapatıldıysa), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri içerir; yalnızca `PivotTable` öğesinin yeniden hesaplanması gerekir. Bu durumda `pivotTable.calculateData()` doğru seçimdir.
Aşağıdaki örnek, özet tablosunun kaynakla ilgili olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden oluşturmak için `calculateData()` yöntemini çağırır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
# Add a pivot table placed at destination cell E3, sourcing from A1:C9
pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivotTable.calculateData()
# Save the workbook to disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Bir çalışma kitabı genellikle aynı paylaşılan önbelleğe bağlı birçok özet tablosu içerir. Bunları listelemek için — örneğin, toplu bir yenileme yapmadan önce veya paylaşılan önbelleğin etkisini değerlendirmek amacıyla — `PivotCache.getPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable` öğesinin koleksiyonunu döndürür.

## Migrating from the Obsolete `PivotTable.refreshData()`
Aspose.Cells for Python via Java v26.7 sürümünden önce, bir özet tablosunu yenilemenin standart yolu, her özet tablosunda ayrı ayrı `PivotTable.refreshData()` çağırmaktı. v26.7 sürümünde bu yöntem **kullanımdan kaldırılmış (obsolete)** olarak işaretlenmiştir ve yukarıda açıklanan önbellek destekli API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `refreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Kaynak değişmemiş olsa bile *her* çağrıldığında verileri kaynaktan yeniden alır.
Önerilen değiştirmeler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden fazla özet tablosu içeren çalışma kitapları için yeni ve verimli örnek deseni gösterir.

## Which Refresh API Should I Use?
Aşağıdaki tablo, mevcut yenileme API'lerini özetler ve her birinin ne zaman seçilmesi gerektiğini gösterir.
| Amaç | Önerilen API | Notlar |
|------|--------------|--------|
| Çalışma kitabının tamamını yenileme | `Workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve özet tabloları kapsar. |
| Yalnızca tek bir çalışma sayfasındaki özet tablolarını yenileme | `Worksheet.refreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Bir pivot önbelleğinin kaynak verileri değişti | `pivotTable.getPivotCache().refresh()` | Paylaşılan önbellekteki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/yerleşim ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynak gidiş-dönüşünü atlar. |
| Paylaşılan önbellekteki tüm özet tablolarını listeleme | `pivotCache.getPivotTables()` | Toplu yenilemeden önce listelemek için kullanın. |
Pratikte, tablo başına kullanımdan kaldırılan `refreshData()` yerine önbellek tabanlı API'leri tercih edin. Bu API'ler paylaşılan önbellekleri dikkate alır, gereksiz kaynak veri alımlarını önler ve yenileme gereksiniminizi karşılayan en dar kapsamı seçmenize olanak tanır.

## Common Pitfalls
- **Kaydetmeden önce yenilemeyi unutmak.** Bir özet tablosu, hesaplanmış değerlerini çalışma sayfasına yalnızca veri zinciri yenilendiğinde yazar. Kaynak hücrelerini değiştirirseniz, `Workbook.save()` çağrısından önce `PivotCache.refresh()` (veya `Workbook.refreshAll()`) çağırın; aksi takdirde kaydedilen dosya hâlâ eski özetlenmiş değerleri içerir.
- **Tablo başına kullanımdan kaldırılan `RefreshData()` yöntemini çağırmak.** v26.7 sürümünde, `PivotTable.RefreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrıda kaynağı yeniden alır. Bir önbelleği paylaşan birden fazla özet tablosu bulunduğunda bu, N adet gereksiz kaynak alımı anlamına gelir. Bunun yerine, tek bir `PivotCache.refresh()` çağrısının ardından tablo başına `calculateData()` kullanın.
- **Yalnızca yerleşim değiştiğinde yenileme yapmak.** Kaynak verilere dokunmadan yalnızca bir özet tablosunun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirdiyseniz, `PivotCache.refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden oluşturmak için `pivotTable.calculateData()` çağırın.
- **`PivotCache.refresh()` tarafından desteklenmeyen dış kaynak.** Özet tablosunun kaynağı bir dış bağlantıdan (veritabanı, OLAP küpü vb.) geliyorsa, `PivotCache.refresh()` onu v26.7 sürümünde yenileyemez — şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Dış kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="python" >}}