---
title: Aspose.Cells for Node.js via C++'da Özet Tabloları Yenileme
linktitle: Aspose.Cells for Node.js via C++'da Özet Tabloları Yenileme
description: Aspose.Cells for Node.js via C++'da v26.7+ pivot-refresh API kullanılarak özet tabloların nasıl yenileneceğini öğrenin. Bu makale, RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables yöntemlerini pratik kod örnekleriyle ele almaktadır.
keywords: Aspose.Cells, Node.js via C++, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tüm çalışma kitabından tek bir özet tablosuna kadar dört farklı kapsamda pivot verilerini yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Node.js via C++ v26.7** ile başlayarak, eski `PivotTable.RefreshData()` yöntemi kullanımdan kaldırılmış olarak işaretlenmiş olup bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.
{{% /alert %}}
## Giriş
Bir özet tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şudur:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine kuruludur; tüm verilerin toplandığı ve toplulaştırıldığı yer burasıdır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable`, *yalnızca* kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla.
4. **Cells** — `PivotTable`'ın hesaplanan değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.
Özellikle önemli bir kavram **paylaşılan önbellektir**. Çalışma kitabındaki birden çok özet tablosu aynı kaynak aralığına başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok özet tablosu başvurabilir ve bu önbelleği yenilemek, ona bağlı olan her `PivotTable`'ı aynı anda yeniler.
{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`), önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini desteklemektedir; yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenememektedir.
{{% /alert %}}
Bu zincir nedeniyle, Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotCache.Refresh()`** — kaynak → önbellek verilerini yeniden yükler VE tüm bağımlı `PivotTable`'ları tek bir işlemde yeniden hesaplar.
- **`PivotTable.CalculateData()`** — zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görünümünü yeniden hesaplar; veri kaynağına geri dönüş yapmaz.
Bu makaledeki tüm senaryolarda çalışma sayfası hücre kaynak verileri kullanılmaktadır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı şekilde davranır.
## Gerekli İçe Aktarmalar
Bu makaledeki tüm JavaScript örnekleri, Aspose.Cells for Node.js via C++ modülünün yüklendiğini ve pivot türlerinin `Aspose.Cells.Pivot` ad alanında bulunduğunu varsayar. Tipik bir kurulum şudur:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (veya `AsposeCells.Pivot.PivotFieldType` üzerinden erişim)
## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme
Çalışma kitabındaki her pivot önbelleğinin ve her özet tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır; her `PivotCache`'i kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Bu, performansın kritik olmadığı genel, tam belge yenilemeleri için önerilen yaklaşımdır.
Aşağıdaki örnek bir Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablosu ekler, bazı kaynak değerleri değiştirir ve ardından her şeyi tek bir çağrıyla güncellemek için `RefreshAll()` yöntemini kullanır.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// A1:C1 hücrelerine başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// A2:C9 hücrelerine veri satırlarını yaz (2020 ve 2021 yılları arasında 8 satır meyve verisi)
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot alanlarını ata: Fruit Satırlar'a, Year Sütunlar'a, Amount Veri'ye
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Değişiklikleri simüle etmek için kaynak verideki birkaç Amount değerini değiştir
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Çalışma kitabındaki her pivot tablosunu / pivot önbelleğini yenile
workbook.refreshAll();

// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```
## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekebilir; örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmamalıdır. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.RefreshPivotTables()` yöntemini sağlar.
Bu, `Workbook.RefreshAll()` yönteminden daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki özet tabloları yenilenir, diğer çalışma sayfalarındaki özet tablolarına dokunulmaz.
Aşağıdaki örnek aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir özet tablosu ekler, bazı kaynak değerleri değiştirir ve ardından yalnızca o çalışma sayfasındaki özet tablolarını yeniler.
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
## Tek Bir Özet Tablosunu Yenileme
Tek bir özet tablosu üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca özet tablosunun kendi görünüm/düzen ayarları mı.
### Kaynak Veri Değişti — `PivotCache.Refresh()` Kullanın
Temel kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.PivotCache.Refresh()` yöntemidir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı olan her `PivotTable`'ı yeniden hesaplar.
{{% alert color="primary" %}}
Özet tabloları tek bir `PivotCache` örneğini paylaştığından, `PivotCache.Refresh()` çağrısı yalnızca başvurduğunuz özet tablosunu değil, **o önbelleğin üzerine kurulmuş tüm** özet tablolarını yeniden hesaplar. İki özet tablosu aynı kaynak aralığını paylaşıyorsa, bir önbelleği yenilemek her ikisini de yeniler.
{{% /alert %}}
Aşağıdaki örnek, bu paylaşılan önbellek davranışını göstermek için aynı kaynak aralığında iki özet tablosu oluşturur, bazı kaynak değerleri değiştirir ve ardından tek bir önbellek başvurusu üzerinden yenileme yapar.
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

// E3 hücresine sabitlenmiş ilk pivot tablosu "Pivot1" ekle, kaynak aralığı A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1 için alanları ata
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// E15'e sabitlenmiş ve AYNI kaynak aralığı A1:C9'u kullanan İKİNCİ bir pivot tablosu "Pivot2" ekle
// Hem Pivot1 hem Pivot2, kaynak aralığı aynı olduğu için tek bir PivotCache'i paylaşır.
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2 için aynı alanları ata
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Veri değişikliğini simüle etmek için kaynak verideki birkaç Miktar hücre değerini değiştir
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Paylaşılan PivotCache'i yenile.
// Pivot1 ve Pivot2 aynı PivotCache'i paylaştığı için, bu tek çağrı
// güncellenmiş kaynaktan HER İKİ pivot tablosunu da (veri + stil) yeniler.
pivotTable1.getPivotCache().refresh();

// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```
### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın
Kaynak veri değişmediyse ancak yalnızca özet tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir bölgeye taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutuyor; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekiyor. Bu durumda, `pivotTable.CalculateData()` doğru seçimdir.
Bu, gereksiz kaynak getirme işleminden kaçınır ve birçok özet tablosu aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.
Aşağıdaki örnek, özet tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `CalculateData()` yöntemini çağırır.
```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Meyve / Yıl / Miktar başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 8 veri satırı yaz (2-9 arası satırlar, A1:C9 kaynak aralığına uygun)
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

// Hedef hücre E3'e yerleştirilen, A1:C9'dan kaynaklanan "Pivot1" adlı bir özet tablo ekleyin
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Alanları ata: Satır için Meyve, Sütun için Yıl, Veri için Miktar
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunum amaçlı bir değişikliktir,
// bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTIRMEZ.
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData(), BU özet tablosunun görüntüsünü (veri + stil) şuradan yeniden oluşturur:
// PivotCache'te zaten tutulan veri. Kaynak veri değişmediği için,
// kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler yeniden hesaplanır
// çalışma sayfası hücrelerine.
pivotTable.calculateData();

// Çalışma kitabını diske kaydet
workbook.save("output.xlsx");
```
## Aynı PivotCache'i Paylaşan Tüm Özet Tablolarını Alma
Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerine kurulmuş birçok özet tablosu içerir. Bunları numaralandırmak için — örneğin, toplu yenileme yapmadan önce veya paylaşılan önbellek etkisini teşhis etmek için — `PivotCache.GetPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı olan her `PivotTable`'ın koleksiyonunu döndürür.
Bu, aynı zamanda iki özet tablosunun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilir veya `GetPivotTables()` tarafından döndürülen koleksiyonu yineleyip hangi özet tablolarının onda göründüğünü gözlemleyebilirsiniz.
Aşağıdaki örnek, aynı kaynak aralığında iki özet tablosu oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin özet tablolarını numaralandırır.

## Kullanımdan Kaldırılan `PivotTable.RefreshData()` Yönteminden Geçiş
Aspose.Cells for Node.js via C++ v26.7'den önce, bir özet tablosunu yenilemenin standart yolu her özet tablosunda ayrı ayrı `PivotTable.RefreshData()` çağırmaktı. v26.7 itibarıyla bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiş olup yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `RefreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Kaynaktan verileri *her* çağrıldığında, kaynak değişmemiş olsa bile yeniden getirir.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok özet tablosu tek bir önbelleği paylaştığında, özet tablosu başına tekrar tekrar `RefreshData()` çağırmak aynı önbelleğin sürekli olarak yeniden getirilmesine neden olur ve bu çok yavaştır.
Önerilen değiştirmeler şunlardır:
- **Çalışma kitabındaki TÜM özet tablolarını yenileme** → `workbook.refreshAll();` kullanın
- **Bazılarını yenileme** → tek bir önbellek için `pivotTable.PivotCache.Refresh();` kullanın. Önbellek paylaşıldığından, bu tek çağrı o önbelleğin üzerine kurulmuş her özet tablosunu günceller. Zaten yenilenmiş bir önbelleğin üzerine kurulmuş diğer özet tabloları güvenle atlanabilir.
- **Yalnızca pivot görünümü/düzeni değişti** → kaynaktan herhangi bir dönüş olmadan mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData();` kullanın.
Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok özet tablosuna sahip çalışma kitapları için yeni verimli kalıbı göstermektedir.
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

// --- Hedef hücre E3'e ilk pivot tablosunu (Pivot1) ekle ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- AYNI kaynak aralığına İKİNCİ pivot tablosunu (Pivot2) ekle ---
// Pivot1 ve Pivot2, TEK bir temel PivotCache'i paylaşır.
// Bu, eski tablo başına RefreshData() yaklaşımının verimsiz hale geldiği tam olarak senaryodur:
// bir tabloyu yenilemek tüm paylaşılan önbelleği yeniden çeker,
// bu yüzden N tabloyu yenilemek aynı pahalı çekme işlemini N kez yapar.
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- Kaynak verideki birkaç Tutar değerini değiştir ---
sheet.getCells().get("C2").putValue(5000);   // Üzüm  2020
sheet.getCells().get("C5").putValue(7500);   // Kiraz 2020
sheet.getCells().get("C9").putValue(9500);   // Kiraz 2021

// --- ESKİMİŞ desen (26.7 öncesi) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // kaynaktan yeniden çeker, tüm önbelleği yeniler
// pivotTable2.RefreshData();  // TEKRAR yeniden çeker — önbellek zaten taze!
// Her çağrı paylaşılan önbelleği yeniden oluşturur, yani N tablo = N gereksiz çekme işlemi.

// --- YENİ v26.7+ deseni: önbelleği BİR KEZ yenile, sonra gerektiğinde yeniden oluştur ---
// PivotCache.Refresh() için tek bir çağrı, değiştirilmiş değerleri paylaşılan
// önbelleğe çeker VE onu referans alan HER pivot tablosunun görünümünü yeniden hesaplar.
// Pivot1 ve Pivot2 tek bir PivotCache'i paylaştığından, bu tek çağrı
// her iki tabloyu da günceller — ikinci bir kaynak gidiş-dönüşü gerekmez.
pivotTable1.getPivotCache().refresh();

// CalculateData() yalnızca bir pivot tablosunun görünümünü (veri + stil)
// önbellekte zaten tutulan verilerden yeniden oluşturur — kaynağa DOKUNMAZ.
// Burada Pivot2 üzerinde yalnızca API'yi göstermek için çağırıyoruz: önbellek
// bir kez yenilendikten sonra, bağımlı herhangi bir tablo kaynağa
// geri dönmeden yeniden oluşturulabilir. Yalnızca pivot tablosunun görünüm/düzen
// ayarları değiştiğinde ve önbellek güncel olduğunda CalculateData()'yı kendi başına kullanın.
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, mevcut yenileme API'lerini ve her birinin ne zaman seçilmesi gerektiğini özetlemektedir.
| Amaç | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki özet tablolarını yenileme | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Tek bir önbellek için kaynak veriler değişti | `pivotTable.PivotCache.Refresh()` | O paylaşılan önbellekteki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak dönüşünü atlar. |
| Paylaşılan önbellekteki tüm özet tablolarını listeleme | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Uygulamada, kullanımdan kaldırılan tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerinden kaçınır ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

{{< app/cells/assistant language="javascript" >}}
