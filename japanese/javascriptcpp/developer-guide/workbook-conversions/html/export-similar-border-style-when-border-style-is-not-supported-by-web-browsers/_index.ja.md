---
title: Webブラウザがサポートしないボーダースタイルと同様のボーダースタイルをJavaScript経由のC++でエクスポート  
linktitle: Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする  
type: docs  
weight: 70  
url: /ja/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Webブラウザがサポートしないボーダーをエクスポートする方法を学びます。ExcelファイルをHTMLに変換する際にAspose.Cells for JavaScript via C++を使用します。  
---  

## **可能な使用シナリオ**  

Microsoft Excelは、一部の種類の点線の枠線をサポートしていますが、Webブラウザではサポートされていません。そのようなExcelファイルをHTMLに変換するとき、Aspose.Cells for JavaScript via C++はその枠線を除去します。ただし、Aspose.Cellsは[**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--)プロパティを使用してそのような枠線の表示もサポートできます。値を**true**に設定してください。そうすると、サポートされていない枠線もHTMLファイルにエクスポートされます。  

## **Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする**  

次のサンプルコードは、いくつかのサポートされていないボーダーを含むExcelファイル（[サンプルExcelファイル](64716806.xlsx)）を読み込み、スクリーンショットは次のとおりです。[**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--)プロパティの効果も示しています。  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options - Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
