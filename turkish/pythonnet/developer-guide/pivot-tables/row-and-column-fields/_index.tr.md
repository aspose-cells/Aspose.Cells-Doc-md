---
title: Aspose.Cells for Python via .NET'te Satır ve Sütun Alanları
linktitle: Satır ve Sütun Alanları
description: Aspose.Cells for Python via .NET'te pivot tablonun satır ve sütun bölgelerine temel alanların nasıl ekleneceğini ve PivotField.set_subtotals kullanılarak pivot alanı ara toplamlarının nasıl denetleneceğini öğrenin.
keywords: Aspose.Cells, Python via .NET, özet tablo, satır alanı, sütun alanı, PivotField, set_subtotals, PivotFieldSubtotalType, ara toplamlar
type: docs
weight: 220
url: /tr/python-net/row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Satır ve sütun alanları, bir pivot tablonun yapı taşlarıdır. Satır bölgesine yerleştirilen bir alan, pivot tablonun solunda dikey olarak görünürken, sütun bölgesine yerleştirilen bir alan ise en üstte yatay olarak görünür. Bu makale, bu bölgelere programlı olarak temel alanların nasıl ekleneceğini ve `PivotField.set_subtotals` yöntemi kullanılarak alan grupları arasında görüntülenen ara toplamların nasıl denetleneceğini gösterir.

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

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.AUTOMATIC, True)

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_automatic.xlsx")
```

## **Senaryo 2 — Tüm Ara Toplamların Bastırılması (None)**

`set_subtotals(PivotFieldSubtotalType.NONE, True)` çağrısı pivot tablosundaki her ara toplam satırını kaldırır ve yalnızca alan satırları ile en altta genel toplamı bırakır. Bu, özet satırları olmadan ham gruplanmış verileri istediğinizde kullanışlıdır.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

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
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
for st in [ac.PivotFieldSubtotalType.SUM, ac.PivotFieldSubtotalType.COUNT, ac.PivotFieldSubtotalType.AVERAGE, ac.PivotFieldSubtotalType.MAX, ac.PivotFieldSubtotalType.MIN, ac.PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_none.xlsx")
```

## **Senaryo 3 — Özel Ara Toplam Alt Kümesi (Toplam + Ortalama)**

Tek bir ara toplam türüyle sınırlı değilsiniz. Her `set_subtotals` çağrısı bir tür üzerinde bağımsız olarak çalışır; bu nedenle yöntemi iki kez — bir kez `SUM` ve bir kez `AVERAGE` ile — çağırmak, her `Category` grubu için iki ara toplam satırından oluşan özel bir alt küme üretir.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells["A1"].put_value("Category")
worksheet.cells["B1"].put_value("Item")
worksheet.cells["C1"].put_value("Year")
worksheet.cells["D1"].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(ac.PivotFieldSubtotalType.AVERAGE, True)

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_custom.xlsx")
```

## **Özet**

Yukarıdaki üç senaryo aynı veri kümesini ve pivot tablo yapısını paylaşır. Aralarındaki tek fark, dış `Category` satır alanına uygulanan `set_subtotals` çağrısıdır. İki alan kuralını unutmayın: bir bölgedeki tek alanın ara toplam oluşturacak bir şeyi yoktur; bu nedenle `set_subtotals`'ın görünür bir etkiye sahip olmasını istediğinizde, satır veya sütun bölgesine her zaman en az iki alan yerleştirin.

## **İlgili Makaleler**

- [Pivot Tablolarda Sayfa Alanları](/cells/tr/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET'te Pivot Tabloları Yenileme](/cells/tr/python-net/refresh-pivot-table/)
- [Pivot Tablolarına Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
