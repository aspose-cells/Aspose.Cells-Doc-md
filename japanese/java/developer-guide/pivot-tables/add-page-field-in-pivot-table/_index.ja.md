---
title: Aspose.Cells for Java でピボットテーブルにフィルターフィールドを追加
linktitle: Aspose.Cells for Java でピボットテーブルにフィルターフィールドを追加
description: Aspose.Cells for Java を使用してピボットテーブルにフィルターフィールドを追加して構成する方法について、フィルターフィールドの追加、単一選択フィルター、複数選択フィルターを説明します。
keywords: Aspose.Cells, Java, ピボットテーブル, フィルターフィールド, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, フィルター
type: docs
weight: 250
url: /ja/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルのフィルターフィールドのライフサイクル全体を完全にサポートしています。ハイレベルの便利な API または低レベルの `PageFields` コレクションを使用してフィルターフィールドを追加できます。また、フィルターを単一選択モードで操作したり、すべてのフィルター項目を表示するようにフィルターをクリアしたり、フィールドを複数選択に切り替えて、Excel のチェックボックス UI を通じてユーザーが複数のフィルター項目を一度に選択できるようにしたりできます。
{{% /alert %}}

## **概要**
フィルターフィールドとは、ピボットテーブルの本体に表示されるソースデータの*どの部分集合*を制御するピボットフィールドです。Excel でレンダリングされたピボットテーブルでは、上部にドロップダウンとして表示されます。利用可能なフィルター項目を 1 つ選択すると、そのフィルター項目に属するレコードのみが集計されるようにピボットテーブルの本体が再構築されます。ピボットフィールドは、`PivotFieldType.Row`、`PivotFieldType.Column`、または `PivotFieldType.Data` として登録されるのではなく、`PivotFieldType.Page` として登録されたときにフィルターフィールドになります。

## **フィルターフィールドの追加**

### addFieldToArea によるフィルターフィールドの追加
次の例では、小さな Fruit / Year / Amount データセットを作成し、`Fruit` を行領域、`Amount` をデータ領域、`Year` をフィルター領域に配置して、E3 セルにピボットテーブルを作成します。その後、ピボットテーブルを更新し、ワークブックを保存します。

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
// 9行のサンプルデータを作成: Fruit、Year、Amount
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
// E3セルを基準位置としてピボットテーブルを追加
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// フィールドを各エリアに追加: Fruitは行、Amountはデータ、Yearはページフィールド
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// ピボットテーブルデータを更新して計算
pivotTable.calculateData();
// ワークブックを保存
workbook.save("pageFieldSample.xlsx");
```

### PageFields.add によるフィルターフィールドの追加
すでに `PivotField` インスタンスを取り扱っている場合は、`PivotTable.PageFields.add` に直接渡すことができます。ピボットテーブルとフィルターフィールドの構築方法は前の例と同じです。最後のフィルター領域への登録だけが、低レベルの API 呼び出しに置き換わります。

```java
import com.aspose.cells.*;
// - ピボットテーブルとページフィールドは、シナリオ 1a とまったく同じ方法で構築されます
//   （Fruit/Year/Amount データ、ピボット位置は E3、Fruit->Row、
//   Amount->Data）。以下では、BaseFields コレクションから Year PivotField を取得し、
//   PageFields.Add に渡します。これは AddFieldToArea の低レベルな代替手段です。
//   結果は機能的にシナリオ 1a と同じになります。
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// ヘッダー
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// サンプルデータ（9 行）
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// A1:C10 を対象として E3 にピボットテーブルを追加
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Fruit -> Row、Amount -> Data（Year は後で Page に追加されます）
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// 低レベルな方法: BaseFields から既存の Year PivotField を取得し
// PageFields.Add(PivotField) を使用して Page 領域に登録します。
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// 保存されたワークブックに新しいページフィールドが反映されるよう更新します
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **単一選択フィルター（フィルター項目を 1 つ表示）**
デフォルトの単一選択動作では、フィルターフィールドは単一のドロップダウンとして表示され、`PivotField.CurrentPageItem` の整数値によって、ピボットテーブルの本体を構成するフィルター項目を指定します。特定のインデックスを設定すると、その項目が 1 つだけ選択されます。特殊なセンチネル値 `0x7FFD`（10 進数 32765）を設定すると、フィルターがクリアされ、すべてのフィルター項目が同時に集計されます。単一選択はデフォルトの動作であるため、明示的に有効にする必要はありません。

### すべての項目を表示する
`CurrentPageItem` に特殊なセンチネル値 `0x7FFD` を設定することは、フィルターをクリアすることと同値です。ピボットテーブルの本体には、フィルターが適用されていない場合と同様に、すべてのフィルター項目が集計されます。

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
// ピボットフィールドを設定: Fruit を Row、Amount を Data、Year を Page に配置
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// ページフィールドのすべての項目が表示されるようにページフィルターをクリアします。
// 0x7FFD（10 進数 32765）は「すべての項目」を表す特殊なセンチネル値であり、
// Excel のページフィールドのドロップダウンで「(All)」を選択することに相当します。
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### 特定の項目を 1 つ表示する
`CurrentPageItem` に実際の項目インデックスを設定すると、そのフィルター項目が 1 つだけ選択されます。このインデックスは、フィルター項目を並べ替えたリスト内での項目の位置です。したがって、例えば `1` は、並べ替え後の 2 番目の項目を選択します。

```java
import com.aspose.cells.*;
// ワークブックを作成
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// サンプルデータを追加（Fruit/Year/Amount）
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
// フィールドを追加：Fruit→Row、Amount→Data、Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// ページフィールド固有の操作
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = ソート順で2番目の項目（例: "2021"）
// ピボットテーブルを更新して計算
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **複数選択フィルター**
複数選択フィルターでは、フィルターのドロップダウンがチェックボックス一覧に変わり、エンドユーザーが複数のフィルター項目を同時に選択できます。Aspose.Cells には、連携して機能する 2 つのプロパティがあります。複数選択 UI を有効にするには、まず `PivotField.IsMultipleItemSelectionAllowed` を `true` に設定する必要があります。有効化後、`PivotItem.IsHidden` によって、チェックボックス一覧に表示する項目を制御できます。これにより、すべての項目を表示したり、特定の項目だけをホワイトリストに含めたりできます。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// サンプルデータ: Fruit | Year | Amount
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
// パート A -- すべての項目を選択（すべての項目を表示）
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// パート B -- ソース値に基づいて特定の項目のみを選択
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

> **注:** `PivotItem.IsHidden` を使用して複数選択フィルターを構成する場合、**少なくとも 1 つの `PivotItem` を表示状態のままにする必要があります** (`IsHidden == false`)。すべての項目を非表示にすると、Excel はファイルを開いたときにクラッシュするか、空のピボットテーブルを表示します。複数選択時のホワイトリストには、必ずソースデータの項目が少なくとも 1 つ含まれることを確認してください。

## **使用すべき API とモード**
以下の表は、各 API とモードをどのような場合に使用するかまとめたものです。詳細をすべて読まずに、最適な組み合わせを選択できます。
| シナリオ / ユースケース | 推奨 API | 使用するプロパティ | 注記 |
|---|---|---|---|
| ソース列名を指定してフィルターフィールドを追加する（最も一般的） | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | 該当なし | ハイレベルの API であり、1 行で追加できます。`PivotField` 参照が必要な場合を除き、これを使用します。 |
| すでに `PivotField` オブジェクトがある場合はフィルターフィールドを追加する | `PivotTable.PageFields.add(PivotField)` | 該当なし | フィールドオブジェクトを他の場所で取得した場合、またはそのオブジェクトを再利用する必要がある場合に使用します。 |
| 1 つのフィルター項目に絞り込む（デフォルトモード） | `PivotField.CurrentPageItem` | 特定のインデックスに設定 | 例えば、`1` は並べ替え後のリスト内の 2 番目の項目を表示します。 |
| すべての項目を表示する / フィルターをクリアする | `PivotField.CurrentPageItem` | `0x7FFD` に設定 | 特殊な値 `0x7FFD`（10 進数 32765）は「すべての項目」を表すセンチネル値です。 |
| Excel で複数選択 UI を有効にする | `PivotField.IsMultipleItemSelectionAllowed` | `true` に設定 | 複数選択を有効にする前に設定する必要があります。 |
| 複数選択一覧で個々の項目を非表示 / 表示する | `PivotItem.IsHidden` | 項目ごとに設定 | 少なくとも 1 つの項目を表示状態にする必要があります (`IsHidden == false`)。 |

{{% alert color="primary" %}}
複数選択フィルターを構成するときは、可視性の制約を常に考慮してください。複数選択のフィルターフィールドですべての `PivotItem` を非表示にすると、Excel でファイルを開いたときにクラッシュするか、空のピボットテーブルが表示されます。ソースデータに基づいてホワイトリストを作成し、少なくとも 1 つの項目を表示状態のままにしてください。これにより、保存したワークブックをすべての環境で確実に開けるようになります。
{{% /alert %}}

{{< app/cells/assistant language="java" >}}