---
title: JSONをExcelに変換するにはC++経由のJavaScriptを使用
linktitle: JSONをExcelに変換します。
type: docs
weight: 300
url: /ja/javascript-cpp/convert-json-to-excel/
description: JSONをExcelファイルに変換する方法を学びましょう。
keywords: JavaScript経由のC++を使用したOffice 2013、2016、2019、365なしでのJSONのインポート。
---

{{% alert color="primary" %}}

Aspose.Cellsは、JSON（JavaScript Object Notation）ファイルをExcelブックに変換することをサポートしています。

{{% /alert %}}

## **JSONをExcelワークブックに変換する**
JSONをExcelファイルに変換する方法を知る必要はありません。Aspose.Cells for JavaScript via C++が最良の解決策を提供します。Aspose.Cells APIはJSONフォーマットをスプレッドシートに変換するサポートを提供します。追加設定には[**JsonLoadOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonloadoptions)クラスを使用できます。

以下のコード例は、JSONをExcelワークブックにインポートする方法を示しています。コードで生成されたxlsxファイルへの変換のために、[source file](sample.json)を参照してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Convert JSON to XLSX</h1>
        <input type="file" id="fileInput" accept=".json" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // create a Workbook object from uploaded file (JSON)
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // save file to xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the XLSX file.</p>';
        });
    </script>
</html>
```

次のコード例は、JsonLoadOptionsクラスを使用して追加設定を指定し、JSONをExcelブックにインポートする例です。参考のため、ソースファイル([sample.json])をコードで変換し、生成されたxlsxファイルを確認してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Load JSON into Workbook and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".json" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an options of loading the file.
            const options = new JsonLoadOptions();
            options.multipleWorksheets = true;

            // Loads the workbook from JSON file
            const book = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save file to xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

次のコード例は、JSON文字列をExcelブックにインポートする例です。また、JSONをインポートするときのレイアウトの場所も指定できます。参考のため、JSON文字列をxlsxファイルに変換するコードを確認してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Import JSON as Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLayoutOptions, JsonUtility, Utils } = AsposeCells;

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

        // Converted logic from JavaScript to browser-compatible code
        const inputJson = JSON.stringify([
            { BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
        ]);
        const sheetName = "Sheet1";
        const row = 3;
        const column = 2;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a Workbook object
            const book = new Workbook();
            const worksheet = book.worksheets.get(sheetName);

            // set JsonLayoutOptions to treat Arrays as Table
            const jsonLayoutOptions = new JsonLayoutOptions();
            jsonLayoutOptions.arrayAsTable = true;

            // Import JSON data into worksheet cells at specified row and column
            AsposeCells.JsonUtility.importData(inputJson, worksheet.cells, row, column, jsonLayoutOptions);

            // Save file to xlsx format and prepare download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">JSON imported as table and file generated. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
