---
title: Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加する
linktitle: フィルターフィールドを追加
description: Aspose.Cells for Java を使用してピボットテーブルのフィルターフィールドを追加および構成する方法を学びます。フィルターフィールドの追加、単一選択フィルタリング、複数選択フィルタリングを含みます。
keywords: Aspose.Cells, Java, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /ja/java/add-filter-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はピボットテーブル内のフィルターフィールドのライフサイクル全体をサポートします。ハイレベルな便利 API または低レベルの `PageFields` コレクションを通じてフィルターフィールドを追加でき、フィルターを単一選択モードで駆動したり、すべてのページアイテムを表示するためにクリアしたり、フィールドを複数選択に切り替えて Excel のチェックボックス UI を通じて複数のページアイテムを一度に選択できるようにすることができます。
{{% /alert %}}

## **概要**

フィルターフィールドは、ソースデータの*どのサブセット*をピボット本体に表示するかを制御するピボットフィールドです。エンドユーザーは Excel でレンダリングされたピボットの上部にあるドロップダウンとしてそれを認識し、利用可能なページアイテムのいずれかを選択すると、そのページアイテムに属するレコードのみが集計されるようにピボット本体が再構築されます。ピボットフィールドは、`PivotFieldType.Row`、`PivotFieldType.Column`、または `PivotFieldType.Data` ではなく `PivotFieldType.Page` として登録されたときにフィルターフィールドになります。

フィルターフィールドは 2 つの動作で機能します。デフォルトの**単一選択**動作では、一度に 1 つのページアイテムのみが表示されるため、ピボット本体は正確に 1 つのサブセットを集計します。**複数選択**動作では、フィールドはチェックボックスリストを公開し、ピボット本体はチェックされたすべてのページアイテムの和集合を集計します。同じソースフィールドは、1 つのプロパティを切り替えることでこれらの動作間を前後に移動できます。

Aspose.Cells for Java は、フィルターフィールドを登録する 2 つの同等の方法を公開しています。ハイレベル API は `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` で、ソース列名を取り、1 回の呼び出しでフィールドを追加します。低レベル API は `PivotTable.PageFields.add(PivotField)` で、すでに `PivotField` 参照を保持しており、同じフィールドインスタンスをページエリアに追加したい場合に使用されます。どちらの API も最終的に同じ `PageFields` コレクションに格納され、この記事の残りでは、それらの間の選択方法と各フィルタリングモードの駆動方法について説明します。

## **フィルターフィールドの追加**

ピボットフィールドをページエリアに登録するには 2 つの方法があります。ハイレベル呼び出しはソース列名を文字列として受け取り、最も一般的なパスです。低レベル呼び出しは既存の `PivotField` インスタンスを受け取り、同じフィールドオブジェクトを複数のピボットエリア間で再利用する必要がある場合に便利です。どちらの呼び出しもフィールドを `PivotTable.PageFields` に配置し、その後、レンダリングされたピボットの上部にページドロップダウンとして表示されます。

### addFieldToArea を使用したフィルターフィールドの追加

次の例は、小さな Fruit / Year / Amount データセットを構築し、E3 セルにピボットテーブルを配置し、行エリアに `Fruit`、データエリアに `Amount`、ページエリアに `Year` を配置し、ピボットを更新してワークブックを保存します。

```java
import com.aspose.cells.*;

// 新しいワークブックを作成
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// ヘッダー行を設定
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 行のサンプルデータ（Fruit、Year、Amount）を入力
Object[][] data = new Object[][]
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

for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// セル E3 にアンカーされたピボットテーブルを追加
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドをそれぞれのエリアに追加：Fruit を行、Amount をデータ、Year をページフィールド
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// ピボットテーブルのデータを更新して計算
pivotTable.calculateData();

// ワークブックを保存
workbook.save("pageFieldSample.xlsx");
```

### PageFields.add を使用したフィルターフィールドの追加

すでに `PivotField` インスタンスを操作している場合は、それを `PivotTable.PageFields.add` に直接渡すことができます。ピボットテーブルとフィルターフィールドの構築は前のシナリオとまったく同じです。ページエリアへの登録の最終ステップのみが低レベル API 呼び出しに置き換えられます。

```java
import com.aspose.cells.*;

// - ピボットテーブルとページフィールドは、シナリオ1aとまったく同じ方法で構築されます
//   (Fruit/Year/Amountデータ、E3にピボット、Fruit->行、
//   Amount->データ)。以下では、Year PivotFieldをBaseFieldsコレクションから取得し、
//   PageFields.Addに渡します - これはAddFieldToAreaの低レベルの代替手段です。
//   結果は機能的にシナリオ1aと同一です。

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// ヘッダー
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// サンプルデータ（9行）
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// A1:C10をカバーするE3にピボットテーブルを追加
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> 行、Amount -> データ (Yearは下でページに移動)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 低レベルのアプローチ：既存のYear PivotFieldをBaseFieldsから取得し、
// PageFields.Add(PivotField)経由でページ領域に登録します。
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// 新しいページフィールドが保存されるワークブックに反映されるように更新します
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **単一選択フィルタリング（1 つのページアイテムの表示）**

デフォルトの単一選択動作では、フィルターフィールドは単一のドロップダウンとしてレンダリングされ、`PivotField.CurrentPageItem` 整数がどのページアイテムがピボット本体を駆動するかを選択します。特定のインデックスを割り当てるとその 1 つのアイテムが選択されます。特別なセンチネル値 `0x7FFD`（10 進数で 32765）を割り当てることでフィルターがクリアされ、すべてのページアイテムが一度に集計されます。単一選択はデフォルトであり、明示的に有効化する必要はありません。

### すべてのアイテムの表示**

`CurrentPageItem` をマジック値 `0x7FFD` に設定することは、フィルターをクリアすることと同等です。ピボット本体はフィルターが適用されていないかのようにすべてのページアイテムを集計します。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// Fruit/Year/Amount データを入力
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// E3 にピボットテーブルを作成
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);

// ピボットフィールドを設定: Fruit を行、Amount をデータ、Year をページ
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");

pivot.calculateData();

// ページフィールドの全項目が表示されるようページフィルターをクリア
// 0x7FFD (10進数 32765) は「全項目」を意味する特殊なセンチネル値です、
// Excel のページフィールドドロップダウンで「(すべて)」を選択するのと同等です。
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);

workbook.save("output.xlsx");
```

### 特定の 1 つのアイテムの表示**

`CurrentPageItem` を実際のインデックスに設定すると、その 1 つのページアイテムのみが選択されます。インデックスはフィルターフィールドのソート済みアイテムリスト内のアイテムの位置であるため、たとえば `1` はソート後に 2 番目のアイテムを選択します。

```java
import com.aspose.cells.*;

// ワークブックを作成
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// サンプルデータを追加 (フルーツ/年/金額)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// E3にピボットテーブルを追加
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// フィールドを追加: フルーツ→行、金額→データ、年→ページ
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// ページフィールド固有の操作
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = ソート順の2番目の項目 (例: "2021")

// ピボットテーブルを更新して計算
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **複数選択フィルタリング**

複数選択フィルタリングは、ページドロップダウンをチェックボックスリストに変え、エンドユーザーが複数のページアイテムを同時に選択できるようにします。Aspose.Cells は連携して機能する 2 つのプロパティを公開しています。`PivotField.IsMultipleItemSelectionAllowed` は、複数選択 UI が有効になる前に `true` に設定する必要があります。有効化された後、`PivotItem.IsHidden` がチェックボックスリストに表示されるアイテムを制御するため、すべてのアイテムを表示するか、特定のアイテムのみをホワイトリストに登録するかを選択できます。

以下のコードは、シナリオ 1a で構築された同じ Year フィルターフィールドで複数選択を有効化し、2 つのパターンを示しています。パート A は、すべてのエントリの `IsHidden` を `false` のままにしてすべてのページアイテムを表示し、パート B は、`switch (pivotItems[i].getStringValue())` ブロックを使用して選択したソース値のみをホワイトリスト化し、その他すべてを非表示にします。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// サンプルデータ: 果物 | 年 | 数量
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

String[][] data = new String[][]
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

for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}

Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// -- ページフィールドで複数選択を有効にする
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// パートA -- すべての項目を選択する（すべての項目を表示する）
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}

// パートB -- ソース値で特定の項目のみを選択する
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **注意:** `PivotItem.IsHidden` を通じて複数選択フィルタリングを使用する場合、**少なくとも 1 つの `PivotItem` を表示状態のままにする**必要があります（`IsHidden == false`）。すべてのアイテムが非表示になっていると、Excel はファイルを開く際にクラッシュするか、空のピボットをレンダリングします。複数選択のホワイトリストにソースデータから少なくとも 1 つのアイテムが含まれていることを必ず確認してください。

## **どの API とどのモードを使用すべきか？**

以下の表は、各シナリオを詳細に読まなくても適切な組み合わせを選択できるように、各 API とモードを使用するタイミングをまとめたものです。

| シナリオ / ユースケース | 推奨 API | 使用するプロパティ | メモ |
|---|---|---|---|
| ソース列名でフィルターフィールドを追加する（最も一般的） | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | ハイレベル、1 行で完結。`PivotField` 参照が必要な場合を除いてこれを使用してください。 |
| すでに `PivotField` オブジェクトを持っている場合にフィルターフィールドを追加する | `PivotTable.PageFields.add(PivotField)` | n/a | フィールドオブジェクトが他の場所で取得されたものであるか、再利用する必要がある場合に使用します。 |
| 単一のページアイテムにフィルターする（デフォルトモード） | `PivotField.CurrentPageItem` | 特定のインデックスに設定 | たとえば、`1` はソート済みリストの 2 番目のアイテムを表示します。 |
| すべてのアイテムを表示する / フィルターをクリアする | `PivotField.CurrentPageItem` | `0x7FFD` に設定 | マジック値 `0x7FFD`（10 進数で 32765）は「すべてのアイテム」のセンチネルです。 |
| Excel で複数選択 UI を有効化する | `PivotField.IsMultipleItemSelectionAllowed` | `true` に設定 | `IsHidden` 呼び出しが有効になる前に必要です。 |
| 複数選択リスト内の個別アイテムの表示 / 非表示を切り替える | `PivotItem.IsHidden` | アイテムごとに設定 | 少なくとも 1 つのアイテムを表示状態のままにする必要があります（`IsHidden == false`）。 |

{{% alert color="primary" %}}
複数選択フィルタリングを設定する際は、可視性の制約を常に覚えておいてください。複数選択フィルターフィールドのすべての `PivotItem` が非表示になっていると、Excel はファイルを開く際にクラッシュするか、空のピボットをレンダリングします。少なくとも 1 つのアイテムが表示されたままになるように、ソースデータに対してホワイトリストを構築してください。そうすれば、保存されたワークブックはすべてのマシンで確実に開きます。
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
