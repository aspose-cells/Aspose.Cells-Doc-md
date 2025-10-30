---
title: One PDFページを各Excelワークシートごとにレンダリング  JavaScript経由のC++によるExcelからPDF変換
linktitle: Excelワークシートごとに1つのPDFページをレンダリングする  ExcelからPDFへの変換
type: docs
weight: 100
url: /ja/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

大きなMicrosoft Excelファイル（たとえば、複数のシートがあり、それぞれに50列と300行以上のデータがあるブック）を扱う場合、ワークシートのサイズに関わらず、PDF出力に各ワークシートごとに1ページ表示させたいことがあります。これは、各ページのサイズが大きく異なる可能性があることを意味します。これは、Aspose.Cells for JavaScriptを使用してC++で実現できます。

{{% /alert %}}

複数のワークシートを持つExcelファイルをPDFに変換するサンプルコードをご確認ください。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Convert Excel to PDF (One Page Per Worksheet)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement one page per worksheet option
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.onePagePerSheet = true;

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

[PdfSaveOptions.onePagePerSheet](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--)オプションを**true**に設定すると、すべてのシートの内容が1つのPDFページにレンダリングされます。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、PDFにレンダリングする直前に[Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)を呼び出すのが最善です。これにより、数式に依存する値が再計算され、正しい値がPDFに表示されることが保証されます。

{{% /alert %}}
