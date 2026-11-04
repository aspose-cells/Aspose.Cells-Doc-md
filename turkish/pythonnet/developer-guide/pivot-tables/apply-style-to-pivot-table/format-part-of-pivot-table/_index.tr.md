---
title: Özet Tablosunun Bir Bölümünü Biçimlendirme
linktitle: Özet Tablosunun Bir Bölümünü Biçimlendirme
description: Özet tablo bölümünü Aspose.Cells for Python via .NET içinde, PivotTable.format aracılığıyla anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine stiller uygulayarak biçimlendirin; biçimler PivotTable.pivot_formats içinde saklanır ve özet tablo yenilendiğinde korunur.
keywords: Aspose.Cells for Python via .NET, özet tablo, biçim, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /tr/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.format_all` tüm özet tabloya tek bir stil uygular ve üst sayfada açıklanmıştır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.
Pratikte, bir özet tablonun yalnızca bir kısmının öne çıkması gerekir. Yaygın hedefler arasında bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, toplam satırı veya ilk iki öğe satırı gibi keyfi bir dikdörtgen bulunur.
Özet tablo hücrelerine doğrudan stil uygulamak aynı şey değildir. Excel, özet‑tablo biçimlendirmesini sıradan hücre‑stili kayıtları yerine anlamsal `PivotArea` bölgeleri olarak depolar. Bir pivot‑alan biçimi, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve özet tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde tekrar çözülür. Öte yandan doğrudan bir hücreye yazılan stil, o hücre konumuna aittir ve özet tablo modeli tarafından izlenmez.
Aspose.Cells, her iki biçimlendirme türünün de kullanılabilmesi için tam `PivotTable.format` aşırı yükleme ailesini sunar:
- `format(PivotArea, Style)` bir stil'i `PivotArea.select` veya `PivotArea.select_field` ile oluşturulan anlamsal bir bölgeye bağlar.
- `format(CellArea, Style)` bir stil'i özet tablo içindeki bir çalışma sayfası dikdörtgenine bağlar.
- `format(int row, int column, Style)` tek bir hücreyi hedef alır.
- `format_all(Style)` tüm özet tabloyu biçimlendirir.

## **Pivot Alanını Biçimlendirme**
Anlamsal alan iş akışı, vurgunun bir alana veya rapor bölgesine bağlı kalması gerektiğinde önerilen yaklaşımdır.
1. `PivotArea(pivot_table)` ile bir `PivotArea` oluşturun. Nesne, o belirli özet tabloya ait anlamsal bir bölgeyi tanımlar.
1. Belirli bir eksende sıfır tabanlı konumuna göre bir alanı `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)` ile seçin.
   - `PivotTableSelectionType.DATA_AND_LABEL` hem alanın etiketlerini hem de verilerini seçer.
   - `PivotTableSelectionType.LABEL_ONLY` yalnızca alanın etiketlerini seçer.
   - `PivotTableSelectionType.DATA_ONLY` yalnızca alanın veri hücrelerini seçer.
1. Alanı adıyla `PivotArea.select_field(PivotFieldType axis_type, string field_name)` ile seçin. Bir satır alanı adla seçildiğinde, bölge o alanın öğeleri tarafından üretilen değer hücrelerine çözülür.
1. `Workbook.create_style()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `PivotTable.format(area, style)` metoduna geçirin.
1. `PivotArea` aşırı yüklemesine yapılan her çağrı, `PivotTable.pivot_formats` içine bir `PivotTableFormat` girdisi ekler.
1. Alan‑bağlantılı biçimler, özet veri hesaplandığında uygulanır. Bu nedenle, stillerin görünür olması için biçimleri uyguladıktan sonra `PivotTable.calculate_data()` çağrısı yapın.
Aşağıdaki örnek, küçük bir meyve‑satış özet tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.select` ve `PivotTableSelectionType.LABEL_ONLY` ile, aynı satır alanı tarafından üretilen değer hücrelerini `PivotArea.select_field` ile biçimler ve ardından özet tabloyu yeniden hesaplayarak her iki stilin de uygulanmasını sağlar.

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **Özet Tablosunun Hücre Alanını Biçimlendirme**
İlgili bölge basit bir çalışma sayfası dikdörtgeni olduğunda ve anlamsal bir özet tablo bölgesi olmadığında `PivotTable.format(CellArea, Style)` kullanın.
`CellArea`, `start_row`, `start_column`, `end_row` ve `end_column` özellikleriyle tanımlanır. Değerler sıfır tabanlı çalışma sayfası koordinatlarıdır ve son koordinatlar dikdörtgenin dahil edildiği son satır ve sütunu gösterir; böylece alan, başlangıç konumundan son konuma kadar tüm hücreleri kapsar.
Alan‑bağlantılı bir biçimden farklı olarak, bir `CellArea` biçimi hücrelere anında uygulanır. Stilin görünmesi için ikinci bir `calculate_data()` çağrısına gerek yoktur.
Bir `CellArea` dikdörtgeni etiket hücreleri ve değer hücrelerini birlikte içerebilir. Sonraki bölüm, Aspose.Cells ve Excel'in bu dikdörtgeni dahili olarak nasıl temsil ettiğini açıklar.
Aşağıdaki örnek, özet tablosunun `E4:F5` dikdörtgenini eğik, açık‑mavi bir stil ile biçimler ve çalışma kitabını daha fazla yeniden hesaplama yapmadan kaydeder.

```python
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **Pivot Alanları ve Hücre Alanları Nasıl Eşlenir**
Excel, özet‑tablo biçimlendirmesini sıradan çalışma sayfası hücre‑stili kayıtları yerine `pivotArea` kayıtları olarak depolar. Aynı model Aspose.Cells tarafından da kullanılır; böylece bir biçimlendirme isteği kaydedildiğinde özet alanlarına dönüştürülür.
Kullanıcı tarafından sağlanan `CellArea` ile dahili olarak depolanan özet alanları arasındaki ilişki iki yönde çok‑çok'tür.
- Bir `CellArea` birden fazla özet alanı üretebilir. Dikdörtgen hem etiket hücrelerini hem de değer hücrelerini kapsıyorsa, özet modeli etiket biçimlendirmesi ile veri biçimlendirmesini bağımsız olarak ele aldığı için ayrı etiket ve veri kurallarına ayrılır.
- Bir özet alanı birden fazla ayrı `CellArea` örneğine çözülebilir. Toplam satırı gibi anlamsal bir bölge veya öğeleri bitişik olmayan bir alan, birden çok dikdörtgeni kapsayabilir. Bu yüzden `PivotArea.get_cell_areas()` tek bir dikdörtgen yerine bir koleksiyon döndürür.
`PivotTable.format` aracılığıyla gerçekleştirilen her biçim işlemi `PivotTable.pivot_formats` içinde kaydedilir. Her `PivotTableFormat` girdisi ilişkili `PivotArea` ve ona uygulanan `Style`ı gösterir. `PivotArea` aşırı yüklemesi her çağrı için tam olarak bir girdi eklerken, farklı anlamsal bölgeler içeren bir `CellArea` birden fazla girdi ekleyebilir.
Depolanan bölgeleri ayırt etmek için her `PivotArea` `only_label` ve `only_data` bayraklarını ortaya çıkarır. Aşağıdaki örnek, hem etiketleri hem de değerleri kapsayan tek bir dikdörtgeni biçimler, `PivotTable.pivot_formats` içeriğini inceler ve her depolanmış özet alanının çözüldüğü `CellArea` koordinatlarını yazdırır.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
Biçimler sıradan hücre stilleri yerine özet alanları olarak saklandığı için yeniden hesaplama ve yenileme sonrasında korunur. Özet tablo `PivotTable.refresh_data` ile yenilendiğinde, `calculate_data` ile yeniden hesaplandığında veya kaydedilip tekrar yüklendiğinde, her depolanmış özet alanı bölgesinin mevcut konumuna yeniden çözülür ve stili yeniden uygulanır.
{{% /alert %}}

Bir vurgunun yenilemeler boyunca bir alana veya anlamsal bir bölgeye bağlı kalması gerektiğinde `select` veya `select_field` ile oluşturulmuş bir `PivotArea` kullanın; mevcut özet‑tablo düzeninde sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda bir `CellArea` kullanın. Tek hücre için `format(int row, int column, Style)` aşırı yüklemesi bir bireysel hücreyi hedef alır. Tüm özet tabloyu bir kerede yeniden stillendirmek istediğinizde, üst sayfada ele alınan `format_all` metodunu kullanın.

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-net/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/python-net/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}