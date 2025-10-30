---
title: ワークシートのセルへのアクセス
type: docs
weight: 10
url: /ja/javascript-cpp/accessing-cells-of-a-worksheet/
description: この例では、ワークシートの最大表示範囲の取得方法と、セルへのアクセス方法をC++ APIで示します。
keywords: セルオブジェクトを取得する、セルにアクセスする、ワークシートの最大表示範囲を取得する。 
---

{{% alert color="primary" %}}

すべてのワークシートには基本的にセルに格納されたデータが含まれています。セルはワークシートの基本的な部分であり、行と列のシーケンスとしてワークシートを構築します。データにアクセスする前に、そのセルにアクセスできるようにする必要があります。そこで、本トピックでは、C++経由のAspose.Cells for JavaScriptを使用して実行時にワークシートセルにアクセスする基本的な方法について解説します。

{{% /alert %}}

## **セルへのアクセス方法**

C++経由のAspose.Cells for JavaScriptは、Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートへアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)を含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションを提供します。

[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションを使ってワークシートのセルにアクセス可能です。C++経由のAspose.Cells for JavaScriptは、セルへのアクセスに3つの基本的な方法を提供します。

1. セル名を使用する。
1. セルの行と列のインデックスを使用します。
1.[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクション内のインデックスを使う方法

 3番目のアプローチが最速であり、1番目のアプローチが最も遅いことを述べました。アプローチ間のパフォーマンスの違いは非常に小さいため、使用するアプローチに関してはパフォーマンスの低下を心配する必要はありません。

### **セルオブジェクトの取得方法（セル名による）**

開発者は、セル名を[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションに渡して特定のセルにアクセスできます。

最初に空のワークシートを作成すると、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションのカウントはゼロです。この方法でセルにアクセスすると、そのセルがコレクションに存在するかをチェックします。存在すればセルオブジェクトを返し、なければ新しい[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)オブジェクトを作成し、コレクションに追加してから返します。この方法は、Microsoft Excelに慣れている場合には最も簡単ですが、他の方法に比べて遅いです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **セルオブジェクトの取得方法（セルの行および列インデックスによる）**

開発者は、行番号と列番号のインデックスを[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションに渡して、特定のセルにアクセスできます。

このアプローチは第1のアプローチと同じように機能します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **セルオブジェクトの取得方法（セルのセルインデックスによる）**

セルの数値インデックスを[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションに渡してアクセスすることも可能です。

この方法を使用してセルにアクセスすると、セルの数値インデックスが範囲外の場合例外がスローされることがあります。最も高速なアクセス方法ですが、重要なのは、新しいセルを追加した後にセルの数値インデックスが変わる可能性があることです。コレクション内のセルは行と列のインデックスによって内部的にソートされています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **ワークシートの最大表示範囲の取得方法**

C++経由のAspose.Cells for JavaScriptは、ワークシートの最大表示範囲にアクセスする機能を提供します。最大表示範囲とは、内容のある最初と最後のセルの範囲であり、ワークシートの内容全体をコピー、選択、または画像として表示する必要がある場合に便利です。

[**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--)を使ってワークシートの最大表示範囲にアクセスできます。以下のサンプルコードは、[**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--)プロパティにアクセスする方法を示しています。

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

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```
