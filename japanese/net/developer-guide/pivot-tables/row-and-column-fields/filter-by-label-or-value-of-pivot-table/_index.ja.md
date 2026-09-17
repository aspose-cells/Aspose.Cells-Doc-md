---
title: ラベルまたは値でピボットテーブルをフィルターする

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];
var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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

description: Aspose.Cells for .NETは包括的なピボットテーブルのフィルター機能をサポートしています。この記事では、ラベルフィルター、日付フィルター、値フィルター、トップ10フィルター、およびピボット項目の非表示/表示によってピボットテーブルのデータをフィルターする方法を説明します。
linktitle: ラベルまたは値でフィルター
keywords: Aspose.Cells, .NET library, spreadsheet, pivot table, filter, label filter, value filter, date filter, top 10 filter, pivot item, hide pivot item
type: docs
weight: 10
url: /ja/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、ピボットテーブルに表示されるデータをフィルタリングするための5つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルターを適用したり、フィールドに日時セルまたは空白のみが含まれる場合に日付フィルターを使用したり、集約された数値に対して値フィルターを適用したり、値フィールドでランク付けするためにトップ10フィルターを使用したり、`IsHidden`プロパティを使用して個々のピボット項目を手動で非表示または再表示したりできます。各戦略は、`PivotField`クラスと`PivotItem`クラスの専用APIを通じて公開されています。
{{% /alert %}}

## **はじめに**
ピボットテーブルは強力な分析ツールですが、生の要約には、表示する必要のある情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、特定のレポートに必要な行、列、または値にピボットテーブルを絞り込むための主要なメカニズムです。Aspose.Cells for .NETは、Microsoft Excelで利用可能なフィルタリング機能を反映し、プログラムで公開することで、レポート生成を完全に自動化できます。
この記事で説明するフィルタリング戦略は次のとおりです:
1. **ラベルフィルター** — テキストラベルに基づいて行または列フィールドの項目をフィルタリングします。
2. **日付フィルター** — 日時値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルター** — データフィールドの集約値に基づいて項目をフィルタリングします。
4. **トップ10フィルター** — 値フィールドでランク付けされた上位または下位のN個の項目のみを表示します。
5. **ピボット項目の非表示 / 再表示** — フィールド内の各項目の表示を手動で制御します。
各アプローチは、`PivotField`クラスの異なるメソッドまたは`PivotItem`クラスのプロパティを使用します。フィルターを適用した後、キャッシュされたデータと計算値が新しいフィルター状態を反映するように、ピボットテーブルで`PivotCache.Refresh()`を呼び出す必要があります。

## **ラベルフィルター**
ラベルフィルターを使用すると、テキストキャプションをパターンと比較して、行または列フィールドの項目をフィルタリングできます。これは、特定の文字で始まる名前、特定の単語を含む名前、またはその他のキャプションベースの基準に一致する製品のみを表示する場合に役立ちます。
Aspose.Cellsは、`PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)`メソッドを通じてラベルフィルタリングを公開します。`filterType`引数は比較モードを選択します（`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank`など）。`label1`および`label2`引数は比較テキストを提供します。単一値の一致のみが必要な場合（例：先頭一致や含む）、`label2`に`string.Empty`を渡します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定されたプレフィックスで始まる項目のみが表示されるようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。

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
// フィルターを有効にするためにピボットテーブルのデータを更新して再計算する
pivotTable.PivotCache.Refresh();
// ワークブックをディスクに保存する
workbook.Save(fileName);
```

## **日付フィルター**
日付フィルターを使用すると、今日、先週、今月、次の四半期、特定の期間などの日付ベースの基準でピボットテーブルを絞り込むことができます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルターです。

{{% alert color="primary" %}}
日付フィルターは、行または列エリアに日時セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルターは期待される結果を生成しません。このフィルターを適用する前に、フィールドが日付としてフォーマットされ、すべての値が有効な`DateTime`インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}

Aspose.Cellsは、`PivotField.FilterByDate(PivotFilterType, params DateTime[] values)`メソッドを通じて日付フィルタリングを公開します。`PivotFilterType`列挙体には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between`などの専用の日付値が含まれます。選択したフィルタータイプに応じて、1つまたは2つの`DateTime`値を渡します（`Between`の場合、開始日と終了日を渡します）。
次の例では、行エリアに日付フィールドを含むピボットテーブルを含むワークブックを読み込み、特定の期間に表示される項目を制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。

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
// ピボットテーブルを含む既存のワークブックを読み込む
var workbook = new Workbook(inputPath);
// ピボットテーブルを含むワークシートにアクセスする (インデックス指定)
var worksheet = workbook.Worksheets[0];
// インデックスでピボットテーブルにアクセスする
var pivotTable = worksheet.PivotTables[0];
// 行領域から日付のPivotFieldを取得する
// (日付フィルターは、行/列領域に日時セルまたは空白のみが含まれている場合にのみ機能します)
PivotField dateField = pivotTable.RowFields[0];
// Betweenフィルターの基準日を定義する
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// ピボットフィールドに日付フィルターを適用する
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);
// フィルターを有効にするためにピボットテーブルを更新して再計算する
pivotTable.PivotCache.Refresh();
// ワークブックを保存する
workbook.Save(outputPath);
```

## **値フィルター**
値フィルターは、ピボットテーブルがデータ領域で計算する集約値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的な使用例には、売上合計が目標額を超える製品のみを表示したり、取引数が範囲内に入る地域のみを表示したりすることが含まれます。
Aspose.Cellsは、`PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`メソッドを通じて値フィルタリングを公開します。`valueFieldIndex`パラメータは、評価するデータフィールドを指定します（`pivotTable.DataFields.IndexOf(dataField)`を使用するか、コレクションを反復処理して位置を見つけます）。`filterType`パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual`などの値を使用します。2つの`double`引数はしきい値を提供します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集約された売上が数値のしきい値を超える項目のみを保持する値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。

## **トップ10フィルター**
トップ10フィルターは、選択した値フィールドに基づいて最高または最低のN個の項目のみを保持する、値フィルターの特殊な形式です。「収益別トップ10製品」や「販売数別ボトム5地域」などのランキングレポートによく使用されます。

{{% alert color="primary" %}}
トップ10フィルターは、ピボットテーブルのデータ領域に1つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも1つの値フィールドがなければ、項目をランク付けするための集約された尺度がなく、フィルターを適用できません。
{{% /alert %}}

Aspose.Cellsは、`PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)`メソッドを通じてトップ10フィルタリングを公開します。`itemCount`パラメータは保持する項目の数を定義し、`filterType`は値の計算方法を制御し（通常は`Sum`ですが、`Count`や`Percent`もあります）、`isTop`は上位の項目を保持する（true）か下位の項目を保持する（false）かを示し、`valueFieldIndex`は項目のランク付けに使用されるデータフィールドのインデックスです。
次の例では、値フィールドを含むピボットテーブルを含むワークブックを読み込み、売上合計で上位10項目のみを保持するトップ10フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load the existing workbook that contains the pivot table
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.Worksheets[0];
// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];
// Confirm there is at least one value PivotField in the data area
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.RowFields[0];
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.FilterTop10(10, PivotFilterType.Sum, true, valueFieldIndex);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook
workbook.Save(outputPath);
```

## **ピボット項目の非表示/再表示によるフィルタリング**
構造化されたフィルターAPIに加えて、Aspose.Cellsでは個々のピボット項目の表示/非表示を直接制御できます。`PivotField`の`PivotItems`コレクションを反復処理して`IsHidden`プロパティを切り替えることで、数式ベースのフィルターを適用せずに特定の項目を選択的に抑制できます。`IsHidden = true`を設定すると項目はピボットテーブルから非表示になり、`IsHidden = false`を設定すると再表示されます。
このアプローチは、特定のレポートに表示すべきでない少数の名前付きカテゴリを非表示にするなど、フィルタリングルールが不規則だったり項目固有だったりする場合に役立ちます。以下の例では、ピボットテーブルを読み込み、名前を指定して特定の項目を非表示にし、再表示する方法を示し、ピボットテーブルを更新してワークブックを保存します。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.Worksheets[0];
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.PivotTables[0];
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.RowFields[0];
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];
    // Hide pivot items that match a specific name/criterion
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.PivotCache.Refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.Save("output_pivot_filtered.xlsx");
```

## **まとめ**
Aspose.Cells for .NETは、Microsoft Excelにあるものと一致する完全なピボットテーブルのフィルタリング機能を提供します。ラベル、日付、および値フィルターは最も一般的な分析シナリオをカバーし、トップ10フィルターはランキングレポートを処理します。フィルタリングルールが不規則な場合、`PivotItem.IsHidden`プロパティは柔軟な項目レベルのフォールバックを提供します。たとえば、ラベルフィルターを適用してから特定の項目を非表示にするなど、これらの戦略を組み合わせることで、コードのみから正確にターゲットを絞ったピボットテーブルレポートを構築できます。

## 関連記事
- [Aspose.Cells for .NETでピボットテーブルの行と列フィールドを追加する](/cells/ja/net/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for .NETでピボットテーブルの値フィールドを管理する](/cells/ja/net/manage-value-fields/)
- [Aspose.Cells for .NETでピボットテーブルとピボットキャッシュを更新する](/cells/ja/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}