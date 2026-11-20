---
title: ピボットテーブルでピボットフィールドをグループ化
linktitle: ピボットテーブルでピボットフィールドをグループ化
description: Aspose.Cells for Python via Java で、ピボットテーブルの行および列のピボットフィールドを月や四半期などの期間や数値範囲にグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.group, PivotFieldGroupOptions, 日付のグループ化, 数値のグループ化, 月, 四半期, 数値範囲, Python
type: docs
weight: 80
url: /ja/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **想定される使用シナリオ**
- ピボットフィールドのグループ化は、ピボットテーブルの行または列フィールドに多数の異なる項目が含まれている場合に便利です。たとえば、数百の日付が含まれる日付フィールドや、散在した多数の数値が含まれる数値フィールドがあります。グループ化により、これらの項目を意味のあるセクションにまとめることができます。日付は月、四半期、年に、数値は 0‑1、2‑3、4‑5 などの範囲にまとめられます。これにより、大規模なピボットテーブルがコンパクトになり、分析が容易になります。Aspose.Cells は `PivotField.group()` メソッド（データ型による自動グループ化）と `PivotField.group(PivotFieldGroupOptions)`（カスタム グループ化オプション）でこの機能を提供します。
- 日付のグループ化は、個々の日付を日、月、四半期、年などの大きな期間にまとめ、時間階層（例: 年、四半期、月）を構築します。時間経過によるトレンドが一目で把握でき、各期間レベルがピボットテーブルの行または列エリアに独立したピボットフィールドとして表示されます。
- グループ化は、ピボットテーブルの ROW または COLUMN エリアに配置されたフィールドに対してのみ利用可能です。データ（値）フィールドは直接グループ化できません。そのようなフィールドをグループ化するには、まずピボットテーブルの行または列エリアに追加する必要があります。

## **ピボットフィールドを自動的にグループ化**
パラメータなしの `PivotField.group()` オーバーロードは、フィールドのデータ型を検査し、自動的にグループ化します。日付（および空白）だけを含むフィールドは月単位でグループ化され、数値（および空白）だけを含むフィールドは自動間隔を使用して数値範囲にグループ化されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load the sample workbook
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Access the second worksheet and its pivot table
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Group the first row field automatically.
# The field contains dates, so it is grouped by months.
field = pt.getRowFields().get(0)
field.group()
# Calculate the pivot table data and save the output file
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **カスタム オプションでピボットフィールドをグループ化**
`PivotFieldGroupOptions` クラスはカスタム グループ化設定を提供します。日付フィールドの場合は `StartDate`、`EndDate`、`GroupTypes` を設定し、数値フィールドの場合は `StartNumber`、`EndNumber`、`Interval` を設定します。`NewPivotField` プロパティは、グループ化が元のフィールドと並行して新しいピボットフィールドを作成するかどうかを制御します（この記事の最後の Note セクションを参照）。

### **月と四半期で日付フィールドをグループ化**
次の例は、サンプル ピボットテーブルの日付行フィールドを開始日と終了日の間で月と四半期にグループ化します。コードは [サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx) を読み込み、グループ化を実行し、ピボットテーブル データを計算して、グループ化された結果を保存します。スクリーンショットは効果を示しています：日付行フィールドが現在四半期と月でグループ化されています。  
`options.GroupTypes` に含まれる値の順序は無視されます。グループ タイプがどの順序で列挙されても、グループ化されたフィールドは常に最も大きな期間から最も小さな期間へ（年、四半期、月、日、時間、分、秒）の順に表示されます。この例では `options.GroupTypes` で月が四半期より先に列挙されていますが、四半期が外側のレベル、月が内側のレベルとして表示されます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# Load the sample workbook
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Access the second worksheet and its pivot table
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Group the first row field (a date field) by months and quarters
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# Calculate the pivot table data and save the output file
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![月と四半期でグループ化されたピボットテーブル](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化**
サンプル ピボットテーブルの `FieldTwo` は最初はデータ（値）フィールドです。行または列フィールドのみがグループ化できるため、コードは最初に `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` を呼び出して `FieldTwo` を行エリアに移動し、ピボットを更新した後、`StartNumber = 0`、`EndNumber = 5`、`Interval = 2` を使用して数値フィールドを 0‑1、2‑3、4‑5 の範囲にグループ化します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Load the sample workbook
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Access the second worksheet and its pivot table
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo is a data field: move it to the row area first,
# because only row/column fields can be grouped
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Group the numeric field into the ranges 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Calculate the pivot table data and save the output file
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Note**

{{% alert color="primary" %}}
- `PivotField.groupBy()` メソッドのオーバーロードは非推奨となり、API から削除されました。代わりに `PivotField.group()` と `PivotField.group(PivotFieldGroupOptions)` を使用します。
- Microsoft Excel では、数値フィールドをグループ化すると元のピボットフィールドがグループ化された範囲に置き換えられますが、日付フィールドをグループ化すると元のフィールドの横に新しいピボットフィールド（各グループ レベルごとに 1 つ、例: 四半期と月）が作成されます。Aspose.Cells 26.10 以降、`PivotField.group()` メソッドは Excel と同じ動作を行います。`PivotFieldGroupOptions.NewPivotField` プロパティは旧バージョンとの互換性のために存在し、数値グループ化ではデフォルトが false、日時グループ化では true です。元のピボットフィールドを置き換えて日付をグループ化したい場合は false に設定してください。
- `PivotFieldGroupOptions.Interval` プロパティは数値グループ化および日単位の日時グループ化（例: 7 日間隔）でのみ有効です。月、四半期、年で日付がグループ化される場合は無視されます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルに行および列フィールドを追加](/cells/ja/python-java/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/python-java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/python-java/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/python-java/apply-style-to-pivot-table/)
- [ピボットテーブルを更新](/cells/ja/python-java/refresh-pivot-table/)
- [ピボットフィールドのアイテムを個別にグループ化](/cells/ja/python-java/discrete-group-pivot-fields/)

{{< app/cells/assistant language="python" >}}