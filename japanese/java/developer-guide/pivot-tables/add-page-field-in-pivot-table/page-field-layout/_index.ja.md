---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for Java を使用して、ピボットテーブルのページフィールド領域のレイアウトを制御する方法を学びます。ピボットテーブルの上部にあるページフィールドの表示順序、折り返し数、フィールド順序の設定を含みます。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
この記事は、**ピボットテーブルにページフィールドを追加** するトピックの続きです。ピボットテーブルの上部にあるフィルターコントロールの帯であるページフィールド領域のレイアウトを、表示順序、折り返し数、フィールドの並べ替えを含めて制御する方法を説明します。
{{% /alert %}}

## **Introduction**
Microsoft Excel のピボットテーブルには、テーブルの行/列/データの本体の上に位置する専用の **ページフィールド領域** があります。この領域はドロップダウンフィルターコントロールの帯（ページフィールドごとに 1 つ）としてレンダリングされ、エンドユーザーが年や地域などの基準でピボットをスライスするためにクリックする部分です。Aspose.Cells はこの領域を `pivotTable.getPageFields()` コレクションを通じてモデル化し、帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。
- `pivotTable.getPageFieldOrder()` （`Aspose.Cells.PrintOrderType` 値）は、追加のページフィールドを既存のフィールドの *横* に配置するか *下* に配置するかを決定します。
- `pivotTable.getPageFieldWrapCount()` は、折り返す前に行または列ごとに配置されるページフィールドの数を設定します。
- `pivotTable.getPageFields().move(currIndex, destIndex)` は、順序モードを変更せずにページフィールドを並べ替えます。
この記事では、共有データセットに対してこれらの各操作を示す 3 つのコード例を通して、結果を並べて比較できるようにします。

## **Source Data**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
8 行すべてがすべてのコード例で同じ順序で入力されているため、ソースデータはシナリオ間で異なることはなく、ページフィールドのレイアウトプロパティのみが異なります。

## **Example 1: Over Then Down**
最初のシナリオでは、2 つのページフィールド (`Year`、`Region`) をピボットテーブルの上部で **1 行に横並びに** 表示するように構成します。`Fruit` を行軸に割り当て、`Year` を最初に、`Region` を 2 番目にページ軸に配置し（`addFieldToArea` 呼び出しの順序が開始インデックスを決定します）、データフィールドとして `Amount` (Sum) を追加します。その後、`pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` と `pivotTable.setPageFieldWrapCount(2)` を設定します。`OVER_THEN_DOWN` と折り返し数 2 を使用すると、2 つのページフィールドはピボットテーブルの上部で水平に 1 行に並んで配置されるため、帯は幅 2 の 1 行を占めます。

```java
import com.aspose.cells.*;
import java.io.File;
String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();
Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();
Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();
// ヘッダー（行0）
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// 行1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// 行2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// 行3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// 行4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// 行5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// 行6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// 行7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// 行8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// PivotTableReportシートを追加
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();
// PivotData!A1:D9をソースとし、PivotTableReportのA1に配置するピボットテーブルを作成
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// フィールドを追加
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // 果物
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // 年
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // 地域
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // 金額
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);
// ページフィールド領域のレイアウトを設定：ページフィールドを最初に横方向に配置し、2つごとに折り返す
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
// 更新して計算
pivotTable.calculateData();
// 保存
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```

## **Example 2: Down Then Over**
この例では、Example 1 とまったく同じように、`Fruit` を行軸に、`Year` と `Region` をページ軸に（最初に `Year`）、`Amount` (Sum) をデータフィールドとして配置します。次に、`pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` と `pivotTable.setPageFieldWrapCount(2)` を設定します。`DOWN_THEN_OVER` と折り返し数 2 を使用すると、2 つのページフィールドは垂直に積み重ねられ、`Year` が上、`Region` がその直下に配置され、ピボットテーブルの上部に 1 つの列を形成します。したがって、帯は Example 1 とは対照的に、幅 1 の 2 行を占めます。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
int pivotReportIdx = workbook.getWorksheets().add();
Worksheet pivotReport = workbook.getWorksheets().get(pivotReportIdx);
pivotReport.setName("PivotTableReport");
String[] headers = new String[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}
Object[][] data = new Object[][]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
int idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
PivotTable pivotTable = pivotReport.getPivotTables().get(idx);
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Example 3: Move a Page Field**
3 番目のシナリオでは、このデータセットとフィールド割り当てを維持し、中立的なレイアウト（折り返し数 `2` の `OVER_THEN_DOWN`）を設定してから、`pageFields.move` 操作を示します。`move(0, 1)` 呼び出しは、インデックス 0 (`Year`) のページフィールドを位置 1 に移動し、位置 1 (`Region`) にあったページフィールドを位置 0 にシフトします。この呼び出しの後、`Region` が最初のページフィールドになり、`Year` が 2 番目になります。折り返しと順序モードは変更されていないため、帯は引き続き水平に並んでレンダリングされ、2 つのドロップダウンの順序のみが入れ替わります。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");
dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);
dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);
dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);
dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);
dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);
dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);
dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);
dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);
Worksheet pivotSheet = workbook.getWorksheets().add("PivotTableReport");
int pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.getPivotTables().get(pivotIdx);
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **Related Articles**
- [ピボットテーブルにページフィールドを追加](/cells/ja/java/add-page-field-in-pivot-table/) — ピボットテーブルにページフィールドを追加する方法を紹介する親ページです。
- [ピボットテーブルの行と列のフィールド](/cells/ja/java/row-and-column-fields/) — ここで示したページ軸の作業を補完する、行軸と列軸へのフィールドの割り当てについて説明します。
- [ピボットテーブルの値フィールドを管理](/cells/ja/java/manage-value-fields/) — この記事で使用されている `Sum` 集計を含む、データ（値）領域の構成方法について説明します。
- [ピボットテーブルを更新](/cells/ja/java/refresh-pivot-table/) — ページフィールドの並べ替え後に必要となる `refreshData()` と `calculateData()` について説明します。
- [ピボットテーブルにスタイルを適用](/cells/ja/java/apply-style-to-pivot-table/) — ページフィールドの帯がレイアウトされた後、レンダリングされたピボットテーブルの書式を設定する方法を示します。

{{< app/cells/assistant language="java" >}}