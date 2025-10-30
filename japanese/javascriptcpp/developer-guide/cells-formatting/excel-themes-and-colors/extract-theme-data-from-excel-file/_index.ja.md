---
title: Excelファイルからテーマデータを抽出する
linktitle: Excelファイルからテーマデータを抽出する
description: C++経由でAspose.Cells for JavaScriptを使用して、Excelファイルからテーマデータを抽出する方法を学びます。スタイルと書式情報を効果的に取得します。
keywords: Aspose.Cells、Excelファイル、テーマデータ、スタイル、フォーマット、JavaScript via C++
type: docs
weight: 120
url: /ja/javascript-cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、Excelファイルからテーマ関連のデータを抽出することができます。たとえば、ワークブックに適用されているテーマ名や、セルまたはその境界に適用されているテーマカラーなどを抽出できます。

Microsoft Excelを使用してワークブックにテーマを適用できます。[ページレイアウト] > [テーマ]コマンドを使用します。

{{% /alert %}}

## Excelファイルからテーマデータを抽出するJavaScriptコード

次のサンプルコードは、ソースブックに適用されたテーマ名を抽出し、その後、セルA1に適用されたテーマカラーとセルの下線のテーマカラーを抽出します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; }
            #result p { margin: 6px 0; }
        </style>
    </head>
    <body>
        <h1>Aspose.Cells Theme & Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, Utils } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Extract theme name applied to this workbook
            const themeName = workbook.theme;
            resultDiv.innerHTML += `<p>Workbook theme: ${themeName}</p>`;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Get the style object
            const style = cell.style;

            if (style.foregroundThemeColor != null) {
                // Extract theme color applied to this cell if theme has foreground theme color defined
                const fgColorType = style.foregroundThemeColor.colorType;
                resultDiv.innerHTML += `<p>Foreground theme color type: ${fgColorType}</p>`;
            } else {
                resultDiv.innerHTML += `<p>Theme has not foreground color defined.</p>`;
            }

            // Extract theme color applied to the bottom border of the cell if theme has border color defined
            const bot = style.borders.get(BorderType.BottomBorder);
            if (bot.themeColor != null) {
                const botColorType = bot.themeColor.colorType;
                resultDiv.innerHTML += `<p>Bottom border theme color type: ${botColorType}</p>`;
            } else {
                resultDiv.innerHTML += `<p>Theme has not Border color defined.</p>`;
            }

            // No file is produced here, but keep download link hidden
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            downloadLink.href = '#';
            downloadLink.textContent = '';
        });
    </script>
</html>
```
