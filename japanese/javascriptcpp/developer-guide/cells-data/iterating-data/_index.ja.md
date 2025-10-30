---
title: JavaScript経由のC++で列挙子を使用し、どのようにどこで使用するか
linktitle: データの反復
type: docs
weight: 55
url: /ja/javascript-cpp/how-and-where-to-use-enumerators/
description: C++ APIを通じてAspose.Cells for JavaScriptを使って列挙子の使い方を学びます。
keywords: C++を使用したJavaScriptの列挙子の使い方、C++を使用したセルの列挙子JavaScript、C++を使用した行の列挙子JavaScript、C++を使用した列の列挙子JavaScript
---

{{% alert color="primary" %}}  

列挙子はコンテナやコレクションを遍歴する能力を提供するオブジェクトです。列挙子はコレクション内のデータを読み取るために使用できますが、基礎となるコレクションを変更することはできません。一方、Arrayは`enumerator`という一つのメソッドを定義しており、それは`IEnumerator`インターフェースを返します。これにより、コレクションへの読み取り専用アクセスが可能になります。  

Aspose.CellsのAPIはたくさんの列挙子を提供していますが、この記事では主に以下にリストされている3つのタイプについて説明しています。  

1. セル列挙子  
1. 行列挙子  
1. 列列挙子  

{{% /alert %}}  

## **列挙子の使用方法**  

### **セル列挙子**  

セル列挙子へのアクセス方法にはさまざまな方法があり、アプリケーションの要件に基づいてこれらのメソッドのいずれかを使用できます。セル列挙子を返すメソッドは次のとおりです。  

1. [**Cells.enumerator**](https://reference.aspose.com/cells/javascript-cpp/cells/#enumerator--)  
1. [**Row.enumerator**](https://reference.aspose.com/cells/javascript-cpp/row/#enumerator--)  
1. [**Range.enumerator**](https://reference.aspose.com/cells/javascript-cpp/range/#enumerator--)  

上記のすべての方法は、初期化されたセルコレクションをトラバースする列挙子を返します。  

{{% alert color="primary" %}}  

セルをトラバースする際には、コレクションを修正してはいけません（新しいセルを作成する操作や既存のセルを削除する操作）。そうしない場合、列挙子はすべてのセルを正しくトラバースできなくなる可能性があります（一部の要素が繰り返しトラバースされたり、スキップされたりすることがあります）。  

{{% /alert %}}  

次のコード例は、Cellsコレクションに対するIEnumeratorインターフェースの実装例を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Values</h1>
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            const resultLines = [];

            // Iterate over all cells in the worksheet
            const cellsEnumerator = worksheet.cells.getEnumerator();
            for (const cell of cellsEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over the first row's cells
            const firstRowEnumerator = worksheet.cells.rows.get(0).getEnumerator();
            for (const cell of firstRowEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            // Iterate over a specific range A1:B10
            const rangeEnumerator = worksheet.cells.createRange("A1:B10").getEnumerator();
            for (const cell of rangeEnumerator) {
                console.log(`${cell.name} ${cell.value}`);
                resultLines.push(`${cell.name} ${cell.value}`);
            }

            document.getElementById('result').innerHTML = `<pre>${resultLines.join('\n')}</pre>`;
        });
    </script>
</html>
```  

### **行列挙子**  

Rowsの列挙子は、[**RowCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/rowcollection/#enumerator--)メソッドを使用してアクセスできます。以下のコード例は、[**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection)に対する`IEnumerator`インターフェースの実装例を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - List Row Indexes</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get RowCollection and iterate using index
            const rows = workbook.worksheets.get(0).cells.rows;
            const rowCount = rows.count;

            // Traverse rows in the collection and display indexes
            let output = '<p>Row indexes:</p><ul>';
            for (let i = 0; i < rowCount; i++) {
                const row = rows.get(i);
                output += `<li>${row.index}</li>`;
                console.log(row.index);
            }
            output += '</ul>';
            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```  

### **列列挙子**  

Columnsの列挙子は、[**ColumnCollection.enumerator**](https://reference.aspose.com/cells/javascript-cpp/columncollection)メソッドを使用してアクセスできます。以下のコード例は、[**ColumnCollection**](https://reference.aspose.com/cells/javascript-cpp/columncollection)に対する`IEnumerator`インターフェースの実装例を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Columns Indexes Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get columns collection from first worksheet
            const columns = workbook.worksheets.get(0).cells.columns;
            // Traverse columns using index
            const count = columns.count;
            let html = '<p>Columns indexes:</p><ul>';
            for (let i = 0; i < count; i++) {
                const col = columns.get(i);
                html += `<li>${col.index}</li>`;
                console.log(col.index);
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

## **列挙子の使用場所**  

列挙子の使用の利点について議論するために、実例を見てみましょう。  

**シナリオ**  

特定の [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 内のすべてのセルを走査し、その値を読み取ることがアプリケーションの要件です。これを実現する方法はいくつかあります。以下にいくつか例を示します。  

### **表示範囲を使用する**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Max Display Range Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Get the MaxDisplayRange
            const displayRange = cells.maxDisplayRange;

            // Loop over all cells in the MaxDisplayRange
            let outputLines = [];
            for (let row = displayRange.firstRow; row < displayRange.rowCount; row++) {
                for (let col = displayRange.firstColumn; col < displayRange.columnCount; col++) {
                    // Read the Cell value (stringValue property)
                    const cell = displayRange.get(row, col);
                    outputLines.push(cell.stringValue);
                    console.log(cell.stringValue);
                }
            }

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```  

### **MaxDataRowおよびMaxDataColumnを使用する**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result { margin-top: 15px; max-height: 400px; overflow: auto; border: 1px solid #ddd; padding: 10px; }
            .cell-value { padding: 2px 0; border-bottom: 1px dashed #eee; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Read Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        function escapeHtml(text) {
            if (text === null || text === undefined) return '';
            return String(text)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p class="error">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection of first worksheet
            const cells2 = workbook.worksheets.get(0).cells;
            const maxDataRow = cells2.maxDataRow;
            const maxDataColumn = cells2.maxDataColumn;

            const outputLines = [];
            // Loop over all cells
            for (let row = 0; row <= maxDataRow; row++) {
                for (let col = 0; col <= maxDataColumn; col++) {
                    // Read the Cell value
                    const currentCell = cells2.checkCell(row, col);
                    if (currentCell) {
                        const cellText = currentCell.stringValue;
                        outputLines.push('<div class="cell-value">' + escapeHtml(cellText) + '</div>');
                        console.log(cellText);
                    }
                }
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p>No cell values found.</p>';
            } else {
                resultDiv.innerHTML = outputLines.join('');
            }
        });
    </script>
</html>
```  

上記のアプローチのそれぞれがほとんど同じロジックを使用していることがわかります。つまり、コレクション内のすべてのセルをループしてセルの値を読み取ります。これにはいくつかの理由で問題が生じる可能性があります。  

1. [**maxRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxRow--)、[**maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--)、[**maxColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxColumn--)、[**maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--)、[**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--) などのAPIは、対応する統計情報を収集するのに追加の時間が必要です。行×列のデータマトリックスが大きい場合、これらのAPIを使用するとパフォーマンスに影響を及ぼす可能性があります。  
1. ほとんどの場合、指定された範囲内のすべてのセルがインスタンス化されていません。そのような状況では、行列内のすべてのセルを確認することは、初期化されたセルのみを確認する場合と比べて効率的ではありません。  
1. Cells row、columnとしてセルにアクセスすることは、範囲内のすべてのセルオブジェクトをインスタンス化することになり、最終的にOutOfMemoryExceptionを引き起こす可能性があります。  

## **結論**  

上記の事実に基づいて、列挙子を使用すべき可能なシナリオが以下に示されています。  

1. セルコレクションの読み取り専用アクセスが必要な場合、つまり、セルの確認のみが必要な場合。  
1. 多数のセルを走査する必要がある場合。  
1. 初期化されたセル/行/列のみを走査する必要がある場合。
