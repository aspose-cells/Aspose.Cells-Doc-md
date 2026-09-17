---
title: ピボットテーブルのラベルまたは値によるフィルタリング
linktitle: ピボットテーブルのラベルまたは値によるフィルタリング
description: Aspose.Cells for Python via .NET は、ピボットテーブルの包括的なフィルタリング機能をサポートしています。この記事では、ラベルフィルタ、日付フィルタ、値フィルタ、トップ 10 フィルタ、およびピボット項目の非表示または再表示によるピボットテーブルデータのフィルタリング方法について説明します。
keywords: Aspose.Cells, Python via .NET ライブラリ, スプレッドシート, ピボットテーブル, フィルタ, ラベルフィルタ, 値フィルタ, 日付フィルタ, トップ 10 フィルタ, ピボット項目, ピボット項目の非表示
type: docs
weight: 10
url: /ja/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルタリングするための 5 つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルタを適用したり、フィールドに日付時刻セルまたは空白のみが含まれる場合に日付フィルタを使用したり、集計された数値に対して値フィルタを適用したり、値フィールドでランク付けするためのトップ 10 フィルタを使用したり、`is_hidden` プロパティを使用して個々のピボット項目を手動で非表示または再表示したりできます。各戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}

## **Introduction**
ピボットテーブルは強力な分析ツールですが、生の要約には、提示する必要がある情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、特定のレポートに必要な行、列、値のみにピボットテーブルを絞り込むための主要なメカニズムです。Aspose.Cells for Python via .NET は、Microsoft Excel で利用可能なフィルタリング機能を反映し、レポート生成を完全に自動化できるようにプログラム的に公開しています。
この記事で説明するフィルタリング戦略は以下のとおりです。
1. **ラベルフィルタ** — 行または列フィールドの項目をそのテキストラベルに基づいてフィルタリングします。
2. **日付フィルタ** — 日付時刻値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルタ** — データフィールドの集計値に基づいて項目をフィルタリングします。
4. **トップ 10 フィルタ** — 値フィールドでランク付けされた上位または下位 N 個の項目のみを表示します。
5. **ピボット項目の非表示 / 再表示** — フィールド内の各項目の表示を手動で制御します。
各アプローチは、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルタを適用した後、キャッシュされたデータと計算値が新しいフィルタ状態を反映するように、ピボットテーブルで `refresh_data()` と `calculate_data()` を呼び出す必要があります。

## **Label Filter**
ラベルフィルタを使用すると、行または列フィールドの項目を、そのテキストキャプションをパターンと比較することでフィルタリングできます。これは、特定の文字で始まる名前、特定の単語を含む名前、またはその他のキャプションベースの条件に一致する製品のみを表示したい場合に役立ちます。
Aspose.Cells は、`PivotField.filter_by_label(PivotFilterType, label_string)` メソッドを通じてラベルフィルタリングを公開しています。`PivotFilterType` 列挙には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数は、比較に使用されるラベル文字列を提供します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定されたプレフィックスで始まる項目のみが表示されるようにするラベルフィルタを適用し、ピボットテーブルを更新して結果を保存します。

```python
import aspose.cells as ac
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = ac.Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the first row PivotField
row_field = pivot_table.row_fields[0]
# Apply the label filter — show only row items whose labels begin with the supplied prefix
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivot_table.pivot_cache.refresh()
# Save the workbook back to disk
workbook.save(fileName)
```

## **Date Filter**
日付フィルタを使用すると、今日、先週、今月、次の四半期、特定の日付範囲などの日付ベースの条件によってピボットテーブルを絞り込むことができます。これらは、日付時刻情報を格納するフィールドに対してのみ機能する特殊なフィルタです。

{{% alert color="primary" %}}
日付フィルタは、行または列領域に日付時刻セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルタは期待どおりの結果を生成しません。このフィルタを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}

Aspose.Cells は、`PivotField.filter_by_date(PivotFilterType, *date_times)` メソッドを通じて日付フィルタリングを公開しています。`PivotFilterType` 列挙には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、および `Between` などの専用の日付値が含まれます。選択したフィルタタイプに応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを含むピボットテーブルを含むワークブックを読み込み、表示される項目を特定の日付範囲に制限する日付フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
from datetime import datetime
input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"
if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)
# Load the existing workbook that contains the pivot table
workbook = ac.Workbook(input_path)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivot_table = worksheet.pivot_tables[0]
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
date_field = pivot_table.row_fields[0]
# Define the date criterion for the Between filter
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
# Apply the date filter on the pivot field
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)
# Refresh and recalculate the pivot table so the filter takes effect
pivot_table.pivot_cache.refresh()
# Persist the workbook
workbook.save(output_path)
```

## **Value Filter**
値フィルタは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを一致させるのではなく、数値の合計をしきい値と比較します。典型的な使用例には、売上合計が目標額を超える製品のみを表示する、またはトランザクション数が範囲内にある地域のみを表示するといったものがあります。
Aspose.Cells は、`PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)` メソッドを通じて値フィルタリングを公開しています。`PivotFilterType` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`value_field` パラメータは、評価するデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超える項目のみを保持する値フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
import aspose.cells as ac
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]
row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break
if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))
pivot_table.pivot_cache.refresh()
workbook.save("output.xlsx")
```

## **Top 10 Filter**
トップ 10 フィルタは、選択した値フィールドに基づいて最高または最低の N 個の項目のみを保持する、値フィルタの特殊な形式です。これは、「収益によるトップ 10 製品」や「販売数によるボトム 5 地域」などのランキングレポートによく使用されます。

{{% alert color="primary" %}}
トップ 10 フィルタは、ピボットテーブルのデータ領域に 1 つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも 1 つの値フィールドがないと、項目をランク付けするための集計された指標が存在しないため、フィルタを適用できません。
{{% /alert %}}

Aspose.Cells は、`PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)` メソッドを通じてトップ 10 フィルタリングを公開しています。`item_count` パラメータは保持する項目の数を定義し、`is_top` は上位の項目を保持するかどうかを示し（True）、`value_field` はランク付けに使用されるデータフィールドを参照し、`PivotFilterType` は値の計算方法を制御します（通常は `Sum` ですが、`Count` や `Percent` もあります）。
次の例では、値フィールドを含むピボットテーブルを含むワークブックを読み込み、売上合計で上位 10 個の項目のみを保持するトップ 10 フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.worksheets[0]
# Access the pivot table by index
pivotTable = worksheet.pivot_tables[0]
# Confirm there is at least one value PivotField in the data area
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.row_fields[0]
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.pivot_cache.refresh()
# Save the workbook
workbook.save(outputPath)
```

## **Filter by Hiding or Unhiding Pivot Items**
構造化されたフィルタ API に加えて、Aspose.Cells では各ピボット項目の表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復処理し、`is_hidden` プロパティを切り替えることで、数式ベースのフィルタを適用せずに特定の項目を選択的に非表示にできます。`is_hidden = True` を設定すると、その項目がピボットテーブルから非表示になります。`is_hidden = False` を設定すると、再表示されて再び表示されるようになります。
このアプローチは、フィルタリングルールが不規則または項目固有の場合（特定のレポートに表示すべきでない少数の名前付きカテゴリを非表示にする場合など）に役立ちます。以下の例では、ピボットテーブルを読み込み、名前で特定の項目を非表示にし、再表示する方法を実演し、ピボットテーブルを更新してワークブックを保存します。

```python
import aspose.cells as ac
# Load an existing workbook containing a pivot table
workbook = ac.Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.worksheets[0]
# Access the pivot table by index (the first pivot table on the sheet)
pivot_table = sheet.pivot_tables[0]
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivot_field = pivot_table.row_fields[0]
# Iterate through the PivotItems collection of the selected PivotField
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]
    # Hide pivot items that match a specific name/criterion
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.name == "Item3":
        item.is_hidden = False
# Refresh and recalculate the pivot table so changes take effect
pivot_table.pivot_cache.refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
```

## **Summary**
Aspose.Cells for Python via .NET は、Microsoft Excel にあるものと同等の完全なピボットテーブルフィルタリング機能を提供します。ラベル、日付、および値フィルタは最も一般的な分析シナリオをカバーし、トップ 10 フィルタはランキングレポートを処理します。フィルタリングルールが不規則な場合は、`PivotItem.is_hidden` プロパティが柔軟な項目レベルの代替手段を提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルタを適用してから特定の項目を非表示にする）ことで、コードから完全に正確にターゲットを絞ったピボットテーブルレポートを構築できます。

## Related Articles
- [ピボットテーブルの挿入](/cells/ja/python-net/pivot-tables/)
- [Aspose.Cells for Python via .NET でピボットテーブルの行と列フィールドを追加](/cells/ja/python-net/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Python via .NET でピボットテーブルにページフィールドを追加](/cells/ja/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET でピボットテーブルの値フィールドを管理](/cells/ja/python-net/manage-value-fields/)
- [Aspose.Cells for Python via .NET でピボットテーブルとピボットキャッシュを更新](/cells/ja/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}