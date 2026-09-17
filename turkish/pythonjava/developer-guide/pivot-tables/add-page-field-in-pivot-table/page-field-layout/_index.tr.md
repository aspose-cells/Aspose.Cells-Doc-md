---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for Python via Java kullanarak bir pivot tablosunda sayfa alanı düzenini nasıl kontrol edeceğinizi öğrenin; sayfa alanı filtre çubuğunun görüntülenme sırasını, kaydırma sayısını ve pivot tablonun üst kısmındaki sayfa alanlarının alan sırasını ayarlamayı kapsar.
keywords: Aspose.Cells for Python via Java, Python Java kütüphanesi, elektronik tablo, pivot tablosu, sayfa alanı, sayfa alanı sırası, sayfa alanı kaydırma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Sayfa alanı bölgesinin — pivot tablonun üst kısmındaki filtre kontrolleri şeridinin — düzenini, görüntüleme sırası, kaydırma sayısı ve alan yeniden sıralaması dahil nasıl kontrol edeceğinizi gösterir.
{{% /alert %}}

## **Introduction**
Microsoft Excel'deki bir pivot tablosu, tablonun satır/sütun/veri gövdesinin üzerinde konumlanan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, açılır filtre kontrollerinden oluşan bir şerit olarak (her sayfa alanı için bir tane) işlenir ve son kullanıcıların pivot tablosunu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells for Python via Java bu bölgeyi `pivot_table.page_fields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl düzenleneceğini kontrol eden üç özellik sunar:
- `pivot_table.page_field_order` (bir `Aspose.Cells.PrintOrderType` değeri) ek sayfa alanlarının mevcut alanların *yanına mı* yoksa *altına mı* yerleştirileceğine karar verir.
- `pivot_table.page_field_wrap_count` kaydırmadan önce her satır veya sütuna kaç sayfa alanı yerleştirileceğini ayarlar.
- `pivot_table.page_fields.move(curr_index, dest_index)` sıra modunu değiştirmeden sayfa alanlarını yeniden sıralar.
Bu makale, elde edilen düzenleri yan yana karşılaştırabilmeniz için her bir işlemi ortak bir veri kümesi üzerinde gösteren üç kod örneği boyunca ilerler.

## **Source Data**
| Meyve  | Yıl  | Bölge  | Tutar |
|--------|------|--------|-------|
| Elma   | 2022 | Kuzey  | 150   |
| Elma   | 2023 | Kuzey  | 180   |
| Muz    | 2022 | Güney  | 120   |
| Muz    | 2023 | Güney  | 140   |
| Kiraz  | 2022 | Doğu   | 200   |
| Kiraz  | 2023 | Doğu   | 220   |
| Üzüm   | 2022 | Batı   | 90    |
| Üzüm   | 2023 | Batı   | 110   |
Tüm sekiz satır her kod örneğinde, aynı sırada doldurulur; böylece kaynak veri senaryolar arasında asla farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri farklılık gösterir.

## **Example 1: Over Then Down**
İlk senaryoda, iki sayfa alanını (`Yıl`, `Bölge`) pivot tablonun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Meyve` alanını satır eksenine atıyoruz, `Yıl` alanını birinci, `Bölge` alanını ikinci sırada olacak şekilde sayfa eksenine yerleştiriyoruz (`add_field_to_area` çağrılarının sırası başlangıç indisini belirler), `Tutar` (Toplam) alanını veri alanı olarak ekliyoruz ve ardından `page_field_order` değerini `PrintOrderType.OVER_THEN_DOWN` ile `page_field_wrap_count = 2` olarak ayarlıyoruz. `OVER_THEN_DOWN` ve kaydırma sayısı 2 ile iki sayfa alanı pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana dizilir; dolayısıyla şerit genişliği iki olan tek bir satır kaplar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType
dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)
workbook = Workbook()
worksheets = workbook.getWorksheets()
pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()
# Headers (row 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")
# Row 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)
# Row 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)
# Row 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)
# Row 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)
# Row 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)
# Row 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)
# Row 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)
# Row 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)
# Add PivotTableReport sheet
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()
# Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)
# Add fields
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # Fruit
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # Year
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # Amount
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)
# Configure page field area layout: place page fields across first, wrap after every 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)
# Refresh and calculate
pivotTable.calculateData()
# Save
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))
jpype.shutdownJVM()
```

## **Example 2: Down Then Over**
Bu örnekte, Örnek 1'deki gibi `Meyve` alanını satır eksenine, `Yıl` ve `Bölge` alanlarını sayfa eksenine (`Yıl` birinci sırada) ve `Tutar` (Toplam) alanını veri alanı olarak yerleştiriyoruz. Ardından `page_field_order` değerini `PrintOrderType.DOWN_THEN_OVER`, `page_field_wrap_count` değerini ise `2` olarak ayarlıyoruz. `DOWN_THEN_OVER` ve kaydırma sayısı 2 ile iki sayfa alanı dikey olarak üst üste yığılır — `Yıl` üstte, `Bölge` doğrudan altında — pivot tablonun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine genişliği bir olan iki satır kaplar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType
workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)
headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])
data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]
for r in range(len(data)):
    for c in range(len(data[r])):
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])
idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)
pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)
pivotTable.calculateData()
workbook.save("pageFieldLayout_downThenOver.xlsx")
jpype.shutdownJVM()
```

## **Example 3: Move a Page Field**
Üçüncü senaryoda bu veri kümesini ve alan dağılımını koruyoruz, nötr bir düzen (`OVER_THEN_DOWN` ve kaydırma sayısı `2`) belirliyoruz ve ardından `page_fields.move` işlemini gösteriyoruz. `move(0, 1)` çağrısı, 0 indisindeki (`Yıl`) sayfa alanını 1 konumuna taşır ve 1 konumundaki (`Bölge`) sayfa alanı 0 konumuna kayar. Bu çağrıdan sonra `Bölge` birinci sayfa alanı, `Yıl` ise ikinci sayfa alanı olur. Kaydırma ve sıra modu değişmediğinden şerit yine yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiştir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType
workbook = Workbook()
dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")
dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")
dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)
dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)
dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)
dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)
dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)
dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)
dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)
dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)
pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)
pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)
pivotTable.getPageFields().move(0, 1)
pivotTable.calculateData()
workbook.save("pageFieldLayout_move.xlsx")
jpype.shutdownJVM()
```

## **Related Articles**
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/python-java/add-page-field-in-pivot-table/) — sayfa alanlarının pivot tablosuna nasıl ekleneceğini tanıtan ana sayfa.
- [Pivot Tablosunda Satır ve Sütun Alanları](/cells/tr/python-java/row-and-column-fields/) — alanların satır ve sütun eksenlerine atanmasını kapsar ve burada gösterilen sayfa ekseni çalışmasını tamamlar.
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/python-java/manage-value-fields/) — veri (değer) alanının nasıl yapılandırılacağını, bu makalede kullanılan `SUM` toplaması dahil açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/python-java/refresh-pivot-table/) — sayfa alanlarını yeniden sıraladıktan sonra gerekli olan `refresh_data` ve `calculate_data` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/) — sayfa alanı şeridi düzenlendikten sonra işlenmiş pivot tablosunun nasıl biçimlendirileceğini gösterir.

{{< app/cells/assistant language="python" >}}