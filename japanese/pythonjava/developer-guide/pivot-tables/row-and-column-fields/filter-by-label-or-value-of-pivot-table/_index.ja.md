---
title: ラベルまたは値によるピボットテーブルのフィルタリング
linktitle: ラベルまたは値によるピボットテーブルのフィルタリング
description: Aspose.Cells for Python via Java は包括的なピボットテーブルのフィルタリング機能をサポートします。この記事では、ラベルフィルター、日付フィルター、値フィルター、トップ10フィルター、およびピボットアイテムの表示/非表示によるフィルタリング方法について説明します。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, トップ10フィルター, ピボットアイテム, ピボットアイテムの非表示
type: docs
weight: 10
url: /ja/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルタリングするための 5 つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルターを適用したり、フィールドに日付時刻セルまたは空白のみが含まれる場合に日付フィルターを使用したり、集計された数値に対して値フィルターを適用したり、値フィールドでランク付けするトップ 10 フィルターを使用したり、`is_hidden` プロパティを使用して個別のピボットアイテムを手動で非表示または再表示したりできます。各戦略は `PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}
## **はじめに**
ピボットテーブルは強力な分析ツールですが、生の概要には特定のレポートに必要な情報よりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、ピボットテーブルを特定のレポートにとって重要な行、列、値に絞り込む主要なメカニズムです。Aspose.Cells for Python via Java は Microsoft Excel で利用可能なフィルタリング機能を反映し、レポート生成を完全に自動化できるようにプログラム的に公開しています。
この記事で説明するフィルタリング戦略は次のとおりです。
1. **ラベルフィルター** — 行または列フィールドのアイテムをテキストラベルに基づいてフィルタリングします。
2. **日付フィルター** — 日付時刻値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルター** — データフィールドの集計値に基づいてアイテムをフィルタリングします。
4. **トップ 10 フィルター** — 値フィールドでランク付けされた上位または下位 N 件のアイテムのみを表示します。
5. **ピボットアイテムの非表示 / 再表示** — フィールド内の各個別アイテムの表示を手動で制御します。
各アプローチは `PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルターを適用した後、ピボットテーブルのキャッシュデータと計算値が新しいフィルター状態を反映するように、ピボットテーブルで `refresh_data()` と `calculate_data()` を呼び出す必要があります。
## **ラベルフィルター**
ラベルフィルターを使用すると、テキストキャプションをパターンと比較することで、行または列フィールドのアイテムをフィルタリングできます。これは、特定の文字で始まる名前、特定の単語を含む名前、またはその他のキャプションベースの基準に一致する製品のみを表示する場合に役立ちます。
Aspose.Cells は `PivotField.filter_by_label(PivotFilterType, str)` メソッドを通じてラベルフィルタリングを公開しています。`PivotFilterType` 列挙には `CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数は比較に使用されるラベル文字列を提供します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定された接頭辞で始まるアイテムのみが表示されるようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# ピボットテーブルを含む既存のワークブックを読み込む
workbook = Workbook(fileName)

# インデックスでワークシートにアクセスする（最初のワークシート）
worksheet = workbook.getWorksheets().get(0)

# インデックスでピボットテーブルにアクセスする
pivotTable = worksheet.getPivotTables().get(0)

# 最初の行 PivotField を取得する
rowField = pivotTable.getRowFields().get(0)

# ラベルフィルターを適用する — 指定されたプレフィックスで始まるラベルの行アイテムのみを表示する
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# フィルターを有効にするためにピボットテーブルのデータを更新して再計算する
pivotTable.getPivotCache().refresh()

# ワークブックをディスクに保存する
workbook.save(fileName)

jpype.shutdownJVM()
```
## **日付フィルター**
日付フィルターを使用すると、今日、先週、今月、次の四半期、特定の日付範囲などの日付ベースの基準でピボットテーブルを絞り込むことができます。これらは日付時刻情報を保存するフィールドに対してのみ機能する特殊なフィルターです。
{{% alert color="primary" %}}
日付フィルターは、行または列エリアに日付時刻セルまたは空白セルのみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルターは期待された結果を生成しません。このフィルターを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}
Aspose.Cells は `PivotField.filter_by_date(PivotFilterType, values)` メソッドを通じて日付フィルタリングを公開しています。`PivotFilterType` 列挙には `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用の日付値が含まれます。選択したフィルタータイプに応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行エリアに日付フィールドを含むピボットテーブルを含むワークブックを読み込み、表示されるアイテムを特定の日付範囲に制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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

# ピボットテーブルを含む既存のワークブックを読み込む
workbook = Workbook(inputPath)

# ピボットテーブルを含むワークシートにアクセスする(インデックスで)
worksheet = workbook.getWorksheets().get(0)

# ピボットテーブルにインデックスでアクセスする
pivotTable = worksheet.getPivotTables().get(0)

# 行エリアから日付PivotFieldを取得する
# (日付フィルターは、行/列エリアに日時セルまたは空白のみが含まれている場合にのみ機能します)
dateField = pivotTable.getRowFields().get(0)

# Betweenフィルターの日付条件を定義する
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# ピボットフィールドに日付フィルターを適用する
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# フィルターを有効にするためにピボットテーブルを更新して再計算する
pivotTable.getPivotCache().refresh()

# ワークブックを保存する
workbook.save(outputPath)

jpype.shutdownJVM()
```
## **値フィルター**
値フィルターは、ピボットテーブルがデータエリアで計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。一般的な使用例には、売上の合計が目標額を超える製品のみを表示したり、取引件数が範囲内にある地域のみを表示したりする場合があります。
Aspose.Cells は `PivotField.filter_by_value(value_field, filter_type, values)` メソッドを通じて値フィルタリングを公開しています。`filter_type` パラメータは `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`value_field` パラメータは評価するデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
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

# PivotFieldCollection に IndexOf がないので、データフィールドのインデックスを手動で見つける
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
## **トップ 10 フィルター**
トップ 10 フィルターは値フィルターの特殊な形式であり、選択された値フィールドに基づいて最高または最低の N 件のアイテムのみを保持します。これは「収益別トップ 10 製品」や「販売件数別ボトム 5 リージョン」などのランキングレポートで一般的に使用されます。
{{% alert color="primary" %}}
トップ 10 フィルターは、ピボットテーブルのデータエリアに 1 つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも 1 つの値フィールドがない場合、アイテムをランク付けするための集計指標が存在せず、フィルターを適用できません。
{{% /alert %}}
Aspose.Cells は `PivotField.filter_top10(item_count, is_top, value_field, filter_type)` メソッドを通じてトップ 10 フィルタリングを公開しています。`item_count` パラメータは保持するアイテム数を定義し、`is_top` は上位のアイテムを保持する（true）か下位のアイテムを保持する（false）かを示し、`value_field` はランク付けに使用されるデータフィールドを参照し、`filter_type` は値の計算方法を制御します（通常は `Sum` ですが、`Count` や `Percent` も使用できます）。
次の例では、値フィールドを含むピボットテーブルを含むワークブックを読み込み、売上の合計で上位 10 件のアイテムのみを保持するトップ 10 フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# ピボットテーブルを含む既存のワークブックを読み込みます
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# ピボットテーブルを保持するワークシート（インデックス0）にアクセスします
worksheet = workbook.getWorksheets().get(0)

# インデックスでピボットテーブルにアクセスします
pivotTable = worksheet.getPivotTables().get(0)

# データ領域に少なくとも1つの値PivotFieldがあることを確認します
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)

# 対象の行PivotField（Top 10を適用するフィールド）を取得します
rowField = pivotTable.getRowFields().get(0)

# 最初（かつ唯一の）データフィールドはインデックス0にあります。Top 10はこれでランク付けされます。
valueFieldIndex = 0

# 行フィールドにTop 10フィルターを適用します：
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true (上位N件; falseなら下位N件)
#   - valueFieldIndex = アイテムのランク付けに使用されるデータフィールドのインデックス
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# フィルターを有効にするために、ピボットテーブルのデータを更新して再計算します
pivotTable.getPivotCache().refresh()

# ワークブックを保存します
workbook.save(outputPath)

jpype.shutdownJVM()
```
## **ピボットアイテムの非表示または再表示によるフィルタリング**
構造化されたフィルター API に加えて、Aspose.Cells では各個別ピボットアイテムの表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復処理し、`is_hidden` プロパティを切り替えることで、数式ベースのフィルターを適用せずに特定のアイテムを選択的に抑制できます。`is_hidden = True` を設定するとアイテムがピボットテーブルから非表示になります。`is_hidden = False` を設定すると再表示され、再び表示されるようになります。
このアプローチは、フィルタリングルールが不規則またはアイテム固有の場合（特定のレポートに表示すべきではない少数の名前付きカテゴリを非表示にする場合など）に役立ちます。以下の例では、ピボットテーブルを読み込み、特定のアイテムを名前で非表示にし、再表示する方法を実証し、ピボットテーブルを更新してワークブックを保存します。
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# ピボットテーブルを含む既存のワークブックを読み込む
workbook = Workbook("pivot_table_sample.xlsx")

# ピボットテーブルを含む最初のワークシートにアクセスする
sheet = workbook.getWorksheets().get(0)

# インデックスでピボットテーブルにアクセスする(シート上の最初のピボットテーブル)
pivotTable = sheet.getPivotTables().get(0)

# 対象のPivotFieldを取得する(アイテムを非表示/再表示する最初の行ラベルフィールド)
pivotField = pivotTable.getRowFields().get(0)

# 選択したPivotFieldのPivotItemsコレクションを反復処理する
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # 特定の名前/条件に一致するピボットアイテムを非表示にする
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # 再表示の例:以前非表示にしたピボットアイテムを再度表示する
    if item.getName() == "Item3":
        item.setIsHidden(False)

# 変更を有効にするためにピボットテーブルを更新して再計算する
pivotTable.getPivotCache().refresh()

# ワークブックを保存する — 非表示アイテムは基になるデータに残る
# が、表示されるピボットテーブルの出力からは除外される
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```
## **まとめ**
Aspose.Cells for Python via Java は、Microsoft Excel にあるものに匹敵する完全なピボットテーブルフィルタリング機能を提供します。ラベル、日付、および値フィルターは最も一般的な分析シナリオをカバーし、トップ 10 フィルターはランキングレポートを処理します。フィルタリングルールが不規則な場合、`PivotItem.is_hidden` プロパティは柔軟性の高いアイテムレベルのフォールバックを提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルターを適用してから特定のアイテムを非表示にする）ことで、コードのみから正確に対象を絞ったピボットテーブルレポートを作成できます。
## 関連記事
- [ピボットテーブルの挿入](/cells/ja/python-java/pivot-tables/)
- [Aspose.Cells for Python via Java でピボットテーブルの行と列フィールドを追加](/cells/ja/python-java/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Python via Java でピボットテーブルにフィルターフィールドを追加](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java でピボットテーブルの値フィールドを管理](/cells/ja/python-java/manage-value-fields/)
- [Aspose.Cells for Python via Java でピボットテーブルとピボットキャッシュを更新](/cells/ja/python-java/refresh-pivot-table/)
{{< app/cells/assistant language="python" >}}