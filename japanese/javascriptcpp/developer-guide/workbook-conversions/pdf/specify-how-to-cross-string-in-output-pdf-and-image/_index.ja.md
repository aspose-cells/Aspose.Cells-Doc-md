---
title: JavaScriptを介して出力されたPDFおよび画像での文字列の交差方法を指定
linktitle: 出力PDFおよびイメージで文字列をクロスする方法を指定します。
type: docs
weight: 120
url: /ja/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: C++を使用して、出力PDF/画像内の文字のはみ出し制御を交差タイプを指定して学びます。
---

## **可能な使用シナリオ**

セルに文字列やテキストが含まれている場合、その文字列がセルの幅を超えると、次の列のセルがnullまたは空の場合に文字列がはみ出します。ExcelをPDF/画像に保存する際に、[**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype)列挙型を使用してこのはみ出しを制御できます。以下の値を持ちます：

- **TextCrossType.Default**：MS Excelのように次のセルに依存して文字列を表示。次のセルがnullの場合は文字列がはみ出すか切り詰められます。

- **TextCrossType.CrossKeep**：MS Excelのように文字列を表示し、PDFや画像にエクスポートします。

- **TextCrossType.CrossOverride**：文字列をすべて他のセルにまたがって表示し、また交差したセルのテキストを上書きします。

- **TextCrossType.StrictInCell**: セルの幅内で文字列のみを表示します。

## **TextCrossTypeを使用して出力PDF/イメージで文字列をクロスする方法を指定します。**

以下のサンプルコードは、サンプルのExcelファイルを読み込み、異なる[**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype)を指定してPDF／画像形式に保存します。サンプルExcelファイルと出力ファイルは以下のリンクからダウンロード可能です：

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### サンプルコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Cross Text Type to PDF and Image</title>
    </head>
    <body>
        <h1>Convert Excel to PDF and PNG (Text Cross Type)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkPdf" style="display: none; margin-right: 10px;">Download PDF</a>
            <a id="downloadLinkPng" style="display: none;">Download PNG</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, ImageOrPrintOptions, SheetRender, TextCrossType, Utils } = AsposeCells;

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
            const downloadLinkPdf = document.getElementById('downloadLinkPdf');
            const downloadLinkPng = document.getElementById('downloadLinkPng');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Clear previous links/messages
            downloadLinkPdf.style.display = 'none';
            downloadLinkPng.style.display = 'none';
            resultDiv.innerHTML = '';

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Initialize PDF save options
            const pdfSaveOptions = new PdfSaveOptions();
            // Set text cross type (converted setter -> property)
            pdfSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Save PDF file data
            const pdfData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            downloadLinkPdf.href = URL.createObjectURL(pdfBlob);
            downloadLinkPdf.download = 'outputCrosssType.pdf';
            downloadLinkPdf.style.display = 'inline-block';
            downloadLinkPdf.textContent = 'Download PDF File';

            // Initialize image or print options
            const imageSaveOptions = new ImageOrPrintOptions();
            // Set text cross type (converted setter -> property)
            imageSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Initialize sheet renderer for first worksheet
            const sheetRenderer = new SheetRender(workbook.worksheets.get(0), imageSaveOptions);

            // Render the first page/image of the sheet to image data
            const imageData = sheetRenderer.toImage(0);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            downloadLinkPng.href = URL.createObjectURL(imageBlob);
            downloadLinkPng.download = 'outputCrosssType.png';
            downloadLinkPng.style.display = 'inline-block';
            downloadLinkPng.textContent = 'Download PNG File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Download links are ready.</p>';
        });
    </script>
</html>
```
