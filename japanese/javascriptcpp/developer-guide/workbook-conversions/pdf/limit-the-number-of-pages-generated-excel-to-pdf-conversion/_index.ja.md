---
title: ページ数の制限を設ける  ExcelからPDFへの変換（C++経由のJavaScript使用）
linktitle: 生成されるページ数を制限  Excel を PDF に変換
type: docs
weight: 180
url: /ja/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: ExcelスプレッドシートをPDFに変換したときに生成されるページ数を制限する方法を学ぶ（C++経由のAspose.Cells for JavaScriptを使用） 
---

{{% alert color="primary" %}}

出力PDFファイルに特定のページ範囲を印刷したい場合があります。C++経由のAspose.Cells for JavaScriptは、ExcelスプレッドシートをPDFフォーマットに変換する際のページ数制限を設定する機能を持ちます。

{{% /alert %}}

## **生成されるページ数の制限**

次の例では、Microsoft Excelファイルのページ3と4をPDFにレンダリングする方法が示されています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Export Example</title>
    </head>
    <body>
        <h1>Export Specific Pages to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Open an Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOption
            const options = new PdfSaveOptions();

            // Print only Page 3 and Page 4 in the output PDF
            // Starting page index (0-based index)
            options.pageIndex = 3;
            // Number of pages to be printed
            options.pageCount = 2;

            // Save the PDF file
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPDF1.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、PDFにレンダリングする直前に[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)を呼び出すのが最良です。これにより、数式依存の値が再計算され、正しい値が出力ファイルにレンダリングされます。

{{% /alert %}}
