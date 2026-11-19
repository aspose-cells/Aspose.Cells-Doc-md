---
title: Aspose.Cells for Node.js via Java でピボットテーブルにフィルターフィールドを追加する
description: Aspose.Cells for Node.js via Java を使用して、ピボットテーブルのフィルターフィールドを追加および構成する方法を説明します。フィルターフィールドの追加、単一選択フィルタリング、複数選択フィルタリングを含みます。
linktitle: フィルターフィールドを追加
keywords: Aspose.Cells, Node.js via Java, ピボットテーブル, フィルターフィールド, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, フィルタ
type: docs
weight: 250
url: /ja/nodejs-java/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブル内のフィルターフィールドのライフサイクル全体をサポートします。高レベルの便利な API または低レベルの `PageFields` コレクションを通じてフィルターフィールドを追加でき、単一選択モードでページフィルタを駆動したり、すべてのページアイテムを表示するようにクリアしたり、フィールドを複数選択に切り替えて Excel のチェックボックス UI を通じてユーザーが複数のページアイテムを一度に選択できるようにすることができます。
{{% /alert %}}

## **はじめに**
フィルターフィールドは、ピボット本体が表示するソースデータの*どのサブセット*を制御するピボットフィールドです。エンドユーザーは Excel でレンダリングされたピボットの上部にあるドロップダウンとしてそれを見て、利用可能なページアイテムの 1 つを選択すると、そのページアイテムに属するレコードのみが要約されるようにピボット本体が再構築されます。ピボットフィールドは、`PivotFieldType.Row`、`PivotFieldType.Column`、または `PivotFieldType.Data` ではなく、`PivotFieldType.Page` として登録されたときにフィルターフィールドになります。
フィルターフィールドは 2 つの動作で動作します。デフォルトの**単一選択**動作では、一度に 1 つのページアイテムのみが表示されるため、ピボット本体は正確に 1 つのサブセットを要約します。**複数選択**動作では、フィールドはチェックボックスリストを公開し、ピボット本体はチェックされたすべてのページアイテムの和集合を要約します。同じソースフィールドは、単一プロパティを切り替えることによって、これらの動作間を前後に移動できます。
Aspose.Cells for Node.js via Java は、フィルターフィールドを登録する 2 つの同等の方法を公開しています。高レベル API は `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` であり、ソース列名を受け取り、1 回の呼び出しでフィールドを追加します。低レベル API は `pivotTable.getPageFields().add(PivotField)` であり、すでに `PivotField` 参照を保持しており、同じフィールドインスタンスをフィルター領域に追加する場合に使用されます。どちらの API も最終的に同じ `PageFields` コレクションにデータを格納し、この記事の残りの部分では、それらの選択方法と各フィルタリングモードの駆動方法について説明します。

## **フィルターフィールドの追加**
フィルター領域にピボットフィールドを登録するには 2 つの方法があります。高レベルの呼び出しはソース列名を文字列として受け取り、最も一般的なパスです。低レベルの呼び出しは既存の `PivotField` インスタンスを受け入れ、同じフィールドオブジェクトを複数のピボット領域で再利用する必要がある場合に便利です。どちらの呼び出しもフィールドを `pivotTable.getPageFields()` に配置し、その後、レンダリングされたピボットの上部にページドロップダウンとして表示されます。

### addFieldToArea によるフィルターフィールドの追加
次の例では、小さな Fruit / Year / Amount データセットを作成し、`Fruit` を行領域に、`Amount` をデータ領域に、`Year` をフィルター領域に持つピボットテーブルをセル E3 に配置し、ピボットを更新して、ワークブックを保存します。

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Set up the header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
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
// Add a pivot table anchored at cell E3
var pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.PAGE, "Year");
// Refresh and calculate the pivot table data
pivotTable.calculateData();
// Save the workbook
workbook.save("pageFieldSample.xlsx");
```

### getPageFields().add によるフィルターフィールドの追加
すでに `PivotField` インスタンスを操作している場合は、それを `pivotTable.getPageFields().add` に直接渡すことができます。ピボットテーブルとフィルターフィールドは前のシナリオとまったく同じように構築されます。最終的なフィルター領域の登録のみが低レベル API 呼び出しに置き換えられます。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
// Headers
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Add pivot table at E3 covering A1:C10
let pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **単一選択フィルタリング (1 つのページアイテムの表示)**
デフォルトの単一選択動作では、フィルターフィールドは単一のドロップダウンとしてレンダリングされ、`PivotField.CurrentPageItem` 整数がどのページアイテムがピボット本体を駆動するかを選択します。特定のインデックスを割り当てるとその 1 つのアイテムが選択されます。特別なセンチネル値 `0x7FFD` (10 進数 32765) を割り当てるとフィルタがクリアされ、すべてのページアイテムが一度に要約されます。単一選択がデフォルトです。明示的に有効化する必要はありません。

### すべてのアイテムの表示
`CurrentPageItem` をマジック値 `0x7FFD` に設定することは、ページフィルタをクリアすることと同等です。フィルタが適用されていないかのように、ピボット本体はすべてのページアイテムを要約します。

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
// Populate Fruit/Year/Amount data
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
// Create pivot table at E3
var pivotTables = sheet.getPivotTables();
var pivotTable = pivotTables.add("=A1:C7", 2, 4);
// Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.PAGE, "Year");
pivotTable.calculateData();
// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);
workbook.save("output.xlsx");
```

### 特定の 1 つのアイテムの表示
`CurrentPageItem` を実際のインデックスに設定すると、その 1 つのページアイテムのみが選択されます。インデックスはフィルターフィールドのソート済みアイテムリスト内のアイテムの位置であるため、たとえば `1` はソート後の 2 番目のアイテムを選択します。

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();
// Add sample data (Fruit/Year/Amount)
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
// Add pivot table at E3
var pivotTables = sheet.getPivotTables();
var pivotTable = pivotTables.add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.PAGE, "Year");
// Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **複数選択フィルタリング**
複数選択フィルタリングは、ページドロップダウンをチェックボックスリストに変え、エンドユーザーが複数のページアイテムを同時に選択できるようにします。Aspose.Cells は連携する 2 つのプロパティを公開しています。複数選択 UI がまったく機能するためには、`PivotField.IsMultipleItemSelectionAllowed` を `true` に設定する必要があります。有効化された後、`PivotItem.IsHidden` はチェックボックスリストに表示されるアイテムを制御するため、すべてのアイテムを表示するか、特定のアイテムのみをホワイトリストに登録するかのいずれかを選択できます。
以下のコードは、シナリオ 1a で構築された同じ Year フィルターフィールドで複数選択を有効化し、2 つのパターンを示します。パート A では、すべてのエントリの `IsHidden` を `false` に設定したままにすることで、すべてのページアイテムを表示します。一方、パート B では、選択したソース値のみをホワイトリストに登録し、`switch (pivotItems[i].getStringValue())` ブロックを使用して他のすべてを非表示にします。

```javascript
const AsposeCells = require("aspose.cells");
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data, Year→Page via AddFieldToArea).
//   Below we apply multi-select filtering on the page field.
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Sample data: Fruit | Year | Amount
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
const pivotTable = pivots.add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.PAGE, "Year");
// — Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Part A — select ALL items (make every item visible)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}
// Part B — select only specific items by source value
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
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **注意:** `PivotItem.IsHidden` を使用して複数選択フィルタリングを使用する場合、**少なくとも 1 つの `PivotItem` は表示されたままにする必要があります** (`IsHidden == false`)。すべてのアイテムが非表示になっている場合、Excel はファイルを開くときにクラッシュするか、空のピボットをレンダリングします。複数選択ホワイトリストにソースデータから少なくとも 1 つのアイテムが含まれていることを常に確認してください。

## **どの API とどのモードを使用すべきか?**
以下の表は、各シナリオの詳細を読むことなく適切な組み合わせを選択できるように、各 API とモードをいつ使用するかについてまとめたものです。
| シナリオ / ユースケース | 推奨 API | 使用するプロパティ | メモ |
|---|---|---|---|
| ソース列名でフィルターフィールドを追加する (最も一般的) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | 高レベルで 1 行で完結します。`PivotField` 参照が必要ない場合はこれを使用してください。 |
| `PivotField` オブジェクトをすでに持っているときにフィルターフィールドを追加する | `pivotTable.getPageFields().add(PivotField)` | n/a | フィールドオブジェクトが他の場所で取得された場合や再利用する必要がある場合に使用します。 |
| 単一のページアイテムにフィルタリングする (デフォルトモード) | `PivotField.CurrentPageItem` | 特定のインデックスに設定 | たとえば、`1` はソート済みリストの 2 番目のアイテムを表示します。 |
| すべてのアイテムを表示する / ページフィルタをクリアする | `PivotField.CurrentPageItem` | `0x7FFD` に設定 | マジック値 `0x7FFD` (10 進数 32765) は「すべてのアイテム」のセンチネル値です。 |
| Excel で複数選択 UI を有効化する | `PivotField.IsMultipleItemSelectionAllowed` | `true` に設定 | `IsHidden` 呼び出しが有効になる前に必要です。 |
| 複数選択リスト内の個々のアイテムを表示 / 非表示にする | `PivotItem.IsHidden` | アイテムごとに設定 | 少なくとも 1 つのアイテムは表示されたままにする必要があります (`IsHidden == false`)。 |

{{% alert color="primary" %}}
複数選択フィルタリングを構成するときは、可視性制約を常に覚えておいてください。複数選択フィルターフィールド内のすべての `PivotItem` が非表示になっている場合、Excel は開くときにクラッシュするか、空のピボットをレンダリングします。ソースデータに対してホワイトリストを構築し、少なくとも 1 つのアイテムが表示されたままになるようにして、保存したワークブックがすべてのマシンで確実に開くようにしてください。
{{% /alert %}}

{{< app/cells/assistant language="nodejs-java" >}}