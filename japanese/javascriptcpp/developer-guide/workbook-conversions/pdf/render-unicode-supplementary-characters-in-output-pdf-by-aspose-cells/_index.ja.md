---
title: Aspose.Cells for JavaScriptを使用して、出力PDFでUnicode補助文字をレンダリング
linktitle: Aspose.Cells による出力PDFでUnicode補助文字をレンダリングする
type: docs
weight: 350
url: /ja/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aspose.Cells for JavaScriptを使用して、出力PDFでUnicode補助文字をレンダリングする方法を学びます。 
---

{{% alert color="primary" %}}

通常のUnicode文字は2バイトであり、Unicode補助文字は4バイトです。Aspose.Cells はこれらの4バイトのUnicode文字のレンダリングをサポートしています。

Unicode文字標準では、補助文字はU+10000からU+10FFFFまでのコードポイントが割り当てられています。つまり、これらはU+FFFFよりも大きいUnicode文字です。

- UTF-8では、これらの文字はそれぞれ4バイトです。
- UTF-16では、これらの文字は2つのサロゲート（16ビットユニット）が必要です。

{{% /alert %}}

## Aspose.Cells for JavaScriptによる出力PDFへのUnicode補助文字のレンダリング

以下のスクリーンショットは、Aspose.Cellsが[source excel file](5115563.xlsx)を[output PDF](5115564.pdf)にレンダリングした様子を示しています。すべてのUnicode補助字符がMicrosoft Excelと同じように正確にレンダリングされているのがわかります。

![todo:image_alt_text](output.png)

## サンプルコード

[ソースExcelファイル](5115563.xlsx)を[出力PDF](5115564.pdf)に変換するためのサンプルコードを使用できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Unicode Supplementary Characters to PDF</title>
    </head>
    <body>
        <h1>Render Unicode Supplementary Characters to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenderUnicodeInOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
