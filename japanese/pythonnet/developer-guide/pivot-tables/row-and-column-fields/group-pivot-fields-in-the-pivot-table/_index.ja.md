---
title: ピボットテーブルでピボットフィールドをグループ化する
linktitle: ピボットテーブルでピボットフィールドをグループ化する
description: Aspose.Cells for Python via .NET で、PivotField.Group および PivotFieldGroupOptions を使用して、ピボットテーブル内の行および列のピボットフィールドを月や四半期などの日付期間や数値範囲にグループ化する方法を説明します。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.Group, PivotFieldGroupOptions, 日付のグループ化, 数値のグループ化, 月, 四半期, 数値範囲, Python via .NET
type: docs
weight: 80
url: /ja/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能な使用シナリオ**
- ピボットフィールドのグループ化は、ピボットテーブルの行フィールドまたは列フィールドに多数の異なる項目（日付フィールドに含まれる数百の日付や、数値フィールドに含まれる多数の散在する値など）が含まれている場合に役立ちます。グループ化により、これらの項目が意味のあるセクション（日付は月、四半期、年、数値は 0-1、2-3、4-5 などの範囲）に集約されます。これにより、大規模なピボットテーブルがコンパクトになり、分析しやすくなります。Aspose.Cells for Python via .NET は、`pivot_field.group()` メソッド（データ型による自動グループ化）と `pivot_field.group(pivot_field_group_options)`（カスタムグループ化オプション）によってこの機能を提供します。
- 日付のグループ化では、個々の日付を日、月、四半期、年などのより大きな期間にまとめ、時系列階層（たとえば年、四半期、月）を構築します。経時的な傾向を一目で把握できるようになり、各期間レベルがピボットテーブルの行または列領域に独自のピボットフィールドとして表示されます。
- グループ化は、ピボットテーブルの ROW（行）または COLUMN（列）領域に配置されたフィールドに対してのみ使用できます。データ（値）フィールドは直接グループ化できません。そのようなフィールドをグループ化するには、最初にピボットテーブルの行または列領域に追加する必要があります。

## **ピボットフィールドを自動的にグループ化する**
パラメーターなしの `pivot_field.group()` オーバーロードは、フィールドのデータ型を検査して自動的にグループ化します。日付のみ（および空白）を含むフィールドは月単位でグループ化されます。数値のみ（および空白）を含むフィールドは、自動間隔を使用して数値範囲にグループ化されます。

```python
import aspose.cells as ac
# サンプルワークブックを読み込む
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 2番目のワークシートとそのピボットテーブルにアクセスする
pt = wb.worksheets[1].pivot_tables[0]
# 最初の行フィールドを自動的にグループ化します。
# フィールドには日付が含まれているため、月ごとにグループ化されます。
field = pt.row_fields[0]
field.group()
# ピボットテーブルのデータを計算して出力ファイルを保存する
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **カスタムオプションでピボットフィールドをグループ化する**
`PivotFieldGroupOptions` クラスは、カスタムグループ化設定を提供します。日付フィールドの場合は `start_date`、`end_date`、`group_types` を設定します。数値フィールドの場合は `start_number`、`end_number`、`interval` を設定します。`new_pivot_field` プロパティは、グループ化によって元のフィールドに加えて新しいピボットフィールドを作成するかどうかを制御します（この記事の最後の「Note」セクションを参照してください）。

### **日付フィールドを月と四半期でグループ化する**
次の例では、サンプルピボットテーブルの日付行フィールドを、開始日から終了日までの間で月と四半期にグループ化します。コードは [サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx) を読み込み、グループ化を実行し、ピボットテーブルのデータを計算して、グループ化された結果を保存します。スクリーンショットはその効果を示しています。日付行フィールドが四半期と月でグループ化されています。
`options.group_types` 内の値の順序は無視されることに注意してください。グループのタイプがどのような順序で記載されていても、グループ化されたフィールドは常に最大の期間から最小の期間の順に表示されます。年、四半期、月、日、時、分、秒です。この例では `options.group_types` で月が四半期より前に記載されていますが、四半期は外側のレベル、月は内側のレベルとして表示されます。

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# サンプルワークブックを読み込む
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 2 番目のワークシートとそのピボットテーブルにアクセスする
pt = wb.worksheets[1].pivot_tables[0]
# 最初の日付フィールドの行フィールドを月と四半期でグループ化する
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# ピボットテーブルのデータを計算して出力ファイルを保存する
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![ピボットテーブルを月と四半期でグループ化した結果](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化する**
サンプルピボットテーブルの `FieldTwo` は、当初はデータ（値）フィールドです。グループ化できるのは行または列フィールドのみであるため、コードは最初に `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` を呼び出して `FieldTwo` を行領域に移動し、ピボットを更新してから、`start_number=0`、`end_number=5`、`interval=2` を使用して数値フィールドを 0-1、2-3、4-5 の範囲にグループ化します。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# サンプルワークブックを読み込む
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 2番目のワークシートとそのピボットテーブルにアクセスする
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwoはデータフィールドです：まず行エリアに移動します、
# 行/列フィールドのみグループ化できるためです
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# 数値フィールドを0-1、2-3、4-5の範囲にグループ化する
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# ピボットテーブルのデータを計算し、出力ファイルを保存する
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **注記**

{{% alert color="primary" %}}
- `pivot_field.group_by()` メソッドのオーバーロードは非推奨となり、API サーフェスから削除されました。`pivot_field.group()` および `pivot_field.group(pivot_field_group_options)` が代替となります。
- Microsoft Excel では、数値フィールドをグループ化すると元のパイボットフィールドがグループ化された範囲に置き換えられますが、日付フィールドをグループ化すると、元のパイボットフィールドの隣に新しいピボットフィールド（グループレベルごとに 1 つ、たとえば四半期や月）が作成されます。Aspose.Cells 26.10 以降、`pivot_field.group()` メソッドは Excel と同じ動作に従います。`PivotFieldGroupOptions.new_pivot_field` プロパティは古いバージョンとの互換性のために存在します。数値グループ化のデフォルトは false、日時グループ化のデフォルトは true です。日付グループ化で元のパイボットフィールドを置き換える（新しいピボットフィールドを作成しない）場合は、false に設定してください。
- `PivotFieldGroupOptions.interval` プロパティは、数値グループ化および日単位での日付グループ化（たとえば、日付を 7 日単位の期間にグループ化する）にのみ有効です。月、四半期、年で日付をグループ化する場合には無視されます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルで行と列のフィールドを追加する](/cells/ja/python-net/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリングする](/cells/ja/python-net/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加する](/cells/ja/python-net/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/python-net/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}