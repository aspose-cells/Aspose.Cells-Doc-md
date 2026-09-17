---
title: Aspose.Cells for Node.js via Java'da Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
linktitle: Aspose.Cells for Node.js via Java'da Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
description: v26.7+ pivot yenileme API'sini kullanarak Aspose.Cells for Node.js via Java'da pivot tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale, pratik kod örnekleriyle RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables konularını ele almaktadır.
keywords: Aspose.Cells, Node.js, Java, pivot tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tüm çalışma kitabından tek bir pivot tablosuna kadar dört farklı kapsamda pivot verilerini yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Node.js via Java v26.7** ile birlikte, eski yöntem olan `PivotTable.RefreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.
{{% /alert %}}

## Giriş
Bir pivot tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şudur:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her pivot tablosu bir `PivotCache` üzerine inşa edilir; tüm veriler burada toplanır ve toplulaştırılır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` *yalnızca* kendi `PivotCache`'inden okur, asla doğrudan veri kaynağından okumaz.
4. **Cells** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells`'i.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`), önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) önbellek API'si aracılığıyla henüz yenilenemez.
{{% /alert %}}

Bu zincir nedeniyle, Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotTable.CalculateData()`** — veri kaynağına geri dönüş olmadan, önceden önbelleğe alınmış verilerden tek bir `PivotTable`'ın görünümünü yeniden hesaplar.
Bu makaledeki tüm senaryolar çalışma sayfası hücresi kaynak verilerini kullanır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı şekilde davranır.

## Hızlı Başlangıç
Çalışma kitabındaki tüm pivot'ları yenileyen en kısa olası koda ihtiyacınız varsa, tek bir çağrı yeterlidir:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Bu makaledeki diğer her şey, bunun yerine daha dar kapsamlı bir API'nin ne zaman seçileceğini açıklar.

## Gerekli İçe Aktarmalar
- `const aspose = require('aspose.cells');`
- Veya belirli içe aktarmalar için: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Çalışma Kitabındaki Tüm Pivot Tablolarını Yenileme
Çalışma kitabındaki her pivot önbelleğinin ve her pivot tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()`'dur. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Bu, performansın sorun olmadığı genel, tam belge yenilemeleri için önerilen yaklaşımdır.
Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığıyla bir çalışma kitabı oluşturur, bir pivot tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncellemek için `RefreshAll()`'ı kullanır.

```javascript
const AsposeCells = require("aspose.cells");
// Yeni bir çalışma kitabı oluştur
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
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
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Özet tablo alanlarını ata: Satırlar'a Fruit, Sütunlar'a Year, Veri'ye Amount
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Amount değerini değiştir
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Çalışma kitabındaki tüm özet tabloları / özet tablo önbelleğini yenile
workbook.refreshAll();
// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```

## Tek Bir Çalışma Sayfasındaki Tüm Pivot Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan pivot tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki pivot tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmamalıdır. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle kapsamlı `Worksheet.RefreshPivotTables()`'ı sağlar.

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
Tek bir pivot tablosu üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak verileri mi, yoksa yalnızca pivot tablosunun görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.Refresh()` Kullanın
Temel kaynak verileri değiştiyse, doğru giriş noktası `pivotTable.PivotCache.Refresh()`'tır. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından bu önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın
Kaynak verileri değişmediyse, ancak yalnızca pivot tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönüş gerekmez. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda `pivotTable.CalculateData()` doğru seçimdir.
Aşağıdaki örnek, pivot tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından onu mevcut önbellekten yeniden işlemek için `CalculateData()`'yı çağırır.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Meyve / Yıl / Tutar başlık satırını yaz
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
// Hedef hücre E3'e yerleştirilen, A1:C9'dan kaynaklanan "Pivot1" adlı bir pivot tablo ekle
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Alanları ata: Satır'a Meyve, Sütun'a Yıl, Veri'ye Tutar
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Bir görünüm/düzen özelliğini değiştir — bu sadece sunum amaçlı bir değişikliktir,
// bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTIRMEZ.
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() BU pivot tablosunun görüntüsünü (veri + stil) şuradan yeniden oluşturur:
// PivotCache'te zaten tutulan veri. Kaynak veri değişmediği için,
// kaynağa gidiş-dönüş gerçekleştirilmez — yalnızca önbelleğe alınmış değerler yeniden hesaplanır
// çalışma sayfası hücrelerine.
pivotTable.calculateData();
// Çalışma kitabını diske kaydet
workbook.save("output.xlsx");
```

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerinde oturan birçok pivot tablosu içerir. Bunları numaralandırmak için — örneğin, toplu bir yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini teşhis etmek için — `PivotCache.GetPivotTables()`'ı kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

## Kullanımdan Kaldırılan `PivotTable.RefreshData()`'dan Geçiş
Aspose.Cells for Node.js via Java v26.7'den önce, bir pivot tablosunu yenilemenin standart yolu her pivot tablosunda ayrı ayrı `PivotTable.RefreshData()`'yı çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `RefreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Kaynak değişmemiş olsa bile, her çağrıldığında verileri kaynaktan yeniden alır.
Önerilen değiştirmeler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok pivot tablosu olan çalışma kitapları için yeni verimli kalıbı gösterir.

## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, kullanılabilir yenileme API'lerini ve her birinin ne zaman seçileceğini özetlemektedir.
| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki pivot tablolarını yenileme | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla kapsamlı. |
| Bir önbellek için kaynak veriler değişti | `pivotTable.PivotCache.Refresh()` | Bu paylaşılan önbellekteki TÜM pivot tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan bir önbellekteki tüm pivot tablolarını listeleme | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Uygulamada, kullanımdan kaldırılan tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak alımlarını önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

## Yaygın Tuzaklar
- **Kaydetmeden önce yenilemeyi unutmak.** Bir pivot tablosu, işlenmiş değerlerini çalışma sayfasına yalnızca veri zinciri yenilendiğinde yazar. Kaynak hücreleri değiştirirseniz, `Workbook.save()`'dan önce `PivotCache.Refresh()`'i (veya `Workbook.RefreshAll()`'ı) çağırın, aksi takdirde kaydedilen dosya hâlâ eski toplulaştırılmış değerleri içerir.
- **Tablo başına kullanımdan kaldırılan `RefreshData()`'yı çağırmak.** v26.7'de `PivotTable.RefreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrı için kaynağı yeniden alır. Bir önbelleği paylaşan birden çok pivot tablosuyla bu, N gereksiz kaynak alımı anlamına gelir. Bunu, tablo başına `CalculateData()` ile takip edilen tek bir `PivotCache.Refresh()` ile değiştirin.
- **Yalnızca düzen değiştiğinde yenilemek.** Kaynak verilere dokunmadan yalnızca bir pivot tablosunun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirdiyseniz, `PivotCache.Refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData()`'yı çağırın.
- **`PivotCache.Refresh()` tarafından desteklenmeyen harici kaynak.** Pivot tablosunun kaynağı harici bir bağlantıdan (veritabanı, OLAP küpü vb.) geliyorsa, `PivotCache.Refresh()` onu v26.7'de yenileyemez — şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Harici kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="nodejs-java" >}}