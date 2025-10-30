---
title: CSVをJavaScript経由のC++でJSONに変換
linktitle: CSVをJSONに変換
type: docs
weight: 220
url: /ja/javascript-cpp/convert-csv-to-json/
description: C++ APIを使用して、CSVファイルをJSONに変換します。
keywords: CSVをJSONに変換、CSVからJSONへ変換、CSV、JSON、C++でCSVをJSONに変換するコード例。
---

## **CSVをJSONに変換**

Aspose.CellsはCSVからJSONへの変換をサポートしています。このため、APIは[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/)クラスを提供します。[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/)クラスはエクスポート範囲をJSONに設定するオプションを提供し、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/)クラスには以下のプロパティがあります。

- [**ExportRangeToJsonOptions.exportAsString**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#exportAsString--): セルの文字列値をJSONにエクスポートします。
- [**ExportRangeToJsonOptions.hasHeaderRow**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#hasHeaderRow--): これが範囲にヘッダ行が含まれるかどうかを示します。
- [**ExportRangeToJsonOptions.indent**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#indent--): インデントを示します。

[**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/)クラスは、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/)クラスで設定されたエクスポートオプションを使用してJSONを出力します。

次のコード例は、[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/)および[**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/)クラスを使用して[ソースCSVファイル](104398879.csv)を読み込み、JSON出力をコンソールに表示します。

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Export CSV Range to JSON Example</title>
    </head>
    <body>
        <h1>Export CSV Range to JSON Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Export to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, JsonSaveOptions, JsonUtility } = AsposeCells;

        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            runButton.disabled = false;
        });

        function escapeHtml(unsafe) {
            return unsafe
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            downloadLink.href = '';
            downloadLink.textContent = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions = new LoadOptions(LoadFormat.Csv);
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            const worksheet = workbook.worksheets.get(0);
            const lastCell = worksheet.cells.lastCell;

            const jsonSaveOptions = new JsonSaveOptions();
            const range = worksheet.cells.createRange(0, 0, lastCell.row + 1, lastCell.column + 1);
            const data = JsonUtility.exportRangeToJson(range, jsonSaveOptions);

            // Display JSON in the result div
            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully!</p><pre>' + escapeHtml(data) + '</pre>';

            // Create a downloadable JSON file
            const blob = new Blob([data], { type: 'application/json' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'exported_range.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';
        });
    </script>
</html>
```

### **コンソール出力**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
