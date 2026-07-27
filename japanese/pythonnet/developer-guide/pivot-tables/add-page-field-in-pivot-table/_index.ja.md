---
title: Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加する
linktitle: フィルターフィールドを追加
description: Aspose.Cells for Python via .NET を使用してピボットテーブルのフィルターフィールドを追加および構成する方法を学習します。フィルターフィールドの追加、単一選択フィルタリング、および複数選択フィルタリングを含みます。
keywords: Aspose.Cells, Python via .NET, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter, ピボットテーブル, フィルターフィールド
type: docs
weight: 250
url: /ja/python-net/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はピボットテーブルにおけるフィルターフィールドの全ライフサイクルをサポートします。ハイレベルの便利な API または低レベルの `page_fields` コレクションを通じてフィルターフィールドを追加でき、単一選択モードでページフィルタを駆動したり、すべてのページアイテムを表示するためにクリアしたり、フィールドを複数選択に切り替えて Excel のチェックボックス UI を通じて複数のページアイテムを一度に選択できるようにすることができます。
{{% /alert %}}

## **はじめに**

フィルターフィールドは、ピボット本体が表示するソースデータの *どのサブセット* を制御するピボットフィールドです。エンドユーザーはレンダリングされたピボットの上部にあるドロップダウンとしてそれを表示し、利用可能なページアイテムのいずれかを選択すると、そのページアイテムに属するレコードのみが要約されるようにピボット本体が再構築されます。ピボットフィールドは、`PivotFieldType.ROW`、`PivotFieldType.COLUMN`、または `PivotFieldType.DATA` ではなく `PivotFieldType.PAGE` として登録されたときにフィルターフィールドになります。

フィルターフィールドは 2 つの動作で操作できます。デフォルトの **単一選択** 動作では、一度に 1 つのページアイテムのみが表示されるため、ピボット本体は正確に 1 つのサブセットを集約します。**複数選択** 動作では、フィールドはチェックボックスリストを公開し、ピボット本体はチェックされたすべてのページアイテムの和集合を集約します。同じソースフィールドは、単一のプロパティを切り替えることによって、これらの動作間を行き来できます。

Aspose.Cells for Python via .NET は、フィルターフィールドを登録するための 2 つの同等の方法を公開しています。ハイレベル API は `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` で、ソース列名を受け取り、単一の呼び出しでフィールドを追加します。低レベル API は `PivotTable.page_fields.add(PivotField)` で、すでに `PivotField` 参照を保持していて、同じフィールドインスタンスをページエリアに追加したい場合に使用されます。どちらの API も最終的に同じ `page_fields` コレクションに格納され、この記事の残りではそれらの選択方法と各フィルタリングモードの駆動方法を説明します。

## **フィルターフィールドの追加**

ページエリアにピボットフィールドを登録するには 2 つの方法があります。ハイレベルの呼び出しはソース列名を文字列として受け取り、最も一般的なパスです。低レベルの呼び出しは既存の `PivotField` インスタンスを受け取り、同じフィールドオブジェクトを複数のピボットエリア間で再利用する場合に便利です。どちらの呼び出しもフィールドを `PivotTable.page_fields` に配置し、その後、レンダリングされたピボットの上部にページドロップダウンとして表示されます。

### add_field_to_area を使用したフィルターフィールドの追加

次の例では、小さな Fruit / Year / Amount データセットを構築し、セル E3 にピボットテーブルを配置し、行エリアに `Fruit`、データエリアに `Amount`、ページエリアに `Year` を配置して、ピボットを更新し、ワークブックを保存します。

```python
import aspose.cells as ac

# 新しいワークブックを作成
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# ヘッダー行を設定
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# サンプルデータ9行を入力: Fruit、Year、Amount
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# セルE3にアンカーされたピボットテーブルを追加
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# フィールドをそれぞれのエリアに追加: Fruitを行、Amountをデータ、Yearをページフィールド
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# ピボットテーブルのデータを更新して計算
pivot_table.calculate_data()

# ワークブックを保存
workbook.save("pageFieldSample.xlsx")
```

### page_fields.add を使用したフィルターフィールドの追加

すでに `PivotField` インスタンスを操作している場合は、それを `PivotTable.page_fields.add` に直接渡すことができます。ピボットテーブルとフィルターフィールドは前のシナリオとまったく同じように構築されます。最終的なページエリアの登録のみが低レベル API 呼び出しに置き換えられます。

```python
import aspose.cells as ac

# — ピボットテーブルとページフィールドは、Scenario 1a とまったく同じように構築されます
#   (Fruit/Year/Amount データ、E3 にピボット、Fruit→行、
#   Amount→データ)。以下では、BaseFields コレクションから
#   Year PivotField を取得し、PageFields.Add に渡します — これは
#   AddFieldToArea の低レベルの代替手段です。結果は
#   Scenario 1a と機能的に同一です。

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# ヘッダー
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# サンプルデータ（9 行）
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# A1:C10 をカバーする E3 にピボットテーブルを追加
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Fruit → 行、Amount → データ（Year は以下にページへ追加）
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 低レベルの方法: BaseFields から既存の Year PivotField を取得し、
# PageFields.Add(PivotField) 経由でページエリアに登録します。
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# 新しいページフィールドが保存されたワークブックに反映されるように更新
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **単一選択フィルタリング (1 つのページアイテムの表示)**

デフォルトの単一選択動作では、フィルターフィールドは単一のドロップダウンとしてレンダリングされ、`PivotField.current_page_item` 整数がピボット本体を駆動するページアイテムを選択します。特定のインデックスを割り当てるとそのアイテムが選択されます。特別なセンチネル値 `0x7FFD` (10 進数で 32765) を割り当てるとフィルタがクリアされ、すべてのページアイテムが一度に集計されます。単一選択はデフォルトであるため、明示的に有効にする必要はありません。

### すべてのアイテムの表示

`current_page_item` をマジック値 `0x7FFD` に設定することは、ページフィルタをクリアすることと同じです。フィルタが適用されていないかのように、ピボット本体はすべてのページアイテムを集約します。

```python
import aspose.cells as ac

# 新しいワークブックを作成
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Fruit/Year/Amount のデータを入力
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# E3 にピボットテーブルを作成
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# ピボットフィールドを設定: Fruit→行、Amount→データ、Year→ページ
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.calculate_data()

# ページフィルタをクリアして、ページフィールドの全項目を表示します。
# 0x7FFD（10進数で32765）は "全項目" を意味する特別なセンチネル値です —
# Excel のページフィールドドロップダウンで「(すべて)」を選択するのと同じです。
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### 特定の 1 つのアイテムの表示

`current_page_item` を実際のインデックスに設定すると、その 1 つのページアイテムのみが選択されます。インデックスはフィルターフィールドのソート済みアイテムリスト内のアイテムの位置であるため、たとえば `1` はソート後の 2 番目のアイテムを選択します。

```python
import aspose.cells as ac

# ワークブックを作成
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# サンプルデータを追加 (果物/年/金額)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# E3にピボットテーブルを追加
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# フィールドを追加: Fruit→行, Amount→データ, Year→ページ
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# ページフィールド固有の操作
pivot_table.page_fields[0].current_page_item = 1  # 1 = ソート順で2番目の項目（例: "2021"）

# ピボットテーブルを更新して計算
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **複数選択フィルタリング**

複数選択フィルタリングはページドロップダウンをチェックボックスリストに変え、エンドユーザーが複数のページアイテムを同時に選択できるようにします。Aspose.Cells は連携して機能する 2 つのプロパティを公開しています。`PivotField.is_multiple_item_selection_allowed` は、複数選択 UI がまったく有効になる前に `True` に設定する必要があります。有効にした後、`PivotItem.is_hidden` がチェックボックスリストに表示されるアイテムを制御するため、すべてのアイテムを表示するか、特定のアイテムのみをホワイトリストに登録するかを選択できます。

以下のコードは、シナリオ 1a で構築された同じ Year フィルターフィールドで複数選択を有効にし、2 つのパターンを示します。パート A はすべての `PivotItem` の `is_hidden` を `False` のままにすることですべてのページアイテムを明らかにし、パート B は選択したソース値のみをホワイトリストに登録し、`pivot_items[i].get_string_value()` をテストする `if` / `elif` ブロックを通じてその他すべてを非表示にします。

```python
import aspose.cells as ac

# — ピボットテーブルとページフィールドは以下とまったく同じ方法で構築されます
#   シナリオ1a（Fruit/Year/Amountデータ、E3にピボット、Fruit→行、
#   Amount→データ、Year→ページをAddFieldToArea経由で設定）。
#   以下ではページフィールドに複数選択フィルタを適用します。

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# サンプルデータ: Fruit | Year | Amount
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — ページフィールドで複数選択を有効化
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# パートA — すべての項目を選択（すべての項目を表示）
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# パートB — ソース値で特定の項目のみを選択
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **注意:** `PivotItem.is_hidden` を通じて複数選択フィルタリングを使用する場合、**少なくとも 1 つの `PivotItem` は表示されたまま** (`is_hidden == False`) である必要があります。すべてのアイテムが非表示になっていると、Excel はファイルを開くときにクラッシュするか、空のピボットをレンダリングします。複数選択のホワイトリストにソースデータの少なくとも 1 つのアイテムが含まれていることを必ず確認してください。

## **どの API とどのモードを使用すべきか?**

次の表は、各シナリオを詳しく読まずに適切な組み合わせを選択できるように、各 API とモードをいつ使用するかをまとめたものです。

| シナリオ / ユースケース | 推奨される API | 使用するプロパティ | メモ |
|---|---|---|---|
| ソース列名でフィルターフィールドを追加する (最も一般的) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | ハイレベル、ワンライナー。`PivotField` 参照が必要ない場合はこれを使用します。 |
| すでに `PivotField` オブジェクトを持っている場合にフィルターフィールドを追加する | `PivotTable.page_fields.add(PivotField)` | n/a | フィールドオブジェクトが他の場所で取得されたものであるか、再利用が必要な場合に使用します。 |
| 単一のページアイテムにフィルタリングする (デフォルトモード) | `PivotField.current_page_item` | 特定のインデックスに設定 | たとえば、`1` はソート済みリストの 2 番目のアイテムを表示します。 |
| すべてのアイテムを表示する / ページフィルタをクリアする | `PivotField.current_page_item` | `0x7FFD` に設定 | マジック値 `0x7FFD` (10 進数で 32765) は「すべてのアイテム」のセンチネルです。 |
| Excel で複数選択 UI を有効にする | `PivotField.is_multiple_item_selection_allowed` | `True` に設定 | `is_hidden` 呼び出しが有効になる前に必要です。 |
| 複数選択リスト内の個別アイテムを非表示 / 表示する | `PivotItem.is_hidden` | アイテムごとに設定 | 少なくとも 1 つのアイテムは表示されたままにする必要があります (`is_hidden == False`)。 |

{{% alert color="primary" %}}
複数選択フィルタリングを構成するときは、表示制約を常に覚えておいてください。複数選択フィルターフィールドのすべての `PivotItem` が非表示になっていると、Excel は開くときにクラッシュするか、空のピボットをレンダリングします。少なくとも 1 つのアイテムが表示されたままになるように、ソースデータに対してホワイトリストを構築してください。そうすれば、保存したワークブックはすべてのマシンで確実に開きます。
{{% /alert %}}


{{< app/cells/assistant language="python" >}}
