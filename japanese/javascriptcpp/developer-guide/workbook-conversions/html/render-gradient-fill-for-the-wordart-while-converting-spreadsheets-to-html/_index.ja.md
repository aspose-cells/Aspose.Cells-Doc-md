---
title: JavaScriptを使用してC++でスプレッドシートをHTMLに変換するときにグラデーション塗りつぶしをレンダリングする
linktitle: スプレッドシートをHTMLに変換する際のWordArtのグラデーションフィルをレンダリング
type: docs
weight: 90
url: /ja/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Aspose.Cells for JavaScriptを使用してC++でスプレッドシートをHTMLに変換するときにWordArtのグラデーション塗りつぶしをレンダリングする方法を学習します。
---

## **可能な使用シナリオ**  
Aspose.Cells 17.1以前は、ExcelファイルをHTML形式に変換した際にWordArtのグラデーション塗りつぶしをレンダリングしませんでした。Aspose.Cells 17.1以降は、WordArtのグラデーション塗りつぶしがサポートされました。以下のスクリーンショットは、Aspose.Cells 17.1と旧バージョンを使用してExcelファイルを変換した際のグラデーション塗りつぶしの効果を比較したものです。  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **スプレッドシートをHTMLに変換する際のWordArtのグラデーションフィルをレンダリング**  
以下のサンプルコードは、[ソースExcelファイル](22774111.xlsx)を[出力HTML形式](22774109.zip)に変換します。ソースExcelファイルには、上記スクリーンショットのようなグラデーション塗りつぶしのWordArtオブジェクトが含まれています。  

## **サンプルコード**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
