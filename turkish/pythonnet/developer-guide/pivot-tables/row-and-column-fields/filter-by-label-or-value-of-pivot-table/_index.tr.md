---
title: Pivot Tablolarını Etikete veya Değere Göre Filtreleme
description: Aspose.Cells for Python via .NET, kapsamlı pivot tablo filtreleme özelliklerini destekler. Bu makale, pivot tablo verilerini etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri ve pivot öğelerini gizleyerek veya görünür hale getirerek nasıl filtreleyeceğinizi açıklar.
linktitle: Pivot Tablolarını Etikete veya Değere Göre Filtreleme
keywords: Aspose.Cells, Python via .NET kütüphanesi, elektronik tablo, pivot tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, pivot öğesi, pivot öğesini gizle
type: docs
weight: 10
url: /tr/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir pivot tabloda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde tarih filtreleri kullanabilir, toplam sayılara karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtreleri kullanabilir veya `is_hidden` özelliğini kullanarak tek tek pivot öğelerini manuel olarak gizleyip görünür hale getirebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıflarındaki özel API'ler aracılığıyla kullanıma sunulur.
{{% /alert %}}

## **Giriş**
Pivot tablolar güçlü analitik araçlardır, ancak ham özetler genellikle sunmanız gerekenden çok daha fazla bilgi içerir. Filtreleme, bir pivot tablosunu belirli bir rapor için önemli olan satır, sütun veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for Python via .NET, Microsoft Excel'de bulunan filtreleme özelliklerini yansıtarak bunları programatik olarak sunar; böylece rapor oluşturma tamamen otomatikleştirilebilir.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boş değerler) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplam değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralanmış yalnızca en yüksek veya en düşük N öğeyi gösterir.
5. **Pivot Öğelerini Gizle / Görünür Hale Getir** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.
Her yaklaşım, `PivotField` sınıfında farklı bir yöntem veya `PivotItem` sınıfında farklı bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için pivot tabloda `refresh_data()` ve `calculate_data()` çağırmanız gerekir.

## **Etiket Filtresi**
Etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı ölçüte uyan ürünleri görüntülemek istediğinizde kullanışlıdır.
Aspose.Cells, etiket filtrelemeyi `PivotField.filter_by_label(PivotFilterType, label_string)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzeri değerler içerir. İkinci bağımsız değişken, karşılaştırma için kullanılan etiket dizesini sağlar.
Aşağıdaki örnek, mevcut bir pivot tablo içeren bir çalışma kitabını yükler, yalnızca başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, pivot tablosunu yeniler ve sonucu kaydeder.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = ac.Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the first row PivotField
row_field = pivot_table.row_fields[0]
# Apply the label filter — show only row items whose labels begin with the supplied prefix
row_field.filter_by_label(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivot_table.pivot_cache.refresh()
# Save the workbook back to disk
workbook.save(fileName)
```

## **Tarih Filtresi**
Tarih filtreleri, bir pivot tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı ölçütlere göre daraltmanıza olanak tanır. Bunlar yalnızca tarih-saat bilgilerini depolayan alanlara karşı çalışan özel filtrelerdir.

{{% alert color="primary" %}}
Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alandaki alan sayılar veya metin gibi başka veri türleri içeriyorsa, tarih filtresi beklenen sonucu vermeyecektir. Filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `datetime` örnekleri veya boş hücreler olduğundan emin olun.
Aspose.Cells, tarih filtrelemeyi `PivotField.filter_by_date(PivotFilterType, *date_times)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak, bir veya iki `datetime` değeri iletirsiniz (`Between` için başlangıç ve bitiş tarihlerini iletirsiniz).
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan pivot tabloya sahip bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

```python
import os
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotFilterType
input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"
if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)
# Load the existing workbook that contains the pivot table
workbook = ac.Workbook(input_path)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
date_field = pivot_table.row_fields[0]
# Define the date criterion for the Between filter
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
# Apply the date filter on the pivot field
date_field.filter_by_date(PivotFilterType.DATE_BETWEEN, start_date, end_date)
# Refresh and recalculate the pivot table so the filter takes effect
pivot_table.pivot_cache.refresh()
# Persist the workbook
workbook.save(output_path)
```

## **Değer Filtresi**
Değer filtreleri, bir pivot tablosunun veri alanında hesapladığı toplam değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değeriyle karşılaştırır. Tipik kullanım durumları arasında yalnızca satış toplamı bir hedef tutarı aşan ürünleri veya yalnızca işlem sayısı bir aralık içinde olan bölgeleri göstermek yer alır.
Aspose.Cells, değer filtrelemeyi `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)` yöntemi aracılığıyla sunar. `PivotFilterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. `value_field` parametresi, hangi veri alanının değerlendirileceğini belirtir ve son bağımsız değişken(ler) eşik değerini/değerlerini sağlar.
Aşağıdaki örnek, pivot tablo içeren bir çalışma kitabını yükler, yalnızca toplam satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFilterType
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]
row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
data_field_index = -1
for i in range(len(pivot_table.data_fields)):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break
if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, PivotFilterType.VALUE_GREATER_THAN, 5000.0, float('inf'))
pivot_table.pivot_cache.refresh()
workbook.save("output.xlsx")
```

## **İlk 10 Filtresi**
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan özel bir değer filtresi biçimidir. "Gelire göre ilk 10 ürün" veya "Satış sayısına göre en düşük 5 bölge" gibi sıralama raporları için yaygın olarak kullanılır.

{{% alert color="primary" %}}
İlk 10 filtresi, yalnızca pivot tablosunun veri alanında bir veya daha fazla değer pivot alanı olduğunda etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplam bir ölçü yoktur ve filtre uygulanamaz.
Aspose.Cells, Top 10 filtrelemesini `PivotField.filter_top10(value_field_index, filter_type, is_top, item_count)` yöntemi üzerinden sunar. `value_field_index` parametresi, öğelerin sıralandığı birleşik değerlere sahip veri alanının dizinidir, `filter_type` `item_count` birimini seçer (`PivotFilterType.COUNT` sabit sayıda öğe tutar, `PivotFilterType.PERCENT` öğelerin bir yüzdesini tutar, bu nedenle `item_count` yüzdenin kendisidir), `is_top` üst öğelerin (True) mi alt öğelerin mi (False) tutulacağını belirtir ve `item_count` kaç öğenin veya hangi yüzdenin tutulacağını tanımlar.
Aşağıdaki örnek, bir değer alanı içeren pivot tabloya sahip bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için bir ilk 10 filtresi uygular, pivot tablosunu yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivotTable = worksheet.pivot_tables[0]
# Confirm there is at least one value PivotField in the data area
if len(pivotTable.data_fields) == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.row_fields[0]
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filter_top10(valueFieldIndex, acp.PivotFilterType.COUNT, True, 10)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.pivot_cache.refresh()
# Save the workbook
workbook.save(outputPath)
```

## **Pivot Öğelerini Gizleyerek veya Görünür Hale Getirerek Filtreleme**
Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir pivot öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField`'in `PivotItems` koleksiyonunda yineleme yaparak ve `is_hidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `is_hidden = True` ayarı, öğeyi pivot tablodan gizler; `is_hidden = False` ayarı onu görünür hale getirir ve tekrar görünür kılar.
Bu yaklaşım, filtreleme kuralı düzensiz veya öğeye özgü olduğunda kullanışlıdır; örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlemek gibi. Aşağıdaki örnek bir pivot tabloyu yükler, ada göre belirli bir öğeyi gizler, onu görünür hale getirmeyi gösterir, pivot tablosunu yeniler ve çalışma kitabını kaydeder.

```python
import aspose.cells as ac
# Load an existing workbook containing a pivot table
workbook = ac.Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.worksheets[0]
# Access the pivot table by index (the first pivot table on the sheet)
pivot_table = sheet.pivot_tables[0]
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivot_field = pivot_table.row_fields[0]
# Iterate through the PivotItems collection of the selected PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]
    # Hide pivot items that match a specific name/criterion
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.name == "Item3":
        item.is_hidden = False
# Refresh and recalculate the pivot table so changes take effect
pivot_table.pivot_cache.refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
```

## **Özet**
Aspose.Cells for Python via .NET, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir pivot tablo filtreleme özellikleri seti sağlar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsarken, ilk 10 filtresi sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.is_hidden` özelliği esnek, öğe düzeyinde bir yedek sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas hedefli pivot tablo raporları oluşturmanıza olanak tanır.

{{< app/cells/assistant language="python-net" >}}