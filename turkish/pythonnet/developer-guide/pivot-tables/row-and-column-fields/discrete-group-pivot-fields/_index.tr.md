---
title: Pivot Alanı Öğelerinin Ayrık Gruplandırılması
linktitle: Ayrık Gruplandırılması
description: Pivot alanı öğelerinin Aspose.Cells for Python via .NET içinde DiscreteGroupItem ve pivot_field_group_options.discrete_group_items kullanılarak meyve ve sebzeler gibi özel adlandırılmış gruplar halinde nasıl gruplandırılacağını öğrenin.
keywords: Aspose.Cells for Python via .NET, özet tablo, ayrık gruplandırma, DiscreteGroupItem, PivotFieldGroupOptions, pivot öğelerini gruplandırma, özel gruplar, PivotField.group, Python, Excel özet tablo
type: docs
weight: 90
url: /tr/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Otomatik gruplandırma, öğeleri veri türüne göre toplar; örneğin tarihleri aylara ve çeyreklere veya sayıları aralıklara dönüştürür. Ayrık gruplandırma ise bunun tersini yapar: belirli ve birbirleriyle ilişkisiz öğeleri özel adlandırılmış gruplarda toplar; örneğin ürünleri meyve ve sebze, mağazaları bölge veya hesapları bölge gruplarına ayırır. Aspose.Cells, ayrık gruplandırmayı `DiscreteGroupItem` sınıfı ve `pivot_field_group_options.discrete_group_items` özelliğiyle sağlar.
- `DiscreteGroupItem` bir grup adı ve bu gruba ait öğelerden oluşur. Öğeler iki şekilde belirlenebilir: adlarıyla (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) veya kaynak verideki sıfır tabanlı konumlarıyla (`DiscreteGroupItem("fruit", [0, 3])`). Her iki biçim de aynı sonucu verir.
- Ayrık gruplandırma, seçenekler `pivot_field.group(PivotFieldGroupOptions)` çağrısına geçirilerek özet tablosunun satır veya sütun alanındaki bir alana uygulanır.

## **Pivot Alanı Öğelerini Öğe Adlarına Göre Gruplandırma**
Aşağıdaki örnek küçük bir satış listesi (ürün, tarih ve tutar) oluşturur ve bundan `product` alanını satır alanında, `date` alanını sütun alanında ve `amount` alanını veri alanında içeren bir özet tablosu oluşturur. Ardından öğe adlarına göre iki özel grup tanımlar: `fruit` (`grape`, `cherry`) ve `vegetables` (`carrot`, `potato`). Bu sonuç, dış düzeyde grup adının ve altında özgün öğelerin iç içe yerleştirildiği iki düzeyli bir satır düzeni gösterir. Böylece eğilimler özel grup ve öğe bazında değerlendirilebilir.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

`calculate_data()` çağrısından sonra özet tablosunun satır alanında `fruit` (`grape` 50, `cherry` 80) ve `vegetable` (`carrot` 60, `potato` 70) ile genel toplam 260 görülür. Sütun etiketlerinde dört tarih (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) korunur.

## **Pivot Alanı Öğelerini Öğe Dizinlerine Göre Gruplandırma**
Öğe adları uzun veya yerelleştirilmiş olduğunda, `DiscreteGroupItem` sınıfının ikinci kurucusu öğeleri dizinle tanımlar. Dizinler, öğelerin kaynak veride göründükleri sıraya göre sıfır tabanlı konumlarıdır; alfabetik sıralamayı yansıtmaz. Yukarıdaki örnek veride `grape` 0, `carrot` 1, `potato` 2 ve `cherry` 3 numaralı öğeler olduğundan `fruit` `{ 0, 3 }`, `vegetable` ise `{ 1, 2 }` olur. Sonuç, ada dayalı örnekle aynıdır.

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **Not**

{{% alert color="primary" %}}
- Herhangi bir özel gruba atanmayan öğeler kaybolmaz. Bu öğeler, özet tablosunda özel gruplarla aynı düzeyde kalır ve her biri kendi tek öğelik girişi olarak görünür. Yukarıdaki örnekte yalnızca `fruit` grubu tanımlanırsa `carrot` ve `potato`, `fruit` grubunun yanında bağımsız girişler olarak satır alanında kalır.
- `pivot_field_group_options.new_pivot_field` özelliği, ayrık gruplandırmanın düzenini denetler. Varsayılan değeri `True` olan bu özellik, gruplandırılan alanı özgün alanın yanında yeni bir dış alan olarak ekleyerek yukarıda gösterilen iki düzeyli düzeni oluşturur (`row_fields` sayısı 2 olur). Bu özellik `False` olarak ayarlanırsa özgün alanın yerini alır; bu durumda satır alanı, yalnızca grup adlarını ve toplanmış değerlerini içeren tek düzeyli bir alan gösterir: `fruit` 130 (50 + 80) ve `vegetable` 130 (60 + 70).
- `DiscreteGroupItem` sınıfının ada ve dizine dayalı kurucuları aynı `discrete_group_items` listesi içinde birlikte kullanılabilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Alanlarını Özet Tablosunda Gruplandırma](/cells/tr/python-net/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-net/pivot-table-add-row-and-column-fields/)
- [Özet Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/python-net/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Biçimlendirme Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}