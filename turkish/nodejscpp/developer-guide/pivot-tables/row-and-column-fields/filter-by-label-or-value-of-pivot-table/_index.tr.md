---
title: Pivot Tablolarını Etikete veya Değere Göre Filtreleme
linktitle: Pivot Tablolarını Etikete veya Değere Göre Filtreleme
description: Aspose.Cells for Node.js via C++, kapsamlı pivot tablo filtreleme yeteneklerini destekler. Bu makale, pivot tablo verilerini etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri kullanarak ve pivot öğelerini gizleyerek veya görünür kılarak nasıl filtreleyeceğinizi açıklar.
keywords: Aspose.Cells, Node.js via C++ kitaplığı, elektronik tablo, pivot tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, pivot öğesi, pivot öğesini gizle
type: docs
weight: 10
url: /tr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, pivot tabloda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde tarih filtrelerini kullanabilir, toplanan sayılara karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtrelerini kullanabilir veya `IsHidden` özelliğini kullanarak bireysel pivot öğelerini manuel olarak gizleyip görünür kılabilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıfları üzerindeki özel API'ler aracılığıyla kullanıma sunulur.

{{% /alert %}}

## **Giriş**

Pivot tablolar güçlü analitik araçlardır, ancak ham özetler genellikle sunmanız gereken bilgilerden çok daha fazlasını içerir. Filtreleme, bir pivot tablosunu belirli bir rapor için önemli olan satırlara, sütunlara veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for Node.js via C++, Microsoft Excel'de bulunan filtreleme yeteneklerini yansıtır ve rapor oluşturmanın tamamen otomatikleştirilebilmesi için bunları programatik olarak sunar.

Bu makalede aşağıdaki filtreleme stratejileri ele alınmıştır:

1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boşluklar) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplanan değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralanmış yalnızca en yüksek veya en düşük N öğeyi gösterir.
5. **Pivot Öğelerini Gizleme / Görünür Kılma** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.

Her yaklaşım, `PivotField` sınıfında farklı bir yöntem veya `PivotItem` sınıfında bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için pivot tablo üzerinde `refreshData()` ve `calculateData()` çağırmanız gerekir.

## **Etiket Filtresi**

Bir etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı kritere uyan ürünleri görüntülemek istediğinizde kullanışlıdır.

Aspose.Cells, etiket filtrelemeyi `PivotField.filterByLabel(PivotFilterType, string)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzeri değerler içerir. İkinci bağımsız değişken, karşılaştırma için kullanılan etiket dizesini sağlar.

Aşağıdaki örnek, mevcut bir pivot tablo içeren bir çalışma kitabını yükler, yalnızca başlıkları belirli bir ön ekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, pivot tablosunu yeniler ve sonucu kaydeder.

```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Mevcut çalışma kitabını pivot tablo içeren olarak yükle
let workbook = new AsposeCells.Workbook(fileName);

// Çalışma sayfasına dizine göre eriş (ilk çalışma sayfası)
let worksheet = workbook.getWorksheets().get(0);

// Pivot tabloya dizine göre eriş
let pivotTable = worksheet.getPivotTables().get(0);

// İlk satır PivotField'ı al
let rowField = pivotTable.getRowFields().get(0);

// Etiket filtresini uygula — yalnızca etiketleri sağlanan ön ek ile başlayan satır öğelerini göster
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Filtrenin etkili olması için pivot tablo verilerini yenile ve yeniden hesapla
pivotTable.getPivotCache().refresh();

// Çalışma kitabını diske geri kaydet
workbook.save(fileName);
```

## **Tarih Filtresi**

Tarih filtreleri, bir pivot tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı kriterlere göre daraltmanıza olanak tanır. Bunlar, yalnızca tarih-saat bilgilerini depolayan alanlara karşı çalışan özel filtrelerdir.

{{% alert color="primary" %}}

Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alan sayılar veya metin gibi başka veri türleri içeriyorsa, tarih filtresi beklenen sonucu üretmez. Filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.

{{% /alert %}}

Aspose.Cells, tarih filtrelemeyi `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak, bir veya iki `DateTime` değeri geçirirsiniz (`Between` için başlangıç ve bitiş tarihlerini geçirirsiniz).

Aşağıdaki örnek, satır alanında bir tarih alanı bulunan pivot tablolu bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}

// Pivot tablosunu içeren mevcut çalışma kitabını yükle
const workbook = new AsposeCells.Workbook(inputPath);

// Pivot tablosunu barındıran çalışma sayfasına eriş (dizine göre)
const worksheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizine göre eriş
const pivotTable = worksheet.getPivotTables().get(0);

// Satır alanından tarih PivotField'ını al
// (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde çalışır)
const dateField = pivotTable.getRowFields().get(0);

// Between filtresi için tarih kriterini tanımla
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// Pivot alanına tarih filtresini uygula
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Filtrenin etkili olması için pivot tablosunu yenile ve yeniden hesapla
pivotTable.getPivotCache().refresh();

// Çalışma kitabını kaydet
workbook.save(outputPath);
```

## **Değer Filtresi**

Değer filtreleri, bir pivot tablosunun veri alanında hesapladığı toplanan değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değerle karşılaştırır. Tipik kullanım durumları arasında yalnızca satış toplamı bir hedef miktarı aşan ürünleri veya işlem sayısı bir aralıkta olan bölgeleri göstermek yer alır.

Aspose.Cells, değer filtrelemeyi `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` yöntemi aracılığıyla sunar. `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. `valueField` parametresi, hangi veri alanının değerlendirilmesi gerektiğini belirtir ve son bağımsız değişken(ler) eşik değer(ler)i sağlar.

Aşağıdaki örnek, pivot tablolu bir çalışma kitabını yükler, yalnızca toplanan satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```javascript
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```

## **İlk 10 Filtresi**

İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan özel bir değer filtresi biçimidir. Genellikle "gelire göre ilk 10 ürün" veya "satış sayısına göre en düşük 5 bölge" gibi sıralama raporları için kullanılır.

{{% alert color="primary" %}}

İlk 10 filtresi yalnızca pivot tablosunun veri alanında bir veya daha fazla değer pivot alanı olduğunda etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplanan bir ölçü yoktur ve filtre uygulanamaz.

{{% /alert %}}

Aspose.Cells, ilk 10 filtrelemeyi `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` yöntemi aracılığıyla sunar. `itemCount` parametresi kaç öğenin tutulacağını tanımlar, `isTop` en yüksek öğelerin (true) mi yoksa en düşük öğelerin (false) mi tutulacağını belirtir, `valueField` sıralama için kullanılan veri alanına başvurur ve `filterType` değerin nasıl hesaplanacağını kontrol eder (genellikle `Sum`, ancak `Count` ve `Percent` da kullanılabilir).

Aşağıdaki örnek, bir değer alanı içeren pivot tablolu bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için bir ilk 10 filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```javascript
const AsposeCells = require("aspose.cells");

// Pivot tablosunu içeren mevcut çalışma kitabını yükle
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// Pivot tablosunu tutan çalışma sayfasına eriş (indeks 0)
const worksheet = workbook.getWorksheets().get(0);

// Pivot tablosuna indeks ile eriş
const pivotTable = worksheet.getPivotTables().get(0);

// Veri alanında en az bir değer PivotField olduğunu doğrula
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);

// Hedef satır PivotField'ını al (Top 10 uygulamak istediğimiz alan)
const rowField = pivotTable.getRowFields().get(0);

// İlk (ve tek) veri alanı indeks 0'da; Top 10 buna göre sıralar.
const valueFieldIndex = 0;

// Satır alanına Top 10 filtresini uygula:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (en üst N; false en alt N anlamına gelir)
//   - valueFieldIndex = öğeleri sıralamak için kullanılan veri alanının indeksi
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Pivot tablo verilerini yenile ve filtrenin etkili olması için yeniden hesapla
pivotTable.getPivotTableCache().refresh();

// Çalışma kitabını kaydet
workbook.save(outputPath);
```

## **Pivot Öğelerini Gizleyerek veya Görünür Kılarak Filtreleme**

Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir pivot öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField` öğesinin `PivotItems` koleksiyonunda yineleme yaparak ve `IsHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `IsHidden = true` ayarı, öğeyi pivot tablosundan gizler; `IsHidden = false` ayarı ise onu görünür kılar ve tekrar görünür hale getirir.

Bu yaklaşım, filtreleme kuralı düzensiz veya öğeye özgü olduğunda, örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlerken kullanışlıdır. Aşağıdaki örnek bir pivot tablosunu yükler, ada göre belirli bir öğeyi gizler, nasıl görünür kılınacağını gösterir, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```javascript
const AsposeCells = require("aspose.cells");

// Bir pivot tablosu içeren mevcut bir çalışma kitabını yükle
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Pivot tablosunu içeren ilk çalışma sayfasına eriş
const sheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizin ile eriş (sayfadaki ilk pivot tablosu)
const pivotTable = sheet.getPivotTables().get(0);

// Hedef PivotField'ı al (öğelerini gizleyeceğimiz/göstereceğimiz ilk satır etiket alanı)
const pivotField = pivotTable.getRowFields().get(0);

// Seçilen PivotField'ın PivotItems koleksiyonu üzerinde yineleme yap
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // Belirli bir ad/kriterle eşleşen pivot öğelerini gizle
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // Gizlemeyi kaldırmayı göster: daha önce gizlenmiş bir pivot öğesini yeniden göster
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// Değişikliklerin etkili olması için pivot tablosunu yenile ve yeniden hesapla
pivotTable.getPivotCache().refreshData();

// Çalışma kitabını kaydet — gizli öğeler alttaki verilerde kalır
// ancak görüntülenen pivot tablosu çıktısından hariç tutulur
workbook.save("output_pivot_filtered.xlsx");
```

## **Özet**

Aspose.Cells for Node.js via C++, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir pivot tablo filtreleme yetenekleri seti sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsar, ilk 10 filtresi ise sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.IsHidden` özelliği esnek, öğe düzeyinde bir geri dönüş seçeneği sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas şekilde hedeflenmiş pivot tablo raporları oluşturmanıza olanak tanır.
javascript
```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Mevcut çalışma kitabını pivot tablo içeren olarak yükle
let workbook = new AsposeCells.Workbook(fileName);

// Çalışma sayfasına dizine göre eriş (ilk çalışma sayfası)
let worksheet = workbook.getWorksheets().get(0);

// Pivot tabloya dizine göre eriş
let pivotTable = worksheet.getPivotTables().get(0);

// İlk satır PivotField'ı al
let rowField = pivotTable.getRowFields().get(0);

// Etiket filtresini uygula — yalnızca etiketleri sağlanan ön ek ile başlayan satır öğelerini göster
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Filtrenin etkili olması için pivot tablo verilerini yenile ve yeniden hesapla
pivotTable.getPivotCache().refresh();

// Çalışma kitabını diske geri kaydet
workbook.save(fileName);javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}

// Pivot tablosunu içeren mevcut çalışma kitabını yükle
const workbook = new AsposeCells.Workbook(inputPath);

// Pivot tablosunu barındıran çalışma sayfasına eriş (dizine göre)
const worksheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizine göre eriş
const pivotTable = worksheet.getPivotTables().get(0);

// Satır alanından tarih PivotField'ını al
// (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde çalışır)
const dateField = pivotTable.getRowFields().get(0);

// Between filtresi için tarih kriterini tanımla
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// Pivot alanına tarih filtresini uygula
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Filtrenin etkili olması için pivot tablosunu yenile ve yeniden hesapla
pivotTable.getPivotCache().refresh();

// Çalışma kitabını kaydet
workbook.save(outputPath);javascript
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");javascript
const AsposeCells = require("aspose.cells");

// Pivot tablosunu içeren mevcut çalışma kitabını yükle
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// Pivot tablosunu tutan çalışma sayfasına eriş (indeks 0)
const worksheet = workbook.getWorksheets().get(0);

// Pivot tablosuna indeks ile eriş
const pivotTable = worksheet.getPivotTables().get(0);

// Veri alanında en az bir değer PivotField olduğunu doğrula
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);

// Hedef satır PivotField'ını al (Top 10 uygulamak istediğimiz alan)
const rowField = pivotTable.getRowFields().get(0);

// İlk (ve tek) veri alanı indeks 0'da; Top 10 buna göre sıralar.
const valueFieldIndex = 0;

// Satır alanına Top 10 filtresini uygula:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (en üst N; false en alt N anlamına gelir)
//   - valueFieldIndex = öğeleri sıralamak için kullanılan veri alanının indeksi
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Pivot tablo verilerini yenile ve filtrenin etkili olması için yeniden hesapla
pivotTable.getPivotTableCache().refresh();

// Çalışma kitabını kaydet
workbook.save(outputPath);javascript
const AsposeCells = require("aspose.cells");

// Bir pivot tablosu içeren mevcut bir çalışma kitabını yükle
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// Pivot tablosunu içeren ilk çalışma sayfasına eriş
const sheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizin ile eriş (sayfadaki ilk pivot tablosu)
const pivotTable = sheet.getPivotTables().get(0);

// Hedef PivotField'ı al (öğelerini gizleyeceğimiz/göstereceğimiz ilk satır etiket alanı)
const pivotField = pivotTable.getRowFields().get(0);

// Seçilen PivotField'ın PivotItems koleksiyonu üzerinde yineleme yap
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // Belirli bir ad/kriterle eşleşen pivot öğelerini gizle
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // Gizlemeyi kaldırmayı göster: daha önce gizlenmiş bir pivot öğesini yeniden göster
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// Değişikliklerin etkili olması için pivot tablosunu yenile ve yeniden hesapla
pivotTable.getPivotCache().refreshData();

// Çalışma kitabını kaydet — gizli öğeler alttaki verilerde kalır
// ancak görüntülenen pivot tablosu çıktısından hariç tutulur
workbook.save("output_pivot_filtered.xlsx");
```

## **Özet**

Aspose.Cells for Node.js via C++, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir pivot tablo filtreleme yetenekleri seti sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsar, ilk 10 filtresi ise sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.IsHidden` özelliği esnek, öğe düzeyinde bir geri dönüş seçeneği sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas şekilde hedeflenmiş pivot tablo raporları oluşturmanıza olanak tanır.
{{< app/cells/assistant language="nodejs-cpp" >}}