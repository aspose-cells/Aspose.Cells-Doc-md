---
title: Aspose.Cells for Python via Java'da Değer Alanları
linktitle: Aspose.Cells for Python via Java'da Değer Alanları
description: Aspose.Cells for Python via Java'da bir pivot tablonun veri bölgesine temel alanların nasıl ekleneceğini, PivotField.Function ile özet fonksiyonunun nasıl değiştirileceğini ve değer alanının Satır veya Sütun eksenine nasıl yerleştirileceğini öğrenin.
keywords: Aspose.Cells, Python via Java, pivot tablosu, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Toplam, Ortalama
type: docs
weight: 230
url: /tr/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Veri Bölgesine Alan Ekleme
Bir temel alanı veri (değer) bölgesine eklemek, pivot tablonun kaynak verilerinizi nasıl topladığını şekillendirmedeki ilk adımdır. Aspose.Cells, `PivotFieldType.DATA` sabitini ve kaynak sütun adını kabul eden `PivotTable.addFieldToArea(PivotFieldType, string)` aşırı yüklemesini kullanıma sunar. Bir alan veri bölgesine eklendikten sonra, API bu alanı, alanların eklenme sırasına göre `PivotTable.DataFields` koleksiyonu aracılığıyla kullanıma sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.SUM` ile özetlenirken, sayısal olmayan bir sütun için varsayılan değer `COUNT`'tur.
## Özet Fonksiyonunu Değiştirme
Veri bölgesine yerleştirilen her alan dahili olarak bir `PivotField` örneği olarak sarmalanır ve `Function` özelliği `ConsolidationFunction` enum'undan bir değer döndürür. Aynı `Function` ayarlayıcısı, `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` ve `VARP` dahil olmak üzere kullanılabilir toplamalar arasında geçiş yapmanıza olanak tanır.
{{% alert color="primary" %}}
`Function`'ı değiştirmek yalnızca toplamayı etkiler, kaynak sütun değişmez.
{{% /alert %}}
Bu nedenle, aynı kaynak sütunu hedefleyen ancak `COUNT` veya `AVERAGE` kullanan ikinci bir veri alanı eklerken tek bir veri alanını `SUM` olarak bırakabilirsiniz; tümü tek bir pivot içinde gerçekleşir.
## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
Bir pivot tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.ValuesField` adında ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Onu, birden çok ölçüyü yan yana düzenlemek için kullanışlı bir temel pivot alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz.
{{% alert color="primary" %}}
`PivotTable.ValuesField`, değer alanı yoksa veya yalnızca bir tane varsa çalışmaz.
{{% /alert %}}
Aşağıdaki senaryolar, yukarıda açıklanan her bir yeteneği aynı pivot yapısına karşı gösteren üç uçtan uca örnek üzerinden ilerler.
## Senaryo 1 — Bir Temel Alanı Değer Bölgesine Sürükleme
Bu senaryo, tek bir temel alanın (`Amount`) mevcut bir pivot tablonun veri bölgesine nasıl yerleştirileceğini gösterir. Paylaşılan pivot yapısı, `Category` ve `Item`'ı Satır eksenine, `Year`'ı ise Sütun eksenine yerleştirir. İşlemden sonra `Amount` veri bölgesinde görünür ve varsayılan olarak `Amount` değerlerinin toplamı (`Sum`) olarak hesaplanır.
```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## Senaryo 2 — Özet Fonksiyonunu Değiştirme
Bu senaryo, Senaryo 1 ile aynı pivot yapısından başlar, ancak `Amount` alanını veri bölgesine iki kez ekler. Her iki veri alanı da aynı kaynak sütuna başvurur, ancak ikinci alan, varsayılan `Sum` yerine `Count` olacak şekilde `PivotField.Function` ayarlayıcısı kullanılarak geçersiz kılınır.
```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT

pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```
## Senaryo 3 — Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
İki veri alanı yerinde olduğunda, `PivotTable.ValuesField` kullanılabilir hale gelir. Bu senaryo, o toplama sanal alanını Sütun bölgesine sürükler, böylece veri bölgesindeki her ölçü, `Year`'ın yanında kendi sütun bloğu olarak görünür.
```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```
Birlikte, bu üç senaryo Aspose.Cells for Python via Java'daki değer alanı manipülasyonunun tüm yönlerini kapsar; varsayılan `Sum` ile tek bir veri alanından, sanal `ValuesField`'ın Satır veya Sütun eksenindeki düzeni kontrol ettiği çoklu ölçülü bir pivota kadar.
## İlgili Makaleler
- [Aspose.Cells for Python via Java'da Pivot Tablo Satır ve Sütun Alanları](/cells/tr/python-java/row-and-column-fields/)
- [Pivot Tablolardaki Sayfa Alanları](/cells/tr/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java'da Pivot Tabloları Yenileme](/cells/tr/python-java/refresh-pivot-table/)
- [Pivot Tablolara Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="python" >}}
