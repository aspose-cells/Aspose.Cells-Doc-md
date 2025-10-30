---
title: JavaScriptを使ってC++経由でPDFにエクスポート時にドキュメント構造をエクスポートする
linktitle: PDF への変換時にドキュメント構造をエクスポート
type: docs
weight: 360
url: /ja/javascript-cpp/export-document-structure-while-converting-to-pdf/
description: C++経由のAspose.Cells for JavaScriptを使用して、Excelファイルをタグ付きPDFに変換しながらドキュメント構造をエクスポートする方法を学ぶ。
---

PDFの論理構造機能は、ドキュメント内容の構造に関する情報をPDFファイルに組み込む仕組みを提供します。C++経由のAspose.Cells for JavaScriptは、セル、行、テーブル、ワークシート、画像、図形、ヘッダー/フッターなど、Microsoft Excelドキュメントの構造情報を保持します。

オプション[PfdSaveOptions.exportDocumentStructure()](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#exportDocumentStructure--)を使用して、エクスポートされたドキュメント構造を持つタグ付きPDFとして保存できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export PDF with Document Structure</title>
    </head>
    <body>
        <h1>Export PDF with Document Structure</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set to export document structure.
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.exportDocumentStructure = true;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF exported successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
