---
title: ハイパーリンクタイプの検出
type: docs
weight: 160
url: /ja/javascript-cpp/detect-hyperlink-type/
description: ハイパーリンクのタイプを検出する方法をAspose.Cells for JavaScript経由のC++ APIを使って学びます。
keywords: ハイパーリンクの種類をJavaScriptで検出、JavaScriptでハイパーリンクのタイプを検出、JavaScriptでハイパーリンクのタイプを取得。
---

## **ハイパーリンクのタイプの検出**

Excelファイルには外部リンク、セル参照、ファイルパスなどさまざまなハイパーリンクの種類があります。Aspose.Cells for JavaScriptを使えば、ハイパーリンクの種類を検出できます。種類は[**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype)列挙体で表され、[**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype)列挙体には以下のメンバーがあります。

- 外部：外部リンク
- ファイルパス：ファイル/フォルダへのローカルおよび完全パス。
- Eメール：メールアドレス
- セル参照：セルまたは名前付き範囲へのリンク

ハイパーリンクの種類を確認するには、[**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink)クラスの[**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--)プロパティを使用し、その返り値の型は[**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype)です。以下のコードスニペットは、この[ソースExcelファイル](94896195.xlsx)を使った[**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--)プロパティの使用例を示しています。

### ソースコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


上記のコードスニペットによって生成された出力は以下の通りです。

コンソール出力
