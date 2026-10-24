---
title: ピボットテーブルでピボットフィールドをグループ化する
linktitle: ピボットテーブルでピボットフィールドをグループ化する
description: Aspose.Cells for Node.js via C++ で PivotField.Group および PivotFieldGroupOptions を使用して、ピボットテーブルの行および列のピボットフィールドを月や四半期などの日付期間や数値範囲にグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.Group, PivotFieldGroupOptions, 日付のグループ化, 数値のグループ化, 月, 四半期, 数値範囲, JavaScript
type: docs
weight: 80
url: /ja/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
- ピボットフィールドのグループ化は、ピボットテーブルの行または列フィールドに多数の個別項目(数百の日付を含む日付フィールドや、多くの散在する値を含む数値フィールドなど)が含まれている場合に役立ちます。グループ化により、これらの項目を意味のあるセクション(日付なら月、四半期、年、数値なら 0-1、2-3、4-5 などの範囲)に集約できます。これにより、大規模なピボットテーブルがコンパクトになり、分析しやすくなります。Aspose.Cells は `pivotField.group()` メソッド(データ型による自動グループ化)と `pivotField.group(PivotFieldGroupOptions)`(カスタムグループ化オプション)を通じてこの機能を提供します。
- 日付のグループ化は、個々の日付を日、月、四半期、年などの大きな期間にまとめ、時間の階層(たとえば年、四半期、月)を構築します。時間の経過に伴う傾向が一目でわかるようになり、各期間レベルがピボットテーブルの行または列領域内の独自のピボットフィールドになります。
- グループ化は、ピボットテーブルの行または列領域に配置されたフィールドに対してのみ使用できます。データ(値)フィールドを直接グループ化することはできません。そのようなフィールドをグループ化するには、最初にピボットテーブルの行または列領域に追加する必要があります。

## **ピボットフィールドを自動的にグループ化する**
パラメーターなしの `pivotField.group()` オーバーロードは、フィールドのデータ型を検査し、自動的にグループ化します。日付のみ(および空白)を含むフィールドは月でグループ化されます。数値のみ(および空白)を含むフィールドは、自動間隔を使用して数値範囲にグループ化されます。

```javascript
const AsposeCells = require("aspose.cells.node");
// サンプルワークブックを読み込む
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセスする
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// 最初の行フィールドを自動的にグループ化する。
// フィールドには日付が含まれているため、月ごとにグループ化されます。
const field = pt.getRowFields().get(0);
field.group();
// ピボットテーブルのデータを計算して出力ファイルを保存する
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **カスタムオプションでピボットフィールドをグループ化する**
`PivotFieldGroupOptions` クラスはカスタムグループ化設定を提供します。日付フィールドの場合は `startDate`、`endDate`、`groupTypes` を設定します。数値フィールドの場合は `startNumber`、`endNumber`、`interval` を設定します。`newPivotField` プロパティは、グループ化によって元のフィールドに加えて新しいピボットフィールドを作成するかどうかを制御します(この記事の最後の「注意」セクションを参照してください)。

### **日付フィールドを月と四半期でグループ化する**
次の例は、サンプルピボットテーブルの日付行フィールドを、指定された開始日と終了日の間で月と四半期によってグループ化します。コードは[サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx)を読み込み、グループ化を実行し、ピボットテーブルのデータを計算して、グループ化された結果を保存します。スクリーンショットはその効果を示しています。日付行フィールドが四半期と月でグループ化されています。
`options.groupTypes` の値の順序は無視されることに注意してください。グループタイプがどの順序でリストされていても、グループ化されたフィールドは常に最大の期間から最小の期間の順(年、四半期、月、日、時、分、秒)で表示されます。この例では、`options.groupTypes` で月が四半期より前にリストされていますが、四半期が外側のレベル、月が内側のレベルとして表示されます。

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセスします
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// 最初の日付フィールド（日時フィールド）を月と四半期でグループ化します
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// ピボットテーブルのデータを計算して出力ファイルを保存します
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![月と四半期でグループ化されたピボットテーブル](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化する**
サンプルピボットテーブルの `FieldTwo` は最初はデータ(値)フィールドです。行または列フィールドのみがグループ化できるため、コードはまず `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` を呼び出して `FieldTwo` を行領域に移動し、ピボットを更新してから、`startNumber = 0`、`endNumber = 5`、`interval = 2` を使用して数値フィールドを 0-1、2-3、4-5 の範囲にグループ化します。

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセス
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwoはデータフィールドです: 最初に列エリアに移動します、
// 行/列フィールドのみをグループ化できるため
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// 数値フィールドを0-1、2-3、4-5の範囲にグループ化します
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// ピボットテーブルのデータを計算し、出力ファイルを保存します
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **注意**

{{% alert color="primary" %}}
- `pivotField.groupBy()` メソッドのオーバーロードは非推奨となり、API 表面から削除されました。代わりに `pivotField.group()` および `pivotField.group(PivotFieldGroupOptions)` を使用してください。
- Microsoft Excel では、数値フィールドをグループ化すると元のピボットフィールドがグループ化された範囲に置き換えられますが、日付フィールドをグループ化すると元のフィールドの横に新しいピボットフィールド(グループレベルごとに 1 つ、たとえば四半期や月)が作成されます。Aspose.Cells 26.10 以降、`pivotField.group()` メソッドは Excel と同じ動作に従います。`pivotFieldGroupOptions.newPivotField` プロパティは古いバージョンとの互換性のために存在します。デフォルトでは、数値グループ化では false、日時グループ化では true になります。日付グループ化で新しいピボットフィールドを作成する代わりに元のピボットフィールドを置き換える場合は、これを false に設定してください。
- `pivotFieldGroupOptions.interval` プロパティは、数値グループ化および日単位での日付グループ化(たとえば、日付を 7 日周期にグループ化する)に対してのみ有効です。日付を月、四半期、年でグループ化する場合は無視されます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルで行と列のフィールドを追加する](/cells/ja/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルターする](/cells/ja/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加する](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}