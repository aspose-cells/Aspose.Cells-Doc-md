---
title: Aspose.Cells for Python via .NET'te Pivot Tabloları Yenileme
linktitle: Aspose.Cells for Python via .NET'te Pivot Tabloları Yenileme
description: Aspose.Cells for Python via .NET'te v26.7+ pivot-yenileme API'sini kullanarak pivot tabloları nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables API'lerini pratik kod örnekleriyle ele almaktadır.
keywords: Aspose.Cells, Python via .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, pivot verilerini dört farklı kapsamda — tüm çalışma kitabından tek bir pivot tabloya kadar — yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Aspose.Cells for Python via .NET v26.7** ile başlayarak, eski `PivotTable.refresh_data()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiş olup bu makalede açıklanan daha verimli, önbellek-farkındalığına sahip API'ler ile değiştirilmelidir.

{{% /alert %}}

## Giriş

Bir pivot tabloyu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.

Dört katmanlı veri zinciri şudur:

1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her pivot tablo bir `PivotCache` üzerine inşa edilir; tüm veriler burada toplanır ve özetlenir.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` *yalnızca* kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Cells** — `PivotTable`'in hesaplanan değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.

Özellikle önemli bir kavram **paylaşılan önbellek (shared cache)**'tir. Bir çalışma kitabındaki birden fazla pivot tablo aynı kaynak aralığa başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok pivot tablo tarafından başvurulabilir ve bu önbelleği yenilemek, ona bağlı her `PivotTable`'ı bir anda yeniler.

{{% alert color="primary" %}}

`PivotCache.source_type` (`PivotTableSourceType` enum'u) önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında bulunan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.

{{% /alert %}}

Bu zincir nedeniyle Aspose.Cells'te iki temel yenileme yolu vardır:

- **`PivotCache.refresh()`** — kaynaktan önbelleğe yeniden yükler VE tek bir işlemde ona bağlı tüm `PivotTable`'ları yeniden hesaplar.
- **`PivotTable.calculate_data()`** — veri kaynağına geri dönmeden, zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar.

Bu makaledeki tüm senaryolarda çalışma sayfası hücresi kaynak verileri kullanılır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı gibi çalışır.

## Gerekli İçe Aktarmalar (Imports)

Bu makaledeki tüm Python örnekleri, pivot türlerinin `aspose.cells.pivot` namespace'inde bulunması nedeniyle aşağıdaki üç içe aktarma ifadesi ile başlar:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Çalışma Kitabındaki Tüm Pivot Tabloları Yenileme

Çalışma kitabındaki her pivot önbelleğinin ve her pivot tablosunun en son kaynak verileri yansıttığından emin olmanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refresh_all()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Bu, performansın endişe olmadığı genel, tam belge yenilemeleri için önerilen yaklaşımdır.

Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir pivot tablo oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıda güncel hale getirmek için `refresh_all()` kullanır.

```python
import aspose.cells as ac

# Yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# A1:C1 hücrelerine başlık satırı yaz
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# A2:C9 hücrelerine veri satırları yaz (2020 ve 2021 yıllarına dağıtılmış 8 satır meyve verisi)
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

# Pivot alanlarını ata: Satırlar'a Fruit, Sütunlar'a Year, Veri'ye Amount
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Değişiklikleri simüle etmek için kaynak verideki birkaç Amount değerini değiştir
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Çalışma kitabındaki tüm pivot tabloları / pivot önbelleklerini yenile
workbook.refresh_all()

# Çalışma kitabını kaydet
workbook.save("output.xlsx")
```

## Tek Bir Çalışma Sayfasındaki Tüm Pivot Tabloları Yenileme

Bazen yalnızca belirli bir çalışma sayfasında bulunan pivot tabloları yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki pivot tabloların ilgisiz olduğu bilindiğinde ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.refresh_pivot_tables()` yöntemini sağlar.

Bu, `Workbook.refresh_all()` yönteminden daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki pivot tablolar yenilenir, diğer çalışma sayfalarındaki pivot tablolara dokunulmaz.

Aşağıdaki örnek aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir pivot tablo ekler, bazı kaynak değerlerini değiştirir ve ardından yalnızca o çalışma sayfasındaki pivot tabloları yeniler.

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

## Tek Bir Pivot Tabloyu Yenileme

Tek bir pivot tablo üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, aslında neyin değiştiğine bağlıdır: altta yatan kaynak veriler mi, yoksa yalnızca pivot tablonun kendisinin görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.refresh()` Kullanın

Altta yatan kaynak veriler değiştiyse, doğru giriş noktası `pivot_table.pivot_cache.refresh()` yöntemidir. Bu çağrı kaynak verilerini önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

{{% alert color="primary" %}}

Pivot tablolar tek bir `PivotCache` örneğini paylaştığından, `PivotCache.refresh()` çağrısı aynı önbellek üzerine inşa edilmiş **tüm** pivot tabloları yeniden hesaplar — yalnızca başvurduğunuz pivot tabloyu değil. İki pivot tablo aynı kaynak aralığı paylaşıyorsa, bir önbelleği yenilemek ikisini birden yeniler.

{{% /alert %}}

Aşağıdaki örnek, bu paylaşılan önbellek davranışını göstermek için aynı kaynak aralığı üzerinde iki pivot tablo oluşturur, bazı kaynak değerlerini değiştirir ve ardından bir önbellek başvurusu üzerinden yenileme yapar.

```python
import aspose.cells as ac

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Başlık satırını yaz: Meyve / Yıl / Miktar
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Yaklaşık 9 veri satırı yaz (üzüm / yaban mersini / kivi / kiraz, 2020-2021 yılları arasında)
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
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# E3 hücresine bağlı "Pivot1" adlı ilk özet tabloyu ekle, kaynak aralığı A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Pivot1 için alanları ata
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Aynı kaynak aralığı A1:C9 kullanarak E15'e bağlı "Pivot2" adlı İKİNCİ bir özet tablo ekle
# Hem Pivot1 hem de Pivot2, kaynak aralıkları aynı olduğu için tek bir PivotCache'i paylaşır.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Pivot2 için aynı alanları ata
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Veri değişikliğini simüle etmek için kaynak verilerdeki birkaç Miktar hücresi değerini değiştir
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Paylaşılan PivotCache'i yenile.
# Pivot1 ve Pivot2 aynı PivotCache'i paylaştığı için bu tek çağrı
# güncellenmiş kaynaktan HER İKİ özet tabloyu da (veri + stil) yeniler.
pivotTable1.pivot_cache.refresh()

# Çalışma kitabını kaydet
workbook.save("output.xlsx")
```

### Yalnızca Görünüm/Düzen Değişti — `calculate_data()` Kullanın

Kaynak veriler değişmediyse ancak yalnızca pivot tablonun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutuyor; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekiyor. Bu durumda `pivot_table.calculate_data()` doğru seçimdir.

Bu, gereksiz kaynak getirme işlemini önler ve birçok pivot tablo aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.

Aşağıdaki örnek pivot tablonun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculate_data()` çağırır.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fruit / Yıl / Tutar başlık satırını yaz
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 8 veri satırı yaz (2-9. satırlar, A1:C9 kaynak aralığına uygun)
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

# Hedef hücre E3'e yerleştirilen, A1:C9'dan kaynak alan "Pivot1" adında bir pivot tablo ekle
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunum amaçlı bir değişikliktir,
# bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını gerektirmez.
pivot_table.refresh_data_on_opening_file = False

# CalculateData() bu pivot tablonun görüntüsünü (veri + stil) PivotCache'te
# zaten tutulan verilerden yeniden oluşturur. Kaynak veriler değişmediği için
# kaynağa geri dönüş yapılmaz — yalnızca önbelleğe alınmış değerler
# çalışma sayfası hücrelerine yeniden hesaplanır.
pivot_table.calculate_data()

# Çalışma kitabını diske kaydet
workbook.save("output.xlsx")
```

## Aynı PivotCache'i Paylaşan Tüm Pivot Tabloları Alma

Bir çalışma kitabı sıklıkla tek bir paylaşılan önbellek üzerinde oturan birçok pivot tablo içerir. Bunları numaralandırmak için — örneğin, toplu yenileme yapmadan önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.get_pivot_tables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı olan her `PivotTable`'ın koleksiyonunu döndürür.

Bu aynı zamanda iki pivot tablonun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilir veya `get_pivot_tables()` tarafından döndürülen koleksiyonu yineleyerek hangi pivot tabloların onun içinde göründüğünü gözlemleyebilirsiniz.

Aşağıdaki örnek aynı kaynak aralığı üzerinde iki pivot tablo oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin pivot tablolarını numaralandırır.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

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
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## Kullanımdan Kaldırılan `PivotTable.refresh_data()` Yönteminden Geçiş (Migration)

Aspose.Cells for Aspose.Cells for Python via .NET v26.7 öncesinde, bir pivot tabloyu yenilemenin standart yolu her pivot tabloda ayrı ayrı `PivotTable.refresh_data()` çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış (obsolete)** olarak işaretlenmiş olup yukarıda açıklanan önbellek-farkındalığına sahip API'ler ile değiştirilmelidir.

Gerçek dünya çalışma kitaplarında tablo başına `refresh_data()` yaklaşımının sorunlu olmasının iki nedeni vardır:

- Kaynak değişmemiş olsa bile *her* çağrıldığında verileri kaynaktan yeniden getirir.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok pivot tablo tek bir önbelleği paylaştığında, pivot tablo başına tekrar tekrar `refresh_data()` çağırmak aynı önbelleğin sürekli olarak yeniden getirilmesine neden olur ve bu çok yavaştır.

Önerilen alternatifler şunlardır:

- **Çalışma kitabındaki TÜM pivot tabloları yenileme** → `workbook.refresh_all();` kullanın.
- **Bazılarını yenileme** → tek bir önbellek için `pivot_table.pivot_cache.refresh();` kullanın. Önbellek paylaşıldığından, bu tek çağrı o önbellek üzerine inşa edilmiş her pivot tabloyu günceller. Zaten yenilenmiş bir önbellek üzerinde oturan diğer pivot tablolar güvenle atlanabilir.
- **Yalnızca pivot görünümü/düzeni değişti** → kaynak verilerine geri dönmeden mevcut önbellekten yeniden işlemek için `pivot_table.calculate_data();` kullanın.

Aşağıdaki örnek, tek bir önbelleği paylaşan birden fazla pivot tabloya sahip çalışma kitapları için yeni verimli kalıbı (pattern) göstermektedir.

```python
import aspose.cells as ac

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Kaynak veriyi oluştur: Meyve / Yıl / Miktar (başlık + 9 satır) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- E3 hedef hücresine ilk pivot tablosunu (Pivot1) ekle ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- AYNI kaynak aralığa İKİNCİ pivot tablosunu (Pivot2) ekle ---
# Hem Pivot1 hem Pivot2 TEK bir PivotCache'i paylaşır.
# Bu, eski tablo başına RefreshData() yaklaşımının verimsiz hale geldiği
# tam olarak senaryodur: bir tabloyu yenilemek tüm paylaşılan önbelleği
# yeniden çeker, dolayısıyla N tabloyu yenilemek aynı pahalı çekme işlemini
# N kez yapar.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Kaynak verideki birkaç Miktar değerini değiştir ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- ESKİMİŞ örüntü (26.7 öncesi) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # kaynaktan yeniden çeker, tüm önbelleği yeniler
# pivot_table2.refresh_data();  # TEKRAR yeniden çeker — önbellek zaten taze!
# Her çağrı paylaşılan önbelleği yeniden oluşturur, dolayısıyla N tablo = N gereksiz çekme.

# --- YENİ v26.7+ örüntü: önbelleği BİR KEZ yenile, sonra gerektiğinde yeniden oluştur ---
# PivotCache.Refresh() için tek bir çağrı, değiştirilen değerleri paylaşılan
# önbelleğe çeker VE onu referans alan HER pivot tablosunun görüntüsünü yeniden hesaplar.
# Pivot1 ve Pivot2 bir PivotCache'i paylaştığından, bu tek çağrı her iki tabloyu da
# günceller — ikinci bir kaynak gidip gelmesi gerekmez.
pivot_table1.pivot_cache.refresh()

# CalculateData() yalnızca bir pivot tablosunun görüntüsünü (veri + stil) önbellekte
# zaten bulunan verilerden yeniden oluşturur — kaynağa DOKUNMAZ.
# CalculateData() işlevini burada Pivot2 üzerinde yalnızca API'yi göstermek için çağırıyoruz:
# önbellek bir kez yenilendikten sonra, kaynağa geri dönmeden herhangi bir bağımlı tablo
# yeniden oluşturulabilir. Yalnızca pivot tablosunun görünüm/düzen ayarları değiştiğinde ve
# önbellek güncel olduğunda CalculateData() işlevini tek başına kullanın.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## Hangi Yenileme API'sini Kullanmalıyım?

Aşağıdaki tablo mevcut yenileme API'lerini özetlemekte ve her birinin ne zaman seçileceğini göstermektedir.

| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.refresh_all()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki pivot tabloları yenileme | `Worksheet.refresh_pivot_tables()` | Tek bir çalışma sayfasıyla sınırlı. |
| Bir önbellek için kaynak verileri değişti | `pivot_table.pivot_cache.refresh()` | O paylaşılan önbellek üzerindeki TÜM pivot tabloları yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivot_table.calculate_data()` | Gereksiz kaynak veri gidiş-dönüşünü atlar. |
| Paylaşılan önbellek üzerindeki tüm pivot tabloları listeleme | `pivot_cache.get_pivot_tables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |

Uygulamada, kullanımdan kaldırılmış tablo başına `refresh_data()` yöntemi yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmeleri önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

{{< app/cells/assistant language="python" >}}