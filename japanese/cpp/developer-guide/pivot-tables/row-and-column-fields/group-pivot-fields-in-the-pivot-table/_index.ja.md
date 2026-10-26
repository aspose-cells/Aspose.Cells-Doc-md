---
title: ピボットテーブルでピボットフィールドをグループ化する
linktitle: ピボットテーブルでピボットフィールドをグループ化する
description: Aspose.Cells for C++ の PivotField.Group および PivotFieldGroupOptions を使用して、ピボットテーブルの行および列のピボットフィールドを月や四半期などの日付期間、および数値範囲にグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, ピボットフィールドのグループ化, PivotField.Group, PivotFieldGroupOptions, 日付グループ化, 数値グループ化, 月, 四半期, 数値範囲, C++
type: docs
weight: 80
url: /ja/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **想定される使用シナリオ**
- ピボットフィールドのグループ化は、ピボットテーブルの行フィールドや列フィールドに多数の異なる項目(数百の日付を含む日付フィールドや、多くの散在した値を持つ数値フィールドなど)が含まれている場合に役立ちます。グループ化により、これらの項目を意味のあるセクションにまとめます。日付は月、四半期、年へ、数値は 0-1、2-3、4-5 などの範囲へまとめられます。これにより、大規模なピボットテーブルがコンパクトになり、分析しやすくなります。Aspose.Cells はこの機能を `PivotField.Group()` メソッド(データ型による自動グループ化)と `PivotField.Group(PivotFieldGroupOptions)`(カスタムグループ化オプション)を通じて実現しています。
- 日付グループ化は個々の日付を日、月、四半期、年といったより大きな期間にまとめ、時間の階層(例えば年、四半期、月)を構築します。経時的な傾向が一目でわかるようになり、各期間レベルがピボットテーブルの行エリアまたは列エリアに独自のピボットフィールドとして表示されます。
- グループ化はピボットテーブルの ROW または COLUMN エリアに配置されたフィールドに対してのみ使用できます。データ(値)フィールドを直接グループ化することはできません。そのようなフィールドをグループ化するには、まずピボットテーブルの行エリアまたは列エリアに追加する必要があります。

## **ピボットフィールドを自動的にグループ化する**
パラメーターなしの `PivotField.Group()` オーバーロードは、フィールドのデータ型を検査して自動的にグループ化します。日付(および空白)のみを含むフィールドは月でグループ化されます。数値(および空白)のみを含むフィールドは、自動間隔を使用して数値範囲にグループ化されます。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **カスタムオプションでピボットフィールドをグループ化する**
`PivotFieldGroupOptions` クラスはカスタムグループ化設定を提供します。日付フィールドの場合は `StartDate`、`EndDate`、`GroupTypes` を設定します。数値フィールドの場合は `StartNumber`、`EndNumber`、`Interval` を設定します。`NewPivotField` プロパティは、グループ化によって元のフィールドに加えて新しいピボットフィールドを作成するかどうかを制御します(この記事の最後の注記セクションを参照してください)。

### **日付フィールドを月と四半期でグループ化する**
次の例では、サンプルピボットテーブルの日付行フィールドを開始日と終了日の間で月と四半期にグループ化しています。コードは [サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx)を読み込み、グループ化を実行し、ピボットテーブルのデータを計算して、グループ化された結果を保存します。スクリーンショットはその効果を示しています。日付行フィールドが四半期と月でグループ化されています。
`options.GroupTypes` の値の順序は無視されることに注意してください。グループタイプがどの順序で並んでいても、グループ化されたフィールドは常に最も大きな期間から最も小さな期間へと表示されます。年、四半期、月、日、時間、分、秒の順です。この例では `options.GroupTypes` で月が四半期より前にリストされていますが、外側のレベルには四半期が、内側のレベルには月が表示されます。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // サンプルワークブックを読み込む
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // 2番目のワークシートとそのピボットテーブルにアクセスする
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // 最初の行フィールド（日付フィールド）を月と四半期でグループ化する
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // グループタイプを設定：月と四半期
    Vector<PivotGroupByType> groupTypes{ PivotGroupByType::Months, PivotGroupByType::Quarters };
    options.SetGroupTypes(groupTypes);
    // 最初の行フィールドにグループ化を適用する
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // ピボットテーブルのデータを計算し、出力ファイルを保存する
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![月と四半期でグループ化されたピボットテーブル](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化する**
サンプルピボットテーブルの `FieldTwo` は最初はデータ(値)フィールドです。行または列フィールドのみがグループ化できるため、コードはまず `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` を呼び出して `FieldTwo` を行エリアに移動し、ピボットを更新してから、`StartNumber = 0`、`EndNumber = 5`、`Interval = 2` を使用して数値フィールドを 0-1、2-3、4-5 の範囲にグループ化します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **注記**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` メソッドのオーバーロードは非推奨となり、API サーフェスから削除されました。`PivotField.Group()` および `PivotField.Group(PivotFieldGroupOptions)` が代替となります。
- Microsoft Excel では、数値フィールドをグループ化すると元のピボットフィールドがグループ化された範囲に置き換えられますが、日付フィールドをグループ化すると、元のフィールドの隣に新しいピボットフィールド(グループレベルごとに 1 つ、例えば四半期と月)が作成されます。Aspose.Cells 26.10 以降、`PivotField.Group()` メソッドは Excel と同じ動作に従います。`PivotFieldGroupOptions.NewPivotField` プロパティは古いバージョンとの互換性のために存在します。デフォルトでは、数値グループ化の場合は false、日時グループ化の場合は true になります。日付グループ化で新しいピボットフィールドを作成する代わりに元のピボットフィールドを置き換えたい場合は、false に設定してください。
- `PivotFieldGroupOptions.Interval` プロパティは、数値グループ化および日付を日でグループ化する場合(例えば、日付を 7 日単位の期間にグループ化する場合)にのみ有効です。日付を月、四半期、年でグループ化する場合には無視されます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルに行と列フィールドを追加する](/cells/ja/cpp/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリングする](/cells/ja/cpp/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにページフィールドを追加する](/cells/ja/cpp/add-page-field-in-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/cpp/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}