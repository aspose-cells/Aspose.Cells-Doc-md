---
title: ピボットテーブルでの上位 10 件の表示またはフィルター
linktitle: ピボットテーブルでの上位 10 件の表示またはフィルター
description: Aspose.Cells for Node.js via Java を使用して、ピボットフィールド内の項目のうち、順位の上位または下位にある項目のみを表示する方法を学びます。この文書では、Excel 97-2003 の Top10AutoShow メソッド、Top10AutoShowSettings によるオプションの読み取り、および FilterTop10 による Excel 2007-365 の上位 10 件フィルターについて説明します。
keywords: Aspose.Cells, Node.js via Java, ピボットテーブル, 上位 10 件, 自動表示, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /ja/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十のメンバーがいると読みにくくなることがあります。上位 10 件レポートは、順位の上位または下位にある項目だけを残します。これは、まさにランキングレポートで必要とされる「売上上位の製品 5 個」や「販売件数下位の地域 3 件」を実現します。Aspose.Cells はこの機能に 2 つのメカニズムを提供しており、Microsoft Excel の 2 つの世代にそれぞれ対応しています。
- **Excel 97-2003 自動表示** — `PivotField.top10AutoShow()` メソッド。これは、ピボットフィールドに直接格納される従来の「上位/下位 N 項目を表示」設定です。元のピボットテーブル形式の一部であるため、新旧すべての Excel バージョンで動作します。
- **Excel 2007-365 上位 10 件のフィルター** — `PivotField.filterTop10()` メソッド。これは、フィールドメニューの「値フィルター」にある「上位 10 件」という新しい値フィルターです。フィールドに関連付けられた `PivotFilter` オブジェクトとして保存され、項目数とパーセントのいずれかに基づくランキングを提供します。

## **Excel 97-2003 における上位 10 件の自動表示（Top10AutoShow）**
従来型の自動表示は、`PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` を 1 回呼び出すことで設定します。
- `isAutoShow` — フィールドの自動表示設定を有効または無効にします。
- `isTop` — `true` の場合は上位の項目（Top）を保持し、`false` の場合は下位の項目（Bottom）を保持します。
- `count` — 保持する項目数です。たとえば、従来の上位 10 件レポートでは 10 を指定します。
- `rankBy` — 項目を順位付けする基準となる値を持つ**データフィールド**の 0 から始まるインデックスです。フィールド自体を基準に項目を順位付けする場合は、-1 を指定します。
順位付けの基準は値フィールドまたはフィールド自体にできます。以下に、代表的な 2 つの方式を示します。

### **値フィールドによる順位付け**
行フィールドの項目を、「Sales の合計」のような通常の値フィールドで順位付けします。次の例では、1 つの行フィールド（`Sport`）と 1 つのデータフィールド（`Sales`）を持つピボットテーブルを作成し、売上に基づく上位 2 件のスポーツを表示します。`rankBy` が 0 なのは、「Sales の合計」がインデックス 0 のデータフィールドだからです。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **フィールド自体による順位付け**
フィールド自体で順位付けすることもできます。この場合は `rankBy` に -1 を渡します。この方式では追加のデータフィールドは不要です。フィールドが行領域（または列領域）にあるだけで十分です。次の例では、フィールド自体による順位付けで下位 3 件のスポーツを表示します。この設定を保存すると、-1 がこの形式の既定値であるため、`rankBy` 属性はピボットテーブル XML から省略されます。また、`getTop10AutoShowSettings().getRankBy()` から -1 が読み戻されます。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **現在のオプションの読み取り（Top10AutoShowSettings）**
`PivotField.getTop10AutoShowSettings()` メソッドは、フィールドに現在格納されている自動表示オプションを公開する `PivotFieldTop10AutoShowSettings` オブジェクトを返します。このオブジェクトを使用すると、既存のワークブックや、設定したばかりのピボットテーブルで項目がどのように表示されるかを確認できます。ファイルから読み込んだワークブックも対象です。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

`isAutoShow()`、`isTop()`、`getAutoShowCount()`、`getRankBy()` の各ゲッターは、ピボットテーブル XML（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`）に書き込まれる従来型の自動表示属性に対応しています。したがって、読み戻される値は、すべての Excel バージョンで有効となる値です。

## **注意**

{{% alert color="primary" %}}
- 直接使用する `PivotField` のゲッター `isAutoShow()`、`isAscendShow()`、`getAutoShowCount()`、`getAutoShowField()` は_obsolete_ としてマークされています。代わりに `getTop10AutoShowSettings()` オブジェクトを使用してください。`isAutoShow()` は `getTop10AutoShowSettings().isAutoShow()`、`isAscendShow()` は `getTop10AutoShowSettings().isTop()`、`getAutoShowCount()` は `getTop10AutoShowSettings().getAutoShowCount()`、`getAutoShowField()` は `getTop10AutoShowSettings().getRankBy()` に置き換えられます。設定を変更するには、サポートされている `top10AutoShow()` メソッドを使用してください。
- `top10AutoShow()` は行フィールドと列フィールドで動作します。ページ（フィルター）領域にのみ置かれたフィールドは、項目がピボットテーブルの本体に配置されていないため、この方法では順位付けできません。
{{% /alert %}}

## **Excel 2007-365：上位 10 件のフィルター（FilterTop10）**
現代の Excel バージョンでは、フィールドメニューの「値フィルター」に「上位 10 件...」という値フィルターがあります。Aspose.Cells は、`PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` メソッドでこの機能に対応しています。このメソッドは、作成された `PivotFilter` を返します。
- `valueFieldIndex` — 集計値によって項目を順位付けするデータフィールドの 0 から始まるインデックスです。
- `type` — `itemCount` の意味を定義します。`PivotFilterType.COUNT` は固定数の項目を保持します（ダイアログの「項目数」オプション）。`PivotFilterType.PERCENT` は項目の一定割合を保持します。この場合、`itemCount` はパーセント値そのものになるため、30 を指定すると上位 30 パーセントの項目が保持されます。`PivotFilterType.SUM` は累積値に基づいて項目を順位付けします。
- `isTop` — 上位の場合は `true`、下位の場合は `false` を指定します。
- `itemCount` — 「上位 N 件」の N の値です。単位は `type` によって異なります。

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` と `filterTop10()` は別々の機能です。自動表示は、ピボットフィールドに設定される従来型の `autoShow` 属性を書き込み、Excel 97 以降のすべての Excel バージョンで尊重されます。`filterTop10()` は新しい `PivotFilter` エントリを書き込むため、Excel 2007 以降が必要です。古い Excel バージョンでワークブックを開くと、新しいフィルターを使用しているピボットテーブルはフォールバックして、すべての項目を表示します。旧来のツールで往復処理する必要がある文書では `top10AutoShow()` を推奨してください。新しいワークブックでは、他の値フィルターと併用できる `filterTop10()` を推奨してください。
{{% /alert %}}

## **関連記事**
- [ラベルまたは値によるピボットテーブルのフィルター](/cells/ja/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルに行フィールドと列フィールドを追加](/cells/ja/nodejs-java/pivot-table-add-row-and-column-fields/)
- [ピボットテーブル内でピボットフィールドをグループ化](/cells/ja/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/nodejs-java/refresh-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}