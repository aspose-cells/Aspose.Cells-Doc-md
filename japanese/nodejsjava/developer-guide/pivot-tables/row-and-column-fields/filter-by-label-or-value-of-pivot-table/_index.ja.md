---
title: ピボットテーブルのラベルまたは値でフィルター処理
linktitle: ピボットテーブルのラベルまたは値でフィルター処理
description: Aspose.Cells for Node.js via Javaは包括的なピボットテーブルのフィルター機能をサポートしています。この記事では、ラベルフィルター、日付フィルター、値フィルター、上位10フィルターを使用したピボットテーブルデータのフィルタリング方法、およびピボットアイテムの非表示または再表示について説明します。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, 上位10フィルター, ピボットアイテム, ピボットアイテムの非表示
type: docs
weight: 10
url: /ja/nodejs-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cellsは、ピボットテーブルに表示されるデータをフィルタリングするための5つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルターを適用したり、フィールドに日付時刻セルまたは空白のみが含まれている場合に日付フィルターを使用したり、集約された数値に対して値フィルターを適用したり、値フィールドでランク付けする上位10フィルターを使用したり、`IsHidden`プロパティを使用して個々のピボットアイテムを手動で非表示または再表示したりできます。各戦略は、`PivotField`クラスと`PivotItem`クラスの専用APIを介して公開されています。
{{% /alert %}}
## **はじめに**
ピボットテーブルは強力な分析ツールですが、生の概要には特定のレポートに必要な情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、特定のレポートにとって重要な行、列、または値にピボットテーブルを絞り込むための主要なメカニズムです。Aspose.Cells for Node.js via Javaは、Microsoft Excelで利用可能なフィルタリング機能を反映し、それらをプログラム的に公開して、レポート生成を完全に自動化できるようにします。
この記事で説明するフィルタリング戦略は以下のとおりです。
1. **ラベルフィルター** — テキストラベルに基づいて行または列フィールドのアイテムをフィルタリングします。
2. **日付フィルター** — 日付時刻値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルター** — データフィールドの集約値に基づいてアイテムをフィルタリングします。
4. **上位10フィルター** — 値フィールドでランク付けされた上位または下位N個のアイテムのみを表示します。
5. **ピボットアイテムの非表示/再表示** — フィールド内の各アイテムの表示を手動で制御します。
各アプローチは、`PivotField`クラスの異なるメソッド、または`PivotItem`クラスのプロパティを使用します。任意のフィルターを適用した後、キャッシュデータと計算値が新しいフィルター状態を反映するように、ピボットテーブルで`refreshData()`と`calculateData()`を呼び出す必要があります。
## **ラベルフィルター**
ラベルフィルターを使用すると、テキストキャプションをパターンと比較することにより、行または列フィールドのアイテムをフィルタリングできます。これは、特定の文字で始まる名前、特定の単語を含む名前、またはその他のキャプション基準に一致する製品のみを表示する場合に役立ちます。
Aspose.Cellsは、`PivotField.filterByLabel(PivotFilterType, string)`メソッドを通じてラベルフィルタリングを公開します。`PivotFilterType`列挙には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank`などの値が含まれます。2番目の引数は比較に使用されるラベル文字列を提供します。
次の例は、ピボットテーブルを含む既存のワークブックを読み込み、指定された接頭辞で始まるキャプションを持つアイテムのみが表示されるようにラベルフィルターを適用し、ピボットテーブルを更新し、結果を保存します。
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

// ラベルフィルターを適用する — ラベルが指定されたプレフィックスで始まる行項目のみを表示する
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// ピボットテーブルのデータを更新して再計算し、フィルターを反映する
pivotTable.getPivotCache().refresh();

// ワークブックをディスクに保存する
workbook.save(fileName);
```
## **日付フィルター**
日付フィルターを使用すると、今日、先週、今月、次の四半期、特定の期間などの日付基準によってピボットテーブルを絞り込むことができます。これらは、日付時刻情報を格納するフィールドに対してのみ機能する特殊なフィルターです。
{{% alert color="primary" %}}
日付フィルターは、行または列領域に日付時刻セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルターは期待される結果を生成しません。このフィルターを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な`DateTime`インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}
Aspose.Cellsは、`PivotField.filterByDate(PivotFilterType, params DateTime[] values)`メソッドを通じて日付フィルタリングを公開します。`PivotFilterType`列挙には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between`などの専用日付値が含まれます。選択したフィルタータイプに応じて、1つまたは2つの`DateTime`値を渡します（`Between`の場合は開始日と終了日を渡します）。
次の例は、行領域に日付フィールドを含むピボットテーブルを持つワークブックを読み込み、特定の期間に表示されるアイテムを制限する日付フィルターを適用し、ピボットテーブルを更新し、ワークブックを保存します。
```javascript
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}

// ピボットテーブルを含む既存のワークブックを読み込む
var workbook = new AsposeCells.Workbook(inputPath);

// ピボットテーブルを含むワークシートにアクセスする（インデックスで）
var worksheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスする
var pivotTable = worksheet.getPivotTables().get(0);

// 行エリアから日付のPivotFieldを取得する
// （日付フィルターは、行/列エリアに日時セルまたは空白のみが含まれている場合にのみ機能します）
let dateField = pivotTable.getRowFields().get(0);

// Betweenフィルターの日付条件を定義する
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);

// ピボットフィールドに日付フィルターを適用する
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// フィルターを反映させるためにピボットテーブルを更新して再計算する
pivotTable.getPivotCache().refresh();

// ワークブックを保存する
workbook.save(outputPath);
```
## **値フィルター**
値フィルターは、ピボットテーブルがデータ領域で計算する集約値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的な使用例には、売上合計が目標額を超える製品のみを表示したり、取引回数が範囲内にある地域のみを表示したりすることが含まれます。
Aspose.Cellsは、`PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)`メソッドを通じて値フィルタリングを公開します。`filterType`パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual`などの値を使用します。`valueField`パラメータは評価するデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例は、ピボットテーブルを持つワークブックを読み込み、集約された売上が数値しきい値を超えるアイテムのみを保持する値フィルターを適用し、ピボットテーブルを更新し、ワークブックを保存します。
```javascript
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);

var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);

// PivotFieldCollectionにはIndexOfがないため、データフィールドのインデックスを手動で検索する
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
## **上位10フィルター**
上位10フィルターは、選択した値フィールドに基づいて最高または最低のN個のアイテムのみを保持する値フィルターの特殊な形式です。「収益別トップ10製品」や「販売数別ボトム5地域」などのランキングレポートで一般的に使用されます。
{{% alert color="primary" %}}
上位10フィルターは、ピボットテーブルのデータ領域に1つ以上の値ピボットフィールドがある場合にのみ有効です。値フィールドがないと、アイテムをランク付けするための集約された指標が存在せず、フィルターを適用できません。
{{% /alert %}}
Aspose.Cellsは、`PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`メソッドを通じて上位10フィルタリングを公開します。`itemCount`パラメータは保持するアイテムの数を定義し、`isTop`は上位のアイテムを保持する（true）か下位のアイテムを保持する（false）かを示し、`valueField`はランク付けに使用されるデータフィールドを参照し、`filterType`は値の計算方法を制御します（通常は`Sum`ですが、`Count`と`Percent`も使用できます）。
次の例は、値フィールドを含むピボットテーブルを持つワークブックを読み込み、売上合計で上位10個のアイテムのみを保持する上位10フィルターを適用し、ピボットテーブルを更新し、ワークブックを保存します。
```javascript
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);

// ピボットテーブルを含むワークシートにアクセスします（インデックス0）
let worksheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスします
let pivotTable = worksheet.getPivotTables().get(0);

// データエリアに少なくとも1つの値PivotFieldがあることを確認します
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);

// 対象の行PivotFieldを取得します（Top 10を適用するフィールド）
let rowField = pivotTable.getRowFields().get(0);

// 最初（かつ唯一の）データフィールドはインデックス0にあります。Top 10はこれによってランク付けされます。
let valueFieldIndex = 0;

// 行フィールドにTop 10フィルターを適用します：
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (上位N件。falseは下位N件を意味します)
//   - valueFieldIndex = アイテムのランク付けに使用されるデータフィールドのインデックス
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// ピボットテーブルのデータを更新し、フィルターが有効になるように再計算します
pivotTable.getPivotCache().refresh();

// ワークブックを保存します
workbook.save(outputPath);
```
## **ピボットアイテムを非表示または再表示してフィルタリングする**
構造化されたフィルターAPIに加えて、Aspose.Cellsでは各ピボットアイテムの表示を直接制御できます。`PivotField`の`PivotItems`コレクションを反復処理し、`IsHidden`プロパティを切り替えることにより、数式ベースのフィルターを適用せずに特定のアイテムを選択的に除外できます。`IsHidden = true`を設定するとアイテムがピボットテーブルから非表示になり、`IsHidden = false`を設定するとアイテムが再表示されて再び見えるようになります。
このアプローチは、特定のレポートに表示すべきではない少数の名前付きカテゴリを非表示にするなど、フィルタリングルールが不規則またはアイテム固有の場合に役立ちます。以下の例は、ピボットテーブルを読み込み、名前で特定のアイテムを非表示にし、再表示する方法を示し、ピボットテーブルを更新し、ワークブックを保存します。
```javascript
.xlsx");

// ピボットテーブルを含む最初のワークシートにアクセスする
let sheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスする（シート上の最初のピボットテーブル）
let pivotTable = sheet.getPivotTables().get(0);

// 対象のPivotFieldを取得する（項目の表示/非表示を切り替える最初の行ラベルフィールド）
let pivotField = pivotTable.getRowFields().get(0);

// 選択したPivotFieldのPivotItemsコレクションを反復処理する
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);

    // 特定の名前/条件に一致するピボット項目を非表示にする
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setIsHidden(true);
    }

    // 非表示解除のデモ：以前に非表示にしたピボット項目を再表示する
    if (item.getName() == "Item3") {
        item.setIsHidden(false);
    }
}

// 変更を反映させるためにピボットテーブルを更新および再計算する
pivotTable.getPivotCache().refreshData();

// ワークブックを保存する — 非表示の項目は元データのまま保持されるが、
// 表示されるピボットテーブルの出力からは除外される
workbook.save("output_pivot_filtered.xlsx");
```
## **まとめ**
Aspose.Cells for Node.js via Javaは、Microsoft Excelにある機能と一致するピボットテーブルのフィルタリング機能の完全なセットを提供します。ラベル、日付、および値フィルターは最も一般的な分析シナリオをカバーし、上位10フィルターはランキングレポートを処理します。フィルタリングルールが不規則な場合、`PivotItem.IsHidden`プロパティは柔軟なアイテムレベルの代替手段を提供します。たとえば、ラベルフィルターを適用してから特定のアイテムを非表示にするなど、これらの戦略を組み合わせることで、完全にコードから正確にターゲットを絞ったピボットテーブルレポートを構築できます。
## 関連記事
- [Aspose.Cells for Node.js via Javaでピボットテーブルの行と列フィールドを追加する](/cells/ja/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Node.js via Javaでピボットテーブルにフィルターフィールドを追加する](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Javaでピボットテーブルの値フィールドを管理する](/cells/ja/nodejs-java/manage-value-fields/)
- [Aspose.Cells for Node.js via Javaでピボットテーブルとピボットキャッシュを更新する](/cells/ja/nodejs-java/refresh-pivot-table/)
{{< app/cells/assistant language="nodejs-java" >}}