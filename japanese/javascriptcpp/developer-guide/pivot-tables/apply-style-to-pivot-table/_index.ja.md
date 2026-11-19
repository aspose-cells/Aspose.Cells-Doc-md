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
            // Scenario 1: Apply a legacy XLS preset autoformat
            // API in use: PivotTable.AutoFormatType
            // Target file format: .xls (legacy)
            // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // Create a new workbook
            const workbook = new Workbook();
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Populate the source data with header row (Fruit, Year, Amount)
            // and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
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
            // Add a pivot table at destination cell E3, using source range A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign fields: Fruit -> Rows, Amount -> Data
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Apply the legacy XLS preset autoformat "Report5"
            // Note: This property is only meaningful when saving as .xls.
            // When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
            // and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // Save the workbook in legacy .xls format
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
            // Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
            // Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
            // (not in Aspose.Cells.Pivot) -- that is why we do not need any extra using for it.
            // GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Header row: Fruit / Year / Amount
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 data rows of Fruit / Year / Amount
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
            // Add a pivot table at E3, sourced from A1:C10
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Apply a modern Excel 2007+ named preset pivot style.
            // PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
            // is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
            // family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
            // newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
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
            // Populate source data: header row + 9 data rows (A1:C10)
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
            // Add pivot table sourced from A1:C10, anchored at E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Step 1: register a new custom pivot table style and capture its index
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Step 2: add a WholeTable element and apply thin black borders on all four sides
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
            // Step 3: add a GrandTotalRow element and apply bold red font
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
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
            // Scenario 4: Apply a single Style to every pivot table cell using FormatAll
            // API in use: PivotTable.FormatAll(Style)
            // Target format: .xlsx
            // GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Populate source data: header row (row 1) + 9 data rows (rows 2-10)
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
            // Add pivot table: source range A1:C10, destination cell E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Build a Style that will be forced onto every cell of the pivot table
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
            // Apply FormatAll: forces this single style onto every cell of the pivot table,
            // overriding any PivotTableStyleType / PivotTableStyleName previously set
            pivotTable.formatAll(style);
            // Save the workbook in the modern .xlsx format
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