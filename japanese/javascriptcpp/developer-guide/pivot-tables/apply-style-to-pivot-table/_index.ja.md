---
title: Aspose.Cells for JavaScript via C++ でピボットテーブルにスタイルを適用する
linktitle: Aspose.Cells for JavaScript via C++ でピボットテーブルにスタイルを適用する
description: Aspose.Cells for JavaScript via C++ でピボットテーブルに組み込みスタイルとカスタムスタイルを適用する方法を説明し、従来の XLS 自動形式、Excel 2007 以降の名前付きスタイル、カスタムピボットテーブルスタイル、および FormatAll ショートカットについて説明します。
keywords: Aspose.Cells for JavaScript via C++ ピボットテーブルスタイル, PivotTableStyleType, AutoFormatType, FormatAll, カスタムスタイル, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /ja/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、従来のピボットテーブル自動形式（`.xls` ファイル向け）と、名前付きまたはカスタムピボットテーブルスタイル（`.xlsx`、`.xlsm`、`.xlsb` ファイル向け）の両方を適用できます。呼び出す API は、ワークブックの読み込み元形式ではなく、保存先のファイル形式によって決まります。
{{% /alert %}}

## **はじめに**
Aspose.Cells は、ピボットテーブル向けの 2 つのスタイル API を提供します。どちらの API を使用するかを決定するのは、読み込み元の形式ではなく、ワークブックを保存する形式です。`.xls` ファイルから読み込んだワークブックを `.xlsx` として再保存する場合は、従来の API ではなく、新しいスタイル API が適用されます。
- `pivotTable.pivotTableStyleType` は、組み込みの名前付きスタイル（ライトテーマとダークテーマ、および Excel 2017 で追加されたスタイルを含む）を選択します。これらのプリセットは読み取り専用です。
- `pivotTable.pivotTableStyleName` は、`workbook.worksheets.tableStyles.addPivotTableStyle(...)` を使用して自分で定義したカスタムスタイルを指定します。プリセットの範囲を超えて色、罫線、フォントを変更する場合は、カスタムスタイルが必要です。
さらに、`pivotTable.formatAll(style)` は、単一の `style` オブジェクトをピボットテーブルのすべてのセルに適用するショートカットです。上記のいずれかのスタイル API で設定した内容をすべて上書きします。元のテーマにかかわらず、統一された外観が必要な場合に便利です。

## **従来の XLS プリセット自動形式を適用する**
`pivotTable.autoFormatType` には、`Aspose.Cells.Pivot.PivotTableAutoFormatType` 列挙型の値を指定します。利用可能な値は、`Report1` から `Report10` まで、`Classic`、および `Table1` から `Table10` までです。
次の例では、新しいワークブックを作成し、Fruit/Year/Amount のサンプルデータを入力して、ピボットテーブルを追加し、`PivotTableAutoFormatType.Report5` を適用します。結果を `.xls` として保存します。

{{% alert color="primary" %}}
**列フィールドがないのはなぜですか？** レポートシリーズ自動形式（`Report1` から `Report10`、および `Table1` から `Table10`）は、行フィールドと値だけからなる**1 次元のピボットテーブル**向けに従来の Excel で設計されているため、列フィールドヘッダーの組み込みスタイルがありません。ピボットテーブルで列フィールドを使用する必要がある場合は、[シナリオ 2](#apply-a-modern-named-preset-pivot-table-style) の `PivotTableStyleType` プリセットを使用してください。このプリセットは、現在の Excel が使用する 2 次元レイアウト向けに設計されています。
{{% /alert %}}

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
            // シナリオ1: 従来のXLSプリセット自動形式を適用する
            // 使用中のAPI: PivotTable.AutoFormatType
            // 対象ファイル形式: .xls（従来形式）
            // 完全な例とデータファイルについては、https://github.com/aspose-cells/Aspose.Cells-for-.NET にアクセスしてください
            // 新しいワークブックを作成する
            const workbook = new Workbook();
            // 最初のワークシートを取得する
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // ヘッダー行（Fruit、Year、Amount）と、2020年および2021年にわたる9行のデータ（grape、blueberry、kiwi、cherry）でソースデータに入力する
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // ソース範囲 A1:C10 を使用して、宛先セル E3 にピボットテーブルを追加する
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // フィールドを割り当てる: Fruit -> 行、Amount -> データ
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 従来のXLSプリセット自動形式「Report5」を適用する
            // 注: このプロパティは .xls 形式で保存する場合にのみ有効です。
            // .xlsx/.xlsm/.xlsb 形式で保存すると、Excel は AutoFormatType を無視し、
            // PivotTableStyleType / PivotTableStyleName で指定された形式を使用します。
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // ワークブックを従来の .xls 形式で保存する
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **新しい名前付きプリセットのピボットテーブルスタイルを適用する**
`pivotTable.pivotTableStyleType` は、Excel 2007 でピボットテーブルに導入された組み込みの名前付きスタイルを選択します。`PivotTableStyleType` 列挙型では、次の 3 つのテーマファミリーが定義されています。`PivotTableStyleLight1` から `PivotTableStyleLight28` までのライトファミリー、`PivotTableStyleMedium1` から `PivotTableStyleMedium28` までのミディアムファミリー、`PivotTableStyleDark1` から `PivotTableStyleDark28` までのダークファミリーです。また、`None` と `Custom` も定義されています。各ファミリーで番号が大きいメンバーは、Excel 2017 で追加されたスタイルです。
これらのプリセットは読み取り専用です。プリセットの内容を超える変更（色、罫線、フォントなど）が必要になった場合は、[シナリオ 3](#define-and-apply-a-custom-pivot-table-style) に示すようにカスタムピボットスタイルを定義する必要があります。

{{% alert color="primary" %}}
**なぜレポートシリーズの自動形式ではなく、新しいプリセットを使うのですか？** `PivotTableAutoFormatType` の `Report1` から `Report10` まで、および `Table1` から `Table10` までの値は、ピボットの列フィールドが導入される前から存在するため、列フィールドヘッダーの書式設定が含まれません。そのため、Excel ではそれらのヘッダーの書式が未設定のまま表示されます。`PivotTableStyleType` のプリセットは、現在の Excel が使用する 2 次元レイアウト向けに設計されており、行フィールドと列フィールドのヘッダーの両方にスタイルを適用します。
{{% /alert %}}

このシナリオでは、シナリオ 1 の Fruit/Year/Amount データセットを再利用します。`Fruit` 行フィールドに加え、`PivotFieldType.Column` を使用して `Year` を列領域に追加します。`pivotTable.pivotTableStyleType` でダークテーマのプリセット `PivotTableStyleDark1` を適用し、結果を `.xlsx` として保存します。この形式では `PivotTableStyleType` が適用されます。

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // シナリオ 2: PivotTableStyleType を使用して、新しい Excel 2007+ の名前付きプリセットスタイルを適用します。
            // 対象ファイル形式: .xlsx。PivotTableStyleType 列挙体は Aspose.Cells 名前空間にあります。
            // Aspose.Cells.Pivot 名前空間にはないため、追加の using 宣言は不要です。
            // GitHub リファレンス: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // ヘッダー行: 果物 / 年 / 金額
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 果物 / 年 / 金額からなる 9 件のデータ行
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // A1:C10 をソースとして E3 にピボットテーブルを追加します。
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // ピボットフィールドを割り当てる: 果物 -> 行領域、年 -> 列領域、金額 -> データ領域
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 新しい Excel 2007+ の名前付きプリセットピボットスタイルを適用します。
            // PivotTableStyleType は .xlsx / .xlsm / .xlsb ファイル向けの正しい API です。AutoFormatType は
            // これらの形式では Excel に無視されます。PivotTableStyleDark1 はダークテーマファミリー
            // (PivotTableStyleDark1..PivotTableStyleDark28) に属し、同じ列挙体には新しい Excel 2017 の
            // ライト/ダークテーマ (PivotTableStyleLight1..Light28 / Dark1..Dark28) も含まれています。
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // 新しい .xlsx 形式で保存します。PivotTableStyleType が有効なのはこの形式です。
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

## **カスタムピボットテーブルスタイルを定義して適用する**
組み込みプリセットは変更できません。色、罫線、フォントについてプリセットとは別の設定が必要になったら、カスタムピボットスタイルを定義する必要があります。手順は次の 3 つです。
1. `workbook.worksheets.tableStyles.addPivotTableStyle(name)` を使用して、ワークブックの `tableStyles` コレクションにカスタムスタイルを追加します。新しく作成したスタイルのインデックスが返されます。
2. `tableStyle.tableStyleElements.add(tableStyleElementType)` を使用して `WholeTable` や `GrandTotalRow` などの要素を追加し、スタイルを構成します。続いて、`tableStyleElement.setElementStyle(style)` を使用して、各要素に `style` を割り当てます。
3. `pivotTable.pivotTableStyleName` をカスタムスタイル名に設定して、ピボットテーブルにカスタムスタイルを適用します。ここでは `pivotTable.pivotTableStyleType` を使用しないでください。このプロパティは組み込みプリセットを適用するプロパティだからです。

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` と `pivotTable.pivotTableStyleType` は、用途が異なります。組み込みプリセットには `pivotTable.pivotTableStyleType` を使用します。`addPivotTableStyle` を使用して定義したカスタムスタイルには、`pivotTable.pivotTableStyleName` を使用します。両方を設定しても問題ありませんが、意図した方に一致するスタイルだけが反映されます。
`TableStyleElementType` には、`WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels`、および `PageFieldValues` などの値があります。
次の例では、`WholeTable` に細い黒色の罫線、`GrandTotalRow` に太字の赤色フォントを適用したカスタムピボットスタイルを定義します。`pivotTable.pivotTableStyleName` でこのスタイルを適用し、`.xlsx` として保存します。
{{% /alert %}}

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
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // ソースデータを入力: ヘッダー行 + 9つのデータ行 (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 200;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 300;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 400;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // A1:C10 をソースとし、E3 に配置するピボットテーブルを追加
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // ステップ1: 新しいカスタムピボットテーブルスタイルを登録し、そのインデックスを取得
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // ステップ2: WholeTable 要素を追加し、4辺すべてに細い黒色の罫線を適用
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // ステップ3: GrandTotalRow 要素を追加し、太い赤色のフォントを適用
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // ステップ4: カスタムスタイルを名前で適用（組み込みプリセット用ではない PivotTableStyleType は使用しない）
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **formatAll でピボットのすべてのセルに 1 つのスタイルを適用する**
`pivotTable.formatAll(style)` は、単一の `style` オブジェクトをピボットテーブルのすべてのセル（データ領域、行および列のヘッダー、および合計を含む）に適用するショートカットです。`pivotTable.pivotTableStyleType` または `pivotTable.pivotTableStyleName` で以前に設定した内容はすべて上書きされます。

{{% alert color="primary" %}}
`formatAll` は、`pivotTable.pivotTableStyleType` と `pivotTable.pivotTableStyleName` の両方を上書きします。ピボットテーブルの全体に、テーマに依存しない統一された外観が必要な場合にのみ使用してください。
次の例では、黄色の単色塗りつぶし、太字の濃青色フォント、および四辺すべてに細い黒色の罫線を持つ `style` を作成し、`formatAll` で適用して `.xlsx` として保存します。
{{% /alert %}}

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
            // シナリオ 4: FormatAll を使用してピボットテーブルのすべてのセルに単一のスタイルを適用します
            // 使用中の API: PivotTable.FormatAll(Style)
            // 対象形式: .xlsx
            // GitHub リファレンス: Aspose.Cells-for-.NET リポジトリのピボットテーブルのスタイル設定例を参照してください
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // ソースデータを入力: ヘッダー行 (行 1) + 9 データ行 (行 2-10)
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // ピボットテーブルを追加: ソース範囲 A1:C10、宛先セル E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // ピボットフィールドを割り当て: Fruit -> 行領域、Year -> 列領域、Amount -> データ領域
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // ピボットテーブルのすべてのセルに強制適用する Style を作成します
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // FormatAll を適用: この単一スタイルをピボットテーブルのすべてのセルに強制適用し、
            // 以前に設定した PivotTableStyleType / PivotTableStyleName を上書きします
            pivotTable.formatAll(style);
            // ワークブックを最新の .xlsx 形式で保存します
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **どのスタイル API を使用すべきか**
スタイル API の選択は、保存するファイル形式によって異なります。以下の表を参照して判断してください。
| 対象ファイル形式 | 使用する API | 注記 |
|---|---|---|
| `.xls`（従来形式） | `pivotTable.autoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` の値（例：`Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。新しい形式として保存する場合は無視されます。 |
| `.xlsx` / `.xlsm` / `.xlsb`（新しい形式、組み込みスタイル） | `pivotTable.pivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` の値（ライトテーマ/ダークテーマ、Excel 2017 で追加されたものを含む）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（新しい形式、カスタムスタイル） | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | 組み込みプリセットでは不十分な場合に使用します。`tableStyleElement.setElementStyle(...)` で構成します。 |
| すべての形式（ピボット全体への一括上書き） | `pivotTable.formatAll(style)` | ピボット全体のすべてのスタイル設定を上書きするショートカットです。 |
判断に迷った場合は `.xlsx` として保存し、組み込みテーマには `pivotTable.pivotTableStyleType` を、カスタムスタイルには `pivotTable.pivotTableStyleName` を使用してください。

{{< app/cells/assistant language="javascript-cpp" >}}