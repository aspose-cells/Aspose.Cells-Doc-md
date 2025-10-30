---
title: JavaScriptを使用してC++でExcelをPDFにレンダリングしながらタイムラインを描画
linktitle: ExcelをPDFにレンダリングする際のタイムラインの描画
type: docs
weight: 60
url: /ja/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: C++を使用してExcelファイルのタイムラインを管理
keywords: Office 2013、Office 2016、Office 2019、Office 365を使わずにJavaScriptを介してC++でタイムラインをPDFに変換
---

## **ExcelをPDFにレンダリングする際のタイムラインの描画**
タイムラインが適用されたExcelファイルを持っていて、そのタイムライン設定を保持したままExcelをPDFにエクスポートしたい場合、Aspose.Cells for JavaScriptはこの機能を標準でサポートしています。タイムラインを含むExcelファイルをPDFにエクスポートすると、生成されたPDFにタイムラインが正しく表示されます。

以下のサンプルコードは、既存のタイムラインを含む[サンプルExcelファイル](input.xlsx)をロードします。その後、ワークブックを[出力PDFファイル](out.pdf)として保存します。以下のスクリーンショットは、ソースのExcelファイルと生成されたPDFファイルを比較したものです。

<img src="out.png" width="60%">

## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
