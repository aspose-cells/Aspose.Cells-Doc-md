---
title: ピボットテーブルのページフィールドレイアウトを変更する
linktitle: ピボットテーブルのページフィールドレイアウトを変更する
description: Aspose.Cells for JavaScript via C++ を使用して、ピボットテーブルのページフィールド領域のレイアウトを制御する方法を学びます。これには、ピボットテーブルの上部にあるページフィールドの表示順序、折り返し数、並び順の設定が含まれます。
keywords: Aspose.Cells for JavaScript via C++, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
本記事は、**ピボットテーブルにページフィールドを追加する**の続きです。ピボットテーブルの上部に配置されたフィルターコントロールのストリップ（ページフィールド領域）のレイアウトを制御する方法を示します。これには、表示順序、折り返し数、フィールドの並べ替えが含まれます。
{{% /alert %}}

## **概要**
Microsoft Excel のピボットテーブルには、表の行・列・データ領域より上にある専用の**ページフィールド領域**があります。この領域は、ページフィールドごとに 1 つ配置されるドロップダウンフィルターのストリップとして描画されます。エンドユーザーはここをクリックして、年や地域などの条件でピボットテーブルを絞り込みます。Aspose.Cells は、この領域を `pivotTable.pageFields` コレクションとして表現し、ストリップの表示レイアウトを制御する 3 つのプロパティを公開します。
- `pivotTable.pageFieldOrder`（`Aspose.Cells.PrintOrderType` の値）によって、追加のページフィールドを既存のフィールドの*横*または*下*のどちらに配置するかが決まります。
- `pivotTable.pageFieldWrapCount` は、折り返しが発生する前に 1 行または 1 列に配置するページフィールド数を設定します。
- `pivotTable.pageFields.move(currIndex, destIndex)` は、順序モードを変更せずにページフィールドを並べ替えます。
本記事では、同一データセットを使用して各操作を示す 3 つのコード例について説明します。各例の結果として得られるレイアウトを並べて比較できます。

## **ソースデータ**
| Fruit | Year | Region | Amount |
|--------|------|--------|--------|
| Apple | 2022 | North | 150 |
| Apple | 2023 | North | 180 |
| Banana | 2022 | South | 120 |
| Banana | 2023 | South | 140 |
| Cherry | 2022 | East | 200 |
| Cherry | 2023 | East | 220 |
| Grape | 2022 | West | 90 |
| Grape | 2023 | West | 110 |
各コード例では、8 行すべてのデータも同じ順序で入力されています。そのため、シナリオごとにソースデータが変化することはなく、変わるのはページフィールドのレイアウトプロパティのみです。

## **例 1: 横方向優先**
最初のシナリオでは、2 つのページフィールド（`Year`、`Region`）をピボットテーブルの上部に**1 行で横並び**になるように構成します。`Fruit` を行領域に配置し、ページフィールド領域には `Year` を先頭、`Region` を次に配置します（`addFieldToArea` 呼び出しの順序によって初期インデックスが決まります）。次に、`Amount` を Sum 集計の値フィールドとして追加します。その後、`pivotTable.pageFieldOrder` を `PrintOrderType.OverThenDown` に設定し、`pivotTable.pageFieldWrapCount = 2` とします。
`OverThenDown` で折り返し数を 2 にすると、2 つのページフィールドはピボットテーブルの上部に 1 行で横並びになります。ストリップは 2 フィールド幅の 1 行を占めます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // ヘッダー（行0）
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // 行1: りんご、2022、北部、150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // 行2: りんご、2023、北部、180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // 行3: バナナ、2022、南部、120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // 行4: バナナ、2023、南部、140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // 行5: さくらんぼ、2022、東部、200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // 行6: さくらんぼ、2023、東部、220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // 行7: ぶどう、2022、西部、90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // 行8: ぶどう、2023、西部、110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // PivotTableReportシートを追加
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // PivotData!A1:D9をデータ元として、PivotTableReportのA1にピボットテーブルを作成
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // フィールドを追加
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // 果物
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // 年
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // 地域
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // 金額
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // ページフィールド領域のレイアウトを設定：ページフィールドを横方向優先で配置し、2つごとに改行
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // 更新して計算
            pivotTable.calculateData();
            // 保存
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **例 2: 縦方向優先**
この例では、例 1 と同様に、`Fruit` を行領域に、`Year` と `Region` をページフィールド領域に（`Year` が先）、`Amount` を Sum 集計の値フィールドとして配置します。その後、`pivotTable.pageFieldOrder` を `PrintOrderType.DownThenOver` に設定し、`pivotTable.pageFieldWrapCount` を `2` に設定します。
`DownThenOver` で折り返し数を 2 にすると、2 つのページフィールドは縦に配置されます。`Year` が上、`Region` がその直下に配置され、ピボットテーブルの上部に 1 列を構成します。したがって、ストリップは 1 フィールド幅の 2 行を占め、例 1 とは異なります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **例 3: ページフィールドを移動する**
3 つ目のシナリオでは、このデータセットとフィールド配置を維持し、中立的なレイアウト（`OverThenDown`、折り返し数 `2`）を設定してから、`pivotTable.pageFields.move` 操作を示します。`move(0, 1)` の呼び出しにより、インデックス 0 のページフィールド（`Year`）が位置 1 に移動し、位置 1 にあったページフィールド（`Region`）が位置 0 に移動します。
この呼び出しの後、`Region` が最初のページフィールド、`Year` が 2 番目のページフィールドになります。折り返し数と順序モードは変更されないため、ストリップは引き続き横並びで描画され、2 つのドロップダウンの順序だけが入れ替わります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **関連記事**
- [ピボットテーブルにページフィールドを追加する](/cells/ja/javascript-cpp/add-page-field-in-pivot-table/) — ピボットテーブルにページフィールドを追加する方法を説明する親」です。
- [ピボットテーブルの値フィールドを管理](/cells/ja/javascript-cpp/manage-value-fields/) — 値領域の構成方法と、この記事で使用する Sum 集計について説明します。
- [ピボットテーブルにスタイルを適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/) — ページフィールドのストリップを配置した後、作成されたピボットテーブルに書式を適用する方法を示します。

{{< app/cells/assistant language="javascript-cpp" >}}