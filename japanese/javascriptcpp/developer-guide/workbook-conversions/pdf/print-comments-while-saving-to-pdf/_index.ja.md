---
title: コメントを印刷しながらPDFに保存する方法（JavaScript経由のC++）
linktitle: PDFへ保存する際にコメントを印刷する
type: docs
weight: 10
url: /ja/javascript-cpp/print-comments-while-saving-to-pdf/
description: ExcelドキュメントをPDFに保存する際にコメントを印刷する方法を学ぶ（Aspose.Cells for JavaScriptを使用してC++経由）
---

{{% alert color="primary" %}}  

Microsoft Excelでは、印刷またはPDF形式への保存時にコメントを印刷する機能が以下のオプションで提供されています  

- なし  
- シートの末尾  
- シートに表示されている通り  

Aspose.Cellsは、同じ機能をサポートするために[**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)列挙型を提供します。[**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)列挙型には次のメンバーがあります  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **PDFへ保存する際にコメントを印刷する**  

次のサンプルコードは、コメントを印刷してPDFに保存する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Print Comments to PDF</title>
    </head>
    <body>
        <h1>Print Comments While Saving to PDF Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.pageSetup.printComments = AsposeCells.PrintCommentsType.PrintSheetEnd;

            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PrintCommentWhileSavingToPdf_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to PDF with comments printed at sheet end. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
