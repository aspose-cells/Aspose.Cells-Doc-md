---
title: Aspose.Cells for Node.js via C++ ile Özet Tablolarını ve Özet Tablo Önbelleklerini Yenileyin
linktitle: Aspose.Cells for Node.js via C++ ile Özet Tablolarını ve Özet Tablo Önbelleklerini Yenileyin
description: Aspose.Cells for Node.js via C++ ile v26.7+ özet tablo yenileme API'sini kullanarak özet tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale; RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables yöntemlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, Node.js via C++, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, özet tablo verilerini çalışma kitabının tamamından tek bir özet tablosuna kadar dört farklı kapsamda yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Node.js via C++ v26.7** sürümünden itibaren, eski `PivotTable.RefreshData()` yöntemi kullanımdan kaldırılmış olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbelleği dikkate alan API'lerle değiştirilmelidir.
{{% /alert %}}

## Introduction
Bir özet tablosunu yenilemek nadiren tek bir işlemdir. Aspose.Cells, arka planda özgün kaynak verinizi çalışma sayfasında görüntülenen değerlere bağlayan katmanlı bir veri zinciri yönetir. Bu zinciri anlamak, her durumda doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şöyledir:
1. **Veri Kaynağı** — ham değerlerin bulunduğu özgün çalışma sayfası aralıkları, veritabanı sorgusu veya birleştirme aralığı.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine kurulur; tüm veri burada toplanır ve toplulaştırılır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` veri kaynağından doğrudan okumaz; yalnızca kendi `PivotCache` öğesinden okur.
4. **Cells** — `PivotTable` nesnesinin hesaplanan değerlerini ve biçimlerini yerleştirdiği çalışma sayfasının `Cells` öğesi.

{{% alert color="primary" %}}
`PivotCache.SourceType` (`PivotTableSourceType` enum türü), önbellek verisinin nereden geldiğini belirtir. v26.7 sürümünden itibaren `PivotCache.refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini, yani çalışma sayfası aralıklarında bulunan verileri destekler. Harici kaynaklar (veritabanları, harici bağlantılar vb.) önbellek API'si üzerinden henüz yenilenemez.
Bu zincir nedeniyle Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotTable.calculateData()`** — zaten önbelleğe alınmış veriden tek bir `PivotTable` nesnesinin görünümünü yeniden hesaplar ve veri kaynağına geri dönmez.
`PivotCache.refresh()` ise kaynak veriyi önbelleğe yeniden okuyarak bu önbelleğe bağlı özet tabloları günceller. Bu makaledeki tüm senaryolar çalışma sayfası hücrelerinden gelen kaynak verileri kullanır; bu nedenle kaynak türü `Sheet` olur ve yenileme işlemleri aşağıda açıklandığı gibi davranır.
{{% /alert %}}

## Quick Start
Çalışma kitabındaki tüm özet tablolarını yenilemek için gereken en kısa kod tek bir çağrıdır:

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Bu makaledeki diğer bölümler, daha dar kapsamlı API'lerden hangisinin seçilmesi gerektiğini açıklar.

## Required Imports
Bu makaledeki tüm JavaScript örneklerinde Aspose.Cells for Node.js via C++ modülünün yüklenmiş olduğu ve özet tablo türlerinin `Aspose.Cells.Pivot` namespace içinde bulunduğu varsayılır. Tipik kurulum şöyledir:
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;` (veya `AsposeCells.Pivot.PivotFieldType` üzerinden erişin)

## Refresh All Pivot Tables in the Workbook
Çalışma kitabındaki tüm önbelleklerin ve özet tabloların en güncel kaynak verileri yansıtmasını sağlamak istediğinizde, en basit ve kapsamlı API `Workbook.refreshAll()` yöntemidir. Tek çağrı tüm çalışma kitabını kapsar; her `PivotCache` öğesini kaynağından yeniler ve ardından bunlara bağlı her `PivotTable` öğesini yeniden hesaplar. Performans bir sorun değilse ve belgenin tamamını kapsayan genel bir yenileme yapılacaksa önerilen yaklaşım budur.
Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablosu ekler, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek çağrıda güncellemek için `refreshAll()` yöntemini kullanır.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
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

## Refresh All Pivot Tables on a Single Worksheet
Bazen yalnızca belirli bir çalışma sayfasındaki özet tablolarını yenilemeniz gerekir. Örneğin, başka çalışma sayfalarındaki özet tablolarının ilişkisiz olduğu biliniyor ve bunlara dokunulmamalıysa bu yöntem kullanılabilir. Bu durumda Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı `Worksheet.refreshPivotTables()` yöntemini sunar.

```javascript
const AsposeCells = require("aspose.cells.node");
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

## Refresh a Single Pivot Table
Tek bir özet tablosu üzerinde ayrıntılı denetim sağlamak istediğinizde, önbellek tabanlı API size iki seçenek sunar. Seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca özet tablosunun kendi görünüm veya düzen ayarları mı?

### Source Data Changed — Use `PivotCache.refresh()`
Temel kaynak verisi değiştiyse doğru giriş noktası `pivotTable.PivotCache.refresh()` yöntemidir. Bu çağrı, kaynak veriyi önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable` öğesini yeniden hesaplar.

### Only View/Layout Changed — Use `calculateData()`
Kaynak veri değişmemiş, yalnızca özet tablosunun görünüm veya düzen ayarları değiştirilmişse (örneğin bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı açılıp kapatıldıysa), veri kaynağına geri dönmenize gerek yoktur. Önbellek zaten doğru verileri içerir; yalnızca görüntülenen `PivotTable` öğesinin yeniden hesaplanması gerekir. Bu durumda doğru seçim `pivotTable.calculateData()` yöntemidir.
Aşağıdaki örnek, özet tablosunun kaynakla ilgili olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden hesaplamak üzere `calculateData()` yöntemini çağırır.

```javascript
const AsposeCells = require("aspose.cells.node");
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
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Bir çalışma kitabında çoğu zaman tek bir paylaşılan önbelleğin üzerinde yer alan çok sayıda özet tablosu bulunur. Bunları listelemek için — örneğin toplu yenileme yapmadan önce veya paylaşılan önbelleğin etkisini teşhis etmek amacıyla — `PivotCache.getPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable` öğesinin koleksiyonunu döndürür.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Aspose.Cells for Node.js via C++ v26.7 sürümünden önce, bir özet tablosunu yenilemenin standart yolu, her özet tablosunda ayrı ayrı `PivotTable.RefreshData()` çağırmaktı. v26.7 sürümünde bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiştir ve yukarıda açıklanan, önbelleği dikkate alan API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `RefreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Her çağrıldığında, kaynak değişmemiş olsa bile, veriyi kaynaktan *her seferinde* yeniden alır; paylaşılan önbelleklerde aynı kaynak veri alımını tekrarlar.
Önerilen değiştirici, bir kez `PivotCache.refresh()` çağrılması ve ardından her özet tablosu için `calculateData()` çağrılmasıdır.
Aşağıdaki örnek, tek bir önbelleği paylaşan çok sayıda özet tablosu içeren çalışma kitapları için yeni ve verimli kalıbı gösterir.

## Which Refresh API Should I Use?
Aşağıdaki tabloda, kullanılabilir yenileme API'leri ve her birinin ne zaman seçilmesi gerektiği özetlenmiştir.
| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenile | `Workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir çalışma sayfasındaki özet tablolarını yenile | `Worksheet.refreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Tek bir önbelleğin kaynak verisi değişti | `pivotTable.PivotCache.refresh()` | Paylaşılan önbellek üzerindeki tüm özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynak veri erişimini önler. |
| Paylaşılan önbellekteki tüm özet tablolarını listele | `pivotCache.getPivotTables()` | Toplu yenilemeden önce listelemek için kullanın. |
Uygulamada, kullanımdan kaldırılmış tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bu API'ler paylaşılan önbellekleri dikkate alır, gereksiz kaynak veri alımını önler ve yenileme gereksiniminizi karşılayan en dar kapsamı seçmenize olanak tanır.

## Common Pitfalls
- **Kaydetmeden önce yenilemeyi unutmak.** Bir özet tablosu, hesaplanan değerlerini çalışma sayfasına yalnızca veri zinciri yenilendiğinde yazar. Kaynak hücreleri değiştirirseniz, `Workbook.save()` çağrısından önce `PivotCache.refresh()` (veya `Workbook.refreshAll()`) yöntemini çağırın; aksi halde kaydedilen dosya hâlâ eski toplulaştırılmış değerleri içerir.
- **Her tablo için kullanımdan kaldırılmış `RefreshData()` çağırmak.** v26.7 sürümünde `PivotTable.RefreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrıda kaynağı yeniden alır. Bir önbelleği paylaşan çok sayıda özet tablosu olduğunda bu, N gereksiz kaynak alma işlemi anlamına gelir. Bunu tek bir `PivotCache.refresh()` çağrısı ve ardından her tablo için `calculateData()` çağrısıyla değiştirin.
- **Yalnızca düzen değiştiğinde yenilemek.** Özet tablosunun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirip kaynak verilere dokunmadıysanız, `PivotCache.refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden hesaplamak için `pivotTable.calculateData()` çağırın.
- **Harici kaynaklar `PivotCache.refresh()` tarafından desteklenmiyor.** Özet tablosunun kaynağı harici bir bağlantıdan geliyorsa (veritabanı, OLAP küpü vb.), v26.7 sürümünde `PivotCache.refresh()` bunu yenileyemez; yöntem şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Harici kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="nodejs-cpp" >}}