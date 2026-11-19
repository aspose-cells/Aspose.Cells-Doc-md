---
title: Pivot Tablolarını Etiket veya Değere Göre Filtreleme
description: Aspose.Cells for Python via Java, kapsamlı özet tablo filtreleme yeteneklerini destekler. Bu makale, özet tablo verilerini etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri kullanarak ve özet öğeleri gizleyerek veya göstererek nasıl filtreleyeceğinizi açıklar.
linktitle: Pivot Tablolarını Etiket veya Değere Göre Filtreleme
keywords: Aspose.Cells, Python via Java kitaplığı, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet öğe, özet öğeyi gizle
type: docs
weight: 10
url: /tr/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir özet tablosunda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde tarih filtreleri kullanabilir, toplama sayılarına karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtreleri kullanabilir veya `is_hidden` özelliğini kullanarak tek tek özet öğeleri manuel olarak gizleyebilir ve gösterebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıfları üzerindeki özel API'ler aracılığıyla kullanıma sunulur.
{{% /alert %}}

## **Giriş**
Özet tablolar güçlü analitik araçlardır, ancak ham özetler genellikle sunmanız gereken bilgilerden çok daha fazlasını içerir. Filtreleme, özet tablosunu belirli bir rapor için önemli olan satır, sütun veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for Python via Java, Microsoft Excel'de bulunan filtreleme yeteneklerini yansıtır ve bunları programatik olarak sunarak rapor oluşturmanın tamamen otomatikleştirilmesini sağlar.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boş değerler) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplama değerlerine göre filtreler.
4. **İlk 10 Filtresi** — yalnızca bir değer alanına göre sıralanmış en yüksek veya en düşük N öğeyi gösterir.
5. **Özet Öğeleri Gizleme / Gösterme** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.
Her yaklaşım, `PivotField` sınıfı üzerinde farklı bir yöntem veya `PivotItem` sınıfı üzerinde bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tablosunda `refresh_data()` ve `calculate_data()` çağırmalısınız.

## **Etiket Filtresi**
Etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir desenle karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı ölçüte uyan ürünleri görüntülemek istediğinizde kullanışlıdır.
Aspose.Cells, etiket filtrelemeyi `PivotField.filter_by_label(PivotFilterType, str)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` gibi değerler içerir. İkinci bağımsız değişken, karşılaştırma için kullanılan etiket dizesini sağlar.
Aşağıdaki örnek, mevcut bir özet tablosu içeren bir çalışma kitabını yükler, yalnızca başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, özet tablosunu yeniler ve sonucu kaydeder.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the first row PivotField
rowField = pivotTable.getRowFields().get(0)
# Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook back to disk
workbook.save(fileName)
jpype.shutdownJVM()
```

## **Tarih Filtresi**
Tarih filtreleri, bir özet tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı ölçütlerle daraltmanıza olanak tanır. Bunlar, yalnızca tarih-saat bilgilerini depolayan alanlara karşı çalışan özel filtrelerdir.

{{% alert color="primary" %}}
Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alan sayılar veya metin gibi başka veri türleri içeriyorsa, tarih filtresi beklenen sonucu üretmeyecektir. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.
Aspose.Cells, tarih filtrelemeyi `PivotField.filter_by_date(PivotFilterType, values)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak bir veya iki `DateTime` değeri geçirirsiniz (`Between` için başlangıç ve bitiş tarihlerini geçirirsiniz).
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan bir özet tablosu içeren bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"
if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")
# Load the existing workbook that contains the pivot table
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
dateField = pivotTable.getRowFields().get(0)
# Define the date criterion for the Between filter
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)
# Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate)
# Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh()
# Persist the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Değer Filtresi**
Değer filtreleri, bir özet tablosunun veri alanında hesapladığı toplama değerleri üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşik değeriyle karşılaştırırlar. Tipik kullanım örnekleri arasında yalnızca satış toplamı bir hedef tutarı aşan ürünleri veya işlem sayısı belirli bir aralıkta olan bölgeleri göstermek yer alır.
Aspose.Cells, değer filtrelemeyi `PivotField.filter_by_value(value_field, filter_type, values)` yöntemi aracılığıyla sunar. `filter_type` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. `value_field` parametresi hangi veri alanının değerlendirileceğini belirtir ve son bağımsız değişken(ler) eşik değerini sağlar.
Aşağıdaki örnek, bir özet tablosu içeren bir çalışma kitabını yükler, yalnızca toplama satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFilterType
workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)
rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break
if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))
pivotTable.getPivotCache().refresh()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **İlk 10 Filtresi**
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan, özel bir değer filtresi biçimidir. Genellikle "gelire göre ilk 10 ürün" veya "satış sayısına göre en düşük 5 bölge" gibi sıralama raporları için kullanılır.

{{% alert color="primary" %}}
İlk 10 filtresi yalnızca özet tablosunun veri alanında bir veya daha fazla değer pivot alanı varsa etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplama bir ölçü yoktur ve filtre uygulanamaz.
Aspose.Cells, Top 10 filtrelemesini `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)` yöntemi üzerinden sunar. `valueFieldIndex` parametresi, öğelerin sıralandığı birleşik değerlere sahip veri alanının dizinidir, `filterType` `itemCount` birimini seçer (`PivotFilterType.COUNT` sabit sayıda öğe tutar, `PivotFilterType.PERCENT` öğelerin bir yüzdesini tutar, bu nedenle `itemCount` yüzdenin kendisidir), `isTop` üst öğelerin (true) mi alt öğelerin mi (false) tutulacağını belirtir ve `itemCount` kaç öğenin veya hangi yüzdenin tutulacağını tanımlar.
Aşağıdaki örnek, bir değer alanı içeren bir özet tablosu bulunan bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için ilk 10 filtresi uygular, özet tablosunu yeniler ve çalışma kitabını kaydeder.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Confirm there is at least one value PivotField in the data area
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.getRowFields().get(0)
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.SUM
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, True, 10)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Özet Öğeleri Gizleyerek veya Göstererek Filtreleme**
Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir özet öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField` öğesinin `PivotItems` koleksiyonunda dolaşarak ve `is_hidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `is_hidden = True` ayarı, öğeyi özet tablosundan gizler; `is_hidden = False` ayarı ise öğeyi gösterir ve tekrar görünür hale getirir.
Bu yaklaşım, filtreleme kuralının düzensiz veya öğeye özgü olduğu durumlarda kullanışlıdır; örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlemek gibi. Aşağıdaki örnek, bir özet tablosu yükler, ada göre belirli bir öğeyi gizler, nasıl gösterileceğini gösterir, özet tablosunu yeniler ve çalışma kitabını kaydeder.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem
# Load an existing workbook containing a pivot table
workbook = Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.getWorksheets().get(0)
# Access the pivot table by index (the first pivot table on the sheet)
pivotTable = sheet.getPivotTables().get(0)
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivotField = pivotTable.getRowFields().get(0)
# Iterate through the PivotItems collection of the selected PivotField
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)
    # Hide pivot items that match a specific name/criterion
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setHidden(True)
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.getName() == "Item3":
        item.setHidden(False)
# Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
jpype.shutdownJVM()
```

## **Özet**
Aspose.Cells for Python via Java, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir özet tablo filtreleme özellikleri seti sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsar; ilk 10 filtresi ise sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `PivotItem.is_hidden` özelliği esnek, öğe düzeyinde bir geri dönüş seçeneği sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas şekilde hedeflenmiş özet tablo raporları oluşturmanıza olanak tanır.

{{< app/cells/assistant language="python" >}}