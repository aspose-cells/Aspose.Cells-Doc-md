---
title: ラベルまたは値によるピボットテーブルのフィルタリング
linktitle: ラベルまたは値によるピボットテーブルのフィルタリング
description: Aspose.Cells for Node.js via C++ は包括的なピボットテーブルのフィルタリング機能をサポートしています。この記事では、ラベルフィルタ、日付フィルタ、値フィルタ、トップ10フィルタの使用、およびピボットアイテムの非表示/再表示によるピボットテーブルデータのフィルタリング方法について説明します。
keywords: Aspose.Cells, Node.js via C++ ライブラリ, スプレッドシート, ピボットテーブル, フィルタ, ラベルフィルタ, 値フィルタ, 日付フィルタ, トップ10フィルタ, ピボットアイテム, ピボットアイテムの非表示
type: docs
weight: 10
url: /ja/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルタリングするための5つの実用的な戦略を提供します。テキストベースの行フィールドまたは列フィールドにラベルフィルタを適用したり、日付と時刻のセルまたは空白のみを含むフィールドに対して日付フィルタを使用したり、集計数値に対して値フィルタを適用したり、値フィールドによってランク付けするトップ10フィルタを使用したり、`IsHidden` プロパティを使用して個別のピボットアイテムを手動で非表示または再表示したりできます。各戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}
## **はじめに**
ピボットテーブルは強力な分析ツールですが、生の集計結果には特定のレポートで提示する必要がある情報をはるかに超えるデータが含まれていることがよくあります。フィルタリングは、ピボットテーブルを特定のレポートにとって重要な行、列、値に絞り込むための主要なメカニズムです。Aspose.Cells for Node.js via C++ は Microsoft Excel で利用できるフィルタリング機能を反映しており、それらをプログラム的に公開することで、レポート生成を完全に自動化できるようにしています。
この記事で扱うフィルタリング戦略は以下の通りです。
1. **ラベルフィルタ** — 行または列フィールドのアイテムを、テキストラベルに基づいてフィルタリングします。
2. **日付フィルタ** — 日時の値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルタ** — データフィールドの集計値に基づいてアイテムをフィルタリングします。
4. **トップ10フィルタ** — 値フィールドでランク付けされた上位または下位N件のアイテムのみを表示します。
5. **ピボットアイテムの非表示/再表示** — フィールド内の各個別アイテムの表示を手動で制御します。
各アプローチは、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルタを適用した後、ピボットテーブルのキャッシュデータと計算値が新しいフィルタ状態を反映するように、ピボットテーブル上で `refreshData()` と `calculateData()` を呼び出す必要があります。
## **ラベルフィルタ**
ラベルフィルタを使用すると、行または列フィールドのアイテムを、テキストキャプションをパターンと比較することによってフィルタリングできます。これは、特定の文字で始まる名前の製品のみを表示したり、特定の単語を含む製品のみを表示したり、その他のキャプション基準に一致する製品のみを表示したりする場合に便利です。
Aspose.Cells は、`PivotField.filterByLabel(PivotFilterType, string)` メソッドを通じてラベルフィルタリングを公開しています。`PivotFilterType` 列挙には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2番目の引数は、比較に使用されるラベル文字列を指定します。
次の例では、既存ピボットテーブルを含むワークブックを読み込み、指定された接頭辞で始まるキャプションを持つアイテムのみが表示されるようにラベルフィルタを適用し、ピボットテーブルを更新して結果を保存します。
```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// ピボットテーブルを含む既存のブックを読み込む
let workbook = new AsposeCells.Workbook(fileName);

// インデックスでワークシートにアクセスする（最初のワークシート）
let worksheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスする
let pivotTable = worksheet.getPivotTables().get(0);

// 最初の行の PivotField を取得する
let rowField = pivotTable.getRowFields().get(0);

// ラベルフィルターを適用する — ラベルが指定された接頭辞で始まる行項目のみを表示する
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// ピボットテーブルのデータを更新して再計算し、フィルターを反映する
pivotTable.getPivotCache().refresh();

// ワークブックをディスクに保存する
workbook.save(fileName);
```
## **日付フィルタ**
日付フィルタを使用すると、今日、先週、今月、来四半期、特定の日付範囲などの日付ベースの基準によってピボットテーブルを絞り込むことができます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルタです。
{{% alert color="primary" %}}
日付フィルタは、行または列エリアに日時セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルタは期待どおりの結果を生成しません。このフィルタを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}
Aspose.Cells は、`PivotField.filterByDate(PivotFilterType, params DateTime[] values)` メソッドを通じて日付フィルタリングを公開しています。`PivotFilterType` 列挙には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用の日付値が含まれます。選択したフィルタタイプに応じて、1つまたは2つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行エリアに日付フィールドを含むピボットテーブルを持つワークブックを読み込み、特定の日付範囲に表示されるアイテムを制限する日付フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。
```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found: " + inputPath);
}

// ピボットテーブルを含む既存のワークブックを読み込む
const workbook = new AsposeCells.Workbook(inputPath);

// ピボットテーブルを含むワークシートにインデックスでアクセスする
const worksheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスする
const pivotTable = worksheet.getPivotTables().get(0);

// 行エリアから日付のピボットフィールドを取得する
// (日付フィルターは、行/列エリアに日時セルまたは空白のみが含まれている場合にのみ機能します)
const dateField = pivotTable.getRowFields().get(0);

// Between フィルターの日付基準を定義する
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// ピボットフィールドに日付フィルターを適用する
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// フィルターが反映されるようにピボットテーブルを更新して再計算する
pivotTable.getPivotCache().refresh();

// ワークブックを保存する
workbook.save(outputPath);
```
## **値フィルタ**
値フィルタは、ピボットテーブルがデータエリアで計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的な使用例としては、売上合計が目標額を超える製品のみを表示したり、取引件数が範囲内にある地域のみを表示したりする場合があります。
Aspose.Cells は、`PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` メソッドを通じて値フィルタリングを公開しています。`filterType` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`valueField` パラメータは評価対象のデータフィールドを指定し、最後の引数はしきい値（複数可）を指定します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。
```javascript
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
## **トップ10フィルタ**
トップ10フィルタは、選択した値フィールドに基づいて最高または最低のN件のアイテムのみを保持する値フィルタの特殊な形式です。「売上高によるトップ10製品」や「販売件数によるワースト5地域」などのランキングレポートで一般的に使用されます。
{{% alert color="primary" %}}
トップ10フィルタは、ピボットテーブルのデータエリアに1つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも1つの値フィールドがないと、アイテムをランク付けするための集計された指標が存在しないため、フィルタを適用できません。
{{% /alert %}}
Aspose.Cells は、`PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` メソッドを通じてトップ10フィルタリングを公開しています。`itemCount` パラメータは保持するアイテム数を定義し、`isTop` は上位アイテムを保持するかどうか（true）または下位アイテムを保持するかどうか（false）を示し、`valueField` はランク付けに使用されるデータフィールドを参照し、`filterType` は値の計算方法を制御します（通常は `Sum` ですが、`Count` や `Percent` も可能です）。
次の例では、値フィールドを含むピボットテーブルを持つワークブックを読み込み、売上合計による上位10件のアイテムのみを保持するトップ10フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。
```javascript
const AsposeCells = require("aspose.cells");

// ピボットテーブルを含む既存のワークブックを読み込む
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// ピボットテーブルを含むワークシートにアクセスする (インデックス0)
const worksheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスする
const pivotTable = worksheet.getPivotTables().get(0);

// データエリアに少なくとも1つの値PivotFieldがあることを確認する
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("Pivot table has no value (data) PivotField.");
}
const valueField = pivotTable.getDataFields().get(0);

// 対象の行PivotFieldを取得する (Top 10を適用するフィールド)
const rowField = pivotTable.getRowFields().get(0);

// 最初(かつ唯一の)データフィールドはインデックス0にある; Top 10はこれでランク付けする。
const valueFieldIndex = 0;

// 行フィールドにTop 10フィルタを適用する:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (上位N件; falseは下位N件)
//   - valueFieldIndex = アイテムをランク付けするために使用されるデータフィールドのインデックス
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// ピボットテーブルのデータを更新し、フィルタが反映されるように再計算する
pivotTable.getPivotTableCache().refresh();

// ワークブックを保存する
workbook.save(outputPath);
```
## **ピボットアイテムの非表示/再表示によるフィルタリング**
構造化されたフィルタ API に加えて、Aspose.Cells では各個別ピボットアイテムの表示を直接制御することもできます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルタを適用せずに特定のアイテムを選択的に非表示にできます。`IsHidden = true` を設定するとアイテムがピボットテーブルから非表示になり、`IsHidden = false` を設定すると再表示されて再び見えるようになります。
このアプローチは、フィルタリングルールが不規則またはアイテム固有の場合（特定のレポートに表示すべきではない少数の名前付きカテゴリを非表示にする場合など）に便利です。以下の例では、ピボットテーブルを読み込み、名前で特定のアイテムを非表示にし、再表示する方法を実演し、ピボットテーブルを更新してワークブックを保存します。
```javascript
const AsposeCells = require("aspose.cells");

// ピボットテーブルを含む既存のワークブックを読み込む
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// ピボットテーブルを含む最初のワークシートにアクセスする
const sheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスする（シート上の最初のピボットテーブル）
const pivotTable = sheet.getPivotTables().get(0);

// 対象の PivotField を取得する（項目を非表示/表示する最初の行ラベルフィールド）
const pivotField = pivotTable.getRowFields().get(0);

// 選択した PivotField の PivotItems コレクションを反復処理する
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // 特定の名前/条件に一致するピボット項目を非表示にする
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // 非表示解除のデモ：以前に非表示にしたピボット項目を再表示する
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// 変更が反映されるようにピボットテーブルを更新して再計算する
pivotTable.getPivotCache().refreshData();

// ワークブックを保存する — 非表示の項目は基になるデータには残るが、
// 表示されるピボットテーブルの出力からは除外される
workbook.save("output_pivot_filtered.xlsx");
```
## **まとめ**
Aspose.Cells for Node.js via C++ は、Microsoft Excel で利用できるものと一致する完全なピボットテーブルのフィルタリング機能を提供します。ラベル、日付、値フィルタは最も一般的な分析シナリオをカバーし、トップ10フィルタはランキングレポートを処理します。フィルタリングルールが不規則な場合は、`PivotItem.IsHidden` プロパティが柔軟性のあるアイテムレベルのフォールバックを提供します。これらの戦略を組み合わせること（たとえば、ラベルフィルタを適用してから特定のアイテムを非表示にする）により、ピボットテーブルのレポートを完全にコードから正確にターゲットして構築できます。
## 関連記事
- [ピボットテーブルの挿入](/cells/ja/nodejs-cpp/pivot-tables/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルの行と列のフィールドを追加する](/cells/ja/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルにページフィールドを追加する](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルの値フィールドを管理する](/cells/ja/nodejs-cpp/manage-value-fields/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルとピボットキャッシュを更新する](/cells/ja/nodejs-cpp/refresh-pivot-table/)
{{< app/cells/assistant language="nodejs-cpp" >}}