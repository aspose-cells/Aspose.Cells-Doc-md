---
title: Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加する
linktitle: フィルターフィールドを追加
description: Aspose.Cells for Node.js via C++ を使用してピボットテーブルのフィルターフィールドを追加および構成する方法について説明します。フィルターフィールドの追加、単一選択フィルタリング、複数選択フィルタリングを含みます。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, フィルターフィールド, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, フィルター
type: docs
weight: 250
url: /ja/nodejs-cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はピボットテーブル内のフィルターフィールドのライフサイクル全体をサポートします。高レベルの便利な API または下位の `PageFields` コレクションを通じてフィルターフィールドを追加でき、単一選択モードでページフィルタを駆動したり、すべてのフィルター項目を表示するためにクリアしたり、Excel のチェックボックス UI を通じてユーザーが複数のフィルター項目を一度に選択できるようにフィールドを複数選択に切り替えることができます。
{{% /alert %}}

## **はじめに**

フィルターフィールドは、ピボット本体が表示するソースデータの*どのサブセット*を制御するピボットフィールドです。エンドユーザーは、Excel でレンダリングされたピボットの上部にあるドロップダウンとしてそれを表示し、利用可能なフィルター項目のいずれかを選択すると、そのフィルター項目に属するレコードのみが集計されるようにピボット本体が再構築されます。ピボットフィールドは、`PivotFieldType.Row`、`PivotFieldType.Column`、または `PivotFieldType.Data` ではなく `PivotFieldType.Page` として登録されたときにフィルターフィールドになります。

フィルターフィールドは2つの動作で動作できます。デフォルトの**単一選択**動作では、一度に1つのフィルター項目のみが表示されるため、ピボット本体は正確に1つのサブセットを集計します。**複数選択**動作では、フィールドはチェックボックスリストを公開し、ピボット本体はチェックされたすべてのフィルター項目の和集合を集計します。同じソースフィールドは、単一のプロパティを切り替えることによって、これらの動作間で前後に移動できます。

Aspose.Cells for Node.js via C++ は、フィルターフィールドを登録するための2つの同等の方法を公開しています。高レベル API は `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` であり、ソース列名を受け取り、単一の呼び出しでフィールドを追加します。下位レベル API は `PivotTable.pageFields.add(PivotField)` であり、すでに `PivotField` 参照を保持していて、同じフィールドインスタンスをフィルター領域に追加したい場合に使用されます。両方の API は最終的に同じ `PageFields` コレクションに格納され、この記事の残りでは、それらの間を選択する方法と各フィルタリングモードを駆動する方法を示します。

## **フィルターフィールドの追加**

フィルター領域にピボットフィールドを登録するには2つの方法があります。高レベルの呼び出しはソース列名を文字列として受け取り、最も一般的なパスです。下位レベルの呼び出しは既存の `PivotField` インスタンスを受け取り、同じフィールドオブジェクトを複数のピボット領域で再利用する場合に便利です。両方の呼び出しはフィールドを `PivotTable.pageFields` に配置し、その後、レンダリングされたピボットの上部にページドロップダウンとして表示されます。

### addFieldToArea を使用したフィルターフィールドの追加

次の例では、小さな Fruit / Year / Amount データセットを構築し、セル E3 にピボットテーブルを配置します。`Fruit` を行領域に、`Amount` をデータ領域に、`Year` をフィルター領域に配置し、ピボットを更新して、ワークブックを保存します。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// ヘッダー行を設定する
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9行のサンプルデータ（Fruit、Year、Amount）を入力する
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

// セルE3を起点にピボットテーブルを追加する
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドをそれぞれのエリアに追加する：Fruitは行、Amountはデータ、Yearはページフィールド
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// ピボットテーブルのデータを更新して計算する
pivotTable.calculateData();

// ワークブックを保存する
workbook.save("pageFieldSample.xlsx");
```

### pageFields.add を使用したフィルターフィールドの追加

すでに `PivotField` インスタンスを操作している場合は、それを `PivotTable.pageFields.add` に直接渡すことができます。ピボットテーブルとフィルターフィールドは前のシナリオとまったく同じように構築されます。最終的なフィルター領域の登録のみが下位レベルの API 呼び出しに置き換えられます。

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// ヘッダー
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// サンプルデータ（9行）
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// E3 に A1:C10 をカバーするピボットテーブルを追加
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> 行、Amount -> データ（Year は下記 Page に配置）
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 低レベルアプローチ：BaseFields から既存の Year PivotField を取得し、
// PageFields.Add(PivotField) 経由で Page 領域に登録する。
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// 新しいページフィールドが保存されたワークブックに反映されるようにリフレッシュ
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **単一選択フィルタリング(1つのフィルター項目の表示)**

デフォルトの単一選択動作では、フィルターフィールドは単一のドロップダウンとしてレンダリングされ、`PivotField.currentPageItem` 整数が、ピボット本体を駆動するフィルター項目を選択します。特定のインデックスを割り当てるとその項目が選択されます。特別なセンチネル値 `0x7FFD`(10進数で 32765)を割り当てると、フィルタがクリアされ、すべてのフィルター項目が一度に集計されます。単一選択がデフォルトです。明示的に有効化する必要はありません。

### すべての項目の表示

`currentPageItem` をマジック値 `0x7FFD` に設定することは、ページフィルタをクリアすることと同等です。ピボット本体は、フィルタが適用されていないかのように、すべてのフィルター項目を集計します。

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Fruit/Year/Amount のデータを入力
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// E3 にピボットテーブルを作成
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// ピボットフィールドを設定: Fruit→行、Amount→データ、Year→ページ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// ページフィールドのフィルターをクリアし、ページフィールドの全項目を表示可能にする。
// 0x7FFD（10進数で32765）は「すべての項目」を意味する特別なセンチネル値です —
// Excel のページフィールド ドロップダウンで「(すべて)」を選択するのと同等です。
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### 1つの特定の項目の表示

`currentPageItem` を実際のインデックスに設定すると、その1つのフィルター項目のみが選択されます。インデックスはフィルターフィールドのソート済み項目リスト内の項目の位置であるため、たとえば `1` はソート後の2番目の項目を選択します。

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// サンプルデータを追加（フルーツ/年/金額）
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// E3にピボットテーブルを追加
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// フィールドを追加：Fruit→行、Amount→データ、Year→ページ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// ページフィールド固有の操作
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = ソート順の2番目の項目（例：「2021」）

// ピボットテーブルを更新して計算
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **複数選択フィルタリング**

複数選択フィルタリングは、ページドロップダウンをチェックボックスリストに変え、エンドユーザーが複数のフィルター項目を同時に選択できるようにします。Aspose.Cells は連携して機能する2つのプロパティを公開しています。`PivotField.isMultipleItemSelectionAllowed` は、複数選択 UI がまったく有効になる前に `true` に設定する必要があります。有効化された後、`PivotItem.isHidden` はチェックボックスリストに表示される項目を制御するため、すべての項目を表示するか、特定の項目のみをホワイトリストに登録することができます。

以下のコードは、シナリオ 1a で構築された同じ Year フィルターフィールドで複数選択を有効化し、2つのパターンを示します。パート A では、すべてのエントリの `isHidden` を `false` のままにしておくことで、すべてのフィルター項目を公開します。一方、パート B では、選択したソース値のみをホワイトリストに登録し、`switch (pivotItems[i].getStringValue())` ブロックを介してその他すべてを非表示にします。

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// サンプルデータ：果物 | 年 | 数量
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// ページフィールドで複数選択を有効にする
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// パートA — すべてのアイテムを選択する（すべてのアイテムを表示する）
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// パートB — ソース値で特定のアイテムのみを選択する
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **注意:** `PivotItem.isHidden` を介して複数選択フィルタリングを使用する場合、**少なくとも 1 つの `PivotItem` を表示状態のままにしておく必要があります**(`isHidden == false`)。すべての項目が非表示になっている場合、Excel はファイルを開くときにクラッシュするか、空のピボットをレンダリングします。複数選択のホワイトリストにソースデータの少なくとも 1 つの項目が含まれていることを常に確認してください。

## **どの API とどのモードを使用すべきか?**

次の表は、各シナリオを詳しく読みなくても適切な組み合わせを選択できるように、各 API とモードをいつ使用するかをまとめたものです。

| シナリオ / ユースケース | 推奨 API | 使用するプロパティ | メモ |
|---|---|---|---|
| ソース列名でフィルターフィールドを追加する(最も一般的) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | 高レベル、1 行で完了します。`PivotField` 参照が必要な場合を除き、これを使用してください。 |
| すでに `PivotField` オブジェクトを保持している場合にフィルターフィールドを追加する | `PivotTable.pageFields.add(PivotField)` | n/a | フィールドオブジェクトが他の場所で取得された場合や再利用する必要がある場合に使用します。 |
| 単一のフィルター項目にフィルタリングする(デフォルトモード) | `PivotField.currentPageItem` | 特定のインデックスに設定 | たとえば、`1` はソート済みリストの 2 番目の項目を表示します。 |
| すべての項目を表示する / ページフィルタをクリアする | `PivotField.currentPageItem` | `0x7FFD` に設定 | マジック値 `0x7FFD`(10進数で 32765)は「すべての項目」のセンチネルです。 |
| Excel で複数選択 UI を有効化する | `PivotField.isMultipleItemSelectionAllowed` | `true` に設定 | `isHidden` の呼び出しが有効になる前に必要です。 |
| 複数選択リストで個々の項目を非表示 / 表示する | `PivotItem.isHidden` | 項目ごとに設定 | 少なくとも 1 つの項目を表示状態のままにしておく必要があります(`isHidden == false`)。 |

{{% alert color="primary" %}}
複数選択フィルタリングを構成するときは、常に可視性の制約を覚えておいてください。複数選択フィルターフィールドのすべての `PivotItem` が非表示になっている場合、Excel は開くときにクラッシュするか、空のピボットをレンダリングします。ソースデータに対してホワイトリストを構築し、少なくとも 1 つの項目が表示されたままになるようにし、保存されたワークブックがすべてのマシンで確実に開けるようにしてください。
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}
