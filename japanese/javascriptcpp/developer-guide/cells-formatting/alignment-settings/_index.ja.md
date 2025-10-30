---
title: 配置設定
linktitle: 配置設定
description: Aspose.Cellsライブラリでは、JavaScript経由C++を使用してセルのアライメント設定を調整し、テキストのレイアウトと表示を変更できます。このドキュメントは、セルのアライメント設定に関する詳細な手順とサンプルコードを提供します。
keywords: Aspose.Cells、セルのアライメント、水平方向のアライメント、垂直方向のアライメント、テキスト折り返しJavaScript経由C++
type: docs
weight: 20
url: /ja/javascript-cpp/cells-alignment-settings/
---

## **配置設定の構成**

### **Microsoft Excelの配置設定**

セルの書式設定にMicrosoft Excelを使用したことがある人であれば、Microsoft Excelの配置設定に精通しているでしょう。

上記の図から分かるように、異なる種類の配置オプションがあります:

- テキストの配置（水平および垂直）
- インデント
- 方向
- テキスト コントロール。
- テキスト方向。

これらの配置設定は、Aspose.Cellsで完全にサポートされており、以下で詳しく説明します。

### **Aspose.Cellsの配置設定**

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションを含みます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスのオブジェクトを表します。

Aspose.Cellsは、[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)と[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)メソッドを提供し、セルの書式設定を取得・設定します。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)クラスは整列設定の構成に役立つプロパティを提供します。

任意のテキスト整列タイプを [**TextAlignmentType**](https://reference.aspose.com/cells/javascript-cpp/textalignmenttype) 列挙型から選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/javascript-cpp/textalignmenttype)列挙型に定義されたプリセットのテキスト整列タイプは次の通りです。

|**テキスト配置タイプ**|**説明**|
| :- | :- |
|Bottom| 下部のテキスト配置を表します。
|Center| 中央のテキスト配置を表します。
|CenterAcross| 横方向に中央揃えのテキスト配置を表します。
|Distributed| 分散テキスト配置を表します。
|Fill| 塗りつぶしのテキスト配置を表します。
|General| 一般的なテキスト配置を表します。
|Justify| 両端揃えのテキスト配置を表します。
|Left| 左揃えのテキスト配置を表します。
|Right| 右揃えのテキスト配置を表します。
|Top| 上部のテキスト配置を表します。
|JustifiedLow| アラビア語のテキストに対して調整されたカシダ長でテキストを配置します。
|ThaiDistributed| 特にタイ語のテキストを分散配置し、各文字を単語として扱います。

{{% alert color="primary" %}}

また、[**Style.isJustifyDistributed(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isJustifyDistributed-boolean-)メソッドを使用して、均等配分設定を適用することもできます。

{{% /alert %}}

#### **水平配置**

[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトの[**horizontalAlignment**](https://reference.aspose.com/cells/javascript-cpp/style/#horizontalAlignment-textalignmenttype-)メソッドを使用して、テキストを水平に整列させます。

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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Visit Aspose!");

            // Setting the horizontal alignment of the text in the "A1" cell
            const style = cell.style;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



#### **垂直配置**

水平整列と同様に、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトの[**verticalAlignment**](https://reference.aspose.com/cells/javascript-cpp/style/#verticalAlignment-textalignmenttype-)メソッドを使用して、テキストを垂直に整列させます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Clearing all the worksheets
            workbook.worksheets.clear();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the horizontal/vertical alignment of the text in the "A1" cell via style
            const style = cell.style;
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


#### **インデント**

セル内のテキストのインデントレベルを [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) オブジェクトの [**indentLevel**](https://reference.aspose.com/cells/javascript-cpp/style/#indentLevel-number-) メソッドで設定することが可能です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Set Cell Indent Level Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the horizontal alignment of the text in the "A1" cell
            const style = cell.style;

            // Setting the indentation level of the text (inside the cell) to 2
            style.indentLevel = 2;

            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```



#### **方向**

セル内のテキストの向き（回転角度）を [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) オブジェクトの [**rotationAngle**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) メソッドで設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Modify Cell</h1>
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
            // This example creates a new workbook, updates A1, sets rotation, and saves the file.
            const fileInput = document.getElementById('fileInput');

            // Instantiate a new Workbook (blank)
            const workbook = new Workbook();

            // Obtain reference to the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Getting the style of the cell
            const style = cell.style;

            // Setting the rotation of the text (inside the cell) to 25
            style.rotationAngle = 25;

            // Assign the modified style back to the cell
            cell.style = style;

            // Save the Excel file in Excel 97-2003 format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **テキストコントロール**

次のセクションでは、テキストの折り返し、収縮に合わせるなど、テキストの制御方法について説明します。

##### **テキストの折り返し**

セルのテキストの折り返しは、すべてのテキストが収まるようにセルの高さを調整します。これにより、テキストの切り取りや隣接セルへのはみ出しを防ぎます。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトの[**isTextWrapped(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isTextWrapped-boolean-)メソッドを使って折り返しをオンまたはオフに設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = workbook.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cells = ws.cells;

            // Increase the width of First Column Width
            cells.columns.get(0).width = 35;

            // Increase the height of first row
            cells.rows.get(0).height = 36;

            // Add Text to the First Cell
            const cellRef = cells.checkCell(0, 0);
            cellRef.value = "I am using the latest version of Aspose.Cells to test this functionality";

            // Make Cell's Text wrap
            const style = cellRef.style;
            style.isTextWrapped = true;
            cellRef.style = style;

            // Save Excel File
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **収縮に合わせる**

セル内のテキストの折り返しの一つの方法は、セルの寸法に合わせてテキストサイズを縮小することです。これは、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトの[**shrinkToFit(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#shrinkToFit-boolean-)メソッドを**true**に設定することで行います。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Cell Style Example</title>
    </head>
    <body>
        <h1>Set Cell Style Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Getting the style of the cell
            const style = cell.style;

            // Shrinking the text to fit according to the dimensions of the cell
            style.shrinkToFit = true;

            // Applying the style back to the cell
            cell.style = style;

            // Saving the Excel file in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


##### **セルの結合**

Microsoft Excelのように、Aspose.Cellsは複数のセルを結合して1つにすることをサポートします。Aspose.Cellsはこのタスクに対して2つのアプローチを提供します。一つは [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) コレクションの [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) メソッドを呼び出す方法です。[**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-)メソッドは、セルを結合するために次のパラメータを受け取ります。

- 最初の行: 結合の開始行。
- 最初の列: 結合の開始列。
- 行数: 結合する行数。
- 列数: 結合する列数。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Cells and Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Create a Workbook.
            const wbk = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Save the Workbook.
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


もう一つは、最初に [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) コレクションの [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-)メソッドを呼び出して、結合するセル範囲を作成し、その範囲の開始と終了を指定した[**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-)メソッドを実行し、[**Range**](https://reference.aspose.com/cells/javascript-cpp/range)オブジェクトを返します。[**Range**](https://reference.aspose.com/cells/javascript-cpp/range)オブジェクトは [**merge**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) メソッドも提供し、指定された範囲を [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) オブジェクトにより結合します。

##### **テキストの方向**

セル内のテキストの読み取り順を設定することが可能です。読み取り順は、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語であり、アラビア語は右から左への言語です。

読み取り順序は [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) オブジェクトの [**textDirection**](https://reference.aspose.com/cells/javascript-cpp/style/#textDirection-textdirectiontype-) プロパティで設定されます。Aspose.Cellsは、事前定義されたテキスト方向タイプを [**TextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/textdirectiontype) 列挙型で提供します。

|**テキスト方向の種類**|**説明**|
| :- | :- |
|Context|最初に入力された文字の言語と一貫した読み取り順|
|LeftToRight|左から右の読み取り順|
|RightToLeft|右から左の読み取り順|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify A1 and Save</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextDirectionType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "I am using the latest version of Aspose.Cells to test this functionality.";

            // Gets style in the "A1" cell
            const style = cell.style;

            // Shrinking the text to fit according to the dimensions of the cell
            style.textDirection = TextDirectionType.LeftToRight;

            // Apply the style back to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **高度なトピック**
- [セルの配置を変更し、既存の書式を保持する](/cells/ja/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/javascript-cpp/line-breaks-and-text-wrapping/)
