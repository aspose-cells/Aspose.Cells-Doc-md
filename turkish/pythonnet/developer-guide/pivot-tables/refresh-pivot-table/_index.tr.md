---
title: Aspose.Cells for Python via .NET ile Pivot Tablolarını ve Pivot Önbelleklerini Yenileyin
linktitle: Aspose.Cells for Python via .NET ile Pivot Tablolarını ve Pivot Önbelleklerini Yenileyin
description: Aspose.Cells for Python via .NET içinde v26.7+ Pivot yenileme API'sini kullanarak Pivot Tablolarının nasıl yenilendiğini öğrenin. Bu makale, RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables işlevlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, Python via .NET, Pivot Tablosu, yenile, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma kitabının tamamından tek bir Pivot Tablosuna kadar dört farklı kapsamda Pivot verilerini yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Python via .NET v26.7** sürümünden başlayarak, eski `PivotTable.refresh_data()` yöntemi eskimiş olarak işaretlenir ve bu makalede açıklanan daha verimli, önbellek farkındalıklı API'lerle değiştirilmelidir.
{{% /alert %}}

## Introduction
Bir Pivot Tablosunu yenileme nadiren tek işlemden oluşur. Aspose.Cells, özgün kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri sürdürür. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şöyledir:
1. **Veri Kaynağı** — özgün çalışma sayfası aralıkları, veritabanı sorgusu veya birleştirme aralığıdır; ham değerler burada bulunur.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsüdür. Her Pivot Tablosu bir `PivotCache` üzerine kurulur; tüm veriler burada toplanır ve birleştirilir.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesidir. Bir `PivotTable` veri kaynağına hiçbir zaman doğrudan erişmez; yalnızca `PivotCache` üzerinden okur.
4. **Cells** — `PivotTable`nin hesaplanan değerlerini ve biçimlerini işlediği çalışma sayfası `Cells` koleksiyonudur.

{{% alert color="primary" %}}
`PivotCache.source_type` (`PivotTableSourceType` enum değeri), önbellek verisinin nereden geldiğini belirtir. v26.7 itibarıyla `PivotCache.refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — başka deyişle çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) önbellek API'si üzerinden henüz yenilenemez.
Bu nedenle Aspose.Cells içinde iki temel yenileme yolu vardır:
- **`PivotTable.calculate_data()`** — önbelleğe alınmış verilerden tek bir `PivotTable`nin görüntüsünü yeniden hesaplar; veri kaynağına geri dönüş yapmaz.
Bu makaledeki tüm senaryolar çalışma sayfası hücrelerinden kaynak veri kullanır; bu nedenle kaynak türü `Sheet` olur ve yenileme işlemleri açıklandığı gibi davranır.
{{% /alert %}}

## Quick Start
Yalnızca çalışma kitabındaki tüm Pivot Tablolarını yenileyen en kısa kodu gerekiyorsa, tek bir çağrı yeterlidir:

```python
import aspose.cells as ac

workbook = ac.Workbook("input.xlsx")
workbook.refresh_all()
workbook.save("output.xlsx")
```

Bu makalenin geri kalanı, daha dar kapsamlı bir API'yi ne zaman seçmeniz gerektiğini açıklar.

## Required Imports
Bu makaledeki tüm Python örnekleri, Pivot türlerinin `aspose.cells.pivot` namespace'inde bulunması nedeniyle aşağıdaki üç içe aktarma ifadesiyle başlar:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Refresh All Pivot Tables in the Workbook
Çalışma kitabındaki her önbelleğin ve her Pivot Tablosunun en son kaynak verileri yansıtmasını sağlamak istediğinizde, en basit ve kapsamlı API `Workbook.refresh_all()` yöntemidir. Tek çağrı tüm çalışma kitabı boyunca ilerler; her `PivotCache` öğesini kaynağından yeniler ve ardından bu önbelleğe bağlı her `PivotTable` nesnesini yeniden hesaplar. Performansın bir sorun olmadığı genel, belgenin tamamını kapsayan yenileme işlemleri için bu yaklaşım önerilir.
Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir Pivot Tablosu yaratır, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncellemek için `refresh_all()` yöntemini kullanır.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write header row into cells A1:C1
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(50)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(60)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(70)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(80)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(90)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(100)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(110)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(120)
# Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.cells.get("C2").put_value(55)
worksheet.cells.get("C5").put_value(85)
worksheet.cells.get("C9").put_value(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refresh_all()
# Save the workbook
workbook.save("output.xlsx")
```

## Refresh All Pivot Tables on a Single Worksheet
Bazı durumlarda yalnızca belirli bir çalışma sayfasında bulunan Pivot Tablolarını yenilemeniz gerekir. Örneğin diğer çalışma sayfalarındaki Pivot Tablolarının ilişkisiz olduğu biliniyorsa ve bunlara dokunulmamalıdır. Bu durumda Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı `Worksheet.refresh_pivot_tables()` yöntemini sunar.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2021)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2021)
worksheet.cells.get("C5").put_value(120)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(180)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2020)
worksheet.cells.get("C7").put_value(130)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(220)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2020)
worksheet.cells.get("C9").put_value(140)
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
worksheet.cells.get("C2").put_value(300)
worksheet.cells.get("C5").put_value(250)
worksheet.cells.get("C9").put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Refresh a Single Pivot Table
Tek bir Pivot Tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca Pivot Tablosunun kendi görünüm veya düzen ayarları mı?

### Source Data Changed — Use `PivotCache.refresh()`
Temel kaynak verileri değiştiyse doğru başlangıç noktası `pivot_table.pivot_cache.refresh()` yöntemidir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından bu önbelleğe bağlı olan her `PivotTable` nesnesini yeniden hesaplar.

### Only View/Layout Changed — Use `calculate_data()`
Kaynak verileri değişmediyse, yalnızca Pivot Tablosunun görünüm veya düzen ayarları değiştirilmişse — örneğin bir alan farklı bir bölgeye taşınmışsa veya açılışta yenileme ayarı değiştirilmişse — veri kaynağına geri dönüşe gerek yoktur. Önbellek zaten doğru verileri içerir; yalnızca işlenmiş `PivotTable` yeniden hesaplanmalıdır. Bu durumda doğru seçim `pivot_table.calculate_data()` yöntemidir.
Aşağıdaki örnek, Pivot Tablosunun kaynakla ilgili olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculate_data()` yöntemini çağırır.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write Fruit / Year / Amount header row
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(150)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(250)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(350)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(450)
# Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivot_table.refresh_data_on_opening_file = False
# calculate_data() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivot_table.calculate_data()
# Save the workbook to disk
workbook.save("output.xlsx")
```

Bir çalışma kitabı genellikle aynı paylaşılan önbelleğin üzerine kurulmuş çok sayıda Pivot Tablosu içerir. Bunları sıralamak için — örneğin toplu yenileme gerçekleştirmeden önce veya paylaşılan önbelleğin etkisini tanılamak için — `PivotCache.get_pivot_tables()` yöntemini kullanın. Bu yöntem, belirtilen önbelleğe bağlı tüm `PivotTable` nesnelerinden oluşan koleksiyonu döndürür.

## Migrating from the Obsolete `PivotTable.refresh_data()`
Aspose.Cells for Python via .NET v26.7 sürümünden önce, bir Pivot Tablosunu yenilemenin standart yolu her Pivot Tablosunda ayrı ayrı `PivotTable.refresh_data()` çağırmaktı. v26.7 itibarıyla bu yöntem **eskimiş** olarak işaretlenir ve yukarıda açıklanan önbellek farkındalıklı API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `refresh_data()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Kaynak değişmemiş olsa bile her çağrıda verileri kaynaktan yeniden getirir.
Önerilen değişiklikler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden fazla Pivot Tablosu içeren çalışma kitapları için yeni ve verimli kalıbı gösterir.

## Which Refresh API Should I Use?
Aşağıdaki tablo, kullanılabilir yenileme API'lerini ve her birinin ne zaman seçilmesi gerektiğini özetler.
| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenile | `Workbook.refresh_all()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki Pivot Tablolarını yenile | `Worksheet.refresh_pivot_tables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Bir önbelleğin kaynak verisi değişti | `pivot_table.pivot_cache.refresh()` | Paylaşılan önbellekteki TÜM Pivot Tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivot_table.calculate_data()` | Gereksiz kaynak gidiş-dönüşünü atlar. |
| Paylaşılan bir önbellekteki tüm Pivot Tablolarını listele | `pivot_cache.get_pivot_tables()` | Toplu yenilemeden önce sıralamak için kullanın. |
Uygulamada, eskimiş tablo başına `refresh_data()` yaklaşımı yerine önbellek tabanlı API'leri tercih edin. Bu API'ler paylaşılan önbelleklerin farkındadır, gereksiz kaynak veri getirmelerini önler ve yenileme gereksiniminizi karşılayan en dar kapsamı seçmenize olanak tanır.

## Common Pitfalls
- **Kaydetmeden önce yenilemeyi unutmak.** Bir Pivot Tablosu, veri zinciri yenilendiğinde işlenmiş değerlerini çalışma sayfasına yazar. Kaynak hücrelerini değiştirdiyseniz `Workbook.save()` çağrısından önce `PivotCache.refresh()` (veya `Workbook.refresh_all()`) çağrısı yapın; aksi halde kaydedilen dosya hâlâ eski birleştirilmiş değerleri içerir.
- **Her tablo için eskimiş `refresh_data()` çağırmak.** v26.7'de `PivotTable.refresh_data()` eskimiş olarak işaretlenir ve her çağrıda kaynağı yeniden getirir. Birden fazla Pivot Tablosu bir önbelleği paylaştığında bu, N gereksiz kaynak getirmesi anlamına gelir. Bunu tek bir `PivotCache.refresh()` çağrısı ve ardından her tablo için `calculate_data()` çağrısıyla değiştirin.
- **Yalnızca düzen değiştiğinde yenilemek.** Bir Pivot Tablosunun görünümünü — sütun sırasını, `ConsolidationFunction` vb. — değiştirdiyseniz ve kaynak verilere dokunmadıysanız, `PivotCache.refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.calculate_data()` çağrısı yapın.
- **`PivotCache.refresh()` tarafından desteklenmeyen harici kaynak.** Pivot Tablosunun kaynağı harici bir bağlantıdan geliyorsa — veritabanı, OLAP küpü vb. — `PivotCache.refresh()` v26.7'de bunu yenileyemez; hâlâ yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Harici kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="python-net" >}}