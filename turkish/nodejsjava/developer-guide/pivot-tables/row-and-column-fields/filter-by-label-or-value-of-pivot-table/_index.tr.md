---
title: Özet Tabloları Etiket veya Değere Göre Filtreleme
linktitle: Özet Tabloları Etiket veya Değere Göre Filtreleme
description: Aspose.Cells for Node.js via Java kapsamlı özet tablo filtreleme yeteneklerini destekler. Bu makale, etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri kullanarak ve özet öğelerini gizleyerek veya göstererek özet tablo verilerinin nasıl filtreleneceğini açıklar.
keywords: Aspose.Cells, Node.js via Java kütüphanesi, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet öğesi, özet öğesini gizle
type: docs
weight: 10
url: /tr/nodejs-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells, bir özet tablosunda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde tarih filtreleri kullanabilir, toplanan sayılara karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtrelerini kullanabilir ya da `IsHidden` özelliğini kullanarak tek tek özet öğelerini manuel olarak gizleyip gösterebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıfları üzerindeki özel API'ler aracılığıyla kullanıma sunulmuştur.
{{% /alert %}}
## **Giriş**
Özet tablolar güçlü analitik araçlardır, ancak ham özetler genellikle sunmanız gerekenden çok daha fazla bilgi içerir. Filtreleme, bir özet tablosunu belirli bir rapor için önemli olan satır, sütun veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for Node.js via Java, Microsoft Excel'de bulunan filtreleme yeteneklerini yansıtarak bunları programatik olarak sunar; böylece rapor oluşturma tamamen otomatikleştirilebilir.
Bu makalede ele alınan filtreleme stratejileri şunlardır:
1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boş değerler) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplanan değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralanmış yalnızca ilk veya son N öğeyi gösterir.
5. **Özet Öğelerini Gizle / Göster** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.
Her yaklaşım, `PivotField` sınıfında farklı bir yöntem veya `PivotItem` sınıfında bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tablosunda `refreshData()` ve `calculateData()` çağrısı yapmanız gerekir.
## **Etiket Filtresi**
Bir etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı ölçüte uyan ürünleri görüntülemek istediğinizde kullanışlıdır.
Aspose.Cells, etiket filtrelemeyi `PivotField.filterByLabel(PivotFilterType, string)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` gibi değerler içerir. İkinci bağımsız değişken, karşılaştırma için kullanılan etiket dizesini sağlar.
Aşağıdaki örnek, mevcut bir özet tablo içeren bir çalışma kitabını yükler, başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, özet tablosunu yeniler ve sonucu kaydeder.
```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// Mevcut çalışma kitabını, içinde bir pivot tablo bulunan şekilde yükle
let workbook = new AsposeCells.Workbook(fileName);

// Çalışma sayfasına dizin ile eriş (ilk çalışma sayfası)
let worksheet = workbook.getWorksheets().get(0);

// Pivot tabloya dizin ile eriş
let pivotTable = worksheet.getPivotTables().get(0);

// İlk satır PivotField'ını al
let rowField = pivotTable.getRowFields().get(0);

// Etiket filtresini uygula — yalnızca etiketleri sağlanan önekle başlayan satır öğelerini göster
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// Pivot tablo verilerini yenile ve yeniden hesapla, böylece filtre etkili olur
pivotTable.getPivotCache().refresh();

// Çalışma kitabını diske geri kaydet
workbook.save(fileName);
```
## **Tarih Filtresi**
Tarih filtreleri, bir özet tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı ölçütlere göre daraltmanıza olanak tanır. Bunlar, yalnızca tarih-saat bilgilerini depolayan alanlara karşı çalışan özel filtrelerdir.
{{% alert color="primary" %}}
Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alan sayılar veya metin gibi başka veri türlerini içeriyorsa, tarih filtresi beklenen sonucu üretmeyecektir. Alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun, ardından bu filtreyi uygulayın.
{{% /alert %}}
Aspose.Cells, tarih filtrelemeyi `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak bir veya iki `DateTime` değeri geçersiniz (`Between` için başlangıç ve bitiş tarihlerini geçersiniz).
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan özet tablosuna sahip bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```javascript
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}

// Pivot tablosunu içeren mevcut çalışma kitabını yükle
var workbook = new AsposeCells.Workbook(inputPath);

// Pivot tablosunu barındıran çalışma sayfasına eriş (dizine göre)
var worksheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizine göre eriş
var pivotTable = worksheet.getPivotTables().get(0);

// Satır alanından tarih PivotField'ını al
// (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde çalışır)
let dateField = pivotTable.getRowFields().get(0);

// Between filtresi için tarih kriterini tanımla
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);

// Pivot alanına tarih filtresini uygula
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// Filtrenin etkili olması için pivot tablosunu yenile ve yeniden hesapla
pivotTable.getPivotCache().refresh();

// Çalışma kitabını kaydet
workbook.save(outputPath);
```
## **Değer Filtresi**
Değer filtreleri, bir özet tablosunun veri alanında hesapladığı toplanan değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değeriyle karşılaştırır. Tipik kullanım durumları arasında yalnızca satış toplamı hedef tutarı aşan ürünleri veya işlem sayısı bir aralık içinde olan bölgeleri göstermek de yer alır.
Aspose.Cells, değer filtrelemeyi `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` yöntemi aracılığıyla sunar. `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. `valueField` parametresi hangi veri alanının değerlendirileceğini belirtir ve son bağımsız değişken(ler) eşik değerini(lerini) sağlar.
Aşağıdaki örnek, özet tablosu olan bir çalışma kitabını yükler, yalnızca toplanan satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```javascript
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);

var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);

// PivotFieldCollection'ın IndexOf'u olmadığından veri alanı indeksini manuel olarak bul
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.Pivot.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```
## **İlk 10 Filtresi**
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan özel bir değer filtresi biçimidir. Genellikle "gelire göre ilk 10 ürün" veya "satış sayısına göre son 5 bölge" gibi sıralama raporları için kullanılır.
{{% alert color="primary" %}}
İlk 10 filtresi yalnızca özet tablosunun veri alanında bir veya daha fazla değer pivot alanı olduğunda etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplanan bir ölçü yoktur ve filtre uygulanamaz.
{{% /alert %}}
Aspose.Cells, ilk 10 filtrelemeyi `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` yöntemi aracılığıyla sunar. `itemCount` parametresi kaç öğenin tutulacağını tanımlar, `isTop` en üstteki öğelerin (true) mi yoksa en alttaki öğelerin (false) mi tutulacağını belirtir, `valueField` sıralama için kullanılan veri alanına başvurur ve `filterType` değerin nasıl hesaplanacağını kontrol eder (genellikle `Sum`, ayrıca `Count` ve `Percent`).
Aşağıdaki örnek, değer alanı içeren özet tablosuna sahip bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için bir ilk 10 filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```javascript
output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);

// Pivot tablosunu barındıran çalışma sayfasına erişin (dizin 0)
let worksheet = workbook.getWorksheets().get(0);

// Dizine göre pivot tablosuna erişin
let pivotTable = worksheet.getPivotTables().get(0);

// Veri alanında en az bir değer PivotField olduğunu doğrulayın
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);

// Hedef satır PivotField'ını alın (Top 10 uygulamak istediğimiz alan)
let rowField = pivotTable.getRowFields().get(0);

// İlk (ve tek) veri alanı 0 dizinindedir; Top 10 bu alana göre sıralar.
let valueFieldIndex = 0;

// Satır alanına Top 10 filtresini uygulayın:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (ilk N; false alt N anlamına gelir)
//   - valueFieldIndex = öğeleri sıralamak için kullanılan veri alanının dizini
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// Pivot tablo verilerini yenileyin ve filtrenin etkili olması için yeniden hesaplayın
pivotTable.getPivotCache().refresh();

// Çalışma kitabını kaydedin
workbook.save(outputPath);
```
## **Özet Öğelerini Gizleyerek veya Göstererek Filtreleme**
Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir özet öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField` öğesinin `PivotItems` koleksiyonunda gezinerek ve `IsHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `IsHidden = true` ayarı öğeyi özet tablosundan gizler; `IsHidden = false` ayarı ise onu tekrar gösterir ve görünür hale getirir.
Bu yaklaşım, filtreleme kuralı düzensiz veya öğeye özgü olduğunda, örneğin belirli bir raporda görünmemesi gereken küçük sayıda adlandırılmış kategoriyi gizlerken kullanışlıdır. Aşağıdaki örnek bir özet tablosunu yükler, belirli bir öğeyi ada göre gizler, onu nasıl göstereceğinizi gösterir, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```javascript
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// İlk çalışma sayfasına erişim sağla, pivot tabloyu içeren sayfa
let sheet = workbook.getWorksheets().get(0);

// Pivot tabloya dizin yoluyla erişim sağla (sayfadaki ilk pivot tablo)
let pivotTable = sheet.getPivotTables().get(0);

// Hedef PivotField'i al (öğelerini gizleyeceğimiz/göstereceğimiz ilk satır etiket alanı)
let pivotField = pivotTable.getRowFields().get(0);

// Seçilen PivotField'in PivotItems koleksiyonu üzerinde yineleme yap
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);

    // Belirli bir ad/ölçütle eşleşen pivot öğelerini gizle
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setIsHidden(true);
    }

    // Gizleme işlemini geri almayı göster: daha önce gizlenmiş bir pivot öğesini yeniden göster
    if (item.getName() == "Item3") {
        item.setIsHidden(false);
    }
}

// Değişikliklerin etkili olması için pivot tabloyu yenile ve yeniden hesapla
pivotTable.getPivotCache().refreshData();

// Çalışma kitabını kaydet — gizli öğeler temel verilerde kalır
// ancak görüntülenen pivot tablo çıktısından hariç tutulur
workbook.save("output_pivot_filtered.xlsx");
```
## **Özet**
Aspose.Cells for Node.js via Java, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir özet tablo filtreleme yetenekleri seti sağlar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsar; ilk 10 filtresi ise sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.IsHidden` özelliği esnek, öğe düzeyinde bir geri dönüş seçeneği sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas şekilde hedeflenmiş özet tablo raporları oluşturmanıza olanak tanır.
{{< app/cells/assistant language="nodejs-java" >}}