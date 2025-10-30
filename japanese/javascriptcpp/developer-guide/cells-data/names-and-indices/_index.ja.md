---
title: セル名と行/列インデックスの変換
linktitle: セル名とインデックス変換
type: docs
weight: 10
url: /ja/javascript-cpp/names-and-indices/
description: C++APIを通じてセル名と行/列インデックス間の変換方法を学びます。
keywords: JavaScriptを使用してC++で行・列インデックスからセル名を取得、セル名から行・列インデックスを取得、安全なワークシート名を作成し、追加する
---

## **行と列のインデックスからセル名を取得**
行と列のインデックスを指定すると、セルの名前を見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells for JavaScriptはC++経由でCellsHelper.cellIndexToNameメソッドを提供し、行と列のインデックスを指定するとセルの名前を取得できます。

{{% alert color="primary" %}} 

Microsoft Excelは行と列のインデックスを1から数え始めます。Microsoft Excelと異なり、Aspose.Cells for JavaScriptはC++経由で行と列のインデックスを0から数え始めます。

{{% /alert %}} 

以下のサンプルコードは、CellsHelper.cellIndexToNameを使用して、既知の行と列のインデックスからセルの名前にアクセスする方法を示しています。コードの出力例：



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **セル名から行と列のインデックスを取得**
セルの名前から行と列のインデックスを見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells for JavaScriptはC++経由でCellsHelper.cellNameToIndexメソッドを提供し、セルの名前から行と列のインデックスを取得できます。

{{% alert color="primary" %}} 

Microsoft Excelは行と列のインデックスを1から数え始めます。Microsoft Excelと異なり、Aspose.Cells for JavaScriptはC++経由で行と列のインデックスを0から数え始めます。

{{% /alert %}} 

以下のサンプルコードは、CellsHelper.cellNameToIndexを使用して、セルの名前から行と列のインデックスを取得する方法を示しています。コードは次の出力を生成します。



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **安全なシート名を作成します。**
ランタイムでシート名を割り当てる必要がある場合があります。このシナリオでは、<>+(?”などの追加文字を含むシート名が存在する可能性があります。そのような文字をプレセットされた文字に置き換える必要があります。同様に、長さが31文字を超える場合は切り詰める必要があります。Apache POIは安全な名前を作成する機能を提供しており、Aspose.Cells for JavaScriptもこれらの問題を処理するために同様の機能を提供します。以下のサンプルコードはこの機能を示しています：



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

出力:

これは最初の名前です。

` <> + (形容詞Private _ " Private"
