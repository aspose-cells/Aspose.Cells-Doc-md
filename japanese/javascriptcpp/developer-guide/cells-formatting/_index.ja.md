---
title: JavaScriptを使ったセルの書式設定（C++経由）
description: 数値書式設定、日付書式設定、フォントスタイル、その他のセルスタイルオプションを含む、Aspose.Cells for JavaScript via C++でセルをフォーマットおよびスタイル設定する方法を学びます。私たちのガイドは、魅力的でプロフェッショナルな見た目のスプレッドシートを作成するのに役立ちます。
keywords: Aspose.Cells for JavaScript via C++、セルの書式設定、スタイリング、数値書式設定、日付書式設定、フォントスタイル、セルスタイルオプション、スプレッドシートの作成、プロフェッショナルな外観、行と列のフォーマット。
linktitle: セルの書式設定
type: docs
weight: 120
url: /ja/javascript-cpp/cells-formatting/
---

## **紹介**

{{% alert color="primary" %}}

Aspose.Cellsは、[Cell](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)および[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)メソッドを提供しており、セルの書式スタイルを取得/設定します。Aspose.Cellsはまた、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)クラスも提供します。

{{% /alert %}}

## **スタイルメソッドを使用したセルの書式設定方法**

セルに異なる種類の書式設定スタイルを適用して、背景色や前景色、枠線、フォント、水平および垂直の配置、インデントレベル、テキストの方向、回転角などを設定する。

### **スタイルメソッドの使用方法**

開発者が異なるセルに異なる書式スタイルを適用する必要がある場合は、[**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)メソッドを使用してセルの[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)を取得し、スタイル属性を指定してから、[**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)メソッドを使用して書式設定を適用するのが良いです。以下は、このアプローチを示す例です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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

            // Instantiate or load workbook
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
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
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

### **異なるセルのフォーマットにスタイルオブジェクトを使用する方法**

開発者が複数のセルに同じ書式スタイルを適用したい場合は、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトを使用できます。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトの使用手順は以下のとおりです。

1. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスの[**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--)メソッドを呼び出して、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトを追加します。
2. 新たに追加された[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトにアクセスします。
3. 望む書式設定を適用するために、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトのプロパティ/属性を設定します。
4. 設定済みの[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトを目的のセルに割り当てます。

このアプローチは、アプリケーションの効率を大幅に改善し、メモリも節約できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
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

### **Microsoft Excel 2007 の事前定義されたスタイルの使用方法**

Microsoft Excel 2007 に異なる書式スタイルを適用する必要がある場合、Aspose.Cells API を使用してスタイルを適用します。以下に、セルに事前定義されたスタイルを適用するこのアプローチをデモンストレーションするための例が示されています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **セル内の選択された文字の書式設定方法**

フォント設定の取り扱いは、セル内のテキストの書式設定方法について説明していますが、セルの内容全体の書式設定方法のみを説明しています。しかし、選択した文字のみを書式設定する場合はどうすればよいでしょうか？

Aspose.Cellsもこの機能をサポートしています。このトピックでは、その機能を効果的に使用する方法について説明します。

### **選択された文字の書式設定方法**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションの各要素は[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスは、セル内の文字列の範囲を選択するための[**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-)メソッドを提供し、以下のパラメータを取ります。

- **開始インデックス**、選択を開始する文字のインデックス。
- **文字数**、選択する文字数。

[**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-)メソッドは、開発者がセル内の文字列を形式設定できるようにする[**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)クラスのインスタンスを返します。コード例のように、出力ファイルのA1セルには「Visit」という単語はデフォルトのフォントでフォーマットされ、「Aspose!」は太字で青色で表示されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

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

{{% alert color="primary" %}}

セル内のリッチテキストの一部を書式設定したい場合は、[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) & [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)メソッドの使用を検討してください。[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--)メソッドはテキストの部分にアクセスし、変更は[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-)メソッドを通じて行えます。一方、**Get**メソッドは[**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)オブジェクトの配列を返し、これらを操作してフォント名、フォント色、太字などのさまざまなプロパティを設定できます。

{{% /alert %}}

## **行および列の書式設定方法**

時には、開発者は行または列に同じ書式を適用する必要があります。セルごとに書式を適用することは時間がかかるため、良い解決策ではありません。
この問題に対処するために、Aspose.Cells がこの記事で詳しく説明しているシンプルで高速な方法を提供します。

### **行および列の書式設定**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートへのアクセスを可能にする[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供し、[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションはさらに[**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--)コレクションを提供します。

### **行の書式設定方法**

[**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--)コレクションの各アイテムは[**Row**](https://reference.aspose.com/cells/javascript-cpp/row)オブジェクトを表します。[**Row**](https://reference.aspose.com/cells/javascript-cpp/row)オブジェクトは、行の書式設定に使用される[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)メソッドを提供します。同じ書式を行に適用するには、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトを使用します。以下にその使用方法を示します。

1. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスに[**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--)メソッドを呼び出して、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトを追加します。
2. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトのプロパティを設定して、書式設定を適用します。
3. relevant属性をONにします。
4. 設定済みの[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトを[**Row**](https://reference.aspose.com/cells/javascript-cpp/row)オブジェクトに割り当てます。

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

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
</html>
```

### **列のフォーマット方法**

[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションは、[**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--)コレクションも提供します。[**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--)コレクション内の各アイテムは[**Column**](https://reference.aspose.com/cells/javascript-cpp/column)オブジェクトを表します。[**Row**](https://reference.aspose.com/cells/javascript-cpp/row)オブジェクトと同様に、[**Column**](https://reference.aspose.com/cells/javascript-cpp/column)オブジェクトも列の書式設定に[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)メソッドを提供します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [位置合わせ設定](/cells/ja/javascript-cpp/cells-alignment-settings/)
- [境界線の設定](/cells/ja/javascript-cpp/cells-border-settings/)
- [ExcelおよびODSファイルの条件付き書式を設定します。](/cells/ja/javascript-cpp/conditional-formatting/)
- [Excelのテーマと色](/cells/ja/javascript-cpp/excel-themes-and-colors/)
- [塗りつぶしの設定](/cells/ja/javascript-cpp/cells-fill-settings/)
- [フォントの設定](/cells/ja/javascript-cpp/cells-font-settings/)
- [ワークブックのセルをフォーマットする](/cells/ja/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [1904年日付システムの実装](/cells/ja/javascript-cpp/implement-1904-date-system/)
- [セルの結合および解除](/cells/ja/javascript-cpp/merging-and-unmerging-cells/)
- [数値の設定](/cells/ja/javascript-cpp/cells-number-settings/)
- [セルのスタイルの取得および設定](/cells/ja/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
