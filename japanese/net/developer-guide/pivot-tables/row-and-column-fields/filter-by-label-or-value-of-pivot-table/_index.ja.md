---
title: ラベルまたは値によるピボットテーブルのフィルタリング
linktitle: ラベルまたは値によるピボットテーブルのフィルタリング
description: Aspose.Cells for .NETは包括的なピボットテーブルのフィルタリング機能をサポートしています。この記事では、ラベルフィルター、日付フィルター、値フィルター、トップ10フィルターを使用してピボットテーブルデータをフィルタリングする方法、およびピボットアイテムを非表示または再表示する方法について説明します。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, トップ10フィルター, ピボットアイテム, ピボットアイテムの非表示
type: docs
weight: 10
url: /ja/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cellsは、ピボットテーブルに表示されるデータをフィルタリングするための5つの実用的な戦略を提供します。テキストベースの行または列フィールドに対してラベルフィルターを適用したり、フィールドに日付時刻セルまたは空白のみが含まれている場合に日付フィルターを使用したり、集計された数値に対して値フィルターを適用したり、値フィールドによるランク付けにトップ10フィルターを使用したり、`IsHidden`プロパティを使用して個々のピボットアイテムを手動で非表示または再表示したりすることができます。各戦略は、`PivotField`クラスと`PivotItem`クラスの専用のAPIを通じて公開されています。
{{% /alert %}}
## **概要**
ピボットテーブルは強力な分析ツールですが、生の要約には、特定のレポートで必要とする情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、ピボットテーブルを特定のレポートにとって重要な行、列、値だけに絞り込むための主要なメカニズムです。Aspose.Cells for .NETは、Microsoft Excelで利用できるフィルタリング機能をミラーリングし、それらをプログラム的に公開することで、レポート生成を完全に自動化できるようにします。
この記事で説明するフィルタリング戦略は以下のとおりです。
1. **ラベルフィルター** — テキストラベルに基づいて行または列フィールドのアイテムをフィルタリングします。
2. **日付フィルター** — 日付時刻値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルター** — データフィールドの集計値に基づいてアイテムをフィルタリングします。
4. **トップ10フィルター** — 値フィールドによってランク付けされた上位または下位N件のアイテムのみを表示します。
5. **ピボットアイテムの非表示/再表示** — フィールド内の各アイテムの表示を手動で制御します。
各アプローチは、`PivotField`クラスの異なるメソッド、または`PivotItem`クラスのプロパティを使用します。フィルターを適用した後、ピボットテーブルのキャッシュデータと計算値が新しいフィルター状態を反映するように、`RefreshData()`と`CalculateData()`をピボットテーブルに対して呼び出す必要があります。
## **ラベルフィルター**
ラベルフィルターを使用すると、行または列フィールドのアイテムをテキストキャプションとパターン比較することでフィルタリングできます。これは、特定の文字で始まる名前、特定の単語を含む名前、またはその他のキャプション基準に一致する製品のみを表示したい場合に便利です。
Aspose.Cellsは、ラベルフィルターを`PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`メソッドを通じて公開しています。`PivotFilterType`列挙体には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank`などの値が含まれます。2番目の引数は、比較に使用されるラベル文字列を提供します。
次の例は、既存のピボットテーブルを含むワークブックを読み込み、指定された接頭辞で始まるキャプションを持つアイテムのみが表示されるようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string fileName = "sample.xlsx";
string prefix = "B";

// ピボットテーブルを含む既存のワークブックを読み込む
Workbook workbook = new Workbook(fileName);

// インデックスでワークシートにアクセスする（最初のワークシート）
Worksheet worksheet = workbook.Worksheets[0];

// インデックスでピボットテーブルにアクセスする
PivotTable pivotTable = worksheet.PivotTables[0];

// 最初の行の PivotField を取得する
PivotField rowField = pivotTable.RowFields[0];

// ラベルフィルターを適用する — ラベルが指定されたプレフィックスで始まる行項目のみを表示する
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);

// ピボットテーブルのデータを更新して再計算し、フィルターを反映する
pivotTable.PivotCache.Refresh();

// ワークブックをディスクに保存する
workbook.Save(fileName);
```
## **日付フィルター**
日付フィルターを使用すると、今日、先週、今月、次の四半期、特定の期間などの日付ベースの基準によってピボットテーブルを絞り込むことができます。これらは、日付時刻情報を格納するフィールドに対してのみ機能する特殊なフィルターです。
{{% alert color="primary" %}}
日付フィルターは、行または列エリアに日付時刻セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルターは期待される結果を生成しません。このフィルターを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な`DateTime`インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}
Aspose.Cellsは、日付フィルターを`PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`メソッドを通じて公開しています。`PivotFilterType`列挙体には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between`などの専用日付値が含まれます。選択したフィルターの種類に応じて、1つまたは2つの`DateTime`値を渡します（`Between`の場合は開始日と終了日を渡します）。
次の例は、行エリアに日付フィールドを含むピボットテーブルを持つワークブックを読み込み、可視アイテムを特定の日付範囲に制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";

if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}

// ピボットテーブルを含む既存のワークブックを読み込みます
var workbook = new Workbook(inputPath);

// ピボットテーブルを含むワークシートにアクセスします（インデックスで指定）
var worksheet = workbook.Worksheets[0];

// インデックスでピボットテーブルにアクセスします
var pivotTable = worksheet.PivotTables[0];

// 行エリアから日付の PivotField を取得します
// （日付フィルターは、行/列エリアに日付時刻セルまたは空白のみが含まれている場合にのみ機能します）
PivotField dateField = pivotTable.RowFields[0];

// Between フィルターの日付条件を指定します
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// ピボットフィールドに日付フィルターを適用します
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);

// フィルターが反映されるように、ピボットテーブルを更新して再計算します
pivotTable.PivotCache.Refresh();

// ワークブックを保存します
workbook.Save(outputPath);
```
## **値フィルター**
値フィルターは、ピボットテーブルがデータエリアで計算する集計値に対して動作します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的な使用例には、売上合計が目標額を超える製品のみを表示する、あるいは取引数が範囲内に収まる地域のみを表示するなどが含まれます。
Aspose.Cellsは、値フィルターを`PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`メソッドを通じて公開しています。`filterType`パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual`などの値を使用します。`valueField`パラメータは評価対象のデータフィールドを指定し、最後の引数はしきい値（複数可）を提供します。
次の例は、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];

var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];

// PivotFieldCollection には IndexOf がないため、データフィールドのインデックスを手動で見つける
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}

pivotTable.PivotCache.Refresh();

workbook.Save("output.xlsx");
```
## **トップ10フィルター**
トップ10フィルターは、選択した値フィールドに基づいて最高または最低のN件のアイテムのみを保持する値フィルターの特殊な形式です。「収益によるトップ10製品」や「販売数によるボトム5地域」などのランキングレポートによく使用されます。
{{% alert color="primary" %}}
トップ10フィルターは、ピボットテーブルのデータエリアに1つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも1つの値フィールドがないと、アイテムをランク付けするための集計された指標が存在しないため、フィルターを適用できません。
{{% /alert %}}
Aspose.Cellsは、トップ10フィルターを`PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)`メソッドを通じて公開しています。`itemCount`パラメータは保持するアイテムの数を定義し、`isTop`は上位のアイテムを保持する（true）か下位のアイテムを保持する（false）かを示し、`valueField`はランク付けに使用されるデータフィールドを参照し、`filterType`は値の計算方法を制御します（通常は`Sum`ですが、`Count`や`Percent`も使用できます）。
次の例は、値フィールドを含むピボットテーブルを持つワークブックを読み込み、売上合計による上位10件のアイテムのみを保持するトップ10フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// ピボットテーブルを含む既存のワークブックを読み込む
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// ピボットテーブルを保持するワークシートにアクセスする (インデックス 0)
Worksheet worksheet = workbook.Worksheets[0];

// インデックスでピボットテーブルにアクセスする
PivotTable pivotTable = worksheet.PivotTables[0];

// データ領域に少なくとも1つの値 PivotField があることを確認する
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];

// 対象の行 PivotField を取得する (Top 10 を適用するフィールド)
PivotField rowField = pivotTable.RowFields[0];

// 最初 (かつ唯一の) データフィールドはインデックス 0 にあります。Top 10 はこれに基づいてランク付けします。
int valueFieldIndex = 0;

// 行フィールドに Top 10 フィルターを適用する:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (上位 N 件; false の場合は下位 N 件)
//   - valueFieldIndex = 項目のランク付けに使用されるデータフィールドのインデックス
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);

// ピボットテーブルのデータを更新し、フィルターが適用されるように再計算する
pivotTable.PivotCache.Refresh();

// ワークブックを保存する
workbook.Save(outputPath);
```
## **ピボットアイテムの非表示/再表示によるフィルタリング**
構造化されたフィルターAPIに加えて、Aspose.Cellsでは各ピボットアイテムの表示を直接制御することができます。`PivotField`の`PivotItems`コレクションを反復処理し、`IsHidden`プロパティを切り替えることで、数式ベースのフィルターを適用せずに特定のアイテムを選択的に非表示にすることができます。`IsHidden = true`を設定するとアイテムがピボットテーブルから非表示になり、`IsHidden = false`を設定すると再表示されて再び見えるようになります。
このアプローチは、フィルタリングルールが不規則な場合、またはアイテム固有の場合（特定のレポートに表示すべきでない少数の名前付きカテゴリを非表示にするなど）に役立ちます。以下の例では、ピボットテーブルを読み込み、名前で特定のアイテムを非表示にし、再表示する方法を実演し、ピボットテーブルを更新してワークブックを保存します。
```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// ピボットテーブルを含む既存のワークブックを読み込む
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// ピボットテーブルを含む最初のワークシートにアクセスする
Worksheet sheet = workbook.Worksheets[0];

// インデックスでピボットテーブルにアクセスする (シート上の最初のピボットテーブル)
PivotTable pivotTable = sheet.PivotTables[0];

// 対象のPivotFieldを取得する (項目を非表示/再表示する最初の行ラベルフィールド)
PivotField pivotField = pivotTable.RowFields[0];

// 選択したPivotFieldのPivotItemsコレクションを反復処理する
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];

    // 特定の名前/条件に一致するピボット項目を非表示にする
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }

    // 再表示のデモ: 以前に非表示にしたピボット項目を再表示する
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}

// 変更を反映させるためにピボットテーブルを更新して再計算する
pivotTable.PivotCache.Refresh();

// ワークブックを保存する — 非表示の項目は基になるデータに残ります
// が、表示されるピボットテーブルの出力からは除外されます
workbook.Save("output_pivot_filtered.xlsx");
```
## **まとめ**
Aspose.Cells for .NETは、Microsoft Excelにあるものと同等の完全なピボットテーブルのフィルタリング機能を提供します。ラベル、日付、および値フィルターは最も一般的な分析シナリオをカバーし、トップ10フィルターはランキングレポートを処理します。フィルタリングルールが不規則な場合は、`PivotItem.IsHidden`プロパティが柔軟なアイテムレベルのフォールバックを提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルターを適用してから特定のアイテムを非表示にする）ことで、ピボットテーブルのレポートをコードから正確にターゲットして構築できます。
## 関連記事
- [ピボットテーブルの挿入](/cells/ja/net/create-pivot-table/)
- [Aspose.Cells for .NETでピボットテーブルの行と列フィールドを追加する](/cells/ja/net/pivot-table-add-row-column-fields/)
- [Aspose.Cells for .NETでピボットテーブルにフィルターフィールドを追加する](/cells/ja/net/add-filter-field-in-pivot-table/)
- [Aspose.Cells for .NETでピボットテーブルの値フィールドを管理する](/cells/ja/net/pivot-table-manage-value-fields/)
- [Aspose.Cells for .NETでピボットテーブルとピボットキャッシュを更新する](/cells/ja/net/refresh-pivot-table/)
{{< app/cells/assistant language="csharp" >}}