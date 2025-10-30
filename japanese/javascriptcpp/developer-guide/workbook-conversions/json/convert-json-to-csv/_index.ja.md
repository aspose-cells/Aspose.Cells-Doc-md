---
title: JSONをCSVに変換するにはC++経由のJavaScriptを使用
linktitle: JSONをCSVに変換する
type: docs
weight: 210
url: /ja/javascript-cpp/convert-json-to-csv/
description: C++経由のAspose.Cells for JavaScriptを使用してJSONデータをCSVに変換する方法を学びましょう。
---

## **JSONをCSVに変換**

Aspose.Cells for JavaScriptは簡単なJSONだけでなくネストされたJSONもCSVに変換可能です。そのためのAPIは[**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions)と[**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility)クラスを提供します。[**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions)クラスは[**JsonLayoutOptions.arrayAsTable**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions/#arrayAsTable--)（配列を表に処理）など、JSONレイアウトのオプションを提供します。[**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility)クラスは[**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions)クラスで設定されたレイアウトオプションを使用してJSONを処理します。

次のコード例では、[**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions)および[**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility)クラスを使用して[ソースJSONファイル](104398869.json)を読み込み、[出力CSVファイル](104398870.csv)を生成します。

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells JSON to CSV Example</title>
    </head>
    <body>
        <h1>Import JSON to CSV Example</h1>
        <input type="file" id="fileInput" accept=".json" />
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const jsonText = await file.text();

            // Create empty workbook
            const workbook = new Workbook();

            // Get Cells from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Set JsonLayoutOptions
            const importOptions = new JsonLayoutOptions();
            importOptions.convertNumericOrDate = true;
            importOptions.arrayAsTable = true;
            importOptions.ignoreTitle = true;

            // Import JSON data into worksheet cells starting at A1 (0,0)
            JsonUtility.importData(jsonText, cells, 0, 0, importOptions);

            // Save Workbook as CSV
            const outputData = workbook.save(SaveFormat.Csv);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleJson_out.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            resultDiv.innerHTML = '<p style="color: green;">JSON imported and CSV prepared. Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```
