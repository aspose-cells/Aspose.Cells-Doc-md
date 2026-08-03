---
title: Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加する
linktitle: フィルターフィールドを追加
description: Aspose.Cells for .NET を使用してピボットテーブルにフィルターフィールドを追加および構成する方法を学びます。フィルターフィールドの追加、単一選択フィルタリング、複数選択フィルタリングを含みます。
keywords: Aspose.Cells, .NET, ピボットテーブル, フィルターフィールド, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, フィルタ
type: docs
weight: 250
url: /ja/net/add-page-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はピボットテーブル内のフィルターフィールドのライフサイクル全体をサポートします。高レベルの便利な API または低レベルの `PageFields` コレクションを介してフィルターフィールドを追加でき、単一選択モードでページフィルタを駆動したり、すべてのページアイテムを表示するためにクリアしたり、フィールドを複数選択に切り替えて Excel のチェックボックス UI を通じてユーザーが複数のページアイテムを一度に選択できるようにしたりできます。
{{% /alert %}}

## **はじめに**

フィルターフィールドとは、ソースデータの*どのサブセット*をピボット本体に表示するかを制御するピボットフィールドです。エンドユーザーには、Excel でレンダリングされたピボットの上部にあるドロップダウンとして表示され、利用可能なページアイテムのいずれかを選択すると、そのページアイテムに属するレコードのみが集計されるようにピボット本体が再構築されます。ピボットフィールドは、`PivotFieldType.Row`、`PivotFieldType.Column`、または `PivotFieldType.Data` ではなく `PivotFieldType.Page` として登録された場合にフィルターフィールドになります。

フィルターフィールドは 2 つの動作で動作できます。デフォルトの**単一選択**動作では、一度に 1 つのページアイテムのみが表示されるため、ピボット本体は正確に 1 つのサブセットを集計します。**複数選択**動作では、フィールドはチェックボックスのリストを公開し、ピボット本体はチェックされたすべてのページアイテムの和集合を集計します。同じソースフィールドを、単一のプロパティを切り替えることによって、これらの動作間で前後に移動できます。

Aspose.Cells for .NET は、フィルターフィールドを登録する 2 つの同等の方法を公開しています。高レベル API は `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` で、ソース列名を受け取り、単一の呼び出しでフィールドを追加します。低レベル API は `PivotTable.PageFields.Add(PivotField)` で、すでに `PivotField` 参照を保持していて、同じフィールドインスタンスをフィルター領域に追加したい場合に使用されます。どちらの API も最終的に同じ `PageFields` コレクションに格納され、この記事の残りの部分では、それらの間の選択方法と各フィルタリングモードの駆動方法を説明します。

## **フィルターフィールドの追加**

ピボットフィールドをフィルター領域に登録するには 2 つの方法があります。高レベルの呼び出しはソース列名を文字列として受け取り、最も一般的なパスです。低レベルの呼び出しは既存の `PivotField` インスタンスを受け入れ、同じフィールドオブジェクトを複数のピボット領域間で再利用する場合に便利です。どちらの呼び出しもフィールドを `PivotTable.PageFields` に配置し、その後、レンダリングされたピボットの上部にページドロップダウンとして表示されます。

### AddFieldToArea によるフィルターフィールドの追加

次の例では、小さな Fruit / Year / Amount データセットを構築し、セル E3 にピボットテーブルを配置し、行領域に `Fruit`、データ領域に `Amount`、フィルター領域に `Year` を配置し、ピボットを更新して、ワークブックを保存します。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 新しいワークブックを作成
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// ヘッダー行を設定
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// サンプルデータ9行を入力：果物、年、金額
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}

// セルE3を基準にピボットテーブルを追加
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// 各エリアにフィールドを追加：果物を行、金額をデータ、年をページフィールド
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// ピボットテーブルのデータを更新して計算
pivotTable.CalculateData();

// ワークブックを保存
workbook.Save("pageFieldSample.xlsx");
```

### PageFields.Add によるフィルターフィールドの追加

すでに `PivotField` インスタンスを操作している場合は、それを直接 `PivotTable.PageFields.Add` に渡すことができます。ピボットテーブルとフィルターフィールドは前のシナリオとまったく同じ方法で構築されます。最終的なフィルター領域の登録のみが低レベル API 呼び出しに置き換えられます。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — ピボットテーブルとページフィールドは、シナリオ 1a とまったく同じように構築されます
//   (Fruit/Year/Amount データ、ピボットは E3、Fruit→Row、
//   Amount→Data)。以下では、Year PivotField を
//   BaseFields コレクションから取得し、PageFields.Add に渡します。これは
//   AddFieldToArea に代わる低レベルの方法です。結果は
//   機能的にはシナリオ 1a と同じです。

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// ヘッダー
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// サンプルデータ (9 行)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// E3 に A1:C10 をカバーするピボットテーブルを追加
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Fruit -> Row、Amount -> Data (Year は下記で Page に追加)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 低レベルのアプローチ: 既存の Year PivotField を BaseFields から取得し、
// PageFields.Add(PivotField) 経由で Page 領域に登録します。
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// 新しいページフィールドが保存されるワークブックに反映されるように更新
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **単一選択フィルタリング（1 つのページアイテムの表示）**

デフォルトの単一選択動作では、フィルターフィールドは単一のドロップダウンとしてレンダリングされ、`PivotField.CurrentPageItem` 整数がどのページアイテムがピボット本体を駆動するかを選択します。特定のインデックスを割り当てるとそのアイテムが選択され、特別なセンチネル値 `0x7FFD`（10 進数で 32765）を割り当てるとフィルタがクリアされ、すべてのページアイテムが一度に集計されます。単一選択がデフォルトであり、明示的に有効にする必要はありません。

### すべてのアイテムの表示

`CurrentPageItem` をマジック値 `0x7FFD` に設定することは、ページフィルタをクリアすることと同等です。つまり、ピボット本体はフィルタが適用されていないかのようにすべてのページアイテムを集計します。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // 新しいワークブックを作成
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // Fruit/Year/Amount のデータを入力
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");

        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };

        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }

        // E3 にピボットテーブルを作成
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // ピボットフィールドを設定: Fruit→行、Amount→データ、Year→ページ
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.CalculateData();

        // ページフィールドのすべてのアイテムが表示されるようにページフィルターをクリア
        // 0x7FFD (10進数 32765) は「すべてのアイテム」を意味する特別なセンチネル値です —
        // Excel のページフィールドドロップダウンで「(すべて)」を選択するのと同等です。
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}
```

### 特定の 1 つのアイテムの表示

`CurrentPageItem` を実際のインデックスに設定すると、そのページアイテムのみが選択されます。インデックスはフィルターフィールドのソート済みアイテムリスト内のアイテムの位置であるため、たとえば `1` を指定すると、ソート後に 2 番目のアイテムが選択されます。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// ワークブックを作成
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// サンプルデータを追加 (果物/年/金額)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");

cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");

cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");

cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");

cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");

// E3にピボットテーブルを追加
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// フィールドを追加: Fruit→行, Amount→データ, Year→ページ
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// ページフィールド固有の操作
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = ソート順の2番目の項目 (例: "2021")

// ピボットテーブルを更新して計算
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **複数選択フィルタリング**

複数選択フィルタリングは、ページドロップダウンをチェックボックスのリストに変換し、エンドユーザーが複数のページアイテムを同時に選択できるようにします。Aspose.Cells は連携する 2 つのプロパティを公開しています。`PivotField.IsMultipleItemSelectionAllowed` は、複数選択 UI が有効になる前に `true` に設定する必要があります。有効にした後、`PivotItem.IsHidden` がチェックボックスリストに表示されるアイテムを制御するため、すべてのアイテムを表示するか、特定のアイテムのみをホワイトリストに登録するかを選択できます。

以下のコードは、シナリオ 1a で構築された同じ Year フィルターフィールドで複数選択を有効にし、2 つのパターンを示しています。パート A は、すべてのエントリの `IsHidden` を `false` のままにしておくことで、すべてのページアイテムを表示します。一方、パート B は、選択したソース値のみをホワイトリストに登録し、`switch (pivotItems[i].GetStringValue())` ブロックを通じて他のすべてを非表示にします。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — ピボットテーブルとページフィールドは、シナリオ 1a とまったく同じ方法で構築されます
//   (Fruit/Year/Amount データ、ピボット位置は E3、Fruit→行、
//   Amount→データ、Year→ページ (AddFieldToArea 経由))
//   以下では、ページフィールドに対して複数選択フィルタを適用します。

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// サンプルデータ: Fruit | Year | Amount
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");

string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}

Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — ページフィールドで複数選択を有効にする
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// パート A — すべての項目を選択する (すべての項目を表示状態にする)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}

// パート B — ソース値で特定の項目のみを選択する
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}

pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

> **注意:** `PivotItem.IsHidden` を使用して複数選択フィルタリングを使用する場合、**少なくとも 1 つの `PivotItem` は表示されたままにする必要があります**（`IsHidden == false`）。すべてのアイテムが非表示になっている場合、Excel はファイルを開くときにクラッシュするか、空のピボットをレンダリングします。複数選択のホワイトリストにソースデータから少なくとも 1 つのアイテムが含まれていることを必ず確認してください。

## **どの API とどのモードを使用すべきですか？**

次の表は、各シナリオで API とモードをいつ使用するかをまとめたもので、すべてのシナリオを詳細に読まなくても適切な組み合わせを選択できるようにします。

| シナリオ / ユースケース | 推奨 API | 使用するプロパティ | メモ |
|---|---|---|---|
| ソース列名でフィルターフィールドを追加する（最も一般的） | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | なし | 高レベル、ワンライン。`PivotField` 参照が必要ない場合はこれを使用してください。 |
| すでに `PivotField` オブジェクトがある場合にフィルターフィールドを追加する | `PivotTable.PageFields.Add(PivotField)` | なし | フィールドオブジェクトが他の場所で取得された場合、または再利用する必要がある場合に使用します。 |
| 単一のページアイテムにフィルタリングする（デフォルトモード） | `PivotField.CurrentPageItem` | 特定のインデックスに設定 | たとえば、`1` はソート済みリストの 2 番目のアイテムを表示します。 |
| すべてのアイテムを表示する / ページフィルタをクリアする | `PivotField.CurrentPageItem` | `0x7FFD` に設定 | マジック値 `0x7FFD`（10 進数で 32765）は「すべてのアイテム」のセンチネルです。 |
| Excel で複数選択 UI を有効にする | `PivotField.IsMultipleItemSelectionAllowed` | `true` に設定 | `IsHidden` 呼び出しが有効になる前に必要です。 |
| 複数選択リスト内の個々のアイテムを表示 / 非表示にする | `PivotItem.IsHidden` | アイテムごとに設定 | 少なくとも 1 つのアイテムは表示されたままにする必要があります（`IsHidden == false`）。 |

{{% alert color="primary" %}}
複数選択フィルタリングを構成するときは、常に可視性の制約を忘れないでください。複数選択フィルターフィールド内のすべての `PivotItem` が非表示になっている場合、Excel は開く際にクラッシュするか、空のピボットをレンダリングします。ソースデータに基づいてホワイトリストを構築し、少なくとも 1 つのアイテムが表示されたままになるようにして、保存されたワークブックがすべてのマシンで確実に開かれるようにしてください。
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
