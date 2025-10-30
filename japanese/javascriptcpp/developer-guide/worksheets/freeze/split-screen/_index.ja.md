---
title: JavaScriptを使用したC++によるExcelシートの分割表示
linktitle: 画面分割
type: docs
weight: 190
url: /ja/javascript-cpp/how-to-split-screen-of-excel-worksheet
description: この記事では、JavaScriptのC++アドオンを使用して、シートを2つまたは4つに分割し、特定の行または列を別のペインに表示する方法を学びます。
keywords: 最上行の固定、最上行の固定
---

## **紹介**

この記事では、大規模なデータセットを操作する際に、同じワークシートの異なる部分を比較するために、2つまたは4つに分割して表示する方法を学びます。分割表示機能はあなたのニーズに応えます。

## **Excelで画面を分割する方法**
ワークシートを2つまたは4つの部分に分割するには、次のようにします:

1. 分割を配置したい行/列/セルを選択します。
2. [表示]タブの[ウィンドウ]グループで、[分割]ボタンをクリックします。

**![画面分割](Split-Screen.png)**

## **列単位でワークシートを分割**

スプレッドシートの2つの領域を垂直に分割するには、分割を表示したい列の右側の列を選択し、Excelの[分割]ボタンをクリックします。

C++を用いたAspose.Cells for JavaScriptでワークシートを垂直に分割することは簡単です。最上部の行のいずれかのセルをアクティブセルとして選択し、[**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--)メソッドで分割します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets C1 cell in the top row as the active cell.
            sheet.activeCell = "C1";

            // Split worksheet vertically on columns
            sheet.split();

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **行単位でワークシートを分割**
Excelウィンドウを水平に分割するには、Excelで分割が発生する行の下の行を選択します。

C++を用いたAspose.Cells for JavaScriptで、左列のセルをアクティブにして横方向にワークシートを分割するのは簡単です。

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
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Sets A6 cell in the left column as the active cell.
            sheet.activeCell = "A6";

            // Split worksheet horizontally on rows
            sheet.split();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **ワークシートを4つの部分に分割する**
同じワークシートの4つの異なるセクションを同時に表示するには、Excelで画面を縦横に分割します。

C++を使ったAspose.Cells for JavaScriptで、最初の行と列以外のセルをアクティブに選択し、縦にワークシートを分割するのは簡単です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Active Cell and Split Worksheet Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets E6 cell as the active cell.
            sheet.activeCell = "E6";

            // Split worksheet into four parts
            sheet.split();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **分割を削除する方法**
ワークシートの分割を解除するには、再び分割ボタンをクリックします。

C++のAspose.Cells for JavaScriptは、分割設定を解除するための[**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--)メソッドを提供します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Worksheet Example</title>
    </head>
    <body>
        <h1>Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Remove split and then split worksheet into four parts
            sheet.removeSplit();
            sheet.split();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet split operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
