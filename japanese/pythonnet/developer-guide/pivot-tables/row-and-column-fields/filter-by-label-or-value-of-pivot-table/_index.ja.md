---
title: ラベルまたは値でピボットテーブルをフィルタリングする
linktitle: ラベルまたは値でピボットテーブルをフィルタリングする
description: Aspose.Cells for Python via .NETは包括的なピボットテーブルのフィルタリング機能をサポートしています。この記事では、ラベルフィルタ、日付フィルタ、値フィルタ、トップ10フィルタ、およびピボットアイテムの表示・非表示によってピボットテーブルデータをフィルタリングする方法について説明します。
keywords: Aspose.Cells, Python via .NET library, スプレッドシート, ピボットテーブル, フィルタ, ラベルフィルタ, 値フィルタ, 日付フィルタ, トップ10フィルタ, ピボットアイテム, ピボットアイテムの非表示
type: docs
weight: 10
url: /ja/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cellsは、ピボットテーブルに表示されるデータをフィルタリングするための5つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルタを適用し、フィールドに日時セルのみが含まれるか空白である場合には日付フィルタを使用し、集計された数値に対して値フィルタを適用し、値フィールドによるランキングでトップ10フィルタを使用するか、`is_hidden`プロパティを使用して個々のピボットアイテムを手動で表示・非表示にすることができます。各戦略は、`PivotField`クラスと`PivotItem`クラスの専用APIを通じて公開されています。

{{% /alert %}}

## **はじめに**

ピボットテーブルは強力な分析ツールですが、生の概要には提示する必要のある情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、特定のレポートにとって重要な行、列、または値にピボットテーブルを絞り込むための主要なメカニズムです。Aspose.Cells for Python via .NETは、Microsoft Excelで利用可能なフィルタリング機能を反映しており、レポート生成を完全に自動化できるようにプログラムで公開しています。

この記事で扱うフィルタリング戦略は次のとおりです。

1. **ラベルフィルタ** — テキストラベルに基づいて行または列フィールドのアイテムをフィルタリングします。
2. **日付フィルタ** — 日時値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルタ** — データフィールドの集計値に基づいてアイテムをフィルタリングします。
4. **トップ10フィルタ** — 値フィールドによるランキングで上位または下位N個のアイテムのみを表示します。
5. **ピボットアイテムの表示・非表示** — フィールド内の各アイテムの表示を手動で制御します。

各アプローチは、`PivotField`クラスの異なるメソッド、または`PivotItem`クラスのプロパティを使用します。フィルタを適用した後、ピボットテーブルで`refresh_data()`と`calculate_data()`を呼び出して、キャッシュされたデータと計算値が新しいフィルタ状態を反映するようにする必要があります。

## **ラベルフィルタ**

ラベルフィルタを使用すると、行または列フィールドのアイテムをテキストキャプションをパターンと比較することでフィルタリングできます。これは、特定の文字で始まる名前、特定の単語を含む名前、または他のキャプション基準に一致する製品のみを表示する場合に便利です。

Aspose.Cellsは、`PivotField.filter_by_label(PivotFilterType, label_string)`メソッドを通じてラベルフィルタリングを公開しています。`PivotFilterType`列挙には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank`などの値が含まれます。2番目の引数は、比較に使用されるラベル文字列を提供します。

次の例は、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定された接頭辞で始まるアイテムのみが表示されるようにラベルフィルタを適用し、ピボットテーブルを更新して結果を保存します。

```python
import aspose.cells as ac

fileName = "sample.xlsx"
prefix = "B"

# ピボットテーブルを含む既存のワークブックをロードします
workbook = ac.Workbook(fileName)

# インデックスでワークシートにアクセスします（最初のワークシート）
worksheet = workbook.worksheets[0]

# インデックスでピボットテーブルにアクセスします
pivot_table = worksheet.pivot_tables[0]

# 最初の行の PivotField を取得します
row_field = pivot_table.row_fields[0]

# ラベルフィルターを適用します — 指定された接頭辞で始まるラベルの行項目のみを表示します
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")

# フィルターを反映するためにピボットテーブルのデータを更新して再計算します
pivot_table.pivot_cache.refresh()

# ワークブックをディスクに保存します
workbook.save(fileName)
```

## **日付フィルタ**

日付フィルタを使用すると、今日、先週、今月、次の四半期、特定の日付範囲などの日付ベースの基準でピボットテーブルを絞り込むことができます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルタです。

{{% alert color="primary" %}}

日付フィルタは、行または列の領域に日時セルのみが含まれるか空白の場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルタは期待される結果を生成しません。このフィルタを適用する前に、フィールドが日付として書式設定され、すべての値が有効な`DateTime`インスタンスまたは空のセルであることを確認してください。

{{% /alert %}}

Aspose.Cellsは、`PivotField.filter_by_date(PivotFilterType, *date_times)`メソッドを通じて日付フィルタリングを公開しています。`PivotFilterType`列挙には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between`などの専用日付値が含まれます。選択したフィルタタイプに応じて、1つまたは2つの`DateTime`値を渡します（`Between`の場合は開始日と終了日を渡します）。

次の例は、行領域に日付フィールドを含むピボットテーブルを持つワークブックを読み込み、表示対象のアイテムを特定の日付範囲に制限する日付フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
from datetime import datetime

input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"

if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)

# ピボットテーブルを含む既存のワークブックを読み込む
workbook = ac.Workbook(input_path)

# ピボットテーブルを含むワークシートにアクセスする(インデックス指定)
worksheet = workbook.worksheets[0]

# インデックスでピボットテーブルにアクセスする
pivot_table = worksheet.pivot_tables[0]

# 行エリアから日付PivotFieldを取得する
# (日付フィルターは、行/列エリアに日時セルまたは空白のみが含まれている場合にのみ機能します)
date_field = pivot_table.row_fields[0]

# Betweenフィルターの日付条件を指定する
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# ピボットフィールドに日付フィルターを適用する
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# フィルターを有効にするためにピボットテーブルを更新して再計算する
pivot_table.pivot_cache.refresh()

# ワークブックを保存する
workbook.save(output_path)
```

## **値フィルタ**

値フィルタは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的な使用例には、売上合計が目標額を超える製品のみを表示する、またはトランザクション数が範囲内に入る地域のみを表示するなどがあります。

Aspose.Cellsは、`PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)`メソッドを通じて値フィルタリングを公開しています。`PivotFilterType`パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual`などの値を使用します。`value_field`パラメータは評価するデータフィールドを指定し、最後の引数はしきい値を提供します。

次の例は、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値しきい値を超えるアイテムのみを保持する値フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
import aspose.cells as ac

workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# PivotFieldCollection には IndexOf がないため、データフィールドのインデックスを手動で見つけます
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

## **トップ10フィルタ**

トップ10フィルタは、選択した値フィールドに基づいて最高または最低のN個のアイテムのみを保持する値フィルタの特殊な形式です。「収益によるトップ10製品」や「売上数によるワースト5地域」などのランキングレポートによく使用されます。

{{% alert color="primary" %}}

トップ10フィルタは、ピボットテーブルのデータ領域に1つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも1つの値フィールドがなければ、アイテムをランク付けするための集計指標がなく、フィルタを適用できません。

{{% /alert %}}

Aspose.Cellsは、`PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)`メソッドを通じてトップ10フィルタリングを公開しています。`item_count`パラメータは保持するアイテムの数を定義し、`is_top`は上位アイテムを保持するか（True）下位アイテムを保持するか（False）を示し、`value_field`はランキングに使用されるデータフィールドを参照し、`PivotFilterType`は値の計算方法を制御します（通常は`Sum`ですが、`Count`や`Percent`も使用できます）。

次の例は、値フィールドを含むピボットテーブルを持つワークブックを読み込み、売上合計による上位10アイテムのみを保持するトップ10フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

# ピボットテーブルを含む既存のワークブックを読み込みます
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)

# ピボットテーブルを含むワークシートにアクセスします（インデックス 0）
worksheet = workbook.worksheets[0]

# インデックスでピボットテーブルにアクセスします
pivotTable = worksheet.pivot_tables[0]

# データ領域に少なくとも 1 つの値 PivotField があることを確認します
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# 対象の行 PivotField（Top 10 を適用するフィールド）を取得します
rowField = pivotTable.row_fields[0]

# 最初（かつ唯一の）データフィールドはインデックス 0 にあります。Top 10 はこれでランク付けします。
valueFieldIndex = 0

# 行フィールドに Top 10 フィルターを適用します:
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (上位 N。false の場合は下位 N)
#   - valueFieldIndex = 項目のランク付けに使用されるデータフィールドのインデックス
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# ピボットテーブルのデータを更新し、フィルターを有効にするために再計算します
pivotTable.pivot_cache.refresh()

# ワークブックを保存します
workbook.save(outputPath)
```

## **ピボットアイテムの表示・非表示によるフィルタリング**

構造化フィルタAPIに加えて、Aspose.Cellsでは各ピボットアイテムの表示を直接制御できます。`PivotField`の`PivotItems`コレクションを反復処理し、`is_hidden`プロパティを切り替えることで、数式ベースのフィルタを適用せずに特定のアイテムを選択的に除外できます。`is_hidden = True`を設定するとアイテムがピボットテーブルから非表示になり、`is_hidden = False`を設定すると再表示されて再び表示されるようになります。

このアプローチは、フィルタリングルールが不規則またはアイテム固有である場合、たとえば特定のレポートに表示すべきではない少数の名前付きカテゴリを非表示にする場合に役立ちます。以下の例では、ピボットテーブルを読み込み、特定のアイテムを名前で非表示にし、再表示する方法を実演し、ピボットテーブルを更新してワークブックを保存します。

```python
import aspose.cells as ac

# ピボットテーブルを含む既存のワークブックを読み込む
workbook = ac.Workbook("pivot_table_sample.xlsx")

# ピボットテーブルを含む最初のワークシートにアクセスする
sheet = workbook.worksheets[0]

# インデックスでピボットテーブルにアクセスする（シート上の最初のピボットテーブル）
pivot_table = sheet.pivot_tables[0]

# 対象のPivotFieldを取得する（アイテムを非表示/再表示する最初の行ラベルフィールド）
pivot_field = pivot_table.row_fields[0]

# 選択したPivotFieldのPivotItemsコレクションを反復処理する
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # 特定の名前/条件に一致するピボットアイテムを非表示にする
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # 再表示の例: 以前に非表示にしたピボットアイテムを再度表示する
    if item.name == "Item3":
        item.is_hidden = False

# 変更を反映させるためにピボットテーブルを更新して再計算する
pivot_table.pivot_cache.refresh()

# ワークブックを保存する — 非表示のアイテムは基になるデータに残ります
# が、表示されるピボットテーブルの出力からは除外されます
workbook.save("output_pivot_filtered.xlsx")
```

## **まとめ**

Aspose.Cells for Python via .NETは、Microsoft Excelにあるものと同等の完全なピボットテーブルフィルタリング機能を提供します。ラベル、日付、および値フィルタは最も一般的な分析シナリオをカバーし、トップ10フィルタはランキングレポートを処理します。フィルタリングルールが不規則な場合は、`PivotItem.is_hidden`プロパティが柔軟なアイテムレベルのフォールバックを提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルタを適用してから特定のアイテムを非表示にする）ことで、コードからピボットテーブルレポートを正確に作成できます。

## 関連記事

- [ピボットテーブルの挿入](/cells/ja/python-net/pivot-tables/)
- [Aspose.Cells for Python via .NETでピボットテーブルの行と列フィールドを追加する](/cells/ja/python-net/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Python via .NETでピボットテーブルにページフィールドを追加する](/cells/ja/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NETでピボットテーブルの値フィールドを管理する](/cells/ja/python-net/manage-value-fields/)
- [Aspose.Cells for Python via .NETでピボットテーブルとピボットキャッシュを更新する](/cells/ja/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}