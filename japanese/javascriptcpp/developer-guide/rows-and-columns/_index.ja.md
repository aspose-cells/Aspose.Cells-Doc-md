---
title: JavaScriptをC++経由で行と列の書式設定
linktitle: 行と列
type: docs
weight: 100
url: /ja/javascript-cpp/adjusting-row-height-and-column-width/
description: C++を使用したAspose.Cells for JavaScriptは、行の高さや列幅の変更、行や列へのフォーマット適用をサポートします。
keywords: 行の高さと列の幅を設定し、行の高さと列の幅を調整し、行の高さや列の幅を変更し、行と列の書式を設定する方法
---

{{% alert color="primary" %}}
スプレッドシートで行や列にデータを追加する際、行の高さや列の幅を変更する必要がある場合があります。時には、行や列に書式を適用するときに、現在の高さや幅を変えてデータを見やすくすることもあります。通常、Microsoft ExcelのWYSIWYG環境で行高や列幅を調整しますが、Aspose.Cellsを用いると、Runtime中にこれらの操作を行うことができます。
{{% /alert %}}

## **行で操作する**

### **行の高さの調整方法**

C++経由のAspose.Cells for JavaScriptは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)があります。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシート内のすべてのセルを表す[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションを提供します。

[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションは、ワークシート内の行や列を管理するための複数のメソッドを提供します。以下に詳細を説明します。

### **行の高さを設定する方法**

単一の行の高さを設定するには、[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの[**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-)メソッドを呼び出します。[**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-)メソッドは次のパラメータを取ります：

- **行インデックス**：高さを変更する行のインデックス。
- **行の高さ**：行に適用する行の高さ。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Row Height Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.rows.get(1).height = 13;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **ワークシート内のすべての行の高さを設定する方法**

全ての行の同じ高さを設定したい場合は、[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの[**standardHeight()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardHeight--)プロパティを使用して行えます。



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Standard Row Height</title>
    </head>
    <body>
        <h1>Set Standard Row Height Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the height of all rows in the worksheet to 15
            worksheet.cells.standardHeight = 15;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Standard row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **列で操作する**

### **列の幅を設定する方法**

列の幅を設定するには、[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの[**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-)メソッドを呼び出します。[**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-)メソッドは次のパラメータを取ります：

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**：設定したい列の幅。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Column Width Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Set Column Width</button>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of the second column to 17.5
            worksheet.cells.columns.get(1).width = 17.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **ピクセル単位で列幅を設定する方法**

列の幅を設定するには、[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの[**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-)メソッドを呼び出します。[**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-)メソッドは次のパラメータを取ります：

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**、ピクセル単位での所望の列の幅。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Column Width In Pixels</title>
    </head>
    <body>
        <h1>Set Column Width In Pixels</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the width of the column in pixels
            // Converted from: worksheet.getCells().setColumnWidthPixel(7, 200);
            // UNIVERSAL GETTER/SETTER CONVERSION applied:
            worksheet.cells.columnWidthPixel = [7, 200];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetColumnWidthInPixels_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **ワークシート内のすべての列の幅を設定する方法**

全列に対して同じ幅を設定したい場合は、[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションの[**standardWidth()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardWidth--)プロパティを使用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Standard Width Example</title>
    </head>
    <body>
        <h1>Set Standard Width Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of all columns in the worksheet to 20.5
            worksheet.cells.standardWidth = 20.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Standard width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [行と列の自動調整](/cells/ja/javascript-cpp/autofit-rows-and-columns/)
- [Aspose.Cellsを使用したテキストを列に変換する](/cells/ja/javascript-cpp/convert-text-to-columns-using-aspose-cells/)
- [行と列のコピー](/cells/ja/javascript-cpp/copying-rows-and-columns/)
- [ワークシート内の空白の行と列を削除](/cells/ja/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/)
- [行と列のグループ化および解除](/cells/ja/javascript-cpp/grouping-and-ungrouping-rows-and-columns/)
- [行と列の非表示および表示](/cells/ja/javascript-cpp/hiding-and-showing-rows-and-columns/)
- [Excelワークシートに行を挿入または削除](/cells/ja/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excelファイルの行と列の挿入と削除](/cells/ja/javascript-cpp/inserting-and-deleting-rows-and-columns/)
- [ワークシート内の重複する行を削除する](/cells/ja/javascript-cpp/remove-duplicate-rows-in-a-worksheet/)
- [ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する](/cells/ja/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
