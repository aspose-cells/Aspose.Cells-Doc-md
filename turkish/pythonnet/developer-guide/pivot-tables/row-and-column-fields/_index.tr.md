---
title: Aspose.Cells for Python via .NET'te PivotTable'a satır ve sütun alanları ekleme
description: Aspose.Cells for Python via .NET'te pivot tablonun satır ve sütun bölgelerine temel alanların nasıl ekleneceğini ve PivotField.set_subtotals kullanılarak pivot alanı ara toplamlarının nasıl denetleneceğini öğrenin.
linktitle: Satır ve Sütun Alanları
keywords: Aspose.Cells, Python via .NET, özet tablo, satır alanı, sütun alanı, PivotField, set_subtotals, PivotFieldSubtotalType, ara toplamlar
type: docs
weight: 220
url: /tr/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Satır veya Sütun Bölgesine Alan Ekleme**
`PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` yöntemi, kaynak verilerden bir temel alanı dört pivot bölgesinden birine taşır. `field_type` bağımsız değişkeni, aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.
- `ROW` — sol tarafa dikey olarak yerleştirilen alanlar
- `COLUMN` — en üste yatay olarak yerleştirilen alanlar
- `DATA` — değerlerinin toplandığı alanlar
- `PAGE` — rapor filtreleri olarak kullanılan alanlar
Alanlar eklendikten sonra, `PivotTable.row_fields` ve `PivotTable.column_fields` özellikleri aracılığıyla bunlara erişebilirsiniz. Her özellik bir `PivotFieldCollection` döndürür. `row_fields` koleksiyonunun 0 dizinindeki alan en dıştaki satır alanıdır ve sonraki dizinler onun içine yerleştirilmiş alanları temsil eder. Aynı dizin kuralı `column_fields` için de geçerlidir.
Alan iç içe yerleştirme sırası önemlidir. Önce `Category` alanını satır bölgesine, ardından `Item` alanını eklemek, dış gruplaması `Category` ve iç gruplaması `Item` olan bir pivot tablo üretir. Sırayı tersine çevirmek hiyerarşiyi de tersine çevirir.

## **Pivot Alanı Ara Toplamları**
`PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` yöntemi, bir pivot alanı için hangi ara toplam satırlarının görüneceğini denetler. Her çağrı tek bir ara toplam türünü bağımsız olarak değiştirir. `shown = True` geçildiğinde ara toplam görüntülenir, `shown = False` geçildiğinde ise gizlenir. Her çağrı yalnızca bir türü etkilediğinden, yöntemin farklı `subtotal_type` değerleriyle birden çok kez çağrılması özel bir ara toplam alt kümesi oluşturur.
`PivotFieldSubtotalType` numaralandırması kullanılabilir ara toplam türlerini tanımlar.
- `AUTOMATIC` — Aspose.Cells varsayılan seçimi seçer (genellikle sayısal alanlar için `SUM`)
- `NONE` — tüm ara toplam satırlarını bastırır
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Ara toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla pivot alanı olduğunda görüntülenir. Tek bir alanın ara toplam oluşturacak anlamlı bir şeyi yoktur, bu nedenle bu durumda `set_subtotals` çağrılarının görünür bir etkisi olmaz. Bu nedenle bu makale, her `Category` grubu arasındaki ara toplam sınırının görünür olması için her örnekte iki satır alanı (`Category` dış, `Item` iç) yerleştirir.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Ara Toplamlar**
`set_subtotals` yöntemini hiç çağırmadığınızda, Aspose.Cells sayısal alanlar için `AUTOMATIC` seçimini uygular. Aşağıdaki örnek, dış `Category` satır alanında `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` çağırarak bu davranışı açıkça doğrular.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get(0, 0).put_value("Category")
worksheet.cells.get(0, 1).put_value("Item")
worksheet.cells.get(0, 2).put_value("Year")
worksheet.cells.get(0, 3).put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **Senaryo 2 — Tüm Ara Toplamların Bastırılması (None)**
`set_subtotals(PivotFieldSubtotalType.NONE, True)` çağrısı pivot tablosundaki her ara toplam satırını kaldırır ve yalnızca alan satırları ile en altta genel toplamı bırakır. Bu, özet satırları olmadan ham gruplanmış verileri istediğinizde kullanışlıdır.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells.get(0, j).put_value(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
]
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells.get(i + 1, j).put_value(data[i][j])
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [PivotFieldSubtotalType.SUM, PivotFieldSubtotalType.COUNT, PivotFieldSubtotalType.AVERAGE, PivotFieldSubtotalType.MAX, PivotFieldSubtotalType.MIN, PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **Senaryo 3 — Özel Ara Toplam Alt Kümesi (Toplam + Ortalama)**
Tek bir ara toplam türüyle sınırlı değilsiniz. Her `set_subtotals` çağrısı bir tür üzerinde bağımsız olarak çalışır; bu nedenle yöntemi iki kez — bir kez `SUM` ve bir kez `AVERAGE` ile — çağırmak, her `Category` grubu için iki ara toplam satırından oluşan özel bir alt küme üretir.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get("A1").put_value("Category")
worksheet.cells.get("B1").put_value("Item")
worksheet.cells.get("C1").put_value("Year")
worksheet.cells.get("D1").put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **Özet**

Bu üç senaryo yalnızca `set_subtotals` çağrılarıyla farklılık gösterir. Diğer her şey — veri kümesi, alanlar ve bu alanların atanmış oldukları bölgeler — aynıdır, bu da düzenlerin doğrudan karşılaştırılabilir olmasını sağlar.
- **Alanların yerleştirilmesi.** `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` çağrısı, bir kaynak sütunu bir bölgeye taşır. Bir bölge içinde, çağrıların sırası görünüm sırasını belirler; bu nedenle ilk çağrı en dıştaki gruba Corresponds (karşılık gelir). Alt toplamlar için aynı bölgede iki veya daha fazla alan gerekir: tek bir alanla gruplar arasında alt toplam yapılacak bir şey bulunmaz.
- **Senaryo 1 — otomatik alt toplamlar.** `set_subtotals` çağrısının yapılmaması, seçimi Excel’e bırakır; Excel, sayısal alanlar için kendi varsayılan alt toplamını uygular. `PivotFieldSubtotalType.AUTOMATIC` ile `set_subtotals` çağrısı, bu seçimi açıkça kaydeder ve dolaylı bırakmaz.
- **Senaryo 2 — alt toplam yok.** `PivotFieldSubtotalType.NONE` ile `set_subtotals` çağrısı, varsayılan alt toplamı devre dışı bırakır; böylece özet tablo, satır alanlarını ve toplamı korur ama Excel'in aksi takdirde araya ekleyeceği alt toplam satırlarını siler.
- **Senaryo 3 — seçilmiş bir alt küme.** Her çağrı tam olarak bir alt toplam türünü açıp kapatır ve çağrılar birbirlerini sıfırlamak yerine birikir. Bu nedenle `PivotFieldSubtotalType.SUM` ile bir kez ve `PivotFieldSubtotalType.AVERAGE` ile bir kez çağrılması, her ikisini de etkinleştirir ve özet tablo bir Toplam alt toplamı, bir Ortalama alt toplamı ve bir toplam sunar.

{{% alert color="primary" %}}
Alt toplamlarla ilgili hiçbir şey satır bölgesine özeldir. `PivotTable.ColumnFields`’ten alınan bir alana aynı `set_subtotals` çağrılarının yapılması, sütun ekseninde aynı üç düzeni üretir, çünkü ayar, eksenin kendisinden ziyade özet alanına aittir.
{{% /alert %}}
## **İlgili Makaleler**

- [Pivot Tablolarında Sayfa Alanları](/cells/tr/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET ile Pivot Tabloları Yenileme](/cells/tr/python-net/refresh-pivot-table/)
- [Pivot Tablolarına Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python-net" >}}