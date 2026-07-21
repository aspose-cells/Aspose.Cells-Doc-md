---
title: Aspose.Cells for Node.js via C++ ile Pivot Tablolarını Yenileme
linktitle: Aspose.Cells for Node.js via C++ ile Pivot Tablolarını Yenileme
description: Aspose.Cells for Node.js via C++ ile v26.7+ pivot yenileme API'sini kullanarak pivot tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables konularını pratik kod örnekleriyle ele almaktadır.
keywords: Aspose.Cells, Node.js via C++, pivot tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, pivot verilerini dört farklı kapsamda — tüm çalışma kitabından tek bir pivot tablosuna kadar — yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Aspose.Cells for Node.js via C++ v26.7** sürümünden itibaren, eski `PivotTable.RefreshData()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiş olup bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.

{{% /alert %}}

## Giriş

Bir pivot tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri sürdürür. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.

Dört katmanlı veri zinciri şudur:

1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsü. Her pivot tablo bir `PivotCache` üzerine inşa edilir; tüm veriler burada toplanır ve birleştirilir.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından değil.
4. **Cells** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.

Özellikle önemli bir kavram **paylaşılan önbellektir**. Bir çalışma kitabındaki birden fazla pivot tablo aynı kaynak aralığına başvurduğunda, bunlar *tek* bir `PivotCache` örneğini paylaşır. Tek bir `PivotCache`'e birçok pivot tablo tarafından başvurulabilir ve o önbelleği yenilemek, ona bağlı her `PivotTable`'ı bir kerede yeniler.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenebilir değildir.

{{% /alert %}}

Bu zincir nedeniyle Aspose.Cells'de iki temel yenileme yolu vardır:

- **`PivotCache.Refresh()`** — kaynak → önbelleği yeniden yükler VE tek bir işlemde tüm bağımlı `PivotTable`'ları yeniden hesaplar.
- **`PivotTable.CalculateData()`** — veri kaynağına geri dönmeden, zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar.

Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynak verilerini kullanır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı gibi çalışır.

## Gerekli İçe Aktarmalar

Bu makaledeki tüm JavaScript örnekleri, Aspose.Cells for Node.js via C++ modülünün yüklenmiş olduğunu ve pivot türlerinin `Aspose.Cells.Pivot` namespace'inde yaşadığını varsayar. Tipik bir kurulum şöyledir:

- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (veya `AsposeCells.Pivot.PivotFieldType` üzerinden erişim)

## Çalışma Kitabındaki Tüm Pivot Tablolarını Yenileme

Çalışma kitabındaki her pivot önbelleğinin ve her pivot tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()`'dur. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kendi kaynağından yeniler ve ardından her bağımlı `PivotTable`'ı yeniden hesaplar. Bu, performansın endişe olmadığı genel, tam belge yenilemeleri için önerilen yaklaşımdır.

Aşağıdaki örnek, bir Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir pivot tablo oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncellemek için `RefreshAll()` kullanır.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// A1:C1 hücrelerine başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// A2:C9 hücrelerine veri satırlarını yaz (2020 ve 2021 yıllarına ait 8 satır meyve verisi)
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

// Özet tablo ekle: kaynak aralık "A1:C9", hedef hücre "E3", ad "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Özet tablo alanlarını ata: Satırlar için Meyve, Sütunlar için Yıl, Veri için Miktar
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Değişiklikleri simüle etmek için kaynak verideki birkaç Miktar değerini değiştir
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Çalışma kitabındaki tüm özet tabloları / özet önbelleklerini yenile
workbook.refreshAll();

// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```

## Tek Bir Çalışma Sayfasındaki Tüm Pivot Tablolarını Yenileme

Bazen yalnızca belirli bir çalışma sayfasında bulunan pivot tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki pivot tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.RefreshPivotTables()` yöntemini sunar.

Bu, `Workbook.RefreshAll()` yönteminden daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki pivot tabloları yenilenir, diğer çalışma sayfalarındaki pivot tablolarına dokunulmaz.

Aşağıdaki örnek aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir pivot tablo ekler, bazı kaynak değerlerini değiştirir ve ardından yalnızca o çalışma sayfasındaki pivot tablolarını yeniler.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

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

let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```

## Tek Bir Pivot Tablosunu Yenileme

Tek bir pivot tablosu üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca pivot tablosunun görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.Refresh()` Kullanın

Temel kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.PivotCache.Refresh()`'tir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

{{% alert color="primary" %}}

Pivot tabloları tek bir `PivotCache` örneğini paylaştığı için, `PivotCache.Refresh()` çağrısı yalnızca başvurduğunuz pivot tablosunu değil, aynı önbellek üzerine inşa edilmiş **tüm** pivot tablolarını yeniden hesaplar. Eğer iki pivot tablo aynı kaynak aralığını paylaşıyorsa, bir önbelleği yenilemek her ikisini de yeniler.

{{% /alert %}}

Aşağıdaki örnek, bu paylaşılan önbellek davranışını göstermek için aynı kaynak aralığı üzerinde iki pivot tablo oluşturur, bazı kaynak değerlerini değiştirir ve ardından tek bir önbellek başvurusu aracılığıyla yenileme yapar.

```javascript
const AsposeCells = require("aspose.cells");

// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Başlık satırını yaz: Meyve / Yıl / Miktar
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Yaklaşık 9 veri satırı yaz (üzüm / yaban mersini / kivi / kiraz, 2020-2021 arası)
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

// E3 hücresine bağlı ilk pivot tablo "Pivot1" ekle, kaynak aralığı A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1 için alanları ata
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// E15'e bağlı İKİNCİ bir pivot tablo "Pivot2" ekle, aynı A1:C9 kaynak aralığını kullanarak
// Hem Pivot1 hem Pivot2, kaynak aralık aynı olduğu için tek bir PivotCache'i paylaşır.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2 için aynı alanları ata
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Veri değişikliğini simüle etmek için kaynak verilerdeki birkaç Miktar hücresi değerini değiştir
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Paylaşılan PivotCache'i yenile.
// Pivot1 ve Pivot2 aynı PivotCache'i paylaştığı için bu tek çağrı
// güncellenmiş kaynaktan HER İKİ pivot tablosunu da (veri + stil) yeniler.
pivotTable1.getPivotCache().refresh();

// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```

### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın

Kaynak veriler değişmediyse ancak yalnızca pivot tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir alana taşındıysa veya dosya açılışında yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda `pivotTable.CalculateData()` doğru seçimdir.

Bu, gereksiz kaynak çağrısını önler ve birçok pivot tablosu aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.

Aşağıdaki örnek, pivot tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `CalculateData()` çağırır.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Fruit / Year / Amount başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 8 veri satırı yaz (2-9 satırları, A1:C9 kaynak aralığına uygun)
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

// Hedef hücre E3'e yerleştirilen, A1:C9'dan kaynaklanan "Pivot1" adlı bir pivot tablo ekle
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Alanları ata: Satır için Fruit, Sütun için Year, Veri için Amount
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunum amaçlı bir değişikliktir,
// bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını gerektirmez.
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData(), BU pivot tablosunun görüntüsünü (veri + stil) PivotCache'te zaten tutulan verilerden yeniden oluşturur.
// Kaynak veriler değişmediğinden, kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler yeniden hesaplanarak
// çalışma sayfası hücrelerine yerleştirilir.
pivotTable.calculateData();

// Çalışma kitabını diske kaydet
workbook.save("output.xlsx");
```

## Aynı PivotCache'i Paylaşan Tüm Pivot Tablolarını Alma

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerinde oturan birçok pivot tablosu içerir. Bunları numaralandırmak için — örneğin, toplu yenileme yapmadan önce veya paylaşılan önbellek etkisini teşhis etmek için — `PivotCache.GetPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

Bu, aynı zamanda iki pivot tablosunun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilir veya `GetPivotTables()` tarafından döndürülen koleksiyonu yineleyerek hangi pivot tablolarının onda göründüğünü gözlemleyebilirsiniz.

Aşağıdaki örnek, aynı kaynak aralığı üzerinde iki pivot tablo oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin pivot tablolarını numaralandırır.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## Kullanımdan Kaldırılan `PivotTable.RefreshData()`'dan Geçiş

Aspose.Cells for Aspose.Cells for Node.js via C++ v26.7'den önce, bir pivot tablosunu yenilemenin standart yolu her pivot tablosunda ayrı ayrı `PivotTable.RefreshData()` çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.

Gerçek dünya çalışma kitaplarında tablo başına `RefreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:

- Kaynak değişmemiş olsa bile *her* çağrıldığında verileri kaynaktan yeniden getirir.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok pivot tablosu tek bir önbelleği paylaştığında, pivot tablosu başına `RefreshData()`'yı tekrar tekrar çağırmak aynı önbelleğin tekrar tekrar yeniden getirilmesine neden olur, bu da çok yavaştır.

Önerilen değiştirmeler şunlardır:

- **Çalışma kitabındaki TÜM pivot tablolarını yenilemek** → `workbook.refreshAll();` kullanın
- **Bunların bir kısmını yenilemek** → tek bir önbellek için `pivotTable.PivotCache.Refresh();` kullanın. Önbellek paylaşıldığı için bu tek çağrı, o önbelleğin üzerine inşa edilmiş her pivot tablosunu günceller. Zaten yenilenmiş bir önbelleğin üzerinde oturan diğer pivot tabloları güvenle atlanabilir.
- **Yalnızca pivot görünümü/düzeni değişti** → kaynak geri çağrısı olmadan mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData();` kullanın.

Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok pivot tablosu olan çalışma kitapları için yeni verimli kalıbı gösterir.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- Kaynak veriyi oluştur: Meyve / Yıl / Tutar (başlık + 9 satır) ---
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

// --- İlk pivot tablosunu (Pivot1) E3 hedef hücresine ekle ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- İKİNCİ pivot tablosunu (Pivot2) AYNI kaynak aralığına ekle ---
// Pivot1 ve Pivot2, TEK bir temel PivotCache'i paylaşır.
// Bu, eski tablo başına RefreshData() yaklaşımının tam olarak verimsiz hale geldiği senaryodur:
// bir tabloyu yenilemek tüm paylaşılan önbelleği yeniden getirir,
// dolayısıyla N tabloyu yenilemek aynı pahalı getirme işlemini N kez yapar.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Kaynak verideki birkaç Tutar değerini değiştir ---
sheet.getCells().get("C2").putValue(5000);   // Üzüm  2020
sheet.getCells().get("C5").putValue(7500);   // Kiraz 2020
sheet.getCells().get("C9").putValue(9500);   // Kiraz 2021

// --- ESKİMİŞ örüntü (26.7 öncesi) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // kaynaktan yeniden getirir, tüm önbelleği yeniler
// pivotTable2.RefreshData();  // TEKRAR yeniden getirir — önbellek zaten taze!
// Her çağrı paylaşılan önbelleği yeniden oluşturur, dolayısıyla N tablo = N gereksiz getirme.

// --- YENİ v26.7+ örüntü: önbelleği BİR KEZ yenile, sonra gerektiğinde yeniden işle ---
// PivotCache.Refresh() için tek bir çağrı, değiştirilen değerleri paylaşılan önbelleğe çeker
// VE ona başvuran HER pivot tablosunun görüntüsünü yeniden hesaplar.
// Pivot1 ve Pivot2 tek bir PivotCache'i paylaştığından, bu tek çağrı
// her iki tabloyu da günceller — ikinci bir kaynak gidip gelme gerekmez.
pivotTable1.getPivotCache().refresh();

// CalculateData() yalnızca bir pivot tablosunun görüntüsünü (veri + stil)
// önbellekte zaten tutulan verilerden yeniden işler — kaynağa DOKUNMAZ.
// Onu burada Pivot2 üzerinde yalnızca API'yi göstermek için çağırıyoruz: önbellek
// bir kez yenilendikten sonra, bağımlı herhangi bir tablo kaynağa geri dönmeden
// yeniden işlenebilir. Yalnızca pivot tablosunun görünüm/düzen ayarları değiştiğinde
// ve önbellek güncel olduğunda CalculateData()'yı kendi başına kullanın.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Hangi Yenileme API'sini Kullanmalıyım?

Aşağıdaki tablo mevcut yenileme API'lerini özetlemekte ve her birini ne zaman seçmeniz gerektiğini göstermektedir.

| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenilemek | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki pivot tablolarını yenilemek | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Bir önbellek için kaynak veriler değişti | `pivotTable.PivotCache.Refresh()` | O paylaşılan önbellekteki TÜM pivot tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak geri çağrısını atlar. |
| Paylaşılan önbellekteki tüm pivot tablolarını listelemek | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |

Uygulamada, kullanımdan kaldırılmış tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak çağrılarını önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

{{< app/cells/assistant language="javascript" >}}