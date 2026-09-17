---
title: Aspose.Cells for Python via .NET'te Özet Tablolarını ve Özet Önbelleklerini Yenileme
linktitle: Aspose.Cells for Python via .NET'te Özet Tablolarını ve Özet Önbelleklerini Yenileme
description: Aspose.Cells for Python via .NET'te v26.7+ özet tablosu yenileme API'sini kullanarak özet tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables konularını pratik kod örnekleriyle ele almaktadır.
keywords: Aspose.Cells, Python via .NET, özet tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, özet verilerini çalışma kitabının tamamından tek bir özet tablosuna kadar dört farklı kapsamda yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Python via .NET v26.7** sürümünden itibaren, eski yöntem olan `PivotTable.refresh_data()` kullanım dışı olarak işaretlenmiş olup bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'ler ile değiştirilmelidir.
{{% /alert %}}

## Giriş
Bir özet tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şudur:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine kuruludur; tüm veriler burada toplanır ve gruplanır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Cells** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.

{{% alert color="primary" %}}
`PivotCache.source_type` (numaralandırma `PivotTableSourceType`), önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini desteklemektedir — yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.
{{% /alert %}}

Bu zincir nedeniyle Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotTable.calculate_data()`** — veri kaynağına geri dönüş olmaksızın, zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar.
Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynak verilerini kullanır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı şekilde davranır.

## Hızlı Başlangıç
Çalışma kitabındaki her özet tablosunu yenileyen en kısa olası koda ihtiyacınız varsa, tek bir çağrı yeterlidir:

```python
import aspose.cells as ac
# Yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# A1:C1 hücrelerine başlık satırı yaz
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# A2:C9 hücrelerine veri satırları yaz (2020 ve 2021 yıllarına yayılmış 8 satır meyve verisi)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)
worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)
worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)
worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)
worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)
worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)
worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)
worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)
# Bir pivot tablo ekle: kaynak aralık "A1:C9", hedef hücre "E3", ad "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Pivot alanlarını ata: Fruit Satırlara, Year Sütunlara, Amount Veriye
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Amount değerini değiştir
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)
# Çalışma kitabındaki tüm pivot tablolarını / pivot önbelleğini yenile
workbook.refresh_all()
# Çalışma kitabını kaydet
workbook.save("output.xlsx")
```

Bu makaledeki diğer her şey, bunun yerine ne zaman daha dar kapsamlı bir API seçmeniz gerektiğini açıklar.

## Gerekli İçe Aktarmalar
Bu makaledeki tüm Python örnekleri, özet tablosu türlerinin `aspose.cells.pivot` ad alanında bulunması nedeniyle aşağıdaki üç içe aktarma ifadesiyle başlar:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme
Çalışma kitabındaki her özet önbelleğinin ve her özet tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refresh_all()`'dur. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Bu yaklaşım, performansın endişe olmadığı genel, tam belge yenilemeleri için önerilen yöntemdir.
Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıda güncel hale getirmek için `refresh_all()` kullanır.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)
worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)
worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)
worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)
worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)
worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)
worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekebilir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmamalıdır. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.refresh_pivot_tables()` yöntemini sunar.

```python
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

## Tek Bir Özet Tablosunu Yenileme
Tek bir özet tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi yoksa yalnızca özet tablosunun görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.refresh()` Kullanın
Temel kaynak veriler değiştiyse, doğru giriş noktası `pivot_table.pivot_cache.refresh()`'tir. Bu çağrı, kaynak verileri önbelleğe geri okur ve ardından bu önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

### Yalnızca Görünüm/Düzen Değişti — `calculate_data()` Kullanın
Kaynak veriler değişmediyse, ancak yalnızca özet tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir bölgeye taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutmaktadır; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda `pivot_table.calculate_data()` doğru seçimdir.
Aşağıdaki örnek, özet tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculate_data()` çağırır.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Fruit / Year / Amount başlık satırını yaz
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# 8 veri satırı yaz (satır 2-9, A1:C9 kaynak aralığına uygun)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)
# "Pivot1" adında, hedef hücre E3'e yerleştirilen ve A1:C9'dan beslenen bir pivot tablo ekle
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunum amaçlı bir değişikliktir,
# bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTİRMEZ.
pivot_table.refresh_data_on_opening_file = False
# CalculateData() BU pivot tablosunun görüntüsünü (veri + stil) PivotCache'te
# zaten tutulan verilerden yeniden işler. Kaynak veri değişmediği için,
# kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler
# çalışma sayfası hücrelerine yeniden hesaplanır.
pivot_table.calculate_data()
# Çalışma kitabını diske kaydet
workbook.save("output.xlsx")
```

Bir çalışma kitabı genellikle tek bir paylaşılan önbellek üzerinde oturan birçok özet tablosu içerir. Bunları numaralandırmak için — örneğin toplu bir yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini incelemek için — `PivotCache.get_pivot_tables()` kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

## Kullanım Dışı `PivotTable.refresh_data()` Yönteminden Geçiş
Aspose.Cells for Python via .NET v26.7 sürümünden önce, bir özet tablosunu yenilemenin standart yolu her özet tablosunda ayrı ayrı `PivotTable.refresh_data()` çağırmaktı. v26.7 itibarıyla bu yöntem **kullanım dışı** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'ler ile değiştirilmelidir.
Tablo başına `refresh_data()` yaklaşımının gerçek dünya çalışma kitaplarında sorunlu olmasının iki nedeni vardır:
- Kaynak değişmemiş olsa bile, her çağrıldığında verileri kaynaktan *her seferinde* yeniden getirir.
Önerilen değiştirmeler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok özet tablosuna sahip çalışma kitapları için yeni verimli kalıbı göstermektedir.

## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, mevcut yenileme API'lerini özetler ve her birinin ne zaman seçilmesi gerektiğini açıklar.
| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenile | `Workbook.refresh_all()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki özet tablolarını yenile | `Worksheet.refresh_pivot_tables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Tek bir önbellek için kaynak veriler değişti | `pivot_table.pivot_cache.refresh()` | Paylaşılan önbellek üzerindeki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivot_table.calculate_data()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan önbellekteki tüm özet tablolarını listele | `pivot_cache.get_pivot_tables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Uygulamada, tablo başına eski `refresh_data()` yöntemi yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerini önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

## Yaygın Hatalar
- **Kaydetmeden önce yenilemeyi unutmak.** Bir özet tablosu, veri zinciri yenilendiğinde yalnızca işlenmiş değerlerini çalışma sayfasına yazar. Kaynak hücrelerini değiştirdiyseniz, `Workbook.save()` çağrısından önce `PivotCache.Refresh()` (veya `Workbook.RefreshAll()`) çağırın; aksi takdirde kaydedilen dosya hâlâ eski gruplanmış değerleri içerir.
- **Tablo başına kullanım dışı `RefreshData()` çağırmak.** v26.7'de `PivotTable.RefreshData()` kullanım dışı olarak işaretlenmiştir ve her çağrı için kaynağı yeniden getirir. Bir önbelleği paylaşan birden çok özet tablosuyla bu, N adet gereksiz kaynak getirmesi anlamına gelir. Bunun yerine tek bir `PivotCache.Refresh()` ve ardından tablo başına `CalculateData()` kullanın.
- **Yalnızca düzen değiştiğinde yenileme yapmak.** Özet tablosunun yalnızca görünümünü değiştirdiyseniz (sütun sırası, `ConsolidationFunction` vb.) ve kaynak verilere dokunmadıysanız, `PivotCache.Refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData()` çağırın.
- **`PivotCache.Refresh()` tarafından desteklenmeyen harici kaynak.** Özet tablosunun kaynağı harici bir bağlantıdan geliyorsa (veritabanı, OLAP küpü vb.), `PivotCache.Refresh()` v26.7'de bunu yenileyemez — şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini desteklemektedir. Harici kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="python-net" >}}