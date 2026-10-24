---
title: ピボットテーブルでピボットフィールドをグループ化する
linktitle: ピボットテーブルでピボットフィールドをグループ化する
description: Aspose.Cells for Java の PivotField.group と PivotFieldGroupOptions を使用して、ピボットテーブル内の行および列のピボットフィールドを、月や四半期などの日付期間や数値範囲にグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.group, PivotFieldGroupOptions, 日付のグループ化, 数値のグループ化, 月, 四半期, 数値範囲, Java
type: docs
weight: 80
url: /ja/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **想定される利用シナリオ**
- ピボットフィールドのグループ化は、ピボットテーブルの行フィールドまたは列フィールドに多数の個別項目（たとえば、数百の日付を含む日付フィールドや、多くの散在する値を含む数値フィールド）が含まれている場合に役立ちます。グループ化により、これらの項目が意味のあるセクションにまとめられます。日付は月、四半期、年単位にまとめられ、数値は 0-1、2-3、4-5 などの範囲にまとめられます。これにより、大規模なピボットテーブルがコンパクトになり、分析しやすくなります。Aspose.Cells はこの機能を `PivotField.group()` メソッド（データ型に基づく自動グループ化）および `PivotField.group(PivotFieldGroupOptions)`（カスタム グループ化オプション）で提供しています。
- 日付のグループ化は、個々の日付を日、月、四半期、年といったより大きな期間にまとめ、時間の階層（たとえば、年、四半期、月）を作成します。時間の経過に伴う傾向を一目で把握できるようになり、各期間レベルがピボットテーブルの行エリアまたは列エリア内の独自のピボットフィールドになります。
- グループ化は、ピボットテーブルの ROW または COLUMN エリアに配置されたフィールドに対してのみ可能です。データ（値）フィールドを直接グループ化することはできません。そのようなフィールドをグループ化するには、まずピボットテーブルの行エリアまたは列エリアに追加する必要があります。

## **ピボットフィールドを自動的にグループ化する**
パラメータなしの `PivotField.group()` オーバーロードは、フィールドのデータ型を検査し、自動的にグループ化します。日付のみ（および空白）を含むフィールドは月単位でグループ化されます。数値のみ（および空白）を含むフィールドは、自動的な間隔で数値範囲にグループ化されます。

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **カスタムオプションでピボットフィールドをグループ化する**
`PivotFieldGroupOptions` クラスは、カスタム グループ化の設定を提供します。日付フィールドの場合は `startDate`、`endDate`、および `groupTypes` を設定します。数値フィールドの場合は `startNumber`、`endNumber`、および `interval` を設定します。`newPivotField` プロパティは、グループ化によって元のフィールドに加えて新しいピボットフィールドを作成するかどうかを制御します（この記事の最後の「注意」セクションを参照してください）。

### **日付フィールドを月と四半期単位でグループ化する**
次の例は、サンプル ピボットテーブルの日付行フィールドを、指定された開始日と終了日の間で月と四半期単位にグループ化します。コードは[サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx)を読み込み、グループ化を実行し、ピボットテーブルのデータを計算して、グループ化された結果を保存します。スクリーンショットはその効果を示しています。日付行フィールドが四半期と月でグループ化されています。
`options.groupTypes` 内の値の順序は無視されることに注意してください。グループタイプがどの順序で記載されていても、グループ化されたフィールドは常に最大の期間から最小の期間の順に表示されます。年、四半期、月、日、時間、分、秒の順です。この例では、`options.groupTypes` で月が四半期より前に記載されていますが、四半期が外側のレベル、月が内側のレベルとして表示されます。

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

### **数値フィールドを範囲にグループ化する**
サンプル ピボットテーブルの `FieldTwo` は最初はデータ（値）フィールドです。行フィールドまたは列フィールドのみがグループ化可能なため、コードはまず `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` を呼び出して `FieldTwo` を行エリアに移動し、ピボットを更新してから、`startNumber = 0`、`endNumber = 5`、および `interval = 2` を使用して数値フィールドを 0-1、2-3、4-5 の範囲にグループ化します。

```java
import com.aspose.cells.*;
// サンプルワークブックを読み込む
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセスする
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwoはデータフィールドです：まず行エリアに移動します、
// 行/列フィールドのみグループ化できるためです
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// 数値フィールドを0-1、2-3、4-5の範囲にグループ化する
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// ピボットテーブルのデータを計算し、出力ファイルを保存する
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **注意**

{{% alert color="primary" %}}
- `PivotField.groupBy()` メソッドのオーバーロードは非推奨となり、API 表面から削除されました。`PivotField.group()` と `PivotField.group(PivotFieldGroupOptions)` が代替となります。
- Microsoft Excel では、数値フィールドをグループ化すると元のピボットフィールドがグループ化された範囲に置き換えられますが、日付フィールドをグループ化すると元のフィールドの隣に新しいピボットフィールド（グループレベルごとに 1 つ、四半期や月など）が組み込まれます。Aspose.Cells 26.10 以降、`PivotField.group()` メソッドは Excel と同じ動作に従います。`PivotFieldGroupOptions.newPivotField` プロパティは古いバージョンとの互換性のために存在します。数値グループ化ではデフォルトで false、日時グループ化では true になります。日付グループ化で新しいピボットフィールドを作成するのではなく置き換えたい場合は、false に設定してください。
- `PivotFieldGroupOptions.interval` プロパティは、数値グループ化と日単位での日付グループ化（たとえば、日付を 7 日単位の期間にグループ化する）の場合にのみ有効であり、月、四半期、年単位で日付をグループ化する場合には無視されます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルで行と列のフィールドを追加する](/cells/ja/java/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリングする](/cells/ja/java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加する](/cells/ja/java/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}