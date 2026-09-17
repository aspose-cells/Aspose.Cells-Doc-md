---
title: ラベルまたは値によるピボットテーブルのフィルタリング
linktitle: ラベルまたは値によるピボットテーブルのフィルタリング
description: Aspose.Cells for Node.js via Java は、ピボットテーブルの包括的なフィルタリング機能をサポートしています。この記事では、ラベルフィルタ、日付フィルタ、値フィルタ、トップ10フィルタ、およびピボットアイテムの非表示/再表示によるピボットテーブルデータのフィルタリング方法について説明します。
keywords: Aspose.Cells, Node.js via Java ライブラリ, ピボットテーブル, フィルタ, ラベルフィルタ, 値フィルタ, 日付フィルタ, トップ10フィルタ, ピボットアイテム, ピボットアイテムを非表示
type: docs
weight: 10
url: /ja/nodejs-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルタリングするための5つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルタを適用したり、フィールドに日時セルのみまたは空白のみが含まれる場合に日付フィルタを使用したり、集計値に対して値フィルタを適用したり、値フィールドによるランク付けにトップ10フィルタを使用したり、`IsHidden` プロパティを使用して個々のピボットアイテムを手動で非表示または再表示したりできます。各戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}

## **Introduction**
ピボットテーブルは強力な分析ツールですが、生の集計には提示する必要がある情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、ピボットテーブルを特定のレポートにとって重要な行、列、値に絞り込むための主要なメカニズムです。Aspose.Cells for Node.js via Java は、Microsoft Excel で利用可能なフィルタリング機能を反映し、レポート生成を完全に自動化できるようにプログラム的に公開しています。
この記事で説明するフィルタリング戦略は以下の通りです。
1. **ラベルフィルタ** — テキストラベルに基づいて行または列フィールドのアイテムをフィルタリングします。
2. **日付フィルタ** — 日時値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルタ** — データフィールドの集計値に基づいてアイテムをフィルタリングします。
4. **トップ10フィルタ** — 値フィールドによってランク付けされた上位または下位 N 個のアイテムのみを表示します。
5. **ピボットアイテムの非表示/再表示** — フィールド内の各アイテムの表示を手動で制御します。
各アプローチでは、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルタを適用した後、ピボットテーブルのキャッシュデータと計算値が新しいフィルタ状態を反映するように、`refreshData()` と `calculateData()` を呼び出す必要があります。

## **Label Filter**
ラベルフィルタを使用すると、行または列フィールドのアイテムを、テキストキャプションとパターンで比較することでフィルタリングできます。これは、特定の文字で始まる名前、特定の単語を含む名前、またはその他のキャプションベースの基準に一致する製品のみを表示する場合に便利です。
Aspose.Cells は、`PivotField.filterByLabel(PivotFilterType, string)` メソッドを通じてラベルフィルタリングを公開しています。`PivotFilterType` 列挙型には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2番目の引数は、比較に使用されるラベル文字列を提供します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定されたプレフィックスで始まるアイテムのみが表示されるようにラベルフィルタを適用し、ピボットテーブルを更新して結果を保存します。

```javascript
let fileName = "sample.xlsx";
let prefix = "B";
// ピボットテーブルを含む既存のワークブックを読み込む
let workbook = new AsposeCells.Workbook(fileName);
// インデックスでワークシートにアクセスする（最初のワークシート）
let worksheet = workbook.getWorksheets().get(0);
// インデックスでピボットテーブルにアクセスする
let pivotTable = worksheet.getPivotTables().get(0);
// 最初の行のPivotFieldを取得する
let rowField = pivotTable.getRowFields().get(0);
// ラベルフィルターを適用する — ラベルが指定された接頭辞で始まる行項目のみを表示する
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");
// ピボットテーブルのデータを更新して再計算し、フィルターを反映する
pivotTable.getPivotCache().refresh();
// ワークブックをディスクに保存する
workbook.save(fileName);
```

## **Date Filter**
日付フィルタを使用すると、今日、先週、今月、次の四半期、または特定の日付範囲などの日付ベースの基準でピボットテーブルを絞り込むことができます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルタです。

{{% alert color="primary" %}}
日付フィルタは、行または列領域に日時セルのみまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルタは期待される結果を生成しません。このフィルタを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}

Aspose.Cells は、`PivotField.filterByDate(PivotFilterType, params DateTime[] values)` メソッドを通じて日付フィルタリングを公開しています。`PivotFilterType` 列挙型には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用日付値が含まれます。選択したフィルタタイプに応じて、1つまたは2つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを含むピボットテーブルを含むワークブックを読み込み、特定の日付範囲に表示されるアイテムを制限する日付フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```javascript
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}
// ピボットテーブルを含む既存のワークブックを読み込む
var workbook = new AsposeCells.Workbook(inputPath);
// ピボットテーブルを含むワークシートにインデックスでアクセスする
var worksheet = workbook.getWorksheets().get(0);
// インデックスでピボットテーブルにアクセスする
var pivotTable = worksheet.getPivotTables().get(0);
// 行エリアから日付のPivotFieldを取得する
// (日付フィルターは、行/列エリアに日時セルまたは空白のみが含まれている場合にのみ機能します)
let dateField = pivotTable.getRowFields().get(0);
// Betweenフィルターの日付基準を定義する
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);
// ピボットフィールドに日付フィルターを適用する
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
// フィルターが反映されるようにピボットテーブルを更新して再計算する
pivotTable.getPivotCache().refresh();
// ワークブックを保存する
workbook.save(outputPath);
```

## **Value Filter**
値フィルタは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。一般的な使用例には、売上合計が目標額を超える製品のみを表示する、またはトランザクション数が範囲内にある地域のみを表示するなどがあります。
Aspose.Cells は、`PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` メソッドを通じて値フィルタリングを公開しています。`filterType` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`valueField` パラメータは評価するデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```javascript
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);
var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);
// PivotFieldCollection には IndexOf がないため、データフィールドのインデックスを手動で検索する
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.Pivot.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **Top 10 Filter**
トップ10フィルタは、選択した値フィールドに基づいて最高または最低の N 個のアイテムのみを保持する、値フィルタの特殊な形式です。これは、「売上によるトップ10製品」や「sales カウントによるボトム5地域」などのランキングレポートによく使用されます。

{{% alert color="primary" %}}
トップ10フィルタは、ピボットテーブルのデータ領域に1つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも1つの値フィールドがないと、アイテムのランク付けに使用する集計尺度がなく、フィルタを適用できません。
{{% /alert %}}

Aspose.Cells は、`PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` メソッドを通じてトップ10フィルタリングを公開しています。`itemCount` パラメータは保持するアイテムの数を定義し、`isTop` は上位アイテムを保持する（true）か下位アイテムを保持する（false）かを示し、`valueField` はランク付けに使用されるデータフィールドを参照し、`filterType` は値の計算方法を制御します（通常は `Sum` ですが、`Count` や `Percent` も使用できます）。
次の例では、値フィールドを含むピボットテーブルを含むワークブックを読み込み、売上の合計による上位10アイテムのみを保持するトップ10フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```javascript
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);
// ピボットテーブルを含むワークシートにアクセスします（インデックス0）
let worksheet = workbook.getWorksheets().get(0);
// インデックスでピボットテーブルにアクセスします
let pivotTable = worksheet.getPivotTables().get(0);
// データエリアに少なくとも1つの値のPivotFieldがあることを確認します
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);
// 対象の行PivotFieldを取得します（Top 10を適用するフィールド）
let rowField = pivotTable.getRowFields().get(0);
// 最初（かつ唯一の）データフィールドはインデックス0にあります。Top 10はこれでランク付けします。
let valueFieldIndex = 0;
// 行フィールドにTop 10フィルターを適用します：
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true（上位N件；falseの場合は下位N件）
//   - valueFieldIndex = アイテムのランク付けに使用されるデータフィールドのインデックス
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);
// ピボットテーブルのデータを更新し、フィルターが有効になるように再計算します
pivotTable.getPivotCache().refresh();
// ワークブックを保存します
workbook.save(outputPath);
```

## **Filter by Hiding or Unhiding Pivot Items**
構造化されたフィルタ API に加えて、Aspose.Cells では各ピボットアイテムの表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルタを適用せずに特定のアイテムを選択的に非表示にできます。`IsHidden = true` を設定するとアイテムがピボットテーブルから非表示になり、`IsHidden = false` を設定すると再表示されて再び表示されるようになります。
このアプローチは、フィルタリングルールが不規則またはアイテム固有の場合、特定のレポートに表示すべきでない少数の名前付きカテゴリを非表示にする場合などに便利です。以下の例では、ピボットテーブルを読み込み、特定のアイテムを名前で非表示にし、再表示する方法を示し、ピボットテーブルを更新してワークブックを保存します。

```javascript
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// ピボットテーブルを含む最初のワークシートにアクセスする
let sheet = workbook.getWorksheets().get(0);
// インデックスでピボットテーブルにアクセスする（シート上の最初のピボットテーブル）
let pivotTable = sheet.getPivotTables().get(0);
// 対象のPivotFieldを取得する（アイテムを表示/非表示にする最初の行ラベルフィールド）
let pivotField = pivotTable.getRowFields().get(0);
// 選択したPivotFieldのPivotItemsコレクションを反復する
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);
    // 特定の名前/条件に一致するピボットアイテムを非表示にする
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setIsHidden(true);
    }
    // 表示の復元を実証する：以前非表示にしたピボットアイテムを再表示する
    if (item.getName() == "Item3") {
        item.setIsHidden(false);
    }
}
// 変更が反映されるようにピボットテーブルを更新して再計算する
pivotTable.getPivotCache().refreshData();
// ワークブックを保存する — 非表示アイテムは基になるデータには残るが
// 表示されるピボットテーブルの出力からは除外される
workbook.save("output_pivot_filtered.xlsx");
```

## **Summary**
Aspose.Cells for Node.js via Java は、Microsoft Excel で利用可能な機能と一致する、ピボットテーブルの完全なフィルタリング機能を提供します。ラベルフィルタ、日付フィルタ、および値フィルタは最も一般的な分析シナリオをカバーし、トップ10フィルタはランキングレポートを処理します。フィルタリングルールが不規則な場合、`PivotItem.IsHidden` プロパティは柔軟なアイテムレベルのフォールバックを提供します。これらの戦略を組み合わせることで（たとえば、ラベルフィルタを適用してから特定のアイテムを非表示にする）、ピボットテーブルのレポートをコードから完全に正確にターゲットにして作成できます。

## Related Articles
- [Add Pivot Table Row and Column Fields in Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/manage-value-fields/)
- [Refresh Pivot Tables and Pivot Caches in Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}