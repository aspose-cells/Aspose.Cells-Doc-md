---
title: JavaScriptとC++を使った異なるページに異なるヘッダーとフッターの設定方法
linktitle: 異なるページ用に異なるヘッダーとフッターの設定
type: docs
weight: 35
url: /ja/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: この記記事では、C++経由のAspose.Cells for JavaScriptを使用してExcelのページセットアップのヘッダーとフッターをプログラム的に設定するサンプルコードを提供します。最初のページ、奇数ページ、偶数ページのヘッダーとフッターの設定例も含まれています。
keywords: ExcelのヘッダーとフッターをJavaScriptとC++を使って最初のページ、奇数ページ、偶数ページに設定する方法
---

{{% alert color="primary" %}}

 MS Excelは、Excel 2007以降、最初のページ、奇数ページ、偶数ページの異なるヘッダーとフッターの設定をサポートしています。
 C++経由のAspose.Cells for JavaScriptはこれらの機能もサポートしています。

{{% /alert %}}

## **MS Excelで異なるヘッダーとフッターの設定**

**![異なるヘッダーとフッターの設定](difpage.png)**

1. **ページレイアウト > 印刷タイトル > ヘッダー/フッター**をクリックします。
1. **奇数ページと偶数ページを異なる設定にする**または**最初のページだけ異なる設定にする**を確認してください。
1. 異なるヘッダーとフッターを入力します。

## ** C++経由のAspose.Cells for JavaScriptを使用したヘッダーとフッターの設定の違い**

Aspose.CellsはExcelと同じように動作します。
 1. [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) と [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) のフラグを設定する 
1. 異なるヘッダーとフッターを入力します。
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
