---
title: C++を使用したJavaScriptによる範囲の管理
linktitle: 範囲
type: docs
weight: 105
url: /ja/javascript-cpp/managing-ranges/
description: Excelの範囲管理方法をAspose.Cells for JavaScriptを使って学びます。範囲の作成、値やスタイルの設定、さまざまな操作を実行します。
---

## **紹介**

Excelでは、マウスのボックス選択を使って複数のセルを選択でき、その選択範囲は「Range」と呼ばれます。

例えば、Excelのセル「A1」で左クリックをしてから「C4」までドラッグできます。選択した矩形範囲は、Aspose.Cells for JavaScriptをC++経由でオブジェクトとして簡単に作成することもできます。

範囲を作成し、値を設定し、スタイルを適用し、その他さまざまな操作を行う方法です。

## **C++経由のAspose.Cells for JavaScriptを使った範囲の管理**

Aspose.Cellsは、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスには[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションが提供されています。

### **範囲の作成**

A1:C4にまたがる長方形領域を作成する場合は、次のコードを使用できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells (converted from getWorksheets().get(0).getCells() to properties)
            const cells = workbook.worksheets.get(0).cells;

            // Create Range A1:C4
            const range = cells.createRange("A1:C4");

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Range A1:C4 created successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **範囲のセルに値を入力する**

A1:C4にまたがるセルの範囲があるとします。行列は4*3=12セルを作ります。それぞれの範囲セルは順に配置されます: Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

次の例は、範囲のセルに値を入力する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Range Value Example</title>
    </head>
    <body>
        <h1>Range Value Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            const range = cells.createRange("A1:C4");

            range.get(0, 0).value = "A1";
            range.get(0, 1).value = "B1";
            range.get(0, 2).value = "C1";
            range.get(3, 0).value = "A4";
            range.get(3, 1).value = "B4";
            range.get(3, 2).value = "C4";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeValueTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **範囲のセルのスタイルを設定する**

次の例は、範囲内のセルのスタイルを設定する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Range Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Gets Cells
            const cells = workbook.worksheets.get(0).cells;
            // Creates Range
            const range = cells.createRange("A1:C4");
            // Puts value
            range.get(0, 0).value = "A1";
            range.get(3, 2).value = "C4";
            // Sets Style
            let style00 = workbook.createStyle();
            style00.pattern = AsposeCells.BackgroundType.Solid;
            style00.foregroundColor = new AsposeCells.Color(255, 0, 0); // Red
            range.get(0, 0).style = style00;
            let style32 = workbook.createStyle();
            style32.pattern = AsposeCells.BackgroundType.HorizontalStripe;
            style32.foregroundColor = new AsposeCells.Color(0, 255, 0); // Green
            range.get(3, 2).style = style32;
            // Saves the Workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeStyleTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **範囲のCurrentRegionを取得する**

CurrentRegionは、現在の範囲を表すRangeオブジェクトを返すプロパティです。 

現在の領域は、空白の行と列の組み合わせによって囲まれた範囲です。読み取り専用です。

Excelでは、CurrentRegionエリアを次の方法で取得できます:
1. マウスボックスを使ってエリア（範囲1）を選択します。
2. 「ホーム - 編集 - 検索と選択 - 特定の場所に移動」をクリックするか、「Ctrl+Shift+*」を使用すると、Excelが自動的にエリア（範囲2）を選択します。これで範囲2は範囲1のCurrentRegionです。

以下のテストファイルをダウンロードし、Excelで開いて、マウスボックスを使ってエリア「A1:D7」を選択し、「Ctrl+Shift+*」をクリックすると、「A1:C3」エリアが選択されているのが見えます。

[current_region.xlsx](current_region.xlsx)

次に、以下の例を実行して、Aspose.Cellsでの動作を確認してください：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Current Region Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Cells
            const cells = worksheet.cells;

            // Create Range
            const src = cells.createRange("A1:D7");

            // Get CurrentRegion (converted from getCurrentRegion())
            const A1C3 = src.currentRegion;

            // Save the workbook (no modifications were required by original code)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.current_region.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Current region obtained successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```


## **高度なトピック**
- [ExcelファイルのAutoFill範囲](/cells/ja/javascript-cpp/autofill-ranges/)
- [Excelの範囲をコピー](/cells/ja/javascript-cpp/copy-ranges-of-Excel/)
- [Excelの範囲のデータをコピーする](/cells/ja/javascript-cpp/copy-range-data-only/)
- [スタイルで範囲データをコピー](/cells/ja/javascript-cpp/copy-range-data-with-style/)
- [ソースの範囲の行の高さのみをコピー](/cells/ja/javascript-cpp/copy-range-style-only/)
- [ユニオン範囲の作成](/cells/ja/javascript-cpp/create-union-range/)
- [範囲を切り取って貼り付ける](/cells/ja/javascript-cpp/cut-and-paste-cells/)
- [範囲を削除する](/cells/ja/javascript-cpp/delete-ranges-from-Excel/)
- [範囲のアドレス、セル数、オフセット、列全体、行全体を取得する](/cells/ja/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [範囲を挿入する](/cells/ja/javascript-cpp/insert-ranges-to-Excel/)
- [セルの範囲を結合または結合解除する](/cells/ja/javascript-cpp/merge-or-unmerge-range-of-cells/)
- [ワークシート内のセルの範囲を移動する](/cells/ja/javascript-cpp/move-range-of-cells-in-a-worksheet/)
- [ワークブックおよびワークシートスコープの名前付き範囲を作成する](/cells/ja/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [範囲内のデータを検索および置換する](/cells/ja/javascript-cpp/search-and-replace-data-in-a-range/)
