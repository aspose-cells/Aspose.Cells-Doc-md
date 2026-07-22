---
title: Aspose.Cells for Java'da Özet Tabloları Yenileme
linktitle: Aspose.Cells for Java'da Özet Tabloları Yenileme
description: Aspose.Cells for Java'da v26.7+ pivot-refresh API'sini kullanarak özet tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale, RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables API'lerini pratik kod örnekleriyle ele almaktadır.
keywords: Aspose.Cells, Java, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, dört farklı kapsamda — çalışma kitabının tamamından tek bir özet tablosuna kadar — pivot verilerini yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Java v26.7** sürümünden itibaren, eski `PivotTable.refreshData()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'ler ile değiştirilmelidir.

{{% /alert %}}

## Giriş

Bir özet tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.

Dört katmanlı veri zinciri şudur:

1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine inşa edilir; tüm veriler burada toplanır ve birleştirilir.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` verileri yalnızca kendi `PivotCache`'inden okur, asla doğrudan veri kaynağından değil.
4. **Hücreler** — `PivotTable`'ın hesaplanan değerleri ve stilleri işlediği çalışma sayfası `Cells` koleksiyonu.

Özellikle önemli bir kavram **paylaşılan önbellek**tir. Bir çalışma kitabındaki birden çok özet tablosu aynı kaynak aralığına başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok özet tablosu tarafından başvurulabilir ve bu önbelleğin yenilenmesi, ona bağlı her `PivotTable`'ı bir defada yeniler.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (`PivotTableSourceType` enum'u), önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini desteklemektedir — yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.

{{% /alert %}}

Bu zincir nedeniyle, Aspose.Cells'te iki temel yenileme yolu vardır:

- **`PivotCache.refresh()`** — tek bir işlemle kaynak → önbelleği yeniden yükler VE ona bağlı tüm `PivotTable`'ları yeniden hesaplar.
- **`PivotTable.calculateData()`** — veri kaynağına geri dönmeden, zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar.

Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynak verilerini kullanır; dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı gibi davranır.

## Gerekli İçe Aktarma Bildirimleri

Bu makaledeki tüm Java örnekleri, pivot türlerinin `com.aspose.cells.pivot` paketinde bulunması nedeniyle aşağıdaki içe aktarma bildirimleriyle başlar:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme

Çalışma kitabındaki her pivot önbelleğinin ve her özet tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refreshAll()` yöntemidir. Tek bir çağrı, çalışma kitabının tamamını dolaşır — her `PivotCache`'i kendi kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Bu, performansın kritik olmadığı genel, tam belge yenilemeleri için önerilen yaklaşımdır.

Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablosu ekler, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncellemek için `refreshAll()` yöntemini kullanır.

```java
import com.aspose.cells.*;

// Yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// A1:C1 hücrelerine başlık satırı yaz
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// A2:C9 hücrelerine veri satırları yaz (2020 ve 2021 yılları arasında 8 satır meyve verisi)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);

// Bir pivot tablo ekle: kaynak aralık "A1:C9", hedef hücre "E3", ad "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot alanlarını ata: Fruit Satırlar'a, Year Sütunlar'a, Amount Veri'ye
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Amount değerini değiştir
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Çalışma kitabındaki her pivot tabloyu / pivot önbelleğini yenile
workbook.refreshAll();

// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```

## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme

Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekebilir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.refreshPivotTables()` yöntemini sunar.

Bu yöntem `Workbook.refreshAll()` yönteminden daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki özet tabloları yenilenir, diğer çalışma sayfalarındaki özet tablolarına dokunulmaz.

Aşağıdaki örnek, aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir özet tablosu ekler, bazı kaynak değerlerini değiştirir ve ardından yalnızca o çalışma sayfasındaki özet tablolarını yeniler.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);

int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```

## Tek Bir Özet Tablosunu Yenileme

Tek bir özet tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: altta yatan kaynak veriler mi, yoksa yalnızca özet tablosunun kendi görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.refresh()` Kullanın

Altta yatan kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.getPivotCache().refresh()` yöntemidir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

{{% alert color="primary" %}}

Özet tabloları tek bir `PivotCache` örneğini paylaştığından, `PivotCache.refresh()` çağrısı yalnızca başvuruda bulunduğunuz tabloyu değil, aynı önbellek üzerine inşa edilmiş **tüm** özet tablolarını yeniden hesaplar. İki özet tablosu aynı kaynak aralığını paylaşıyorsa, bir önbelleği yenilemek her ikisini birden yeniler.

{{% /alert %}}

Aşağıdaki örnek, paylaşılan önbellek davranışını göstermek için aynı kaynak aralığı üzerinde iki özet tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından tek bir önbellek başvurusu üzerinden yenileme yapar.

```java
import com.aspose.cells.*;

// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Başlık satırını yaz: Meyve / Yıl / Miktar
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Yaklaşık 9 veri satırı yaz (üzüm / yaban mersini / kivi / kiraz, 2020-2021 arasında)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// E3 hücresine bağlı ilk pivot tablosu "Pivot1" ekle, kaynak aralığı A1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1 için alanları ata
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// E15'e bağlı İKİNCİ pivot tablosu "Pivot2" ekle, AYNI kaynak aralığı A1:C9 kullanılarak
// Pivot1 ve Pivot2, kaynak aralığı aynı olduğu için tek bir PivotCache'i paylaşır.
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2 için aynı alanları ata
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// Veri değişikliğini simüle etmek için kaynak verilerdeki birkaç Miktar hücresi değerini değiştir
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Paylaşılan PivotCache'i yenile.
// Pivot1 ve Pivot2 aynı PivotCache'i paylaştığı için bu tek çağrı
// güncellenmiş kaynaktan HER İKİ pivot tablosunu da (veri + stil) yeniler.
pivotTable1.refreshData();

// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```

### Yalnızca Görünüm/Düzen Değişti — `calculateData()` Kullanın

Kaynak veriler değişmediyse, ancak yalnızca özet tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir alana taşındıysa veya dosya açılırken yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutuyor; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekiyor. Bu durumda, `pivotTable.calculateData()` doğru seçimdir.

Bu, gereksiz kaynak getirme işlemini önler ve birçok özet tablosu aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.

Aşağıdaki örnek, özet tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculateData()` yöntemini çağırır.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Fruit / Year / Amount başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 8 veri satırı yaz (satır 2-9, kaynak aralığı A1:C9'a uyuyor)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);

// Hedef hücre E3'e yerleştirilen, A1:C9'dan beslenen "Pivot1" adlı bir pivot tablo ekle
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Alanları ata: Fruit -> Row, Year -> Column, Amount -> Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Bir görünüm/düzen özelliğini değiştir -- bu yalnızca sunuma yönelik bir değişikliktir,
// bu nedenle PivotCache.Refresh() üzerinden kaynak verilerin yeniden okunmasını GEREKTİRMEZ.
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() BU pivot tablosunun görüntüsünü (veri + stil) PivotCache'te zaten
// tutulan verilerden yeniden oluşturur. Kaynak veri değişmediği için kaynağa gidiş-dönüş
// yapılmaz -- yalnızca önbelleğe alınmış değerler çalışma sayfası hücrelerine yeniden hesaplanır.
pivotTable.calculateData();

// Çalışma kitabını diske kaydet
workbook.save("output.xlsx");
```

## Aynı PivotCache'i Paylaşan Tüm Özet Tablolarını Alma

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerinde oturan birçok özet tablosu içerir. Bunları numaralandırmak için — örneğin toplu yenileme yapmadan önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.getPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

Bu, iki özet tablosunun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilirsiniz (`==` operatörünü kullanarak) veya basitçe `getPivotTables()` tarafından döndürülen koleksiyonu yineleyerek hangi özet tablolarının orada göründüğünü gözlemleyebilirsiniz.

Aşağıdaki örnek, aynı kaynak aralığı üzerinde iki özet tablosu oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin özet tablolarını numaralandırır.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

int pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

boolean sameCache = pivotTable1.getPivotCache() == pivotTable2.getPivotCache();
System.out.println("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
System.out.println("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (PivotTable pt : sharedPivotTables)
{
    System.out.println("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Kullanımdan Kaldırılan `PivotTable.refreshData()` Yönteminden Geçiş

Aspose.Cells for Java v26.7 öncesinde, bir özet tablosunu yenilemenin standart yolu her özet tablosunda ayrı ayrı `PivotTable.refreshData()` yöntemini çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış (obsolete)** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'ler ile değiştirilmelidir.

Tablo başına `refreshData()` yaklaşımının gerçek dünya çalışma kitaplarında sorunlu olmasının iki nedeni vardır:

- Kaynak değişmemiş olsa bile, her çağrıldığında verileri kaynaktan yeniden getirir.
- Her çağrı, paylaşılan önbelleğin tamamını yeniler. Birçok özet tablosu tek bir önbelleği paylaştığında, özet tablosu başına tekrar tekrar `refreshData()` çağırmak, aynı önbelleğin tekrar tekrar yeniden getirilmesine neden olur; bu da çok yavaştır.

Önerilen değiştirmeler şunlardır:

- **Çalışma kitabındaki TÜM özet tablolarını yenileme** → `workbook.refreshAll();` kullanın
- **Bunlardan BAZILARINI yenileme** → tek bir önbellek için `pivotTable.getPivotCache().refresh();` kullanın. Önbellek paylaşıldığından, bu tek çağrı o önbelleğin üzerine inşa edilmiş her özet tablosunu günceller. Zaten yenilenmiş bir önbelleğin üzerinde oturan diğer özet tabloları güvenle atlanabilir.
- **Yalnızca pivot görünümü/düzeni değişti** → kaynak yeniden getirme olmadan mevcut önbellekten yeniden işlemek için `pivotTable.calculateData();` kullanın.

Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok özet tablosuna sahip çalışma kitapları için yeni verimli kalıbı göstermektedir.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- Kaynak verileri oluştur: Fruit / Year / Amount (başlık + 9 satır) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- İlk pivot tablosunu (Pivot1) hedef hücre E3'e ekle ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- İKİNCİ pivot tablosunu (Pivot2) AYNI kaynak aralığına ekle ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Kaynak verilerdeki birkaç Amount değerini değiştir ---
sheet.getCells().get("C2").putValue(5000);   // Üzüm  2020
sheet.getCells().get("C5").putValue(7500);   // Kiraz 2020
sheet.getCells().get("C9").putValue(9500);   // Kiraz 2021

// --- YENİ v26.7+ kalıbı: önbelleği BİR KEZ yenile, sonra gerektiğinde yeniden oluştur ---
pivotTable1.getPivotCache().refresh();

// Kaynağa dokunmadan ikinci pivot tablosunun görünümünü/düzenini yeniden oluştur
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Hangi Yenileme API'sini Kullanmalıyım?

Aşağıdaki tablo, mevcut yenileme API'lerini ve her birinin ne zaman seçilmesi gerektiğini özetlemektedir.

| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki özet tablolarını yenileme | `Worksheet.refreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Bir önbellek için kaynak veriler değişti | `pivotTable.getPivotCache().refresh()` | O paylaşılan önbellek üzerindeki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynak yeniden getirme işlemini atlar. |
| Paylaşılan önbellek üzerindeki tüm özet tablolarını listeleme | `pivotCache.getPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |

Pratikte, kullanımdan kaldırılan tablo başına `refreshData()` yöntemi yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirme işlemlerini önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

{{< app/cells/assistant language="java" >}}