---
title: C++経由でJavaScriptを使用してWorkbook内の未使用のスタイルを削除する
linktitle: ワークブック内の未使用のスタイルを削除する
type: docs
weight: 340
url: /ja/javascript-cpp/remove-unused-styles-inside-the-workbook/
description: C++経由でAspose.Cells for JavaScriptを使用してワークブックから未使用のスタイルを削除する方法を学習します。
---

{{% alert color="primary" %}}  
Excelファイルの未使用スタイルは容量を増やすだけでなく、PDFやHTMLなど他のフォーマットに変換する際にパフォーマンス問題も引き起こします。Aspose.Cellsは、[**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--)を提供し、ワークブック内の未使用スタイルをすべて削除します。  
{{% /alert %}}  

次のコードは [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--) の使用法を説明しています。このコードは提供されたリンクからダウンロード可能な [テンプレートExcelファイル](5115520.xlsx) を読み込みます。これは未使用のスタイル **AsposeStyle** を含んでいます; このスタイル及びすべての未使用スタイルは、コードの実行後に削除されます。  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Unused Styles</title>
    </head>
    <body>
        <h1>Remove Unused Styles Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Remove all unused styles inside the workbook
            workbook.removeUnusedStyles();

            // Save the modified workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Unused styles removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
