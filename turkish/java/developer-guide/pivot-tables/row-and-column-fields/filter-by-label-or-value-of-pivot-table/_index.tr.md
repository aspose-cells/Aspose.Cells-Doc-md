---
title: Etiket veya Değere Göre Özet Tablolarını Filtreleme
linktitle: Etiket veya Değere Göre Özet Tablolarını Filtreleme
description: Aspose.Cells for Java, kapsamlı özet tablo filtreleme yeteneklerini destekler. Bu makale, özet tablo verilerinin etiket filtreleri, tarih filtreleri, değer filtreleri ve ilk 10 filtresi kullanılarak veya özet öğeleri gizlenip görünür hâle getirilerek nasıl filtreleneceğini açıklar.
keywords: Aspose.Cells, Java kitaplığı, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet öğesi, özet öğesini gizleme
type: docs
weight: 10
url: /tr/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir özet tabloda görüntülenen verileri filtrelemek için beş kullanışlı strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücrelerini veya boş hücreleri içeriyorsa tarih filtreleri kullanabilir, toplulaştırılmış sayısal değerlere karşı değer filtreleri uygulayabilir, bir değer alanına göre öğeleri sıralamak için ilk 10 filtresini kullanabilir veya `IsHidden` özelliğini kullanarak özet öğelerini tek tek gizleyip görünür hâle getirebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıflarındaki ilgili API'lerle sunulur.
{{% /alert %}}

## **Giriş**
Özet tablolar güçlü analitik araçlardır; ancak ham özetler genellikle sunmak istediğinizden çok daha fazla bilgi içerir. Filtreleme, bir özet tabloyu belirli bir rapor için önemli satırlar, sütunlar veya değerlerle sınırlandırmanın temel yoludur. Aspose.Cells for Java, Microsoft Excel'de bulunan filtreleme yeteneklerini yansıtır ve bunları programatik olarak sunar; böylece rapor oluşturma süreci tamamen otomatikleştirilebilir.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Etiket Filtresi** — metin etiketlerine göre satır veya sütun alanı öğelerini filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri veya boş değerler içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplulaştırılmış değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralanan en üstteki veya en alttaki N öğeyi gösterir.
5. **Özet Öğelerini Gizleme / Görünür Hâle Getirme** — bir alandaki her bir öğenin görünürlüğünü elle denetler.
Her yaklaşım, `PivotField` sınıfındaki ilgili yöntemlerden birini veya `PivotItem` sınıfındaki özelliklerden birini kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıması için özet tabloda `getPivotCache().refresh()` çağrısı yapmalısınız.

## **Etiket Filtresi**
Etiket filtresi, bir satır veya sütun alanının öğelerini metin etiketlerini bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Yalnızca adları belirli bir harfle başlayan, belirli bir sözcük içeren veya başka bir etiket ölçütüyle eşleşen ürünleri görüntülemek istediğinizde bu özellik yararlıdır.
Aspose.Cells, etiket filtrelemesini `PivotField.filterByLabel(PivotFilterType, String)` yöntemiyle sunar. `PivotFilterType` şu değerleri içerir: `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzerleri. İkinci argüman, karşılaştırmada kullanılan etiket dizesini sağlar.
Aşağıdaki örnek, mevcut bir özet tablo içeren çalışma kitabını yükler, yalnızca etiketleri belirli bir önekten başlayan öğelerin kalmasını sağlayan bir etiket filtresi uygular, özet tabloyu yeniler ve sonucu kaydeder.

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Tarih Filtresi**
Tarih filtreleri, bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarihe dayalı ölçütlerle özet tabloyu daraltmanızı sağlar. Bunlar, yalnızca tarih-saat bilgisi saklayan alanlara karşı çalışan özelleşmiş filtrelerdir.

{{% alert color="primary" %}}
Tarih filtresi, satır veya sütun alanı yalnızca tarih-saat hücrelerinden veya boş değerlerden oluşuyorsa çalışır. İlgili alan sayı veya metin gibi başka veri türleri içeriyorsa tarih filtresi beklenen sonucu vermez. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirilmiş olduğundan ve tüm değerlerin geçerli `DateTime` örnekleri ya da boş hücreler olduğundan emin olun.
Aspose.Cells, tarih filtrelemesini `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` yöntemiyle sunar. `PivotFilterType` şu özel tarih değerlerini içerir: `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between`. Seçilen filtre türüne bağlı olarak bir veya iki `DateTime` değeri belirtirsiniz (`Between` için başlangıç ve bitiş tarihlerini belirtirsiniz).
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan ve belirli bir tarih aralığındaki öğeleri görünür kılan bir özet tabloyu içeren çalışma kitabını yükler, özet tabloya bir tarih filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.
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
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Değer Filtresi**
Değer filtreleri, bir özet tablonun veri alanında hesapladığı toplulaştırılmış değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değerle karşılaştırırlar. Bu filtreler; yalnızca satış toplamı belirli bir hedef tutarı aşan ürünleri veya işlem sayısı belirli bir aralıkta kalan bölgeleri görüntülemek için sıkça kullanılır.
Aspose.Cells, değer filtrelemesini `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` yöntemiyle sunar. `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` değerlerinden birini alır. `valueField` parametresi değerlendirilecek veri alanını belirtir; son argüman veya argümanlar ise eşik değer(ler)i sağlar.
Aşağıdaki örnek, bir özet tablo içeren çalışma kitabını yükler, toplulaştırılmış satış toplamı sayısal bir eşiği aşan öğeleri koruyan bir değer filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **İlk 10 Filtresi**
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan değer filtresinin özelleşmiş bir biçimidir. Gelir bazında ilk 10 ürün veya satış sayısına göre son 5 bölge gibi sıralama raporlarında sıkça kullanılır.

{{% alert color="primary" %}}
İlk 10 filtresi, yalnızca özet tablonun veri alanında bir veya daha fazla değer alanı bulunduğunda etkilidir. En az bir değer alanı olmadığında, öğeleri sıralayacak toplulaştırılmış bir ölçüt bulunmaz ve filtre uygulanamaz.
Aspose.Cells, ilk 10 filtrelemesini `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)` yöntemiyle sunar. `valueFieldIndex` parametresi, öğelerin toplulaştırılmış değerlerine göre sıralandığı veri alanının dizinidir; `filterType` parametresi, `itemCount` için kullanılacak birimi belirler (`PivotFilterType.COUNT` belirli sayıda öğeyi tutar, `PivotFilterType.PERCENT` öğelerin belirli bir yüzdesini tutar ve bu durumda `itemCount` yüzde değeridir); `isTop` parametresi, en üstteki öğelerin (true) mi yoksa en alttaki öğelerin (false) mi tutulacağını belirtir; `itemCount` ise kaç öğenin veya hangi yüzdenin tutulacağını tanımlar.
Aşağıdaki örnek, bir değer alanı bulunan özet tabloyu içeren çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için ilk 10 filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.
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
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Özet Öğelerini Gizleyerek veya Görünür Hâle Getirerek Filtreleme**
Yapılandırılmış filtre API'lerine ek olarak Aspose.Cells, her bir özet öğesinin görünürlüğünü doğrudan denetlemenize olanak tanır. Bir `PivotField` nesnesinin `PivotItems` koleksiyonu üzerinde iterasyon yaparak ve `IsHidden` özelliğini değiştirerek, belirli öğeleri formül tabanlı bir filtre uygulamadan seçici olarak gizleyebilirsiniz. `IsHidden = true` ayarı öğeyi özet tabloda gizler; `IsHidden = false` ayarı ise öğeyi yeniden görünür kılar.
Bu yaklaşım, filtreleme kuralı düzensiz veya öğeye özgü olduğunda yararlıdır; örneğin belirli bir raporda yer almaması gereken birkaç kategoriyi gizlemek için kullanılabilir. Aşağıdaki örnek bir özet tabloyu yükler, ada göre belirli bir öğeyi gizler, görünür hâle getirme işlemini gösterir, özet tabloyu yeniler ve çalışma kitabını kaydeder.

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Özet**
Aspose.Cells for Java, Microsoft Excel'dekilerle uyumlu kapsamlı bir özet tablo filtreleme özelliği seti sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsarken ilk 10 filtresi sıralama raporlarını destekler. Filtreleme kuralı düzensiz olduğunda, `PivotItem.IsHidden` özelliği öğe düzeyinde esnek bir alternatif sunar. Bu stratejilerin birleştirilmesi — örneğin bir etiket filtresi uygulayıp ardından belirli öğeleri gizlemek — tamamen kod aracılığıyla belirli ölçütlere uygun özet tablo raporları oluşturmanıza olanak tanır.

## İlgili Makaleler
- [Özet Tablosu Ekle](/cells/tr/java/create-pivot-table/)
- [Aspose.Cells for Java ile Özet Tablosuna Satır ve Sütun Alanları Ekle](/cells/tr/java/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Java ile Özet Tablosuna Filtre Alanları Ekle](/cells/tr/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java ile Özet Tablosu Değer Alanlarını Yönet](/cells/tr/java/manage-value-fields/)
- [Aspose.Cells for Java ile Özet Tablolarını ve Özet Önbelleklerini Yenile](/cells/tr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}