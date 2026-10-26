---
title: ピボットテーブルでピボットフィールドをグループ化する
linktitle: ピボットテーブルでピボットフィールドをグループ化する
description: Aspose.Cells for .NET で、PivotField.Group と PivotFieldGroupOptions を使用して、ピボットテーブルの行および列のピボットフィールドを月や四半期などの日付期間や数値範囲にグループ化する方法を説明します。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.Group, PivotFieldGroupOptions, 日付のグループ化, 数値のグループ化, 月, 四半期, 数値範囲, C#
type: docs
weight: 80
url: /ja/net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **想定される使用シナリオ**
- ピボットテーブルの行または列フィールドに多数の日付を含む日付フィールドや、多数の散在した値を含む数値フィールドなど、多くの異なる項目が含まれている場合、ピボットフィールドのグループ化が役立ちます。グループ化により、これらの項目を意味のあるセクションにまとめます。日付を月、四半期、年ごとにまとめ、数値を 0-1、2-3、4-5 などの範囲にまとめます。これにより、大規模なピボットテーブルがコンパクトになり、分析しやすくなります。Aspose.Cells はこの機能を `PivotField.Group()` メソッド (データ型による自動グループ化) と `PivotField.Group(PivotFieldGroupOptions)` (カスタムグループ化オプション) で提供しています。
- 日付のグループ化では、個々の日付を日、月、四半期、年などのより大きな期間にまとめ、時間の階層構造 (年、四半期、月など) を構築します。経時的な傾向を一目で把握できるようになり、各期間レベルはピボットテーブルの行または列エリア内の独自のピボットフィールドになります。
- グループ化は、ピボットテーブルの ROW または COLUMN エリアに配置されたフィールドでのみ使用できます。データ(値)フィールドを直接グループ化することはできません。そのようなフィールドをグループ化するには、まずピボットテーブルの行または列エリアに追加する必要があります。

## **ピボットフィールドを自動的にグループ化する**
引数なしの `PivotField.Group()` オーバーロードは、フィールドのデータ型を調べて自動的にグループ化します。日付(および空白)のみを含むフィールドは月別にグループ化されます。数値(および空白)のみを含むフィールドは、自動間隔を使用して数値範囲にグループ化されます。

```csharp
using Aspose.Cells.Pivot;
// サンプルワークブックを読み込む
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセスする
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// 最初の行フィールドを自動的にグループ化する。
// フィールドには日付が含まれているため、月ごとにグループ化されます。
PivotField field = pt.RowFields[0];
field.Group();
// ピボットテーブルのデータを計算し、出力ファイルを保存する
pt.CalculateData();
wb.Save("outputAutoGroupPivotField.xlsx");
```

## **カスタムオプションでピボットフィールドをグループ化する**
`PivotFieldGroupOptions` クラスはカスタムグループ化の設定を提供します。日付フィールドの場合は `StartDate`、`EndDate`、`GroupTypes` を設定します。数値フィールドの場合は `StartNumber`、`EndNumber`、`Interval` を設定します。`NewPivotField` プロパティは、グループ化によって元のフィールドに加えて新しいピボットフィールドを作成するかどうかを制御します (この記事の最後の「注釈」セクションを参照してください)。

### **日付フィールドを月と四半期でグループ化する**
次の例では、サンプルピボットテーブルの日付行フィールドを開始日と終了日の間で月と四半期別にグループ化しています。コードは [サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx) を読み込み、グループ化を実行し、ピボットテーブルのデータを計算して、グループ化された結果を保存します。スクリーンショットは効果を示しています。日付行フィールドは四半期と月でグループ化されています。
`options.GroupTypes` の値の順序は無視されることに注意してください。グループタイプの順序にかかわらず、グループ化されたフィールドは常に最大の期間から最小の期間の順に表示されます。年、四半期、月、日、時間、分、秒の順です。この例では `options.GroupTypes` で月が四半期より前にリストされていますが、四半期が外側のレベル、月が内側のレベルとして表示されます。

```csharp
using Aspose.Cells.Pivot;
// サンプルワークブックを読み込む
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセスする
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// 最初の行フィールド（日付フィールド）を月と四半期でグループ化する
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartDate = new DateTime(2008, 1, 1);
options.EndDate = new DateTime(2008, 9, 5);
options.GroupTypes = new PivotGroupByType[] { PivotGroupByType.Months, PivotGroupByType.Quarters };
pt.RowFields[0].Group(options);
// ピボットテーブルのデータを計算し、出力ファイルを保存する
pt.CalculateData();
wb.Save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![ピボットテーブルを月と四半期でグループ化した結果](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化する**
サンプルピボットテーブルの `FieldTwo` は最初はデータ(値)フィールドです。グループ化できるのは行または列フィールドのみであるため、コードは最初に `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` を呼び出して `FieldTwo` を行エリアに移動し、ピボットを更新してから、`StartNumber = 0`、`EndNumber = 5`、`Interval = 2` を使用して数値フィールドを 0-1、2-3、4-5 の範囲にグループ化します。

```csharp
using Aspose.Cells.Pivot;
// サンプルワークブックを読み込む
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 2番目のワークシートとそのピボットテーブルにアクセスする
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// FieldTwoはデータフィールドです: 最初にそれを行エリアに移動します、
// 行/列フィールドのみをグループ化できるためです
pt.AddFieldToArea(PivotFieldType.Row, "FieldTwo");
pt.CalculateData();
// 数値フィールドを0-1、2-3、4-5の範囲にグループ化する
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartNumber = 0;
options.EndNumber = 5;
options.Interval = 2;
pt.RowFields[1].Group(options);
// ピボットテーブルのデータを計算し、出力ファイルを保存する
pt.CalculateData();
wb.Save("outputNumberGroupPivotField.xlsx");
```

## **注釈**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` メソッドのオーバーロードは非推奨となり、API サーフェスから削除されました。代わりに `PivotField.Group()` および `PivotField.Group(PivotFieldGroupOptions)` を使用してください。
- Microsoft Excel では、数値フィールドをグループ化すると、元のピボットフィールドがグループ化された範囲に置き換えられますが、日付フィールドをグループ化すると、元のフィールドの隣に新しいピボットフィールド (グループレベルごとに 1 つ、四半期や月など) が作成されます。Aspose.Cells 26.10 以降、`PivotField.Group()` メソッドは Excel と同じ動作に従います。`PivotFieldGroupOptions.NewPivotField` プロパティは古いバージョンとの互換性のために存在します。数値のグループ化の場合は既定で false、日時のグループ化の場合は true になります。日付のグループ化で新しいピボットフィールドを作成する代わりに元のピボットフィールドを置き換える場合は、false に設定してください。
- `PivotFieldGroupOptions.Interval` プロパティは、数値のグループ化と、日単位での日付のグループ化 (たとえば、日付を 7 日周期にグループ化する) に対してのみ有効です。月、四半期、年で日付をグループ化する場合は無視されます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルに行と列のフィールドを追加する](/cells/ja/net/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリングする](/cells/ja/net/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加する](/cells/ja/net/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}