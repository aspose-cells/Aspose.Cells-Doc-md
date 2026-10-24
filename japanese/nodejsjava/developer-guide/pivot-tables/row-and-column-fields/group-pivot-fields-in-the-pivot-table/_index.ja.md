---
title: ピボットテーブルでピボットフィールドをグループ化する
linktitle: ピボットテーブルでピボットフィールドをグループ化する
description: Aspose.Cells for Node.js via Java の PivotField.group と PivotFieldGroupOptions を使用して、ピボットテーブルの行と列のピボットフィールドを月や四半期などの日付期間や数値範囲にグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.group, PivotFieldGroupOptions, 日付グループ化, 数値グループ化, 月, 四半期, 数値範囲, Node.js
type: docs
weight: 80
url: /ja/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能な使用シナリオ**
- ピボットフィールドのグループ化は、ピボットテーブルの行または列フィールドに多数の異なる項目(数百の日付を含む日付フィールドや、多くの散在した値を含む数値フィールドなど)が含まれている場合に役立ちます。グループ化により、これらの項目が意味のあるセクションにまとめられます。日付は月、四半期、年単位にまとめられ、数値は 0-1、2-3、4-5 などの範囲にまとめられます。これにより、大規模なピボットテーブルがコンパクトになり、分析しやすくなります。Aspose.Cells for Node.js via Java は、`PivotField.group()` メソッド(データ型による自動グループ化)と `PivotField.group(PivotFieldGroupOptions)`(カスタムグループ化オプション)を通じてこの機能を提供します。
- 日付グループ化は、個々の日付を日、月、四半期、年などの大きな期間にまとめ、時系列階層(例: 年、四半期、月)を構築します。時間の経過に伴う傾向が見えるようになり、各期間レベルはピボットテーブルの行または列領域に独自のピボットフィールドとして表示されます。
- グループ化は、ピボットテーブルの ROW または COLUMN 領域に配置されたフィールドでのみ使用できます。データ(値)フィールドを直接グループ化することはできません。このようなフィールドをグループ化するには、まずピボットテーブルの行または列領域に追加する必要があります。

## **ピボットフィールドを自動的にグループ化する**
パラメーターなしの `PivotField.group()` オーバーロードは、フィールドのデータ型を検査し、自動的にグループ化します。日付(および空白)のみを含むフィールドは月でグループ化されます。数値(および空白)のみを含むフィールドは、自動間隔を使用して数値範囲にグループ化されます。

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセスします
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// 最初の行フィールドを自動的にグループ化します。
// フィールドには日付が含まれているため、月単位でグループ化されます。
let field = pt.getRowFields().get(0);
field.group();
// ピボットテーブルのデータを計算し、出力ファイルを保存します
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **カスタムオプションでピボットフィールドをグループ化する**
`PivotFieldGroupOptions` クラスはカスタムグループ化設定を提供します。日付フィールドの場合は、`StartDate`、`EndDate`、`GroupTypes` を設定します。数値フィールドの場合は、`StartNumber`、`EndNumber`、`Interval` を設定します。`NewPivotField` プロパティは、グループ化によって元のフィールドの隣に新しいピボットフィールドを作成するかどうかを制御します(この記事の最後にある注意セクションを参照)。

### **日付フィールドを月と四半期でグループ化する**
次の例は、サンプルピボットテーブルの日付行フィールドを、指定された開始日と終了日の間で月や四半期に基づいてグループ化します。コードは[サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx)を読み込み、グループ化を実行し、ピボットテーブルのデータを計算して、グループ化した結果を保存します。スクリーンショットはその効果を示しています。日付行フィールドが四半期と月でグループ化されています。
`options.GroupTypes` の値の順序は無視されることに注意してください。グループタイプがどの順序でリストされていても、グループ化されたフィールドは常に最大の期間から最小の期間へと表示されます。年、四半期、月、日、時間、分、秒の順です。この例では、`options.GroupTypes` で月が四半期より前にリストされていますが、四半期が外側のレベル、月が内側のレベルとして表示されます。

```javascript
const AsposeCells = require("aspose.cells");
// サンプルワークブックを読み込む
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセス
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// 最初の行フィールド（日付フィールド）を月と四半期でグループ化する
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// ピボットテーブルのデータを計算し、出力ファイルを保存する
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![月と四半期でグループ化されたピボットテーブル](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化する**
サンプルピボットテーブルの `FieldTwo` は、最初はデータ(値)フィールドです。行または列フィールドのみがグループ化できるため、コードは最初に `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` を呼び出して `FieldTwo` を行領域に移動し、ピボットを更新してから、数値フィールドを `StartNumber = 0`、`EndNumber = 5`、`Interval = 2` を使用して 0-1、2-3、4-5 の範囲にグループ化します。

```javascript
const AsposeCells = require("aspose.cells");
// サンプルワークブックを読み込む
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセスする
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwoはデータフィールドです: まず行エリアに移動します、
// 行/列フィールドのみグループ化できるためです
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// 数値フィールドを0-1、2-3、4-5の範囲にグループ化する
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// ピボットテーブルのデータを計算して出力ファイルを保存する
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **注意**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` メソッド オーバーロードは非推奨となり、API サーフェスから削除されました。`PivotField.group()` と `PivotField.group(PivotFieldGroupOptions)` が代替です。
- Microsoft Excel では、数値フィールドをグループ化すると、元のピボットフィールドがグループ化された範囲に置き換えられます。一方、日付フィールドをグループ化すると、元のフィールドの隣に新しいピボットフィールド(グループレベルごとに 1 つ、たとえば四半期と月)が作成されます。Aspose.Cells for Node.js via Java 26.10 以降、`PivotField.group()` メソッドは Excel と同じ動作に従います。`PivotFieldGroupOptions.NewPivotField` プロパティは古いバージョンとの互換性のために存在します。数値グループ化の場合は既定で false、日時グループ化の場合は true になります。日付グループ化で新しいピボットフィールドを作成する代わりに元のピボットフィールドを置き換えたい場合は、false に設定します。
- `PivotFieldGroupOptions.Interval` プロパティは、数値グループ化および日単位での日付グループ化(たとえば、日付を 7 日間の期間にグループ化する)に対してのみ有効であり、月、四半期、年で日付をグループ化する場合は無視されます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルで行と列フィールドを追加する](/cells/ja/nodejs-java/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルターする](/cells/ja/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加する](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/nodejs-java/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}