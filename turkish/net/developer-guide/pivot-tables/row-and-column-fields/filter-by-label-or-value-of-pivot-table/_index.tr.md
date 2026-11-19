---
title: Pivot Tablolarını Etiket veya Değere Göre Filtreleme
linktitle: Etikete veya Değere Göre Filtreleme
description: Aspose.Cells for .NET, kapsamlı pivot tablo filtreleme özelliklerini destekler. Bu makale, pivot tablo verilerini etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri kullanarak ve pivot öğelerini gizleyerek veya görünür kılarak nasıl filtreleneceğini açıklar.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, pivot tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, pivot öğesi, pivot öğesini gizle
type: docs
weight: 10
url: /tr/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir pivot tablosunda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde tarih filtreleri kullanabilir, toplu sayılara karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtreleri kullanabilir veya `IsHidden` özelliğini kullanarak tek tek pivot öğelerini manuel olarak gizleyip görünür kılabilirsiniz. Her bir strateji, `PivotField` ve `PivotItem` sınıfları üzerindeki özel API'ler aracılığıyla kullanıma sunulur.
{{% /alert %}}

## **Introduction**
Pivot tabloları güçlü analitik araçlardır, ancak ham özetler genellikle sunmanız gereken bilgilerden çok daha fazlasını içerir. Filtreleme, bir pivot tablosunu belirli bir rapor için önemli olan satır, sütun veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for .NET, Microsoft Excel'de bulunan filtreleme özelliklerini yansıtır ve bunları programlı olarak sunarak rapor oluşturmanın tamamen otomatikleştirilmesini sağlar.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Label Filter** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Date Filter** — yalnızca tarih-saat değerleri (veya boşluklar) içeren satır veya sütun alanlarını filtreler.
3. **Value Filter** — öğeleri bir veri alanının toplu değerlerine göre filtreler.
4. **Top 10 Filter** — yalnızca bir değer alanına göre sıralanan en üst veya en alt N öğeyi gösterir.
5. **Hide / Unhide Pivot Items** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.
Her yaklaşım, `PivotField` sınıfında farklı bir yöntem veya `PivotItem` sınıfında bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınan verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için pivot tablosunda `PivotCache.Refresh()` çağrısı yapmanız gerekir.

## **Label Filter**
Etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı kritere uyan ürünleri görüntülemek istediğinizde kullanışlıdır.
Aspose.Cells, etiket filtrelemeyi `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)` yöntemi aracılığıyla sunar. `filterType` argümanı karşılaştırma modunu seçer (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` vb.). `label1` ve `label2` argümanları karşılaştırma metnini sağlar — yalnızca tek değerli bir eşleşmeye ihtiyacınız olduğunda `label2` için `string.Empty` geçin (örneğin, başlayan veya içeren).
Aşağıdaki örnek, mevcut bir pivot tablo içeren bir çalışma kitabını yükler, başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, pivot tablosunu yeniler ve sonucu kaydeder.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string fileName = "sample.xlsx";
string prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.Worksheets[0];
// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];
// Retrieve the first row PivotField
PivotField rowField = pivotTable.RowFields[0];
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook back to disk
workbook.Save(fileName);
```

## **Date Filter**
Tarih filtreleri, bir pivot tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı kriterlere göre daraltmanıza olanak tanır. Bunlar, yalnızca tarih-saat bilgisi depolayan alanlara karşı çalışan özel filtrelerdir.

{{% alert color="primary" %}}
Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alan sayılar veya metin gibi başka veri türleri içeriyorsa, tarih filtresi beklenen sonucu üretmez. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.
Aspose.Cells, tarih filtrelemeyi `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması, `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak, bir veya iki `DateTime` değeri geçersiniz (`Between` için başlangıç ve bitiş tarihlerini geçersiniz).
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan bir pivot tabloya sahip bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

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
// Load the existing workbook that contains the pivot table
var workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.Worksheets[0];
// Access the pivot table by index
var pivotTable = worksheet.PivotTables[0];
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.RowFields[0];
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.PivotCache.Refresh();
// Persist the workbook
workbook.Save(outputPath);
```

## **Value Filter**
Değer filtreleri, bir pivot tablosunun veri alanında hesapladığı toplu değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değeriyle karşılaştırırlar. Tipik kullanım örnekleri arasında yalnızca satış toplamı hedef tutarı aşan ürünleri veya işlem sayısı belirli bir aralıkta olan bölgeleri göstermek yer alır.
Aspose.Cells, değer filtrelemeyi `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` yöntemi aracılığıyla sunar. `valueFieldIndex` parametresi, hangi veri alanının değerlendirileceğini belirtir (konumu bulmak için `pivotTable.DataFields.IndexOf(dataField)` kullanın veya koleksiyonda yineleme yapın). `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. İki `double` argümanı eşik değerini (veya değerlerini) sağlar.
Aşağıdaki örnek, bir pivot tablo içeren bir çalışma kitabını yükler, yalnızca toplu satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];
var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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

## **Top 10 Filter**
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan özel bir değer filtresi biçimidir. "Gelire göre ilk 10 ürün" veya "Satış sayısına göre en kötü 5 bölge" gibi sıralama raporları için yaygın olarak kullanılır.

{{% alert color="primary" %}}
İlk 10 filtresi, yalnızca pivot tablosunun veri alanında bir veya daha fazla değer pivot alanı olduğunda etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için karşılaştırılacak toplu bir ölçü yoktur ve filtre uygulanamaz.
Aspose.Cells, Top 10 filtrelemesini `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` yöntemi üzerinden sunar. `valueFieldIndex` parametresi, öğelerin sıralandığı birleşik değerlere sahip veri alanının dizinidir, `filterType` `itemCount` birimini seçer (`Count` sabit sayıda öğe tutar, `Percent` öğelerin bir yüzdesini tutar, bu nedenle `itemCount` yüzdenin kendisidir), `isTop` üst öğelerin (true) mi alt öğelerin mi (false) tutulacağını belirtir ve `itemCount` kaç öğenin veya hangi yüzdenin tutulacağını tanımlar.
Aşağıdaki örnek, bir değer alanı içeren bir pivot tabloya sahip bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için bir ilk 10 filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load the existing workbook that contains the pivot table
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.Worksheets[0];
// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];
// Confirm there is at least one value PivotField in the data area
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.RowFields[0];
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - valueFieldIndex = 0 — the data field used to rank items
//   - filterType  = PivotFilterType.Count (keep a fixed number of items;
//     PivotFilterType.Percent would interpret 10 as "top 10 percent")
//   - isTop       = true (top N; false would mean bottom N)
//   - itemCount   = 10
rowField.FilterTop10(valueFieldIndex, PivotFilterType.Count, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook
workbook.Save(outputPath);
```

## **Filter by Hiding or Unhiding Pivot Items**
Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir pivot öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField`'in `PivotItems` koleksiyonunda yineleme yaparak ve `IsHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `IsHidden = true` ayarı, öğeyi pivot tablosundan gizler; `IsHidden = false` ayarı, öğeyi görünür kılar ve tekrar görünür hale getirir.
Bu yaklaşım, filtreleme kuralı düzensiz veya öğeye özgü olduğunda, örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlerken kullanışlıdır. Aşağıdaki örnek bir pivot tablo yükler, belirli bir öğeyi ada göre gizler, onu nasıl görünür kılacağınızı gösterir, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.Worksheets[0];
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.PivotTables[0];
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.RowFields[0];
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];
    // Hide pivot items that match a specific name/criterion
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.PivotCache.Refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.Save("output_pivot_filtered.xlsx");
```

## **Summary**
Aspose.Cells for .NET, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir pivot tablo filtreleme özellikleri seti sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsar, ilk 10 filtresi ise sıralama raporlarını yönetir. Filtreleme kuralı düzensiz olduğunda, `PivotItem.IsHidden` özelliği esnek, öğe düzeyinde bir geri dönüş sunar. Bu stratejileri birleştirmek — örneğin, bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas şekilde hedeflenmiş pivot tablo raporları oluşturmanıza olanak tanır.

## Related Articles
- [Aspose.Cells for .NET'te Pivot Tablo Satır ve Sütun Alanları Ekleme](/cells/tr/net/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for .NET'te Pivot Tablo Değer Alanlarını Yönetme](/cells/tr/net/manage-value-fields/)
- [Aspose.Cells for .NET'te Pivot Tablolarını ve Pivot Önbelleklerini Yenileme](/cells/tr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}