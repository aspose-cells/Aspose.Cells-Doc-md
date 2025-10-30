---
title: ExcelからHTMLへの変換時にDataBar、ColorScale、およびIconSetの条件付き書式をエクスポートします（JavaScript経由のC++）。
linktitle: Excel を HTML に変換する際の DataBar、ColorScale、および IconSet 条件付き書式をエクスポート
type: docs
weight: 30
url: /ja/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

ExcelファイルをHTMLに変換するときにDataBar、ColorScale、IconSetの条件付き書式をエクスポートできます。この機能はMicrosoft Excelでは部分的にサポートされていますが、Aspose.Cells for JavaScriptは完全にサポートします。

{{% /alert %}}  

## **Excel を HTML に変換する際の DataBar、ColorScale、および IconSet 条件付き書式をエクスポート**  
[サンプルexcelファイル](5115558.xlsx)はDataBar、ColorScale、IconSet条件付き書式設定を含んでいます。指定されたリンクから[サンプルexcelファイル](5115558.xlsx)をダウンロードできます。  

![todo:image_alt_text](conversion_1.png)  

Aspose.Cellsの出力HTMLファイルを使用したDataBar、ColorScale、IconSet条件付き書式設定を示す次のスクリーンショットです。ご覧の通り、これは[サンプルexcelファイル](5115558.xlsx)とまったく同じように見えます。  

![todo:image_alt_text](conversion_2.png)  

### **サンプルコード**  
以下のサンプルコードは、サンプルのExcelファイルをHTMLに変換します（普通の[ExcelからHTMLへの変換](/cells/ja/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml)）。  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
