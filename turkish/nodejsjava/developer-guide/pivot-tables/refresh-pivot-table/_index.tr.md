---
title: Aspose.Cells for Node.js via Java'da Özet Tabloları Yenileme
linktitle: Aspose.Cells for Node.js via Java'da Özet Tabloları Yenileme
description: Aspose.Cells for Node.js via Java'da v26.7+ pivot yenileme API'sini kullanarak özet tabloları yenilemeyi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables yöntemlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, Node.js, Java, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells, özet verilerini dört farklı kapsamda — tüm çalışma kitabından tek bir özet tablosuna kadar — yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sağlar. **Aspose.Cells for Node.js via Java v26.7** sürümünden itibaren, eski yöntem olan `PivotTable.RefreshData()` kullanımdan kaldırılmış (obsolete) olarak işaretlenmiş olup bu makalede açıklanan daha verimli ve önbellek farkındaki (cache-aware) API'lerle değiştirilmelidir.

{{% /alert %}}

## Giriş

Bir özet tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.

Dört katmanlı veri zinciri şudur:

1. **Veri Kaynağı** — ham değerlerin yaşadığı orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine kuruludur; tüm veriler burada toplanır ve toplanır (aggregate).
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Cells** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells` hücreleri.

Özellikle önemli bir kavram **paylaşılan önbellek**tir. Bir çalışma kitabındaki birden çok özet tablosu aynı kaynak aralığa başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok özet tablosu başvurabilir ve bu önbelleği yenilemek, ona bağlı olan her `PivotTable`'ı aynı anda yeniler.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`) önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında yaşayan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenebilir değildir.

{{% /alert %}}

Bu zincir nedeniyle Aspose.Cells'de iki temel yenileme yolu vardır:

- **`PivotCache.Refresh()`** — kaynaktan önbelleğe yeniden yükler VE tek bir işlemde tüm bağımlı `PivotTable`'ları yeniden hesaplar.
- **`PivotTable.CalculateData()`** — önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar; veri kaynağına geri dönmez.

Bu makaledeki tüm senaryolar çalışma sayfası hücresi kaynak verilerini kullanır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı gibi çalışır.

## Gerekli İçe Aktarmalar

Bu makaledeki tüm JavaScript örnekleri Aspose.Cells for Node.js via Java modülünü gerektirir. Pivot türleri aynı modülün parçası olan `Aspose.Cells.Pivot` namespace'inde yaşar:

- `const aspose = require('aspose.cells');`
- Veya belirli içe aktarmalar için: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme

Çalışma kitabındaki her pivot önbelleğinin ve her özet tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kaynağından yeniler ve ardından bağımlı olan her `PivotTable`'ı yeniden hesaplar. Performansın önemli olmadığı genel, tam belge yenilemeleri için önerilen yaklaşım budur.

Aşağıdaki örnek, bir Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablosu oluşturur, bazı kaynak değerleri değiştirir ve ardından her şeyi tek bir çağrıda güncel hale getirmek için `RefreshAll()` yöntemini kullanır.

```javascript
const AsposeCells = require("aspose.cells");

// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
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

// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();

// Save the workbook
workbook.save("output.xlsx");
```

## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme

Bazen yalnızca belirli bir çalışma sayfasında yaşayan özet tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğine kapsamlandırılmış `Worksheet.RefreshPivotTables()` yöntemini sağlar.

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

Tek bir özet tablosu üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, aslında neyin değiştiğine bağlıdır: altta yatan kaynak veriler mi, yoksa yalnızca özet tablosunun görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.Refresh()` Kullanın

Altta yatan kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.PivotCache.Refresh()` yöntemidir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından bu önbelleğe bağımlı olan her `PivotTable`'ı yeniden hesaplar.

{{% alert color="primary" %}}

Özet tabloları tek bir `PivotCache` örneğini paylaştığından, `PivotCache.Refresh()` çağrısı o önbellek üzerine kurulmuş **tüm** özet tablolarını yeniden hesaplar — yalnızca başvurduğunuzu değil. İki özet tablosu aynı kaynak aralığını paylaşıyorsa, bir önbelleği yenilemek her ikisini de yeniler.

{{% /alert %}}

Aşağıdaki örnek, bu paylaşılan önbellek davranışını göstermek için aynı kaynak aralığında iki özet tablosu oluşturur, bazı kaynak değerleri değiştirir ve ardından bir önbellek başvurusu üzerinden yenileme yapar.


### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın

Kaynak veriler değişmemişse, ancak yalnızca özet tablosunun görünüm veya düzen ayarları değiştirilmişse (örneğin, bir alan farklı bir alana taşınmış veya açılışta yenileme ayarı değiştirilmişse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda, `pivotTable.CalculateData()` doğru seçimdir.

Bu, gereksiz kaynak alımını önler ve birçok özet tablosu aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.

Aşağıdaki örnek, özet tablosunun kaynakla ilgisi olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `CalculateData()` yöntemini çağırır.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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

// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();

// Save the workbook to disk
workbook.save("output.xlsx");
```

## Aynı PivotCache'i Paylaşan Tüm Özet Tablolarını Alma

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerine oturan birçok özet tablosu içerir. Bunları numaralandırmak için — örneğin, toplu yenileme yapmadan önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.GetPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağımlı olan her `PivotTable`'ın koleksiyonunu döndürür.

Bu, aynı zamanda iki özet tablosunun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilir veya `GetPivotTables()` tarafından döndürülen koleksiyonu yineleyerek hangi özet tablolarının göründüğünü gözlemleyebilirsiniz.

Aşağıdaki örnek, aynı kaynak aralığında iki özet tablosu oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin özet tablolarını numaralandırır.


## Eski `PivotTable.RefreshData()` Yönteminden Geçiş

Aspose.Cells for Node.js via Java v26.7'den önce, bir özet tablosunu yenilemenin standart yolu her özet tablosunda ayrı ayrı `PivotTable.RefreshData()` çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış (obsolete)** olarak işaretlenmiş olup yukarıda açıklanan önbellek farkındaki API'lerle değiştirilmelidir.

Gerçek dünya çalışma kitaplarında tablo başına `RefreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:

- Kaynak değişmemiş olsa bile *her* çağrıldığında verileri kaynaktan yeniden alır.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok özet tablosu tek bir önbelleği paylaştığında, özet tablosu başına `RefreshData()` çağrısının tekrarlanması aynı önbelleğin sürekli olarak yeniden alınmasına neden olur; bu da çok yavaştır.

Önerilen değiştirmeler şunlardır:

- **Çalışma kitabındaki TÜM özet tablolarını yenileyin** → `workbook.refreshAll();` kullanın
- **Bazılarını yenileyin** → tek bir önbellek için `pivotTable.getPivotCache().refresh();` kullanın. Önbellek paylaşıldığından, bu tek çağrı o önbelleğin üzerine kurulmuş her özet tablosunu günceller. Zaten yenilenmiş bir önbelleğin üzerine oturan diğer özet tabloları güvenle atlanabilir.
- **Yalnızca özet tablosunun görünümü/düzeni değişti** → kaynağa herhangi bir geri dönüş olmadan mevcut önbellekten yeniden işlemek için `pivotTable.calculateData();` kullanın.

Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok özet tablosuna sahip çalışma kitapları için yeni verimli kalıbı gösterir.


## Hangi Yenileme API'sini Kullanmalıyım?

Aşağıdaki tablo mevcut yenileme API'lerini özetler ve her birinin ne zaman seçileceğini gösterir.

| Amaç | Önerilen API | Notlar |
|------|--------------|--------|
| Çalışma kitabındaki her şeyi yenileyin | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki özet tablolarını yenileyin | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasına kapsamlı. |
| Tek önbellek için kaynak veriler değişti | `pivotTable.PivotCache.Refresh()` | O paylaşılan önbellekteki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan önbellekteki tüm özet tablolarını listeleyin | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |

Uygulamada, eski tablo başına `RefreshData()` yöntemi yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak alımlarını önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.{{< app/cells/assistant language="javascript" >}}
