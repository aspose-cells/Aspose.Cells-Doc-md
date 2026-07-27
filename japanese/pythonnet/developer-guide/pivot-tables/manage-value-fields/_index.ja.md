---
title: Aspose.Cells for .NET でピボットテーブルの値フィールドを管理する
linktitle: 値フィールド
description: Aspose.Cells for Python via .NET で、ピボットテーブルのデータ領域に基本フィールドを追加する方法、PivotField.function を使用して集計関数を変更する方法、値フィールドを Row または Column 軸にプロットする方法を学習します。
keywords: Aspose.Cells, Python via .NET, pivot table, value field, PivotField, PivotField.function, data field, PivotTable.values_field, Sum, Average
type: docs
weight: 230
url: /ja/python-net/pivot-table-manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域へのフィールドの追加
データ（値）領域への基本フィールドの追加は、ピボットテーブルがソースデータを集計する方法を形作る最初のステップです。Aspose.Cells は、定数 `PivotFieldType.DATA` とソース列名を受け取るオーバーロードである `PivotTable.add_field_to_area(PivotFieldType, str)` を公開しています。フィールドがデータ領域に追加されると、API はそれを `PivotTable.data_fields` コレクションを通じて、フィールドが追加された順序で公開します。デフォルトでは、数値のソース列は `ConsolidationFunction.SUM` で集計され、非数値列はデフォルトで `Count` になります。
## 集計関数の変更
データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `function` プロパティは `ConsolidationFunction` 列挙型の値を返します。同じ `function` セッターを使用すると、`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` を含む利用可能な集計を切り替えることができます。
{{% alert color="primary" %}}
`function` を変更しても集計にのみ影響し、ソース列は変更されません。
{{% /alert %}}
したがって、1 つのピボット内で、1 つのデータフィールドを `Sum` のままにして、同じソース列を対象とするが `Count` または `Average` を使用する 2 番目のデータフィールドを追加することができます。
## Row または Column 軸への値フィールドのプロット
ピボットテーブルに 2 つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.values_field` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。基本ピボットフィールドとして Row または Column 領域にドラッグすることができ、複数のメジャーを並べてレイアウトする場合に便利です。
{{% alert color="primary" %}}
値フィールドが存在しない、または 1 つしかない場合、`PivotTable.values_field` は機能しません。
{{% /alert %}}
以下のシナリオでは、上記の各機能を同じピボット構造に対して実証する 3 つのエンドツーエンドの例を順に説明します。
## シナリオ 1 — 基本フィールドを値領域にドラッグする
このシナリオでは、単一の基本フィールド (`Amount`) を既存ピボットテーブルのデータ領域に配置する方法を示します。共有されるピボット構造では、`Category` と `Item` が Row 軸に、`Year` が Column 軸に配置されます。操作後、`Amount` はデータ領域に表示され、デフォルトで `Amount` の `Sum` として計算されます。
```python
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# A1:D1のヘッダー
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

# A2:D9のデータ行、jで分岐するネストループを使用
for i in range(1, 9):
    for j in range(4):
        if j == 0:
            worksheet.cells[i, j].put_value("Fruit" if i <= 4 else "Vegetable")
        elif j == 1:
            if i == 1 or i == 2:
                worksheet.cells[i, j].put_value("Apple")
            elif i == 3 or i == 4:
                worksheet.cells[i, j].put_value("Banana")
            elif i == 5 or i == 6:
                worksheet.cells[i, j].put_value("Carrot")
            else:
                worksheet.cells[i, j].put_value("Daikon")
        elif j == 2:
            worksheet.cells[i, j].put_value(2020 + ((i - 1) % 2))
        elif j == 3:
            if i == 1:
                worksheet.cells[i, j].put_value(100)
            elif i == 2:
                worksheet.cells[i, j].put_value(150)
            elif i == 3:
                worksheet.cells[i, j].put_value(80)
            elif i == 4:
                worksheet.cells[i, j].put_value(90)
            elif i == 5:
                worksheet.cells[i, j].put_value(50)
            elif i == 6:
                worksheet.cells[i, j].put_value(60)
            elif i == 7:
                worksheet.cells[i, j].put_value(40)
            else:
                worksheet.cells[i, j].put_value(45)

# F3にPivotTable1という名前のピボットテーブルを追加
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# ピボットレイアウト: 行にCategoryとItem、列にYear、データフィールドにAmount
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## シナリオ 2 — 集計関数の変更
このシナリオはシナリオ 1 と同じピボット構造から始まりますが、`Amount` フィールドをデータ領域に 2 回追加します。両方のデータフィールドは同じソース列を参照しますが、2 番目のフィールドは `PivotField.function` セッターを使用してオーバーライドされ、デフォルトの `Sum` ではなく `Count` になります。
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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
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
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

count_field = pivot_table.data_fields[1]
count_field.function = ac.ConsolidationFunction.COUNT

pivot_table.calculate_data()

workbook.save("output_function.xlsx")
```
## シナリオ 3 — Row または Column 軸への値フィールドのプロット
2 つのデータフィールドが配置されると、`PivotTable.values_field` が使用可能になります。このシナリオでは、その集計仮想フィールドを Column 領域にドラッグし、データ領域の各メジャーが `Year` の隣に独自の列ブロックとして表示されるようにします。
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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
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
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ac.ConsolidationFunction.COUNT

# 値フィールドを列軸にプロットします。
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()

workbook.save("output_plot.xlsx")
```
これら 3 つのシナリオを合わせると、Aspose.Cells for Python via .NET での値フィールド操作のすべての側面をカバーします。デフォルトの `Sum` を持つ単一データフィールドから、仮想 `ValuesField` が Row または Column 軸のレイアウトを制御する複数メジャーのピボットまでを対象とします。

{{< app/cells/assistant language="python" >}}
