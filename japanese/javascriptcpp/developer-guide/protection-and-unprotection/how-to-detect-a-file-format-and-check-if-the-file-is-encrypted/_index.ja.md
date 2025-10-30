---
title: JavaScriptを使用したファイル形式の検出と、ファイルが暗号化されているかどうかを確認する方法（C++経由）
linktitle: ファイルフォーマットを検出してファイルが暗号化されているかどうかをチェックする方法
type: docs
weight: 2700
url: /ja/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Aspose.Cells for JavaScriptを使用したファイル形式の検出とファイルが暗号化されているかどうかを確認する方法（C++経由）
---

{{% alert color="primary" %}}  
ファイルの拡張子だけではファイル内容が適切であることを保証できないため、ファイルを開く前にファイル形式を検出する必要があります。ファイルは暗号化されている（パスワード保護された）場合もあり、そのまま読めないこともあります。Aspose.Cells for JavaScriptをC++で使用して、[**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-)静的メソッドや関連APIを利用してドキュメントを処理します。  
{{% /alert %}}  

次のサンプルコードは、ファイルパスを使用してファイルの形式を検出し、その拡張子をチェックし、ファイルが暗号化されているかどうかを判断する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells File Format Detection Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Detect file format
            const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(arrayBuffer));

            // Gets the detected load format (converted getter -> property)
            const extension = AsposeCells.FileFormatUtil.loadFormatToExtension(info.loadFormat);
            const encrypted = info.isEncrypted;

            console.log("The spreadsheet format is: " + extension);
            console.log("The file is encrypted: " + encrypted);

            resultDiv.innerHTML = `<p>The spreadsheet format is: <strong>${extension}</strong></p>
                                   <p>The file is encrypted: <strong>${encrypted}</strong></p>`;
        });
    </script>
</html>
```
