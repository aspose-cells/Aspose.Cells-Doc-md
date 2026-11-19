---
title: ピボットテーブルでピボットフィールドをグループ化
linktitle: ピボットテーブルでピボットフィールドをグループ化
description: Aspose.Cells for Java の PivotField.group と PivotFieldGroupOptions を使用して、ピボットテーブルの行および列ピボットフィールドを月や四半期などの日付期間や数値範囲にグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.group, PivotFieldGroupOptions, 日付のグループ化, 数値のグループ化, 月, 四半期, 数値範囲, Java
type: docs
weight: 80
url: /ja/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
- ピボットフィールドのグループ化は、ピボットテーブルの行または列フィールドに多数の個別項目が含まれる場合に便利です。たとえば、数百の日付がある日付フィールドや、多くの散在した値を持つ数値フィールドです。グループ化により、これらの項目が意味のあるセクションにまとめられます。日付は月、四半期、年に、数値は 0‑1、2‑3、4‑5 などの範囲にグループ化されます。これにより、大きなピボットテーブルがコンパクトになり、分析が容易になります。Aspose.Cells は `PivotField.group()` メソッド（データ型による自動グループ化）および `PivotField.group(PivotFieldGroupOptions)`（カスタムグループ化オプション）を通じてこの機能を提供します。
- 日付のグループ化は個々の日付を日、月、四半期、年といった大きな期間にまとめ、時間階層（例：年、四半期、月）を構築します。時間経過によるトレンドが一目で分かり、各期間レベルがピボットテーブルの行または列領域の独立したピボットフィールドとなります。
- グループ化はピボットテーブルの ROW または COLUMN エリアに配置されたフィールドにのみ適用可能です。データ（値）フィールドは直接グループ化できません。そのようなフィールドをグループ化するには、まずピボットテーブルの行または列エリアに追加する必要があります。

## **ピボットフィールドを自動的にグループ化**
パラメータなしの `PivotField.group()` オーバーロードはフィールドのデータ型を検査し、自動的にグループ化します。日付（および空白）のみを含むフィールドは月単位でグループ化され、数値（および空白）のみを含むフィールドは自動間隔を使用して数値範囲にグループ化されます。

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **カスタムオプションでピボットフィールドをグループ化**
`PivotFieldGroupOptions` クラスはカスタムグループ化設定を提供します。日付フィールドの場合は `startDate`、`endDate`、`groupTypes` を設定します。数値フィールドの場合は `startNumber`、`endNumber`、`interval` を設定します。`newPivotField` プロパティは、グループ化時に元のフィールドと並んで新しいピボットフィールドを作成するかどうかを制御します（この記事の最後の Note セクションを参照）。

### **日付フィールドを月および四半期でグループ化**
次の例は、サンプルピボットテーブルの日付行フィールドを開始日と終了日の間で月と四半期にグループ化します。コードは [sample Excel file](sampleGroupPivotFieldsInPivotTable.xlsx) を読み込み、グループ化を実行し、ピボットテーブルデータを計算し、グループ化された結果を保存します。スクリーンショットはその効果を示しており、日付行フィールドが四半期と月でグループ化されていることが分かります。  
`options.groupTypes` の値の順序は無視されます。グループタイプの列挙順に関係なく、グループ化されたフィールドは常に最も大きな期間から最も小さな期間へと表示されます：年、四半期、月、日、時、分、秒。この例では `options.groupTypes` に月が四半期より先に記述されていますが、四半期が外側のレベル、月が内側のレベルとして表示されます。

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![月と四半期でグループ化されたピボットテーブル](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化**
`FieldTwo` はサンプルピボットテーブルのデータ（値）フィールドとして最初に存在します。行または列フィールドのみがグループ化できるため、コードは最初に `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` を呼び出して `FieldTwo` を行エリアに移動し、ピボットテーブルをリフレッシュした後、`startNumber = 0`、`endNumber = 5`、`interval = 2` を使用して数値フィールドを 0‑1、2‑3、4‑5 の範囲にグループ化します。

```java
import com.aspose.cells.*;
// Load the sample workbook
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Access the second worksheet and its pivot table
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo is a data field: move it to the row area first,
// because only row/column fields can be grouped
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Group the numeric field into the ranges 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Calculate the pivot table data and save the output file
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Note**

{{% alert color="primary" %}}
- `PivotField.groupBy()` メソッドのオーバーロードは非推奨となり、API から削除されました。代わりに `PivotField.group()` および `PivotField.group(PivotFieldGroupOptions)` が使用されます。
- Microsoft Excel では、数値フィールドをグループ化すると元のピボットフィールドはグループ化された範囲で置き換えられますが、日付フィールドをグループ化すると元のフィールドの横に新しいピボットフィールド（各グループレベルごとに 1 つ、例: 四半期と月）が作成されます。Aspose.Cells 26.10 以降、`PivotField.group()` メソッドは Excel と同様の動作をします。`PivotFieldGroupOptions.newPivotField` プロパティは旧バージョンとの互換性のために存在し、数値グループ化ではデフォルトが false、日付時刻グループ化では true です。元のピボットフィールドを置き換えて日付をグループ化したい場合は false に設定してください。
- `PivotFieldGroupOptions.interval` プロパティは数値グループ化と日単位の日付グループ化（例: 7 日間の期間に日付をグループ化）でのみ有効で、月、四半期、年での日付グループ化時には無視されます。
{{% /alert %}}

## **Related Articles**
- [ピボットテーブルに行と列のフィールドを追加](/cells/ja/java/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/java/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルをリフレッシュ](/cells/ja/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}