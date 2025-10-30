---
title: JavaScript経由でC++を使用してXLSBのリビジョンをXLSMに変換
linktitle: XLSBのリビジョンをXLSMに変換する
type: docs
weight: 290
url: /ja/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Aspose.Cells for JavaScriptを使用してXLSBファイルのリビジョンをXLSM形式に完全変換する方法を学習します。
---

{{% alert color="primary" %}}

Aspose.Cellsは現在、XLSBファイルのリビジョンを完全にXLSMファイルに変換することをサポートしています。リビジョンは\xl\revisionsパス内にあります。拡張子をZIPに変更することで閲覧できます。\xl\revisions パスには .bin 拡張子のファイルが含まれています。

Aspose.Cellsを使用してXLSBファイルをXLSMに変換した際、これらの .bin ファイルは正常に .xml ファイルに変換されることが、これら2つのスクリーンショットで示されています。

{{% /alert %}}

 以下のコード例は、C++経由でAspose.Cells for JavaScriptを使ってXLSBファイルをXLSM形式に変換する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
