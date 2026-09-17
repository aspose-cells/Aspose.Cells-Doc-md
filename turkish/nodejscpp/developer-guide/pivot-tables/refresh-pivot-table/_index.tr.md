---
title: Aspose.Cells for Node.js via C++'ta Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
linktitle: Aspose.Cells for Node.js via C++'ta Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
description: Aspose.Cells for Node.js via C++'ta v26.7+ pivot yenileme API'sini kullanarak pivot tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables konularını pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, Node.js via C++, pivot tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tüm çalışma kitabından tek bir pivot tablosuna kadar dört farklı kapsamda pivot verilerini yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sağlar. **Aspose.Cells for Node.js via C++ v26.7**'den itibaren eski `PivotTable.RefreshData()` yöntemi kullanımdan kaldırılmış olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.
{{% /alert %}}

## Giriş
Bir pivot tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şudur:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her pivot tablosu bir `PivotCache` üzerine inşa edilir; tüm veriler burada toplanır ve gruplanır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable`, yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Cells** — `PivotTable`'ın hesaplanan değerlerini ve stillerini işlediği çalışma sayfası `Cells`'i.

{{% alert color="primary" %}}
`PivotCache.SourceType` (`PivotTableSourceType` numaralandırması) önbellek verilerinin nereden geldiğini gösterir. v26.7 itibarıyla, `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini desteklemektedir — yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) önbellek API'si aracılığıyla henüz yenilenemez.
{{% /alert %}}

Bu zincir nedeniyle, Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotTable.CalculateData()`** — bir `PivotTable`'ın görüntüsünü zaten önbelleğe alınmış verilerden yeniden hesaplar, veri kaynağına geri dönüş olmaz.
Bu makaledeki tüm senaryolar çalışma sayfası hücresi kaynak verilerini kullanır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı gibi çalışır.

## Hızlı Başlangıç
Çalışma kitabındaki her pivot'u yenileyen en kısa koda ihtiyacınız varsa, tek bir çağrı yeterlidir:

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
// Pivot alanlarını ata: Satırlar için Meyve, Sütunlar için Yıl, Veri için Miktar
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Miktar değerini değiştir
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Çalışma kitabındaki tüm pivot tabloları / pivot önbelleklerini yenile
workbook.refreshAll();
// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```

Bu makaledeki diğer her şey, bunun yerine ne zaman daha dar kapsamlı bir API seçmeniz gerektiğini açıklar.

## Gerekli İçe Aktarmalar
Bu makaledeki tüm JavaScript örnekleri, Aspose.Cells for Node.js via C++ modülünün yüklendiğini ve pivot türlerinin `Aspose.Cells.Pivot` ad alanında yaşadığını varsayar. Tipik bir kurulum şudur:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (veya `AsposeCells.Pivot.PivotFieldType` aracılığıyla erişin)

## Çalışma Kitabındaki Tüm Pivot Tablolarını Yenileme
Çalışma kitabındaki her pivot önbelleğinin ve her pivot tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()`'dur. Tek bir çağrı tüm çalışma kitabını tarar — her `PivotCache`'i kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Performansın sorun olmadığı genel, tam belge yenilemeleri için önerilen yaklaşım budur.
Aşağıdaki örnek, Meyve/Yıl/Tutar kaynak aralığına sahip bir çalışma kitabı oluşturur, bir pivot tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncel hale getirmek için `RefreshAll()`'ı kullanır.

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

## Tek Bir Çalışma Sayfasındaki Tüm Pivot Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan pivot tablolarını yenilemeniz gerekebilir — örneğin, diğer çalışma sayfalarındaki pivot tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmamalıdır. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.RefreshPivotTables()` yöntemini sağlar.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Meyve / Yıl / Miktar başlık satırını yaz
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
// "Pivot1" adında, hedef hücre E3'e yerleştirilen ve A1:C9'dan kaynak alan bir pivot tablo ekle
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Alanları ata: Satır için Meyve, Sütun için Yıl, Veri için Miktar
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");
// Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunum amaçlı bir değişikliktir,
// bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını gerektirmez.
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData(), BU pivot tablonun görüntüsünü (veri + stil) PivotCache'te zaten
// tutulan verilerden yeniden oluşturur. Kaynak veriler değişmediği için,
// kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler yeniden hesaplanarak
// çalışma sayfası hücrelerine yazılır.
pivotTable.calculateData();
// Çalışma kitabını diske kaydet
workbook.save("output.xlsx");
```

## Tek Bir Pivot Tablosunu Yenileme
Tek bir pivot tablosu üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak verileri mi yoksa yalnızca pivot tablosunun görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.Refresh()` Kullanın
Temel kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.PivotCache.Refresh()`'tır. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın
Kaynak veriler değişmediyse ancak yalnızca pivot tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir bölgeye taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda, `pivotTable.CalculateData()` doğru seçimdir.
Aşağıdaki örnek, pivot tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `CalculateData()`'yı çağırır.
Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerine yerleşmiş birçok pivot tablosu içerir. Bunları numaralandırmak için — örneğin, toplu bir yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini teşhis etmek için — `PivotCache.GetPivotTables()`'ı kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

## Kullanımdan Kaldırılan `PivotTable.RefreshData()`'dan Geçiş
Aspose.Cells for Node.js via C++ v26.7'den önce, bir pivot tablosunu yenilemenin standart yolu, her pivot tablosunda ayrı ayrı `PivotTable.RefreshData()` çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `RefreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Kaynak değişmemiş olsa bile, çağrıldığında *her seferinde* verileri kaynaktan yeniden getirir.
Önerilen değiştirmeler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok pivot tablosuna sahip çalışma kitapları için yeni verimli kalıbı göstermektedir.

## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, kullanılabilir yenileme API'lerini ve her birinin ne zaman seçileceğini özetlemektedir.
| Amaç | Önerilen API | Notlar |
|------|--------------|--------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki pivot tablolarını yenileme | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Bir önbellek için kaynak veriler değişti | `pivotTable.PivotCache.Refresh()` | Paylaşılan önbellek üzerindeki TÜM pivot tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan önbellek üzerindeki tüm pivot tablolarını listeleme | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Uygulamada, kullanımdan kaldırılmış tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerinden kaçınır ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

## Yaygın Tuzaklar
- **Kaydetmeden önce yenilemeyi unutmak.** Bir pivot tablosu, işlenmiş değerlerini çalışma sayfasına yalnızca veri zinciri yenilendiğinde yazar. Kaynak hücreleri değiştirirseniz, `Workbook.save()`'dan önce `PivotCache.Refresh()` (veya `Workbook.RefreshAll()`) çağırın, aksi takdirde kaydedilen dosya hâlâ eski toplu değerleri içerir.
- **Tablo başına kullanımdan kaldırılmış `RefreshData()` çağırmak.** v26.7'de `PivotTable.RefreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrı için kaynağı yeniden getirir. Bir önbelleği paylaşan birden çok pivot tablosuyla bu, N gereksiz kaynak getirmesi anlamına gelir. Tablo başına tek bir `PivotCache.Refresh()` ve ardından `CalculateData()` ile değiştirin.
- **Yalnızca düzen değiştiğinde yenilemek.** Kaynak verilere dokunmadan yalnızca bir pivot tablosunun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirdiyseniz, `PivotCache.Refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData()`'yı çağırın.
- **`PivotCache.Refresh()` tarafından desteklenmeyen harici kaynak.** Pivot tablosunun kaynağı harici bir bağlantıdan (veritabanı, OLAP küpü vb.) geliyorsa, `PivotCache.Refresh()` onu v26.7'de yenileyemez — şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini desteklemektedir. Harici kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}