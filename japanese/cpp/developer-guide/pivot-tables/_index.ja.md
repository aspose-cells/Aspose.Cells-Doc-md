---
title: ピボットテーブルの作成
linktitle: ピボットテーブルの作成
description: Aspose.Cells for C++ を使用してピボットテーブルを作成し、書式を設定します。
keywords: ピボットテーブルの作成, ピボットテーブルの挿入, ピボットテーブルの書式設定.
type: docs
weight: 160
url: /ja/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルとは？**
ピボットテーブルは、インタラクティブなサマリーレポートです。行ごとに記録された大量のデータを使用せずに、コンパクトなマトリクスに集約できます。どの列を行ラベルとするか、どの列を列ラベルとするか、どの列を集約して値とするかを指定できます。グループ化と計算はピボットテーブルが行います。
- **要約** — 長い数式チェーンではなく、製品別、地域別、または四半期ごとの売上合計を表示します。
- **比較** — 行にカテゴリ、列に期間を置くことで、一覧形式のデータが傾向を一目で確認できるクロスレポートになります。
- **詳細表示** — 任意の集計値をダブルクリックすると、その背後にある元の行を確認できます。
- **更新** — 元データが変更された場合、1回の更新でレポート全体を再計算できます。
代表的な利用場面は、販売ダッシュボード、経費の内訳、在庫分析などです。「これらの数値はカテゴリと時間によってどのように内訳されるか？」のような質問に利用できます。Aspose.Cells for C++ では、ワークシートの [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) メソッドを使用してピボットテーブルを作成します。ピボットテーブルの作成後は、[PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) クラスを使用して操作できます。

## **ピボットテーブルの作成**
次のサンプルコードは、ピボットテーブルを作成して操作する方法を示しています。このコードで生成された[出力 Excel ファイル](23167010.xlsx)と、生成された Excel ファイルを Microsoft Excel で表示したスクリーンショットを確認してください。
![ピボットテーブルの作成例](create-pivot-table_1.png)

## **サンプルコード**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // 新しいワークブックを作成し、最初のワークシートを取得する
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // ソースデータ（スポーツと四半期ごとの売上）を書き込む
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // A1:C8をソースとして、宛先セルE3にピボットテーブルを追加する
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // ピボットフィールドを割り当てる：Sportを行、Quarterを列、Salesをデータに配置する
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // ワークブックを保存する
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}