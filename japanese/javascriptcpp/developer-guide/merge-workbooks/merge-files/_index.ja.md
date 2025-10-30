---
title: JavaScriptを通じてC++でファイルを結合
linktitle: ファイルの結合
type: docs
weight: 20
url: /ja/javascript-cpp/merge-files/
---

## **紹介**

Aspose.Cellsはファイルのマージにさまざまな方法を提供しています。データ、書式設定、数式を含むシンプルなファイルには [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) 方法が複数のブックを結合するのに適しており、[**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-) 方法はシートを新しいブックにコピーするのに適しています。これらの方法は使いやすく効果的ですが、多数のファイルをマージする場合、システムリソースを大量に使用することがあります。これを避けるために、より効率的な [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-) 静的メソッドを使用します。

## **Merge Files Using Aspose.Cells for JavaScript via C++**

以下のサンプルコードは、[**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-) メソッドを使用して大きなファイルをマージする例です。Book1.xlsとBook2.xlsの2つの大きなファイルを対象とし、それらには書式設定済みのデータと数式のみが含まれています。

{{% alert color="primary" %}}

[**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-)メソッドは、データ、スタイル、書式、数式の結合のみをサポートしています。チャート、図、コメントなどのオブジェクトは、このメソッドを使用して結合することはできません。さらに、一時的なデータを処理するためのキャッシュファイルが使用されます。

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Excel Files and Rename Sheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" multiple />
        <button id="runExample">Merge and Rename Sheets</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            if (!fileInput.files.length || fileInput.files.length < 2) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least two Excel files to merge.</p>';
                return;
            }

            // Read selected files into Uint8Array array
            const files = [];
            for (let i = 0; i < fileInput.files.length; i++) {
                const file = fileInput.files[i];
                const arrayBuffer = await file.arrayBuffer();
                files.push(new Uint8Array(arrayBuffer));
            }

            // Create cacheFile name and destination name (virtual in browser)
            const cacheFile = "test.txt";
            const dest = "output.xlsx";

            // Call CellsHelper.mergeFiles with file byte arrays, cacheFile name and destination name
            // Note: In the browser environment mergeFiles is expected to accept file byte arrays and return merged file bytes.
            const mergedData = CellsHelper.mergeFiles(files, cacheFile, dest);

            // Log cacheFile as in original code
            console.log(cacheFile);

            // Load the merged workbook from returned bytes
            const workbook = new Workbook(new Uint8Array(mergedData));

            // Rename sheets sequentially starting at 1
            let i = 1;
            const worksheets = workbook.worksheets;
            for (let j = 0; j < worksheets.count; j++) {
                worksheets.get(j).name = `Sheet1${i}`;
                i++;
            }

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Merged and Renamed Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Files merged and sheets renamed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
