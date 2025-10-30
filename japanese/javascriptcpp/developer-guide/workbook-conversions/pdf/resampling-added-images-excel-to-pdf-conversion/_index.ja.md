---
title: 画像のリサンプリング  JavaScript経由のC++によるExcelからPDFへの変換
linktitle: 画像のリサンプリング
type: docs
weight: 150
url: /ja/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Excelファイルに追加された画像を圧縮してPDFサイズを縮小し、変換パフォーマンスを向上させる方法をAspose.Cells for JavaScriptを使用して学びます。
---

{{% alert color="primary" %}}

多くの画像が含まれる大きなMicrosoft Excelファイルを扱う際、PDF出力ファイルのサイズを減らし、全体の変換性能を向上させるために、追加された画像を圧縮する必要がある場合があります。Aspose.Cells for JavaScriptは、リサンプリングによって出力PDFのファイルサイズを縮小し、パフォーマンスをやや向上させることをサポートしています。

{{% /alert %}}

Aspose.Cells APIを使用してタスクを実行する方法を説明する以下のサンプルコードをご覧ください。この例では、Microsoft ExcelファイルをPDFファイルに変換しながら、ファイル内の画像を圧縮しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set Image Resample properties (converted from setImageResample(300, 70))
            // Universal setter->property conversion: setImageResample(...) -> imageResample = [...]
            pdfSaveOptions.imageResample = [300, 70];

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out_pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

[**imageResample(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#imageResample-number-number-)オプションを使用すると、出力PDFのサイズを最小限に抑えることができますが、画像の品質には少し影響を与える可能性があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
