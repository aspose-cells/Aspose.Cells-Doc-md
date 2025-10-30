---
title: ExcelをPDFにレンダリングする際にスライサーを描画する
type: docs
weight: 60
url: /ja/javascript-cpp/draw-slicer-while-rendering-excel-to-pdf/
---

## **ExcelをPDFにレンダリングする際にスライサーを描画する**
スライサーが適用されたExcelファイルを持っていて、スライサー設定を保持したままExcelをPDFにエクスポートしたい場合、Aspose.Cells for JavaScriptをC++で使用してこれを標準でサポートします。スライサーを付けてExcelファイルをエクスポートすると、生成されたPDFにスライサーの設定が反映されます。

次のサンプルコードは、既存のスライサーが含まれる[sample Excelファイル](94044165.xlsx)を読み込みます。その後、ワークブックを[output PDFファイル](94044166.pdf)として保存します。次のスクリーンショットは、元のExcelファイルと生成されたPDFファイルを比較しています。

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **サンプルコード**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as PDF</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleSlicerChart.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
