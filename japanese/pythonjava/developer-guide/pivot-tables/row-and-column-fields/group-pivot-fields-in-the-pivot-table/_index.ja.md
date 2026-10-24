---
title: ピボットテーブルでピボットフィールドをグループ化する
linktitle: ピボットテーブルでピボットフィールドをグループ化する
description: Aspose.Cells for Python via Java で PivotField.group および PivotFieldGroupOptions を使用して、ピボットテーブルの行と列のピボットフィールドを月や四半期などの日付期間や数値範囲にグループ化する方法を学習します。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.group, PivotFieldGroupOptions, 日付のグループ化, 数値のグループ化, 月, 四半期, 数値範囲, Python
type: docs
weight: 80
url: /ja/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
- ピボットフィールドのグループ化は、ピボットテーブルの行または列フィールドに多数の個別アイテム（数百の日付を含む日付フィールドや、多くの散在する値を持つ数値フィールドなど）が含まれている場合に役立ちます。グループ化により、これらのアイテムが意味のあるセクションにまとめられます。日付は月、四半期、年、数値は 0-1、2-3、4-5 などの範囲にまとめられます。これにより、大規模なピボットテーブルがコンパクトになり、分析が容易になります。Aspose.Cells はこの機能を `PivotField.group()` メソッド（データ型による自動グループ化）と `PivotField.group(PivotFieldGroupOptions)`（カスタム グループ化オプション）で提供します。
- 日付グループ化は、個々の日付を日、月、四半期、年などのより大きな期間に集約し、時間の階層を構築します（例：年、四半期、月）。経時的な傾向が一目でわかるようになり、各期間レベルはピボットテーブルの行または列領域の独自のピボットフィールドになります。
- グループ化は、ピボットテーブルの ROW または COLUMN 領域に配置されているフィールドに対してのみ可能です。データ（値）フィールドを直接グループ化することはできません。そのようなフィールドをグループ化するには、まずそのフィールドをピボットテーブルの行または列領域に追加する必要があります。

## **Group Pivot Fields Automatically**
パラメータなしの `PivotField.group()` オーバーロードは、フィールドのデータ型を検査し、自動的にグループ化します。日付のみ（および空白）を含むフィールドは月別にグループ化されます。数値のみ（および空白）を含むフィールドは、自動間隔を使用して数値範囲にグループ化されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# サンプルワークブックを読み込む
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 2番目のワークシートとそのピボットテーブルにアクセスする
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# 最初の行フィールドを自動的にグループ化する。
# フィールドには日付が含まれているため、月でグループ化されます。
field = pt.getRowFields().get(0)
field.group()
# ピボットテーブルのデータを計算し、出力ファイルを保存する
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Group Pivot Fields with Custom Options**
`PivotFieldGroupOptions` クラスは、カスタム グループ化設定を提供します。日付フィールドの場合、`StartDate`、`EndDate`、および `GroupTypes` を設定します。数値フィールドの場合、`StartNumber`、`EndNumber`、および `Interval` を設定します。`NewPivotField` プロパティは、グループ化が元のフィールドの隣に新しいピボットフィールドを作成するかどうかを制御します（この記事の最後の「Note」セクションを参照してください）。

### **Group a Date Field by Months and Quarters**
次の例は、サンプルピボットテーブルの日付の行フィールドを開始日と終了日の間で月と四半期にグループ化します。コードは [サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx) を読み込み、グループ化を実行し、ピボットテーブルのデータを計算して、グループ化された結果を保存します。スクリーンショットは効果を示しています。日付の行フィールドは四半期と月でグループ化されています。
`options.GroupTypes` の値の順序は無視されることに注意してください。グループタイプの順序に関係なく、グループ化されたフィールドは常に最大の期間から最小の順に表示されます。年、四半期、月、日、時間、分、秒の順です。この例では、`options.GroupTypes` で月が四半期より前にリストされていますが、四半期は外側のレベルとして、月は内側のレベルとして表示されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# サンプルワークブックを読み込む
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 2番目のワークシートとそのピボットテーブルにアクセスする
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# 最初の日付行フィールドを月と四半期でグループ化する
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# ピボットテーブルのデータを計算して出力ファイルを保存する
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

### **Group a Numeric Field into Ranges**
サンプルピボットテーブルの `FieldTwo` は最初はデータ（値）フィールドです。行または列フィールドのみをグループ化できるため、コードは最初に `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` を呼び出して `FieldTwo` を行領域に移動し、ピボットを更新してから、`StartNumber = 0`、`EndNumber = 5`、および `Interval = 2` を使用して数値フィールドを 0-1、2-3、4-5 の範囲にグループ化します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# サンプルワークブックを読み込む
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 2番目のワークシートとそのピボットテーブルにアクセスする
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo はデータフィールドです: まず行エリアに移動します,
# 行/列フィールドのみをグループ化できるためです
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# 数値フィールドを 0-1, 2-3, 4-5 の範囲にグループ化します
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# ピボットテーブルのデータを計算し、出力ファイルを保存します
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Note**

{{% alert color="primary" %}}
- `PivotField.groupBy()` メソッドのオーバーロードは非推奨であり、API サーフェスから削除されています。`PivotField.group()` および `PivotField.group(PivotFieldGroupOptions)` が代替です。
- Microsoft Excel では、数値フィールドをグループ化すると元のピボットフィールドがグループ化された範囲に置き換えられますが、日付フィールドをグループ化すると元のフィールドの横に新しいピボットフィールド（グループレベルごとに 1 つ、たとえば四半期と月）が作成されます。Aspose.Cells 26.10 以降、`PivotField.group()` メソッドは Excel と同じ動作に従います。`PivotFieldGroupOptions.NewPivotField` プロパティは古いバージョンとの互換性のために存在します。数値グループ化ではデフォルトで false、日時グループ化ではデフォルトで true になります。日付グループ化で新しいピボットフィールドを作成する代わりに元のピボットフィールドを置き換えたい場合は false に設定します。
- `PivotFieldGroupOptions.Interval` プロパティは、数値グループ化および日付の日単位のグループ化（たとえば、日付を 7 日周期にグループ化）の場合にのみ有効で、日付が月、四半期、または年でグループ化される場合には無視されます。
{{% /alert %}}

## **Related Articles**
- [ピボットテーブルに行と列のフィールドを追加する](/cells/ja/python-java/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリングする](/cells/ja/python-java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加する](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/python-java/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}