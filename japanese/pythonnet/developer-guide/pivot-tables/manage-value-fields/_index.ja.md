---
title: Aspose.Cells for Python via .NET でピボットテーブルの値フィールドを管理する
linktitle: Aspose.Cells for Python via .NET でピボットテーブルの値フィールドを管理する
description: Aspose.Cells for Python via .NET で、ピボットテーブルのデータ領域にベースフィールドを追加する方法、PivotField.function を使用して集計関数を変更する方法、および値フィールドを行または列の軸にプロットする方法を学習します。
keywords: Aspose.Cells, Python via .NET, ピボットテーブル, 値フィールド, PivotField, PivotField.function, データフィールド, PivotTable.values_field, Sum, Average
type: docs
weight: 230
url: /ja/python-net/manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域にフィールドを追加する
データ（値）領域にベースフィールドを追加することは、ピボットテーブルでソースデータを集計する方法を設定する最初の手順です。Aspose.Cells は `PivotTable.AddFieldToArea(PivotFieldType, string)` を提供しています。このオーバーロードは、定数 `PivotFieldType.DATA` とソース列名を受け取ります。データ領域にフィールドを追加すると、API はそのフィールドを `PivotTable.DataFields` コレクションを通じて公開します。フィールドは追加された順序で並びます。既定では、数値型のソース列は `Sum` で集計され、非数値型の列は `Count` で集計されます。

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

## 集計関数の変更
フィールドをデータ領域に追加すると、そのフィールドは `PivotTable.DataFields` 内の `PivotField` オブジェクトとして Aspose.Cells から公開されます。各 `PivotField` には、`ConsolidationFunction` 型の書き込み可能な `Function` プロパティがあり、そのフィールドが参照する値に適用される集計を制御します。`ConsolidationFunction` は、次のメンバーを持つ列挙型です。`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp`。最初の 6 つは現実的な使用事例の大部分をカバーし、最後の 4 つは分散分析に役立つ統計集計です。

{{% alert color="primary" %}}
`Function` を変更しても集計関数だけが変更され、ソース列やピボットテーブルの行・列構造は変更されません。既存のデータフィールドの集計関数を切り替えるには、`pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` を設定し、その後 `pivotTable.calculate_data()` を呼び出してピボットテーブルを再描画します。
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

## 値フィールドを行または列の軸にプロットする
ピボットテーブルに 2 つ以上のデータフィールドが含まれる場合、Aspose.Cells は `PivotTable.ValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。この仮想フィールドを行領域または列領域にピボットのベースフィールドとしてドラッグでき、複数の指標を横に並べて表示する場合に便利です。

{{% alert color="primary" %}}
値フィールドがない場合や 1 つしかない場合、`PivotTable.ValuesField` は機能しません。
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