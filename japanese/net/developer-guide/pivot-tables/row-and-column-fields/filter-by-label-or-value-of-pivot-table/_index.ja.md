---
title: ラベルまたは値によるピボットテーブルのフィルタリング
linktitle: ラベルまたは値によるピボットテーブルのフィルタリング
description: Aspose.Cells for .NET は、包括的なピボットテーブルのフィルタリング機能を備えています。ラベルフィルター、日付フィルター、値フィルター、上位 10 フィルター、およびピボット項目の非表示または表示処理を使用して、ピボットテーブルのデータをフィルタリングする方法を説明します。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, 上位 10 フィルター, ピボット項目, ピボット項目の非表示
type: docs
weight: 10
url: /ja/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells には、ピボットテーブルに表示されるデータをフィルタリングするための実用的な戦略が 5 つあります。テキストベースの行フィールドまたは列フィールドにはラベルフィルターを、日時セルまたは空セルだけを含むフィールドには日付フィルターを、集計された数値には値フィルターを、値フィールドによる順位付けには上位 10 フィルターを、`IsHidden` プロパティで個々のピボット項目を手動で非表示または表示できます。各戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を通じて利用できます。
{{% /alert %}}

## **はじめに**
ピボットテーブルは強力な分析ツールですが、未整理の集計結果には、レポートで提示する必要のある情報より多くの情報が含まれることがよくあります。フィルタリングは、特定のレポートで必要な行、列、または値にピボットテーブルを絞り込む主な手段です。Aspose.Cells for .NET は、Microsoft Excel のフィルタリング機能をプログラムから利用できるようにします。これにより、レポート生成を完全に自動化できます。
この文書では、次のフィルタリング戦略について説明します。
1. **ラベルフィルター** — テキストラベルに基づいて行または列フィールドの項目をフィルタリングします。
2. **日付フィルター** — 日時値（または空セル）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルター** — データフィールドの集計値に基づいて項目をフィルタリングします。
4. **上位 10 フィルター** — 値フィールドによる順位付けで上位または下位 N 項目だけを表示します。
5. **ピボット項目の非表示/表示** — フィールド内の各項目の表示を個別に手動で制御します。
各方法では、`PivotField` クラスのいずれかのメソッド、または `PivotItem` クラスのプロパティを使用します。フィルターを適用した後は、キャッシュされたデータと計算済みの値が新しいフィルター状態を反映するよう、ピボットテーブルの `PivotCache.Refresh()` を呼び出す必要があります。

## **ラベルフィルター**
ラベルフィルターでは、行または列フィールドの項目を、そのテキストキャプションとパターンで比較してフィルタリングできます。特定の文字で始まる製品名、特定の語を含む製品名、またはキャプションに基づくその他の条件に一致する製品だけを表示したい場合に便利です。
Aspose.Cells は、`PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)` メソッドによってラベルフィルタリング機能を提供します。`filterType` 引数は比較モード（`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` など）を選択します。`label1` と `label2` 引数は比較対象のテキストを指定します。1 つの値との照合だけが必要な場合（例：前方一致または部分一致）、`label2` に `string.Empty` を渡します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定した接頭辞で始まる項目だけを表示するラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string fileName = "sample.xlsx";
string prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.Worksheets[0];
// Access the pivot table by index
PivotTable pivotTable = worksheet.PivotTables[0];
// Retrieve the first row PivotField
PivotField rowField = pivotTable.RowFields[0];
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook back to disk
workbook.Save(fileName);
```

## **日付フィルター**
日付フィルターでは、今日、先週、今月、来四半期、または特定の日付範囲などの日付基準に基づいてピボットテーブルを絞り込めます。日時情報を格納するフィールドでのみ機能する特殊なフィルターです。

{{% alert color="primary" %}}
日付フィルターは、行または列領域に日時セルまたは空値だけが含まれている場合にのみ機能します。元のフィールドに数値やテキストなど他のデータ型が含まれている場合、日付フィルターは期待どおりの結果になりません。このフィルターを適用する前に、フィールドが日付として書式設定され、すべての値が有効な `DateTime` インスタンスまたは空セルであることを確認してください。
Aspose.Cells は、`PivotField.FilterByDate(PivotFilterType, params DateTime[] values)` メソッドによって日付フィルタリング機能を提供します。`PivotFilterType` 列挙型には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用値が含まれています。選択したフィルターの種類に応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを持つピボットテーブルのあるワークブックを読み込み、表示可能な項目を特定の日付範囲に制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
{{% /alert %}}

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
// Load the existing workbook that contains the pivot table
var workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.Worksheets[0];
// Access the pivot table by index
var pivotTable = worksheet.PivotTables[0];
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.RowFields[0];
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.PivotCache.Refresh();
// Persist the workbook
workbook.Save(outputPath);
```

## **値フィルター**
値フィルターは、ピボットテーブルがデータ領域で計算する集計値に対して作用します。テキストラベルを照合する代わりに、数値の集計結果をしきい値と比較します。売上合計が目標金額を超える製品だけを表示したり、取引件数が特定の範囲にある地域だけを表示したりする場合の典型的な使用例です。
Aspose.Cells は、`PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` メソッドによって値フィルタリング機能を提供します。`valueFieldIndex` パラメーターは、評価対象のデータフィールドを指定します（`pivotTable.DataFields.IndexOf(dataField)` を使用するか、コレクションを反復処理して位置を探します）。`filterType` パラメーターには、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を指定します。`double` 型の 2 つの引数でしきい値を指定します。
次の例では、ピボットテーブルのあるワークブックを読み込み、集計された売上高が数値のしきい値を超える項目だけを残す値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。

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

## **上位 10 フィルター**
上位 10 フィルターは、値フィルターの一種であり、選択した値フィールドに基づいて、最高または下位 N 項目だけを残します。「売上上位 10 製品」や「販売件数下位 5 地域」などのランキングレポートに一般に使用されます。

{{% alert color="primary" %}}
上位 10 フィルターは、データ領域に 1 つ以上の値ピボットフィールドがある場合にのみ有効です。値フィールドが少なくとも 1 つなければ、項目を順位付けするための集計指標が存在しないため、このフィルターを適用できません。
Aspose.Cells は `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` メソッドを通じて Top 10 フィルターを提供します。`valueFieldIndex` パラメーターは項目のランク付けに使用されるデータ フィールドのインデックスであり、`filterType` は `itemCount` の単位を選択します（`Count` は固定数の項目を保持し、`Percent` は項目の割合を保持するため、`itemCount` がその割合の値になります）。`isTop` は上位の項目（true）か下位の項目（false）のどちらを保持するかを示し、`itemCount` は保持する項目数または割合を定義します。
次の例では、値フィールドを含むピボットテーブルのあるワークブックを読み込み、売上合計による上位 10 項目だけを維持する上位 10 フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
{{% /alert %}}

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
//   - valueFieldIndex = 0 — the data field used to rank items
//   - filterType  = PivotFilterType.Count (keep a fixed number of items;
//     PivotFilterType.Percent would interpret 10 as "top 10 percent")
//   - isTop       = true (top N; false would mean bottom N)
//   - itemCount   = 10
rowField.FilterTop10(valueFieldIndex, PivotFilterType.Count, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.PivotCache.Refresh();
// Save the workbook
workbook.Save(outputPath);
```

## **ピボット項目の非表示または表示によるフィルタリング**
構造化されたフィルター API に加えて、Aspose.Cells では、各ピボット項目の表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式に基づくフィルターを適用せずに、特定の項目を個別に非表示にできます。`IsHidden = true` を設定すると、その項目はピボットテーブルから非表示になります。`IsHidden = false` を設定すると、項目が再び表示されます。
この方法は、フィルター条件が規則的でない場合や項目ごとに異なる場合に適しています。たとえば、特定のレポートに表示すべきでない、名前が指定された少数のカテゴリを非表示にする場合です。次の例では、ピボットテーブルを含むワークブックを読み込み、名前を指定して特定の項目を非表示にし、その項目を再表示する方法を例示し、ピボットテーブルを更新してワークブックを保存します。

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
Aspose.Cells for .NET は、Microsoft Excel に備わっているものと同じ完全なピボットテーブルのフィルタリング機能を提供します。ラベルフィルター、日付フィルター、値フィルターは一般的な分析シナリオに対応し、上位 10 フィルターはランキングレポートに対応します。フィルター条件が規則的でない場合、`PivotItem.IsHidden` プロパティを項目単位の柔軟な代替手段として利用できます。ラベルフィルターを適用してから特定の項目を非表示にする場合のように、これらの戦略を組み合わせることで、コードのみで正確に絞り込んだピボットテーブルのレポートを作成できます。

## 関連記事
- [Aspose.Cells for .NET でピボットテーブルの行および列フィールドを追加](/cells/ja/net/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for .NET でピボットテーブルの値フィールドを管理](/cells/ja/net/manage-value-fields/)
- [Aspose.Cells for .NET でピボットテーブルと PivotCache を更新](/cells/ja/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}