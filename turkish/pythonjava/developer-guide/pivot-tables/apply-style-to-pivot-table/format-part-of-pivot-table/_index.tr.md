---
title: Pivot Tablosunun Bir Bölümünü Biçimlendirme
linktitle: Pivot Tablosunun Bir Bölümünü Biçimlendirme
description: Aspose.Cells for Python via Java kullanarak bir pivot tablosunun bir bölümünü, PivotTable.format aracılığıyla anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine stil uygulayarak biçimlendirin; biçimler PivotTable.getPivotFormats() içinde depolanır ve pivot tablo yenilendiğinde korunur.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, pivot tablo, biçim, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /tr/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.formatAll` tek bir stili tüm pivot tabloya uygular ve ana sayfada ele alınır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.  
Uygulamada, genellikle bir pivot tablonun sadece bir bölümü vurgulanması gerekir. Yaygın hedefler arasında bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, toplam satırı ve ilk iki öğe satırı gibi keyfi bir dikdörtgen bulunur.  
Bir pivot tablonun çalışma sayfası hücrelerine doğrudan stil uygulamak aynı şey değildir. Excel, pivot tablo biçimlendirmesini sıradan hücre stili kayıtları yerine anlamsal `PivotArea` bölgeleri olarak saklar.  
Pivot bölgesi biçimi, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve pivot tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde yeniden çözülür. Öte yandan, bir hücreye doğrudan yazılan stil o hücre konumuna ait olur ve pivot modeli tarafından izlenmez.  
Aspose.Cells, her iki biçimlendirme türünün de kullanılabilmesi için tamamen `PivotTable.format` aşırı yükleme ailesini sunar:
- `format(PivotArea, Style)` bir stili, `PivotArea.select` veya `PivotArea.selectField` ile oluşturulan anlamsal bir bölgeye bağlar.
- `format(CellArea, Style)` bir stili, pivot tablo içindeki bir çalışma sayfası dikdörtgenine bağlar.
- `format(int row, int column, Style)` tek bir hücreyi hedef alır.
- `formatAll(Style)` tüm pivot tabloyu biçimlendirir.

## **Pivot Alanını Biçimlendirme**
Anlamsal alan iş akışı, bir vurgunun bir alana veya rapor bölgesine bağlı kalması gerektiğinde önerilen yaklaşımdır.
1. `PivotArea(pivot_table)` ile bir `PivotArea` oluşturun. Nesne, belirli pivot tabloya ait bir anlamsal bölgeyi tanımlar.
1. `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` ile bir eksende sıfır tabanlı konumuna göre alan seçin.
   - `PivotTableSelectionType.DATA_AND_LABEL` hem alanın etiketlerini hem de verilerini seçer.
   - `PivotTableSelectionType.LABEL_ONLY` yalnızca alanın etiketlerini seçer.
   - `PivotTableSelectionType.DATA_ONLY` yalnızca alanın veri hücrelerini seçer.
1. `PivotArea.selectField(PivotFieldType axisType, String fieldName)` ile alanı adla seçin. Bir satır alanı adla seçildiğinde, bölge o alanın öğeleri tarafından üretilen değer hücrelerine çözülür.
1. `workbook.createStyle()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `PivotTable.format(area, style)` yöntemine iletin.
1. `PivotArea` aşırı yüklemesine yapılan her çağrı, `PivotTable.getPivotFormats()` içinde bir `PivotTableFormat` girdisi ekler.
1. Alan‑bağlantılı biçimler, pivot verileri hesaplandığında uygulanır. Bu nedenle, stillerin görünür olması için biçimleri uyguladıktan sonra `PivotTable.calculateData()` çağırın.  
Aşağıdaki örnek, küçük bir meyve‑satış pivot tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.select` ve `PivotTableSelectionType.LABEL_ONLY` ile biçimler, aynı satır alanı tarafından üretilen değer hücrelerini `PivotArea.selectField` ile biçimler ve ardından her iki stili de uygulamak için pivot tabloyu yeniden hesaplar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Pivot Tablosunun Hücre Alanını Biçimlendirme**
İlgili bölge basit bir çalışma sayfası dikdörtgeni olduğunda, `PivotTable.format(CellArea, Style)` kullanın; anlamsal bir pivot bölgesi değildir.  
Bir `CellArea`, `getStartRow()`, `getStartColumn()`, `getEndRow()` ve `getEndColumn()` özellikleriyle tanımlanır. Değerler sıfır tabanlı çalışma sayfası koordinatlarıdır ve son koordinatlar, dikdörtgen içinde dahil edilen son satır ve sütunu belirler; böylece bölge başlangıç konumundan son konuma kadar (dahil) hücreleri kapsar.  
Alan‑bağlantılı bir biçimlemenin aksine, bir `CellArea` biçimi hücrelere hemen uygulanır. Stil görünümü için başka bir `PivotTable.calculateData()` çağrısına gerek yoktur.  
Bir `CellArea` dikdörtgeni etiket hücreleri ve değer hücrelerini birlikte içerebilir. Sonraki bölüm, Aspose.Cells ve Excel'in bu dikdörtgeni dahili olarak nasıl temsil ettiğini açıklar.  
Aşağıdaki örnek, pivot tablonun `E4:F5` dikdörtgenini italik, açık mavi bir stil ile biçimler ve çalışmayı daha fazla yeniden hesaplama yapmadan kaydeder.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    CellArea,
    PivotFieldType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **Pivot Alanları ve Hücre Alanları Nasıl Eşlenir**
Excel, pivot tablo biçimlendirmesini sıradan çalışma sayfası hücre‑stili kayıtları yerine `pivotArea` kayıtları olarak saklar. Aynı model Aspose.Cells tarafından da kullanılır; böylece bir biçimlendirme isteği kaydedildiğinde pivot alanlarına dönüştürülür.  
Kullanıcının sağladığı `CellArea` ile dahili olarak saklanan pivot alanları arasındaki ilişki iki yönde çok‑tan‑çoğa bir bağdır.  
- Tek bir `CellArea` birden fazla pivot alanı üretebilir. Dikdörtgen hem etiket hem de değer hücrelerini kapsıyorsa, etiket ve veri kurallarına ayrı ayrı bölünür; çünkü pivot modeli etiket biçimlendirmesini veri biçimlendirmesinden bağımsız olarak ele alır.  
- Tek bir pivot alanı birden çok ayrık `CellArea` örneğine çözülebilir. Toplam satır gibi bir anlamsal bölge ya da öğeleri kesintili bir alan, birden çok dikdörtgeni kapsayabilir. Bu nedenle `PivotArea.getCellAreas()` tek bir dikdörtgen yerine bir koleksiyon döndürür.  
`PivotTable.format` aracılığıyla gerçekleştirilen her biçim işlemi `PivotTable.getPivotFormats()` içinde kaydedilir. Her `PivotTableFormat` girdisi, ilgili `PivotArea` ve ona uygulanan `Style` öğesini gösterir. `PivotArea` aşırı yüklemesi her çağrı için tam bir giriş ekler, farklı anlamsal bölgeler içeren bir `CellArea` ise birden çok giriş ekleyebilir.  
Depolanan bölgeleri ayırt etmek için her `PivotArea`, `getOnlyLabel()` ve `getOnlyData()` bayraklarını sunar. Aşağıdaki örnek, hem etiketleri hem de değerleri kapsayan tek bir dikdörtgeni biçimler, `PivotTable.getPivotFormats()` inceleyerek her depolanmış pivot alanının çözdüğü `CellArea` koordinatlarını yazdırır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Biçimler, sıradan hücre stilleri yerine pivot alanları olarak saklandığı için yeniden hesaplama ve yenileme sonrası da korunur. Pivot tablo `PivotTable.refreshData()` ile yenilendiğinde, `PivotTable.calculateData()` ile yeniden hesaplandığında veya kaydedilip yeniden yüklendiğinde, her depolanmış pivot alanı bölgesinin mevcut konumuna yeniden çözülür ve stili yeniden uygulanır.
{{% /alert %}}

Bir vurgunun yenilemeler boyunca bir alana veya anlamsal bölgeye bağlı kalması gerektiğinde `select` veya `selectField` ile oluşturulmuş bir `PivotArea` kullanın; mevcut pivot‑tablo düzenindeki sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda bir `CellArea` kullanın. Tek hücre `format(int row, int column, Style)` aşırı yüklemesi tek bir hücreyi hedef alır. Tüm pivot tabloyu tek seferde yeniden stilize etmek istediğinizde, ana sayfada ele alınan `formatAll` yöntemini kullanın.

## **Related Articles**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-java/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/python-java/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}