---
title: PivotField Öğelerinin Ayrık Gruplandırılması
linktitle: Ayrık Gruplandırılması
description: Java üzerinden Aspose.Cells for Python ile DiscreteGroupItem ve PivotFieldGroupOptions.getDiscreteGroupItems kullanılarak meyve ve sebze gibi özel adlandırılmış gruplara PivotField öğelerinin nasıl gruplandırılacağını öğrenin.
keywords: Aspose.Cells, özet tablo, ayrık gruplandırma, DiscreteGroupItem, PivotFieldGroupOptions, özet tablosu öğelerini gruplandırma, özel gruplar, PivotField.group, Java üzerinden Python, Excel özet tablo
type: docs
weight: 90
url: /tr/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Otomatik gruplandırma, öğeleri veri türüne göre toplar; örneğin tarihleri aylara ve çeyrelere, sayıları ise aralıklara dönüştürür. Ayrık gruplandırma ise bunun tam tersi bir sorunu çözer: belirli ve birbiriyle ilgisiz öğeleri meyve ve sebze gibi özel adlandırılmış gruplarda toplar; ürünleri meyve ve sebze gruplarına, mağazaları bölgelere veya hesapları bölümlere ayırır. Aspose.Cells, `DiscreteGroupItem` sınıfı ve `PivotFieldGroupOptions.getDiscreteGroupItems()` yöntemi aracılığıyla ayrık gruplandırma sağlar.
- Bir `DiscreteGroupItem`, bir grup adı ve o gruba ait öğelerden oluşur. Öğeler iki şekilde belirlenebilir: adlarıyla (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) veya kaynak verideki sıfırdan başlayan konumlarıyla (`DiscreteGroupItem("fruit", [0, 3])`). Her iki biçim de aynı sonucu verir.
- Ayrık gruplandırma, seçenekler `PivotField.group(PivotFieldGroupOptions)` aracılığıyla iletilerek özet tablosunun satır veya sütun alanlarındaki bir özet alanına uygulanır.

## **PivotField Öğelerini Öğe Adlarına Göre Gruplandırma**
Aşağıdaki örnekte küçük bir satış listesi (ürün, tarih ve tutar) oluşturulur ve bu listeden bir özet tablo hazırlanır. Özet tabloda `product` satır alanına, `date` sütun alanına ve `amount` veri alanına eklenir. Ardından öğe adlarına göre iki özel grup tanımlanır: meyve (`grape`, `cherry`) ve sebze (`carrot`, `potato`). Sonuç, iki düzeyli bir satır düzeni gösterir: dış düzeyde grup adı, altında ise özgün öğeler iç içe yerleştirilir. Böylece eğilimler özel grup ve öğe bazında incelenebilir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

`calculateData()` çağrısından sonra özet tablosunun satır alanında meyve (`grape` 50, `cherry` 80) ve sebze (`carrot` 60, `potato` 70) gösterilir; genel toplam 260'dır. Sütun etiketlerinde dört tarih (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) korunur.

## **PivotField Öğelerini Öğe İndekslerine Göre Gruplandırma**
Öğe adları uzun veya yerelleştirilmiş olduğunda, `DiscreteGroupItem` sınıfının ikinci kurucusu öğeleri indekslerle belirler. İndeksler, öğelerin kaynak veride göründükleri sıradaki sıfırdan başlayan konumlarıdır; alfabetik sıra değildir. Yukarıdaki örnek veride `grape` öğesinin indeksi 0, `carrot` öğesinin indeksi 1, `potato` öğesinin indeksi 2 ve `cherry` öğesinin indeksi 3'tür. Dolayısıyla meyve grubu `{ 0, 3 }`, sebze grubu ise `{ 1, 2 }` indekslerini içerir. Sonuç, öğe adına dayalı örnekle aynıdır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **Not**

{{% alert color="primary" %}}
- Hiçbir özel gruba atanmayan öğeler kaybolmaz. Bunlar özet tablosunda özel gruplarla aynı düzeyde kalır ve her biri tek öğeden oluşan ayrı bir kayıt olarak görünür. Yukarıdaki örnekte yalnızca meyve grubu tanımlanırsa `carrot` ve `potato`, satır alanında meyve grubunun yanında bağımsız kayıtlar olarak kalır.
- `PivotFieldGroupOptions.getNewPivotField()` ve `setNewPivotField()` yöntemleri ayrık gruplandırmanın düzenini belirler. `getNewPivotField()` varsayılan olarak true değerini alır; bu, gruplandırılan alanı özgün alanın yanında yeni bir üst alan olarak ekleyerek yukarıda gösterilen iki düzeyli düzeni oluşturur (`getRowFields()` ile alınan alan sayısı 2 olur). `setNewPivotField(false)` kullanarak özgün alanı değiştirin; bu durumda satır alanı yalnızca grup adlarını ve toplanan değerlerini içeren tek düzeyli bir yapı gösterir: meyve 130 (50 + 80) ve sebze 130 (60 + 70).
- `DiscreteGroupItem` sınıfının ada dayalı ve indeks dayalı kurucuları, aynı `getDiscreteGroupItems()` koleksiyonu içinde birlikte kullanılabilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablosunda Özet Alanlarını Gruplandırma](/cells/tr/python-java/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-java/pivot-table-add-row-and-column-fields/)
- [Etikete veya Değere Göre Özet Tablolarını Filtreleme](/cells/tr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}