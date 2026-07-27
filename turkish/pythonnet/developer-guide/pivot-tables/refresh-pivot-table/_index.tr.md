---
title: Aspose.Cells for Python via .NET'te Özet Tabloları Yenileme
linktitle: Aspose.Cells for Python via .NET'te Özet Tabloları Yenileme
description: Aspose.Cells for Python via .NET'te v26.7+ pivot-yenileme API'sini kullanarak özet tabloları nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables yöntemlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, Python via .NET, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, özet tablo verilerini dört farklı kapsamda — çalışma kitabının tamamından tek bir özet tabloya kadar — yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Python via .NET v26.7** sürümünden itibaren eski `PivotTable.refresh_data()` yöntemi kullanımdan kaldırılmış olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'ler ile değiştirilmelidir.
{{% /alert %}}
## Giriş
Bir özet tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şudur:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya birleştirme aralığı.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsü. Her özet tablo bir `PivotCache` üzerine inşa edilir; tüm veriler burada toplanır ve gruplanır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Hücreler** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.
Özellikle önemli bir kavram **paylaşılan önbellek**tir. Bir çalışma kitabındaki birden fazla özet tablo aynı kaynak aralığa başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok özet tablo başvurabilir ve o önbelleği yenilemek, ona bağlı her `PivotTable`'ı bir defada yeniler.
{{% alert color="primary" %}}
`PivotCache.source_type` (enum `PivotTableSourceType`) önbellek verilerinin nereden geldiğini belirtir. v26.7 sürümü itibarıyla, `PivotCache.refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında yaşayan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.
{{% /alert %}}
Bu zincir nedeniyle Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotCache.refresh()`** — kaynak → önbelleği yeniden yükler VE tek bir işlemde ona bağlı tüm `PivotTable`'ları yeniden hesaplar.
- **`PivotTable.calculate_data()`** — veri kaynağına geri dönmeden, zaten önbelleğe alınmış verilerden tek bir `PivotTable` görüntüsünü yeniden hesaplar.
Bu makaledeki tüm senaryolarda çalışma sayfası hücresi kaynak verileri kullanılır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı şekilde çalışır.
## Gerekli İçe Aktarmalar
Bu makaledeki tüm Python örnekleri, pivot türlerinin `aspose.cells.pivot` namespace'inde bulunması nedeniyle aşağıdaki üç içe aktarma ifadesiyle başlar:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`
## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme
Çalışma kitabındaki her pivot önbelleğinin ve her özet tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refresh_all()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kendi kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Performansın kritik olmadığı genel, tam belge yenilemeleri için önerilen yaklaşım budur.
Aşağıdaki örnek, bir Fruit/Year/Amount kaynak aralığıyla bir çalışma kitabı oluşturur, bir özet tablosu ekler, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncellemek için `refresh_all()` yöntemini kullanır.
```python
import aspose.cells as ac

# Yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# A1:C1 hücrelerine başlık satırı yaz
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# A2:C9 hücrelerine veri satırları yaz (2020 ve 2021 yılları arasında 8 satır meyve verisi)
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

# Bir pivot tablo ekle: kaynak aralığı "A1:C9", hedef hücre "E3", ad "Pivot1"
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

# Çalışma kitabındaki tüm pivot tabloları / pivot önbelleklerini yenile
workbook.refresh_all()

# Çalışma kitabını kaydet
workbook.save("output.xlsx")
```
## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu bilindiğinde ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.refresh_pivot_tables()` yöntemini sunar.
Bu yöntem `Workbook.refresh_all()` yönteminden daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki özet tabloları yenilenir, diğer çalışma sayfalarındaki özet tablolarına dokunulmaz.
Aşağıdaki örnek aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir özet tablosu ekler, bazı kaynak değerlerini değiştirir ve ardından yalnızca o çalışma sayfasındaki özet tablolarını yeniler.
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
## Tek Bir Özet Tablosunu Yenileme
Tek bir özet tablosu üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi yoksa yalnızca özet tablosunun görünüm/düzen ayarları mı.
### Kaynak Veriler Değişti — `PivotCache.refresh()` Kullanın
Temel kaynak veriler değiştiyse, doğru giriş noktası `pivot_table.pivot_cache.refresh()` yöntemidir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.
{{% alert color="primary" %}}
Özet tabloları tek bir `PivotCache` örneğini paylaştığı için, `PivotCache.refresh()` çağrısı yalnızca başvurduğunuz özet tablosunu değil, aynı önbellek üzerine inşa edilmiş **tüm** özet tablolarını yeniden hesaplar. İki özet tablosu aynı kaynak aralığını paylaşıyorsa, bir önbelleği yenilemek her ikisini de yeniler.
{{% /alert %}}
Aşağıdaki örnek, bu paylaşılan önbellek davranışını göstermek için aynı kaynak aralığında iki özet tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından tek bir önbellek başvurusu üzerinden yenileme yapar.
```python
ac

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Başlık satırını yaz: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Yaklaşık 9 veri satırı yaz (2020-2021 arası grape / blueberry / kiwi / cherry)
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

# E3 hücresine sabitlenmiş, kaynak aralığı A1:C9 olan ilk pivot tablo "Pivot1" ekle
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Pivot1 için alanları ata
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# AYNI A1:C9 kaynak aralığını kullanarak E15'e sabitlenmiş İKİNCİ pivot tablo "Pivot2" ekle
# Pivot1 ve Pivot2, kaynak aralığı aynı olduğu için tek bir PivotCache'i paylaşır.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Pivot2 için aynı alanları ata
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Veri değişikliğini simüle etmek için kaynak verideki birkaç Amount hücre değerini değiştir
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Paylaşılan PivotCache'i yenile.
# Pivot1 ve Pivot2 aynı PivotCache'i paylaştığı için, bu tek çağrı güncellenmiş kaynaktan HER İKİ pivot tabloyu da (veri + stil) yeniler.
pivotTable1.pivot_cache.refresh()

# Çalışma kitabını kaydet
workbook.save("output.xlsx")
```
### Yalnızca Görünüm/Düzen Değişti — `calculate_data()` Kullanın
Kaynak veriler değişmediyse, ancak yalnızca özet tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir bölgeye taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutuyor; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekiyor. Bu durumda `pivot_table.calculate_data()` doğru seçimdir.
Bu yaklaşım, gereksiz kaynak getirme işleminden kaçınır ve birçok özet tablosu aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.
Aşağıdaki örnek, özet tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculate_data()` yöntemini çağırır.
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fruit / Year / Amount başlık satırını yaz
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 8 veri satırı yaz (2-9. satırlar, kaynak aralığı A1:C9'a uyuyor)
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

# E3 hücresine yerleştirilen, A1:C9'dan beslenen "Pivot1" adlı bir pivot tablo ekle
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunumla ilgili bir değişikliktir,
# dolayısıyla PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTİRMEZ.
pivot_table.refresh_data_on_opening_file = False

# CalculateData(), BU pivot tablosunun görüntüsünü (veri + stil) PivotCache'de
# zaten tutulan verilerden yeniden oluşturur. Kaynak veriler değişmediği için
# kaynağa geri dönüş yapılmaz — yalnızca önbelleğe alınmış değerler çalışma sayfası
# hücrelerine yeniden hesaplanır.
pivot_table.calculate_data()

# Çalışma kitabını diske kaydet
workbook.save("output.xlsx")
```
## Aynı PivotCache'i Paylaşan Tüm Özet Tablolarını Alma
Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerinde oturan birçok özet tablosu içerir. Bunları numaralandırmak için — örneğin toplu yenileme yapmadan önce veya paylaşılan önbellek etkisini teşhis etmek için — `PivotCache.get_pivot_tables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.
Bu aynı zamanda iki özet tablosunun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilir veya `get_pivot_tables()` tarafından döndürülen koleksiyon üzerinde yineleyerek hangi özet tablolarının bu koleksiyonda göründüğünü gözlemleyebilirsiniz.
Aşağıdaki örnek, aynı kaynak aralığında iki özet tablosu oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin özet tablolarını numaralandırır.

## Kullanımdan Kaldırılan `PivotTable.refresh_data()` Yönteminden Geçiş
Aspose.Cells for Python via .NET v26.7 sürümünden önce, bir özet tablosunu yenilemenin standart yolu her özet tablosunda ayrı ayrı `PivotTable.refresh_data()` çağırmaktı. v26.7 itibarıyla bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'ler ile değiştirilmelidir.
Tablo başına `refresh_data()` yaklaşımının gerçek dünya çalışma kitaplarında sorunlu olmasının iki nedeni vardır:
- Kaynaktan veriyi *her çağrıldığında*, kaynak değişmemiş olsa bile yeniden getirir.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok özet tablosu tek bir önbelleği paylaştığında, özet tablosu başına sürekli `refresh_data()` çağırmak aynı önbelleğin tekrar tekrar yeniden getirilmesine neden olur, bu da çok yavaştır.
Önerilen değiştirmeler şunlardır:
- **Çalışma kitabındaki TÜM özet tablolarını yenileme** → `workbook.refresh_all();` kullanın
- **Bazılarını yenileme** → tek bir önbellek için `pivot_table.pivot_cache.refresh();` kullanın. Önbellek paylaşıldığı için bu tek çağrı, o önbelleğin üzerine inşa edilmiş her özet tablosunu günceller. Zaten yenilenmiş bir önbelleğin üzerinde oturan diğer özet tabloları güvenle atlanabilir.
- **Yalnızca pivot görünümü/düzeni değişti** → kaynağa herhangi bir geri dönüş olmadan mevcut önbellekten yeniden işlemek için `pivot_table.calculate_data();` kullanın.
Aşağıdaki örnek, tek bir önbelleği paylaşan birden fazla özet tablosuna sahip çalışma kitapları için yeni ve verimli kalıbı göstermektedir.
```python
.cells as ac

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

# --- İlk pivot tablosunu (Pivot1) E3 hedef hücresine ekle ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- İKİNCİ pivot tablosunu (Pivot2) AYNI kaynak aralığa ekle ---
# Hem Pivot1 hem de Pivot2 TEK bir alttaki PivotCache'i paylaşır.
# Bu tam olarak eski tablo başına RefreshData() yaklaşımının
# verimsiz hale geldiği senaryodur: bir tabloyu yenilemek tüm paylaşılan
# önbelleği yeniden çeker, dolayısıyla N tabloyu yenilemek aynı pahalı
# çekme işlemini N kez yapar.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Kaynak verideki birkaç Miktar değerini değiştir ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- ESKİ (26.7 öncesi) kalıp — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # kaynaktan yeniden çeker, tüm önbelleği yeniler
# pivot_table2.refresh_data();  # TEKRAR yeniden çeker — önbellek zaten taze!
# Her çağrı paylaşılan önbelleği yeniden oluşturur, dolayısıyla N tablo = N gereksiz çekme.

# --- YENİ v26.7+ kalıbı: önbelleği BİR KEZ yenile, ardından gerektiğinde yeniden oluştur ---
# PivotCache.Refresh() için tek bir çağrı, değiştirilen değerleri paylaşılan
# önbelleğe çeker VE onu referans alan HER pivot tablosunun görüntüsünü yeniden hesaplar.
# Pivot1 ve Pivot2 tek bir PivotCache'i paylaştığından, bu tek çağrı her iki
# tabloyu da günceller — ikinci bir kaynak gidiş-dönüşü gerekmez.
pivot_table1.pivot_cache.refresh()

# CalculateData() yalnızca bir pivot tablosunun görüntüsünü (veri + stil)
# önbellekte zaten tutulan veriden yeniden oluşturur — kaynağa DOKUNMAZ.
# Burada Pivot2 üzerinde yalnızca API'yi göstermek için çağrıyoruz: önbellek
# bir kez yenilendikten sonra, bağımlı herhangi bir tablo kaynağa geri
# dönmeden yeniden oluşturulabilir. CalculateData()'yı yalnızca pivot
# tablosunun görünüm/düzen ayarları değiştiğinde ve önbellek güncel olduğunda
# kendi başına kullanın.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```
## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, mevcut yenileme API'lerini ve her birinin ne zaman seçileceğini özetlemektedir.
| Amaç | Önerilen API | Notlar |
|------|--------------|--------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.refresh_all()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki özet tablolarını yenileme | `Worksheet.refresh_pivot_tables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Tek bir önbelleğin kaynak verileri değişti | `pivot_table.pivot_cache.refresh()` | O paylaşılan önbellekteki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivot_table.calculate_data()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan önbellekteki tüm özet tablolarını listeleme | `pivot_cache.get_pivot_tables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Uygulamada, kullanımdan kaldırılmış tablo başına `refresh_data()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerinden kaçınır ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

{{< app/cells/assistant language="python" >}}
