---
title: ピボットテーブルでの Top 10 の表示またはフィルター
linktitle: ピボットテーブルでの Top 10 の表示またはフィルター
description: Aspose.Cells for Node.js via C++ を使用して、ピボットフィールドで上位または下位の項目のみを表示する方法を学びます。この ensinarでは、Excel 97-2003 の Top10AutoShow メソッド、Top10AutoShowSettings によるオプションの読み取り、FilterTop10 による Excel 2007-365 の Top 10 フィルターについて説明します。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, 上位 10, 自動表示, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /ja/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十のメンバーがある場合に読みにくくなることがあります。Top 10 レポートでは、順位の上位または下位の項目だけが表示されるため、「売上による上位 5 製品」や「販売数による下位 3 地域」など、ランキングレポートに最適です。Aspose.Cells はこの機能として 2 つのメカニズムをサポートしており、それぞれ Microsoft Excel の 2 つの世代に対応しています。
- **Excel 97-2003 AutoShow** — `pivotField.top10AutoShow()` メソッドです。ピボットフィールドに直接保存される古典的な「上位/下位 N 項目を表示」設定です。元のピボットテーブル形式の一部であるため、新旧すべての Excel バージョンで動作します。
- **Excel 2007-365 Top 10 フィルター** — `pivotField.filterTop10()` メソッドです。フィールドメニューの「値フィルター」にある新しい Top 10 値フィルターです。フィールドに関連付けられた `PivotFilter` オブジェクトとして保存され、項目数と割合に基づくランキングに対応します。

## **Excel 97-2003 での Top 10 表示 (top10AutoShow)**
古典的な AutoShow は、1 回の `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)` 呼び出しで設定します。
- `isAutoShow` — フィールドの AutoShow 設定を有効または無効にします。
- `isTop` — `true` の場合は順位の上位の項目（Top）を保持し、`false` の場合は下位の項目（Bottom）を保持します。
- `count` — 保持する項目数です。古典的な Top 10 レポートでは 10 などを指定します。
- `rankBy` — 項目を順位付けする基準となる **データフィールド** の 0 開始インデックスです。フィールド自体を使用して項目を順位付けする場合は -1 を指定します。
ランキングは、値フィールドまたはフィールド自体で決定できます。下面に、代表的な 2 つの例を示します。

### **値フィールドによるランキング**
行フィールドの項目を、`Sales` の合計のような通常の値フィールドに基づいて順位付けします。次の例では、行フィールド (`Sport`) とデータフィールド (`Sales`) を 1 つずつ持つピボットテーブルを作成し、売上上位 2 つのスポーツを表示します。`Sales` の合計がインデックス 0 のデータフィールドであるため、`rankBy` は 0 です。

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **フィールド自体によるランキング**
フィールド自体で順位付けすることもできます。その場合は `rankBy` に -1 を指定します。このバリエーションでは追加のデータフィールドは不要であり、フィールドを行（または列）領域に配置するだけです。次の例では、フィールド自体で順位付けした下位 3 つのスポーツを表示します。この設定を保存すると、-1 がこの形式の既定値であるため、ピボットテーブル XML から `rankBy` 属性が省略されます。また、`top10AutoShowSettings.getRankBy()` は -1 を読み取ります。

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **現在のオプションの読み取り (Top10AutoShowSettings)**
`pivotField.getTop10AutoShowSettings()` ゲッターは、フィールドに現在保存されている AutoShow オプションを公開する `PivotFieldTop10AutoShowSettings` オブジェクトを返します。既存のワークブックや、直前に設定したピボットテーブルが項目をどのように表示するかを調べる場合に使用します。ファイルから読み込んだワークブックにも使用できます。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

4 つのプロパティは、ピボットテーブル XML に書き込まれる古典的な AutoShow 属性 (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) に対応しています。したがって、読み取られた値は、すべての Excel バージョンで適用される設定値です。

## **注記**

{{% alert color="primary" %}}
- `PivotField` の直接のゲッターである `isAutoShow`、`getIsAscendShow()`、`getAutoShowCount()`、`getAutoShowField()` は非推奨になっています。代わりに `Top10AutoShowSettings` オブジェクトを使用してください。`pivotField.isAutoShow` は `top10AutoShowSettings.isAutoShow` に、`pivotField.getIsAscendShow()` は `top10AutoShowSettings.isTop` に、`pivotField.getAutoShowCount()` は `top10AutoShowSettings.getAutoShowCount()` に、`pivotField.getAutoShowField()` は `top10AutoShowSettings.getRankBy()` に対応します。設定を変更するには、`pivotField.top10AutoShow()` メソッドを使用してください。
- `top10AutoShow()` は行フィールドと列フィールドで機能します。ページ（フィルター）領域にのみ存在するフィールドは、項目がピボットテーブルの本体領域に配置されないため、この方法では順位付けできません。
{{% /alert %}}

## **Excel 2007-365 の Top 10 フィルター (filterTop10)**
新しい Excel バージョンでは、フィールドメニューの「値フィルター」にある「Top 10...」で、Top 10 を値フィルターとして利用できます。Aspose.Cells はこの機能を `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)` メソッドでモデル化しています。このメソッドは、作成された `PivotFilter` を返します。
- `valueFieldIndex` — 集計値に基づいて項目を順位付けするデータフィールドの 0 開始インデックスです。
- `type` — `itemCount` の意味を指定します。`PivotFilterType.Count` は固定数の項目を保持します（ダイアログの「項目数」オプション）。`PivotFilterType.Percent` は項目の割合を保持するため、`itemCount` は割合そのものになります。30 を指定すると、上位 30% が保持されます。`PivotFilterType.SUM` は累積値のカバレッジに基づいて順位付けします。
- `isTop` — `true` の場合は Top、`false` の場合は Bottom を指定します。
- `itemCount` — Top N の N を指定します。その単位は `type` によって異なります。

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` と `filterTop10` は異なる機能です。AutoShow は、ピボットフィールドに古典的な `autoShow` 属性を書き込むため、Excel 97 以降のすべての Excel バージョンで適用されます。`filterTop10` はモダンな `PivotFilter` エントリを作成するため、Excel 2007 以降が必要です。古い Excel バージョンでワークブックを開くと、新しいフィルターを使用するピボットテーブルは、すべての項目を表示する動作にフォールバックします。レガシートールとの往復処理が必要なドキュメントでは `top10AutoShow` を、モダンなワークブックでは `filterTop10` を優先してください。`filterTop10` は他の値フィルターと組み合わせることができるためです。
{{% /alert %}}

## **関連記事**
- [ラベルまたは値によるピボットテーブルのフィルター](/cells/ja/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルに行と列のフィールドを追加](/cells/ja/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/nodejs-cpp/refresh-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}