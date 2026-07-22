---
title: ピボットテーブルのページフィールド
linktitle: ピボットテーブルのページフィールド
description: Aspose.Cells for Node.js via Java を使用して、ピボットテーブルのページフィールドを追加および構成する方法を説明します。ページフィールドの追加、単一選択フィルタリング、複数選択フィルタリングを含みます。
keywords: Aspose.Cells, Node.js via Java, ピボットテーブル, ページフィールド, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, フィルタ
type: docs
weight: 250
url: /ja/nodejs-java/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブル内のページフィールドのライフサイクル全体をサポートします。高レベルの便利な API または低レベルの `PageFields` コレクションを通じてページフィールドを追加でき、単一選択モードでページフィルタを駆動したり、すべてのページアイテムを表示するようにクリアしたり、フィールドを複数選択に切り替えて Excel のチェックボックス UI を通じてユーザーが複数のページアイテムを一度に選択できるようにすることができます。
{{% /alert %}}

## **はじめに**

ページフィールドは、ピボット本体が表示するソースデータの*どのサブセット*を制御するピボットフィールドです。エンドユーザーは Excel でレンダリングされたピボットの上部にあるドロップダウンとしてそれを見て、利用可能なページアイテムの 1 つを選択すると、そのページアイテムに属するレコードのみが要約されるようにピボット本体が再構築されます。ピボットフィールドは、`PivotFieldType.Row`、`PivotFieldType.Column`、または `PivotFieldType.Data` ではなく、`PivotFieldType.Page` として登録されたときにページフィールドになります。

ページフィールドは 2 つの動作で動作します。デフォルトの**単一選択**動作では、一度に 1 つのページアイテムのみが表示されるため、ピボット本体は正確に 1 つのサブセットを要約します。**複数選択**動作では、フィールドはチェックボックスリストを公開し、ピボット本体はチェックされたすべてのページアイテムの和集合を要約します。同じソースフィールドは、単一プロパティを切り替えることによって、これらの動作間を前後に移動できます。

Aspose.Cells for Node.js via Java は、ページフィールドを登録する 2 つの同等の方法を公開しています。高レベル API は `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` であり、ソース列名を受け取り、1 回の呼び出しでフィールドを追加します。低レベル API は `pivotTable.getPageFields().add(PivotField)` であり、すでに `PivotField` 参照を保持しており、同じフィールドインスタンスをページ領域に追加する場合に使用されます。どちらの API も最終的に同じ `PageFields` コレクションにデータを格納し、この記事の残りの部分では、それらの選択方法と各フィルタリングモードの駆動方法について説明します。

## **ページフィールドの追加**

ページ領域にピボットフィールドを登録するには 2 つの方法があります。高レベルの呼び出しはソース列名を文字列として受け取り、最も一般的なパスです。低レベルの呼び出しは既存の `PivotField` インスタンスを受け入れ、同じフィールドオブジェクトを複数のピボット領域で再利用する必要がある場合に便利です。どちらの呼び出しもフィールドを `pivotTable.getPageFields()` に配置し、その後、レンダリングされたピボットの上部にページドロップダウンとして表示されます。

### addFieldToArea によるページフィールドの追加

次の例では、小さな Fruit / Year / Amount データセットを作成し、`Fruit` を行領域に、`Amount` をデータ領域に、`Year` をページ領域に持つピボットテーブルをセル E3 に配置し、ピボットを更新して、ワークブックを保存します。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// ヘッダー行を設定する
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9行のサンプルデータを入力：果物、年、金額
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// セルE3にアンカーされたピボットテーブルを追加する
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドをそれぞれのエリアに追加：果物を行、金額をデータ、年をページフィールド
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// ピボットテーブルのデータを更新して計算する
pivotTable.refreshData();
pivotTable.calculateData();

// ワークブックを保存する
workbook.save("pageFieldSample.xlsx");
```

### getPageFields().add によるページフィールドの追加

すでに `PivotField` インスタンスを操作している場合は、それを `pivotTable.getPageFields().add` に直接渡すことができます。ピボットテーブルとページフィールドは前のシナリオとまったく同じように構築されます。最終的なページ領域の登録のみが低レベル API 呼び出しに置き換えられます。

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// ヘッダー
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// サンプルデータ (9 行)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// E3 に A1:C10 をカバーするピボットテーブルを追加
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> 行、Amount -> データ (Year は下記のように Page に配置)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 低レベルアプローチ：BaseFields から既存の Year PivotField を取得し、
// PageFields.Add(PivotField) 経由で Page エリアに登録する。
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// 新しいページフィールドが保存されたワークブックに反映されるように更新
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **単一選択フィルタリング (1 つのページアイテムの表示)**

デフォルトの単一選択動作では、ページフィールドは単一のドロップダウンとしてレンダリングされ、`PivotField.CurrentPageItem` 整数がどのページアイテムがピボット本体を駆動するかを選択します。特定のインデックスを割り当てるとその 1 つのアイテムが選択されます。特別なセンチネル値 `0x7FFD` (10 進数 32765) を割り当てるとフィルタがクリアされ、すべてのページアイテムが一度に要約されます。単一選択がデフォルトです。明示的に有効化する必要はありません。

### すべてのアイテムの表示

`CurrentPageItem` をマジック値 `0x7FFD` に設定することは、ページフィルタをクリアすることと同等です。フィルタが適用されていないかのように、ピボット本体はすべてのページアイテムを要約します。

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// Fruit/Year/Amount のデータを入力
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// E3 にピボットテーブルを作成
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// ピボットフィールドを設定: Fruit→行、Amount→データ、Year→ページ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// ページフィールドのフィルタをクリアして、ページフィールド内のすべての項目を表示する。
// 0x7FFD (10進数 32765) は「すべての項目」を意味する特別なセンチネル値です —
// Excel のページフィールドドロップダウンで「(すべて)」を選択するのと同じです。
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### 特定の 1 つのアイテムの表示

`CurrentPageItem` を実際のインデックスに設定すると、その 1 つのページアイテムのみが選択されます。インデックスはページフィールドのソート済みアイテムリスト内のアイテムの位置であるため、たとえば `1` はソート後の 2 番目のアイテムを選択します。

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// サンプルデータを追加 (フルーツ/年/金額)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// E3にピボットテーブルを追加
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// フィールドを追加: フルーツ→行、金額→データ、年→ページ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// ページフィールド固有の操作
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = ソート順の2番目のアイテム (例: "2021")

// ピボットテーブルを更新して計算
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **複数選択フィルタリング**

複数選択フィルタリングは、ページドロップダウンをチェックボックスリストに変え、エンドユーザーが複数のページアイテムを同時に選択できるようにします。Aspose.Cells は連携する 2 つのプロパティを公開しています。複数選択 UI がまったく機能するためには、`PivotField.IsMultipleItemSelectionAllowed` を `true` に設定する必要があります。有効化された後、`PivotItem.IsHidden` はチェックボックスリストに表示されるアイテムを制御するため、すべてのアイテムを表示するか、特定のアイテムのみをホワイトリストに登録するかのいずれかを選択できます。

以下のコードは、シナリオ 1a で構築された同じ Year ページフィールドで複数選択を有効化し、2 つのパターンを示します。パート A では、すべてのエントリの `IsHidden` を `false` に設定したままにすることで、すべてのページアイテムを表示します。一方、パート B では、選択したソース値のみをホワイトリストに登録し、`switch (pivotItems[i].getStringValue())` ブロックを使用して他のすべてを非表示にします。

```javascript
const AsposeCells = require("aspose.cells");

// — ピボットテーブルとページフィールドは、シナリオ1aとまったく同じ方法で構築されます
//   (Fruit/Year/Amountデータ、E3にピボット、Fruit→Row、
//   Amount→Data、Year→Page via AddFieldToArea)。
//   以下では、ページフィールドに複数選択フィルタリングを適用します。

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// サンプルデータ: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — ページフィールドで複数選択を有効にする
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// パートA — すべてのアイテムを選択する（すべてのアイテムを表示する）
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// パートB — ソース値によって特定のアイテムのみを選択する
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **注意:** `PivotItem.IsHidden` を使用して複数選択フィルタリングを使用する場合、**少なくとも 1 つの `PivotItem` は表示されたままにする必要があります** (`IsHidden == false`)。すべてのアイテムが非表示になっている場合、Excel はファイルを開くときにクラッシュするか、空のピボットをレンダリングします。複数選択ホワイトリストにソースデータから少なくとも 1 つのアイテムが含まれていることを常に確認してください。

## **どの API とどのモードを使用すべきか?**

以下の表は、各シナリオの詳細を読むことなく適切な組み合わせを選択できるように、各 API とモードをいつ使用するかについてまとめたものです。

| シナリオ / ユースケース | 推奨 API | 使用するプロパティ | メモ |
|---|---|---|---|
| ソース列名でページフィールドを追加する (最も一般的) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | 高レベルで 1 行で完結します。`PivotField` 参照が必要ない場合はこれを使用してください。 |
| `PivotField` オブジェクトをすでに持っているときにページフィールドを追加する | `pivotTable.getPageFields().add(PivotField)` | n/a | フィールドオブジェクトが他の場所で取得された場合や再利用する必要がある場合に使用します。 |
| 単一のページアイテムにフィルタリングする (デフォルトモード) | `PivotField.CurrentPageItem` | 特定のインデックスに設定 | たとえば、`1` はソート済みリストの 2 番目のアイテムを表示します。 |
| すべてのアイテムを表示する / ページフィルタをクリアする | `PivotField.CurrentPageItem` | `0x7FFD` に設定 | マジック値 `0x7FFD` (10 進数 32765) は「すべてのアイテム」のセンチネル値です。 |
| Excel で複数選択 UI を有効化する | `PivotField.IsMultipleItemSelectionAllowed` | `true` に設定 | `IsHidden` 呼び出しが有効になる前に必要です。 |
| 複数選択リスト内の個々のアイテムを表示 / 非表示にする | `PivotItem.IsHidden` | アイテムごとに設定 | 少なくとも 1 つのアイテムは表示されたままにする必要があります (`IsHidden == false`)。 |

{{% alert color="primary" %}}
複数選択フィルタリングを構成するときは、可視性制約を常に覚えておいてください。複数選択ページフィールド内のすべての `PivotItem` が非表示になっている場合、Excel は開くときにクラッシュするか、空のピボットをレンダリングします。ソースデータに対してホワイトリストを構築し、少なくとも 1 つのアイテムが表示されたままになるようにして、保存したワークブックがすべてのマシンで確実に開くようにしてください。
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}