---
title: エラーを無視してExcelからPDFへのレンダリングを行う方法を学ぶ（C++経由のAspose.Cells for JavaScriptを使用）
linktitle: Excel を PDF にレンダリングする際のエラーを無視
type: docs
weight: 80
url: /ja/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: ExcelファイルをPDFに変換する際にエラーを無視する方法を学ぶ（C++経由のAspose.Cells for JavaScriptを使用）
---

## **可能な使用シナリオ**  

時にはExcelファイルをPDFに変換する際にエラーや例外が発生し、変換処理が終了することがあります。こうしたエラーをすべて無視したい場合は、[**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--)プロパティを利用してください。これにより、変換はエラーや例外なしでスムーズに完了しますが、データの損失が生じる可能性があります。  

## **Excel を PDF にレンダリングする際のエラーを無視**  

以下のコードは、[サンプルExcelファイル](55541778.xlsx)を読み込みますが、これはエラーがあり、[PDFへの変換](55541779.pdf)の際に17.11のバージョンでエラーが発生します。ただし、[**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--)プロパティを使用しているためエラーはスローされません。しかし、このスクリーンショットに示すような丸い赤い矢印型のシェイプは失われます。  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
