---
title: Etiket veya Değere Göre Özet Tabloları Filtreleme
linktitle: Etiket veya Değere Göre Özet Tabloları Filtreleme
description: Aspose.Cells for Java kapsamlı özet tablo filtreleme özelliklerini destekler. Bu makale, etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri kullanarak ve öğeleri gizleyerek veya görünür hale getirerek özet tablo verilerinin nasıl filtreleneceğini açıklar.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet öğe, özet öğeyi gizle
type: docs
weight: 10
url: /tr/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, bir özet tablosunda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde tarih filtreleri kullanabilir, toplu sayılara karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtreleri kullanabilir veya `IsHidden` özelliğini kullanarak tek tek özet öğeleri manuel olarak gizleyebilir ve görünür hale getirebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıfları üzerindeki özel API'ler aracılığıyla sunulur.

{{% /alert %}}

## **Giriş**

Özet tablolar güçlü analiz araçlarıdır, ancak ham özetler genellikle sunmanız gerekenden çok daha fazla bilgi içerir. Filtreleme, bir özet tablosunu belirli bir rapor için önemli olan satırlara, sütunlara veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for Java, Microsoft Excel'de bulunan filtreleme özelliklerini yansıtır ve rapor oluşturmanın tamamen otomatikleştirilebilmesi için bunları programlı olarak sunar.

Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:

1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boş değerler) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplu değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralanmış yalnızca en üst veya en alt N öğeyi gösterir.
5. **Özet Öğelerini Gizleme / Görünür Hale Getirme** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.

Her yaklaşım, `PivotField` sınıfında farklı bir yöntem veya `PivotItem` sınıfında bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tablo üzerinde `refreshData()` ve `calculateData()` çağırmalısınız.

## **Etiket Filtresi**

Bir etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı kritere uyan ürünleri görüntülemek istediğinizde kullanışlıdır.

Aspose.Cells, etiket filtrelemeyi `PivotField.filterByLabel(PivotFilterType, String)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzeri değerleri içerir. İkinci argüman, karşılaştırma için kullanılan etiket dizesini sağlar.

Aşağıdaki örnek, mevcut bir özet tablo içeren bir çalışma kitabını yükler, yalnızca başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, özet tablosunu yeniler ve sonucu kaydeder.

```java
import com.aspose.cells.*;

String fileName = "sample.xlsx";
String prefix = "B";

// Pivot tablosu içeren mevcut çalışma kitabını yükle
Workbook workbook = new Workbook(fileName);

// Çalışma sayfasına dizine göre erişin (ilk çalışma sayfası)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizine göre erişin
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// İlk satır PivotField'ını al
PivotField rowField = pivotTable.getRowFields().get(0);

// Etiket filtresini uygula - yalnızca etiketleri sağlanan önekle başlayan satır öğelerini göster
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");

// Filtrenin etkili olması için pivot tablo verilerini yenileyin ve yeniden hesaplayın
pivotTable.refreshData();

// Çalışma kitabını tekrar diske kaydedin
workbook.save(fileName);
```

## **Tarih Filtresi**

Tarih filtreleri, özet tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı kriterlere göre daraltmanıza olanak tanır. Bunlar yalnızca tarih-saat bilgisi depolayan alanlara karşı çalışan özel filtrelerdir.

{{% alert color="primary" %}}

Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alandaki veri türü sayılar veya metin gibi başka türler içeriyorsa, tarih filtresi beklenen sonucu üretmez. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.

{{% /alert %}}

Aspose.Cells, tarih filtrelemeyi `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak bir veya iki `DateTime` değeri geçirirsiniz (`Between` için başlangıç ve bitiş tarihlerini geçirirsiniz).

Aşağıdaki örnek, satır alanında tarih alanı içeren bir özet tabloya sahip bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.

```java
import java.io.File;
import java.io.FileNotFoundException;

String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";

if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}

// Pivot tablosunu içeren mevcut çalışma kitabını yükleyin
Workbook workbook = new Workbook(inputPath);

// Pivot tablosunu barındıran çalışma sayfasına erişin (dizine göre)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizine göre erişin
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Tarih PivotField'ını satır alanından alın
// (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde çalışır)
PivotField dateField = pivotTable.getRowFields().get(0);

// Between filtresi için tarih kriterini tanımlayın
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// Pivot alanına tarih filtresini uygulayın
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);

// Filtrenin etkili olması için pivot tablosunu yenileyin ve yeniden hesaplayın
pivotTable.refreshData();

// Çalışma kitabını kaydedin
workbook.save(outputPath);
```

## **Değer Filtresi**

Değer filtreleri, bir özet tablosunun veri alanında hesapladığı toplu değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değerle karşılaştırır. Tipik kullanım durumları arasında yalnızca satış toplamı bir hedef tutarı aşan ürünlerin veya yalnızca işlem sayısı belirli bir aralıkta olan bölgelerin gösterilmesi yer alır.

Aspose.Cells, değer filtrelemeyi `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` yöntemi aracılığıyla sunar. `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerleri kullanır. `valueField` parametresi hangi veri alanının değerlendirileceğini belirtir ve son argüman(lar) eşik değer(ler)ini sağlar.

Aşağıdaki örnek, bir özet tablo içeren bir çalışma kitabını yükler, yalnızca toplu satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);

PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);

// PivotFieldCollection'da IndexOf olmadığından veri alanı indeksini manuel olarak bul
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}

pivotTable.refreshData();

workbook.save("output.xlsx");
```

## **İlk 10 Filtresi**

İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan özel bir değer filtresi biçimidir. Genellikle "gelire göre ilk 10 ürün" veya "satış sayısına göre en alt 5 bölge" gibi sıralama raporları için kullanılır.

{{% alert color="primary" %}}

İlk 10 filtresi yalnızca özet tablosunun veri alanında bir veya daha fazla değer pivot alanı olduğunda etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplu bir ölçü yoktur ve filtre uygulanamaz.

{{% /alert %}}

Aspose.Cells, ilk 10 filtrelemeyi `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)` yöntemi aracılığıyla sunar. `itemCount` parametresi kaç öğenin tutulacağını tanımlar, `isTop` en üst öğelerin mi (true) yoksa en alt öğelerin mi (false) tutulacağını belirtir, `valueField` sıralama için kullanılan veri alanına referans verir ve `filterType` değerin nasıl hesaplanacağını kontrol eder (genellikle `Sum`, ancak `Count` ve `Percent` da kullanılır).

Aşağıdaki örnek, bir değer alanı içeren bir özet tabloya sahip bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için bir ilk 10 filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.

```java
import com.aspose.cells.*;

// Pivot tablosunu içeren mevcut çalışma kitabını yükleyin
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// Pivot tablosunu barındıran çalışma sayfasına erişin (indeks 0)
Worksheet worksheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizine göre erişin
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// Veri alanında en az bir değer PivotField olduğunu doğrulayın
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);

// Hedef satır PivotField'ını alın (Top 10 uygulamak istediğimiz alan)
PivotField rowField = pivotTable.getRowFields().get(0);

// İlk (ve tek) veri alanı 0. dizindedir; Top 10 buna göre sıralar.
int valueFieldIndex = 0;

// Satır alanına Top 10 filtresini uygulayın:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (üst N; false alt N anlamına gelir)
//   - valueFieldIndex = öğeleri sıralamak için kullanılan veri alanının indeksi
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);

// Pivot tablo verilerini yenileyin ve filtrenin etkili olması için yeniden hesaplayın
pivotTable.refreshData();

// Çalışma kitabını kaydedin
workbook.save(outputPath);
```

## **Özet Öğelerini Gizleyerek veya Görünür Hale Getirerek Filtreleme**

Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir özet öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField`'ın `PivotItems` koleksiyonunda gezinerek ve `IsHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `IsHidden = true` ayarı öğeyi özet tablosundan gizler; `IsHidden = false` ayarı öğeyi görünür hale getirir ve tekrar görünür kılar.

Bu yaklaşım, filtreleme kuralının düzensiz veya öğeye özgü olduğu durumlarda, örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlerken kullanışlıdır. Aşağıdaki örnek bir özet tablosunu yükler, belirli bir öğeyi ada göre gizler, nasıl görünür hale getirileceğini gösterir, özet tablosunu yeniler ve çalışma kitabını kaydeder.

```java
import com.aspose.cells.*;

// Pivot tablosu içeren mevcut bir çalışma kitabını yükle
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// Pivot tablosunu içeren ilk çalışma sayfasına eriş
Worksheet sheet = workbook.getWorksheets().get(0);

// Pivot tablosuna dizine göre eriş (sayfadaki ilk pivot tablosu)
PivotTable pivotTable = sheet.getPivotTables().get(0);

// Hedef PivotField'i al (öğelerini gizleyeceğimiz/göstereceğimiz ilk satır etiket alanı)
PivotField pivotField = pivotTable.getRowFields().get(0);

// Seçilen PivotField'in PivotItems koleksiyonu üzerinde yineleme yap
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);

    // Belirli bir ad/ölçütle eşleşen pivot öğelerini gizle
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }

    // Gizlemeyi kaldırmayı göster: daha önce gizlenmiş bir pivot öğesini yeniden göster
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}

// Değişikliklerin etkili olması için pivot tablosunu yenile ve yeniden hesapla
pivotTable.refreshData();

// Çalışma kitabını kaydet - gizli öğeler alttaki verilerde kalır
// ancak görüntülenen pivot tablosu çıktısından çıkarılır
workbook.save("output_pivot_filtered.xlsx");
```

## **Özet**

Aspose.Cells for Java, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir özet tablo filtreleme özellikleri seti sunar. Etiket, tarih ve değer filtreleri en yaygın analiz senaryolarını kapsar, ilk 10 filtresi ise sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.IsHidden` özelliği esnek, öğe düzeyinde bir geri dönüş sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas şekilde hedeflenmiş özet tablo raporları oluşturmanıza olanak tanır.
{{< app/cells/assistant language="java" >}}
