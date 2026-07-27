---
title: Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加する
linktitle: フィルターフィールドを追加
description: Aspose.Cells for Python via Java を使用してピボットテーブルにフィルターフィールドを追加および構成する方法を学びます。フィルターフィールドの追加、単一選択フィルター、複数選択フィルターを含みます。
keywords: Aspose.Cells, Python, Java, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /ja/python-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はピボットテーブルにおけるフィルターフィールドのライフサイクル全体をサポートします。ハイレベルな便利 API または低レベルの `page_fields` コレクションを通じてフィルターフィールドを追加でき、単一選択モードでフィルターを操作したり、すべてのフィルター項目を表示するためにクリアしたり、フィールドを複数選択に切り替えて Excel のチェックボックス UI を通じてユーザーが複数のフィルター項目を一度に選択できるようにすることができます。
{{% /alert %}}

## **はじめに**

フィルターフィールドとは、*ソースデータのどのサブセット* をピボット本体に表示するかを制御するピボットフィールドです。エンドユーザーは Excel でレンダリングされたピボットの上部にあるドロップダウンとしてそれを認識し、利用可能なフィルター項目のいずれかを選択すると、そのフィルター項目に属するレコードのみが集計されるようにピボット本体が再構築されます。ピボットフィールドは、`PivotFieldType.ROW`、`PivotFieldType.COLUMN`、または `PivotFieldType.DATA` ではなく `PivotFieldType.PAGE` として登録されたときにフィルターフィールドになります。

フィルターフィールドは 2 つの動作で動作できます。デフォルトの **単一選択** 動作では、一度に 1 つのフィルター項目のみが表示されるため、ピボット本体は正確に 1 つのサブセットを集計します。**複数選択** 動作では、フィールドはチェックボックスのリストを公開し、ピボット本体はチェックされたすべてのフィルター項目の和集合を集計します。同じソースフィールドは、単一のプロパティを切り替えることによって、これらの動作間を前後に移動できます。

Aspose.Cells for Python via Java は、フィルターフィールドを登録するために 2 つの同等の方法を公開しています。ハイレベル API は `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` で、ソース列名を受け取り、1 回の呼び出しでフィールドを追加します。低レベル API は `PivotTable.page_fields.add(PivotField)` で、すでに `PivotField` 参照を保持しており、同じフィールドインスタンスをページエリアに追加したい場合に使用されます。両方の API は最終的に同じ `page_fields` コレクションを設定し、この記事の残りではそれらの間の選択方法と各フィルターモードの操作方法を説明します。

## **フィルターフィールドの追加**

ページエリアにピボットフィールドを登録するには 2 つの方法があります。ハイレベル呼び出しはソース列名を文字列として受け取り、最も一般的なパスです。低レベル呼び出しは既存の `PivotField` インスタンスを受け取り、同じフィールドオブジェクトを複数のピボットエリア間で再利用する必要がある場合に便利です。両方の呼び出しはフィールドを `PivotTable.page_fields` に配置し、その後、レンダリングされたピボットの上部にページドロップダウンとして表示されます。

### add_field_to_area によるフィルターフィールドの追加

次の例では、小さな Fruit / Year / Amount データセットを作成し、`Fruit` を行エリア、`Amount` をデータエリア、`Year` をページエリアに持つピボットテーブルをセル E3 に配置し、ピボットを更新して、ワークブックを保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# 新しいワークブックを作成
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# ヘッダー行を設定
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9行のサンプルデータ（Fruit、Year、Amount）を入力
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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# セルE3にアンカーを置くピボットテーブルを追加
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# フィールドをそれぞれのエリアに追加：Fruitは行、Amountはデータ、Yearはページフィールド
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# ピボットテーブルのデータを更新して計算
pivotTable.refreshData()
pivotTable.calculateData()

# ワークブックを保存
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### page_fields.add によるフィルターフィールドの追加

すでに `PivotField` インスタンスを操作している場合は、それを直接 `PivotTable.page_fields.add` に渡すことができます。ピボットテーブルとフィルターフィールドは前のシナリオとまったく同じように構築されます。ページエリアの登録のみが低レベル API 呼び出しに置き換えられます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — ピボットテーブルとページフィールドは、シナリオ 1a とまったく同じ方法で構築されます
#   (Fruit/Year/Amount データ、E3 にピボット、Fruit→行、
#   Amount→データ)。以下では、BaseFields コレクションから
#   Year PivotField を取得し、PageFields.Add に渡します。
#   これは AddFieldToArea の代わりに使用する低レベルの方法です。
#   その結果はシナリオ 1a と機能的に同一です。

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# ヘッダー
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# サンプルデータ (9 行)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# E3 に A1:C10 を範囲とするピボットテーブルを追加
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Fruit -> 行、Amount -> データ (Year は下記でページに追加)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 低レベルの方法: BaseFields から既存の Year PivotField を取得し、
# PageFields.Add(PivotField) を介してページ領域に登録します。
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# 新しいページフィールドが保存されるワークブックに反映されるように更新します
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **単一選択フィルター (1 つのフィルター項目の表示)**

デフォルトの単一選択動作では、フィルターフィールドは単一のドロップダウンとしてレンダリングされ、`PivotField.current_page_item` 整数がピボット本体を駆動するフィルター項目を選択します。特定のインデックスを割り当てるとその 1 つの項目が選択されます。特別なセンチネル値 `0x7FFD` (10 進数で 32765) を割り当てるとフィルターがクリアされ、すべてのフィルター項目が一度に集計されます。単一選択がデフォルトであり、明示的に有効にする必要はありません。

### すべての項目の表示

`current_page_item` をマジック値 `0x7FFD` に設定することは、フィルターをクリアすることと同等です。フィルターが適用されていないかのように、ピボット本体はすべてのフィルター項目を集計します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 新しいワークブックを作成
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Fruit/Year/Amount のデータを入力
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

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
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# E3 にピボットテーブルを作成
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# ピボットフィールドを設定: Fruit→行、Amount→データ、Year→ページ
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.refreshData()
pivotTable.calculateData()

# ページフィールドのフィルターをクリアし、すべての項目を表示可能にする。
# 0x7FFD (10進数 32765) は「すべての項目」を意味する特殊なセンチネル値です —
# Excel のページフィールドドロップダウンで「(すべて)」を選択するのと同等です。
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### 特定の 1 つの項目の表示

`current_page_item` を実際のインデックスに設定すると、その 1 つのフィルター項目のみが選択されます。インデックスはフィルターフィールドのソート済み項目リスト内の項目の位置であるため、たとえば `1` はソート後の 2 番目の項目を選択します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# ワークブックを作成
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# サンプルデータを追加 (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# E3にピボットテーブルを追加
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# フィールドを追加: Fruit→行、Amount→データ、Year→ページ
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# ページフィールド固有の操作
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = ソート順の2番目の項目 (例: "2021")

# ピボットテーブルを更新して計算
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **複数選択フィルター**

複数選択フィルターは、ページドロップダウンをチェックボックスのリストに変換し、エンドユーザーが複数のフィルター項目を同時に選択できるようにします。Aspose.Cells は連携して動作する 2 つのプロパティを公開しています。`PivotField.is_multiple_item_selection_allowed` は、複数選択 UI がまったく有効になる前に `True` に設定する必要があります。有効にした後、`PivotItem.is_hidden` はチェックボックスリストに表示される項目を制御するため、すべての項目を表示するか、特定の項目のみをホワイトリスト化するかを選択できます。

以下のコードは、シナリオ 1a で構築された同じ Year フィルターフィールドで複数選択を有効にし、2 つのパターンを示します。パート A では、すべてのエントリの `is_hidden` を `False` のままにしておくことですべてのフィルター項目を公開し、パート B では、`switch (pivot_items[i].get_string_value())` ブロックを介して選択したソース値のみをホワイトリスト化し、他のすべてを非表示にします。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — ピボットテーブルとページフィールドは以下とまったく同じ構成です
#   シナリオ1a (Fruit/Year/Amountデータ、E3にピボット、Fruit→Row、
#   Amount→Data、Year→PageはAddFieldToAreaを使用)。
#   以下ではページフィールドに複数選択フィルタを適用します。

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# サンプルデータ: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

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
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — ページフィールドで複数選択を有効化
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# パートA — すべての項目を選択 (すべての項目を表示する)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# パートB — ソース値によって特定の項目のみを選択
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **注意:** `PivotItem.is_hidden` を通じて複数選択フィルターを使用する場合、**少なくとも 1 つの `PivotItem` は表示されたまま** (`is_hidden == False`) でなければなりません。すべての項目が非表示になっていると、Excel はファイルを開くときにクラッシュするか、空のピボットをレンダリングします。複数選択のホワイトリストにソースデータの少なくとも 1 つの項目が含まれていることを常に確認してください。

## **どの API とどのモードを使用すべきか?**

次の表は、各シナリオとモードをいつ使用すべきかをまとめたもので、すべてのシナリオを詳しく読まなくても適切な組み合わせを選択できます。

| シナリオ / ユースケース | 推奨 API | 使用するプロパティ | 注意事項 |
|---|---|---|---|
| ソース列名でフィルターフィールドを追加する (最も一般的) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | なし | ハイレベル、ワンライナー。`PivotField` 参照が必要ない限り、これを使用してください。 |
| すでに `PivotField` オブジェクトを保持している場合にフィルターフィールドを追加する | `PivotTable.page_fields.add(PivotField)` | なし | フィールドオブジェクトが他の場所で取得された場合や再利用する必要がある場合に使用します。 |
| 単一のフィルター項目にフィルターする (デフォルトモード) | `PivotField.current_page_item` | 特定のインデックスに設定 | たとえば、`1` はソート済みリストの 2 番目の項目を表示します。 |
| すべての項目を表示する / フィルターをクリアする | `PivotField.current_page_item` | `0x7FFD` に設定 | マジック値 `0x7FFD` (10 進数 32765) は「すべての項目」のセンチネル値です。 |
| Excel で複数選択 UI を有効にする | `PivotField.is_multiple_item_selection_allowed` | `True` に設定 | `is_hidden` 呼び出しが有効になる前に必要です。 |
| 複数選択リスト内の個別項目を非表示 / 表示する | `PivotItem.is_hidden` | 項目ごとに設定 | 少なくとも 1 つの項目が表示されたまま (`is_hidden == False`) でなければなりません。 |

{{% alert color="primary" %}}
複数選択フィルターを構成するときは、常に可視性制約を覚えておいてください。複数選択フィルターフィールドのすべての `PivotItem` が非表示になっていると、Excel は開いたときにクラッシュするか、空のピボットをレンダリングします。ソースデータに対してホワイトリストを構築して少なくとも 1 つの項目が表示されたままになるようにし、保存されたワークブックがすべてのマシンで確実に開くようにしてください。
{{% /alert %}}



{{< app/cells/assistant language="python" >}}