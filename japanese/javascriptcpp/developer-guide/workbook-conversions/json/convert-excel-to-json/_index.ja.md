---
title: JavaScript経由のC++でExcelをJSONに変換
linktitle: ExcelをJSONに変換
type: docs
weight: 300
url: /ja/javascript-cpp/convert-excel-to-json/
description: C++を使用してExcelファイルをJSONに変換する方法を学びます。
keywords: ExcelワークブックをJSON JavaScript経由でC++でエクスポート
---

{{% alert color="primary" %}}  
Aspose.Cellsは、WorkbookをJSON（JavaScript Object Notation）ファイルに変換することをサポートしています。  
{{% /alert %}}  

## **ExcelワークブックをJSONに変換**  

ExcelワークブックをJSONに変換する方法を知る必要はありません。なぜなら、Aspose.Cells for JavaScript via C++ライブラリが最良の解決策を提供しているからです。Aspose.Cells APIはスプレッドシートをJSONフォーマットに変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)メソッドの第二引数として[**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/)を渡してください。また、[**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions/)クラスを使用して、ワークシートをJSONにエクスポートする追加設定を指定することも可能です。  

以下のコード例は、ExcelワークブックをJSONにエクスポートする例です。変換されたJSONファイルは、[ソースファイル](sample.xlsx)をコードにより変換した結果を参考にしてください。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Convert the workbook to JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to JSON completed. Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```  

以下のコード例は、JsonSaveOptionsクラスを使用して追加設定を指定し、ExcelワークブックをJSONにエクスポートする例です。変換されたJSONファイルは、[ソースファイル](sample.xlsx)をコードにより変換した結果を参考にしてください。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, JsonSaveOptions, Utils } = AsposeCells;

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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an options of saving the file.
            const options = new JsonSaveOptions();

            // Set the exporting range.
            options.exportArea = CellArea.createCellArea("B1", "C4");

            // Convert the workbook to json file.
            const outputData = workbook.save(SaveFormat.Json, options);

            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```
