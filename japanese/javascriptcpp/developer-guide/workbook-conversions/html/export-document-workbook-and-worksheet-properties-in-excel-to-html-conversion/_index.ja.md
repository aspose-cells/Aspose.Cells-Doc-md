---
title: JavaScript経由のC++によるExcelのドキュメント、ブック、ワークシートのプロパティをHTMLにエクスポート
linktitle: Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする
type: docs
weight: 50
url: /ja/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: ExcelをHTMLにエクスポートする際に、ドキュメント、ブック、ワークシートのプロパティをAspose.Cells for JavaScript via C++を使ってエクスポートする方法を学びます。
---

## **可能な使用シナリオ**  

Microsoft ExcelファイルをMicrosoft ExcelまたはAspose.Cells for JavaScript via C++を使ってHTMLにエクスポートすると、以下のスクリーンショットのようにさまざまな種類のドキュメント、ブック、ワークシートのプロパティもエクスポートされます。これらのプロパティをエクスポートしないようにするには、[**HtmlSaveOptions.exportDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportDocumentProperties--)、[**HtmlSaveOptions.exportWorkbookProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorkbookProperties--)、および[**HtmlSaveOptions.exportWorksheetProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetProperties--)を**false**に設定してください。これらのプロパティのデフォルト値は**true**です。次のスクリーンショットは、エクスポートされたHTMLにおけるこれらのプロパティの表示例です。  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Excelのドキュメント、ワークブック、ワークシートのプロパティをHTMLにエクスポートする**  

次のサンプルコードは、[サンプルExcelファイル](61767776.xlsx) を読み込み、ドキュメント、ワークブック、ワークシートのプロパティをエクスポートせずにHTMLに変換します（ [出力HTML](61767779.zip) 参照）。  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export HTML without Properties</title>
    </head>
    <body>
        <h1>Export Excel to HTML (without document/workbook/worksheet properties)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // We do not want to export document, workbook and worksheet properties
            options.exportDocumentProperties = false;
            options.exportWorkbookProperties = false;
            options.exportWorksheetProperties = false;

            // Export the Excel file to Html with Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
