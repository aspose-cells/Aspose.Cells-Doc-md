---
title: JavaScriptとC++を使用したJSON
linktitle: Json
type: docs
weight: 300
url: /ja/javascript-cpp/convert-workbook-to-json/
description: ExcelワークブックをJSONに変換する方法をAspose.Cells for JavaScript via C++で学びましょう。
---

{{% alert color="primary" %}}
Aspose.Cellsは、ワークブックをJson（JavaScript Object Notation）ファイルに変換することをサポートしています。
{{% /alert %}}

## **ExcelワークブックをJSONに変換**

Aspose.Cells APIは、スプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-)メソッドの第2引数として[**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat)を渡します。さらに、[**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions)クラスを使用してワークシートのエクスポート設定を追加で指定することも可能です。

次のコード例では、[**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json)列挙型メンバーを使用してアクティブなワークシートをJSONにエクスポートする方法を示しています。ソースファイル（book1.xlsx）をコードで変換し、出力されるJsonファイル（book1.Json）を参照してください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [CSVをJSONに変換](/cells/ja/javascript-cpp/convert-csv-to-json/)
- [ExcelをJSONに変換する](/cells/ja/javascript-cpp/convert-excel-to-json/)
- [JSONをCSVに変換](/cells/ja/javascript-cpp/convert-json-to-csv/)
- [JSONをExcelに変換する](/cells/ja/javascript-cpp/convert-json-to-excel/)
