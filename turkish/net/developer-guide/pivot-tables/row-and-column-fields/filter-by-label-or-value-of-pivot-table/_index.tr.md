---
title: Özet Tabloları Etikete veya Değere Göre Filtreleme
linktitle: Özet Tabloları Etikete veya Değere Göre Filtreleme
description: Aspose.Cells for .NET, kapsamlı özet tablo filtreleme yeteneklerini destekler. Bu makale, özet tablo verilerini etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri ile filtrelemeyi ve özet öğeleri gizleyerek veya görünür kılarak filtrelemeyi açıklar.
keywords: Aspose.Cells, .NET library, spreadsheet, pivot table, filter, label filter, value filter, date filter, top 10 filter, pivot item, hide pivot item
type: docs
weight: 10
url: /tr/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells, özet tablosunda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde tarih filtrelerini kullanabilir, toplanan sayılara karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtrelerini kullanabilir veya `IsHidden` özelliğini kullanarak tek tek özet öğelerini manuel olarak gizleyebilir ve görünür kılabilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıfları üzerindeki özel API'ler aracılığıyla kullanıma sunulur.
{{% /alert %}}
## **Giriş**
Özet tablolar güçlü analiz araçlarıdır, ancak ham özetler genellikle sunmanız gerekenden çok daha fazla bilgi içerir. Filtreleme, bir özet tablosunu belirli bir rapor için önemli olan satırlara, sütunlara veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for .NET, Microsoft Excel'de bulunan filtreleme yeteneklerini yansıtır ve bunları programatik olarak sunarak rapor oluşturmanın tamamen otomatikleştirilmesini sağlar.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boşluklar) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplanan değerlerine göre filtreler.
4. **İlk 10 Filtresi** — yalnızca bir değer alanına göre sıralanan en yüksek veya en düşük N öğeyi gösterir.
5. **Özet Öğelerini Gizle / Görünür Kıl** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.
Her yaklaşım, `PivotField` sınıfında farklı bir yöntem veya `PivotItem` sınıfında bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınan verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tablosunda `RefreshData()` ve `CalculateData()` çağırmalısınız.
## **Etiket Filtresi**
Etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı kritere uyan ürünleri görüntülemek istediğinizde kullanışlıdır.
Aspose.Cells, etiket filtrelemeyi `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzeri değerler içerir. İkinci argüman, karşılaştırma için kullanılan etiket dizesini sağlar.
Aşağıdaki örnek, mevcut bir özet tablo içeren bir çalışma kitabını yükler, başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, özet tablosunu yeniler ve sonucu kaydeder.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string fileName = "sample.xlsx";
string prefix = "B";

// Pivot tablosu içeren mevcut çalışma kitabını yükle
Workbook workbook = new Workbook(fileName);

// Çalışma sayfasına dizine göre eriş (ilk çalışma sayfası)
Worksheet worksheet = workbook.Worksheets[0];

// Pivot tablosuna dizine göre eriş
PivotTable pivotTable = worksheet.PivotTables[0];

// İlk satır PivotField'ını al
PivotField rowField = pivotTable.RowFields[0];

// Etiket filtresini uygula — yalnızca etiketleri sağlanan ön ek ile başlayan satır öğelerini göster
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);

// Filtrenin etkili olması için pivot tablo verilerini yenile ve yeniden hesapla
pivotTable.PivotCache.Refresh();

// Çalışma kitabını tekrar diske kaydet
workbook.Save(fileName);
```
## **Tarih Filtresi**
Tarih filtreleri, özet tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı kriterlere göre daraltmanıza olanak tanır. Bunlar, yalnızca tarih-saat bilgilerini depolayan alanlara karşı çalışan özelleşmiş filtrelerdir.
{{% alert color="primary" %}}
Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alan sayılar veya metin gibi başka veri türleri içeriyorsa, tarih filtresi beklenen sonucu üretmeyecektir. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.
{{% /alert %}}
Aspose.Cells, tarih filtrelemeyi `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak, bir veya iki `DateTime` değeri geçirirsiniz (`Between` için başlangıç ve bitiş tarihlerini geçirirsiniz).
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan özet tabloya sahip bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";

if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}

// Pivot tablosunu içeren mevcut çalışma kitabını yükle
var workbook = new Workbook(inputPath);

// Pivot tablosunu tutan çalışma sayfasına eriş (dizine göre)
var worksheet = workbook.Worksheets[0];

// Pivot tablosuna dizine göre eriş
var pivotTable = worksheet.PivotTables[0];

// Satır alanından tarih PivotField'ını al
// (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde çalışır)
PivotField dateField = pivotTable.RowFields[0];

// Between filtresi için tarih kriterini tanımla
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Pivot alanına tarih filtresini uygula
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);

// Filtrenin geçerli olması için pivot tablosunu yenile ve yeniden hesapla
pivotTable.PivotCache.Refresh();

// Çalışma kitabını kaydet
workbook.Save(outputPath);
```
## **Değer Filtresi**
Değer filtreleri, bir özet tablosunun veri alanında hesapladığı toplanan değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değeriyle karşılaştırırlar. Tipik kullanım durumları arasında yalnızca satış toplamı hedef tutarı aşan ürünleri veya işlem sayısı belirli bir aralıkta olan bölgeleri göstermek yer alır.
Aspose.Cells, değer filtrelemeyi `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` yöntemi aracılığıyla sunar. `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. `valueField` parametresi hangi veri alanının değerlendirileceğini belirtir ve son argüman(lar) eşik değerini(lerini) sağlar.
Aşağıdaki örnek, bir özet tablo içeren bir çalışma kitabını yükler, toplanan satışları sayısal eşiği aşan öğeleri yalnızca tutan bir değer filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];

var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];

// PivotFieldCollection'da IndexOf olmadığı için veri alanı indeksini manuel olarak bul
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}

pivotTable.PivotCache.Refresh();

workbook.Save("output.xlsx");
```
## **İlk 10 Filtresi**
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan özelleşmiş bir değer filtresi biçimidir. Genellikle "gelire göre ilk 10 ürün" veya "satış sayısına göre son 5 bölge" gibi sıralama raporları için kullanılır.
{{% alert color="primary" %}}
İlk 10 filtresi yalnızca özet tablosunun veri alanında bir veya daha fazla değer pivot alanı olduğunda etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplanan bir ölçü yoktur ve filtre uygulanamaz.
{{% /alert %}}
Aspose.Cells, ilk 10 filtrelemeyi `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)` yöntemi aracılığıyla sunar. `itemCount` parametresi kaç öğenin tutulacağını tanımlar, `isTop` en üst öğelerin (true) mi yoksa en alt öğelerin (false) mi tutulacağını belirtir, `valueField` sıralama için kullanılan veri alanına referans verir ve `filterType` değerin nasıl hesaplanacağını kontrol eder (genellikle `Sum`, ancak `Count` ve `Percent` de kullanılır).
Aşağıdaki örnek, bir değer alanı içeren özet tabloya sahip bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için bir ilk 10 filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Mevcut çalışma kitabını yükle (pivot tabloyu içeren)
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Pivot tabloyu barındıran çalışma sayfasına eriş (indeks 0)
Worksheet worksheet = workbook.Worksheets[0];

// Pivot tabloya indekse göre eriş
PivotTable pivotTable = worksheet.PivotTables[0];

// Veri alanında en az bir değer PivotField olduğunu doğrula
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot tablosunda değer (veri) PivotField yok.");
}
PivotField valueField = pivotTable.DataFields[0];

// Hedef satır PivotField'ını al (Top 10 uygulamak istediğimiz alan)
PivotField rowField = pivotTable.RowFields[0];

// İlk (ve tek) veri alanı 0. indekstedir; Top 10 sıralaması buna göre yapılır.
int valueFieldIndex = 0;

// Satır alanında Top 10 filtresini uygula:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (ilk N; false son N anlamına gelir)
//   - valueFieldIndex = öğeleri sıralamak için kullanılan veri alanının indeksi
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);

// Pivot tablo verilerini yenile ve filtrenin etkili olması için yeniden hesapla
pivotTable.PivotCache.Refresh();

// Çalışma kitabını kaydet
workbook.Save(outputPath);
```
## **Özet Öğelerini Gizleyerek veya Görünür Kılarak Filtreleme**
Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir özet öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField`'in `PivotItems` koleksiyonunda gezinerek ve `IsHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `IsHidden = true` ayarı öğeyi özet tablosundan gizler; `IsHidden = false` ayarı onu görünür kılar ve tekrar görünür hale getirir.
Bu yaklaşım, filtreleme kuralı düzensiz veya öğeye özgü olduğunda, örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlerken kullanışlıdır. Aşağıdaki örnek bir özet tablosunu yükler, ada göre belirli bir öğeyi gizler, nasıl görünür kılınacağını gösterir, özet tablosunu yeniler ve çalışma kitabını kaydeder.
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Mevcut bir çalışma kitabını pivot tablo içeren yükleyin
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Pivot tabloyu içeren ilk çalışma sayfasına erişin
Worksheet sheet = workbook.Worksheets[0];

// Pivot tablosuna dizine göre erişin (sayfadaki ilk pivot tablosu)
PivotTable pivotTable = sheet.PivotTables[0];

// Hedef PivotField alanını alın (öğelerini gizleyeceğimiz/göstereceğimiz ilk satır etiket alanı)
PivotField pivotField = pivotTable.RowFields[0];

// Seçilen PivotField alanının PivotItems koleksiyonu üzerinde yineleme yapın
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];

    // Belirli bir ada/ölçüte uyan pivot öğelerini gizleyin
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }

    // Gizlemeyi kaldırmayı gösterin: daha önce gizlenmiş bir pivot öğesini tekrar gösterin
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}

// Değişikliklerin etkili olması için pivot tabloyu yenileyin ve yeniden hesaplayın
pivotTable.PivotCache.Refresh();

// Çalışma kitabını kaydedin — gizli öğeler alttaki verilerde kalır,
// ancak görüntülenen pivot tablo çıktısından hariç tutulur
workbook.Save("output_pivot_filtered.xlsx");
```
## **Özet**
Aspose.Cells for .NET, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir özet tablo filtreleme yetenekleri seti sağlar. Etiket, tarih ve değer filtreleri en yaygın analiz senaryolarını kapsar, ilk 10 filtresi ise sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.IsHidden` özelliği esnek, öğe düzeyinde bir geri dönüş seçeneği sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas hedefli özet tablo raporları oluşturmanıza olanak tanır.
{{< app/cells/assistant language="csharp" >}}