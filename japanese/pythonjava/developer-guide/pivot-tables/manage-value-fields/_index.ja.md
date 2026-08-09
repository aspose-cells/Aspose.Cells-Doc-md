---
title: Aspose.Cells for Python via Java の値フィールド
linktitle: Aspose.Cells for Python via Java の値フィールド
description: Aspose.Cells for Python via Java で、ピボットテーブルのデータ領域に基本フィールドを追加する方法、PivotField.Function で集計関数を変更する方法、Row または Column 軸に値フィールドをプロットする方法を学びます。
keywords: Aspose.Cells, Python via Java, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域へのフィールドの追加
基本フィールドをデータ（値）領域に追加することが、ピボットテーブルがソースデータを集計する方法を形作る最初のステップです。Aspose.Cells は `PivotTable.addFieldToArea(PivotFieldType, string)` を公開しています。これは定数 `PivotFieldType.DATA` とソース列名を受け取るオーバーロードです。フィールドがデータ領域に追加されると、API はそれを `PivotTable.DataFields` コレクションを通じて、フィールドが追加された順序で公開します。デフォルトでは、数値ソース列は `ConsolidationFunction.SUM` で集計され、非数値列のデフォルトは `COUNT` になります。

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

## 集計関数の変更
データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `Function` プロパティは `ConsolidationFunction` 列挙型の値を返します。同じ `Function` セッターを使用すると、`SUM`、`COUNT`、`AVERAGE`、`MAX`、`MIN`、`PRODUCT`、`STDDEV`、`STDDEVP`、`VAR`、`VARP` を含む利用可能な集計関数を切り替えることができます。
{{% alert color="primary" %}}
`Function` を変更しても集計にのみ影響し、ソース列は変更されません。
{{% /alert %}}
したがって、1 つのデータフィールドを `SUM` のままにして、同じソース列を対象としつつ `COUNT` または `AVERAGE` を使用する 2 つ目のデータフィールドを、単一のピボット内で追加することができます。

```python
as ac
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

## Row または Column 軸への値フィールドのプロット
ピボットテーブルに 2 つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.ValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。これを基本ピボットフィールドとして Row 領域または Column 領域にドラッグできます。これは複数のメジャーを並べてレイアウトする場合に役立ちます。
{{% alert color="primary" %}}
値フィールドが存在しない場合、または 1 つしかない場合、`PivotTable.ValuesField` は機能しません。
{{% /alert %}}
以下のシナリオでは、同じピボット構造に対して上記で説明した各機能を示す 3 つのエンドツーエンドの例を紹介します。

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

{{< app/cells/assistant language="python" >}}