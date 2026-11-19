---
title: ラベルや値によるピボットテーブルのフィルタリング
linktitle: ラベルや値によるピボットテーブルのフィルタリング
description: Aspose.Cells for Node.js via C++ は包括的なピボットテーブルフィルタリング機能をサポートします。この記事では、ラベルフィルタ、日付フィルタ、値フィルタ、トップ10フィルタを使用してピボットテーブルデータをフィルタリングする方法や、ピボットアイテムを非表示・再表示する方法について説明します。
keywords: Aspose.Cells, Node.js via C++ ライブラリ, スプレッドシート, ピボットテーブル, フィルタ, ラベルフィルタ, 値フィルタ, 日付フィルタ, トップ10フィルタ, ピボットアイテム, ピボットアイテムの非表示
type: docs
weight: 10
url: /ja/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルタリングするための 5 つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルタを適用したり、フィールドに日時セルのみまたは空白のみが含まれる場合に日付フィルタを使用したり、集計された数値に対して値フィルタを適用したり、値フィールドによるランキングにトップ 10 フィルタを使用したり、`IsHidden` プロパティを使用して個々のピボットアイテムを手動で非表示または再表示したりできます。各戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}

## **Introduction**
ピボットテーブルは強力な分析ツールですが、生の集計には、特定のレポートで必要となる情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、ピボットテーブルを特定のレポートに関連する行、列、値のみに絞り込むための主要なメカニズムです。Aspose.Cells for Node.js via C++ は、Microsoft Excel で利用可能なフィルタリング機能をミラーリングし、レポート生成を完全に自動化できるようにプログラム的に公開します。
この記事で扱うフィルタリング戦略は次のとおりです。
1. **ラベルフィルタ** — 行または列フィールドのアイテムをテキストラベルに基づいてフィルタリングします。
2. **日付フィルタ** — 日時値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルタ** — データフィールドの集計値に基づいてアイテムをフィルタリングします。
4. **トップ 10 フィルタ** — 値フィールドによってランク付けされた上位または下位 N 個のアイテムのみを表示します。
5. **ピボットアイテムの非表示 / 再表示** — フィールド内の各アイテムの表示を手動で制御します。
各アプローチは、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルタを適用した後、新しいフィルタ状態を反映してキャッシュされたデータと計算値を更新するため、ピボットテーブルで `getPivotCache().refresh()` を呼び出す必要があります。

## **Label Filter**
ラベルフィルタを使用すると、行または列フィールドのアイテムを、テキストキャプションとパターンを比較してフィルタリングできます。これは、名前の先頭が特定の文字で始まる製品、特定の単語を含む製品、またはその他のキャプションベースの基準に一致する製品のみを表示する場合に便利です。
Aspose.Cells は、`PivotField.filterByLabel(PivotFilterType, string)` メソッドを通じてラベルフィルタリングを公開しています。`PivotFilterType` 列挙型には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数は、比較に使用されるラベル文字列を指定します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定された接頭辞で始まるアイテムのみが表示されるようにラベルフィルタを適用し、ピボットテーブルを更新して結果を保存します。

```javascript
const AsposeCells = require("aspose.cells.node");
let fileName = "sample.xlsx";
let prefix = "B";
// Load the existing workbook containing a pivot table
let workbook = new AsposeCells.Workbook(fileName);
// Access the worksheet by index (first worksheet)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
let rowField = pivotTable.getRowFields().get(0);
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **Date Filter**
日付フィルタを使用すると、今日、先週、今月、次の四半期、または特定の日付範囲などの日付ベースの基準でピボットテーブルを絞り込むことができます。これらは、日時情報を格納するフィールドに対してのみ機能するフィルタです。

{{% alert color="primary" %}}
日付フィルタは、行または列エリアに日時セルのみまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルタは期待どおりの結果を生成しません。このフィルタを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
Aspose.Cells は、`PivotField.filterByDate(PivotFilterType, params DateTime[] values)` メソッドを通じて日付フィルタリングを公開しています。`PivotFilterType` 列挙型には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用日付値が含まれます。選択したフィルタタイプに応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行エリアに日付フィールドを含むピボットテーブルを含むワークブックを読み込み、表示範囲を特定の日付範囲に制限する日付フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");
const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
const workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
const worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
const pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
const dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **Value Filter**
値フィルタは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的な使用例としては、売上合計が目標額を超える製品のみを表示したり、取引件数が範囲内に収まる地域のみを表示したりすることが挙げられます。
Aspose.Cells は、`PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` メソッドを通じて値フィルタリングを公開しています。`filterType` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`valueField` パラメータは評価するデータフィールドを指定し、最後の引数はしきい値を指定します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```javascript
const AsposeCells = require("aspose.cells.node");
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Top 10 Filter**
トップ 10 フィルタは、選択した値フィールドに基づいて最高または最低の N 個のアイテムのみを保持する、値フィルタの特殊な形式です。「売上によるトップ 10 製品」や「販売件数によるボトム 5 地域」などのランキングレポートで一般的に使用されます。

{{% alert color="primary" %}}
トップ 10 フィルタは、ピボットテーブルにデータ領域に 1 つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも 1 つの値フィールドがないと、アイテムをランク付けするための集計されたメジャーがないため、フィルタを適用できません。
Aspose.Cells は `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)` メソッドを通じて Top 10 フィルターを提供します。`valueFieldIndex` パラメーターは項目のランク付けに使用されるデータ フィールドのインデックスであり、`filterType` は `itemCount` の単位を選択します（`PivotFilterType.Count` は固定数の項目を保持し、`PivotFilterType.Percent` は項目の割合を保持するため、`itemCount` がその割合の値になります）。`isTop` は上位の項目（true）か下位の項目（false）のどちらを保持するかを示し、`itemCount` は保持する項目数または割合を定義します。
次の例では、値フィールドを含むピボットテーブルを含むワークブックを読み込み、売上の合計による上位 10 個のアイテムのみを保持するトップ 10 フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
// Load the existing workbook that contains the pivot table
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
const worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
const pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
const rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
const valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **Filter by Hiding or Unhiding Pivot Items**
構造化されたフィルタ API に加えて、Aspose.Cells では各ピボットアイテムの表示を直接制御することもできます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルタを適用せずに特定のアイテムを選択的に非表示にできます。`IsHidden = true` を設定すると、アイテムがピボットテーブルから非表示になります。`IsHidden = false` を設定すると、アイテムの非表示が解除され、再び表示されるようになります。
このアプローチは、フィルタリングルールが不規則である、またはアイテム固有である場合、たとえば特定のレポートに表示すべきでない少数の名前付きカテゴリを非表示にする場合に役立ちます。以下の例では、ピボットテーブルを読み込み、特定のアイテムを名前で非表示にし、再表示する方法を実演し、ピボットテーブルを更新してワークブックを保存します。

```javascript
const AsposeCells = require("aspose.cells.node");
// Load an existing workbook containing a pivot table
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
const sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
const pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
const pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **Summary**
Aspose.Cells for Node.js via C++ は、Microsoft Excel で利用可能な機能と一致する、完全なピボットテーブルフィルタリング機能を提供します。ラベル、値、および日付フィルタは最も一般的な分析シナリオをカバーし、トップ 10 フィルタはランキングレポートを処理します。フィルタリングルールが不規則な場合、`PivotItem.IsHidden` プロパティは柔軟なアイテムレベルのフォールバックを提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルタを適用してから特定のアイテムを非表示にする）ことで、完全にコードから正確に対象を絞ったピボットテーブルレポートを作成できます。

## Related Articles
- [ピボットテーブルの挿入](/cells/ja/nodejs-cpp/create-pivot-table/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルの行と列フィールドを追加する](/cells/ja/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルにページフィールドを追加する](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルの値フィールドを管理する](/cells/ja/nodejs-cpp/manage-value-fields/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルとピボットキャッシュを更新する](/cells/ja/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}