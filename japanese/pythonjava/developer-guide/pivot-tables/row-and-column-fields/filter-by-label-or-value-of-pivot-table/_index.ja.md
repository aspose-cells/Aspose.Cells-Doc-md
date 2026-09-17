---
title: ラベルまたは値でピボットテーブルをフィルタリング
linktitle: ラベルまたは値でピボットテーブルをフィルタリング
description: Aspose.Cells for Python via Java は包括的なピボットテーブルのフィルタリング機能をサポートします。この記事では、ラベルフィルタ、日付フィルタ、値フィルタ、トップ 10 フィルタ、およびピボットアイテムの非表示/再表示によってピボットテーブルのデータをフィルタリングする方法を説明します。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, ピボットテーブル, フィルタ, ラベルフィルタ, 値フィルタ, 日付フィルタ, トップ 10 フィルタ, ピボットアイテム, ピボットアイテムを非表示
type: docs
weight: 10
url: /ja/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルタリングするための 5 つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルタを適用したり、フィールドに日時セルまたは空白のみが含まれている場合に日付フィルタを使用したり、データフィールドの集計値に対して値フィルタを適用したり、値フィールドでランク付けするトップ 10 フィルタを使用したり、`is_hidden` プロパティを使用して個々のピボットアイテムを手動で非表示または再表示したりできます。各戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}

## **Introduction**
ピボットテーブルは強力な分析ツールですが、生の要約には提示に必要な情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、特定のレポートに関連する行、列、値だけにピボットテーブルを絞り込むための主要なメカニズムです。Aspose.Cells for Python via Java は、Microsoft Excel で利用可能なフィルタリング機能を反映し、レポート生成を完全に自動化できるようにプログラム的に公開しています。
この記事で扱うフィルタリング戦略は以下の通りです。
1. **ラベルフィルタ** — テキストラベルに基づいて行または列フィールドのアイテムをフィルタリングします。
2. **日付フィルタ** — 日時値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルタ** — データフィールドの集計値に基づいてアイテムをフィルタリングします。
4. **トップ 10 フィルタ** — 値フィールドでランク付けされた上位または下位 N 個のアイテムのみを表示します。
5. **ピボットアイテムの非表示/再表示** — フィールド内の各アイテムの表示を手動で制御します。
各アプローチでは、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルタを適用した後、ピボットテーブルに対して `refresh_data()` と `calculate_data()` を呼び出して、キャッシュされたデータと計算値が新しいフィルタ状態を反映するようにする必要があります。

## **Label Filter**
ラベルフィルタを使用すると、テキストキャプションをパターンと比較して、行または列フィールドのアイテムをフィルタリングできます。これは、特定の文字で始まる名前の製品、特定の単語を含む製品、またはその他のキャプション基準に一致する製品のみを表示する場合に便利です。
Aspose.Cells は、`PivotField.filter_by_label(PivotFilterType, str)` メソッドを通じてラベルフィルタリングを公開しています。`PivotFilterType` 列挙には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数は、比較に使用されるラベル文字列を提供します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、ラベルフィルタを適用して、指定された接頭辞で始まるキャプションを持つアイテムのみが表示されるようにし、ピボットテーブルを更新して結果を保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType
fileName = "sample.xlsx"
prefix = "B"
# Load the existing workbook containing a pivot table
workbook = Workbook(fileName)
# Access the worksheet by index (first worksheet)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the first row PivotField
rowField = pivotTable.getRowFields().get(0)
# Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")
# Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook back to disk
workbook.save(fileName)
jpype.shutdownJVM()
```

## **Date Filter**
日付フィルタを使用すると、今日、先週、今月、次の四半期、特定の期間などの日付ベースの条件でピボットテーブルを絞り込むことができます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルタです。

{{% alert color="primary" %}}
日付フィルタは、行または列領域に日時セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルタは期待される結果を生成しません。このフィルタを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}

Aspose.Cells は、`PivotField.filter_by_date(PivotFilterType, values)` メソッドを通じて日付フィルタリングを公開しています。`PivotFilterType` 列挙には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、および `Between` などの専用日付値が含まれます。選択したフィルタタイプに応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを含むピボットテーブルを持つワークブックを読み込み、特定の期間に表示されるアイテムを制限する日付フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType
inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"
if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")
# Load the existing workbook that contains the pivot table
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (by index)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Retrieve the date PivotField from the row area
# (Date filter only works when the row/column area contains only date-time cells or blanks)
dateField = pivotTable.getRowFields().get(0)
# Define the date criterion for the Between filter
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)
# Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)
# Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh()
# Persist the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Value Filter**
値フィルタは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的な使用例には、売上合計が目標額を超える製品のみを表示する、または取引件数が範囲内にある地域のみを表示するなどがあります。
Aspose.Cells は、`PivotField.filter_by_value(value_field, filter_type, values)` メソッドを通じて値フィルタリングを公開しています。`filter_type` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`value_field` パラメータは、評価するデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType
workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)
rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)
# Find the data field index manually since PivotFieldCollection doesn't have IndexOf
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break
if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))
pivotTable.getPivotCache().refresh()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Top 10 Filter**
トップ 10 フィルタは、選択した値フィールドに基づいて最高または最低の N 個のアイテムのみを保持する値フィルタの特殊な形式です。これは、「売上によるトップ 10 製品」や「販売件数によるボトム 5 地域」などのランキングレポートによく使用されます。

{{% alert color="primary" %}}
トップ 10 フィルタは、データ領域に 1 つ以上の値ピボットフィールドがあるピボットテーブルに対してのみ有効です。値フィールドが少なくとも 1 つないと、アイテムをランク付けするための集計尺度がなく、フィルタを適用できません。
{{% /alert %}}

Aspose.Cells は、`PivotField.filter_top10(item_count, is_top, value_field, filter_type)` メソッドを通じてトップ 10 フィルタリングを公開しています。`item_count` パラメータは保持するアイテムの数を定義し、`is_top` は上位のアイテムを保持する（true）か下位のアイテムを保持する（false）かを示し、`value_field` はランク付けに使用されるデータフィールドを参照し、`filter_type` は値の計算方法を制御します（通常は `Sum` ですが、`Count` や `Percent` も使用できます）。
次の例では、値フィールドを含むピボットテーブルを持つワークブックを読み込み、売上の合計による上位 10 個のアイテムのみを保持するトップ 10 フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType
# Load the existing workbook that contains the pivot table
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)
# Access the worksheet that holds the pivot table (index 0)
worksheet = workbook.getWorksheets().get(0)
# Access the pivot table by index
pivotTable = worksheet.getPivotTables().get(0)
# Confirm there is at least one value PivotField in the data area
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)
# Retrieve the target row PivotField (the field we want to apply Top 10 on)
rowField = pivotTable.getRowFields().get(0)
# The first (and only) data field is at index 0; Top 10 ranks by it.
valueFieldIndex = 0
# Apply the Top 10 filter on the row field:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (top N; false would mean bottom N)
#   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)
# Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh()
# Save the workbook
workbook.save(outputPath)
jpype.shutdownJVM()
```

## **Filter by Hiding or Unhiding Pivot Items**
構造化されたフィルタ API に加えて、Aspose.Cells では各ピボットアイテムの表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復処理し、`is_hidden` プロパティを切り替えることで、数式ベースのフィルタを適用せずに特定のアイテムを選択的に非表示にできます。`is_hidden = True` を設定すると、アイテムがピボットテーブルから非表示になります。`is_hidden = False` を設定すると、再表示されて再び表示されるようになります。
このアプローチは、特定のレポートに表示すべきではない少数の名前付きカテゴリを非表示にするなど、フィルタリングルールが不規則またはアイテム固有の場合に役立ちます。以下の例では、ピボットテーブルを読み込み、特定のアイテムを名前で非表示にし、再表示する方法を実証し、ピボットテーブルを更新してワークブックを保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem
# Load an existing workbook containing a pivot table
workbook = Workbook("pivot_table_sample.xlsx")
# Access the first worksheet which contains the pivot table
sheet = workbook.getWorksheets().get(0)
# Access the pivot table by index (the first pivot table on the sheet)
pivotTable = sheet.getPivotTables().get(0)
# Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
pivotField = pivotTable.getRowFields().get(0)
# Iterate through the PivotItems collection of the selected PivotField
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)
    # Hide pivot items that match a specific name/criterion
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)
    # Demonstrate unhiding: re-show a previously hidden pivot item
    if item.getName() == "Item3":
        item.setIsHidden(False)
# Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh()
# Save the workbook — hidden items stay in the underlying data
# but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx")
jpype.shutdownJVM()
```

## **Summary**
Aspose.Cells for Python via Java は、Microsoft Excel で見られるものに匹敵する完全なピボットテーブルのフィルタリング機能を提供します。ラベルフィルタ、日付フィルタ、値フィルタは最も一般的な分析シナリオをカバーし、トップ 10 フィルタはランキングレポートを処理します。フィルタリングルールが不規則な場合、`PivotItem.is_hidden` プロパティは柔軟なアイテムレベルのフォールバックを提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルタを適用してから特定のアイテムを非表示にする）ことで、コードのみから正確にターゲットを絞ったピボットテーブルレポートを構築できます。

## Related Articles
- [ピボットテーブルの挿入](/cells/ja/python-java/pivot-tables/)
- [Aspose.Cells for Python via Java でピボットテーブルに行と列フィールドを追加](/cells/ja/python-java/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Python via Java でピボットテーブルにページフィールドを追加](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java でピボットテーブルの値フィールドを管理](/cells/ja/python-java/manage-value-fields/)
- [Aspose.Cells for Python via Java でピボットテーブルとピボットキャッシュを更新](/cells/ja/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}