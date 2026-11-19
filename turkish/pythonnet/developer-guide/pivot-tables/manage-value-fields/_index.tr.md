---
title: Aspose.Cells for Python via .NET ile Özet Tablo Değer Alanlarını Yönetme
linktitle: Değer Alanları
description: Aspose.Cells for Python via .NET'de bir özet tablonun veri bölgesine temel alanlar eklemeyi, PivotField.function ile özet işlevini değiştirmeyi ve değer alanını Satır ya da Sütun eksenine çizdirmeyi öğrenin.
keywords: Aspose.Cells, Python via .NET, özet tablo, değer alanı, PivotField, PivotField.function, veri alanı, PivotTable.values_field, Sum, Average
type: docs
weight: 230
url: /tr/python-net/manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Veri Bölgesine Alan Ekleme**
Veri (değer) bölgesine bir temel alan eklemek, bir özet tablonun kaynak verileri nasıl topladığına şekil vermenin ilk adımıdır. Aspose.Cells, `PivotTable.AddFieldToArea(PivotFieldType, string)` yöntemini sunar; bu aşırı yükleme `PivotFieldType.DATA` sabitini ve kaynak sütun adını alır. Bir alan veri bölgesine eklendiğinde, API bu alanı `PivotTable.DataFields` koleksiyonu aracılığıyla, alanların eklendiği sıraya göre sunar. Varsayılan olarak, sayısal bir kaynak sütun `Sum` ile özetlenirken, sayısal olmayan sütun `Count` ile özetlenir.

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
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## **Özet İşlevini Değiştirme**
Bir alan veri bölgesinde yer aldığında, Aspose.Cells bu alanı `PivotTable.DataFields` üzerindeki `PivotField` nesnesi aracılığıyla sunar. Her `PivotField`'in, alana uygulanan özetleme işlemini kontrol eden, `ConsolidationFunction` türünde yazılabilir bir `Function` özelliği vardır. `ConsolidationFunction` enum'ı `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` ve `Varp` üyelerine sahiptir — ilk altı, gerçek dünya kullanım senaryolarının büyük çoğunluğunu kapsar, son dört ise varyans analizinde yararlı istatistiksel toplamalar sağlar.

{{% alert color="primary" %}}
`Function`'ı değiştirmek yalnızca özetlemeyi etkiler; kaynak sütun ve özet tablonun satır/sütun yapısı değiştirilmez. Mevcut bir veri alanı için özetlemeyi değiştirmek amacıyla, `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` şeklinde ayarlayın ve ardından özet tabloyu yeniden oluşturmak için `pivotTable.calculate_data()` metodunu çağırın.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import ConsolidationFunction
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
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```

## **Değer Alanlarını Satır veya Sütun Ekseni Üzerine Çizdirme**
Bir özet tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.ValuesField` adlı ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde yer alan her veri alanının toplamını temsil eder. Satır veya Sütun bölgesine temel bir pivot alanı olarak sürükleyebilirsiniz; bu, birden fazla ölçütü yan yana düzenlemek için kullanışlıdır.

{{% alert color="primary" %}}
`PivotTable.ValuesField` yalnızca hiçbir ya da yalnızca bir değer alanı bulunduğunda çalışmaz.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import ConsolidationFunction
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
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field)
pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

{{< app/cells/assistant language="python-net" >}}