---
title: Etikete veya Değere Göre Özet Tablolarını Filtreleme
linktitle: Etikete veya Değere Göre Özet Tablolarını Filtreleme
description: Aspose.Cells for Java, kapsamlı özet tablo filtreleme özelliklerini destekler. Bu makale, etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri ve özet tablo öğelerini gizleyerek veya görünür hâle getirerek özet tablo verilerinin nasıl filtreleneceğini açıklar.
keywords: Aspose.Cells, Java kitaplığı, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet tablo öğesi, özet tablo öğesini gizleme
type: docs
weight: 10
url: /tr/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir özet tabloda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücrelerini veya boş değerleri içeriyorsa tarih filtreleri kullanabilir, toplulaştırılmış sayılar üzerinde değer filtreleri uygulayabilir, bir değer alanına göre sıralama yapmak için ilk 10 filtresini kullanabilir veya `IsHidden` özelliğini kullanarak bireysel özet tablo öğelerini elle gizleyip görünür hâle getirebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıflarındaki ilgili API'ler aracılığıyla sunulur.
{{% /alert %}}

## **Giriş**
Özet tablolar güçlü analitik araçlardır; ancak ham özetler genellikle sunmak istediğinizden çok daha fazla bilgi içerir. Filtreleme, bir özet tabloyu belirli bir rapor için gereken satırlarla, sütunlarla veya değerlerle daraltmanın temel mekanizmasıdır. Aspose.Cells for Java, Microsoft Excel'de kullanılabilen filtreleme özelliklerini programatik olarak sunar; böylece rapor oluşturma süreci tamamen otomatikleştirilebilir.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Etiket Filtresi** — metin etiketlerine göre bir satır veya sütun alanının öğelerini filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerlerini veya boş hücreleri içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplulaştırılmış değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralama yaparak yalnızca ilk veya son N öğeyi gösterir.
5. **Özet Tablo Öğelerini Gizleme / Görünür Hâle Getirme** — bir alandaki her bireysel öğenin görünürlüğünü elle denetler.
Her yaklaşım, `PivotField` sınıfında farklı bir metot veya `PivotItem` sınıfında bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tablo üzerinde `refreshData()` ve `calculateData()` çağırın.

## **Etiket Filtresi**
Etiket filtresi, bir satır veya sütun alanının öğelerini, metin etiketlerini bir desenle karşılaştırarak filtrelemenizi sağlar. Yalnızca adları belirli bir harfle başlayan, belirli bir sözcük içeren veya başka bir etiket ölçütüyle eşleşen ürünleri görüntülemek istediğinizde bu yöntem kullanışlıdır.
Aspose.Cells, etiket filtrelemeyi `PivotField.filterByLabel(PivotFilterType, String)` metoduyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzeri değerleri içerir. İkinci argüman, karşılaştırmada kullanılacak etiket dizesini belirtir.
Aşağıdaki örnek, mevcut bir özet tablo içeren bir çalışma kitabını yükler ve yalnızca etiketleri belirli bir ön ekle başlayan öğelerin görünür kalmasını sağlayan bir etiket filtresi uygular. Ardından özet tabloyu yeniler ve sonucu kaydeder.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Pivot tablosu içeren mevcut çalışma kitabını yükle
Workbook workbook = new Workbook(fileName);
// Çalışma sayfasına dizinle eriş (ilk çalışma sayfası)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Pivot tablosuna dizinle eriş
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// İlk satır PivotField'ını al
PivotField rowField = pivotTable.getRowFields().get(0);
// Etiket filtresini uygula - yalnızca etiketleri sağlanan ön ekle başlayan satır öğelerini göster
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Filtre geçerli olsun diye pivot tablosu verilerini yenile ve yeniden hesapla
pivotTable.refreshData();
// Çalışma kitabını diske geri kaydet
workbook.save(fileName);
```

## **Tarih Filtresi**
Tarih filtreleri, bugün, geçen hafta, bu ay, sonraki çeyrek veya belirli bir tarih aralığı gibi tarihe dayalı ölçütlere göre bir özet tabloyu daraltmanızı sağlar. Bunlar, yalnızca tarih-saat bilgisi saklayan alanlarda çalışan özel filtrelerdir.

{{% alert color="primary" %}}
Tarih filtresi, yalnızca tarih-saat hücreleri veya boş değerler içeren bir satır veya sütun alanında çalışır. İlgili alan sayı veya metin gibi başka veri türleri içeriyorsa tarih filtresi beklenen sonucu vermez. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm hücrelerin geçerli `DateTime` değerleri içerdiğinden veya boş olduğundan emin olun.
Aspose.Cells, tarih filtrelemeyi `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` metoduyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerlerini içerir. Belirlenen filtre türüne göre bir veya iki `DateTime` değeri belirtirsiniz; `Between` filtresi için başlangıç ve bitiş tarihlerini verirsiniz.
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan bir özet tablo içeren bir çalışma kitabını yükler ve yalnızca belirli bir tarih aralığındaki öğelerin görünür kalmasını sağlayan bir tarih filtresi uygular. Ardından özet tabloyu yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

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
// Pivot tablosunu içeren çalışma sayfasına erişin (dizinle)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Pivot tablosuna dizinle erişin
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Tarih PivotField'ini satır alanından alın
// (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boş hücreler içerdiğinde çalışır)
PivotField dateField = pivotTable.getRowFields().get(0);
// Between filtresi için tarih ölçütünü tanımlayın
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Pivot alanına tarih filtresini uygulayın
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Filtrenin etkinleşmesi için pivot tablosunu yenileyin ve yeniden hesaplayın
pivotTable.refreshData();
// Çalışma kitabını kaydedin
workbook.save(outputPath);
```

## **Değer Filtresi**
Değer filtreleri, bir özet tablonun veri alanında hesapladığı toplulaştırılmış değerler üzerinde çalışır. Metin etiketleriyle eşleştirmek yerine, sayısal toplamları bir eşik değerle karşılaştırırlar. Tipik kullanım durumları arasında yalnızca satış toplamı hedef tutarı aşan ürünlerin veya işlem sayısı belirli bir aralıkta bulunan bölgelerin gösterilmesi yer alır.
Aspose.Cells, değer filtrelemeyi `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` metoduyla sunar. `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerleri kullanır. `valueField` parametresi, değerlendirilecek veri alanını belirtir; son argüman veya argümanlar ise eşik değerleri sağlar.
Aşağıdaki örnek, bir özet tablo içeren bir çalışma kitabını yükler ve yalnızca toplulaştırılmış satış toplamları sayısal bir eşiği aşan öğeleri bırakan bir değer filtresi uygular. Ardından özet tabloyu yeniler ve çalışma kitabını kaydeder.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// PivotFieldCollection'ın IndexOf metodu olmadığından veri alanı dizinini manuel olarak bul
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
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi koruyan özel bir değer filtresi türüdür. Gelire göre ilk 10 ürün veya satış sayısına göre son 5 bölge gibi sıralama raporlarında yaygın olarak kullanılır.

{{% alert color="primary" %}}
İlk 10 filtresi, yalnızca özet tablonun veri alanında bir veya daha fazla değer alanı bulunduğunda etkilidir. En az bir değer alanı yoksa, öğeleri sıralamak için kullanılacak toplulaştırılmış bir ölçü bulunmaz ve filtre uygulanamaz.
Aspose.Cells, ilk 10 filtrelemeyi `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)` metoduyla sunar. `itemCount` parametresi, kaç öğenin korunacağını belirtir; `isTop`, en yüksek öğelerin mi (true) yoksa en düşük öğelerin mi (false) korunacağını gösterir; `valueField`, sıralamada kullanılan veri alanına başvurur ve `filterType`, değerin nasıl hesaplandığını denetler. Genellikle `Sum` kullanılır; `Count` ve `Percent` de kullanılabilir.
Aşağıdaki örnek, bir değer alanı bulunan bir özet tabloyu içeren çalışma kitabını yükler ve satış toplamına göre yalnızca en yüksek 10 öğeyi koruyan bir ilk 10 filtresi uygular. Ardından özet tabloyu yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.SUM, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.refreshData();
// Save the workbook
workbook.save(outputPath);
```

## **Özet Tablo Öğelerini Gizleyerek veya Görünür Hâle Getirerek Filtreleme**
Yapılandırılmış filtre API'lerine ek olarak Aspose.Cells, her bireysel özet tablo öğesinin görünürlüğünü doğrudan denetlemenize olanak tanır. Bir `PivotField` nesnesinin `PivotItems` koleksiyonunda gezinip `IsHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `IsHidden = true` ayarı öğeyi özet tablodan gizler; `IsHidden = false` ayarı öğeyi yeniden görünür hâle getirir.
Bu yaklaşım, filtre kuralı düzensiz veya öğeye özgü olduğunda kullanışlıdır. Örneğin, belirli bir raporda görünmesi gerekmeyen az sayıdaki adlandırılmış kategoriyi gizlemek için bu yaklaşımdan yararlanılabilir. Aşağıdaki örnek, bir özet tabloyu yükler, ada göre belirli bir öğeyi gizler ve öğenin nasıl görünür hâle getirileceğini gösterir. Ardından özet tabloyu yeniler ve çalışma kitabını kaydeder.

```java
import com.aspose.cells.*;
// Bir pivot tablosu içeren mevcut çalışma kitabını yükleyin
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Pivot tablosunu içeren ilk çalışma sayfasına erişin
Worksheet sheet = workbook.getWorksheets().get(0);
// Pivot tablosuna dizinle erişin (sayfadaki ilk pivot tablosu)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Hedef PivotField alanını alın (öğeleri gizleyeceğimiz/göstereceğimiz ilk satır etiketi alanı)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Seçilen PivotField alanının PivotItems koleksiyonu üzerinde yineleyin
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Belirli bir ada/kriterle eşleşen pivot öğelerini gizleyin
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Gizlemeyi kaldırma işlemini gösterin: daha önce gizlenmiş bir pivot öğesini yeniden gösterin
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Değişikliklerin geçerli olması için pivot tablosunu yenileyin ve yeniden hesaplayın
pivotTable.refreshData();
// Çalışma kitabını kaydedin - gizli öğeler temel veride kalır
// ancak görüntülenen pivot tablosu çıktısından hariç tutulur
workbook.save("output_pivot_filtered.xlsx");
```

## **Özet**
Aspose.Cells for Java, Microsoft Excel'dekilerle eşleşen kapsamlı bir özet tablo filtreleme özellikleri paketi sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsarken ilk 10 filtresi sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda `PivotItem.IsHidden` özelliği, öğe düzeyinde esnek bir alternatif sunar. Bu stratejileri birleştirerek — örneğin bir etiket filtresi uygulayıp ardından belirli öğeleri gizleyerek — tamamen kod aracılığıyla hassas biçimde hedeflenmiş özet tablo raporları oluşturabilirsiniz.

## İlgili Makaleler
- [Özet Tablo Ekle](/cells/tr/java/create-pivot-table/)
- [Aspose.Cells for Java ile Özet Tabloya Satır ve Sütun Alanları Ekle](/cells/tr/java/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Java ile Özet Tabloya Filtre Alanları Ekle](/cells/tr/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java ile Özet Tablosunun Değer Alanlarını Yönet](/cells/tr/java/manage-value-fields/)
- [Aspose.Cells for Java ile Özet Tablolarını ve Özet Tablo Önbelleklerini Yenile](/cells/tr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}